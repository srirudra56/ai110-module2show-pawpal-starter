from dataclasses import dataclass, field
from datetime import date, time
from typing import List


@dataclass
class Task:
    task_name: str
    task_type: str
    scheduled_date: date
    scheduled_time: time
    pet_name: str
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    pet_type: str
    age: int
    care_needs: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a care task for this pet."""
        self.tasks.append(task)

    def view_tasks(self) -> List[Task]:
        """Return all tasks assigned to this pet."""
        return self.tasks


class Owner:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's list."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from the owner's list."""
        if pet in self.pets:
            self.pets.remove(pet)

    def view_pets(self) -> List[Pet]:
        """Return all pets owned by this owner."""
        return self.pets


class Scheduler:
    def __init__(self) -> None:
        self.scheduled_tasks: List[Task] = []

    def schedule_task(self, task: Task) -> None:
        """Add a task to the schedule."""
        self.scheduled_tasks.append(task)

    def remove_task(self, task: Task) -> None:
        """Remove a task from the schedule."""
        if task in self.scheduled_tasks:
            self.scheduled_tasks.remove(task)

    def view_todays_tasks(self) -> List[Task]:
        """Return tasks scheduled for today."""
        today = date.today()
        return [
            task
            for task in self.scheduled_tasks
            if task.scheduled_date == today
        ]