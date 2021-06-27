![image](../images/TL_Header.png)
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

![image](../images/Turtlesim.png)


You can think of the ROS master node set up by the `roscore` command to be the abstract layer shown in the figure below.

![image](../images/roslayer.png)

The ROS node `turtlesim_node` essentially provides the graphical output and simulates the movement of the turtle in the 2D plane.

Now, open another terminal and lets see how to communicate to the `turtlesim_node`. In the terminal use the `rostopic` command
```
$ rostopic list
```
This command will show the ROS Topics that are currently in use. To get a little more info on those topics, we can add the verbose option to the above command
```
$ rostopic list -v
```
Now, alongside each topic you will be able to see its message type and the number of publishers / subscribers to that topic.

Now lets checkout what is being published in those ROS topics using `rostopic echo`. Enter the following command to the terminal
```
$ rostopic echo /turtle1/pose
```
You will see the position and velocity of the turtle in the global coordinate frame continuously being published and printed on the screen.
To exit press `Ctrl`+C.


