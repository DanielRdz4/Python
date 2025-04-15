
musicians = []
def build_person(first_name, last_name, age=None):
    """Return all info of a specific person"""
   
    if age:
        person={'first name': first_name, 'last name': last_name, 'age':age} 
    else:
        person={'first name': first_name, 'last name': last_name, }
    return person

musician=build_person('jimi','hendrix',)
print(musician)

