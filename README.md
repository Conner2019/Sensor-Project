# Sensor-Project
Project Tutorial

This project uses a Raspberry Pi and Philips Hue lights. 
The longer a sound sensor takes in input the lights will turn on and get brighter. 
After 5 seconds of no sound input the light will turn off.
You will need:
A Raspberry Pi
Philips Hue Lights and Bridge
A Sound Sensor
A Breadboard
5 wires

First we need to set up the circuit. 
Connect one wire from the GND of the RPI to the negative side of the breadboard and second one from the GND on the Sound Sensor
to the negative rail . Connect another wire from the 3V3 to the positive rail. 
Then on the Sound Sensor connect VCC to the positive rail and the DO to #18 on the RPI.

Assuming your Bridge and lights are already connected we can move on to the coding.
Download the Qhue Library then open up a Python file on your RPi. 

https://github.com/Conner2019/Sensor-Project/blob/master/sensorTest.py
This code creates a group on lights connected to your bridge. 
It listen for input and increases a counter for the brightness level on a half-second interval. 
The counter is reset when there is no input. 

Paste this code into your file then change the bridge IP and username, save it, and open up the terminal.
Type sudo python sensorTest.py into the terminal and hit ENTER.
Now your light should be working.

