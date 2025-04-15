
usernames=['dani','fani','juan']

def greet_user(names):
    """Función que saluda a todos los usuarios de la lista usernames"""
    for name in names:
        print(f"Hi! {name.title()}")

greet_user(usernames)