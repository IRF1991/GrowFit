import 'package:flutter/material.dart';
import '../services/data_service.dart';

class UserProfileScreen extends StatefulWidget {
  const UserProfileScreen({Key? key}) : super(key: key);

  @override
  State<UserProfileScreen> createState() => _UserProfileScreenState();
}

class _UserProfileScreenState extends State<UserProfileScreen> {
  late Future<List<dynamic>> _userProfileFuture;

  @override
  void initState() {
    super.initState();
    _userProfileFuture = DataService.getUserProfile();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Perfil de Usuario')),
      body: FutureBuilder<List<dynamic>>(
        future: _userProfileFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          } else if (!snapshot.hasData || snapshot.data!.isEmpty) {
            return const Center(child: Text('No hay datos de usuario'));
          } else {
            final user = snapshot.data![0];
            return ListView(
              children: user.entries.map<Widget>((entry) {
                return ListTile(
                  title: Text('${entry.key}: ${entry.value}'),
                );
              }).toList(),
            );
          }
        },
      ),
    );
  }
}