from alerting_system.config import Alert
from literals.enums import DispatchType
from utils.logs_formatter import get_bold, get_info_color, get_warn_color


# Service to handle dispatching alerts based on different strategies
class DispatchService:
    @staticmethod
    def dispatch(alert: Alert):
        for strategy in alert.dispatch_strategy_list:
            dispatch_type = strategy.type
            match dispatch_type:
                case DispatchType.CONSOLE:
                    ConsoleDispatch.dispatch(strategy.message)
                case DispatchType.EMAIL:
                    EmailDispatch.dispatch(strategy.subject, strategy.message)


# Class to handle console dispatching of alerts
class ConsoleDispatch:
    @staticmethod
    def dispatch(message: str):
        print(f"{get_info_color('[INFO]')} AlertingService: Dispatching to Console")
        print(f"{get_warn_color('[WARN]')} Alert: `{message}`")


# Class to handle email dispatching of alerts
class EmailDispatch:
    @staticmethod
    def dispatch(subject: str, message: str):
        print(
            f"{get_info_color('[INFO]')} AlertingService: {get_bold('Dispatching an Email')}\nSubject: {subject}\nMessage: {message}"
        )
