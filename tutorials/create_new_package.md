![image](../images/TL_Header.png)
# **Creating a New ROS Project / Package**

For starters, we will use the terms - project and package interchangeably. In this tutorial we will learn to create a new project.
This tutorial assumes you have successfully completed the previous tutorial to [Create a ROS Catkin Workspace](tutorials/create_a_ros_workspace.md).
After creating the catkin workspace in your home directory, you should have a directory structure like
```
+-- ~/
|   +-- catkin_ws/
|   |   +-- build/
|   |   +-- devel/
|   |   +-- src/
```
All our source code for our project / package will be placed in the `~/catkin_ws/src` directory.
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

Now, lets check the contents of the current directory, `src`, that you are in, you should see
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

You can observe there are 2 `CMakeLists.txt`. For our project we will need to edit only the file inside our project folder, i.e., `~/catkin_ws/src/ros_workshop/CMakeLists.txt`.
> Again, it is suggested not to fiddle with the other file `~/catkin_ws/src/CMakeLists.txt`.

The `package.xml` file contains meta data on your package, like who created this package and what are the dependecies of this package.

Typically, a C++ project is divided into the `src` directory and the `include` directory. The `include` directory contains header files (`.h` extension)
that contain definition of classes and declarations of higher level functions. While the main code, the definition of those functions and lower level functions are placed in `.cpp` files placed inside the `src` directory.

The catkin workspace has a `src` directory, aka `~/catkin_ws/src` where all the user-written code is present. Inside this directory, we organize our code in form
of projects / packages. Each project has its own `src` directory where you actually write your C++ programs.

To summarize
```
+-- ~/
|   +-- catkin_ws/
|   |   +-- build/                  <-- Not to be edited
|   |   +-- devel/                  <-- Not to be edited
|   |   +-- src/
|   |   |   +-- CMakeLists.txt      <-- Not to be edited
|   |   |   +-- ros_workshop/       <-- Only the contents inside this will be edited
|   |   |   |   +-- CMakeLists.txt  <-- Will be edited
|   |   |   |   +-- package.xml     <-- Will be edited
|   |   |   |   +-- include/        <-- Contents inside this will be edited
|   |   |   |   +-- src/            <-- Contents inside this will be edited
```

Now, the final step of the process, you need to again use `catkin_make`. Remember, `catkin_make` shall only be performed inside the `~/catkin_ws/` directory.
```
$ cd ~/catkin_ws
$ catkin_make
```
Congratulations, you have initialized your first ROS project. `May the force be with you`
