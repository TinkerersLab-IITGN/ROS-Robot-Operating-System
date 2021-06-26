![image](images/TL_Header.png)
# **Playing with Turtlesim to Understand ROS Topics**

This tutorial assumes you have succesfully installed ROS on your Linux desktop.
Turtlesim is a very simplistic 2D robot simulator intended to understand and experiment with rostopics. To run the simulator, you need two terminals, one to start
the ros master node and second to start the turtlebot simulator node. Fire up a terminal and run
```
$ roscore
```
On another fresh terminal run
```
$ rosrun turtlesim turtlesim_node
```
This will open a small square window like one below,

![image](images/Turtlesim.png)


You can think of the ROS master node set up by the `roscore` command to be the abstract layer shown in the figure below.

![image](images/roslayer.png)

The ROS node `turtlesim_node` essentially provides the graphical out and simulates the movement of the turtle in the 2D plane.

