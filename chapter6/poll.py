
employee_list = ['john','pepe','luis','jose','mateo','lucas','mario']
pending_poll=[]

employee_response={
    'john': 'no',
    'pepe': 'no',
    'luis': 'yes',
    'jose': 'yes',
}

for employee, response in employee_response.items():
    print(f"{employee}'s answer was {response}")

for employee in employee_list:
    if employee not in employee_response.keys():
        pending_poll.append(employee)

for employee in pending_poll:
    print(f"{employee}, please take the poll")