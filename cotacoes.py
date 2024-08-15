import requests

# Função para buscar as cotações
def get_currency_rates():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    response = requests.get(url)
    data = response.json()

    rates = {
        "USD_BRL": f'{(data["USDBRL"]["bid"])}',
        "EUR_BRL": f'{(data["EURBRL"]["bid"])}',
        "BTC_BRL": f'{(data["BTCBRL"]["bid"])}',
    }
    print(rates)
    return rates