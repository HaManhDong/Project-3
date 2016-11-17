
# from ElearningSystem.models import models
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os.path

BASE = declarative_base()
CURRENT_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
# print('xxxxxxxxxxxxx')
# class Role(BASE):

class User(BASE):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    username = Column(String)
    password = Column(String)
    account = Column(String)
    email = Column(String)
    def __repr__(self):
        return self.id

ENGINE = create_engine('sqlite:///'+CURRENT_FOLDER_PATH+'/database/user.db', echo=True)
BASE.metadata.create_all(ENGINE)
SESSION = sessionmaker(bind=ENGINE)

class UserService:

    def __init__(self):
        self.session = SESSION()

    def addUser(self, username, password, account_name, email):
        user = User(username=username, password=password, account=account_name, email=email)
        self.session.add(user)
        self.session.commit()
        return True

    def searchUser(self, username):
        for user in self.session.query(User.username):
            if user==username:
                return True
            else:
                return False
    def closeSession(self):
        self.session.close()