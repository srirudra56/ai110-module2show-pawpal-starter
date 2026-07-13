from datetime import date, time, timedelta

from pawpal_system import Pet, Scheduler, Task


def test_mark_complete():
    task = Task(
        "Morning Walk",
        "Walk",
        date.today(),
        time(8, 0),
        "Buddy"
    )

    task.mark_complete()

    assert task.completed is True


def test_add_task():
    pet = Pet(
        "Buddy",
        "Dog",
        4,
        "Walk twice daily"
    )

    task = Task(
        "Morning Walk",
        "Walk",
        date.today(),
        time(8, 0),
        "Buddy"
    )

    pet.add_task(task)

    assert len(pet.tasks) == 1

def test_sort_by_time():
    scheduler = Scheduler()

    late_task = Task(
        "Evening Walk",
        "Walking",
        date.today(),
        time(18, 0),
        "Buddy"
    )

    early_task = Task(
        "Breakfast",
        "Feeding",
        date.today(),
        time(8, 0),
        "Luna"
    )

    middle_task = Task(
        "Morning Walk",
        "Walking",
        date.today(),
        time(10, 0),
        "Buddy"
    )

    scheduler.schedule_task(late_task)
    scheduler.schedule_task(early_task)
    scheduler.schedule_task(middle_task)

    sorted_tasks = scheduler.sort_by_time()

    assert sorted_tasks[0] == early_task
    assert sorted_tasks[1] == middle_task
    assert sorted_tasks[2] == late_task


def test_daily_task_creates_next_day_task():
    daily_task = Task(
        "Morning Walk",
        "Walking",
        date.today(),
        time(8, 0),
        "Buddy",
        frequency="daily"
    )

    new_task = daily_task.mark_complete()

    assert daily_task.completed is True
    assert new_task is not None
    assert new_task.scheduled_date == date.today() + timedelta(days=1)
    assert new_task.frequency == "daily"
    assert new_task.completed is False


def test_conflict_detection():
    scheduler = Scheduler()

    first_task = Task(
        "Feed Buddy",
        "Feeding",
        date.today(),
        time(14, 0),
        "Buddy"
    )

    second_task = Task(
        "Brush Luna",
        "Grooming",
        date.today(),
        time(14, 0),
        "Luna"
    )

    first_warning = scheduler.schedule_task(first_task)
    second_warning = scheduler.schedule_task(second_task)

    assert first_warning is None
    assert second_warning is not None
    assert "Warning" in second_warning