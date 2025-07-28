def load_tasks():
    """Загружает задачи из файла 'tasks.txt'."""
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Сохраняет задачи в файл 'tasks.txt'."""
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task}\n")


def show_tasks(tasks):
    """Выводит список всех задач."""
    if not tasks:
        print("Список задач пуст.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task(tasks, task_text):
    """Добавляет новую задачу в список."""
    tasks.append(task_text)
    save_tasks(tasks)
    print(f"Задача '{task_text}' добавлена.")


def remove_task(tasks, task_number):
    """Удаляет задачу по номеру."""
    try:
        task_text = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Задача '{task_text}' удалена.")
    except IndexError:
        print("Некорректный номер задачи.")


def main():
    """Главная функция программы."""
    tasks = load_tasks()

    while True:
        print("\nВыберите действие:")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выйти")

        choice = input("Ваш выбор: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            task_text = input("Введите новую задачу: ")
            add_task(tasks, task_text)
        elif choice == '3':
            show_tasks(tasks)
            if tasks:
                try:
                    task_number = int(input("Введите номер задачи для удаления: "))
                    remove_task(tasks, task_number)
                except ValueError:
                    print("Пожалуйста, введите корректное число.")
        elif choice == '4':
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие от 1 до 4.")


if __name__ == "__main__":
    main()