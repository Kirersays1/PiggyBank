
![Logo](https://i.imgur.com/FkN7v31.png)


# PIGGY BANK

This application is a DEMO designed to track expenses and income through a web form built with Streamlit. Data is stored in a remote MongoDB database, and users can visualize their financial data through graphs on another tab.

Design and Patterns Used:
- [Three-tier Architecture](https://www.ibm.com/topics/three-tier-architecture)
- [MVC](https://codigofacilito.com/articulos/mvc-model-view-controller-explicado)
- [CRUD](https://developer.mozilla.org/es/docs/Glossary/CRUD)
- [Singleton](https://refactoring.guru/es/design-patterns/singleton)
- [Observer](https://refactoring.guru/design-patterns/observer)

Usage:
It's a DEMO for portfolio purposes, feel free to use it as u want.


## Installation

pip install -r requirements.txt




## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`db_url` Its your API key to MongoDB

`db_name` Name of your database

`collection_name` Name of your Data Collection


## Deployment

To deploy this project run

```bash
  streamlit run main.py
```


## Acknowledgements

 - [Original Project made by Sven Bo](https://github.com/Sven-Bo/streamlit-income-expense-tracker/tree/master)



## Authors

- [Ever Essaú Rodriguez Sandoval](https://github.com/Kirersays1)


## Feedback

If you have any feedback, please reach out at uselessmexicano@gmail.com


## License

MIT License

Copyright (c) [2024] [Ever Essaú Rodriguez Sandoval]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Lessons Learned

I didn't have experience deploying web apps in Python or using NOSQL Databases, i know it exists things like Django or Flask but for this project i wanted to try Streamlit. It was a great experience to  


## Contributing

Contributions are always welcome!

[ko-fi](https://ko-fi.com/essaurodriguez)

## Tech
**Client** :  Streamlit, Python

**Database** : MongoDB