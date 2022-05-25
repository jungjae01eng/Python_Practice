# @author Jungjae Lee
# Independent Study
# Created on May 24, 2022
# Sources: Python Tutorial by TechWorld with Nana on the Youtube channel
# --------------------------------------------------------------------------------


from Project03_User import User
from Project03_Post import Post


app_user_one = User("nn@nn.com", "Jungjae Lee", "pwd1", "Student")
app_user_one.get_user_info()

app_user_one.change_job_title("Engineer")
app_user_one.get_user_info()

app_user_two = User("jj@nn.com", "James Bond", "pwd2", "Agent")
app_user_two.get_user_info()


new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()