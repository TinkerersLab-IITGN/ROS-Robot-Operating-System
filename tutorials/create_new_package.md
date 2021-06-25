![image](images/TL_Header.png)
# **Creating a New ROS Project / Package**

For starters, we will use the terms - project and packages interchangeably. In this tutorial we will learn to create a new project.
This tutorial assumes you have successfully completed the previous tutorial to [Create a ROS Catkin Workspace](tutorials/create_a_ros_workspace.md).
After creating the catkin workspace in your home directory, you should have a directory structure like
```
+-- ~/
|   +-- catkin_ws/
|   |   +-- src/
|   |   +-- devel/
|   |   +-- build/
```
All our source code for our project / package will placed in the `~/catkin_ws/src` directory.
> The directories `~/catkin_ws/build` and `~/catkin_ws/devel`
> will contain executables and other stuff, something not to be messed with by us, beginners, at the moment. 
> (`catkin tools` automatically handles these stuff).

To create a new project, first change directory to `~/catkin_ws/src`. Then use the `catkin_create_pkg` command to create a new package / project
```
$ cd ~/catkin_ws/src
$ catkin_create_pkg ros_workshop std_msgs roscpp rospy
```
The string `ros_workshop` next to the `catkin_create_pkg` command is the name of the new project you are creating. You can use any name that you wish.

The following 3 strings `std_msgs`, `roscpp` and `rospy` are names of 3 more ros packages that your current project / package depends on. You may have
your projects depend on many more packages (even packages that you have built)
> The package
> - `std_msgs` provides you built in rostopic message type for several useful data like position, velocity etc.
> - `roscpp` provides ROS library functions for your C++ code
> - `rospy` provides ROS library functions for your Python code

Now, is you check the contents of the current directory, `src`, that you are in, you should see
```
+-- ~/catkin_ws/src/
|   +-- CMakeLists.txt
|   +-- ros_workshop/
|   |   +-- CMakeLists.txt
|   |   +-- package.xml
|   |   +-- include/
|   |   +-- src/
```

It is understable if things get a bit confusing because of multiple files and folders with the same name.
