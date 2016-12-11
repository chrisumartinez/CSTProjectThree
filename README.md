##SYNOPSIS
----------
The name of the following project is Light Slow Draw (LSD).
The following project allows works with the webcam that tracks hand movement and
allows to perform  the two types of actions:
- a user can move his hand and create trails of different size and color
- a user can move his hand and draw with his finger immediately on the screen
Moreover, the program allows to upload created pieces of art to the imgur.

The Github repository for the project is the following:
https://gist.github.com/chrisumartinez/CSTProjectThree

The project consists of the following files:
- Draw.py -> The file with the code for trails, movements and handtracking
- GUI.kv -> The file with the GUI code for the interface
- GUIFinal.py -> The man file that combines the ode for the program and the GUI

##MOTIVATION
------------
The project is believed to have an entertaining purpose. It allows to draw in
the real life right in front of the camera. It might be an interesting game for
children and students. Later on it might also be developed and allow people to
communicate through painting in the air during a video chat.

##REQUIREMENTS
--------------
In order to run the program it is required to have the following libraries
installed:
-OpenCV
-kivy
-numpy
-pyimgur
-tkinter

##RUNNING
---------
How to run the LSD:

1. Make sure that you have all the required libraries installed and that your
webcam is on.
2. Run the "GUIFinal.py" file.
3. In the opened window make sure your hand is located inside of the green square
4. The default mode is "Trails". You can play with colors and sizes or change it
into the drawing mode by pressing the "K" button. In order to draw, press "A",
to erase press "S". In order to change colors or sizes press "J" to decrease,
and "L" to increase the size or the RGB number.
5. You can also make a screenshot and post it to Imgur. The link to the photo
will appear in the terminal

##CONTRIBUTORS
--------------
Adrian Figeroua
Christian Martinez
Darya Yanouskaya

##SOURCES
---------
The project that was used in the creation of the program as a base for the hand
recognition is the following:
https://github.com/vipul-sharma20/gesture-opencv/blob/master/gesture.py

##FUTURE PLANS
--------------
In the future we expect to make it run smooth and add some more brush types.
