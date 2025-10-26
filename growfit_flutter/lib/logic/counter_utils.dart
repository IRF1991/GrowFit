/// Utility functions for handling counters in GrowFit (Dart version).

int incrementCounter(int counter) => counter + 1;

int reduceCounter(int counter) => counter > 0 ? counter - 1 : 0;

Future<int> countDown(int counter, {Function(int)? onTick}) async {
  while (counter > 0) {
    await Future.delayed(const Duration(seconds: 1));
    counter--;
    if (onTick != null) onTick(counter);
  }
  return 0;
}
