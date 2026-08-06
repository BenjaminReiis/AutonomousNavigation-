import 'package:flutter/material.dart';



class TelemetryCard extends StatelessWidget{


const TelemetryCard({super.key});



@override

Widget build(
BuildContext context
){


return Card(


child:

Padding(

padding:

const EdgeInsets.all(20),



child:

Column(

children:[


const Text(

"Telemetria",

style:

TextStyle(

fontSize:20

),


),



const Text(

"GPS: conectado"

),



const Text(

"IMU: conectado"

),



const Text(

"LiDAR: conectado"

),



],


),


),


);


}


}
