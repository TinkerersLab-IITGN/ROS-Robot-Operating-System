![image](../images/TL_Header.png)

# Installation Guide

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

## **Option 3: VM (Virtual Machine)**