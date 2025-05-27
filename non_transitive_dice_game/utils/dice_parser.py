from core.dice import Dice
from utils.color import Color
class DiceParser:
    @staticmethod
    def parse(args):
        if len(args) < 3:
            raise ValueError(Color.error("You must provide at least 3 dice."))
        dice_list = []
        for arg in args:
            try:
                faces = list(map(int, arg.split(',')))
                if len(faces) < 1:
                    raise ValueError
                dice_list.append(Dice(faces))
            except:
                raise ValueError(Color.error(f"Invalid dice: '{arg}' must be a comma-separated list of integers."))
        return dice_list