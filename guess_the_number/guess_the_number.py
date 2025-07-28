import random


def guess_the_number(max_attempts=10):
    """
    Игра, где пользователь должен угадать число за ограниченное количество попыток.
    """
    secret_number = random.randint(1, 100)
    attempts = 0

    print(f"Я загадал число от 1 до 100. У вас есть {max_attempts} попыток.")

    while attempts < max_attempts:
        try:
            user_guess = int(input("Ваша попытка: "))
            attempts += 1

            if user_guess < secret_number:
                print("Слишком мало.")
            elif user_guess > secret_number:
                print("Слишком много.")
            else:
                print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток!")
                return  # Выходим из функции, так как игра закончена
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    # Этот код выполнится, если закончились попытки
    print("\nПопытки закончились. Вы проиграли.")
    print(f"Я загадал число {secret_number}.")


if __name__ == "__main__":
    guess_the_number()