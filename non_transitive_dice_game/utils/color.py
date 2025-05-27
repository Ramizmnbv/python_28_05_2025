class Color:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'

    @staticmethod
    def colorize(text, color):
        return f"{color}{text}{Color.RESET}"

    @staticmethod
    def error(text):
        return Color.colorize(text, Color.RED)

    @staticmethod
    def success(text):
        return Color.colorize(text, Color.GREEN)

    @staticmethod
    def warning(text):
        return Color.colorize(text, Color.YELLOW)

    @staticmethod
    def info(text):
        return Color.colorize(text, Color.CYAN)

    @staticmethod
    def highlight(text):
        return Color.colorize(text, Color.BOLD + Color.BLUE)