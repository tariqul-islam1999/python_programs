# Class to validate task priority
class TaskPriorityValidator:
    def is_valid_priority(self, priority):
        is_valid = priority in [1, 2, 3]  # Boolean: True if priority is 1, 2, or 3
        return is_valid

# Create validator instance
validator = TaskPriorityValidator()

# Get user input
task_priority = int(input("Enter task priority (1-3): "))

# Check and display result
result = validator.is_valid_priority(task_priority)
print(f"Priority {task_priority} is {'valid' if result else 'invalid'}")