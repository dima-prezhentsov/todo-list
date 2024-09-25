
from todo import *

def main():
    todo_list = Todo()
    
    todo_list.add_task(description="First task")
    todo_list.add_task(description="Second task")
    todo_list.add_task(description="Third task")
    
    todo_list.view_tasks()
    
    todo_list.remove_task(task_id=1)
    
    todo_list.view_tasks()
    
    todo_list.update_status(task_id=2, status=TaskStatus.IN_PROGRESS)
    
    todo_list.view_tasks()


if __name__ == "__main__":
    main()