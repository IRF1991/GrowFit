// Pantalla NewRoutineScreen migrada desde Kivy

import 'package:flutter/material.dart';

/// Screen for creating a new routine.
/// Includes a text field for the routine name, button to add a new exercise, and back navigation.
class NewRoutineScreen extends StatefulWidget {
  const NewRoutineScreen({super.key});

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
            // Title of the screen
            const Text(
              'NEW ROUTINE',
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 40),
            ),
            const SizedBox(height: 30),
            // Text field for entering the routine name
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
            // Button to add a new exercise to the routine
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
            // TODO: Add a list of exercises added to the routine here
            // (This will display the exercises as the user adds them)
            // ...
            // Button to go back to the previous screen
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
