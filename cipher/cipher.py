def caesar_cipher(text, shift, mode):
    """
    Шифрует или дешифрует текст с помощью шифра Цезаря.
    """
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            # Обработка строчных букв
            start = ord('a')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        elif 'A' <= char <= 'Z':
            # Обработка заглавных букв
            start = ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            # Символы, не являющиеся буквами, оставляем без изменений
            result += char
    return result


def main():
    """Главная функция для работы с шифром."""
    while True:
        print("\nВыберите действие:")
        print("1. Зашифровать")
        print("2. Дешифровать")
        print("3. Выйти")

        choice = input("Ваш выбор: ")

        if choice == '1' or choice == '2':
            text = input("Введите текст: ")
            try:
                shift = int(input("Введите сдвиг (число): "))
                mode = "encrypt" if choice == '1' else "decrypt"

                # Если дешифровка, сдвиг должен быть отрицательным
                if mode == "decrypt":
                    shift = -shift

                encrypted_text = caesar_cipher(text, shift, mode)
                print(f"Результат: {encrypted_text}")
            except ValueError:
                print("Сдвиг должен быть числом.")
        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")


if __name__ == "__main__":
    main()