from typing import List

from pydantic import BaseModel


class SeriesBase(BaseModel):
    series_id: int
    series_name: str
    aliases: str
    season: int
    poster: str
    banner: str
    fanart: str
    status: str
    firstaired: str
    network: str
    networkid: str
    runtime: int
    language: str
    genre: str
    overview: str
    lastupdated: str
    airsdayofweek: str
    airstime: str
    rating: str
    imdbid: str
    zap2itid: str
    added: str
    addedby: str
    siterating: str
    siteratingcount: str
    slug: str



class SeriesCreate(SeriesBase):
    pass


class Series(SeriesBase):
    id: int

    class Config:
        orm_mode = True

