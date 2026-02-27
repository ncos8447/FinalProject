from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from helpers import load_tasks, save_tasks

app = FastAPI()

#pydantic models

#full task model for returning tasks

class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = True

#model for creating task

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

#root endpoint

@app.get("/")
def root():
    return {"message": "FastAPI Task Manager is running"}

#get tasks

@app.get("/tasks")
def get_tasks(completed: bool | None = None):
    tasks = load_tasks()
    if completed is not None:
        tasks = [task for task in tasks if task["completed"] == completed]
    return tasks

#get single task

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

#create new task

@app.post("/tasks")
def create_task(task: TaskCreate):
    tasks = load_tasks()

    if tasks:
        new_id = tasks[-1]["id"] + 1
    else:
        new_id = 1

    new_task = {
        "id": new_id,
        "title": task.title,
        "description": task.description,
        "completed": False,
    }

    tasks.append(new_task)
    save_tasks(tasks)
    return new_task

#update tasks
@app.get("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskCreate):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["description"] = updated_task.description
            save_tasks(tasks)
            return task

    raise HTTPException(status_code=404, detail="Task not found")

#delete ONE task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = load_tasks()

    new_tasks = [task for task in tasks if task["id"] == task_id]

    if len(new_tasks) == len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")

    save_tasks(new_tasks)
    return {"message": "Task deleted successfully"}

#delete ALL tasks
@app.delete("/tasks/{task_id}")
def delete_all_tasks():
    save_tasks([])
    return {"message": "Tasks deleted successfully"}

#task stats

@app.get("/tasks/stats")
def task_stats():
    tasks = load_tasks()

    total = len(tasks)
    completed = len([task for task in tasks if task["completed"]])
    pending = total - completed

    if total > 0:
        percentage = (completed / total) * 100
    else:
        percentage = 0

    return {
        "total_tasks": total,
        "pending_tasks": pending,
        "completed_tasks": completed,
        "completion_percentage": percentage
    }





