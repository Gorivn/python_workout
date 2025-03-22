import random

def guessing_game():
    '''Угадай число'''
    answer = random.randint(1, 100)

    while True:
        user_number = int(input('Введите ваше число: '))

        if user_number == answer:
            print(f'Вы угадали число {user_number}!')
            break
        elif user_number > answer:
            print(f'Число {user_number} слишком большое!')
        elif user_number < answer:
            print(f'Число {user_number} слишком маленькое!')


def main():
    guessing_game()


if __name__ == '__main__':
    main()

