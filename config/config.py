from literals.enums import AlertType, DispatchType, EventType


# Class to configure alerts based on event type and count
class AlertConfig:
    def __init__(self, type: AlertType, count: int, window_size_in_secs: int = None):
        self.type = type  # The type of log (e.g., ERROR, WARNING)
        self.count = count  # The number of events required to trigger the log
        self.window_size_in_secs = (
            window_size_in_secs  # Optional time window for the count
        )


# Class to define the strategy for dispatching alerts
class DispatchStrategy:
    def __init__(self, type: DispatchType, message: str, subject: str = None):
        self.type = type  # The type of dispatch (e.g., EMAIL, SMS)
        self.message = message  # The message to be sent
        self.subject = subject  # Optional subject for the dispatch


# Class to represent an alert
class Alert:
    def __init__(
        self,
        client: str,
        event_type: EventType,
        alert_config: AlertConfig,
        dispatch_strategy_list: list[DispatchStrategy],
    ):
        self.client = client  # The client associated with the alert
        self.event_type = event_type  # The type of event triggering the alert
        self.alert_config = alert_config  # The configuration of the alert
        self.dispatch_strategy_list = (
            dispatch_strategy_list  # List of strategies to dispatch the alert
        )
