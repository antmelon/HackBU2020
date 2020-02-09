from models import User, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
file_path = os.path.abspath(os.getcwd())+"/database.db"
engine = create_engine('sqlite:///{file_path}'.format(file_path=file_path), echo=True)
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
session.query(User).all()
us = session.query(User).first()
print(us.textbooks_have)
