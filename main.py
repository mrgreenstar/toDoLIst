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
            print("\'show -all\' to show all tasks\n"
                "\'show -all -done\' to show only done tasks\n"
                "\'show {id}\' to show task with certain id\n"
                "\'mad {id}\' to mark task with certain id as done ")
        # To add task
        elif sys.argv[1] == "add" and sys.argv[2] == "-m" and sys.argv[3]:
            print("Add option")
            task = ToDoList(sys.argv[3])
            session.add(task)
            session.commit()
        elif sys.argv[1] == "show":
            if sys.argv[2] == "-all":
                # Show only done tasks
                if sys.argv[len(sys.argv) - 1] == "-done":
                    tasks = session.query(ToDoList).filter(ToDoList.is_done == True).all()
                    for task in tasks:
                        print(task)
                        print("".rjust(50, '-'))
                # Show all tasks
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
        # Mark task as done. MarkAsDone = MAD
        elif sys.argv[1] == "mad":
            task_id = int(sys.argv[2])
            task = session.query(ToDoList).filter(ToDoList.id == task_id).first()
            task.is_done = True
            session.commit()
        elif sys.argv[1] == "delete":
            if len(sys.argv) == 2:
                print("You have to give an id of task")
            else:
                task_id = int(sys.argv[2])
                session.query(ToDoList).filter(ToDoList.id == task_id).delete()
                session.commit()
        else:
            print("other option")
    except IndexError:
        print("Error")
