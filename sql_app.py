from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String(50), nullable=False)  
    email = Column(String(100), nullable=False) 
    password = Column(String(128), nullable=False) 
    img_address = Column(String(128), nullable=False) 

db_directory = r'E:\Bilal\PYTHON\ML\Unsupervised\Deep_Learning\Object_detection_API\Human_pose_tensorflow\Kivy_app\project_app\db_directory'
os.makedirs(db_directory, exist_ok=True)
DATABASE_URL = f"sqlite:///{db_directory}/users.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
