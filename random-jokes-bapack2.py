from requests import get
from os import name, system
from random import randint

def clear():
    system('cls') if name == 'nt' else system('clear')

def get_jokes():
    return get('https://jokes-bapack2-api.herokuapp.com/v1/text').json()['data']

def random_joke():
    return jokes[randint(0, total_jokes - 1)]

jokes       = get_jokes()
total_jokes = len(jokes)
command     = ''

while command.lower().strip() != 'exit':
    clear()
    print(random_joke())
    print('\nPress [enter] to get another jokes, or type "exit" if you want to.')
    command = input()
