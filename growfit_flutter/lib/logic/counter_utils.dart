
/// Utility functions for handling counters in GrowFit.
/// Provides increment, decrement, and countdown logic for integer counters.
library;

/// Increments the given counter by 1.
int incrementCounter(int counter) => counter + 1;

/// Decrements the given counter by 1, but not below 0.
int reduceCounter(int counter) => counter > 0 ? counter - 1 : 0;

/// Asynchronously counts down from the given counter to 0, calling [onTick] on each tick.
Future<int> countDown(int counter, {Function(int)? onTick}) async {
  while (counter > 0) {
    await Future.delayed(const Duration(seconds: 1));
    counter--;
    if (onTick != null) onTick(counter);
  }
  return 0;
}
