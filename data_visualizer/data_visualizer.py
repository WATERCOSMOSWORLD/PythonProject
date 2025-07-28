import pandas as pd
import matplotlib.pyplot as plt

def visualize_sales_data(file_path):
    """
    Загружает данные о продажах из CSV-файла и строит график.
    """
    try:
        df = pd.read_csv(file_path)

        plt.figure(figsize=(10, 6))
        plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-')
        plt.title('Ежемесячные продажи')
        plt.xlabel('Месяц')
        plt.ylabel('Продажи')
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
    except KeyError:
        print("Ошибка: CSV-файл должен содержать столбцы 'Month' и 'Sales'.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    visualize_sales_data('data.csv')