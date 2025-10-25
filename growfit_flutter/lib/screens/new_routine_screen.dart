// Pantalla NewRoutineScreen migrada desde Kivy

import 'package:flutter/material.dart';

/// Pantalla para crear una nueva rutina.
/// Incluye campo de texto para el nombre, botón para nuevo ejercicio y botón para volver.
class NewRoutineScreen extends StatefulWidget {
  @override
  _NewRoutineScreenState createState() => _NewRoutineScreenState();
}

class _NewRoutineScreenState extends State<NewRoutineScreen> {
  final TextEditingController _routineNameController = TextEditingController();

  @override
  void dispose() {
    _routineNameController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('NEW ROUTINE')),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Text(
              'NEW ROUTINE',
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 40),
            ),
            const SizedBox(height: 30),
            TextField(
              controller: _routineNameController,
              textAlign: TextAlign.center,
              style: const TextStyle(fontSize: 30),
              decoration: const InputDecoration(
                hintText: 'Enter routine name',
                border: OutlineInputBorder(),
                contentPadding: EdgeInsets.symmetric(vertical: 14),
              ),
            ),
            const SizedBox(height: 30),
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/new_exercise');
              },
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 24),
                textStyle: const TextStyle(fontSize: 20),
              ),
              child: const Text('New Exercise'),
            ),
            const SizedBox(height: 10),
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamedAndRemoveUntil(context, '/', (route) => false);
              },
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 24),
                textStyle: const TextStyle(fontSize: 20),
                backgroundColor: Colors.grey,
              ),
              child: const Text('Back'),
            ),
          ],
        ),
      ),
    );
  }
}
