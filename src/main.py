'''
Expenses and Incomes App with python, MongoDB and Streamlit
Made by Ever Essaú Rodriguez Sandoval
Based by the video and code of the youtube channel : Coding Is Fun /  Sven-Bo

https://www.youtube.com/watch?v=3egaMfE9388&t=734s
'''

import calendar
import locale
import src.database as db # local import

locale.setlocale(locale.LC_TIME, '') #get local language from user

from datetime import datetime
from streamlit_option_menu import option_menu  #pip install streamlit-option-menu

import streamlit as st  #pip install streamlit
import plotly.graph_objects as go  #pip install plotly

# ------------------------- SETTINGS ----------------------------------------
incomes = ["Salarios", "Blogs", "Otros"]
expenses = [
    "Renta", "Utilidades", "Viveres", "Carro", "Otros gastos", "Ahorro"
]
currency = "MXN"
page_title = "PiggyBank"
page_icon = "🐽"
layout = "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

with open("styles.css", "r") as css_file:
  st.markdown(f'<style>{css_file.read()}</style>', unsafe_allow_html=True)

st.title(page_title + " " + page_icon)
# ------------------ NAVIGATION MENU --------------------------------------
selected = option_menu(
    menu_title=None,
    options=["Data Entry", "Data Visualization" , "Generate Report"],
    icons=["🐽", "bar_chart",":play:"],  #emojipedia
    orientation="horizontal",
)

# --------Drop down values for periods -------------------------
years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])


# ---------INPUT & SAVE DATA---
if selected == "Data Entry":
  st.header(f"Entrada de datos en {currency}")
  with st.form("entry_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    col1.selectbox("Select Month", months, key="month")
    col2.selectbox("Select Year", years, key="year")
    "---"
    with st.expander("Ingreso"):
      for income in incomes:
        st.number_input(f"{income}:",
                        min_value=0,
                        format="%i",
                        step=10,
                        key=income)
    with st.expander("Expenses"):
      for expense in expenses:
        st.number_input(f"{expense}:",
                        min_value=0,
                        format="%i",
                        step=10,
                        key=expense)
    with st.expander("Comment"):
      comment = st.text_area("", placeholder="Enter a comment here...")
    "------------"
    submitted = st.form_submit_button("Save Data")
    if submitted:
      period = str(st.session_state["year"]) + "_" + str(
          st.session_state["month"])
      incomes = {income: st.session_state[income] for income in incomes}
      expenses = {expense: st.session_state[expense] for expense in expenses}
      
      st.write(f"incomes: {incomes}")
      st.write(f"expenses: {expenses}")
      db.insertPeriod(period,incomes,expenses,comment)
      st.success("Data Saved")

# ------------ Plot periods ---------------
if selected == "Data Visualization":
  st.header("Data Visualization")
  with st.form("saved_periods"):
    period = st.selectbox("Select Period: ", db.get_all_periods())
    submitted = st.form_submit_button("Plot Period")
    if submitted:
      period_data = db.get_period(period)
      st.write(period_data)

      incomes = period_data["incomes"]
      expenses = period_data["expenses"]
      comment = period_data["comment"]
      print(incomes)
      print(expenses)

      # Create metrics
      total_income = sum(incomes.values())
      total_expense = sum(expenses.values())
      remaining_budget = total_income - total_expense
      col1, col2, col3 = st.columns(3)
      col1.metric("Total Income", f"{total_income} {currency}")
      col2.metric("Total Expense", f"{total_expense} {currency}")
      col3.metric("Remaining Budget", f"{remaining_budget} {currency}")
      st.text(f"Comment: {comment}")

      # Create sankey chart
      label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
      source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
      target = [len(incomes)] * len(incomes) + [
          label.index(expense) for expense in expenses.keys()
      ]
      value = list(incomes.values()) + list(expenses.values())

      # Data to dict, dict to sankey
      link = dict(source=source, target=target, value=value)
      node = dict(label=label, pad=20, thickness=30, color="#E694FF")
      data = go.Sankey(link=link, node=node)

      # Plot it!
      fig = go.Figure(data)
      fig.update_layout(margin=dict(l=0, r=0, t=5, b=5))
      st.plotly_chart(fig, use_container_width=True)

# ---------- Create Report -----------------
#TODO CREATE AN APPI TO OBTAIN DATA
#TODO Create PDF download option
if selected == "Generate Report":
  st.header("Generate PDF report about period")