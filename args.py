# args.py

def echo(user, lang, sys):
    print("User:", user, "Language:", lang, "Platform:", sys)

echo('Mike', 'Python', 'ChromeOS')

echo(lang = 'Python', sys = 'Windows 11', user = 'Adam')

def mirror(user = 'Lauren', lang = 'Python'):
    print("\nUser: ", user, "Language: ", lang)

mirror()
mirror(lang = 'JavaScript')
mirror(user = 'Big Mike')
mirror('Attractive', 'C++')
