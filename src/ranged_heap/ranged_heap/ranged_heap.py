"""Implementation of the RangedHeap data structure."""

from typing import Any, List, Set, Tuple

from .bisectw import bs_add, bs_delete
from .errors import (
    ChoiceNotFoundError,
    EmptyHeapError,
    InvalidChoiceError,
    InvalidRangeError,
)


class RangedHeap:
    """RangedHeap is a data structure that maintains a collection of choices associated with integer values within a specified range.

    Attributes:
        k (int): The range of values a choice can have.
        best_id (int): Index indicating whether to return the min or max value choice.
        size (int): Number of choices currently in the heap.
        ranged (List[Set]): List of sets where each set contains choices for a specific value.
        actual_value_ranged (List): List of actual values present in the heap.

    Methods:
        __init__(self, k: int, choices: List[Tuple[Any, int]], min_: bool = True):
            Initializes a RangedHeap instance.

        pop_best(self) -> Any:
            Removes and returns the best choice from the heap.

        _pop_best_twins(self) -> Any:
            Helper method to remove and return the best choice.

        get_best(self) -> Any:
            Returns the best choice from the heap without removing it.

        _get_best_twins(self) -> Any:
            Helper method to return the best choice without removing it.

        delete_choice(self, key: Any, value: int) -> None:
            Deletes a specific choice from the heap.

        add_choice(self, key: Any, value: int) -> None:
            Adds a new choice to the heap.

        adjust_choice(self, key: Any, old_value: int, new_value: int) -> None:
            Adjusts the value of an existing choice in the heap.

        __is_invalid_choice(self, value: int) -> bool:
            Checks if a value is invalid.

        __str__(self) -> str:
            Returns a string representation of the heap.

        __len__(self) -> int:
            Returns the number of choices in the heap.
    """

    def __init__(self, k: int, choices: List[Tuple[Any, int]], min_: bool = True):
        """Initialize a RangedHeap.

        Args:
            k (int): A positive integer indicating the range of values a choice can have.
            choices (List[Tuple[Any, int]]): A list of pairs where each pair contains:
                - A key associated with the choice (Any).
                - A value associated with the choice (int).
            min_ (bool, optional): If True, get_best() will return the key with the lowest value.
                                   If False, get_best() will return the key with the highest value.
                                   Defaults to True.
        """
        if k < 0:
            raise InvalidRangeError()

        self.k = k
        self.best_id = 0 if min_ else -1
        self.size = len(choices)
        self.ranged: List[Set] = [set() for _ in range(k + 1)]
        self.actual_value_ranged = []

        for choice in choices:
            self.ranged[choice[1]].add(choice[0])

        for idx, choices_id in enumerate(self.ranged):
            if choices_id:
                self.actual_value_ranged.append(idx)

    def pop_best(self) -> Any:
        """Remove and return the best choice from the heap.

        Returns:
            Any: The key of the best choice.

        Raises:
            EmptyHeapError: If the heap is empty.
        """
        if self.size >= 1:
            choice_to_pick = self._pop_best_twins()
            self.size -= 1
            if not self.ranged[self.actual_value_ranged[self.best_id]]:
                del self.actual_value_ranged[self.best_id]
            return choice_to_pick

        raise EmptyHeapError()

    def _pop_best_twins(self) -> Any:
        """Helper method to remove and return the best choice.

        Returns:
            Any: The key of the best choice.
        """
        choice_to_pick = list(self.ranged[self.actual_value_ranged[self.best_id]])[0]
        self.ranged[self.actual_value_ranged[self.best_id]].remove(choice_to_pick)
        return choice_to_pick

    def get_best(self) -> Any:
        """Return the best choice from the heap without removing it.

        Returns:
            Any: The key of the best choice.

        Raises:
            EmptyHeapError: If the heap is empty.
        """
        if self.size >= 1:
            return self._get_best_twins()

        raise EmptyHeapError()

    def _get_best_twins(self) -> Any:
        """Helper method to return the best choice without removing it.

        Returns:
            Any: The key of the best choice.
        """
        return list(self.ranged[self.actual_value_ranged[self.best_id]])[0]

    def delete_choice(self, key: Any, value: int) -> None:
        """Delete a specific choice from the heap.

        Args:
            key (Any): The key of the choice to be deleted.
            value (int): The value associated with the choice.

        Raises:
            InvalidChoiceError: If the value is invalid.
            ChoiceNotFoundError: If the choice is not found in the heap.
        """
        if self.__is_invalid_choice(value):
            raise InvalidChoiceError(value=value)

        if key not in self.ranged[value]:
            raise ChoiceNotFoundError(key, value)

        self.ranged[value].remove(key)
        self.size -= 1

        if not self.ranged[value]:
            bs_delete(self.actual_value_ranged, value)

    def add_choice(self, key: Any, value: int) -> None:
        """Add a new choice to the heap.

        Args:
            key (Any): The key of the choice to be added.
            value (int): The value associated with the choice.

        Raises:
            InvalidChoiceError: If the value is invalid.
        """
        if self.__is_invalid_choice(value):
            raise InvalidChoiceError(value=value)

        if not self.ranged[value]:
            bs_add(self.actual_value_ranged, value)
        self.ranged[value].add(key)
        self.size += 1

    def adjust_choice(self, key: Any, old_value: int, new_value: int) -> None:
        """Adjust the value of an existing choice in the heap.

        Args:
            key (Any): The key of the choice to be adjusted.
            old_value (int): The current value of the choice.
            new_value (int): The new value to be assigned to the choice.

        Raises:
            InvalidChoiceError: If either old_value or new_value is invalid.
            ChoiceNotFoundError: If the choice is not found in the heap.
        """
        if self.__is_invalid_choice(old_value):
            raise InvalidChoiceError(value=old_value)

        if self.__is_invalid_choice(new_value):
            raise InvalidChoiceError(value=new_value)

        if key not in self.ranged[old_value]:
            raise ChoiceNotFoundError(key, old_value)

        self.ranged[old_value].remove(key)

        bs_delete(self.actual_value_ranged, old_value)

        if not self.ranged[new_value]:
            bs_add(self.actual_value_ranged, new_value)
        self.ranged[new_value].add(key)

    def __is_invalid_choice(self, value: int) -> bool:
        """Check if a value is invalid.

        Args:
            value (int): The value to check.

        Returns:
            bool: True if the value is invalid, False otherwise.
        """
        return value < 0 or value > self.k

    def __str__(self) -> str:
        """Return a string representation of the heap.

        Returns:
            str: String representation of the heap.
        """
        s = ""
        for idx, choices_per_value in enumerate(self.ranged):
            choices_key = " ".join(choices_per_value)
            s += f"[{idx}] -> {{{choices_key}}}\n"
        return s

    def __len__(self) -> int:
        """Return the number of choices in the heap.

        Returns:
            int: The number of choices in the heap.
        """
        return self.size
