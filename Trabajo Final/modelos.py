import requests
from db import get_db_connection
from config import API_KEY, BASE_URL

class Conversion:
    def __init__(self, amount, from_currency, to_currency):
        self.amount = amount
        self.from_currency = from_currency
        self.to_currency = to_currency

    def convert(self):
        url = f"{BASE_URL}?access_key={API_KEY}&base={self.from_currency}"
        response = requests.get(url)
        rates = response.json().get('rates', {})
        
        if self.to_currency in rates:
            self.converted_amount = self.amount * rates[self.to_currency]
            return self.converted_amount
        else:
            raise ValueError("Currency not found")

    def save_to_db(self):
        conexion = get_db_connection()
        conexion.execute('INSERT INTO conversion_history (amount, from_currency, to_currency, converted_amount) VALUES (?, ?, ?, ?)',
                         (self.amount, self.from_currency, self.to_currency, self.converted_amount))
        conexion.commit()
        conexion.close()
