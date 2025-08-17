# Class to manage bug tracker
class BugTracker:
    def __init__(self):
        self.bug_list = []  # List to store bug IDs
    def add_and_check_bug(self, bug_id):
        is_present = bug_id in self.bug_list  # Boolean: True if bug_id exists
        self.bug_list.append(bug_id)  # Add bug_id to list
        return is_present

# Create tracker instance
tracker = BugTracker()

# Get user input
bug_id = input("Enter bug ID: ")

# Add bug and check if it existed
result = tracker.add_and_check_bug(bug_id)
print(f"Bug {bug_id} {'existed' if result else 'was added'}")
print(f"Bug list: {tracker.bug_list}")