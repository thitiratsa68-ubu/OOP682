from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session

from .models import Task, TaskCreate
from . import models_orm


class ITaskRepository(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, task: TaskCreate):
        pass

    @abstractmethod
    def get_by_id(self, task_id: int):
        pass

    @abstractmethod
    def update(self, task):
        pass


class SqlTaskRepository(ITaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(models_orm.Task).all()

    def create(self, task_in: TaskCreate):
        db_task = models_orm.Task(**task_in.dict())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def get_by_id(self, task_id: int):
        return (
            self.db.query(models_orm.Task)
            .filter(models_orm.Task.id == task_id)
            .first()
        )

    def update(self, task):
        self.db.commit()
        self.db.refresh(task)
        return task
    def get_by_title(self, title: str):
     return self.db.query(models_orm.Task).filter(models_orm.Task.title == title).first()

    
