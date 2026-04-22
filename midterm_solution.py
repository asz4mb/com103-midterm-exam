# DORM ROOM CHORE TRACKER 
# Step 1: Get room monitor name
while True:
    monitor_name = input("Room monitor name: ").strip()

    if not monitor_name:
        print("Enter a valid monitor name")
        continue

    if monitor_name.isdigit():
        print("It cannot be only numbers")
        continue

    if len(monitor_name) == 1:
        print("Name must be more than one letter")
        continue

    if "  " in monitor_name:
        print("No multiple spaces allowed")
        continue

    # Manual check: letters and spaces only
    valid = True
    for ch in monitor_name:
        if not (('a' <= ch.lower() <= 'z') or ch == ' '):
            valid = False
            break

    if not valid:
        print("Name must contain letters only")
        continue

    parts = monitor_name.split()
    if all(len(p) == 1 for p in parts) and len(parts) > 1:
        print("Enter proper words, not just letters")
        continue

    break


# Step 2: Get room number (allows 205-B but not letters only or special chars)
while True:
    room_number = input("Room number: ").strip()

    if not room_number:
        print("Enter a room number")
        continue

    has_digit = False
    valid = True

    for ch in room_number:
        if '0' <= ch <= '9':
            has_digit = True
        elif ('a' <= ch.lower() <= 'z') or ch == '-':
            continue
        else:
            valid = False
            break

    if not valid:
        print("It should not contain special characters")
        continue

    if not has_digit:
        print("It should not be letters only")
        continue

    break


# Step 3: Display chores
chores = [
    ("Sweeping / Mopping", "Daily"),
    ("Dishwashing", "After meals"),
    ("Taking Out Trash", "Every other day"),
    ("Cleaning Bathroom", "Weekly"),
    ("Buying Groceries", "Weekly")
]

print("\n==========================================")
print("   DORM ROOM -- CHORE LIST")
print("==========================================")

for i in range(len(chores)):
    print(str(i + 1) + ". " + chores[i][0] + " [" + chores[i][1] + "]")

print("==========================================\n")


# Step 4: Assign chores
assigned_chores = []
used_numbers = set()
completed = 0

assignment = 1
while assignment <= 4:
    print("--- CHORE " + str(assignment) + " ---")

    while True:
        choice = input("Chore number (0 to skip): ")

        if not choice or not choice.isdigit() or len(choice) != 1:
            print("Enter a single digit (0–5)")
            continue

        number = int(choice)

        if number < 0 or number > 5:
            print("Must be between 0 and 5")
        elif number != 0 and number in used_numbers:
            print("Chore already assigned")
        else:
            break

    if number == 0:
        assignment += 1
        continue

    used_numbers.add(number)

    # Roommate name (no isalpha)
    while True:
        roommate = input("Roommate name: ").strip()

        if not roommate:
            print("Name cannot be empty")
            continue

        valid = True
        for ch in roommate:
            if not (('a' <= ch.lower() <= 'z') or ch == ' '):
                valid = False
                break

        if not valid:
            print("Letters only please")
            continue

        break

    # Status
    while True:
        status = input("Completed? (yes/no): ").lower()

        if status == "yes" or status == "no":
            break
        print("Enter yes or no")

    if status == "yes":
        completed += 1

    assigned_chores.append((
        chores[number - 1][0],
        chores[number - 1][1],
        roommate,
        status.upper()
    ))

    assignment += 1


# Step 5: Calculate
total = len(assigned_chores)

if total > 0:
    rate = (completed / total) * 100
else:
    rate = 0


if rate == 100:
    room_status = "ROOM IS SPOTLESS!"
elif rate >= 50:
    room_status = "ALMOST THERE!"
else:
    room_status = "NEEDS CATCHING UP!"


# Step 6: Report
print("\n=============================================")
print("     ROOM " + room_number + " -- WEEKLY CHORE REPORT")
print("=============================================")
print("Room Monitor : " + monitor_name)
print("---------------------------------------------")

count = 1
for chore in assigned_chores:
    print("[" + str(count) + "] " + chore[0] + " [" + chore[1] + "]")
    print("    Roommate : " + chore[2])
    print("    Status   : " + chore[3])
    print()
    count += 1

print("---------------------------------------------")
print("Completed      : " + str(completed) + " out of " + str(total))
print("Completion Rate: " + str(rate) + "%")
print("Room Status    : " + room_status)
print("=============================================")
