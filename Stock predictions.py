def printTransactions(m, k, d, names, owned, prices):
    transactions = []
    for i in range(k):
        name = names[i]
        owned_shares = owned[i]
        price_trend = prices[i]
        
        current_price = price_trend[-1]
        previous_price = price_trend[-2]
        
        if current_price > previous_price:
            max_buy = int(m // current_price)
            if max_buy > 0:
                transactions.append(f"{name} BUY {max_buy}")
                m -= max_buy * current_price
        elif current_price < previous_price and owned_shares > 0:
            transactions.append(f"{name} SELL {owned_shares}")

    print(len(transactions))
    for transaction in transactions:
        print(transaction)

        
        
m, k, d = [float(i) for i in input().strip().split()]
k = int(k)
d = int(d)
names = []
owned = []
prices = []
for data in range(k):
    temp = input().strip().split()
    names.append(temp[0])
    owned.append(int(temp[1]))
    prices.append([float(i) for i in temp[2:7]])


printTransactions(m, k, d, names, owned, prices)
