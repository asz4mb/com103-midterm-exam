This program is a **console-based Dorm Room Chore Tracker** that helps organize, assign, and monitor household responsibilities among roommates while ensuring clean and structured user input.

It begins by asking for the **room monitor’s name**, applying strict validation rules to ensure the input is meaningful. The name must contain only letters and spaces, cannot be purely numeric, must be longer than one character, and cannot include irregular spacing or symbols. This ensures consistent and readable identification of the person in charge.

Next, the program collects the **room number**, allowing flexible formats such as “205-B” while preventing invalid inputs like special characters or purely alphabetical entries. This step ensures that each room is properly labeled without ambiguity.

After gathering basic details, the program displays a **predefined list of chores** along with their expected frequency (e.g., daily, weekly). The user is then prompted to assign up to four chores. Each chore assignment includes:

* Selecting a chore from the list (with duplicate prevention)
* Entering a roommate’s name (validated similarly to the monitor’s name)
* Indicating whether the task has been completed (“yes” or “no”)

The program keeps track of which chores have been assigned and counts how many have been completed.

Once all assignments are done, it calculates a **completion rate** based on the number of finished tasks relative to the total assigned. Based on this percentage, it determines an overall **room status**, such as:

* *“ROOM IS SPOTLESS!”* for full completion
* *“ALMOST THERE!”* for partial progress
* *“NEEDS CATCHING UP!”* for low completion

Finally, the program generates a **formatted weekly chore report**, displaying:

* Room number and monitor name
* A detailed list of assigned chores with assigned roommates and completion status
* Total completed tasks and overall completion rate
* The final room status

Overall, this code demonstrates structured input validation, use of loops and conditionals, data tracking with lists and sets, and formatted output to create a simple but effective task management system for shared living spaces.
