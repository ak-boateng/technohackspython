# import needed modules,packages

import requests


# Get source_currency, target_currency, and amount_to_convert from the user


source = str(
    input("Which currency do you want to convert from: ")).upper()
target = str(
    input("Which currency do you want to convert from: ")).upper()

amount = float(input(
    "How much do you want to convert(use . to separate paper notes and coins): "))

# API Call to Franfurter Open Source API

response = requests.get(
    f"https://api.frankfurter.app/latest?amount={amount}&from={source}&to={target}")


# Error Handling

if response.status_code == 200:
    data = response.json()
    converted_amount = data['rates'][target]
    # Print the conversion result
    print(f"{amount} {source} is {converted_amount} in {target}")
else:
    # Print an error message if the request failed
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")
