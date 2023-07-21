import random
import time


def display_intro():
    print('''
Вы находитесь в землях, заселенных драконами.
Перед собой вы видите две пещеры. В одной из них - дружелюбный дракон,
который готов поделиться с вами сокровищами. Во второй - 
жадный и голодный дракон, который мигом вас съест.''')
    print()


def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        print('В какую пещеру вы войдете? (нажмите клавишу 1 или 2)')
        cave = input()

    return cave


def check_cave(chosen_cave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Ее темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    print()
    time.sleep(2)

    friendly_cave = random.randint(1, 2)

    if chosen_cave == str(friendly_cave):
        print('...делится с вами сокровищами!')
    else:
        print('...моментально вас съедает!')


replay = 'да'
while replay.lower() == 'да' or replay.lower() == 'д':
    display_intro()
    cave_number = choose_cave()
    check_cave(cave_number)

    print('Попытаете удачу еще раз? (да или нет)')
    replay = input()