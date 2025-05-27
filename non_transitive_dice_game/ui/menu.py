from ui.table_display import TableDisplay

class Menu:
    @staticmethod
    def select_bit():
        while True:
            print("0 - 0\n1 - 1\nX - exit\n? - help")
            choice = input("Your selection: ").lower()
            if choice == 'x':
                return None
            if choice == '?':
                print("You need to guess 0 or 1. If correct, you start; else, computer starts.")
            elif choice in ('0', '1'):
                return int(choice)
            else:
                print("Invalid input.")

    @staticmethod
    def select_face(size):
        while True:
            print("\n".join([f"{i} - {i}" for i in range(size)]) + "\nX - exit\n? - help")
            choice = input("Your selection: ").lower()
            if choice == 'x':
                return None
            if choice == '?':
                print("Add your number modulo dice size to reveal the result.")
            elif choice.isdigit() and 0 <= int(choice) < size:
                return int(choice)
            else:
                print("Invalid input.")

    @staticmethod
    def select_dice(dice_list, owner, exclude=None):
        while True:
            print(f"\nChoose {owner}'s dice:")
            for i, dice in enumerate(dice_list):
                if i == exclude:
                    continue
                print(f"{i} - {dice}")
            print("X - exit\n? - help")
            choice = input("Your selection: ").lower()
            if choice == 'x':
                return None
            if choice == '?':
                TableDisplay.show(dice_list)
            elif choice.isdigit():
                idx = int(choice)
                if idx < len(dice_list) and idx != exclude:
                    return idx
            print("Invalid input.")