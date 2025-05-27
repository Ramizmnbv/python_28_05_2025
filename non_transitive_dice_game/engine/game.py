from utils.dice_parser import DiceParser
from ui.menu import Menu
from core.fair_generator import FairRandomGenerator
from core.dice import Dice

class NonTransitiveDiceGame:
    def __init__(self, args):
        self.args = args
        self.dice_set = []

    def start(self):
        try:
            self.dice_set = DiceParser.parse(self.args)
        except ValueError as e:
            print(f"Error: {e}\nExample: python main.py 1,2,3,4,5,6 2,2,4,4,9,9 3,3,3,5,5,5")
            return

        print("Let's determine who makes the first move.")
        selector = FairRandomGenerator(2)
        computer_bit, hmac_hex = selector.commit()
        print(f"I selected a random value in the range 0..1 (HMAC={hmac_hex})")
        user_bit = Menu.select_bit()
        if user_bit is None:
            return
        result = selector.reveal(user_bit)
        if result["value"] == 1:
            print("I make the first move.")
            computer_index = Menu.select_dice(self.dice_set, "computer", exclude=None)
            user_index = Menu.select_dice(self.dice_set, "user", exclude=computer_index)
        else:
            print("You make the first move.")
            user_index = Menu.select_dice(self.dice_set, "user", exclude=None)
            computer_index = Menu.select_dice(self.dice_set, "computer", exclude=user_index)

        user_dice = self.dice_set[user_index]
        comp_dice = self.dice_set[computer_index]

        print("\nIt's time for my roll.")
        computer_roll = FairRandomGenerator(len(comp_dice.faces))
        computer_index, hmac_hex = computer_roll.commit()
        print(f"I selected a random value in the range 0..{len(comp_dice.faces) - 1} (HMAC={hmac_hex})")
        user_input = Menu.select_face(len(comp_dice.faces))
        if user_input is None:
            return
        result = computer_roll.reveal(user_input)
        computer_value = comp_dice.faces[result["value"]]
        print(f"My roll result is {computer_value}.")

        print("\nIt's time for your roll.")
        user_roll = FairRandomGenerator(len(user_dice.faces))
        user_index, hmac_hex = user_roll.commit()
        print(f"I selected a random value in the range 0..{len(user_dice.faces) - 1} (HMAC={hmac_hex})")
        user_input = Menu.select_face(len(user_dice.faces))
        if user_input is None:
            return
        result = user_roll.reveal(user_input)
        user_value = user_dice.faces[result["value"]]
        print(f"Your roll result is {user_value}.")

        if user_value > computer_value:
            print(f"\nYou win ({user_value} > {computer_value})!")
        elif user_value < computer_value:
            print(f"\nI win ({computer_value} > {user_value})!")
        else:
            print("\nIt's a draw!")