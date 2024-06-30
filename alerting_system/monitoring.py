from datetime import datetime, timedelta
from alerting_system.logger import Logger
from literals.enums import AlertType, EventStatus, TextFormatType
from alerting_system.event import Event
from alerting_system.config import Alert
from alerting_system.dispatcher import DispatchService

logger = Logger()


# Service to monitor events and trigger alerts
class MonitoringService:
    def __init__(self, alert_configs: list[Alert]):
        self.alert_configs: list[Alert] = alert_configs  # List of alert configurations
        self.event_history: list[Event] = []  # History of events

    # Log information messages for event processing
    def log_info_message(self, event: Event, alert: Alert, message_type: EventStatus):
        logger.info(
            f"MonitoringService: Client {event.client} {event.type} {alert.alert_config.type} {message_type}"
        )

    # Monitor incoming events
    def monitor_event(self, event: Event):
        self.event_history.append(event)  # Add event to history
        for alert in self.alert_configs:
            if alert.client == event.client and alert.event_type == event.type:
                self.log_info_message(event, alert, EventStatus.STARTS)
                if self.check_threshold(alert, event):
                    self.trigger_alert(alert)
                else:
                    self.log_info_message(event, alert, EventStatus.ENDS)

    # Check if the alert threshold is breached
    def check_threshold(self, alert: Alert, event: Event) -> bool:
        alert_type = alert.alert_config.type
        match alert_type:
            case AlertType.SIMPLE_COUNT:
                return self.check_simple_count(alert)
            case AlertType.TUMBLING_WINDOW:
                return self.check_tumbling_window(alert, event.timestamp)
            case AlertType.SLIDING_WINDOW:
                return self.check_sliding_window(alert, event.timestamp)
            case _:
                return False

    # Check if the simple count threshold is breached
    def check_simple_count(self, alert: Alert) -> bool:
        events = [
            e
            for e in self.event_history
            if e.client == alert.client and e.type == alert.event_type
        ]
        return len(events) >= alert.alert_config.count

    # Check if the tumbling window threshold is breached
    def check_tumbling_window(self, alert: Alert, timestamp: datetime) -> bool:
        start_of_day = timestamp.replace(hour=0, minute=0, second=0, microsecond=0)
        bucket_start = start_of_day + timedelta(
            seconds=(timestamp - start_of_day).seconds
            // alert.alert_config.window_size_in_secs
            * alert.alert_config.window_size_in_secs
        )
        bucket_end = bucket_start + timedelta(
            seconds=alert.alert_config.window_size_in_secs
        )
        events = [
            e
            for e in self.event_history
            if e.client == alert.client
            and e.type == alert.event_type
            and bucket_start <= e.timestamp < bucket_end
        ]
        return len(events) >= alert.alert_config.count

    # Check if the sliding window threshold is breached
    def check_sliding_window(self, alert: Alert, timestamp: datetime) -> bool:
        window_start = timestamp - timedelta(
            seconds=alert.alert_config.window_size_in_secs
        )
        events = [
            e
            for e in self.event_history
            if e.client == alert.client
            and e.type == alert.event_type
            and window_start <= e.timestamp <= timestamp
        ]
        return len(events) >= alert.alert_config.count

    # Trigger the alert and dispatch it
    def trigger_alert(self, alert: Alert):
        logger.info(
            f"MonitoringService: Client {alert.client} {alert.event_type} {logger.get_formatted_text('threshold breached', TextFormatType.BOLD)}"
        )
        DispatchService.dispatch(alert)
