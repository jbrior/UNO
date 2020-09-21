
def translate_card(card):
    if "_" in card:
        x = card[:card.index("_")]
    else:
        x = card

    if x[0] == "r":
        return "RED " + "'" + str(x[1:]).replace("-", " ").capitalize() + "'"
    elif x[0] == "g":
        return "GREEN " + "'" + str(x[1:]).replace("-", " ").capitalize() + "'"
    elif x[0] == "y":
        return "YELLOW " + "'" + str(x[1:]).replace("-", " ").capitalize() + "'"
    elif x[0] == "b":
        return "BLUE " + "'" + str(x[1:]).replace("-", " ").capitalize() + "'"
    elif x[0] == "w":
        return "WILD"
    elif x[0] == "d":
        return "DRAW 4"
    else:
        return "Invalid Card"
