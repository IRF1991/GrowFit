import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart';
import 'package:growfit_flutter/data_management/device_id_manager.dart';

class DeveloperToolsScreen extends StatefulWidget {
  const DeveloperToolsScreen({Key? key}) : super(key: key);

  @override
  State<DeveloperToolsScreen> createState() => _DeveloperToolsScreenState();
}

class _DeveloperToolsScreenState extends State<DeveloperToolsScreen> {
  String? _deviceId;
  String? _deviceIdPath;
  String _status = '';

  Future<void> _loadDeviceId() async {
    final id = await DeviceIdManager.getDeviceId();
    setState(() {
      _deviceId = id;
      _status = 'Device ID cargado';
    });
  }

  Future<void> _deleteDeviceId() async {
    final path = await DeviceIdManager.deleteDeviceId();
    setState(() {
      _deviceId = null;
      _deviceIdPath = path;
      _status = 'device_id.txt borrado';
    });
  }

  Future<void> _regenerateDeviceId() async {
    final id = await DeviceIdManager.getDeviceId();
    setState(() {
      _deviceId = id;
      _status = 'Device ID regenerado';
    });
  }

  @override
  void initState() {
    super.initState();
    _loadDeviceId();
  }

  @override
  Widget build(BuildContext context) {
    if (!kDebugMode) {
      return const SizedBox.shrink();
    }
    return Scaffold(
      appBar: AppBar(title: const Text('Developer Tools')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Device ID: ${_deviceId ?? "(no existe)"}'),
            const SizedBox(height: 8),
            if (_deviceIdPath != null) Text('Ruta: $_deviceIdPath'),
            const SizedBox(height: 16),
            Row(
              children: [
                Expanded(
                  child: ElevatedButton(
                    onPressed: _deleteDeviceId,
                    child: const Text('Borrar device_id.txt'),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: ElevatedButton(
                    onPressed: _regenerateDeviceId,
                    child: const Text('Regenerar device_id'),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 16),
            Text(_status),
          ],
        ),
      ),
    );
  }
}
