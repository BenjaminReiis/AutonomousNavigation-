import 'package:flutter/material.dart';



class RobotCard extends StatelessWidget{


const RobotCard({super.key});



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

"ANS-Robot-01",

style:

TextStyle(

fontSize:22,

fontWeight:FontWeight.bold

),


),



const SizedBox(height:10),



const Text(

"Status: ONLINE"

),



const Text(

"Bateria: 100%"

),



],


),


),


);


}


}
