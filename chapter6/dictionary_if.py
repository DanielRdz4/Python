
fav_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
}

friends = ['sarah','jen']

for name in fav_languages.keys():

    if name in friends:
        language = fav_languages[name]
        print(f'Hi {name.title()} I see you love {language}')
    else:
        print(name.title())