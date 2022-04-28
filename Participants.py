from Hand import Hand
from Strategies import dealer_strategy


class Participant:
    def __init__(self, name, budget, strategy):
        """
        :param name: the name of the participant
        :param budget: the budget of the participant
        :param strategy: the participant's strategy
        """
        self.name = name
        self.budget = budget
        self.strategy = strategy
        self.hand = Hand()
        self.bust = False

    def busted(self):
        """
        the participant busted - so now the bust is True and the participant lost one chip
        """
        self.bust = True
        self.budget -= 1

    def reset(self):
        """
        reset the values of the participants that changed during the game
        """
        self.hand = Hand()
        self.bust = False


class Player(Participant):
    def __init__(self, name, budget, strategy):
        """
        :param name: player name
        :param budget: initial budget to start the game
        :param strategy: strategy function for players decisions
        """
        super().__init__(name, budget, strategy)

    def __str__(self):
        """
         represents the class Player as a string
        :return: his title (player) and his name
        """
        return f"Player {self.name}"


class Dealer(Participant):
    def __init__(self, name: str, budget=100):
        """
        :param name: dealer's name
        :param budget: initial budget to start the game
        :param strategy: strategy function for dealers decisions
        """
        super().__init__(name, budget, dealer_strategy)

    def __str__(self):
        """
         represents the class Dealer as a string
        :return: his title (dealer) and his name
        """
        return f"Dealer {self.name}"

    def deal_card(self, pack, participant_hand, count):
        """
        take [count] cards from the pack and gives it to the participant hand
        :param pack: the card pack
        :param participant_hand: the hand of the participant (player or the dealer himself)
        :param count: how many times repeat this action
        :return: the cards the dealer deals as a string
        """
        cards = []
        while count:
            card = pack.take_card()
            participant_hand.given_card(card)
            cards.append(card)
            count -= 1
        return '\n'.join([c.__str__() for c in cards])
