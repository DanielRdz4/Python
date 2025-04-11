
prompt='This program will repeat anything that you type'
prompt+='\nIf you want to quit the progtam type quit'
print(prompt)

message=""
while message != 'quit':
    message = input('I will repeat this: ')
    if message != 'quit':
        print(message)
