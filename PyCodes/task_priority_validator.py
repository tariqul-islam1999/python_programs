"""

Simple Task Priority Validator
-------------------------------
Chekcs the task's priority for process

"""
class TaskPriorityValidator:
    def is_valid_priority(self, priority):
        is_valid = priority in [1, 2, 3]
        return is_valid

validator = TaskPriorityValidator()
task_name = input("Enter Task Name : ")
task_priority = int(input("Set task's priority (1-3): "))
result = validator.is_valid_priority(task_priority)
print(f"Task - {task_name} | Priority - {task_priority} | {'Valid' if result else 'invalid'}")