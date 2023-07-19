from random import randint
from decouple import config
from winning_logic import check_result


def get_bet():
    while True:
        bet = input("Сделайте ставку на число от 1 до 30: ")
        if randint(1, 30):
            return int(bet)
        else:
            print("Ошибка. Пожалуйста, введите число от 1 до 30.")


def play_again():
    while True:
        choice = input("Хотите ли вы сыграть еще раз? (да/нет): ")
        if choice.lower() == "да":
            return True
        elif choice.lower() == "нет":
            return False
        else:
            print("Ошибка. Пожалуйста, введите 'да' или 'нет'.")


def play_game():
    money = config("MY-MONEY", cast=int)
    while True:
        print(f"Ваш текущий капитал: ${money}")
        bet = get_bet()
        winning_slot = randint(1, 30)
        money = check_result(bet, winning_slot, money)
        if money <= 0:
            print("У вас закончились деньги. Игра окончена.")
            break
        if not play_again():
            print("Итог игры:")
            if money > config('MY-MONEY', cast=int):
                print("Вы в выигрыше!")
            else:
                print("Вы в проигрыше.")
            break


play_game()
