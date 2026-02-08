
from .repositories import ITaskRepository
from .models import Task, TaskCreate
from fastapi import HTTPException

class TaskService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def get_tasks(self):
        return self.repo.get_all()

    def create_task(self, task_in: TaskCreate):
        # Business logic could go here
        existing_task = self.repo.get_by_title(task_in.title)
        if existing_task:
         raise HTTPException(
            status_code=400,
            detail="Task title already exists"
        )

    
        return self.repo.create(task_in)
        

        
    def mark_complete(self, task_id: int):
        task = self.repo.get_by_id(task_id)
        if not task:
            raise ValueError("Task not found")

        task.completed = True
        return self.repo.update(task)