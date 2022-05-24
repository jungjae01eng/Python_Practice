# @author Jungjae Lee
# Independent Study
# Created on May 22, 2022
# Last Updated on May 23, 2022
# Sources: Python Tutorial by TechWorld with Nana on the Youtube channel
# --------------------------------------------------------------------------------


def days_to_units11_1(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"56: {num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"56: {num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "56: unsupported unit"


def validate_and_execute11_1(days_and_unit_dictionary):
    try:
        user_input_number11_1 = int(days_and_unit_dictionary["days"])
        if user_input_number11_1 > 0:
            calculated_value11_1 = days_to_units11_1(user_input_number11_1, days_and_unit_dictionary["unit"])
            print(calculated_value11_1)
        elif user_input_number11_1 == 0:
            print("55: You entered a 0; please enter a valid positive number")
        else:
            print("55: You entered a negative value, so no conversion possible")

    except ValueError:
        print("55: Your input is not a number")


user_input_message = "53: Enter the number of days and conversion unit: "
