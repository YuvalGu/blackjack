# a few simple test functions
# test 1 game example
from BlackjackGame import Game
from Participants import Player, Dealer
from Strategies import strategy3, strategy1


def test():
    dealer = Dealer('Eli', 10000)
    a = Player('Alice', 100, strategy1)
    b = Player('Bob', 200, strategy3)
    c = Player('Clod', 100, strategy1)
    d = Player('Dian', 250, strategy3)
    # print("Dealer:", dealer.name)
    # print("Players:", a.name, b.name, c.name, d.name)
    players = [a, b, c, d]
    g = Game(dealer, players)
    g.run()
    print(g.log)  # should print all game history


# test simulation of 300 games
def test_sim():
    dealer = Dealer('Eli', 10000)
    a = Player('Alice', 500, strategy3)
    b = Player('Bob', 500, strategy1)
    c = Player('Clod', 500, strategy1)
    for i in range(300):
        g = Game(dealer, [a, b, c])
        g.run()
    print(a.name, a.budget)  # which budget is higher?
    print(b.name, b.budget)
    print(c.name, c.budget)


test()
