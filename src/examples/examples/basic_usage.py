from typing import List, Tuple
import ranged_heap as rh

def main():
    # Define a list of choices where each choice is a tuple (key, value)
    choices: List[Tuple[str, int]] = [
        ('choice1', 3),
        ('choice2', 1),
        ('choice3', 2),
        ('choice4', 3),
        ('choice5', 1)
    ]
    
    # Create a RangedHeap with range k and choices, setting min_ to True to get the lowest value
    k = 3
    ranged_heap = rh.RangedHeap(k, choices, min_=True)
    
    # Display the current state of the RangedHeap
    print("Initial RangedHeap state:")
    print(ranged_heap)
    
    # Get the best choice (lowest value in this case)
    best_choice = ranged_heap.get_best()
    print(f"The best choice is: {best_choice}")
    
    # Pop the best choice
    popped_choice = ranged_heap.pop_best()
    print(f"Popped the best choice: {popped_choice}")
    
    # Display the current state of the RangedHeap
    print("RangedHeap state after popping the best choice:")
    print(ranged_heap)
    
    # Add a new choice
    ranged_heap.add_choice('choice6', 0)
    print("RangedHeap state after adding a new choice (choice6, 0):")
    print(ranged_heap)
    
    # Adjust a choice's value
    ranged_heap.adjust_choice('choice4', 3, 1)
    print("RangedHeap state after adjusting choice4's value from 3 to 1:")
    print(ranged_heap)
    
    # Delete a choice
    ranged_heap.delete_choice('choice4', 1)
    print("RangedHeap state after deleting choice2 with value 1:")
    print(ranged_heap)
    
    # Display the final size of the RangedHeap
    print(f"Final size of the RangedHeap: {len(ranged_heap)}")

if __name__ == "__main__":
    main()
