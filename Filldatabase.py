from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from models import User, Base , Textbook

file_path = os.path.abspath(os.getcwd())+"/database.db"
engine = create_engine('sqlite:///{file_path}'.format(file_path=file_path), echo=True)
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)

session = DBSession()

text1 = Textbook(id = 2, title ='Discrete Math', author = 'Christopher Eppolito')
session.add(text1)
session.commit()
"""
text2 = Textbook(id = 3,title ='Ethics in computer Science', author = 'Weinshank Cape')
session.add(text2)
session.commit()"""



new_user = User(id = 1, name ='Korhan', fullname = 'Korhan Citlak', nickname = 'roblox')
new_user.textbooks.append(text1)
session.add(new_user)

#new_user.textbooks_have = relationship(
#  id = 2, title ='Discrete Math', author = 'Christopher Eppolito')
session.commit()
