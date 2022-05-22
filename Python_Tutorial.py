# @author Jungjae Lee
# Independent Study
# Created on May 20, 2022
# Last Updated on May 21, 2022
# Sources: Python Tutorial by TechWorld with Nana on the Youtube channel
# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
# --------------------------------- (1) Variables --------------------------------
calculation_to_hours = 24
name_of_unit = "hours"

print("1: 50 days are " + str(50 * 24) + " hours")
print(f"2: 50 days are {50 * calculation_to_hours} hours")
print(f"3: 50 days are {50 * calculation_to_hours} {name_of_unit}")


# --------------------------------------------------------------------------------
# --------------------------------- (2) Functions --------------------------------
def days_to_units2_1():
    print(f"4: 50 days are {50 * calculation_to_hours} {name_of_unit}")


def days_to_units2_2(num_of_days):
    print(f"5: {num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}")


def days_to_units2_3(num_of_days, custom_message):
    print(f"6: {num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}")
    print("7: " + custom_message)


days_to_units2_1()
days_to_units2_2(50)
days_to_units2_3(50, "Awesome!")


# --------------------------------------------------------------------------------
# ----------------------------------- (3) Scope ----------------------------------
def scope_check3_1():
    print("8: " + name_of_unit)     # Global variables
    # print(num_of_days)            # Internal variables: Inside another function - Does not exist in this function


def scope_check3_2(num_of_days):
    my_var1 = "11: variable inside function"
    print("9: " + name_of_unit)
    print(num_of_days)
    print(my_var1)


scope_check3_1()
scope_check3_2(50)


# --------------------------------------------------------------------------------
# -------------------------------- (4) User Input --------------------------------
def days_to_units4_1(num_of_days):
    return f"14: {num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"


def days_to_units4_2(num_of_days):
    return f"16: {num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"


user_input4_1 = input("12: Enter the number of days you want to convert to hours: ")
print("13: " + user_input4_1)
my_var4_1 = days_to_units4_1(50)
print(my_var4_1)

user_input4_2 = input("15: Enter the number of days you want to convert to hours: ")
user_input_number4_2 = int(user_input4_2)
calculated_value4_2 = days_to_units4_2(user_input_number4_2)
print(calculated_value4_2)


# --------------------------------------------------------------------------------
# --------------- (5) Conditionals (if/else) and Boolean Data Type ---------------
def days_to_units5_1(num_of_days):
    if num_of_days > 0:
        return f"18: {num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"
    elif num_of_days == 0:
        return "18: You entered a 0; please enter a valid positive number"
    else:
        return "18: You entered a negative value, so no conversion possible"


def days_to_units5_2(num_of_days):
    if num_of_days > 0:
        return f"20: {num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"
    elif num_of_days == 0:
        return "20: You entered a 0; please enter a valid positive number"


def validate_and_execute5_2():
    if user_input5_2.isdigit():  # validation - only if the user input is a number
        user_input_number5_2 = int(user_input5_2)
        calculated_value5_2 = days_to_units5_2(user_input_number5_2)
        print(calculated_value5_2)
    else:
        print("20: Your input is not a number")


def days_to_units5_3(num_of_days):
    return f"22: {num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"


def validate_and_execute5_3():
    if user_input5_3.isdigit():  # validation - only if the user input is a number

        user_input_number5_3 = int(user_input5_3)
        if user_input_number5_3 > 0:
            calculated_value5_3 = days_to_units5_3(user_input_number5_3)
            print(calculated_value5_3)
        elif user_input_number5_3 == 0:
            print("22: You entered a 0; please enter a valid positive number")
    else:
        print("22: Your input is not a number")


user_input5_1 = input("17: Enter the number of days you want to convert to hours: ")
calculated_value5_1 = days_to_units5_1(int(user_input5_1))
print(calculated_value5_1)

user_input5_2 = input("19: Enter the number of days you want to convert to hours: ")
validate_and_execute5_2()

user_input5_3 = input("21: Enter the number of days you want to convert to hours: ")
validate_and_execute5_3()


# --------------------------------------------------------------------------------
# ---------------------- (6) Error Handling with Try/Except ----------------------
def days_to_units6_1(num_of_days):
    return f"24: {num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"


def validate_and_execute6_1():
    try:
        user_input_number6_1 = int(user_input6_1)
        if user_input_number6_1 > 0:
            calculated_value6_1 = days_to_units6_1(user_input_number6_1)
            print(calculated_value6_1)
        elif user_input_number6_1 == 0:
            print("24: You entered a 0; please enter a valid positive number")
        else:
            print("24: You entered a negative value, so no conversion possible")

    except ValueError:
        print("24: Your input is not a number")


user_input6_1 = input("23: Enter the number of days you want to convert to hours: ")
validate_and_execute6_1()


# --------------------------------------------------------------------------------
# -------------------------------- (7) While Loops -------------------------------
def days_to_units7_1(num_of_days):
    return f"26: {num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"


