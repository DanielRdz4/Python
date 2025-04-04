favorite_languages = {
    'jen': ['python', 'ruby'], 
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    
    if len(languages) >= 2:
        print(f"\n{name.title()} favourites languages are: ")
        for language in languages:
            print(language)
    else:
        print(f"\n{name.title()}'s favourite language is {languages[0]}")
        