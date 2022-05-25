# @author Jungjae Lee
# Independent Study
# Created on May 23, 2022
# Sources: Python Tutorial by TechWorld with Nana on the Youtube channel
# --------------------------------------------------------------------------------


class User:
    def __init__(self, user_email, user_name, user_password, current_job_title):   # Construct object from User class
        self.email = user_email
        self.name = user_name
        self.password = user_password
        self.current_job_title = current_job_title          # name of the variable can be the same

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"user {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}.")