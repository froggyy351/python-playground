from fastapi import FastAPI

class Task:
    next_task_id = 1
    
    def __init__(self, task_id: int, title: str, isDone: bool):
        self.task_id = self.next_task_id
        Task.next_task_id += 1
        self.title = title
        self.isDone = False

