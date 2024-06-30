from datetime import datetime
from literals.enums import EventType


# Class to represent an event
class Event:
    def __init__(self, client: str, type: EventType, timestamp: datetime):
        self.client = client  # The client associated with the event
        self.type = type  # The type of the event (e.g., PAYMENT_EXCEPTION, USERSERVICE_EXCEPTION)
        self.timestamp = timestamp  # The timestamp when the event occurred
