// Pantalla NewExerciseScreen migrada desde Kivy

import 'package:flutter/material.dart';

/// Pantalla para crear un nuevo ejercicio.
/// Permite modificar sets y repeticiones, y volver atrás.
class NewExerciseScreen extends StatefulWidget {
  const NewExerciseScreen({Key? key}) : super(key: key);

  @override
  _NewExerciseScreenState createState() => _NewExerciseScreenState();
}

class _NewExerciseScreenState extends State<NewExerciseScreen> {
  int repsCounter = 12;
  int setsCounter = 0;

  void incrementReps() {
    setState(() {
      repsCounter++;
    });
  }

  void decrementReps() {
    setState(() {
      if (repsCounter > 0) repsCounter--;
    });
  }

  void resetReps() {
    setState(() {
      repsCounter = 12;
    });
  }

  void incrementSets() {
    setState(() {
      setsCounter++;
    });
  }

  void decrementSets() {
    setState(() {
      if (setsCounter > 0) setsCounter--;
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
            Text(
              'Sets: $setsCounter',
              textAlign: TextAlign.center,
              style: const TextStyle(fontSize: 30),
            ),
            const SizedBox(height: 10),
            Text(
              'Repetitions: $repsCounter',
              textAlign: TextAlign.center,
              style: const TextStyle(fontSize: 30),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: incrementReps,
              style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 18)),
              child: const Text('+1 Rep'),
            ),
            ElevatedButton(
              onPressed: decrementReps,
              style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 18)),
              child: const Text('-1 Rep'),
            ),
            ElevatedButton(
              onPressed: resetReps,
              style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 18)),
              child: const Text('Reset Reps'),
            ),
            ElevatedButton(
              onPressed: incrementSets,
              style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 18)),
              child: const Text('+1 Set'),
            ),
            ElevatedButton(
              onPressed: decrementSets,
              style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 18)),
              child: const Text('-1 Set'),
            ),
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
