![image](../images/TL_Header.png)

# **Dual Boot**

Here, we setup Ubuntu 20.04 LTS on your system as native Operating System in parallel with Windows OS. We assume you have Windows 10 OS preinstalled on your PC. This method is recommended for confident users as mistakes in following the instructions might result in loss of data on hard drives. The installation procedure is inspired from [It's FOSS](https://itsfoss.com/) website - [How to Install Ubuntu Alongside Windows 10](https://itsfoss.com/install-ubuntu-1404-dual-boot-mode-windows-8-81-uefi/). In this procedure you need a blank USB thumb drive (minimum 4GB space), Ubuntu 20.04 LTS .iso image from the official website, and a tool to create a bootable thumb drive like [balenaEtcher](https://www.balena.io/etcher/) or [Rufus](https://rufus.ie/en_US/).

## Step 1 - Partitioning Disk for Ubuntu

It is highly recommended you backup your data before proceeding.

You can create partitions in a continuous segment of storage device like hard disk or thumb drives such that the OS treats them as separate drives. (You might have observed different letter drives C:, D:, E: etc. for a single hard disk in some computers) We want to create an unallocated partition from available disk space. 

1. In Windows 10 OS, open Disk Manangement by searching for "disk partition" in taskbar.
2. Here, you can see the partitions on each of the hard disks you might have in the lower section of the window. You will have one row for each hard disk, hence, systems with both SSD and HDD will observe 2 rows. Select the largest partition on the disk of your choice (do not choose any of the recovery or EFI / boot partitions) and right click on it. Click on shrink volume. The computer will query the largest continuous space available on that drive which will take a couple of minutes.

> If you choose to install Ubuntu on your SSD (you can get boot up time less than 10 seconds) you might additionally need to switch the hard disk driver to AHCI drivers from Intel drivers. Head to this [link](https://itsfoss.com/dual-boot-hdd-ssd/) for more details.

3. Next create a partition of atleast 50 GB (= 51200 MB) and click "Shrink". After another few minutes, you will find an "Unallocated" partition of the size you desired along the same row. Exit "Disk Management".

> To uninstall the Ubuntu OS you could simply format this partition and merge with another partition that is active in Windows OS

## Step 2 - Creating a Bootable USB Thumb / Pen Drive with Ubuntu OS image

In this step, we prepare a USB thumb / pen drive / SD card (minimum 4GB space) to be able to directly boot Ubuntu from it.

1. For this we need the .ISO image file of Ubuntu 20.04 LTS Desktop from the [official Ubuntu website](https://ubuntu.com/). You can alternatively download it from Indian servers from this [link](https://launchpad.net/ubuntu/+cdmirrors).
2. Next you need a tool to create the bootable drive from the Ubuntu image. You may find balenaEtcher pretty easy to use. After installation, the steps would be as simple as selecting the .ISO image file, selecting the USB drive and clicking "Create". The process takes 5 to 10 minutes to prepare the drive.

> After USB installation is done you might want to revert the changes made on the USB drive by following the instructions [here](https://www.diskpart.com/articles/format-bootable-usb-drive-3889i.html)

## Step 3 - Booting into Ubuntu OS and Installing onto Hard Drive

You may choose boot from the USB drive via Windows Advanced Startup interface or have a look under the hood by going into the BIOS of your system.
Unplug and replug your USB drive.

To use the Windows Advanced Startup interface -

1. Search for "uefi" from the taskbar in Windows, and open "Change advanced startup options" in System settings.
2. Go to the "Advanced Startup" tab and click on "Restart Now".
3. You will enter a blue screen with the title "Choose an option". Select "Use a device".
4. Identify the bootable USB drive you prepared and select it.

BIOS is an operating system written onto the motherboard of your system. It handles the hardware until you have booted into the OS of your choice from the hard drive. To take the BIOS route -

1. Search for the BIOS key on the internet for the make of your PC. For DELL PCs the key is F2.
2. Restart the system. When the system is just starting. Keep on repeatedly pressing the BIOS key until you enter the BIOS screen.
3. Go to "Boot" tab in the BIOS. Here, you need to change the boot order. By default, the Windows boot manager gets the top priority to boot from the hard drive. Change the priority order so that the USB drive gets the highest priority to boot.
4. Save and exit the BIOS. The system will automatically reboot.

> If you are unable to boot from the USB drive, you might need to disable "Secure Boot" under the "Security" tab or the "Boot" tab.

After completing either of the above set of steps, your system will restart and enter the Grub bootloader. It is a dark screen with the option to install Ubuntu. You may also choose to try Ubuntu without installing.

1. Select "Install Ubuntu" and hit enter. You will observe Ubuntu 20.04 LTS Focal Fossa booting up.
2. Upon boot up, you will find the option to install Ubuntu in a graphical user interface. Proceed with the instructions on the screen until you come to the "Updates and other software" section.
3. In this section, we recommend to go with "Minimal Installation" and unchecking "Other options" to fasten the installation process. You can always install your desired software later. Click on "Continue". The next section will take a couple of minutes to load.
4. In this "Installation type" section, you will be able to choose the option to "Install Ubuntu alongside Windows Boot Manager". If you unfortunately cannot find this option follow the instructions under "Approach 2" [here](https://itsfoss.com/install-ubuntu-1404-dual-boot-mode-windows-8-81-uefi/) to setup a partition table by selecting the "something else" option.
5. Proceed with the instructions on the screen and install Ubuntu. The installation process may take upto 30 minutes to complete.
6. Once complete, you will be prompted to restart the system. Make sure to remove the USB drive when prompted on the screen to do so.
7. After restart, you will again enter the Grub bootloader program giving you the option to boot into Ubuntu or Windows. You will be prompted this option every time you power on your device. As a sanity check I recommend booting into Windows first to see everything is good.
8. Restart and boot into Ubuntu OS. Set up connection to internet via WiFi or ethernet available at the top right. 
> For connecting to IITGN-SSO, you can simply check the "No CA certificate required" field and enter your credentials. Make sure you have selected "peap" authentication method.
10. Open a terminal and run the following commands
```
$ sudo apt update
$ sudo apt upgrade
```
> Often in dual boot setups you might find a mismatch of time in the two OS. This is because the two OS treat the system time clock as either local time or the RTC time by default. A quickfix to this problem is given [here](https://askubuntu.com/questions/169376/clock-time-is-off-on-dual-boot). You need to open a terminal and enter the following commands -
> ```
> $ timedatectl set-local-rtc 1
> $ sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"
> ```

You can install 3rd party drivers like NVIDIA drivers by following instructions [here](https://linuxize.com/post/how-to-nvidia-drivers-on-ubuntu-20-04/) to get the best performance from your hardware.

---

Now, we are ready to install ROS.

Go through the [ROS Installation](https://github.com/GauravViramgami/ROS-Workshop-TL/blob/main/docs/ROS.md) doc to install ROS.
