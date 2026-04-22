# DORM ROOM CHORE TRACKER (NO FUNCTIONS, NO isalpha)

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
