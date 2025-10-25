// Pantalla RoutineScreen migrada desde Kivy

import 'package:flutter/material.dart';

/// Pantalla de detalles de rutina.
/// (Pendiente de implementar lógica y UI).
class RoutineScreen extends StatelessWidget {
  const RoutineScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Routine')), 
      body: const Center(
        child: Text(
          'Routine Screen (to be implemented)',
          style: TextStyle(fontSize: 22),
        ),
      ),
    );
  }
}
