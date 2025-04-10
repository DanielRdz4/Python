prompt='This program will repeat anything that you type'
prompt+='\nIf you want to quit the progtam type quit'
print(prompt)

active = True
while active:
    message = input('I will repeat this: ')
    if message != 'quit':
        print(message)
    else:
        active = False