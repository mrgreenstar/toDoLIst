'''
    Simple CRUD application.
    You can add/update/remove your everyday plans.
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Entity.ToDoListEntity import ToDoList

if __name__ == '__main__':
    engine = create_engine('mysql://mrgreenstar:ThePassword@localhost:3306/todolist')
    Session = sessionmaker(bind=engine)
    session = Session()
    args = sys.argv[1:]
    
    