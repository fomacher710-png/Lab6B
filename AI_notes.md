Gemini 

create a command-line task-duration tracker. The user enters a task name and positive whole-number minutes for each task. A blank task name ends entry. The program displays total minutes and the task with the longest duration. Use only the Python standard library and keep the code beginner-readable.


## Improvement 3: Duplicate Task-Name Handling

- **Feature Added**: Handled duplicate task names during input.
- **Behavior**: When an entered task name matches an existing task (case-insensitive):
  - Prompts the user to choose between:
    - `[a]dd`: Accumulate the new duration onto the existing task's duration.
    - `[o]verwrite`: Replace the existing duration with the new duration.
    - `[c]ancel`: Abort entering the duplicate task and return to the task name prompt.
- **Rationale**: Prevents accidental duplicate entries and allows users to update or extend time logged for identical tasks without cluttering the final summary.
