# @author Jungjae Lee
# Independent Study
# Created on May 22, 2022
# Sources: Python Tutorial by TechWorld with Nana on the Youtube channel
# --------------------------------------------------------------------------------


"""
Exercise:
    a. Accept user input of goal and a deadline
    b. Print back How much time remains until that deadline
"""


from datetime import datetime

user_input = input("Enter your goal with a deadline separated by a colon: (Ex: Learn Python:08.05.2022) ")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]


deadline_date = datetime.datetime.strptime(deadline, "%m.%d.%Y")    # If we use %m.%d.%y, it will be 08.05.22
today_date = datetime.datetime.today()

time_remaining = deadline_date - today_date


hours_till = int(time_remaining.total_seconds() / 60 / 60)


print(today_date)
print(deadline_date)

print(f"Time remaining for your goal: {goal} is {time_remaining}")
print(f"Time remaining for your goal in days: {goal} is {time_remaining.days} days")
print(f"Time remaining for your goal in days: {goal} is {hours_till} hours")