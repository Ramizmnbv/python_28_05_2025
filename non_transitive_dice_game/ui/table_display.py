from tabulate import tabulate
from logic.probability import ProbabilityCalculator
from utils.color import Color
class TableDisplay:
    @staticmethod
    def show(dice_list):
        print(Color.info("\nProbability of the win for the user:"))
        headers = [Color.highlight("User dice vs Computer dice")] + [Color.highlight(str(dice.faces)) for dice in dice_list]
        table = []
        for i, user_dice in enumerate(dice_list):
            row = [str(user_dice.faces)]
            for j, comp_dice in enumerate(dice_list):
                if i == j:
                    row.append("-")
                else:
                    prob = ProbabilityCalculator.calculate(user_dice.faces, comp_dice.faces)
                    result_color = Color.success if prob > 0.5 else Color.warning 
                    row.append(result_color(f"{prob:.4f}"))
            table.append(row)
        print(Color.info(tabulate(table, headers=headers, tablefmt="grid")))