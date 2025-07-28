import os
import shutil


def sort_files(directory):
    """
    Сортирует файлы в указанной директории по их расширению.
    """
    if not os.path.exists(directory):
        print(f"Ошибка: Директория '{directory}' не существует.")
        return

    # Получаем список всех файлов в директории
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Проверяем, является ли это файлом, а не папкой
        if os.path.isfile(file_path):
            # Получаем расширение файла
            _, file_extension = os.path.splitext(filename)
            file_extension = file_extension.lower()

            # Создаём папку для этого типа файлов, если её нет
            if file_extension:
                target_folder = os.path.join(directory, file_extension[1:])
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                # Перемещаем файл в нужную папку
                shutil.move(file_path, target_folder)
                print(f"Файл '{filename}' перемещён в '{file_extension[1:]}'.")


def main():
    """Главная функция программы."""
    print("Добро пожаловать в Сортировщик Файлов!")
    directory_to_sort = input("Введите путь к папке для сортировки: ")

    # Проверяем, существует ли папка
    if os.path.isdir(directory_to_sort):
        sort_files(directory_to_sort)
        print("Сортировка завершена!")
    else:
        print("Некорректный путь. Пожалуйста, введите путь к существующей папке.")


if __name__ == "__main__":
    main()