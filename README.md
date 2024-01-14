
# Getting started

## Requirements¶
 - Python 3.8+

FastAPI stands on the shoulders of giants:

 - Starlette for the web parts.
 - Pydantic for the data parts.

## Run server

This examples need the pipenv shell activated to work -> run: $ pipenv shell (to activate the env)

Then cd into the example you want to run

Then run the server

```console
$ uvicorn main:app --reload 
```
<!-- --reload is to restart the server every time something changes  -->

## Interactive API docs

### docs

http://127.0.0.1:8000/docs.

You will see the automatic interactive API documentation (provided by Swagger UI):

### redocs

http://127.0.0.1:8000/redoc.

You will see the alternative automatic documentation (provided by ReDoc):

## Tutorial

 - Basic: https://fastapi.tiangolo.com/tutorial/
 - Advanced: 


### Optional Dependencies
 #### Used by Pydantic:

 - email_validator - for email validation.
 - pydantic-settings - for settings management.
 - pydantic-extra-types - for extra types to be used with Pydantic.

#### Used by Starlette:

 - httpx - Required if you want to use the TestClient.
 - jinja2 - Required if you want to use the default template configuration.
 - python-multipart - Required if you want to support form "parsing", with request.form().
 - itsdangerous - Required for SessionMiddleware support.
 - pyyaml - Required for Starlette's SchemaGenerator support (you probably don't need it with FastAPI).
 - ujson - Required if you want to use UJSONResponse.

#### Used by FastAPI / Starlette:

 - uvicorn - for the server that loads and serves your application.
 - orjson - Required if you want to use ORJSONResponse.
You can install all of these with pip install "fastapi[all]".

## Models

 - SQLAlchemy uses the term "model" to refer to these classes and instances that interact with the database.

 - But Pydantic also uses the term "model" to refer to something different, the data validation, conversion, and documentation classes and instances.

## Docker

Containerize a Python application (https://docs.docker.com/language/python/containerize/)