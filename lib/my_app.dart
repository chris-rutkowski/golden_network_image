import 'package:flutter/material.dart';

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        body: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Container(height: 20, width: 100, color: Colors.red),
              Image.network(
                'https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png',
                width: 100,
                height: 100,
                fit: BoxFit.cover,
                frameBuilder: (context, child, frame, wasSynchronouslyLoaded) {
                  debugPrint('frameBuilder called for frame=$frame, wasSync=$wasSynchronouslyLoaded ');
                  return child;
                },
              ),
              Container(height: 20, width: 100, color: Colors.blue),
            ],
          ),
        ),
      ),
    );
  }
}
