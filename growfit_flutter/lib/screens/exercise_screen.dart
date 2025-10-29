// Pantalla ExerciseScreen migrada desde Kivy

import 'package:flutter/material.dart';

/// Screen to view and edit an exercise.
/// (Logic and UI pending implementation.)
class ExerciseScreen extends StatelessWidget {
  const ExerciseScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Exercise')), 
      body: const Center(
        // Placeholder for exercise details and editing UI
        child: Text(
          'Exercise Screen (to be implemented)',
          style: TextStyle(fontSize: 22),
        ),
      ),
    );
  }
}
