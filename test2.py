import deck as d
import test

r = d.red_cards
g = d.green_cards
y = d.yellow_cards
b = d.blue_cards
w = d.wild_cards

for i in range(len(r) - 1):
    result = test.translate_card(r[i])
    print(result)

for i in range(len(g) - 1):
    result = test.translate_card(g[i])
    print(result)

for i in range(len(y) - 1):
    result = test.translate_card(y[i])
    print(result)

for i in range(len(b) - 1):
    result = test.translate_card(b[i])
    print(result)

for i in range(len(w) - 1):
    result = test.translate_card(w[i])
    print(result)