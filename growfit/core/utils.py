# Counter utility functions

def increment_counter(counter):
    """Increment the given counter by 1."""
    return counter + 1

def reduce_counter(counter):
    """Decrement the given counter by 1, ensuring it doesn't go below 0."""
    if counter <= 0:
        return 0
    return counter - 1

def count_down(counter):
    """Count down the last counter by 1 every second until it reaches 0.
        It will be used to manage the countdown timer during exercises, rest between sets and timers.
    """
    while counter > 0:
        counter = reduce_counter(counter)
        yield counter