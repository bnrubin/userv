from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Fact(db.Model):
    __tablename__ = 'fact'

    id = Column(Integer, primary_key=True)
    author = Column(String(100))
    name = Column(String(20))
    added = Column(DateTime)
    value = Column(String(200))
    popularity = Column(Integer)

    def __repr__(self):
        return '<Fact(name=%s)>' % self.name

