# Counter utility functions

def increment_counter(counter):
    """Increment the given counter by 1."""
    return counter + 1

def reduce_counter(counter):
    """Decrement the given counter by 1, ensuring it doesn't go below 0."""
    if counter <= 0:
        return 0
    return counter - 1