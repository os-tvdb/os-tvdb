from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


#@app.get("/items/{item_id}")

### Authentication ###

# Login #
#@app.post("/login")

# Refresh Token - JWT #
@app.get("/refresh_token")
def refresh_token():
    return {"Refresh" : "token"}


### Episodes ###
@app.get("/episodes/{id}")
def episode_id():
    return {"Episde": "Blah"}

### Languages ###
@app.get("/languages")
def languages():
    return {"Languages": "Language List"}

@app.get("/languages/{id}")
def language_id():
    return {"Language": "English"}

### Movies - Do we want this?? ###
@app.get("/movies/{id}")
def movies():
    return {"movie": "name"}

### Search ###
@app.get("/search/series")
def series_search():
    return {"Series": "Whatever is searched for"}

@app.get("/search/series/params")
def series_search_param():
    return {"Series": "With params"}

### Series ###
@app.get("/series/{id}")
def series_id():
    return {"Series": "ID"}

@app.head("/series/{id}")
def series_id():
    return {"Series": "ID"}

@app.get("/series/{id}/actors")
def series_id_actors():
    return {"Series ID": "Actors list"}

@app.get("/series/{id}/episodes")
def series_id_episodes():
    return {"Series": "Episode List"}

@app.get("/series/{id}/episodes/query")
def series_episodes_query():
    return {"Series": "Episodes Query"}

@app.get("/series/{id}/episodes/query/params")
def series_episode_query_params():
    return {"Series": "Query Params"}

@app.get("/series/{id}/episodes/summary")
def series_summary():
    return {"Series": "Summary"}

@app.get("/series/{id}/filter")
def series_filter():
    return {"Series": "Filter"}

@app.get("/series/{id}/filter/params")
def series_filter_params():
    return {"Series": "Filter Params"}

@app.get("/series/{id}/images")
def series_id_image():
    return {"Series": "Image link"}

@app.get("/series/{id}/images/query")
def series_id_image_query():
    return {"image": "link"}

@app.get("/series/{id}/images/query/params")
def series_id_image_query_params():
    return {"Image": "Series image query"}

### Updates - Recently Updated ###

@app.get("/updated/query")
def updated_querys():
    return {"Updated": "Query"}
@app.get("/updated/query/params")
def updated_query_params():
    return {"Updated": "Query Params"}

### Users ###

@app.get("/user")
def user():
    return {"User": "ME!"}

@app.get("/user/favourites")
def user_favourites():
    return {"User": "Favourites"}

@app.delete("/user/favourites/{id}")

@app.put("/user/favourites/{id}")
    
@app.get("/user/ratings")
def user_rating():
    return {"User": "Rating"}

@app.get("/user/ratings/query")
def user_rating_query():
    return {"User": "Rating query"}

@app.get("/user/ratings/query/params")
def user_rating_query_param():
    return {"User": "rating query param"}

#@app.delete("/user/ratings/{itemType}/{itemId}")

#@app.put("/user/ratings/{itemType}/{itemId}/{itemRating}")