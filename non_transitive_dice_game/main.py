import sys
from engine.game import NonTransitiveDiceGame
from utils.color import Color

def main():
    args = sys.argv[1:]
    if not args:
        print(Color.error("You must provide at least 3 dice as CLI arguments."))
        print(Color.info("Example: python main.py 1,2,3 3,4,5 2,2,6"))
        return

    game = NonTransitiveDiceGame(args)
    game.start()

if __name__ == "__main__":
    main()