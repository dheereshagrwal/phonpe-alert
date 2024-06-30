from collections import deque
from datetime import datetime
from alerting_system.event import Event
from alerting_system.monitoring import MonitoringService
from literals.counts import (
    LOGIN_FAILURE_COUNT,
    PAYMENT_EXCEPTION_COUNT,
    USERSERVICE_EXCEPTION_COUNT,
)
from literals.enums import EventType


def main():
    # Initialize monitoring service
    monitoring_service = MonitoringService()

    # Initialize a deque for events
    events = deque()

    # Generate PAYMENT_EXCEPTION events for client X
    for _ in range(PAYMENT_EXCEPTION_COUNT):
        events.append(
            Event(
                client="X", type=EventType.PAYMENT_EXCEPTION, timestamp=datetime.now()
            )
        )

    # Generate USERSERVICE_EXCEPTION events for client X
    for _ in range(USERSERVICE_EXCEPTION_COUNT):
        events.append(
            Event(
                client="X",
                type=EventType.USERSERVICE_EXCEPTION,
                timestamp=datetime.now(),
            )
        )

    # Generate LOGIN_FAILURE events for client Y
    for _ in range(LOGIN_FAILURE_COUNT):
        events.append(
            Event(client="Y", type=EventType.LOGIN_FAILURE, timestamp=datetime.now())
        )

    # Process each event
    while events:
        event = events.popleft()
        monitoring_service.monitor_event(event)


if __name__ == "__main__":
    main()
