from fastapi import FastAPI, Depends, HTTPException
# Taskクラス
class Task:
    next_task_id = 1
    
    def __init__(self, title: str):
        self.task_id = self.next_task_id
        Task.next_task_id += 1
        self.title = title
        self.isDone = False
        
app = FastAPI()
tasks: dict[int, Task] = {1: Task("洗濯物"), 2: Task("掃除機")}

# Depends
def task_db():
    return tasks

# GET（単）
@app.get("/todo/{task_id}")
def get_todo_byId(task_id: int, db: dict = Depends(task_db)):
    if task_id not in db:
        raise HTTPException(status_code=404, detail=f"id:{task_id}のタスクは見つかりません")
    return db[task_id]

# GET（複）
@app.get("/")
def get_todos(db: dict = Depends(task_db)):
    return db

# POST


# PUT


# DELETE


