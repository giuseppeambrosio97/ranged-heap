# Quickstart

Here’s a quick example to get you started with RangedHeap.

From the ranged_heap module you can import the RangedHeap class, like:

```python
import ranged_heap as rh

rh.RangedHeap
```

## Init the RangedHeap

```python
# Define the range and initial choices
k = 10  # Range of values (0 to 10)
choices = [("choice1", 5), ("choice2", 3), ("choice3", 8)]

# Initialize the RangedHeap
heap = rh.RangedHeap(k, choices, min_=True)
```

## Add a new choice

```python
heap.add_choice("choice4", 7)
```

## Get the best choice

```python
best_choice = heap.get_best()
print(f"The best choice is: {best_choice}")
```

## Pop the best choice

```python
best_choice = heap.pop_best()
print(f"The best choice popped is: {best_choice}")
```

## Delete a choice

```python
heap.delete_choice("choice4", 7)
```

## Adjust the value of a choice

```python
heap.adjust_choice("choice1", 5, 2)
```

## Check the RangedHeap size

```python
size = len(heap)
print(f"The number of choices in the heap is: {size}")
```
