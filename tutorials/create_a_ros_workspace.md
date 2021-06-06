![image](../images/TL_Header.png)

# **Create a ROS Workspace**

Let's create and build a [catkin workspace](http://wiki.ros.org/catkin/workspaces).

Open the Linux CLI and run the following commands:

```
mkdir -p ~/catkin_ws/src
```
```
cd ~/catkin_ws/
```
```
catkin_make
```

The [catkin_make](http://wiki.ros.org/catkin/commands/catkin_make) command is a convenience tool for working with [catkin workspaces](http://wiki.ros.org/catkin/workspaces). Running it the first time in your workspace, it will create a CMakeLists.txt link in your 'src' folder.

> **Python 3 users in ROS Melodic and earlier:** note, if you are building ROS from source to achieve Python 3 compatibility, and have setup your system appropriately (ie: have the Python 3 versions of all the required ROS Python packages installed, such as catkin) the first catkin_make command in a clean catkin workspace must be:
> ```
> catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
> ```
> This will configure [catkin_make](http://wiki.ros.org/catkin/commands/catkin_make) with Python 3. You may then proceed to use just catkin_make for subsequent builds.

Additionally, if you look in your current directory you should now have a 'build' and 'devel' folder. Inside the 'devel' folder you can see that there are now several setup.*sh files. Sourcing any of these files will overlay this workspace on top of your environment. To understand more about this see the general catkin documentation: [catkin](http://wiki.ros.org/catkin). Before continuing source your new setup.*sh file:

```
source devel/setup.bash
```

To make sure your workspace is properly overlayed by the setup script, make sure ROS_PACKAGE_PATH environment variable includes the directory you're in.

```
echo $ROS_PACKAGE_PATH
```
`Output: /home/youruser/catkin_ws/src:/opt/ros/noetic/share`

