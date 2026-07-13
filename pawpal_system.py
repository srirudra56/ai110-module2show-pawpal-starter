from dataclasses import dataclass, field
from datetime import date, time, timedelta
from typing import List


@dataclass
class Task:
    task_name: str
    task_type: str
    scheduled_date: date
    scheduled_time: time
    pet_name: str
    frequency: str = "once"   # once, daily, weekly
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

        if self.frequency == "daily":
           return Task(
             task_name=self.task_name,
             task_type=self.task_type,
             scheduled_date=self.scheduled_date + timedelta(days=1),
             scheduled_time=self.scheduled_time,
             pet_name=self.pet_name,
             frequency="daily"
            )

        if self.frequency == "weekly":
           return Task(
             task_name=self.task_name,
             task_type=self.task_type,
             scheduled_date=self.scheduled_date + timedelta(days=7),
             scheduled_time=self.scheduled_time,
             pet_name=self.pet_name,
             frequency="weekly"
            )

        return None
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

    def schedule_task(self, task: Task):
        """Add a task to the schedule."""
        warning = self.check_conflict(task)
        self.scheduled_tasks.append(task)
        return warning

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

    def sort_by_time(self) -> List[Task]:
        """Return scheduled tasks sorted from earliest to latest."""
        return sorted(
            self.scheduled_tasks,
            key=lambda task: task.scheduled_time
        )

    def filter_by_pet(self, pet_name: str) -> List[Task]:
        """Return tasks assigned to a specific pet."""
        return [
            task
            for task in self.scheduled_tasks
            if task.pet_name.lower() == pet_name.lower()
        ]

    def filter_by_status(self, completed: bool) -> List[Task]:
        """Return tasks filtered by completion status."""
        return [
            task
            for task in self.scheduled_tasks
            if task.completed == completed
        ]
    
    def check_conflict(self, new_task: Task) -> str | None:
        """Return a warning if another task is scheduled at the same date and time."""
        for existing_task in self.scheduled_tasks:
            same_date = existing_task.scheduled_date == new_task.scheduled_date
            same_time = existing_task.scheduled_time == new_task.scheduled_time

            if same_date and same_time:
               return (
                 f"Warning: {new_task.task_name} for {new_task.pet_name} "
                 f"conflicts with {existing_task.task_name} for "
                 f"{existing_task.pet_name} at "
                 f"{new_task.scheduled_time.strftime('%I:%M %p')}."
                )

        return None