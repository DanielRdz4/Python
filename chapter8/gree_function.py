def greet_user(username):
    """Display a simple greeting"""
    print(f"The user's name is {username.title()}")

username=input("Name?: ")
greet_user(username)