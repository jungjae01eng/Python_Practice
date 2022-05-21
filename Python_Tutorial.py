# @author Jungjae Lee
# Independent Study
# Created on May 20, 2022
# Sources: "Python Tutorial" by TechWorld with Nana on Youtube
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