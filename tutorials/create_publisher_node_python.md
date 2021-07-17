![image](../images/TL_Header.png)
# **Creating a Publisher Node in Python**

After completing the tutorials on rostopics and creating a ROS package, you can try to build a publisher node in Python that will publish on the `/turtle1/cmd_vel`.
Lets check out the package we had created in the previous tutorial
```
+-- ~/catkin_ws/src/
|   +-- CMakeLists.txt
|   +-- ros_workshop/
|   |   +-- CMakeLists.txt
|   |   +-- package.xml
|   |   +-- include/
|   |   +-- src/
```
Proceed to create a new directory named `scripts` in the directory `~/catkin_ws/src/ros_workshop`
```
$ cd ~/catkin_ws/src/ros_workshop
$ mkdir -p scripts
```
We will place our Python scripts in this directory.

Now create a Python script in this directory and open a text editor to edit the script.
```
$ cd ~/catkin_ws/src/ros_workshop/scripts/
$ touch commander.py
$ gedit commander.py
```

We 
