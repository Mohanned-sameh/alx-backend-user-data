#!/usr/bin/env python3
"""
function that returns log message obfuscated
"""
from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str] = []):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        Returns log message obfuscated
        """
        record.message = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR
        )
        return logging.Formatter.format(self, record)


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Returns log message obfuscated
    """
    for field in fields:
        message = re.sub(
            rf"{field}=(.*?){separator}",
            f"{field}={redaction}{separator}",
            message,
        )
    return message
