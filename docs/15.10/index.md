---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/WilyWerewolf/ReleaseNotes -->

(ubuntu-15-10-release-notes)=
# Ubuntu 15.10 release notes

(15-10-introduction)=
## Introduction

These release notes for **Ubuntu 15.10** (Wily Werewolf) provide an overview of the release and document the known issues with Ubuntu 15.10 and its flavors.


(15-10-support-lifespan)=
### Support lifespan

Ubuntu 15.10 will be supported for 9 months for Ubuntu Desktop, Ubuntu Server, Ubuntu Core, Kubuntu, Ubuntu Kylin along with all other flavours.


(15-10-official-flavour-release-notes)=
### Official flavour release notes

Find the links to release notes for official flavors [here](https://wiki.ubuntu.com/Official_flavours).


(get-ubuntu-15-10)=
## Get Ubuntu 15.10


(download-ubuntu-15-10)=
### Download Ubuntu 15.10

Images can be downloaded from a location near you.
##
**Note:** The Ubuntu Desktop images are now bigger than a standard CD, and you should use a USB or DVD for installation.

You can download ISOs from:

[releases.ubuntu.com/15.10/](http://releases.ubuntu.com/15.10/) (Ubuntu Desktop, Server, and Snappy Core)

[cdimage.ubuntu.com/ubuntu/releases/15.10/release/](http://cdimage.ubuntu.com/ubuntu/releases/15.10/release/) (Less Popular Ubuntu Images)

[cloud-images.ubuntu.com/releases/15.10/release/](http://cloud-images.ubuntu.com/releases/15.10/release/) (Ubuntu Cloud Server)

[cdimage.ubuntu.com/netboot/15.10/](http://cdimage.ubuntu.com/netboot/15.10/) (Ubuntu Netboot)


##[cdimage.ubuntu.com/ubuntu-core/releases/15.10/release/release/](http://cdimage.ubuntu.com/ubuntu-core/releases/15.10/release/release/) (Ubuntu Core)

##[cdimage.ubuntu.com/edubuntu/releases/15.10/release/release/](http://cdimage.ubuntu.com/edubuntu/releases/15.10/release/release/) (Edubuntu DVD)

[cdimage.ubuntu.com/kubuntu/releases/15.10/release/](http://cdimage.ubuntu.com/kubuntu/releases/15.10/release/) (Kubuntu)

[cdimage.ubuntu.com/lubuntu/releases/15.10/release/](http://cdimage.ubuntu.com/lubuntu/releases/15.10/release/) (Lubuntu)

[cdimage.ubuntu.com/ubuntustudio/releases/15.10/release/](http://cdimage.ubuntu.com/ubuntustudio/releases/15.10/release/) (Ubuntu Studio)

[cdimage.ubuntu.com/ubuntu-gnome/releases/15.10/release/](http://cdimage.ubuntu.com/ubuntu-gnome/releases/15.10/release/) (Ubuntu GNOME)

[cdimage.ubuntu.com/ubuntukylin/releases/15.10/release/](http://cdimage.ubuntu.com/ubuntukylin/releases/15.10/release/) (Ubuntu Kylin)

[cdimage.ubuntu.com/ubuntu-mate/releases/15.10/release/](http://cdimage.ubuntu.com/ubuntu-mate/releases/15.10/release/) (Ubuntu MATE)

[cdimage.ubuntu.com/xubuntu/releases/15.10/release/](http://cdimage.ubuntu.com/xubuntu/releases/15.10/release/) (Xubuntu)

##[cdimage.ubuntu.com/mythbuntu/releases/15.10/release/](http://cdimage.ubuntu.com/mythbuntu/releases/15.10/release/) (Mythbuntu)

##[cdimage.ubuntu.com/kubuntu-active/releases/15.10/release/](http://cdimage.ubuntu.com/kubuntu-active/releases/15.10/release/) (Kubuntu Active)



(15-10-upgrading-from-ubuntu-15-04)=
### Upgrading from Ubuntu 15.04

To upgrade on a desktop system:

* Open the "Software & Updates" Setting in System Settings.

* Select the 3rd Tab called "Updates".

* Set the "Notify me of a new Ubuntu version" dropdown menu to "For any new version".

* Press Alt+F2 and type in "update-manager" (without the quotes) into the command box.

* Update Manager should open up and tell you: New distribution release '15.10' is available.

* Click Upgrade and follow the on-screen instructions.

To upgrade on a server system:

* Install the `update-manager-core` package if it is not already installed.

* Make sure the /etc/update-manager/release-upgrades is set to normal.

* Launch the upgrade tool with the command `sudo do-release-upgrade`.

* Follow the on-screen instructions.
Note that the server upgrade will use GNU screen and automatically re-attach in case of dropped connection problems.

There are no offline upgrade options for Ubuntu Desktop and Ubuntu Server. Please ensure you have network connectivity to one of the official mirrors or to a locally accessible mirror and follow the instructions above.


(new-features-in-15-10)=
## New features in 15.10



(15-10-updated-packages)=
### Updated Packages

As with every new release, packages--applications and software of all kinds--are being updated at a rapid pace. Many of these packages came from an automatic sync from [Debian](http://www.debian.org)'s unstable branch; others have been explicitly pulled in for Ubuntu 15.10.

For a list of all packages being accepted for Ubuntu 15.10, please subscribe to [wily-changes](https://lists.ubuntu.com/mailman/listinfo/wily-changes).


(15-10-linux-kernel-4-2)=
### Linux kernel 4.2

Linux 4.2 is another exciting update with the following highlights:

* New AMDGPU kernel driver for supporting recent and near-term Radeon GPUs
* Intel Broxton support
* F2FS file-system encryption support
* NV-DIMM support

A new kernel for the Raspberry Pi 2 has also landed in the official archive.

##
##[systemd](http://freedesktop.org/wiki/Software/systemd/) integration has been improved.


(15-10-ubuntu-desktop)=
### Ubuntu Desktop

The general theme for 15.10 on the desktop is one of bug fixes and incremental quality improvements as well as a more significant change in the move to systemd as an init system.


(15-10-unity)=
#### Unity

Unity has had many bugs fixed and new features added.  Locally integrated menus are now available for unfocussed windows.  There have been a number of usability improvements to the dash.


(15-10-compiz)=
#### Compiz

*  Various fixes and improvements.
*  Refined integration with the MATE desktop.


(15-10-general)=
#### General

* Firefox is updated to version 41 and Chromium is updated to version 45.

* MATE is updated to 1.10.

* Most of the GNOME platform is now based on version 3.16.

* Blueman 2.0 is now included and used by several flavours along with BlueZ 5.35.

* Support for the new Steam Controller - Just install Steam from the Software Center and then pair the controller in Big Picture mode.


(15-10-libreoffice)=
#### LibreOffice

LibreOffice 5.0.2 brings a lot of improvements to entire package.  For more information on these improvements please see the LibreOffice release notes [available here](https://wiki.documentfoundation.org/ReleaseNotes/5.0).

##
##




##
##
##


(15-10-ubuntu-server)=
### Ubuntu Server


(15-10-openstack-liberty)=
#### OpenStack Liberty

Ubuntu 15.10 includes  the latest OpenStack release, Liberty, including the following components:

* OpenStack Identity - Keystone
* OpenStack Imaging - Glance
* OpenStack Block Storage - Cinder
* OpenStack Networking - Neutron
* OpenStack Telemetry - Ceilometer and Aodh
* OpenStack Orchestration - Heat
* OpenStack Dashboard - Horizon
* OpenStack Object Storage - Swift
* OpenStack Database as a Service - Trove
* OpenStack DNS - Designate
* OpenStack Bare-metal - Ironic
* OpenStack Filesystem - Manila
* OpenStack Key Manager - Barbican

Ubuntu 15.10 provides Swift 2.5.0 including experimental support for erasure coded storage.

Please refer to the [OpenStack Liberty release notes](https://wiki.openstack.org/wiki/ReleaseNotes/Liberty) for full details of this release of OpenStack.

OpenStack Liberty is also provided via the [Ubuntu Cloud Archive](https://wiki.ubuntu.com/ServerTeam/CloudArchive) for OpenStack Liberty for Ubuntu 14.04 LTS users.

Ubuntu 15.10 also includes the second Ubuntu release of of the Nova driver for LXD ('nova-compute-lxd'). This driver should not be considered ready for production use and is still provided for experimentation and early testing at this point in time in preparation for its first GA release in 16.04.

**WARNING**: Upgrading an OpenStack deployment is a non-trivial process and care should be taken to plan and test upgrade procedures which will be specific to each OpenStack deployment.

Make sure you read the [OpenStack Charm Release Notes](https://wiki.ubuntu.com/ServerTeam/OpenStackCharms/ReleaseNotes1510) for more information about how to deploy Ubuntu OpenStack using Juju.


(15-10-juju)=
#### Juju

Juju, the service orchestration tool for Ubuntu, has been updated to the latest current stable release, 1.24.6. See the upstream [release notes](https://juju.ubuntu.com/docs/reference-release-notes.html) for full details of all new features and improvements in this release.


(15-10-libvirt-1-2-16)=
#### libvirt 1.2.16

Libvirt has been updated to the 1.2.16 release.


(15-10-qemu-2-3)=
#### qemu 2.3

Qemu has been updated to the 2.3 release.

See [wiki.qemu.org/ChangeLog/2.3](http://wiki.qemu.org/ChangeLog/2.3) for details.


(15-10-open-vswitch-2-4-0)=
#### Open vSwitch 2.4.0

Ubuntu 15.10 includes the latest release of Open vSwitch, 2.4.0.

Ubuntu 15.10 also includes an experimental preview of Open vSwitch integrated with DPDK (Data Plane Development Kit) enabling fast packet processing through userspace usage of compatible networking cards - see the openvswitch-switch-dpdk package for more details.


(15-10-ceph-0-94-3)=
#### Ceph 0.94.3

Ubuntu 15.10 includes the latests stable release of Ceph, 0.94.3 'Hammer'.

For full details on the Ceph Hammer release, please refer to the [upstream release notes](http://ceph.com/docs/master/release-notes/).

##
##
##
##
##
##
##
##
##
##

##
##
##
##
##
##
##
##
##


##
##
##[cloud-images.ubuntu.com/releases/wily/current](http://cloud-images.ubuntu.com/releases/wily/current) for the foreseeable future.
##
##
##
##‘Snappy’ Ubuntu Core is the smallest and most secure edition of Ubuntu. It is a super-lean, transactionally ##updated version of Ubuntu, perfect for inventors, technologists and the active and growing Ubuntu developer ##community, for cloud container hosts and smart, connected devices. It powers drones, robots, network ##switches, mobile base stations, industrial gateways, and IoT home hubs.
##
##


(15-10-known-issues)=
## Known issues

As is to be expected, with any release, there are some significant known bugs that users may run into with this release of Ubuntu 15.10.  The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:



(15-10-boot-installation-and-post-install)=
### Boot, installation and post-install

* In Virtualbox, the installer currently has a bug where after the installation is complete, the installation medium will eject, but you will be unable to press ENTER to reboot. Powering off and back on should boot you into your installed system. This is being tracked in bug Bug:1447038

* The amd64 (Intel x86 64bit) images specifically targeted at Apple hardware (amd64+mac) are no longer produced. Most Apple computers are now capable of booting the amd64 image directly using the EFI (not legacy) boot method so long as their firmware is up to date. If for some reason your hardware doesn't boot properly using the amd64 image, make sure you don't have a pending EFI update and if that still doesn't work, then patch the 64-bit ISO using the software in [bug #1298894](https://bugs.launchpad.net/ubuntu-cdimage/+bug/1298894/comments/16) (tested working on Macbook 2,1). Alternatively, simply use the i386 (32bit) image instead.

* Due to changes in syslinux, it is not currently possible to use usb-creator from 14.04 and earlier releases to write USB images for 15.04 or later; we believe that it is also not possible to use usb-creator from a 15.04 or later system to write USB images for earlier releases.  For now the workaround is to use a matching release of Ubuntu to write the images, but we intend to issue updates soon to work around this incompatibility.  [Bug:1325801](https://help.ubuntu.com/community/Bug:1325801), Bug:1446646 and Bug:1499746


_ During installation on a _blank disk* on a UEFI system, if the user creates custom partitions, the installer displays a 'Force UEFI installation?' dialog while there is no pre-installed system (Bug:1447256). This dialog is not displayed if the custom partitioner is not used. This message is harmless since no previous installation exists on the system and you can proceed with the installation.


* On DELL XPS 13, the EFI partition is wiped if the option "wipe whole disk and install" is selected in the partitioner (Bug:1499323) The EFI partition and the boot can be restored by following the instruction documented in the bug report.

* Binary drivers installed manually during a live session (for example wifi) are not installed on the completed system (Bug:1508063) The workaround is to either do an installation without pre-installing the drivers in the live session, or after installation, install the drivers from the boot medium.

* Randomly during installation in Ubiquity only mode (ie not from a live session) unity-system-settings dies unexpectedly (Bug:1508327) resulting in missing or incorrect windows decorations or other visual issues. This has no impact on the installed system and you can proceed with the installation normally

* golang is now an officially supported language and Ubuntu 15.10 includes golang 1.5, which lacks shared library support. Due to the nature of golang static linking, 3rd party developers desiring bug and security fixes from Ubuntu's updated golang packages will need to rebuild their software with these updates.


(15-10-upgrade)=
### Upgrade

* If several keyboard layouts are configured before upgrade, the wrong layout might be selected after upgrade (Bug:1447157) Re-select the keyboard layout of your choice from the keyboard indicator or system-settings to make it the default. This setting will then persist upon reboot.





(15-10-graphics-and-display)=
### Graphics and Display

* AMD's **fglrx** driver does not work with the current kernel (Bug:1493888). It is warmly recommended to uninstall the fglrx driver before upgrading to Ubuntu 15.10. The open source "radeon" driver can be used as a temporary replacement until a fix is available.




(15-10-official-flavours)=
## Official flavours

The release notes for the official flavours can be found at the following links:

* Kubuntu [wiki.ubuntu.com/WilyWerewolf/ReleaseNotes/Kubuntu](https://wiki.ubuntu.com/WilyWerewolf/ReleaseNotes/Kubuntu)

* Lubuntu [wiki.ubuntu.com/WilyWerewolf/ReleaseNotes/Lubuntu](https://wiki.ubuntu.com/WilyWerewolf/ReleaseNotes/Lubuntu)

* Ubuntu GNOME [wiki.ubuntu.com/WilyWerewolf/ReleaseNotes/UbuntuGNOME](https://wiki.ubuntu.com/WilyWerewolf/ReleaseNotes/UbuntuGNOME)

* Ubuntu Kylin [wiki.ubuntu.com/WilyWerewolf/ReleaseNotes/UbuntuKylin](https://wiki.ubuntu.com/WilyWerewolf/ReleaseNotes/UbuntuKylin)

* Ubuntu MATE [wiki.ubuntu.com/WilyWerewolf/ReleaseNotes/UbuntuMATE](https://wiki.ubuntu.com/WilyWerewolf/ReleaseNotes/UbuntuMATE)

* Ubuntu Studio [wiki.ubuntu.com/WilyWerewolf/ReleaseNotes/UbuntuStudio](https://wiki.ubuntu.com/WilyWerewolf/ReleaseNotes/UbuntuStudio)

* Xubuntu [wiki.ubuntu.com/WilyWerewolf/FinalRelease/Xubuntu](https://wiki.ubuntu.com/WilyWerewolf/FinalRelease/Xubuntu)


(15-10-more-information)=
## More information


(15-10-reporting-bugs)=
### Reporting bugs

Your comments, bug reports, patches and suggestions will help fix bugs and improve the quality of future releases. Please [report bugs using the tools provided](http://help.ubuntu.com/community/ReportingBugs).

If you want to help out with bugs, the [Bug Squad](http://wiki.ubuntu.com/BugSquad) is always looking for help.


(15-10-participate-in-ubuntu)=
### Participate in Ubuntu


If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

[www.ubuntu.com/community/get-involved](http://www.ubuntu.com/community/get-involved)


(15-10-more-about-ubuntu)=
### More about Ubuntu

You can find out more about Ubuntu on the [Ubuntu website](http://www.ubuntu.com) and [Ubuntu wiki](http://wiki.ubuntu.com).

To sign up for future Ubuntu development announcements, please subscribe to Ubuntu's development announcement list at:

[lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce](http://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce)
