
/// Screen for creating a new exercise.
/// Allows the user to set sets and repetitions, and navigate back.

import 'package:flutter/material.dart';
import 'package:growfit_flutter/logic/counter_utils.dart';

/// Pantalla para crear un nuevo ejercicio.
/// Permite modificar sets y repeticiones, y volver atrás.
class NewExerciseScreen extends StatefulWidget {
  const NewExerciseScreen({super.key});

  @override
  _NewExerciseScreenState createState() => _NewExerciseScreenState();
}

class _NewExerciseScreenState extends State<NewExerciseScreen> {

  final TextEditingController _exerciseNameController = TextEditingController();
  int repsCounter = 12;
  int setsCounter = 3;

  void incrementReps() {
    setState(() {
      repsCounter = incrementCounter(repsCounter);
    });
  }

  void decrementReps() {
    setState(() {
      repsCounter = reduceCounter(repsCounter);
    });
  }

  void resetReps() {
    setState(() {
      repsCounter = 12;
    });
  }

  void incrementSets() {
    setState(() {
      setsCounter = incrementCounter(setsCounter);
    });
  }

  void decrementSets() {
    setState(() {
      setsCounter = reduceCounter(setsCounter);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('New Exercise')),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [

            // Input field for exercise name
            TextField(
              controller: _exerciseNameController,
              textAlign: TextAlign.center,
              style: const TextStyle(fontSize: 28),
              maxLength: 28,
              decoration: const InputDecoration(
                hintText: 'Enter exercise name',
                border: OutlineInputBorder(),
                contentPadding: EdgeInsets.symmetric(vertical: 10),
                counterText: '',
              ),
            ),

            // Display current number of sets
            Text(
              'Sets: $setsCounter',
              textAlign: TextAlign.center,
              style: const TextStyle(fontSize: 30),
            ),
            const SizedBox(height: 10),

            // Display current number of repetitions
            Text(
              'Repetitions: $repsCounter',
              textAlign: TextAlign.center,
              style: const TextStyle(fontSize: 30),
            ),
            const SizedBox(height: 20),

            // Button to increment repetitions
            ElevatedButton(
              onPressed: incrementReps,
              style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 18)),
              child: const Text('+1 Rep'),
            ),

            // Button to decrement repetitions
            ElevatedButton(
              onPressed: decrementReps,
              style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 18)),
              child: const Text('-1 Rep'),
            ),

            // Button to reset repetitions to default value
            ElevatedButton(
              onPressed: resetReps,
              style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 18)),
              child: const Text('Reset Reps'),
            ),

            // Button to increment sets
            ElevatedButton(
              onPressed: incrementSets,
              style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 18)),
              child: const Text('+1 Set'),
            ),

            // Button to decrement sets
            ElevatedButton(
              onPressed: decrementSets,
              style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 18)),
              child: const Text('-1 Set'),
            ),

            // Button to go back to the previous screen
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamedAndRemoveUntil(context, '/new_routine', (route) => false);
              },
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 18),
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
