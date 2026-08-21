"""

Simple Bug Tracker
------------------
This program will find if the bug exist in the list otherwise bug id will added
in the list

"""

class BugTracker:
    def __init__(self):
        self.bug_list = [] 

    def add_and_check_bug(self, bug_id):
        if bug_id in self.bug_list:
            return True
        else:
            self.bug_list.append(bug_id)
            return False

tracker = BugTracker()

while True:
    bug_id = input("Enter bug ID: ")
    is_existed = tracker.add_and_check_bug(bug_id)

    if is_existed:
        print(f"Bug {bug_id} exist")
        break
    else:
        print(f"Bug {bug_id} was added")

    print(f"Bug list: {tracker.bug_list}")