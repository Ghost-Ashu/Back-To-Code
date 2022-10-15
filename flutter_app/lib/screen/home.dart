import 'Package:flutter/material.dart';
import 'package:flutter_app/widgets/left_bar.dart';
import 'package:flutter_app/widgets/left_bar.dart';




class HomeScreenState extends StatefulWidget {
  @override
  _HomeScreenStateState createState() => _HomeScreenStateState();
}

class _HomeScreenStateState extends State<HomeScreenState> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor:Colors.white70.withOpacity(.8) ,
        appBar:AppBar(
          title:Text("BMI CALCULATOR ", textDirection:TextDirection.ltr
          ),
          backgroundColor: Colors. red,
          centerTitle: true,
        ),
        body:SingleChildScrollView(
          child: Column(
            children: [
              SizedBox(height:20),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Container(
                    width: 110,
                    child:TextField(
                      style:TextStyle(
                        fontSize: 42,
                        fontWeight: FontWeight.w300,
                        color:Colors.red,
                      ),
                      keyboardType: TextInputType.number,

                      decoration:InputDecoration(

                      hintText: "Height",
                        hintStyle: TextStyle(
                          fontSize: 30,
                          fontWeight: FontWeight.w300,
                            color:Colors.red.withOpacity(.8)
                        ),
                      ),

                    )
                  ),
                  Container(
                      width: 110,
                      child:TextField(
                        style:TextStyle(
                          fontSize: 42,
                          fontWeight: FontWeight.w300,
                        ),
                        keyboardType: TextInputType.number,

                        decoration:InputDecoration(
                          hintText: "Mass",
                          hintStyle: TextStyle(
                            fontSize: 30,
                            fontWeight: FontWeight.w300,
                            color:Colors.red.withOpacity(.8)
                          ),
                        ),

                      )
                  ),
                ],
              ),
              SizedBox(height: 30),
              Container(
                child:
                  Text("CALCULATE",
                  style:TextStyle(
                    fontSize: 22,
                    fontWeight: FontWeight.bold,
                    color:Colors.red,

                  )
                  )
              ),
              SizedBox(height: 50),
              Container(
                  child:
                  Text("10",
                      style:TextStyle(
                        fontSize: 90,
                        color:Colors.red,

                      )
                  )
              ),
              SizedBox(height: 50),
              Container(
                  child:
                  Text("normal weight",
                      style:TextStyle(
                        fontSize: 32,
                        fontWeight: FontWeight.w400,
                        color:Colors.red,

                      )
                  )
              ),
              SizedBox(height: 10),
              LeftBar(barWidth:40),
              SizedBox(height: 20),
              LeftBar(barWidth:40,),
              SizedBox(height: 20),
              LeftBar(barWidth:40,),

            ],
          ),

        )


    );
  }
}


