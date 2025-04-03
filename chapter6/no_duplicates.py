favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print('the following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language)

