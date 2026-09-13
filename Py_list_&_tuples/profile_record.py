"""
User Profile Builder
---------------------
collect basic user details & store into list.

"""
name = input("Enter Your Name : ")
country = input("Enter Your Country : ")
city = input("Enter Your City : ")
age = int(input("Enter Your Age : "))
email = input("Enter Your E-mail : ")
hobbies = input("Enter Your Hobbies (separated by commas) : ")
hobbies_list = [hobby.strip() for hobby in hobbies.split(",")]
user_data = {
    "name" : name,
    "location" : {
        "country" : country,
        "city" : city
    },
    "personal_details" : {
        "age" : age,
        "email" : email
    },
    "hobbies" : hobbies_list
}

print("\n==========Profile Details==========")
print(f"Name : {user_data['name']}")
print(f"\nPersonal Details :")
print(f"Age : {user_data['personal_details']['age']}")
print(f"Email : {user_data['personal_details']['email']}")
print(f"Hobbies :")
print(f"{user_data['hobbies']}")