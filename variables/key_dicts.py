#!/usr/bin/env python3.8

favorites_languages = {
    'danilo':'C++',
    'rosy':'java',
    'nycolas':'ruby',
    'joaquim':'python',
}

friends = ['danilo', 'rosy']

for name in favorites_languages.keys():
    if name in friends:
        print("This is my friend "+name.title()+" programming in "+favorites_languages[name])
    else:
        print(name.title())

if 'danilo' in favorites_languages.keys():
    print("My favorite developer is Danilo")


