import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart';
import 'package:growfit_flutter/dev_screens/developer_tools_screen.dart';

/// Pantalla principal (HOME).
/// Muestra el título y un botón para crear una nueva rutina.
class MainScreen extends StatelessWidget {
  const MainScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('HOME')),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Text(
              'HOME',
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 40),
            ),
            const SizedBox(height: 40),
            ElevatedButton(
              onPressed: () {
                // Aquí iría la lógica de crear usuario si es necesario, en Flutter se haría diferente
                Navigator.pushNamed(context, '/new_routine');
              },
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 24),
                textStyle: const TextStyle(fontSize: 20),
              ),
              child: const Text('New Routine'),
            ),
            if (kDebugMode) ...[
              const SizedBox(height: 24),
              ElevatedButton(
                onPressed: () {
                  Navigator.of(context).push(
                    MaterialPageRoute(
                      builder: (_) => const DeveloperToolsScreen(),
                    ),
                  );
                },
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.deepPurple,
                  padding: const EdgeInsets.symmetric(vertical: 20),
                  textStyle: const TextStyle(fontSize: 18),
                ),
                child: const Text('DEV MODE'),
              ),
            ],
            // ...existing code...
          ],
        ),
      ),
    );
  }
}
