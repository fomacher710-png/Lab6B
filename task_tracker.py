def main():
    tasks = []

    print("--- Task Duration Tracker ---")
    print("Enter tasks and their duration in minutes.")
    print("Press Enter on an empty task name when finished.\n")

    while True:
        # Prompt for task name
        task_name = input("Enter task name: ").strip()

        # Blank task name ends entry
        if not task_name:
            break

        # Check for duplicate task name
        existing_task = next((t for t in tasks if t["name"].lower() == task_name.lower()), None)
        action = None
        if existing_task:
            print(f" Task '{existing_task['name']}' already exists (Current duration: {existing_task['duration']} min).")
            while True:
                choice = input(" Choose action - [a]dd time, [o]verwrite duration, or [c]ancel: ").strip().lower()
                if choice in ['a', 'add']:
                    action = 'add'
                    break
                elif choice in ['o', 'overwrite']:
                    action = 'overwrite'
                    break
                elif choice in ['c', 'cancel']:
                    action = 'cancel'
                    break
                else:
                    print("  Invalid choice. Please enter 'a' to add, 'o' to overwrite, or 'c' to cancel.")
            
            if action == 'cancel':
                print(" Entry cancelled.\n")
                continue

        # Prompt for positive whole-number minutes with validation
        while True:
            duration_input = input(f"Enter duration for '{task_name}' (in minutes): ").strip()

            # 1. Reject blank / empty input
            if not duration_input:
                print(" Invalid input: Duration cannot be blank.")
                continue

            # 2. Reject non-numeric input
            try:
                duration = int(duration_input)
            except ValueError:
                print(" Invalid input: Duration must be a numeric whole number.")
                continue

            # 3. Reject zero and negative values
            if duration <= 0:
                print(" Invalid input: Duration must be greater than zero.")
                continue

            # Valid duration accepted
            if existing_task:
                if action == 'add':
                    existing_task['duration'] += duration
                    print(f" Added {duration} min to '{existing_task['name']}'. New total: {existing_task['duration']} min.")
                elif action == 'overwrite':
                    existing_task['duration'] = duration
                    print(f" Updated duration for '{existing_task['name']}' to {duration} min.")
            else:
                tasks.append({"name": task_name, "duration": duration})
            break

        print()  # Empty line for better readability

    # Display results
    if not tasks:
        print("\nNo tasks were entered.")
        return

    # Calculate total minutes
    total_minutes = sum(task["duration"] for task in tasks)

    # Find the task with the longest duration
    longest_task = max(tasks, key=lambda x: x["duration"])

    print("\n" + "=" * 30)
    print("SUMMARY")
    print("=" * 30)
    
    # Itemized task breakdown
    print("Tasks Entered:")
    for index, task in enumerate(tasks, start=1):
        print(f"  {index}. {task['name']}: {task['duration']} minute(s)")
    
    print("-" * 30)
    print(f"Total time spent: {total_minutes} minute(s)")
    print(f"Longest task: {longest_task['name']} ({longest_task['duration']} minute(s))")


if __name__ == "__main__":
    main()