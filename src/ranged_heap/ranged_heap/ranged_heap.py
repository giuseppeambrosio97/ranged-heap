"""
    This module contains the implementation of RangedHeap data structure.
"""

from typing import Any, List, Tuple, Set


class RangedHeap:

    def __init__(self, k: int, choices: List[Tuple[Any, int]], min_: bool = True):
        """
        Args:
            k (int): is a positive integer that indicated the range of value
                     a generic choice can have
            choices (List[Any, int]): list of pairs where each in each pair:
                                    - First element is a key associated with the choice
                                    - Second element is a value associated with the choice
            min_ (bool, optional): If True getBest() take the key with the lowest value,
                                  if False take the largest.
                                  Defaults to True:bool.
        """
        if k < 0:
            raise ValueError("k must be greater or equal to 0")

        self.best_id = 0 if min_ else -1

        self.size = len(choices)
        self.ranged: List[Set] = [set() for _ in range(k+1)]
        self.actual_value_ranged = []

        for choice in choices:
            self.ranged[choice[1]].add(choice[0])

        for id, choices_id in enumerate(self.ranged):
            if choices_id:
                self.actual_value_ranged.append(id)

    def pop_best(self) -> Any:
        if self.size >= 1:
            choice_to_pick = self._pop_best_twins()
            self.size -= 1
            if not self.ranged[self.actual_value_ranged[self.best_id]]:
                del self.actual_value_ranged[self.best_id]
            return choice_to_pick
        
        raise RuntimeError('The Ranged Heap is empty!')

    def _pop_best_twins(self) -> Any:       
        choice_to_pick = list(
            self.ranged[self.actual_value_ranged[self.best_id]])[0]
        self.ranged[self.actual_value_ranged[self.best_id]].remove(
            choice_to_pick)
        return choice_to_pick

    def get_best(self) -> Any:
        if self.size >= 1:
            choice_to_pick = self._get_best_twins()
            return choice_to_pick
        
        raise RuntimeError('The Ranged Heap is empty!')

    def _get_best_twins(self) -> Any:    
        choice_to_pick = list(
            self.ranged[self.actual_value_ranged[self.best_id]])[0]
        return choice_to_pick

    def delete_choice(self, key: Any, value: int):      
        self.ranged[value].remove(key)
        self.size -= 1

        if not self.ranged[value]:
            self.__binary_search_delete(value)

    def add_choice(self, key: Any, value: int):     
        if not self.ranged[value]:
            self.__binary_search_add(value)
        self.ranged[value].add(key)
        self.size += 1

    def adjust_choice(self, key: Any, old_value: int, new_value: int):       
        self.ranged[old_value].remove(key)

        if not self.ranged[old_value]:
            self.__binary_search_delete(old_value)

        if not self.ranged[new_value]:
            self.__binary_search_add(new_value)
        self.ranged[new_value].add(key)

    def __binary_search_delete(self, x: int):      
        l = 0
        r = len(self.actual_value_ranged)-1

        while l <= r:
            c = (l + r) // 2
            if self.actual_value_ranged[c] == x:
                break
            elif self.actual_value_ranged[c] < x:
                l = c + 1
            else:
                r = c - 1
        del self.actual_value_ranged[c]

    def __binary_search_add(self, x: int):      
        if len(self.actual_value_ranged) == 0:
            self.actual_value_ranged.append(x)
        elif x < self.actual_value_ranged[0]:
            self.actual_value_ranged.insert(0, x)
        elif x > self.actual_value_ranged[-1]:
            self.actual_value_ranged.append(x)
        else:
            l = 0
            r = len(self.actual_value_ranged)-1

            while l <= r:
                c = (l + r) // 2
                if self.actual_value_ranged[c] < x:
                    if x < self.actual_value_ranged[c+1]:
                        break
                    else:
                        l = c + 1
                else:
                    r = c - 1
            self.actual_value_ranged.insert(c+1, x)

    def __str__(self):
        s = ''
        for id, choice_per_value in enumerate(self.ranged):
            choices_key = ''
            for choice in choice_per_value:
                choices_key += ' ' + str(choice)
            s += '[' + str(id) + ']->' + choices_key + '\n'
        return s

    def __len__(self):
        return self.size
