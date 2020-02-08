from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os

file_path = os.path.abspath(os.getcwd())+"/database.db"
engine = create_engine('sqlite:///{file_path}'.format(file_path=file_path), echo=True)

Base = declarative_base()

textbook_user_list = Table('books and users', Base.metadata,
    Column('left_id', Integer, ForeignKey('users.id')),
    Column('right_id', Integer, ForeignKey('textbooks.id'))
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    textbooks_have = relationship("Textbook", secondary=textbook_user_list, back_populates="users")
    textbooks_wanted = relationship("Textbook", back_populates="wanted_textbooks")
    def __init__(self, uname):
        pass


class Textbook(Base):
    __tablename__ = 'textbooks'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    owners = relationship("User", secondary=textbook_user_list, back_populates="textbooks")
