from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ToDoList(Base):
    __tablename__ = 'todolist'
    id = Column(Integer, primary_key = True)
    created_at = Column(DateTime, default=datetime.now)
    description = Column(String(200))
    finished_at = Column(DateTime, onupdate=datetime.now)
    is_done = Column(Boolean, default=False)
    
    def __init__(self, description):
        self.description = description
        self.created_at = datetime.now()
        self.is_done = False
    
    def __repr__(self):
        return "<ToDoList(description:{}, created_at: {})>".format(
            self.description, self.created_at)

    def __str__(self):
        view = "Created at: {}\nDescriprion: {}\nIs done: {}"
        return view.format(self.created_at, self.description, self.is_done)