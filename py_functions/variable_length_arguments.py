"""
Variable Length Arguments
-------------------------
basic structure of (*args,**kwargs) & it's operations.

"""
# Bill Calculator Using (*args)

def calculator (*prices):
    total = 0
    for price in prices:
        total += price
    return total

bill1 = calculator(100,200,300)
bill2 = calculator(220,540,840,700)

print(f"1st Bill Total : {bill1}")
print(f"2nd Bill Total : {bill2}")

# User Profile Using (**kwargs)

def build_profile(**details):
    print("-------- User Profile ----------")
    for key,val in details.items():
        print(f"{key} : {val}")
    
build_profile(name = "Tariqul", age = 26 , city = "Dhaka")
build_profile(name = "Faisal", phn_number = "+880 1870000000" , email = "faisal@example.com")

# Event Registration Using (*args,**kwargs)

def registration(*attendees,**event_info):
    print("Attendees : ")
    for name in attendees:
        print(f" {name}")

    print(f"\nEvent Details : ")
    for key,val in event_info.items():
        print(f"{key} : {val}")

registration("Faisal","Karim","Rasel",location="Dhaka", time="6PM")
registration("Tariqul","Islam",location="Cumilla")