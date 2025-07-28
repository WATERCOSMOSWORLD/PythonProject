import os


def rename_files(directory, prefix="new_file_"):
    """
    Переименовывает все файлы в указанной директории, добавляя префикс.
    """
    if not os.path.exists(directory):
        print(f"Ошибка: Директория '{directory}' не существует.")
        return

    print(f"Начинаю переименование файлов в '{directory}'...")

    # Получаем список всех файлов в директории
    for index, filename in enumerate(os.listdir(directory)):
        # Создаем полный путь к старому файлу
        old_file_path = os.path.join(directory, filename)

        # Проверяем, является ли это файлом, а не папкой
        if os.path.isfile(old_file_path):
            # Создаем новое имя файла с префиксом и индексом
            new_filename = f"{prefix}{index + 1}{os.path.splitext(filename)[1]}"
            new_file_path = os.path.join(directory, new_filename)

            # Переименовываем файл
            os.rename(old_file_path, new_file_path)
            print(f"Переименован '{filename}' в '{new_filename}'.")

    print("Переименование завершено!")


def main():
    """Главная функция программы."""
    print("Добро пожаловать в Переименовщик Файлов!")
    directory_to_rename = input("Введите путь к папке для переименования: ")

    if os.path.isdir(directory_to_rename):
        rename_files(directory_to_rename)
    else:
        print("Некорректный путь. Пожалуйста, введите путь к существующей папке.")


if __name__ == "__main__":
    main()