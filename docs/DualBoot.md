![image](../images/TL_Header.png)

# **Dual Boot**

Here, we setup Ubuntu 20.04 LTS on your system as native Operating System in parallel with Windows OS. We assume you have Windows 10 OS preinstalled on your PC. This method is recommended for confident users as mistakes in following the instructions might result in loss of data on hard drives. The installation procedure is inspired from [It's FOSS](https://itsfoss.com/) website - [How to Install Ubuntu Alongside Windows 10](https://itsfoss.com/install-ubuntu-1404-dual-boot-mode-windows-8-81-uefi/). In this procedure you need a blank USB thumb drive (minimum 4GB space), Ubuntu 20.04 LTS .iso image from the official website, and a tool to create a bootable thumb drive like or [balenaEtcher](https://www.balena.io/etcher/) or [Rufus](https://rufus.ie/en_US/).

## **Step 1: Paritioning Disk for Ubuntu**

You can create partitions in a continuous segment of storage device like hard disk or thumb drives such that the OS treats them as separate drives. (You might have observed different letter drives C:\, D:\, E:\ etc. for a single hard disk in some computers) We want to create an unlabelled partition from available disk space. 

1. In Windows 10 OS, open Disk Manangement by searching for "disk partition" in taskbar.
2. Here, you can see the partitions on each of the hard disks you might have in the lower section of the window. You will have one row for each hard disk, hence, systems with both SSD and HDD will observe 2 rows. Select the largest partition on the disk of your choice (do not choose any of the recovery or EFI / boot partitions) and right click on it. Click on shrink volume. The computer will query the largest continuous space available on that drive which will take a couple of minutes.

If you choose to install Ubuntu on your SSD (you can get boot up time less than 10 seconds) you might additionally need to switch the hard disk driver to AHCI drivers from Intel drivers.

3. Next create a partition of atleast 50 GB (= 51200 MB) and click "Shrink". After another few minutes, you will find an "Unallocated" partition of the size you desired along the same row. Exit "Disk Management".

(To uninstall the Ubuntu OS you could simply format this partition and merge with another partition that is active in windows)

## **Step 2:** 

Now, we are ready to install ROS.

Go through the [ROS Installation](https://github.com/GauravViramgami/ROS-Workshop-TL/blob/main/docs/ROS.md) doc to install ROS.
