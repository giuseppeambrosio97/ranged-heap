# RangedHeap

Welcome to the RangedHeap documentation! This documentation provides an overview of the RangedHeap data structure, its methods, and examples of its usage.

For more details, please refer to the [documentation](https://giuseppeambrosio97.github.io/ranged-heap/).

## What is RangedHeap?

RangedHeap is a data structure designed to manage a collection of choices associated with integer values within a specified range [0, k]. It supports efficient operations for adding, deleting, and retrieving choices based on their integer values.

## Features

- **Efficient Choice Management**: Manage choices efficiently within a specified integer range.
- **Dynamic Updates**: Support dynamic updates to the heap as choices change.
- **Optimized Retrieval**: Quickly retrieve the best choice based on specified criteria (minimum or maximum).

## How to Use

The RangedHeap is particularly useful for implementing algorithms that require optimal selection from a set of integer-ranged choices, such as greedy algorithms.

### Example Usage

```python
import ranged_heap as rh

choices = [(1, 4), (2, 3), (3, 5), (0, 6), (5, 7), (8, 9)]
k = max(end for _, end in choices)
ranged_heap = rh.RangedHeap(k, choices)
```
