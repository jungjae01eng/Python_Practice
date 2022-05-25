# @author Jungjae Lee
# Independent Study
# Created on May 23, 2022
# Sources: Python Tutorial by TechWorld with Nana on the Youtube channel
# --------------------------------------------------------------------------------


class Post:
    def __init__(self, message, author):
        self.message = message
        self.author = author

    def get_post_info(self):
        print(f"Post: {self.message} written by {self.author}")