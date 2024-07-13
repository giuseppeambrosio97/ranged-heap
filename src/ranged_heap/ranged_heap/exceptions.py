import abc
from typing import Optional


class RangedHeapBaseException(abc.ABC, Exception):
    """Base class for other exceptions with default error message."""

    default_message: str = "An error occurred."

    def __init__(self, message: Optional[str] = None, **kwargs):
        if message is None:
            message = self.default_message.format(**kwargs)
        super().__init__(message)


class InvalidRangeError(RangedHeapBaseException):
    """Raised when the range k is less than 0."""

    default_message: str = "k must be greater or equal to 0."


class EmptyHeapError(RangedHeapBaseException):
    """Raised when trying to pop or get the best choice from an empty heap."""

    default_message: str = "The Ranged Heap is empty!"


class ChoiceNotFoundError(RangedHeapBaseException):
    """Raised when attempting to delete a choice that doesn't exist in the specified value range."""

    default_message: str = "Choice {key} not found in value {value}."

    def __init__(self, key: str, value: int, message: Optional[str] = None):
        super().__init__(message, key=key, value=value)


class InvalidChoiceError(RangedHeapBaseException):
    """Raised when attempting to add or adjust a choice with an invalid value (out of range)."""

    default_message: str = "Value {value} is out of range."

    def __init__(self, value: int, message: Optional[str] = None):
        super().__init__(message, value=value)
