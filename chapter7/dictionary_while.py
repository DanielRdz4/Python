
poll_answers ={}

poll_status= True
continue_poll = 'Y'

while poll_status:
    if continue_poll == 'Y':
        name= input('Name: ')
        answer = input('Favourite colour: ')
        poll_answers[name] = answer
    else:
        poll_status = False
        break
    continue_poll = input('Would you like to continue Y/N:')

for user_name, user_response in poll_answers.items():
    print(f"{user_name}'s favourite colour is: {user_response}")