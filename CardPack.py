from Card import Card
from random import shuffle


class CardPack:
    def __init__(self):
        """
        we created a pack by calling the card class 52 times.
        for each suit we scanned 13 ranks, created a card and added it to the pack.
        """
        self.pack = []
        ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
                 'K': 10, 'A': 11}
        suits = {'Spade': '♠', 'Diamond': '♦', 'Heart': '♥', 'Club': '♣'}
        for suit_key in suits:
            for key in ranks:
                card = Card(key, ranks[key], suit_key, suits[suit_key])
                self.pack.append(card)

    def shuffle(self):
        """
        shuffling the stack randomly.
        """
        shuffle(self.pack)

    def take_card(self):
        """
        :return: a card from the top of the pack.
        """
        return self.pack.pop()
