import 'package:flutter/material.dart';

import '../widgets/map_widget.dart';

class MapScreen extends StatelessWidget {
  const MapScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Mapa do Robô"),
      ),
      body: const Padding(
        padding: EdgeInsets.all(16),
        child: MapWidget(),
      ),
    );
  }
}
