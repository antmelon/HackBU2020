from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os

file_path = os.path.abspath(os.getcwd())+"/database.db"
engine = create_engine('sqlite:///{file_path}'.format(file_path=file_path), echo=True)

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __init__(self, uname):
        pass


class Textbook(Base):
    __tablename__ = 'textbooks'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    owner = relationship("User", back_populates="owned_textbooks")
