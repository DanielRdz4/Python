
alien_speed = input("alien speed: ")

alien_0={'X': 0,'Y':25,'speed':alien_speed}

if alien_0['speed'] == 'fast':
    X_increment = 3
elif alien_0['speed'] == 'medium':
    X_increment = 2
else:
    X_increment = 1

alien_0['X'] += X_increment

print(alien_0['X'])