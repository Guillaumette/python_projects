import random

HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
        |
         |
         |
        ===''', '''
    +---+
    0   |
    |   |
        |
       ===''', '''
    +---+
    0   |
   /|   |
        |
       ===''', '''
    +---+
    0   |
   /|\  |
        |
       ===''', '''
    +---+
    0   |
   /|\  |
   /    |
       ===''', '''
    +---+
    0   |
   /|\  |
   / \  |
       ===''']
words = 'аист акула бабуин баран барсук бобер бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук лимон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'.split()


def get_random_word(word_list):
    '''Функция возвращает случайную строку из переданного списка.'''
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]


def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '-' * len(secret_word)

    for i in range(len(secret_word)):  # заменяет пропуски отгаданными буквами
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

    for letter in blanks:  # Показывает секретное слово с пробелами между буквами
        print(letter, end=' ')
    print()


def get_guess(already_guessed):
    '''Возвращает букву, введенную игроком. Эта функция проверяет, что игрок ввел только одну букву.'''
    while True:
        print('Введите букву.')
        guess = input().lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess is already_guessed:
            print('Вы уже называли эту букву. Введите другую.')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ.')
        else:
            return guess


def replay():
    '''Эта функция возвращает True, если игрок хочет сыграть заново, иначе возвращает False'''
    print('Хотите сыграть еще? (да или нет)')
    return input().lower().startswith('д')


print('=====В И С Е Л И Ц А=====')
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words)
game_is_done = False

while True:
    display_board(missed_letters, correct_letters, secret_word)

    # Позволяет игроку ввести букву.
    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters += guess

        # Проверяет, выиграл ли игрок.
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print(f'ДА! Секретное слово - "{secret_word}"! Вы угадали!')
            game_is_done = True
    else:
        missed_letters += guess

        # Проверяет, превысил ли игрок лимит попыток и проиграл.
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            print('Вы исчерпали все попытки!\nНе угадано букв: ' + str(len(missed_letters)) + ' и угадано букв: ' + str(
                len(correct_letters)) + '. Было загадано слово "' + secret_word + '".')
            game_is_done = True

    # Запрашивает, хочет ли игрок сыграть заново (только если игра завершена).
    if game_is_done:
        if replay():
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word = get_random_word(words)
        else:
            break