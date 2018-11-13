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
    print(sys.argv)
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
        elif sys.argv[1] == "show":
            if sys.argv[2] == "-all":
                if sys.argv[3] == "mad":
                    tasks = session.query(ToDoList).filter(ToDoList.is_done == True).all()
                    for task in tasks:
                        print(task)
                        print("".rjust(50, '-'))
                else:
                    tasks = session.query(ToDoList).all()
                    for task in tasks:
                        print(task)
                        print("".rjust(50, '-'))
            # Get task with certain id
            if sys.argv[2].isdigit():
                task_id = abs(int(sys.argv[2]))
                task = session.query(ToDoList).filter(ToDoList.id == task_id).first()
                if task is None:
                    print("Can't find task with this id. Please try again")
                else:
                    print(task)
            elif sys.argv[2].isalpha():
                print("Wrong id")
            # Get all done tasks
            if sys.argv[2] == "-done":
                tasks = session.query(ToDoList).filter(ToDoList.is_done == 1).all()
                for task in tasks:
                    print(task)
        # Mark task as done. MarkAsDone = MAD
        elif sys.argv[1] == "mad":
            task_id = int(sys.argv[2])
            task = session.query(ToDoList).filter(ToDoList.id == task_id).first()
            task.is_done = True
            session.commit()
        else:
            print("other option")
    except IndexError:
        print("Error")
