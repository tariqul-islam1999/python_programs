# Class to manage test case statuses
class StatusCounter:
    def __init__(self):
        self.status_list = []  # List to store statuses
    def count_status(self, status):
        is_valid = status.lower() in ["pass", "fail"]  # Boolean: True if valid status
        if is_valid:
            self.status_list.append(status.lower())  # Add valid status to list
        return is_valid, self.status_list.count(status.lower())  # Return validity and count

# Create counter instance
counter = StatusCounter()

# Get user input
status = input("Enter test case status (pass/fail): ")

# Count and display result
valid, count = counter.count_status(status)
print(f"Status {status} is {'valid' if valid else 'invalid'}, count: {count}")
print(f"Status list: {counter.status_list}")