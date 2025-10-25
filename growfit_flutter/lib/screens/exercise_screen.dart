// Pantalla ExerciseScreen migrada desde Kivy

import 'package:flutter/material.dart';

/// Pantalla de detalles de ejercicio.
/// (Pendiente de implementar lógica y UI).
class ExerciseScreen extends StatelessWidget {
  const ExerciseScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Exercise')), 
      body: const Center(
        child: Text(
          'Exercise Screen (to be implemented)',
          style: TextStyle(fontSize: 22),
        ),
      ),
    );
  }
}
