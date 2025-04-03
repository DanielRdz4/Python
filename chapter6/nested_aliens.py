
aliens=[]

for alien in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow' }
    aliens.append(new_alien)

print(f'aliens created: {len(aliens)}')
print('\nalien caracteristics:')
for caracteristics in set(new_alien.values()):
    print(caracteristics)