def validate_and_execute7_1():
    try:
        user_input_number7_1 = int(user_input7_1)
        if user_input_number7_1 > 0:
            calculated_value7_1 = days_to_units7_1(user_input_number7_1)
            print(calculated_value7_1)
        elif user_input_number7_1 == 0:
            print("26: You entered a 0; please enter a valid positive number")
        else:
            print("26: You entered a negative value, so no conversion possible")

    except ValueError:
        print("26: Your input is not a number")


user_input7_1 = ""
while user_input7_1 != "exit":
    user_input7_1 = input("25: Enter the number of days you want to convert to hours: ")
    print("Please type exit to exit from the code if you wish to stop the loop")
    validate_and_execute7_1()


# --------------------------------------------------------------------------------
# ---------------------------- (8) Lists and For Loops ---------------------------
my_list8_1 = ["January", "February", "March"]
print(my_list8_1[1])

my_list8_1.append("April")
print(my_list8_1)


def days_to_units8_1(num_of_days):
    return f"32: {num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"


def validate_and_execute8_1():
    try:
        user_input_number8_1 = int(num_of_days8_1)
        if user_input_number8_1 > 0:
            calculated_value8_1 = days_to_units8_1(user_input_number8_1)
            print(calculated_value8_1)
        elif user_input_number8_1 == 0:
            print("32: You entered a 0; please enter a valid positive number")
        else:
            print("32: You entered a negative value, so no conversion possible")

    except ValueError:
        print("32: Your input is not a number")


user_input8_1 = ""
while user_input8_1 != "exit":
    user_input8_1 = input("30: Enter the number of days as a comma-separated list you want to convert to hours: ")
    print("31: Please type exit to exit from the code if you wish to stop the loop")
    print(user_input8_1.split(", "))

    for num_of_days8_1 in user_input8_1.split(", "):   # split function return list of input values
        validate_and_execute8_1()


# --------------------------------------------------------------------------------
# ----------------------------------- (9) Sets -----------------------------------
my_set9_1 = {"January", "February", "March"}   # CANNOT access the element individually
for element in my_set9_1:
    print(element)

my_set9_1.add("April")
print(my_set9_1)
my_set9_1.remove("January")
print(my_set9_1)


def days_to_units9_1(num_of_days):
    return f"44: {num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"


def validate_and_execute9_1():
    try:
        user_input_number9_1 = int(num_of_days9_1)
        if user_input_number9_1 > 0:
            calculated_value9_1 = days_to_units9_1(user_input_number9_1)
            print(calculated_value9_1)
        elif user_input_number9_1 == 0:
            print("44: You entered a 0; please enter a valid positive number")
        else:
            print("44: You entered a negative value, so no conversion possible")

    except ValueError:
        print("44: Your input is not a number")


user_input9_1 = ""
while user_input9_1 != "exit":
    user_input9_1 = input("38: Enter the number of days as a comma-separated list you want to convert to hours: ")
    print("39: Please type exit to exit from the code if you wish to stop the loop")
    list_of_days = user_input9_1.split(", ")
    print(list_of_days)
    print(set(list_of_days))
    print(type(list_of_days))
    print(type(set(list_of_days)))

    for num_of_days9_1 in set(user_input9_1.split(", ")):   # set does NOT allow duplicate values
        validate_and_execute9_1()


# List vs Sets
# Sets do not have an order, in which if you run the code, the order of the sets will be different each time


# --------------------------------------------------------------------------------
# --------------------------- (10) Dictionary Data Type --------------------------
my_list10_1 = ["20", "30"]
print(my_list10_1[1])

my_dictionary = {"days": 20, "unit": "hours", "message": "all good"}
print(my_dictionary["unit"])


def days_to_units10_1(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"49: {num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"49: {num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def validate_and_execute10_1():
    try:
        user_input_number10_1 = int(days_and_unit_dictionary["days"])
        if user_input_number10_1 > 0:
            calculated_value10_1 = days_to_units10_1(user_input_number10_1, days_and_unit_dictionary["unit"])
            print(calculated_value10_1)
        elif user_input_number10_1 == 0:
            print("49: You entered a 0; please enter a valid positive number")
        else:
            print("49: You entered a negative value, so no conversion possible")

    except ValueError:
        print("49: Your input is not a number")


user_input10_1 = ""
while user_input10_1 != "exit":
    user_input10_1 = input("47: Enter the number of days and conversion unit: ")
    print("48: Please type exit to exit from the code if you wish to stop the loop")
    days_and_unit = user_input10_1.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_and_execute10_1()


# --------------------------------------------------------------------------------
# ------------------------- Standalone Built-In Functions ------------------------
# print()       # Prints to the standard output device
# input()       # Asks user for input
# set()         # Returns a new set
# int()         # Converts value into an integer number


# --------------------------------------------------------------------------------
# ---------------------------------- Data Types ----------------------------------
# message = "enter some value"                      # string
# days = 20                                         # integer
# price = 9.99                                      # float
# valid_number = True                               # boolean: Check conditions whether it is true or not
# list_of_days = [20, 40, 20, 100]                  # list
# list_of_months = ["January", February", "March"]  # list in string
# set_of_days = {20, 45, 100}                       # sets: similar to list but does not allow duplicated value
# days_and_ unit = {"days": 10, "unit": "hours"}    # dictionary
