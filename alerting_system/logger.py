from literals.enums import LogLevel, TextFormatType


class Logger:
    def __init__(self, name: str = None):
        self.name = name

    def log(self, level: LogLevel, message: str):
        level_str = ""
        match level:
            case LogLevel.INFO:
                level_str = f"\033[94m[{level}]\033[0m"  # Blue color
            case LogLevel.WARNING:
                level_str = f"\033[93m[{level}]\033[0m"  # Yellow color
            case LogLevel.ERROR:
                level_str = f"\033[91m[{level}]\033[0m"  # Red color
            case _:
                level_str = "[UNKNOWN]"

        print(f"{level_str} {message}")

    def info(self, message: str):
        self.log(LogLevel.INFO, message)

    def warning(self, message: str):
        self.log(LogLevel.WARNING, message)

    def error(self, message: str):
        self.log(LogLevel.ERROR, message)

    @staticmethod
    def get_formatted_text(text: str, format_type: TextFormatType) -> str:
        """
        Returns the formatted text based on the specified format type.
        Supported format types: 'bold', 'italic', 'underline', etc.
        """
        # Apply formatting based on the format_type
        match format_type:
            case TextFormatType.BOLD:
                return f"\033[1m{text}\033[0m"  # Apply bold formatting
            case TextFormatType.ITALIC:
                return f"\033[3m{text}\033[0m"  # Apply italic formatting
            case TextFormatType.UNDERLINE:
                return f"\033[4m{text}\033[0m"  # Apply underline formatting
            case _:
                return text  # Unsupported format type, return original text
