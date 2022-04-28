import random


def strategy1(player_hand, dealer_hand):
    player_value = player_hand.value()
    dealer_value = dealer_hand.value()

    if player_value < dealer_value:
        return 'hit'

    if player_hand.soft:
        if player_value < 17:
            return 'hit'
        elif player_value > 18:
            return 'stand'
        else:
            if random.choice([0, 1]):
                return 'hit'
            else:
                return 'stand'
    else:
        if player_value < 11:
            return 'hit'
        elif player_value > 17:
            return 'stand'
        else:
            return 'hit'


def strategy3(player_hand, dealer_hand):
    pvalue = player_hand.value()
    dvalue = dealer_hand.value()
    psoft = player_hand.soft
    dsoft = dealer_hand.soft
    phard = not player_hand.soft
    dhard = not dealer_hand.soft

    if 17 <= dvalue <= 21:  # Dealer pat hand
        if pvalue < dvalue:
            return 'hit'
    elif 7 <= dvalue <= 11:
        if pvalue <= dvalue or 12 <= pvalue <= 15:
            return 'hit'
    elif dvalue < 7:
        if pvalue < 12:
            return 'hit'
        elif psoft and pvalue < 16:
            return 'hit'

    if dhard and 12 <= dvalue <= 16:  # Dealer "stiff" hand
        if pvalue < dvalue:
            return 'hit'
        elif psoft and pvalue <= 16:
            return 'hit'

    if dsoft and 12 <= dvalue <= 16:
        if pvalue <= 12:
            return 'hit'
        elif psoft and pvalue <= 18:
            return 'hit'

    return 'stand'


def dealer_strategy(_, dealer_hand):
    """
    :param dealer_hand: the dealer hand
    :return: 'hit' if the value of the hand is less than 17, or 'stand' is the value greater than 17
    """
    dvalue = dealer_hand.value()
    if dvalue < 17:
        return 'hit'
    else:
        return 'stand'
