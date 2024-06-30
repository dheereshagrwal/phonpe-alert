from utils.logs_formatter import get_bold


PAYMENT_EXCEPTION_CONSOLE_MESSAGE = get_bold("issue in payment")
PAYMENT_EXCEPTION_EMAIL_SUBJECT = "payment exception threshold breached"
PAYMENT_EXCEPTION_EMAIL_MESSAGE = "Threshold breached for payment exceptions"

USERSERVICE_EXCEPTION_CONSOLE_MESSAGE = get_bold("issue in user service")
USERSERVICE_EXCEPTION_EMAIL_SUBJECT = "user service exception threshold breached"
USERSERVICE_EXCEPTION_EMAIL_MESSAGE = "Threshold breached for user service exceptions"

LOGIN_FAILURE_CONSOLE_MESSAGE = get_bold("too many login failures")
LOGIN_FAILURE_EMAIL_SUBJECT = "login failure threshold breached"
LOGIN_FAILURE_EMAIL_MESSAGE = "Too many login failures"
