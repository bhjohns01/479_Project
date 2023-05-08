# 479_Project
This is Bryce, Brian, and Kati's final project for 479

Three test case files are provided: input1.txt, input2.txt, input3.txt
There are 10 robots utilized over this terrain. 
The terrain is a 20x20 grid with random obstacles created every run.

Main.py 
- Main function: Reads in a text file that includes multiple orders and their delivery locations. Creates the robot instances, bags the orders accordingly, and place the bags into the robots.
- def sorting() function: bags the orders in accordance to their attributes and size.

foodOrder.py:
- class foodOrder()
- stores items, location, and attaches the items characteristics from the menu (if available)

grid.py
- hey bryce wanna do this

animation.py
- runAnimation is the one function that is called in main, pass the robots array to the first parameter of run animation and the grid to the second. The whole animation is created and controlled from this one function call. 
- Utilizes turtle module
- Uses functions drawx and drawy to create the animated grid
- Obstical function is used to create red circles, representing the randomly generated obstacles in known terrain.
- moveRobots function controls how many pixels the robots are to move, and if their movement will be tracked by a line. 

