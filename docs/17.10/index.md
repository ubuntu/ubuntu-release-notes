---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/ArtfulAardvark/ReleaseNotes -->

(ubuntu-17-10-release-notes)=
# Ubuntu 17.10 release notes

**WARNING: Release reached End of Life**

**This release is no longer supported, please see [Releases](https://help.ubuntu.com/community/Releases)**

**WARNING: Release reached End of Life**


(17-10-introduction)=
## Introduction

These release notes for **Ubuntu 17.10** (Artful Aardvark) provide an overview of the release and document the known issues with Ubuntu 17.10 and its flavors.


(17-10-support-lifespan)=
### Support lifespan

Ubuntu 17.10 was supported for 9 months until [July 2018](https://wiki.ubuntu.com/Releases).


(17-10-official-flavour-release-notes)=
### Official flavour release notes

Find the links to release notes for official flavors [here](https://wiki.ubuntu.com/Official_flavours).


(get-ubuntu-17-10)=
## Get Ubuntu 17.10


(download-ubuntu-17-10)=
### Download Ubuntu 17.10

Images can be downloaded from a location near you.

You can download ISOs and flashable images from:

[releases.ubuntu.com/17.10/](http://releases.ubuntu.com/17.10/) (Ubuntu Desktop and Server)

[cdimage.ubuntu.com/ubuntu/releases/17.10/release/](http://cdimage.ubuntu.com/ubuntu/releases/17.10/release/) (Less Popular Ubuntu Images)

[cloud-images.ubuntu.com/daily/server/artful/current/](http://cloud-images.ubuntu.com/daily/server/artful/current/) (Ubuntu Cloud Images)

[cdimage.ubuntu.com/netboot/17.10/](http://cdimage.ubuntu.com/netboot/17.10/) (Ubuntu Netboot)

[cdimage.ubuntu.com/kubuntu/releases/17.10/release/](http://cdimage.ubuntu.com/kubuntu/releases/17.10/release/) (Kubuntu)

[cdimage.ubuntu.com/lubuntu/releases/17.10/release/](http://cdimage.ubuntu.com/lubuntu/releases/17.10/release/) (Lubuntu and Lubuntu Alternate)

[cdimage.ubuntu.com/ubuntu-budgie/releases/17.10/release/](http://cdimage.ubuntu.com/ubuntu-budgie/releases/17.10/release/) (Ubuntu Budgie)

[cdimage.ubuntu.com/ubuntukylin/releases/17.10/release/](http://cdimage.ubuntu.com/ubuntukylin/releases/17.10/release/) (Ubuntu Kylin)

[ubuntu-mate.org/download/](https://ubuntu-mate.org/download/) (Ubuntu MATE)

[cdimage.ubuntu.com/ubuntustudio/releases/17.10/release/](http://cdimage.ubuntu.com/ubuntustudio/releases/17.10/release/) (Ubuntu Studio)

[cdimage.ubuntu.com/xubuntu/releases/17.10/release/](http://cdimage.ubuntu.com/xubuntu/releases/17.10/release/) (Xubuntu)

As fixes will be included in new images between now and release, any daily cloud image from today or later (i.e. a serial of 20170926 or higher) should be considered a beta image.  Bugs found should be filed against the appropriate packages or, failing that, the cloud-images project in Launchpad.


(17-10-upgrading-from-ubuntu-17-04)=
### Upgrading from Ubuntu 17.04

To upgrade on a desktop system:

* Open the "Software & Updates" Setting in System Settings.

* Select the 3rd Tab called "Updates".

* Set the "Notify me of a new Ubuntu version" dropdown menu to "For any new version".

* Press Alt+F2 and type in "update-manager -c" (without the quotes) into the command box.

* Update Manager should open up and tell you: New distribution release '17.10' is available.

* If not you can also use "/usr/lib/ubuntu-release-upgrader/check-new-release-gtk"

* Click Upgrade and follow the on-screen instructions.

To upgrade on a server system:

* Install the `update-manager-core` package if it is not already installed.

* Make sure the `Prompt` line in /etc/update-manager/release-upgrades is set to normal.

* Launch the upgrade tool with the command `sudo do-release-upgrade`.

* Follow the on-screen instructions.
Note that the server upgrade will use GNU screen and automatically re-attach in case of dropped connection problems.




* For other changes since 16.04 LTS, see the [17.04 Release Notes](https://wiki.ubuntu.com/ZestyZapus/ReleaseNotes) and [16.10 Release Notes](https://wiki.ubuntu.com/YakketyYak/ReleaseNotes).


(17-10-updated-packages)=
### Updated Packages


(17-10-linux-kernel-4-13)=
#### Linux kernel 4.13

Ubuntu 17.10 is based on the Linux release series **4.13**. It includes support for the new IBM z14 mainframe CPACF instructions and new KVM features.


(17-10-network-configuration)=
#### Network configuration

**ifupdown** has been deprecated in favor of **netplan** and is no longer present on new installs. The installer will generate a configuration file for netplan in _/etc/netplan_, which will set up the system to configure the network via systemd-networkd or NetworkManager. Desktop users will see their system fully managed via NetworkManager as it has been the case in previous releases, but Server users now have their network devices managed via systemd-networkd on new installs. This only applies to new installations.

Given that ifupdown is no longer installed by default, its commands will not be present: _ifup_ and _ifdown_ are thus unavailable, replaced by `ip link set $device up` and `ip link set $device down`.

The `networkctl` command is also available for users to see a summary of the network devices. `networkctl status` will display the current global state of IP addresses on the system; and `networkctl status $device` can display the details specific to a network device.

For more information about netplan, please refer to the manual page using the `man 5 netplan` command.


(17-10-ubuntu-desktop)=
### Ubuntu Desktop

* **32-bit** installer images are no longer provided for Ubuntu Desktop.

* The Ubuntu Desktop now uses **GNOME** instead of Unity.

_ On supported systems, **Wayland** is now the default display server. The older display server is still available: just choose _Ubuntu on Xorg* from the cog on the log in screen.

* **GDM** has replaced LightDM as the default display manager. The login screen now uses virtual terminal 1 instead of virtual terminal 7.

* Window control buttons are back on the **right** for the first time since 2010.

* Apps provided by GNOME have been updated to **3.26**. For more details about GNOME 3.26, see their [Release Notes](https://help.gnome.org/misc/release-notes/3.26/).

* **Driverless printing support** is now available for [IPP Everywhere](http://www.pwg.org/dynamo/eveprinters.php), [Apple AirPrint](https://support.apple.com/en-us/HT201311), [Wi-Fi Direct](https://www.wi-fi.org/discover-wi-fi/wi-fi-direct) devices. Follow the [instructions from 17.04](https://wiki.ubuntu.com/ZestyZapus/ReleaseNotes#Driverless_Printing).

_ Printer configuration is now done in the Settings app: Choose _Devices_ and then _Printers_. The tool uses the same algorithms for identifying printers and choosing drivers as the formerly used system-config-printer, and makes full use of driverless printing to support as many printers as possible. Note that some options, like printer sharing, are missing. To reach them, click the _Additional Printer Settings…* button at the end of the list of available print queues and you get good old system-config-printer.

* The **Amazon** app now loads in the default web browser.

* The default on screen keyboard is GNOME's **Caribou** instead of Onboard.

* **Calendar** now supports recurring events.

* **LibreOffice** has been updated to [5.4](https://wiki.documentfoundation.org/ReleaseNotes/5.4).

* **Python 2** is no longer installed by default. Python 3 has been updated to 3.6.

* The **Rhythmbox** music player now uses the [alternate user interface](https://github.com/fossfreedom/alternative-toolbar) created by Ubuntu Budgie developer David Mohamed.

* The **Settings** app has been redesigned.

* **Simple Scan** has a new workflow and design and is now part of core GNOME.

* System Log has been replaced by **Logs**, an app to view logs from the systemd journal.

_ The **Ubuntu GNOME** flavor has been discontinued. If you are using Ubuntu GNOME, you will be upgraded to Ubuntu. Choose the _Ubuntu* session from the cog on the login screen if you would like the default Ubuntu experience.

_ Install **gnome-session** and choose _GNOME* from the cog on the login screen if you would like to try a more upstream version of GNOME. If you'd like to also install more core apps, install the **vanilla-gnome-desktop** metapackage.


(17-10-ubuntu-server)=
### Ubuntu Server


(17-10-qemu-2-10)=
#### qemu 2.10

Qemu has been updated to the 2.10 release.

Since the last version was 2.8 see both Changelogs of [2.9](http://wiki.qemu.org/ChangeLog/2.9) and [2.10](http://wiki.qemu.org/ChangeLog/2.10) for details.

Among many other changes there is one that might need follow on activity by the user/admin: Image locking is added and enabled by default. This generally makes execution much safer, but can break some old use cases that now explicitly have to opt-in to ignore/share the locks by [tools](https://git.qemu.org/?p=qemu.git;a=commit;h=335e9937) and [subcommands](https://git.qemu.org/?p=qemu.git;a=commit;h=459571f7) using the _--force-share_ option or the [share-rw dqev property](https://git.qemu.org/?p=qemu.git;a=commit;h=dabd18f6).


(17-10-libvirt-3-6)=
#### libvirt 3.6

Libvirt has been updated to version 3.6.
See the [Changelogs](https://libvirt.org/news.html) for details.


(17-10-lxd-2-18)=
#### LXD 2.18

LXD was updated to version 2.18.

Some of the top new features are:

* Native Ceph RBD support
* Support for cloud instance types
* Preseeding of the "lxd init" questions through yaml
* New client library
* Improved storage handling (volume resize, auto re-mapping on attach, ...)
* A lot of small improvements to the client tool

See the [Changelogs](https://linuxcontainers.org/lxd/news/) for details.


(17-10-dpdk-17-05-2)=
#### DPDK 17.05.2

Ubuntu 17.10 includes the latest release of DPDK that has stable updates: 17.05.2.

See the [Release Notes](http://dpdk.org/doc/guides/rel_notes/release_17_05.html) as well as the stable release [announcement stable .1](http://dpdk.org/ml/archives/announce/2017-June/000133.html) [announcement stable .2](http://dpdk.org/ml/archives/announce/2017-September/000144.html) and for more detail.

This made it possible to integrate Open vSwitch 2.8.


(17-10-open-vswitch-2-8)=
#### Open vSwitch 2.8

Open vSwitch has been updated to 2.8.

Please read the [release notes](http://openvswitch.org/releases/NEWS-2.8.0) for more detail.

Remember that since version 2.7 you need to specify dpdk devices via [dpdk-devargs](http://docs.openvswitch.org/en/latest/howto/dpdk/#ports-and-bridges).


(17-10-new-bind9-ksk)=
#### New Bind9 KSK

The DNS server bind9 was updated to include the new Key Signing Key (KSK) that was published on July 11, 2017. Starting on October 11, 2017, that key will sign the root zone key, which in turn is used to sign the actual root zones. For more details, visit:

* [2017 Root Key Rollover – What Does it Mean for BIND Users](https://www.isc.org/blogs/2017-root-key-rollover-what-does-it-mean-for-bind-users/)

* [Root Zone KSK Rollover](https://www.icann.org/resources/pages/ksk-rollover/)
Existing installations of bind9 should automatically update their anchor keys following RFC 5011, but new installations after the rollover event on October 11th, 2017, will need this new package or have the key updated manually.


(17-10-cloud-init)=
#### cloud-init

The version was updated to [17.1](https://launchpad.net/cloud-init/trunk/17.1). Notable new features include:

* Python 3.6 support
* Ec2 support for IPv6 instance configuration
* Expedited boot time through cloud-id optimization
* Support for netplan yaml in cloud-init
* Add cloud-init subcommands collect-logs, analyze and schema for developers
* Apport integration from cloud-init via ‘ubuntu-bug  cloud-init’
* Significant unittest and integration test coverage improvements


(17-10-curtin)=
#### curtin

The version was updated to [0.1.0~bzr519-0ubuntu1](https://launchpad.net/ubuntu/+source/curtin/0.1.0~bzr519-0ubuntu1). Notable new features include:

* Network configuration passthrough for ubuntu and centos
* More resilient UEFI/grub interaction
* Better support for mdadm arrays
* Ubuntu Core 16 Support
* Improved bcache support


(17-10-samba)=
#### Samba

Samba was updated to version [4.6.7](https://www.samba.org/samba/history/samba-4.6.7.html).

Noteable changes in the 4.6.x series include:

* Multi-process Netlogon support
* New options for controlling TCP ports used for RPC services
* AD LDAP and replication performance improvements
* DNS improvements

The OS Version for the printing server has been increased to announce Windows Server 2003 R2 SP2
ID mapping checks added to the testparm(1) tool. There are some ID mapping backends which are not allowed to be used for the default backend. Winbind will no longer start if an invalid backend is configured as the default backend.


(17-10-known-issues)=
## Known issues

As is to be expected, with any release, there are some significant known bugs that users may run into with this release of Ubuntu 17.10.  The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:


(17-10-incompatibility-with-bios-in-certain-lenovo-acer-systems)=
### Incompatibility with BIOS in certain Lenovo, Acer systems

A bug in the Linux 4.13 kernel shipped in Ubuntu 17.10 can leave users unable to update any of their BIOS settings, including their system’s boot order, after booting this version of Ubuntu.

A kernel with a fix for this issue will be available in zesty-updates shortly, but, the Ubuntu 17.10 installer images still contain the kernel with this bug.  Users with affected systems should not upgrade to Ubuntu 17.10 **or boot an Ubuntu 17.10 installer image** until this issue as resolved.  Doing so may result in your computer requiring professional servicing in order to restore BIOS functionality.

A full list of known affected models can be found in Bug:1734147.

If you have already installed Ubuntu 17.10 on an affected system, you may not immediately notice this problem because Ubuntu will continue to boot from disk.  To verify whether your system has been affected by this bug, create a USB stick with the Ubuntu 16.04 desktop image and try to boot it.  If you are able to boot it, your system has most likely not been impacted by this bug.


(17-10-desktop)=
### Desktop

* Bluetooth audio devices cannot be used in the Greeter.  This will cause issues for people using the accessibility features such as screenreaders at the login screen.  Once logged in everything should work as expected.

* Some admin utilities will not work with GNOME on Wayland since the apps have not been adapted to use PolicyKit to only use admin privileges for the specific functions needed. Also, some screenshot and screencast apps and all remote desktop server apps do not currently work on GNOME on Wayland. As a workaround, you can use the Ubuntu on Xorg session. For more details read upstream notes about [known issues and major changes](https://fedoraproject.org/wiki/How_to_debug_Wayland_problems#Known_issues.2C_frequent_complaints.2C_fundamental_changes).

* Exiting the live session may get stuck with a "A start job is running for " error. You may need to forcefully power off the computer if you see this. (Bug:1706939)

* The Dock and Appindicator system extensions appear to be Off in tools like GNOME Tweaks. (They are on but cannot be disabled because they are system extensions for the Ubuntu session.) (Bug:1718850)

* Mouse & Touchpad settings and behavior will not work right in the Ubuntu desktop if `xserver-xorg-input-synaptics` is installed. Some desktop environments such as Unity require `xserver-xorg-input-synaptics`. (Bug:1686081)

* The screen reader is not working for the Ubuntu installer from the menu 'Install Ubuntu' (Bug:1719995) but it works fine when the installer is started from the live session.

* The Color Emoji feature of GNOME 3.26 is not available in Ubuntu 17.10.

* Tracker is not installed by default. When installed, you must log out and log back in for the tracker service to start (Bug:1697769)

* Opening the Users panel in Control Center is slow.

* Systems may fail to boot when connected over DisplayPort to an external screen, on NVidia graphics hardware such as the GTX970 chipset. (Bug:1723619)

* When an external monitor is connected to a laptop, the login screen is only displayed on the internal one and in some case is not visible (Bug:1723025)

* The warning dialog when a user force a UEFI installation does not respond to input event and the installation is then blocked at this stage (Bug:1724482) Avoid yourself some troubles and do not force a UEFI installation without a UEFI partition, grub-installer will fail anyway.

* Doing an "Entire disk" installation over an existing LVM installation will fail because the installer selects the wrong boot device (Bug:1724417) Use custom partitioning instead and manually select the right boot device in the combo box.


(17-10-server)=
### Server

* On s390x architecture, in KVM virtual machines interface names are not preserved on upgrade, and new predictable interface names are used. This will result in lack of network connectivity due to incorrect names in `/etc/network/interfaces`. An upgrade SRU to preserve `ethX` interface names is being prepared. (Bug:1682437)

* Partitioning step allows to configure LVM across multiple devices without requiring to setup a separate /boot partition. This may lead to failure to install the bootloader at the end of the installation, and failures to boot the resultant installations. (Bug:1680101)

* LVM configuration cannot be removed when volume groups with the same name are found during installation. Partitioner does not support installation when multiple conflicting/identical volume groups have been detected. For example reinstalling Ubuntu with LVM across multiple disk drives that had individual LVM installations of Ubuntu. As a workaround, please format disk drives prior to installation, or from the built in shell provided in the installer. (Bug:1679184)

* cio_ignore blacklist is no longer active after installation, because not all install-time parameters, like cio_ignore (s390x), are propagated to the installed system. Workaround is to edit /etc/zipl.conf to apply these and re-run sudo zipl to update the IPL. (Bug:1571561)


(17-10-printing)=
### Printing

* USB printers do not get set up automatically and IPP-over-USB does not work at all. Please set up your USB printer using "Devices"/"Printers" in the GNOME Settings. If possible, especially for driverless printing, connect your printer via network (Ethernet or Wi-Fi) or wait to upgrade to 17.10 until the problem gets fixed (Bug:1721839).





(17-10-official-flavours)=
## Official flavours

The release notes for the official flavours can be found at the following links:

* Kubuntu [wiki.ubuntu.com/ArtfulAardvark/ReleaseNotes/Kubuntu](https://wiki.ubuntu.com/ArtfulAardvark/ReleaseNotes/Kubuntu)

* Lubuntu [wiki.ubuntu.com/ArtfulAardvark/ReleaseNotes/Lubuntu](https://wiki.ubuntu.com/ArtfulAardvark/ReleaseNotes/Lubuntu)

* Ubuntu Budgie [ubuntubudgie.org/blog/2017/09/25/17-10-release-notes](https://ubuntubudgie.org/blog/2017/09/25/17-10-release-notes)

* Ubuntu Kylin [wiki.ubuntu.com/ArtfulAardvark/ReleaseNotes/UbuntuKylin](https://wiki.ubuntu.com/ArtfulAardvark/ReleaseNotes/UbuntuKylin)

* Ubuntu MATE [ubuntu-mate.org/blog/ubuntu-mate-artful-final-release/](https://ubuntu-mate.org/blog/ubuntu-mate-artful-final-release/)

* Ubuntu Studio [wiki.ubuntu.com/ArtfulAardvark/ReleaseNotes/UbuntuStudio](https://wiki.ubuntu.com/ArtfulAardvark/ReleaseNotes/UbuntuStudio)

* Xubuntu [wiki.xubuntu.org/releases/17.10/release-notes](http://wiki.xubuntu.org/releases/17.10/release-notes)


(17-10-more-information)=
## More information


(17-10-reporting-bugs)=
### Reporting bugs

Your comments, bug reports, patches and suggestions will help fix bugs and improve the quality of future releases. Please [report bugs using the tools provided](http://help.ubuntu.com/community/ReportingBugs).

If you want to help out with bugs, the [Bug Squad](http://wiki.ubuntu.com/BugSquad) is always looking for help.


(17-10-participate-in-ubuntu)=
### Participate in Ubuntu


If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

[community.ubuntu.com/contribute](https://community.ubuntu.com/contribute)


(17-10-more-about-ubuntu)=
### More about Ubuntu

You can find out more about Ubuntu on the [Ubuntu website](https://www.ubuntu.com) and [Ubuntu wiki](https://wiki.ubuntu.com).

To sign up for future Ubuntu development announcements, please subscribe to Ubuntu's development announcement list at:

[lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce](https://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce)
