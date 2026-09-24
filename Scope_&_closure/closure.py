"""
Python Closure
---------------
basic operations of closure & it's uses

"""

def make_multiplier(factor):
    def multiply(number):
        return number*factor
    return multiply

val1 = make_multiplier(2)
val2 = make_multiplier(3)

print(val1(5))
print(val2(5))

#----------------------------------------------------------------

def parent_function(name,coins):
    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print(f"{name} has {coins} coins left")
        elif coins == 1:
            print(f"{name} has {coins} coin left")
        else:
            print(f"{name} is out of coins")
    return play_game

user1 = parent_function("Tariqul",5)
user2 = parent_function("Faisal",3)

user1()
user1()
user1()
user2()
user2()
user1()
user2()