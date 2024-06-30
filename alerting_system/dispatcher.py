from alerting_system.config import Alert
from alerting_system.logger import Logger
from literals.enums import DispatchType, TextFormatType

logger = Logger()


class DispatchService:
    class ConsoleDispatch:
        @staticmethod
        def dispatch(message: str):
            logger.info(
                f"AlertingService: {logger.get_formatted_text('Dispatching to Console', TextFormatType.BOLD)}"
            )
            logger.warning(f"Alert: {message}")

    class EmailDispatch:
        @staticmethod
        def dispatch(subject: str, message: str):
            logger.info(
                f"AlertingService: {logger.get_formatted_text('Dispatching an Email', TextFormatType.BOLD)}\nSubject: {subject}\nMessage: {message}"
            )

    @staticmethod
    def dispatch(alert: Alert):
        for strategy in alert.dispatch_strategy_list:
            dispatch_type = strategy.type
            if dispatch_type == DispatchType.CONSOLE:
                DispatchService.ConsoleDispatch.dispatch(strategy.message)
            elif dispatch_type == DispatchType.EMAIL:
                DispatchService.EmailDispatch.dispatch(
                    strategy.subject, strategy.message
                )
