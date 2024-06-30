def get_bold(text: str) -> str:
    return f"\033[1m{text}\033[0m"


def get_warn_color(text: str) -> str:
    return f"\033[93m{text}\033[0m"  # Yellow color


def get_error_color(text: str) -> str:
    return f"\033[91m{text}\033[0m"  # Red color


def get_info_color(text: str) -> str:
    return f"\033[94m{text}\033[0m"  # Blue color
