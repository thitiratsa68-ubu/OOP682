from fastapi import FastAPI, Depends, HTTPException
from typing import List
from .models import Task, TaskCreate
from .repositories import SqlTaskRepository
from .services import TaskService
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from . import models_orm


models_orm.Base.metadata.create_all(bind=engine)

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()






# main.py

# เดิม:
# def get_task_service():
#     return TaskService(InMemoryTaskRepository())

# ใหม่ (ใช้ SQL):
def get_task_service(db: Session = Depends(get_db)):
    repo = SqlTaskRepository(db)
    return TaskService(repo)

# Dependency Provider


@app.get("/tasks", response_model=List[Task])
def read_tasks(service: TaskService = Depends(get_task_service)):
    return service.get_tasks()

@app.post("/tasks", response_model=Task)
def create_task(
    task: TaskCreate, 
    service: TaskService = Depends(get_task_service)
):
    return service.create_task(task)

@app.put("/tasks/{task_id}/complete", response_model=Task)
def mark_task_complete(
    task_id: int,
    service: TaskService = Depends(get_task_service)
):
    try:
        return service.mark_complete(task_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")
    


