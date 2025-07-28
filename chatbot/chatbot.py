def get_response(user_input):
    """Возвращает ответ бота на основе ввода пользователя."""
    user_input = user_input.lower().strip()

    if "привет" in user_input or "здравствуй" in user_input:
        return "Привет! Чем могу помочь?"
    elif "как дела" in user_input or "как ты" in user_input:
        return "У меня всё отлично, спасибо, что спросил!"
    elif "пока" in user_input or "до свидания" in user_input:
        return "До свидания! Обращайся ещё."
    elif "помощь" in user_input:
        return "Я могу отвечать на простые вопросы вроде 'привет', 'как дела' или 'пока'."
    else:
        return "Извини, я не понял. Попробуй задать другой вопрос."

def main():
    """Главная функция для общения с ботом."""
    print("Привет! Я простой чат-бот. Напиши 'пока' или 'до свидания', чтобы выйти.")
    while True:
        user_input = input("Вы: ")
        if "пока" in user_input.lower() or "до свидания" in user_input.lower():
            print("Бот:", get_response(user_input))
            break
        print("Бот:", get_response(user_input))

if __name__ == "__main__":
    main()