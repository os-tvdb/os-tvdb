from typing import List

from pydantic import BaseModel


class SeriesBase(BaseModel):
    series: str
    summary: str = None


class SeriesCreate(SeriesBase):
    pass


class Series(SeriesBase):
    id: int

    class Config:
        orm_mode = True

