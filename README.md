# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

## Sample Output

```text
Today's Schedule
-----------------
08:00 AM | Buddy | Morning Walk (Walk)
08:30 AM | Buddy | Feed Breakfast (Feeding)
06:00 PM | Luna | Brush Fur (Grooming)
```

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

Used:

python3 -m pytest

The tests verify:

-marking a task as complete
-adding a task to a pet
-sorting tasks in chronological order
-creating the next occurrence of a daily recurring task
-detecting scheduling conflicts

Confidence:

5 stars
I have a high level of confidence in PawPal+ because the automated tests verify the system's main scheduling behaviors and all tests pass successfully.

```
# Paste your pytest output here
```
========================================= test session starts =========================================
platform darwin -- Python 3.12.5, pytest-9.0.3, pluggy-1.6.0
rootdir: /Users/srirudrapatlori/ai110-module2show-pawpal-starter
plugins: anyio-4.13.0
collected 5 items                                                                                     

test/test_pawpal.py .....                                                                       [100%]

========================================== 5 passed in 0.02s ==========================================

## 📐 Smarter Scheduling


| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | Scheduler.sort_by_time() | sorts tasks by earliest to latest using each task's scheduled time |
| Filtering | Scheduler.filter_by_pet() and Scheduler.filter_by_status() | Filters tasks by pet names or by completed/incomplete status |
| Conflict handling | Scheduler.check_conflict() and Scheduler.schedule_task() | Checks for tasks within the same date and time and returns a warning message |
| Recurring tasks | Task.mark_complete() | Creates the next occurence for daily tasks after 1 day and weekly tasks after 7 days |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
