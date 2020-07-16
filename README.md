<h1 align="center">FastApi E-commerce Applications Endpoints 👋</h1>

## Introduction

> FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

>The key features that I like in FastApi are:
><ul>
<li>Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.</li>
<li>Fast to code: Increase the speed to develop features by about 200% to 300%. *</li>
<li>Fewer bugs: Reduce about 40% of human (developer) induced errors. *</li>
<li>Easy: Designed to be easy to use and learn. Less time reading docs.</li>
<li>Robust: Get production-ready code. With automatic interactive documentation.</li>
<li>Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.</li>
</ul>

>This Repository is aimed at helping those who are working on e-commerce applications.

 ## A few assumptions:
<ol>
<li>You have a good understanding of Python Language</li>
<li>The project you want to use this codebase for uses an SQL Database</li>
<li>You have an understanding of sqlalchemy as an ORM
</ol>

>The Repository contains 5 main files namely:
<ol>
<li>main.py</li>
This file is the entry point for the application. It contains the main routes and redirects all user requested routes to their respective functions.
<li>crud.py</li>
This file contains the main functions that interact with the database, it is basically where the business logic happens.
<li>models.py</li>
This file is similar to the one in Django. In this file is where we define our database tables.
<li>schema.py</li>
This file contains the data schemas for our application.
<li>database.py</li>
This file contains our database connection string.
</ol>

# Endpoints
>A basic E-commerce application has features such as Log in/ Register/ Cart functionalities/ Payment Functionalities/ Admin CRUD capabilities among other functionalities.

>We have the following API's
<ul>
<b><li>/register</li>
<li>/login</li>
<li>/get_user/username</li>
<li>/add_item</li>
<li>/get_item/id</li>
<li>/del_item/id</li>
<li>/add_to_cart/username</li>
<li>/del_cart_item/id</li>
<li>/payment</li>
<li>/callback</li></b>
</ul>

>TO NOTE: The MPESA module is not yet complete.I will be updating it in a few days



## Code Samples

> Just to show you how the flow works here is the working example of the <b>get_item/id</b> endpoint.

<b>main.py</b>
```
@app.get("/get_item/{id}", response_model=schemas.ItemAInfo)
def get_user(id, db:Session = Depends(get_db)):
    db_item = crud.get_item_by_id(db, id=id)
    if db_item is None:
        raise HTTPException(status_code=400, detail="No item found")
    return db_item
```

The above piece of code handles the endpoint and calls the function <b>get_item_by_id</b> in the crud.py file for further processing.

<b>crud.py</b>
```
def get_item_by_id(db: Session, id: int):
    return db.query(models.ItemInfo).filter(models.ItemInfo.id == id).first()
```
The above piece of code handles the <b>get_item_by_id call</b> and queries the <b>DB</b> for an item with the <b>id passed in the parameter</b>


## Install

```sh
git clone 
pip install -re requirements.txt
cd sql_app
```

## Usage

```sh
uvicorn main:app --reload
```

## Author

👤 **Collins H. Munene**

* Website: [My portfolio](https://collinsmunene.github.io/collinshillary.github.io/)
* Twitter: [@Hillary Collins](https://twitter.com/HillaryCollns)
* Github: [@Collins Munene](https://github.com/CollinsMunene)
* LinkedIn: [@Collins Munene](https://linkedin.com/in/collins-hillary-munene)

## Show your support

Give a ⭐️ if this project helped you!
