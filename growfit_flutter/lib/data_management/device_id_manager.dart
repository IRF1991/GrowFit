import 'dart:math';
import 'dart:io';
import 'package:flutter/foundation.dart';
import 'package:path_provider/path_provider.dart';

/// Utility to manage and persist a unique device_id for GrowFit.
/// The device_id follows the format: 'us_xxxxxxxx' (user) or 'te_xxxxxxxx' (testing)
class DeviceIdManager {
  /// DEV MODE ONLY
  /// Borra el archivo device_id.txt y devuelve la ruta borrada (o null si no existía)
  static Future<String?> deleteDeviceId() async {
    final dir = await getApplicationDocumentsDirectory();
    final file = File('${dir.path}/$_fileName');
    if (await file.exists()) {
      await file.delete();
      print('[DeviceIdManager] device_id.txt borrado en: ${file.path}');
      return file.path;
    }
    return null;
  }
  static const _fileName = 'device_id.txt';

  /// USER MODE
  /// Generates a device_id with the given prefix ('us' or 'te').
  static String _generateDeviceId({bool isTesting = false}) {
    final prefix = isTesting ? 'te' : 'us';
    final random = Random();
    final id = List.generate(8, (_) => random.nextInt(16).toRadixString(16)).join();
    return '${prefix}_$id';
  }

  /// Returns the device_id: reads from file if it exists, or generates and saves a new one if not.
  /// Returns the device_id: reads from file if it exists, or generates and saves a new one if not.
  /// Automatically uses 'te_' prefix in debug mode, 'us_' in release mode.
  static Future<String> getDeviceId() async {
    final dir = await getApplicationDocumentsDirectory();
    final file = File('${dir.path}/$_fileName');
    print('[DeviceIdManager] Intentando acceder a: \'${file.path}\'');
    if (await file.exists()) {
      final id = await file.readAsString();
  print('[DeviceIdManager] Leído device_id: $id');
  print('[DeviceIdManager] Ruta real: ${file.path}');
      if (id.trim().isNotEmpty) {
        return id.trim();
      }
    }
    final isTesting = kDebugMode;
    final newId = _generateDeviceId(isTesting: isTesting);
    await file.writeAsString(newId);
  print('[DeviceIdManager] Generado y guardado device_id: $newId');
  print('[DeviceIdManager] Ruta real: ${file.path}');
    return newId;
  }
}
