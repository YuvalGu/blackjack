class Hand:
    def __init__(self):
        self.cards = []
        self.soft = self.is_soft()

    def given_card(self, card):
        """
        adding the given card to cards and changing the values of the player's aces [if there are any] if needed
        :param card: another card to player's hand
        """
        self.cards.append(card)
        if self.value() > 21:
            # check if the player has Aces that can change to 1
            aces = self.get_ace_cards()
            while aces != [] and self.value() > 21:
                ace = aces.pop()
                ace.value = 1
        # if the additional card has a value of 11, the hand can change from soft to hard
        # if the additional card caused the hand value to be more than 21 and we changed the ace to 1:
        # the hand can change from hard to soft
        self.soft = self.is_soft()

    def is_soft(self):
        """
        soft hand - player has ace card with value 11
        hard hand - o.w
        :return: true if cards contain ace with value 11, false o.w
        """
        for card in self.cards:
            if card.name == 'Ace' and card.value == 11:
                return True
        return False

    def value(self):
        """
        :return: summarizes all cards value the player has
        """
        sum = 0
        for card in self.cards:
            sum += card.value
        return sum

    def get_ace_cards(self):
        """
        :return: list of aces the player has
        """
        aces = []
        for card in self.cards:
            if card.name == 'Ace':
                aces.append(card)
        return aces