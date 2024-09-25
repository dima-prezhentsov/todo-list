
from enum import Enum


class TaskStatus(Enum):
    NOT_STARTED = 1
    IN_PROGRESS = 2
    DONE = 3

class Task:
    __id = 0
    
    def __init__(self, description: str):
      self.description = description
      self.status = TaskStatus.NOT_STARTED
      Task.__id += 1
      self.id = Task.__id

    


class Todo:
    def __init__(self):
      self.tasks: list[Task] = []
      
      
    def add_task(self, description: str):
        newTask = Task(description=description)
        self.tasks.append(newTask)
        return newTask
    
    def remove_task(self, task_id: int):
        for index, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[index]
        return self.tasks
    
    def update_status(self, task_id: int, status: TaskStatus):
        for index, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks[index].status = status
                return
        raise Exception("Task Not Found")
    
    def view_tasks(self):
        print("--------------- TASKS ---------------")
        count: int = 0
        for task in self.tasks:
            count += 1
            print("Task: ", count, " id: ", task.id, " description: ", task.description, " status: ", task.status)
            