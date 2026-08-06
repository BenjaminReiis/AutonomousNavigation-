import 'package:flutter/material.dart';

import 'screens/dashboard_screen.dart';



void main(){


runApp(

const AutonomousApp()

);


}



class AutonomousApp extends StatelessWidget{


const AutonomousApp({super.key});



@override

Widget build(
BuildContext context
){


return MaterialApp(

debugShowCheckedModeBanner:false,


title:"Autonomous Robot",



theme:ThemeData(

brightness:Brightness.dark,


primarySwatch:Colors.blue,


),



home:

const DashboardScreen(),


);


}


}
