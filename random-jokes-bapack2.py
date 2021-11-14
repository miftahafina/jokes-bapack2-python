from requests import get
from os import name, system

while True:
    if name == 'nt':
        system('cls')
    else:
        system('clear')

    r = get('https://jokes-bapack2-api.herokuapp.com/v1/text/random')
    print(r.json()['data'])
    print('\nPress [enter] to get another jokes, or [ctrl c] to exit')
    input()
