import 'package:flutter/material.dart';

class MapWidget extends StatefulWidget {
  const MapWidget({super.key});

  @override
  State<MapWidget> createState() => _MapWidgetState();
}

class _MapWidgetState extends State<MapWidget> {
  double robotX = 120;
  double robotY = 150;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      height: 400,
      decoration: BoxDecoration(
        color: Colors.black87,
        border: Border.all(color: Colors.blueAccent),
      ),
      child: Stack(
        children: [
          Positioned(
            left: robotX,
            top: robotY,
            child: const Icon(
              Icons.smart_toy,
              color: Colors.green,
              size: 40,
            ),
          ),
        ],
      ),
    );
  }
}
