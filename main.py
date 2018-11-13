'''
    Simple CRUD application.
    You can add/update/remove your everyday plans.
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import ToDoList, Base

if __name__ == '__main__':
    engine = create_engine('mysql://mrgreenstar:ThePassword@localhost:3306/todolist')
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    try:
        # If app was started without args or with arg '-h'
        if len(sys.argv) == 1 or sys.argv[1] == "-h":
            print("Help option")
        # To add task
        elif sys.argv[1] == "add" and sys.argv[2] == "-m" and sys.argv[3]:
            print("Add option")
            task = ToDoList(sys.argv[3])
            session.add(task)
            session.commit()
        else:
            print("other option")
    except IndexError:
        print("Error")
