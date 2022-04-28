from CardPack import CardPack


class Game:
    def __init__(self, dealer, players):
        """
        the table game is made of:
        :param dealer: the dealer
        :param players: list of 2-6 players
        :param pack: a card pack
        :param log: documentation of events relevant to the game.
        """
        self.dealer = dealer
        self.players = players
        self.pack = CardPack()
        self.log = Documentation()

    def run(self):
        """
        deals 2 cards per participant (dealer and players), deals card to participant while he asks to be hit
        and wasn't busted. once all participants finish, we check who won
        """
        self.reset_round()
        # check if there are players:
        if len(self.players) == 0:
            self.log.add_event(f"there are no players. Game over!")
            return
        if self.dealer.budget == 0:
            self.log.add_event(f"Dealer's budget is over")
            return
        # At the beginning of the game the dealer deals 2 cards to each player.
        for player in self.players:
            cards = self.dealer.deal_card(self.pack, player.hand, 2)
            self.log.add_event(f'{player} gets\n{cards}')
            self.log.add_event(f"current {player.name}'s hand value is {player.hand.value()}")
        # At the end of the round, the dealer deals 2 cards to himself as well.
        cards = self.dealer.deal_card(self.pack, self.dealer.hand, 2)
        self.log.add_event(f'{self.dealer} gets\n{cards}')
        self.log.add_event(f"current {self.dealer.name}'s hand value is {self.dealer.hand.value()}")
        # at this point no one busted (because no one has hand value > 21)
        for player in self.players:
            self.participant_turn(player)
        # dealer's turn:
        self.participant_turn(self.dealer)
        # check who won:
        for player in self.players:
            self.check_if_wins(player)

    def check_if_wins(self, player):
        """
        check the player vs dealer
        if the dealer won - one chip is added to his budget, player loses one.
        if the player won - one chip is added to his budget, dealer loses one.
        if it's a tie - no chips today
        :param player: the player
        """
        if player.bust:
            if not self.dealer.bust:
                # dealer wins:
                self.log.add_event(f"{self.dealer} defeats {player}")
                # adding one chip to the dealer's budget if dealer not busted
                self.dealer.budget += 1
        elif self.dealer.bust:
            # player wins
            self.log.add_event(f"{player} defeats {self.dealer}")
            player.budget += 1
        elif self.dealer.hand.value() > player.hand.value():  # not the player nor the dealer aren't busted
            # dealer wins:
            self.log.add_event(f"{self.dealer} defeats {player}")
            # adding one chip to the dealer's budget
            self.dealer.budget += 1
            # decreasing one chip from the player's budget
            player.budget -= 1
        elif self.dealer.hand.value() == player.hand.value():
            self.log.add_event(f"{self.dealer} and {player} are in a tie! no chips today")
        else:  # dealer's hand value < player's hand value
            # player wins
            self.log.add_event(f"{player} defeats {self.dealer}")
            player.budget += 1
            self.dealer.budget -= 1
        # if the player lost all his money he is out of the game
        if player.budget == 0:
            self.log.add_event(f"{player.name}'s budget is 0. {player.name} is out of the game!")
            self.players.remove(player)

    def participant_turn(self, participant):
        self.log.add_event(f"{participant}'s turn:")
        self.log.add_event(f"current {participant.name}'s hand value is {participant.hand.value()}")
        while not participant.bust:
            # as long as he is not busted, the player can choose to hit or stand.
            if 'hit' == participant.strategy(participant.hand, self.dealer.hand):
                self.log.add_event(f'{participant}: hit!')
                card = self.dealer.deal_card(self.pack, participant.hand, 1)
                self.log.add_event(f'{participant} gets\n{card}')
                pvalue = participant.hand.value()
                self.log.add_event(f"current {participant.name}'s hand value is {pvalue}")
                if pvalue > 21:
                    participant.busted()
                    self.log.add_event(f'BUST!')
            else:
                self.log.add_event(f'{participant}: stand')
                break

    def reset_round(self):
        """
        reset card pack, participants and documentation
        """
        # reset pack
        self.pack = CardPack()
        self.pack.shuffle()
        # reset participants
        for player in self.players:
            player.reset()
        self.dealer.reset()
        # reset documentation
        self.log.reset()


class Documentation:
    def __init__(self):
        self.events = []

    def add_event(self, str):
        self.events.append(str)

    def reset(self):
        self.events = []

    def __str__(self):
        return '\n'.join(self.events)
