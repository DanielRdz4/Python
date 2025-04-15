
def fortmated_name(first_name, last_name):
    """Gives format to the given name"""
    full_name=f"{first_name} {last_name}"
    return full_name.title()

musician =fortmated_name('jimmi', 'hendrix')

print(musician)