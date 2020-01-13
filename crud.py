from sqlalchemy.orm import Session

from . import models, schemas

def get_series_by_id(db: Session, series_id: int):
    return db.query(models.Series).filter(models.Series.series_id == series_id).first()

def get_series(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Series).offset(skip).limit(limit).all()


def create_series(db: Session, item: schemas.SeriesCreate):
    db_item = models.Series(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item