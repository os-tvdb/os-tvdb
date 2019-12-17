# OS-TVDB

This is a VERY EARLY attempt at building an Open Source clone of tvdb.com.
Why? A lot of people (myself included) dont agree with the way tvdb.com is being run...so as always, if you dont like something, do something about it. So here we are...


# Current State

This is completely useless as it is. It does nothing apart from return json that is statically set in main.py
All i have done is layed out the endpoints the same as tvdb.com so this _could_ be a drop in replacement. 

## What am i using
This is currently being written in python using FastAPI (https://fastapi.tiangolo.com)

## Whats the plan?

As of now, i think the best way forward is to create a somewhat usable API.
A web UI can then be written in any language that calls the API.


## Test it yourself?

You will need to install the FastAPI python module `pip install fastapi[all]`.
Then, once you have pulled down the repo you can start the develoment server with `uvicorn main:app --reload`

You should then be able to get to `/` on `127.0.0.1:8000`
You can also get to the swagger UI on `127.0.0.1:8000/docs`

Read more at https://fastapi.tiangolo.com