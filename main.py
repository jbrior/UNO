import random as r
import deal_cards as deal
import format_card_name as fcn

hands = deal.deal_cards()
p1_h = hands[0]
p2_h = hands[1]
init_card = hands[2]
current_deck = deal.temp_deck
turn_pos = 1
round_count = 1

def display_hands():
    print("Player 1:")
    for i in range(len(p1_h)):
        print(f"{i+1}: {fcn.translate_card(p1_h[i])}")
    print()
    print("Player 2:")
    for i in range(len(p2_h)):
        print(f"{i+1}: {fcn.translate_card(p2_h[i])}")
    print()
    print(f"Deck Count: {len(current_deck)}")
    print(f"Current Card Down: {fcn.translate_card(init_card)}")
    print()

def draw_card(player):
    x = r.randint(0, len(current_deck) - 1)

    if player == 1:
        p1_h.append(current_deck[x])
    else:
        p2_h.append(current_deck[x])

    current_deck.remove(current_deck[x])

def place_card(p, c):
    global init_card
    fpc = fcn.translate_card(c)
    fic = fcn.translate_card(init_card)

    if fpc[0] == "d":
        print("draw4 placed")
    elif fpc[0] == "w":
        print("wild card placed")
    elif fpc[0] == fic[0] or fpc[fpc.index(" ")-1:] == fic[fic.index(" ")-1:]:
        print("card matched")
    else:
        print("not a match")
        return

    if p == 1:
        init_card = c
        p1_h.remove(p1_h[c - 1])
    else:
        init_card = c
        p2_h.remove(p2_h[c - 1])


def start():
    global turn_pos
    global round_count

    if turn_pos == 1:
        print(f"----------------Turn {round_count}------------------")

    display_hands()

    if turn_pos == 1:
        p_input = input(f"P{turn_pos}'s Turn: ").strip()
        action = p_input[0]
        if action == "d":
            draw_card(turn_pos)
        elif action == "p":
            card = int(p_input[1:])
            place_card(1, card)
        turn_pos = 2
    else:
        p_input = input(f"P{turn_pos}'s Turn: ").replace(" ", "").lower()
        action = p_input[0]
        if action == "d":
            draw_card(turn_pos)
        elif action == "p":
            card = int(p_input[1:])
            place_card(2, card)

        round_count += 1
        turn_pos = 1

    start()

start()
