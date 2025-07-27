import random
import string


def generate_password(length):
    # Объединяем все возможные символы
    characters = string.ascii_letters + string.digits + string.punctuation

    # Генерируем случайный пароль указанной длины
    password = ''.join(random.choice(characters) for i in range(length))
    return password


if __name__ == "__main__":
    try:
        # Спрашиваем у пользователя желаемую длину пароля
        password_length = int(input("Введите желаемую длину пароля: "))

        # Проверяем, чтобы длина была больше нуля
        if password_length <= 0:
            print("Длина пароля должна быть положительным числом.")
        else:
            new_password = generate_password(password_length)
            print("Сгенерированный пароль:", new_password)
    except ValueError:
        print("Пожалуйста, введите корректное число.")