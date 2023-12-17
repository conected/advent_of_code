import re

THRESHOLDS = {
    'red': 12,
    'green': 13,
    'blue': 14
}


class Game:
    def __init__(self, game_input):
        self.id = 0
        self.hands = []

        self._parse_input(game_input)

    def _parse_input(self, game_input):
        id = re.match('^Game (?P<game_id>[1-9][0-9]*): .*$', game_input).group('game_id')
        self.id = int(id)

        all_hands = game_input.split(': ')[1]
        for hand in all_hands.split('; '):
            balls = hand.split(', ')

            parsed_hand = {}
            for balls_of_single_color in balls:
                amount, color = balls_of_single_color.split(' ')

                color = color.replace('\n', '')

                parsed_hand[color] = int(amount)

            self.hands.append(parsed_hand)

    def is_valid(self):
        for hand in self.hands:
            for color, amount in hand.items():
                if amount > THRESHOLDS[color]:
                    return False

        return True


games = open('input', 'r')

solution = 0
for game_input in games.readlines():
    game = Game(game_input)

    if game.is_valid():
        solution += game.id

print(f"The sum of indexes of all valid games is {solution}.")
