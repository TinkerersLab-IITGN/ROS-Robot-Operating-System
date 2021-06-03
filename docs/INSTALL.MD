![image](../images/TL_Header.png)

# **Installation Guide**

We will be working on a Linux based environment for ROS. If you don’t have any Linux based environment setup, there are three ways to setup Linux environment and install ROS: <br>

1. Dual Boot
2. WSL (Windows Subsystem for Linux) - (Recommended)
3. VM (Virtual Machine)

## **Option 1: Dual Boot**

## **Option 2: WSL (Windows Subsystem for Linux) - (Recommended)**
(For Windows 10)

First we need to install WSL. Follow the below given steps to install WSL2 on Windows 10. (The complete documentation is also given here: [Microsoft](https://docs.microsoft.com/en-us/windows/wsl/install-win10))

### **Step 1: Enable the Windows Subsystem for Linux**

You must first enable the "Windows Subsystem for Linux" optional feature before installing any Linux distributions on Windows.

Open Powershell as administrator and run (i.e. in Start menu search for “cmd” and you will be able to see option of “Command Prompt”, Right click on it and select “Run as administrator” and run the following command)

`dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart`

Now, we will install WSL 2.

### **Step 2: Enable Virtual Machine Feature**

Before installing WSL 2, you must enable the Virtual Machine Platform optional feature.

Run the following command in the same Powershell opened in the 1st step:

`dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart`

Restart your machine to complete the WSL install and update to WSL 2.

### **Step 3: Download the Linux kernel update package**

Download the latest package from here: [WSL2 Linux kernel update package for x64 machines](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)

Run the update package downloaded in the previous step. (Double-click to run - you will be prompted for elevated permissions, select ‘yes’ to approve this installation.)

### **Step 4: Set WSL 2 as your default version**

Again open PowerShell and run this command to set WSL 2 as the default version when installing a new Linux distribution:

`wsl --set-default-version 2`

### **Step 5: Install Ubuntu 20.04 LTS Linux distribution**

Open the [Microsoft Store](https://aka.ms/wslstore) and search for “Ubuntu 20.04 LTS” or you can also use the direct link to [Ubuntu 20.04 LTS](https://www.microsoft.com/en-in/p/ubuntu-2004-lts/9n6svws3rx71?rtc=1#activetab=pivot:overviewtab). In the Microsoft Store in Ubuntu 20.04 LTS page select “GET” and then “Install”.

After the installation gets completed, you will be able to see the “Ubuntu 20.04 LTS” option in the Start Menu. Open it.

The first time you launch a newly installed Linux distribution, a console window will open and you'll be asked to wait for a minute or two for files to decompress and be stored on your PC. All future launches should take less than a second. Then it will ask you to create a user account and password for the Linux distribution.

**Congratulations! You have successfully installed and set up a Linux distribution.**

Now, we will set up GUI.

### **Step 6: Set up X-server application VcXsrv**

Download the setup of X-server application VcXsrv from [here](https://sourceforge.net/projects/vcxsrv/).

Now run the downloaded file (Double click on it). After it gets installed you will be able to see XLaunch icon in the Start Menu. Click on it. 

Choose defaults for display settings and how to start a client. When you arrive at the screen of Extra Settings as shown in the below image, uncheck "Native opengl" option and check "Disable access control" option. (i.e. Click next until you arrive at the "Extra Settings" screen and set it as below shown image)

![image](../images/XLaunch_setup.PNG)

When you click “finish” you will be able to see the VcXsrv icon down in the taskbar that means the server is running.

Now, we need to set the `DISPLAY` environment variable that tells WSL 2 where to send the graphics for any application that needs a display to function. For this, you will need to know the IP address for the Windows host machine. You can find this by going to `Settings -> Network & Internet` and looking under the properties of your current connection (it will be labeled as “IPv4 Address”). 

After getting the IP address open the Linux distribution that you installed (Search "Ubuntu 20.04 LTS" in Start Menu and click on it). Then run this command and replace {your_ip_address} with your IP address:

`echo 'export DISPLAY={your_ip_address}:0.0' >> ~/.bashrc`

Now source the edited .bashrc file by running the following command:

`source ~/.bashrc`

Now, run the following commands to install x11-apps:

`sudo apt update` <br>
`sudo apt install x11-apps`

Now, we are ready to install ROS.

### **Step 7: Install ROS**

Run the following two commands to get updated packages:

`sudo apt update` <br>
`sudo apt upgrade`

Setup your computer to accept software from packages.ros.org. by running following command:

`sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'`

Set up ypur keys by running the following command:

`sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654`

> - If you experience issues connecting to the keyserver, you can try substituting `hkp://pgp.mit.edu:80` or `hkp://keyserver.ubuntu.com:80` in the previous command. 
> - Alternatively, you can use `curl` instead of the `apt-key` command, which can be helpful if you are behind a proxy server:
> - `curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -`

Now, run the following commands so that the packages added by ROS get updated:

`sudo apt update` <br>
`sudo apt upgrade`

Now, run the below command to install Desktop-Full Installation:

`sudo apt install ros-noetic-desktop-full`

> Desktop-Full Install: (Recommended) : Includes everything in Desktop plus 2D/3D simulators and 2D/3D perception packages

You must source this script in every bash terminal you use ROS in. To do so, run the following commands:

`echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc` <br>
`source ~/.bashrc`

Up to now you have installed what you need to run the core ROS packages. To create and manage your own ROS workspaces, there are various tools and requirements that are distributed separately. For example, rosinstall is a frequently used command-line tool that enables you to easily download many source trees for ROS packages with one command.

Now to install this tool and other dependencies for building ROS packages, run:

`sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential`

Before you can use many ROS tools, you will need to initialize rosdep. rosdep enables you to easily install system dependencies for source you want to compile and is required to run some core components in ROS.

To install it and initialize it run the following commands:

`sudo apt install python3-rosdep` <br>
`sudo rosdep init` <br>
`rosdep update`

**Congratulations! You have successfully installed and set up ROS.** 

## **Option 3: VM (Virtual Machine)**