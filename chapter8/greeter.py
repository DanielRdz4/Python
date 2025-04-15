
def get_format_name(f_name, l_name, middle_name=""):
    """Función que da formato a los nombres"""
    if middle_name:
        name = f"{f_name.title()} {middle_name.title()} {l_name.title()}"
    else:
        name = f"{f_name.title()} {l_name.title()}"
    return name

#User input
status= True
first_time= True
while status:
    if first_time == True:  
        first_name = input("First name: ")
        middle_name = input("Middle name (If necesesary): ")
        last_name = input("Last name: ")
        formated_name = get_format_name(first_name,last_name,middle_name,)
        print(formated_name)
        first_time = False

    else:
        continue_running = input("Would you like to continue: Y/N: ")
        if continue_running == "Y":
            first_name = input("First name: ")
            middle_name = input("Middle name (If necesesary): ")
            last_name = input("Last name: ")
            formated_name=get_format_name(first_name,middle_name,last_name)
            print(formated_name)
        else:
            status=False

    