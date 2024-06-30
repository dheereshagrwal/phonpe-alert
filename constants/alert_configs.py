from alerting_system.config import Alert, AlertConfig, DispatchStrategy
from literals.enums import AlertType, EventType, DispatchType
from literals.counts import (
    LOGIN_FAILURE_COUNT,
    PAYMENT_EXCEPTION_COUNT,
    PAYMENT_EXCEPTION_WINDOW_SIZE,
    USERSERVICE_EXCEPTION_COUNT,
    USERSERVICE_EXCEPTION_WINDOW_SIZE,
)
from literals.messages import (
    LOGIN_FAILURE_CONSOLE_MESSAGE,
    LOGIN_FAILURE_EMAIL_MESSAGE,
    LOGIN_FAILURE_EMAIL_SUBJECT,
    PAYMENT_EXCEPTION_CONSOLE_MESSAGE,
    PAYMENT_EXCEPTION_EMAIL_MESSAGE,
    PAYMENT_EXCEPTION_EMAIL_SUBJECT,
    USERSERVICE_EXCEPTION_CONSOLE_MESSAGE,
    USERSERVICE_EXCEPTION_EMAIL_MESSAGE,
    USERSERVICE_EXCEPTION_EMAIL_SUBJECT,
)

alert_configs = [
    Alert(
        client="X",
        event_type=EventType.PAYMENT_EXCEPTION,
        alert_config=AlertConfig(
            type=AlertType.TUMBLING_WINDOW,
            count=PAYMENT_EXCEPTION_COUNT,
            window_size_in_secs=PAYMENT_EXCEPTION_WINDOW_SIZE,
        ),
        dispatch_strategy_list=[
            DispatchStrategy(
                type=DispatchType.CONSOLE, message=PAYMENT_EXCEPTION_CONSOLE_MESSAGE
            ),
            DispatchStrategy(
                type=DispatchType.EMAIL,
                subject=PAYMENT_EXCEPTION_EMAIL_SUBJECT,
                message=PAYMENT_EXCEPTION_EMAIL_MESSAGE,
            ),
        ],
    ),
    Alert(
        client="X",
        event_type=EventType.USERSERVICE_EXCEPTION,
        alert_config=AlertConfig(
            type=AlertType.SLIDING_WINDOW,
            count=USERSERVICE_EXCEPTION_COUNT,
            window_size_in_secs=USERSERVICE_EXCEPTION_WINDOW_SIZE,
        ),
        dispatch_strategy_list=[
            DispatchStrategy(
                type=DispatchType.CONSOLE,
                message=USERSERVICE_EXCEPTION_CONSOLE_MESSAGE,
            ),
            DispatchStrategy(
                type=DispatchType.EMAIL,
                subject=USERSERVICE_EXCEPTION_EMAIL_SUBJECT,
                message=USERSERVICE_EXCEPTION_EMAIL_MESSAGE,
            ),
        ],
    ),
    Alert(
        client="Y",
        event_type=EventType.LOGIN_FAILURE,
        alert_config=AlertConfig(
            type=AlertType.SIMPLE_COUNT, count=LOGIN_FAILURE_COUNT
        ),
        dispatch_strategy_list=[
            DispatchStrategy(
                type=DispatchType.CONSOLE, message=LOGIN_FAILURE_CONSOLE_MESSAGE
            ),
            DispatchStrategy(
                type=DispatchType.EMAIL,
                subject=LOGIN_FAILURE_EMAIL_SUBJECT,
                message=LOGIN_FAILURE_EMAIL_MESSAGE,
            ),
        ],
    ),
]
