# This is a sample Python script.
import requests
import json
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

param = {"symbol": "ETHBTC"}
def get_info(result=None):
    response = requests.get(url="https://api1.binance.com/api/v3/ticker/price", params=result)

    with open('info.txt', 'w') as file:
        file.write(response.text)
    return response.text


def main():
    result = input('Bведите курc, например: ETH-BTC')
    result = result.upper().replace('-', '').replace(' ', '').replace('.', '')
    result = {"symbol": result}

    json_file = json.loads(get_info(result))
    if len(json_file) == 2:
        print(f'''КУРС: {json_file["symbol"]}
ПРАЙС: {json_file["price"]}\n''')
    else:
        for sym in json_file:
            print(f'''КУРС: {sym["symbol"]}
ПРАЙС: {sym["price"]}\n''')



if __name__ == "__main__":
    main()
