![image](../images/TL_Header.png)

# **ROS Installation**

Open the command line interface of the Linux distribution you installed. (i.e Linux Terminal)

## **Step 1: Update the packages**
Run the following two commands to get updated packages:

```
sudo apt update
```
```
sudo apt upgrade
```

## **Step 2: Setup your sources.list**
Setup your computer to accept software from packages.ros.org. by running following command:

```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

## **Step 3: Set up your keys**
Set up your keys by running the following command:

```
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```

> - If you experience issues connecting to the keyserver, you can try substituting `hkp://pgp.mit.edu:80` or `hkp://keyserver.ubuntu.com:80` in the previous command. 
> - Alternatively, you can use `curl` instead of the `apt-key` command, which can be helpful if you are behind a proxy server:
> ```
> curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -
> ```

## **Step 4: Update the packages added by ROS**
Now, run the following commands so that the packages added by ROS get updated:

```
sudo apt update
```
```
sudo apt upgrade
```

## **Step 5: Installation**
Now, run the below command to install Desktop-Full Installation:

```
sudo apt install ros-noetic-desktop-full
```

> Desktop-Full Install: (Recommended) : Includes everything in Desktop plus 2D/3D simulators and 2D/3D perception packages

## **Step 6: Environment setup**
You must source this script in every bash terminal you use ROS in. To do so, run the following commands:

```
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
```
```
source ~/.bashrc
```

## **Step 7: Dependencies for building packages**
Up to now you have installed what you need to run the core ROS packages. To create and manage your own ROS workspaces, there are various tools and requirements that are distributed separately. For example, rosinstall is a frequently used command-line tool that enables you to easily download many source trees for ROS packages with one command.

Now to install this tool and other dependencies for building ROS packages, run:

```
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
```


## **Step 8: Initialize rosdep**
Before you can use many ROS tools, you will need to initialize rosdep. rosdep enables you to easily install system dependencies for source you want to compile and is required to run some core components in ROS.

To install it and initialize it run the following commands:

```
sudo apt install python3-rosdep
```
```
sudo rosdep init
```
```
rosdep update
```

(The complete documentation for ROS installation is also given here: [ROS](http://wiki.ros.org/noetic/Installation/Ubuntu))

**Congratulations! You have successfully installed and set up ROS.** 

Now, you can start with the [first tutorial](../tutorials/create_a_ros_workspace.md).