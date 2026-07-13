from datetime import date, time

from pawpal_system import Pet, Task


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