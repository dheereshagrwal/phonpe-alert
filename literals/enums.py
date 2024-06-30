from enum import Enum, auto


class DispatchType(Enum):
    CONSOLE = auto()
    EMAIL = auto()

    def __str__(self):
        return self.name


class AlertType(Enum):
    SIMPLE_COUNT = auto()
    TUMBLING_WINDOW = auto()
    SLIDING_WINDOW = auto()

    def __str__(self):
        return self.name


class EventType(Enum):
    PAYMENT_EXCEPTION = auto()
    USERSERVICE_EXCEPTION = auto()
    LOGIN_FAILURE = auto()

    def __str__(self):
        return self.name


class EventStatus(Enum):
    STARTS = auto()
    ENDS = auto()

    def __str__(self):
        return self.name.lower()


class LogLevel(Enum):
    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()

    def __str__(self):
        return self.name


class TextFormatType(Enum):
    BOLD = auto()
    ITALIC = auto()
    UNDERLINE = auto()

    def __str__(self):
        return self.name.lower()
