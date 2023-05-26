register = [{'id': 4, 'date': '2023-05-20', 'time': '11:00:00', 'moneda_from': 'EUR', 'cantidad_from': 1.0, 'moneda_to': 'BTC', 'cantidad_to': 1000.0}, {'id': 5, 'date': '2023-05-24', 'time': '12:15:00', 'moneda_from': 'BTC', 'cantidad_from': 10.0, 'moneda_to': 'ETH', 'cantidad_to': 35000.0}]
all_crypt = ["EUR", "BTC", "ETH", "USDT", "BNB", "XRP", "ADA", "SOL", "DOT", "MATIC"]

mis_cripto = []
for moneda in all_crypt:
    for cripto in register:
        if moneda == cripto["moneda_to"]:
            mis_cripto.append(moneda)
            return mis_cripto

print(mis_cripto)