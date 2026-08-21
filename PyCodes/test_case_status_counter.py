"""

Test Case Status Counter
-------------------------
Checks how many test cases passes or failed & takes only valid values (pass/fail) from user

"""
class StatusCounter:
    def __init__(self):
        self.pass_count = 0
        self.fail_count = 0

    def add_status(self, status):
        status = status.lower()

        if status == "pass":
            self.pass_count += 1
            return True
        elif status == "fail":
            self.fail_count += 1
            return True
        else:
            return False

counter = StatusCounter()
status = input("Enter test case status (pass/fail): ")
is_valid = counter.add_status(status)

if is_valid:
    print(f"Status - {status} is valid")
    print(f"Total Pass : {counter.pass_count}, Total Fail: {counter.fail_count}")
else:
    print(f"Status {status} is invalid!")