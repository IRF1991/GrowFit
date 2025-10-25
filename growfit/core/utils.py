"""
Simple and useful functions for handling counters in GrowFit.
These functions help you add, subtract, and count down easily.
"""

def increment_counter(counter):
    """Adds 1 to the counter."""
    return counter + 1

def reduce_counter(counter):
    """Subtracts 1 from the counter, but never goes below 0."""
    return max(0, counter - 1)

def count_down(counter):
    """Counts down from the given value to 0."""
    import time
    while counter > 0:
        time.sleep(1)
        counter -= 1
    return 0