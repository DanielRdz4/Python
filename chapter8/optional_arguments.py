
def fortmated_name(first_name, last_name, middle_name=""):
    """Gives format to the given name"""
    if middle_name:
        full_name =f'{first_name} {middle_name} {last_name}'
    else:
        full_name=f"{first_name} {last_name}"
    return full_name.title()

musician =fortmated_name('jimmi', 'hendrix')

print(musician)