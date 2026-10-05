def main():
    tasks = []

    print("--- Task Duration Tracker ---")
    print("Enter tasks and their duration in minutes.")

    while True:
        # Display main option menu
        print("\nOptions:")
        print("  1. Add or update a task")
        print("  2. Remove a recorded task")
        print("  3. Finish and view summary")
        
        choice = input("Choose an option (1-3): ").strip()

        # Option 3: Finish task entry
        if choice == "3":
            break

        # Option 2: Remove a recorded task
        elif choice == "2":
            if not tasks:
                print(" No tasks recorded yet to remove.")
                continue

            print("\nCurrent Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"  {idx}. {task['name']} ({task['duration']} min)")

            remove_input = input("Enter the task number to remove (or press Enter to cancel): ").strip()
            if not remove_input:
                print(" Selection cancelled.")
                continue

            if remove_input.isdigit():
                remove_idx = int(remove_input) - 1
                if 0 <= remove_idx < len(tasks):
                    removed_task = tasks.pop(remove_idx)
                    print(f" Removed '{removed_task['name']}' ({removed_task['duration']} min).")
                else:
                    print(" Invalid task number.")
            else:
                print(" Invalid input: Please enter a numeric task number.")

        # Option 1: Add or update a task
        elif choice == "1":
            task_name = input("\nEnter task name: ").strip()

            if not task_name:
                print(" Task name cannot be empty.")
                continue

            # Check for duplicate task name
            existing_task = next((t for t in tasks if t["name"].lower() == task_name.lower()), None)
            action = None
            if existing_task:
                print(f" Task '{existing_task['name']}' already exists (Current duration: {existing_task['duration']} min).")
                while True:
                    act_choice = input(" Choose action - [a]dd time, [o]verwrite duration, or [c]ancel: ").strip().lower()
                    if act_choice in ['a', 'add']:
                        action = 'add'
                        break
                    elif act_choice in ['o', 'overwrite']:
                        action = 'overwrite'
                        break
                    elif act_choice in ['c', 'cancel']:
                        action = 'cancel'
                        break
                    else:
                        print("  Invalid choice. Please enter 'a' to add, 'o' to overwrite, or 'c' to cancel.")
                
                if action == 'cancel':
                    print(" Entry cancelled.")
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

        else:
            print(" Invalid option. Please enter 1, 2, or 3.")

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