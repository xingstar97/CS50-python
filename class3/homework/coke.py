sum = 0

while sum<50:
    due = 50-sum
    print(f"Amount due: {due}")
    coin = int(input("Insert coin: "))
    if coin in [25,10,5]:
        sum += coin

owe = sum -50
print(f"Change owed: {owe}")