task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

Level = 0
match priority:
    case "high":
        Level = 1
    case "medium":
        Level = 2
    case "low":
        Level = 3

if time_bound == "yes" and Level != 0:
    print(
        f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
    )
elif time_bound == "no" and Level != 0:
    print(
        f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."
    )
