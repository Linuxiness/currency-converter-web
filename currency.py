
import requests

def currency_converter(amount, from_currency, to_currency):
    # Use the 'requests' library to fetch the current exchange rate
    url = f'https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}'
    res = requests.get(url)
    data = res.json()
    exchange_rate = data['rates'][to_currency]

    # Multiply the amount by the exchange rate to get the converted amount
    converted_amount = amount * exchange_rate

    return converted_amount

# Ask the user for the amount and currencies to convert
amount = float(input("Enter the amount: "))
from_currency = input("Enter the currency to convert from (e.g. USD, EUR): ")
to_currency = input("Enter the currency to convert to (e.g. USD, EUR): ")

# Use the currency_converter function to get the converted amount
converted_amount = currency_converter(amount, from_currency, to_currency)

# Print the result
print(f"{amount} {from_currency} is equivalent to {converted_amount} {to_currency}")
