"""Defines a Game class with a level property that enforces value bounds.

The level property uses a setter to clamp values between 0 and 100. 
The class constructor sets a default level of 0.

Some example Game instances are created and their level property 
printed to demonstrate the clamping behavior.
"""
class Game:

    def __init__(self, level=0):
        self.level = level

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if value < 0:
            self._level = 0
        elif value > 100:
            self._level = 100
        else:
            self._level = value

games = [Game(), Game(10), Game(-10), Game(133)]
print(games)

print([game.level for game in games])

for game in games:
    print(game.level)