from alerting_system.config import Alert
from alerting_system.logger import Logger
from literals.enums import DispatchType, TextFormatType

logger = Logger()


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
        logger.info("AlertingService: Dispatching to Console")
        logger.warning(f"Alert: {message}")


# Class to handle email dispatching of alerts
class EmailDispatch:
    @staticmethod
    def dispatch(subject: str, message: str):
        logger.info(
            f"AlertingService: {logger.get_formatted_text('Dispatching an Email', TextFormatType.BOLD)}\nSubject: {subject}\nMessage: {message}"
        )
