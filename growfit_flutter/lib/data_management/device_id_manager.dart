import 'dart:math';

/// Utility to generate a unique device_id for GrowFit.
/// Follows the format: 'us_xxxxxxxx' (user) or 'te_xxxxxxxx' (testing)
class DeviceIdManager {
  /// Generates a device_id with the given prefix ('us' or 'te').
  static String generateDeviceId({bool isTesting = false}) {
    final prefix = isTesting ? 'te' : 'us';
    final random = Random();
    final id = List.generate(8, (_) => random.nextInt(16).toRadixString(16)).join();
    return '${prefix}_$id';
  }
}
