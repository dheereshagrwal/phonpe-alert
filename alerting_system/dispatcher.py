from config.config import Alert
from alerting_system.logger import Logger
from literals.enums import DispatchType, TextFormatType

logger = Logger()


class DispatchService:
    _instance = None

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

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def dispatch(alert: Alert):
        for strategy in alert.dispatch_strategy_list:
            dispatch_type = strategy.type
            match dispatch_type:
                case DispatchType.CONSOLE:
                    DispatchService.ConsoleDispatch.dispatch(strategy.message)
                case DispatchType.EMAIL:
                    DispatchService.EmailDispatch.dispatch(
                        strategy.subject, strategy.message
                    )
                case _:
                    raise NotImplementedError(
                        f"Dispatch type {dispatch_type} not implemented"
                    )
