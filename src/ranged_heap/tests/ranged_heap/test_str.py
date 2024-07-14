from ranged_heap.ranged_heap import RangedHeap


def test_str(ranged_heap: RangedHeap, ranged_heap_str: str):
    """Test function to validate the string representation (__str__) of a RangedHeap object.

    Args:
        ranged_heap (RangedHeap): An instance of RangedHeap to test.
        ranged_heap_str (str): The expected string representation of the RangedHeap object.

    Raises:
        AssertionError: If the actual string representation of ranged_heap does not match
                        the expected ranged_heap_str.
    """
    def sorted_str(s):
        lines = s.strip().split("\n")
        sorted_lines = []
        for line in lines:
            if line.strip():  # Non-empty lines
                index_part, choices_part = line.split(" -> ")
                choices_sorted = " ".join(sorted(choices_part.strip("{}").split()))
                sorted_lines.append(f"{index_part} -> {{{choices_sorted}}}")
            else:  # Empty lines
                sorted_lines.append("")
        return "\n".join(sorted_lines)

    assert sorted_str(str(ranged_heap)) == sorted_str(ranged_heap_str)
