from datetime import date, time

from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Sarah", "sarah@email.com")

dog = Pet("Buddy", "Dog", 4, "Walk twice daily")
cat = Pet("Luna", "Cat", 2, "Brush weekly")

owner.add_pet(dog)
owner.add_pet(cat)

# These tasks are intentionally created out of time order.
task1 = Task(
    task_name="Evening Walk",
    task_type="Walking",
    scheduled_date=date.today(),
    scheduled_time=time(18, 0),
    pet_name="Buddy",
    frequency="daily"
)

task2 = Task(
    task_name="Breakfast",
    task_type="Feeding",
    scheduled_date=date.today(),
    scheduled_time=time(8, 0),
    pet_name="Luna"
)

task3 = Task(
    task_name="Morning Walk",
    task_type="Walking",
    scheduled_date=date.today(),
    scheduled_time=time(10, 0),
    pet_name="Buddy"
)

dog.add_task(task1)
cat.add_task(task2)
dog.add_task(task3)

conflict_task1 = Task(
    task_name="Feed Buddy",
    task_type="Feeding",
    scheduled_date=date.today(),
    scheduled_time=time(14, 0),
    pet_name="Buddy"
)

conflict_task2 = Task(
    task_name="Brush Luna",
    task_type="Grooming",
    scheduled_date=date.today(),
    scheduled_time=time(14, 0),
    pet_name="Luna"
)

scheduler = Scheduler()

# Add them out of order.
scheduler.schedule_task(task1)
scheduler.schedule_task(task2)
scheduler.schedule_task(task3)

warning = scheduler.schedule_task(conflict_task1)
if warning:
    print(warning)

warning = scheduler.schedule_task(conflict_task2)
if warning:
    print(warning)

# Mark one task complete so status filtering can be tested.
task2.mark_complete()

new_task = task1.mark_complete()

if new_task:
    scheduler.schedule_task(new_task)

print("Tasks Sorted by Time")
print("--------------------")

for task in scheduler.sort_by_time():
    print(
        f"{task.scheduled_time.strftime('%I:%M %p')} | "
        f"{task.pet_name} | {task.task_name}"
    )


print("\nBuddy's Tasks")
print("-------------")

for task in scheduler.filter_by_pet("Buddy"):
    print(
        f"{task.scheduled_time.strftime('%I:%M %p')} | "
        f"{task.task_name}"
    )


print("\nIncomplete Tasks")
print("----------------")

for task in scheduler.filter_by_status(False):
    print(
        f"{task.pet_name} | {task.task_name}"
    )


print("\nCompleted Tasks")
print("---------------")

for task in scheduler.filter_by_status(True):
    print(
        f"{task.pet_name} | {task.task_name}"
    )