import requests
from bs4 import BeautifulSoup


def scrape_habr_posts():
    """Собирает заголовки последних постов с сайта Habr.com."""
    url = "https://habr.com/ru/articles/"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Вызывает ошибку для плохих HTTP-ответов

        soup = BeautifulSoup(response.text, 'html.parser')

        # Находим все элементы с заголовками статей
        # На Habr.com заголовки находятся в теге <h3> с классом "tm-title__link"
        headlines = soup.find_all('h2', class_='tm-title tm-title_h2')

        print("Последние статьи с Habr.com:")
        if headlines:
            for headline in headlines:
                # Извлекаем текст из дочернего элемента <span>
                title_text = headline.find('span').text.strip()
                print(f"- {title_text}")
        else:
            print("Не удалось найти заголовки.")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к сайту: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    scrape_habr_posts()