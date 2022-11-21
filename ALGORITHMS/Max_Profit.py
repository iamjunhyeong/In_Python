stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]

m = 0
while stock:
    if len(stock) == 1: break
    buy = stock.pop(0)
    bnf = max(stock) - buy
    if m < bnf: m = bnf

print(m)