// Pantalla RoutineScreen migrada desde Kivy

import 'package:flutter/material.dart';

/// Screen to display the details of a routine and its exercises.
/// (Logic and UI pending implementation.)
class RoutineScreen extends StatelessWidget {
  const RoutineScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Routine')), 
      body: const Center(
        // Placeholder for routine details and exercises list
        child: Text(
          'Routine Screen (to be implemented)',
          style: TextStyle(fontSize: 22),
        ),
      ),
    );
  }
}
