from enum import Enum
import logging


class Colors(Enum):
    YELLOW = "\033[93m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    MAGENTA = "\033[95m"
    WHITE = "\033[90m"
    RESET = "\033[0m"


class Symbols(Enum):
    INFO = "ℹ️"
    WARNING = "⚠️"
    ERROR = "❌"
    SUCCESS = "✅"
    DEBUG = "🔎"


class ColoredLogger(logging.Logger):
    """A logger that outputs colored logs to the console."""

    def __init__(self, name: str):
        super().__init__(name)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        self.addHandler(handler)

    def info(self, msg: str, *args, **kwargs) -> None:
        colored_msg = f"{Symbols.INFO.value} {Colors.WHITE.value}{msg}{Colors.RESET.value}"
        super().info(colored_msg, *args, **kwargs)

    def warning(self, msg: str, *args, **kwargs) -> None:
        colored_msg = f"{Symbols.WARNING.value} {Colors.YELLOW.value}{msg}{Colors.RESET.value}"
        super().warning(colored_msg, *args, **kwargs)

    def error(self, msg: str, *args, **kwargs) -> None:
        colored_msg = f"{Symbols.ERROR.value} {Colors.RED.value}{msg}{Colors.RESET.value}"
        super().error(colored_msg, *args, **kwargs)

    def success(self, msg: str, *args, **kwargs) -> None:
        colored_msg = f"{Symbols.SUCCESS.value} {Colors.GREEN.value}{msg}{Colors.RESET.value}"
        super().info(colored_msg, *args, **kwargs)

    def debug(self, msg: str, *args, **kwargs) -> None:
        colored_msg = f"{Symbols.DEBUG.value} {Colors.MAGENTA.value}{msg}{Colors.RESET.value}"
        super().debug(colored_msg, *args, **kwargs)


logger = ColoredLogger(__name__)
