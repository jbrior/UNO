import random as r
import deck as d

r_cards = d.red_cards
g_cards = d.green_cards
y_cards = d.yellow_cards
b_cards = d.blue_cards
w_cards = d.wild_cards

full_deck = r_cards + g_cards + y_cards + b_cards + w_cards

temp_deck = full_deck

def deal_cards():
    global temp_deck

    p1_hand = []
    p2_hand = []

    for i in range(7):
        x = r.randint(0, len(temp_deck) - 1)
        p1_hand.append(temp_deck[x])
        temp_deck.remove(temp_deck[x])

        x = r.randint(0, len(temp_deck) - 1)
        p2_hand.append(temp_deck[x])
        temp_deck.remove(temp_deck[x])

    x = r.randint(0, len(temp_deck) - 1)
    init_card = temp_deck[x]
    temp_deck.remove(init_card)

    return [p1_hand, p2_hand, init_card]