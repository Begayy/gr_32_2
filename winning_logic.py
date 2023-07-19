def check_result(bet, winning_slot, money):
    if bet == winning_slot:
        money += bet * 2
        print("Поздравляем! Вы выиграли!")
    else:
        money -= bet
        print("Вы проиграли.")

    print(f"Ваш текущий капитал: ${money}")
    return money
