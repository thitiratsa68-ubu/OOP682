from fastapi import APIRouter, HTTPException
from .repositories import InMemoryTaskRepository
from .services import TaskService
from .models import Task, TaskCreate

router = APIRouter()

repo = InMemoryTaskRepository()
service = TaskService(repo)


@router.get("/tasks", response_model=list[Task])
def get_tasks():
    return service.get_tasks()


@router.post("/tasks", response_model=Task)
def create_task(task_in: TaskCreate):
    return service.create_task(task_in)


@router.put("/tasks/{task_id}/complete", response_model=Task)
def mark_task_complete(task_id: int):
    try:
        return service.mark_complete(task_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")
