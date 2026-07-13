from datetime import date, time

from pawpal_system import Owner, Pet, Task, Scheduler


# Create an owner
owner = Owner("Sarah", "sarah@email.com")

# Create pets
dog = Pet("Buddy", "Dog", 4, "Walk twice daily")
cat = Pet("Luna", "Cat", 2, "Brush weekly")

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# Create tasks
task1 = Task(
    "Morning Walk",
    "Walk",
    date.today(),
    time(8, 0),
    "Buddy"
)

task2 = Task(
    "Feed Breakfast",
    "Feeding",
    date.today(),
    time(8, 30),
    "Buddy"
)

task3 = Task(
    "Brush Fur",
    "Grooming",
    date.today(),
    time(6, 0),
    "Luna"
)

# Add tasks to pets
dog.add_task(task1)
dog.add_task(task2)
cat.add_task(task3)

# Create scheduler
scheduler = Scheduler()

# Schedule tasks
scheduler.schedule_task(task1)
scheduler.schedule_task(task2)
scheduler.schedule_task(task3)

# Print today's schedule
print("Today's Schedule")
print("-----------------")

for task in scheduler.view_todays_tasks():
    print(
        f"{task.scheduled_time.strftime('%I:%M %p')} | "
        f"{task.pet_name} | "
        f"{task.task_name} ({task.task_type})"
    )