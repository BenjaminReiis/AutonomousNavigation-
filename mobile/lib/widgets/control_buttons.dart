import 'package:flutter/material.dart';



class ControlButtons extends StatelessWidget{


const ControlButtons({super.key});



@override

Widget build(
BuildContext context
){


return Column(


children:[


ElevatedButton(

style:

ElevatedButton.styleFrom(

backgroundColor:Colors.green

),



onPressed:(){},



child:

const Text(

"INICIAR ROBÔ"

),


),



ElevatedButton(

style:

ElevatedButton.styleFrom(

backgroundColor:Colors.blue

),



onPressed:(){},



child:

const Text(

"PARAR"

),


),



ElevatedButton(

style:

ElevatedButton.styleFrom(

backgroundColor:Colors.red

),



onPressed:(){},



child:

const Text(

"EMERGÊNCIA"

),


),


],


);


}


}
