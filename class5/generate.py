import random

# random.choice(seq) seq means a list, the function picks one item from the list randomly

coin = random.choice(["heads","tails"])
print(coin)

# random.randint(a,b)
# generate a random number between a and b (inluding a and b)

number = random.randint(1,10)
print(number)


# random.shuffle(x) x should be a list
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

