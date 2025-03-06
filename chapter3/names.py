
names = ['fany','dani','juan']

print(names)

names[2] = 'jesus'

print(names)

names.append('nova')
names.append('omar')

print(names)

names.insert(0,'pepe')
print(names)

del names[0]
print(names)

names.pop(2)
print(names)

names.remove('nova')
print(names)

me_cae_mal = 'omar'
names.remove(me_cae_mal)

print(f"\n Quito a {me_cae_mal}, por tonto")
