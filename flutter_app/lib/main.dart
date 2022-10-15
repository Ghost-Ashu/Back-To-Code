import 'Package:flutter/material.dart';
import 'package:flutter_app/screen/home.dart';
void main () {
  runApp(MyApp()
  );
}



class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "BMI CALCULATOR",
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.red,
        visualDensity: VisualDensity.adaptivePlatformDensity,

      ),
      home: HomeScreenState(),
    );
  }
}

