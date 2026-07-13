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

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
