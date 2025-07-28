import requests


def get_exchange_rates(base_currency):
    """Получает курсы валют относительно базовой валюты."""
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Вызывает ошибку, если запрос был неуспешным
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None


def convert_currency(amount, from_currency, to_currency, rates):
    """Конвертирует сумму из одной валюты в другую."""
    if from_currency not in rates or to_currency not in rates:
        print("Некорректная валюта.")
        return None

    # Конвертируем сумму в базовую валюту (в данном случае, USD)
    amount_in_usd = amount / rates[from_currency]
    # Конвертируем из USD в целевую валюту
    converted_amount = amount_in_usd * rates[to_currency]

    return converted_amount


if __name__ == "__main__":
    base_currency = "USD"
    rates_data = get_exchange_rates(base_currency)

    if rates_data and rates_data.get("result") == "success":
        rates = rates_data["rates"]

        try:
            from_currency = input("Введите валюту для конвертации (например, KZT): ").upper()
            to_currency = input("Введите целевую валюту (например, EUR): ").upper()
            amount = float(input(f"Введите сумму в {from_currency}: "))

            if from_currency == base_currency:
                # Если исходная валюта - базовая, конвертируем напрямую
                converted_amount = amount * rates[to_currency]
            else:
                converted_amount = convert_currency(amount, from_currency, to_currency, rates)

            if converted_amount is not None:
                print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

        except ValueError:
            print("Пожалуйста, введите корректную сумму.")
        except KeyError:
            print("Один из кодов валют некорректен или отсутствует в данных.")
    else:
        print("Не удалось получить актуальные курсы валют. Попробуйте позже.")