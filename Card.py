class Card:
    def __init__(self, name: str, value: int, suit: str, symbol: str):
        """

        :param name: card name
        :param value: the card's value
        :param suit: the card's type
        Example: name=King, value=10, suit=Heart
        """
        self.name = name
        self.value = value
        self.suit = suit
        self.symbol = symbol

    def __str__(self):
        """
        represents the class Card as a string
        :return: shape of a card with the symbol suit and the name
        """
        if self.name == '10':
            space = ''
        else:
            space = ' '
        lines = [[] for i in range(9)]
        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(self.name, space))  # use two {} one for char, one for space or char
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(self.symbol))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, self.name))
        lines[8].append('└─────────┘')
        result = []
        for index, line in enumerate(lines):
            result.append(''.join(lines[index]))
        return '\n'.join(result)
