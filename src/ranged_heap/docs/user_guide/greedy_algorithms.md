# Greedy Algorithms

Greedy algorithms build up a solution piece by piece, always choosing the next piece that offers the most immediate benefit. This local optimal choice is the hallmark of greedy algorithms. Some common examples of greedy algorithms include:

- Activity Selection Problem
- Fractional Knapsack Problem
- Prim’s Minimum Spanning Tree
- Dijkstra’s Shortest Path

## Why RangedHeap?

The RangedHeap data structure provides an efficient way to handle choices with integer values in the range [0, k]. It offers the following benefits that align well with the needs of greedy algorithms:

- Efficient Retrieval of Best Choice: The get_best() and pop_best() methods allow for quick retrieval of the minimum or maximum choice, which is essential for making the best local decision in greedy algorithms.
- Dynamic Updates: The add_choice(), delete_choice(), and adjust_choice() methods enable dynamic updates to the heap, which is necessary when the set of choices changes during the execution of the algorithm.
- Range Constraints: By constraining the choices to a specific range, RangedHeap ensures that the algorithm operates within the defined bounds, making it more efficient and easier to manage and optimize.

### Example: Activity Selection Problem

The activity selection problem is a classic example where greedy algorithms are used. The goal is to select the maximum number of activities that don't overlap. Given a set of activities with start and end times, the greedy choice is to always pick the next activity that ends the earliest.

#### Using RangedHeap

Here's how the RangedHeap can be used to solve the activity selection problem:

- Initialization: Create a RangedHeap with the end times of activities.
- Add Activities: Add each activity to the heap with its end time as the key.
- Select Activities: Use the pop_best() method to repeatedly select the activity with the earliest end time that doesn't overlap with the previously selected activity.

```python
activities = [(1, 4), (2, 3), (3, 5), (0, 6), (5, 7), (8, 9)]
k = max(end for _, end in activities)
ranged_heap = RangedHeap(k, [(i, end) for i, (_, end) in enumerate(activities)])

selected_activities = []
last_end_time = -1

while len(ranged_heap) > 0:
    best_activity_idx = ranged_heap.pop_best()
    start, end = activities[best_activity_idx]
    if start >= last_end_time:
        selected_activities.append((start, end))
        last_end_time = end

print("Selected activities:", selected_activities)
```

## Conclusion

The RangedHeap data structure is a powerful tool for implementing greedy algorithms when the choices are constrained to integer values within a specific range. Its efficient methods for adding, deleting, and retrieving the best choices make it particularly suitable for problems where the set of choices dynamically changes. By leveraging RangedHeap, one can implement optimized and efficient greedy solutions for a variety of problems.

## References

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to Algorithms. MIT Press.
- Kleinberg, J., & Tardos, É. (2005). Algorithm Design. Pearson.

By understanding and utilizing the RangedHeap, developers can enhance their implementation of greedy algorithms, leading to more efficient and effective solutions.
