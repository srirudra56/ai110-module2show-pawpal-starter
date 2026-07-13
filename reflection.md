# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.

- What classes did you include, and what responsibilities did you assign to each?
-Initial UML Design contains Owner, Pet, Task, and Scheduler 
-The owner class stores the owners name, email address, and list of pets. Responsible for adding pets, removing pets, and displaying owner's pets. 
-The pet class stores the name, type, age, care needs, and assigned tasks. It is responsible for adding care tasks and displaying the tasks associated with the pet. 
-The task class represents feeding, walking, grooming, or attending a vet appointment. It stores task name, task type, scheduled date, scheduled time, and completion status. Includes marking a task as complete
-The scheduler class manages the scheduled tasks. It is responsible for scheduling tasks, removing tasks, and displaying the tasks scheduled for the current day. 
-The relationships in the design show that one owner can have multiple pets, each pet can have multiple tasks, and the scheduler can manage multiple tasks 

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
After reviewing the class skeleton, I realized there was no pet name for the particular task and time so I added an extra string for that in the task class. I also updated the UML diagram.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
My scheduler considers the task date, scheduled time, pet name, completion status, and recurrence frequency. It sorts tasks by time so the earliest tasks appear first, filters tasks by pet or completion status, and checks whether two tasks are scheduled for the exact same date and time. It also creates the next occurrence for daily and weekly recurring tasks.

I decided that date and time were the most important constraints because pet care tasks need to happen at the correct time. Completion status was also important because it helps the owner distinguish finished tasks from tasks that still need attention. Pet name matters because an owner may manage multiple pets, while recurrence frequency helps automate repeated care activities.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff in my scheduler is that conflict detection only checks whether two tasks have the exact same date and time. This keeps the algorithm simple and easy to understand, but it does not detect tasks whose time ranges overlap. For example, a 30-minute walk at 2:00 PM and a feeding task at 2:15 PM would not be identified as a conflict. I chose the simpler approach because the current Task class does not store task duration, and exact-time matching is enough for the basic version of the app.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI throughout the project to help brainstorm the initial system design, create a UML diagram, generate class skeletons, debug Python errors, and implement algorithms such as sorting, filtering, recurring tasks, and conflict detection. AI also helped me write automated tests, improve my README, and explain Python concepts that I did not fully understand. The most helpful prompts were specific questions such as "How should the Scheduler retrieve tasks?" or "Why is this test failing?" because they provided focused explanations instead of large amounts of unnecessary code.
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

One example where I did not accept an AI suggestion as-is was the recurring task implementation. AI suggested moving the recurring logic into the Scheduler class, but I chose to keep the recurring behavior inside the Task.mark_complete() method because it fit my class design better and kept responsibilities clear. I verified the implementation by running main.py and my automated tests to confirm that recurring tasks were created correctly.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
I tested several important behaviors, including marking tasks as complete, adding tasks to pets, sorting tasks by scheduled time, filtering tasks by pet and completion status, generating recurring daily tasks, and detecting scheduling conflicts. These tests were important because they verified the core functionality of the scheduler and ensured that the main features worked as expected

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
I am highly confident that my scheduler works correctly because the automated tests passed and the demo program produced the expected results. If I had more time, I would test additional edge cases such as overlapping task durations, larger numbers of pets and tasks, invalid user input, and more complex recurring schedules.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

The part I am most satisfied with is building the scheduler logic. I successfully implemented sorting, filtering, recurring tasks, and conflict detection while keeping the classes organized and easy to understand.
**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I had another iteration, I would improve the Streamlit interface by allowing users to edit or delete tasks, choose custom recurring schedules, and display the schedule with more interactive filtering and searching options.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
One important thing I learned is that AI is most useful as a development assistant rather than a replacement for my own decisions. I still needed to understand the code, evaluate AI suggestions, and choose the implementation that best fit my project's design.