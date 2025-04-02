
alien_attributes = ['color','points']
alien_dictionary={}

for attribute in alien_attributes:
    alien_dictionary[attribute]=input(f'alien {attribute}: ')
print(f'the alien color is {alien_dictionary['color']}')
print(f'The alien value is {alien_dictionary['points']}')
