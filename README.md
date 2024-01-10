
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