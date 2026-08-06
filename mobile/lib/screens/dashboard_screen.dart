import 'package:flutter/material.dart';


import '../widgets/robot_card.dart';

import '../widgets/control_buttons.dart';

import '../widgets/telemetry_card.dart';



class DashboardScreen extends StatelessWidget{


const DashboardScreen({super.key});



@override

Widget build(
BuildContext context
){


return Scaffold(


appBar:AppBar(

title:

const Text(

"Robot Control Dashboard"

),


),



body:

SingleChildScrollView(


child:

Padding(

padding:

const EdgeInsets.all(16),



child:

Column(

children:[


const RobotCard(),



const SizedBox(height:20),



const ControlButtons(),



const SizedBox(height:20),



const TelemetryCard(),



],


),


),


),


);


}


}
