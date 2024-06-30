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
