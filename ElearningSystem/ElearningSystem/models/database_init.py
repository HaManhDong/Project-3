
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os.path

BASE = declarative_base()
CURRENT_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
ENGINE = create_engine('sqlite:///'+CURRENT_FOLDER_PATH+'/database/user.db', echo=True)
BASE.metadata.create_all(ENGINE)
SESSION = sessionmaker(bind=ENGINE)