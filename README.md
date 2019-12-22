# OS-TVDB

This is a VERY EARLY attempt at building an Open Source clone of thetvdb.com.
Why? A lot of people (myself included) dont agree with the way thetvdb.com is being run...so as always, if you dont like something, do something about it. So here we are...


# Current State

This currently does _almost_ nothing.
I had added the ability to read from a SQLite database just for development purpose. 
At the moment all that will actually do is display all series that are in the DB (just one, id=1 series=family guy summary=whatever i pulled from thetvdb.com)
Use "DB Browser for SQLite" to view edit data if you want.

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