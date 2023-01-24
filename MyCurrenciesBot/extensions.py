import json
import requests
from config import currencies


class APIException(Exception):
    pass


class CurrenciesPrise:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        quote = quote.lower()
        base = base.lower()

        if quote == base:
            raise APIException(f"Невозможно перевести одинаковые валюты {base}."
                                      f"\n(для вызова подсказки введите /help)")
        try:
            quote_ticker = currencies[quote]
        except KeyError as e:
            raise APIException(f"Не удалось обработать валюту {quote}. Выберите из списка доступных валют."
                                      f"\n(для вызова подсказки введите /help)")
        try:
            base_ticker = currencies[base]
        except KeyError as e:
            raise APIException(f"Не удалось обработать валюту {base}. Выберите из списка доступных валют."
                                      f"\n(для вызова подсказки введите /help)")
        try:
            amount = float(amount)
            if amount <= 0:
                raise APIException(f"Не удалось обработать количество {amount}. Введите положительное число.")
        except ValueError as e:
            raise APIException(f"Не удалось обработать количество {amount}. Введите число в необходимом формате."
                                      f"\n(для вызова подсказки введите /help)")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        rate = json.loads(r.content)[currencies[base]]
        total_rate = amount * rate
        return total_rate





