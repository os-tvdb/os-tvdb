from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Series(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, index=True)
    series_id = Column(Integer, index=True)
    series_name = Column(String, index=True)
    aliases = Column(String)
    season = Column(Integer)
    poster = Column(String)
    banner = Column(String)
    fanart = Column(String)
    status = Column(String)
    firstaired = Column(String)
    network = Column(String)
    networkid = Column(String)
    runtime = Column(Integer)
    language = Column(String)
    genre = Column(String)
    overview = Column(String)
    lastupdated = Column(String)
    airsdayofweek = Column(String)
    airstime = Column(String)
    rating = Column(String)
    imdbid = Column(String)
    zap2itid = Column(String)
    added = Column(String)
    addedby = Column(String)
    siterating = Column(String)
    siteratingcount = Column(String)
    slug = Column(String)