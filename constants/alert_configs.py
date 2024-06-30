from config.config import Alert, AlertConfig, DispatchStrategy
from alerting_system.logger import Logger
from literals.enums import AlertType, EventType, DispatchType, TextFormatType
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

logger = Logger()
ALERT_CONFIGS = [
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
                type=DispatchType.CONSOLE,
                message=logger.get_formatted_text(
                    PAYMENT_EXCEPTION_CONSOLE_MESSAGE, TextFormatType.BOLD
                ),
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
                message=logger.get_formatted_text(
                    USERSERVICE_EXCEPTION_CONSOLE_MESSAGE, TextFormatType.BOLD
                ),
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
                type=DispatchType.CONSOLE,
                message=logger.get_formatted_text(
                    LOGIN_FAILURE_CONSOLE_MESSAGE, TextFormatType.BOLD
                ),
            ),
            DispatchStrategy(
                type=DispatchType.EMAIL,
                subject=LOGIN_FAILURE_EMAIL_SUBJECT,
                message=LOGIN_FAILURE_EMAIL_MESSAGE,
            ),
        ],
    ),
]
