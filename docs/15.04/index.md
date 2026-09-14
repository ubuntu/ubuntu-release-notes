---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/VividVervet/ReleaseNotes -->

(ubuntu-15-04-release-notes)=
# Ubuntu 15.04 release notes

(15-04-introduction)=
## Introduction

These release notes for **Ubuntu 15.04** (Vivid Vervet) provide an overview of the release and document the known issues with Ubuntu 15.04 and its flavors.


(15-04-support-lifespan)=
### Support lifespan

Ubuntu 15.04 will be supported for 9 months for Ubuntu Desktop, Ubuntu Server, Ubuntu Core, Kubuntu, Ubuntu Kylin along with all other flavours.


(15-04-official-flavour-release-notes)=
### Official flavour release notes

Find the links to release notes for official flavors [here](https://wiki.ubuntu.com/Official_flavours).


(get-ubuntu-15-04)=
## Get Ubuntu 15.04


(download-ubuntu-15-04)=
### Download Ubuntu 15.04

Images can be downloaded from a location near you.
##
**Note:** The Ubuntu Desktop images are now bigger than a standard CD, and you should use a USB or DVD for installation.

You can download ISOs from:

[releases.ubuntu.com/15.04/](http://releases.ubuntu.com/15.04/) (Ubuntu Desktop, Server, and Snappy Core)

[cloud-images.ubuntu.com/releases/15.04/release/](http://cloud-images.ubuntu.com/releases/15.04/release/) (Ubuntu Cloud Server)

[cdimage.ubuntu.com/netboot/15.04/](http://cdimage.ubuntu.com/netboot/15.04/) (Ubuntu Netboot)


##[cdimage.ubuntu.com/ubuntu-core/releases/15.04/release/](http://cdimage.ubuntu.com/ubuntu-core/releases/15.04/release/) (Ubuntu Core)

##[cdimage.ubuntu.com/edubuntu/releases/15.04/release/](http://cdimage.ubuntu.com/edubuntu/releases/15.04/release/) (Edubuntu DVD)

[cdimage.ubuntu.com/kubuntu/releases/15.04/release/](http://cdimage.ubuntu.com/kubuntu/releases/15.04/release/) (Kubuntu)

[cdimage.ubuntu.com/lubuntu/releases/15.04/release/](http://cdimage.ubuntu.com/lubuntu/releases/15.04/release/) (Lubuntu)

[cdimage.ubuntu.com/ubuntustudio/releases/15.04/release/](http://cdimage.ubuntu.com/ubuntustudio/releases/15.04/release/) (Ubuntu Studio)

[cdimage.ubuntu.com/ubuntu-gnome/releases/15.04/release/](http://cdimage.ubuntu.com/ubuntu-gnome/releases/15.04/release/) (Ubuntu GNOME)

[cdimage.ubuntu.com/ubuntukylin/releases/15.04/release/](http://cdimage.ubuntu.com/ubuntukylin/releases/15.04/release/) (Ubuntu Kylin)

[cdimage.ubuntu.com/ubuntu-mate/releases/15.04/release/](http://cdimage.ubuntu.com/ubuntu-mate/releases/15.04/release/) (Ubuntu MATE)

[cdimage.ubuntu.com/xubuntu/releases/15.04/release/](http://cdimage.ubuntu.com/xubuntu/releases/15.04/release/) (Xubuntu)

##[cdimage.ubuntu.com/mythbuntu/releases/15.04/release/](http://cdimage.ubuntu.com/mythbuntu/releases/15.04/release/) (Mythbuntu)

##[cdimage.ubuntu.com/kubuntu-active/releases/15.04/release/](http://cdimage.ubuntu.com/kubuntu-active/releases/15.04/release/) (Kubuntu Active)



(15-04-upgrading-from-ubuntu-14-10)=
### Upgrading from Ubuntu 14.10

To upgrade on a desktop system:

* Open the "Software & Updates" Setting in Systemsettings.

* Select the 3rd Tab called "Updates".

* Set the "Notify me of a new Ubuntu version" dropdown menu to "For any new version".

* Press Alt+F2 and type in "update-manager" (without the quotes) into the command box.

* Update Manager should open up and tell you: New distribution release '15.04' is available.

* Click Upgrade and follow the on-screen instructions.

To upgrade on a server system:

* Install the `update-manager-core` package if it is not already installed.

* Make sure the /etc/update-manager/release-upgrades is set to normal.

* Launch the upgrade tool with the command `sudo do-release-upgrade`.

* Follow the on-screen instructions.
Note that the server upgrade will use GNU screen and automatically re-attach in case of dropped connection problems.

There are no offline upgrade options for Ubuntu Desktop and Ubuntu Server. Please ensure you have network connectivity to one of the official mirrors or to a locally accessible mirror and follow the instructions above.


(new-features-in-15-04)=
## New features in 15.04



(15-04-updated-packages)=
### Updated Packages

As with every new release, packages--applications and software of all kinds--are being updated at a rapid pace. Many of these packages came from an automatic sync from [Debian](http://www.debian.org)'s unstable branch; others have been explicitly pulled in for Ubuntu 15.04.

For a list of all packages being accepted for Ubuntu 15.04, please subscribe to [vivid-changes](https://lists.ubuntu.com/mailman/listinfo/vivid-changes).


(15-04-linux-kernel-3-19)=
### Linux kernel 3.19

For servers we see a number of performance related improvements including network send batching and the introduction of the data centre congestion algorithm, as well as the introduction of discard support in Device Mapper raid configurations.  There are also improvements to inode locking which should show benefits under heavy load.  Netfilter (nftables) continues to evolve gaining facilities for package logging and dumping.  A number of filesystems gained minor new features, including btrfs which improved its disk replacement in raid 5 and 6 configurations, and support for scrubbing in those.  NFS gained hole punching and preallocation support.  Overlayfs finally moved upstream so simplifying its provision in Ubuntu.  On the networking side we see the start of routing and switch offload support, and the addition of checksum offload for Generic UDP Encapsulation.  Finally we see the introduction of the cutely named foo-over-UDP support, allowing a number of other protocols to nest inside.

On cloud we saw a number of Device Mapper thin storage improvements including performance improvements under high load, and speedier discards in these thin configurations.  Xen saw a number of minor fixes.  For Hyper-v we see the ext2 filesystem gain freeze support allowing default configurations to be snapshotted. Openvswitch continued to evolve gaining basic MPLS support and Geneve tunnelling.

On the security front we see a slew of improvements in Apparmor as well as improved seccomp support including support for cross thread protection.  This release also brings support for signed kexec a key gap in secure boot support.


(15-04-boot-and-service-management)=
### Boot and service management

[systemd](http://freedesktop.org/wiki/Software/systemd/) has replaced [Upstart](http://upstart.ubuntu.com/) as the standard boot and service manager on all Ubuntu flavors except Touch. At the time of the 15.04 release there are no known major problems which prevent booting. The only service which does not currently start is [Juju](https://launchpad.net/bugs/1409639), which will be fixed in a post-release update soon; all other packaged Ubuntu services are expected to work.

Upstart continues to control user sessions.

If your system does not boot after installing or upgrading, please file a bug report and [tag it with `systemd-boot`](https://bugs.launchpad.net/ubuntu/+bugs?field.tag=systemd-boot). Please see [/usr/share/doc/systemd/README.Debian](https://wiki.ubuntu.com/file:///usr/share/doc/systemd/README.Debian) about how to debug early boot or shutdown problems.

You can boot with Upstart once by selecting "Advanced options for Ubuntu" in the GRUB boot menu and starting the "Ubuntu, with Linux ... (upstart)" entry. To switch back permanently, install the `upstart-sysv` package (this will remove `systemd-sysv` and `ubuntu-standard`).

If you use custom or third-party Upstart jobs, you need to write a corresponding systemd service file or SysV init.d script for it. Please see [systemd for Upstart users](https://wiki.ubuntu.com/SystemdForUpstartUsers) for a comprehensive guide.


(15-04-ubuntu-desktop)=
### Ubuntu Desktop

The general theme for 15.04 on the desktop is one of bug fixes and incremental quality improvements as well as a more significant change in the move to systemd as an init system.


(15-04-unity)=
#### Unity

Unity has had many bugs fixed and new features added.  Locally integrated menus are now available for unfocussed windows.  There have been a number of usability improvements to the dash.


(15-04-unity-7-3)=
##### Unity 7.3

*  A configuration option to have menus displayed at all times instead of only on mouseover.

*  Enable the Dash, HUD, or logout dialogs over fullscreen windows.

*  Tweaks to animations for faster startup and shutdown experiences.


(15-04-compiz-0-9-12)=
##### Compiz 0.9.12

*  Fixes for various problems that occur only with the nVidia proprietary driver (mostly blank or black windows) (thanks nVidia).

*  Full integrated support for the MATE desktop on a par with Gnome2 and Unity

*  Refresh of the gtk-window-decorator for Gnome2 support


(15-04-general)=
#### General

Firefox is updated to version 37 and Chromium is updated to version 41.

Most of the Gnome platform is now based on version 3.14.
Qt updated to version 5.4.

Pulseaudio is updated to version 6 paving the way for a move to Bluez5 next release.


(15-04-libreoffice)=
#### LibreOffice

LibreOffice 4.4 brings a lot of improvements including improved change tracking in Writer, improve mail merge performance, improved shapes which can now have fully formatted content with tables etc, more statistics functions in Calc, improved OpenGL support for slide transitions in Impress and Draw, password protected documents in Impress.  Support for digital signed PDF exports has been added, as has support for connecting to Sharepoint and One Drive.  Many new multimedia formats are supported including .ra, .rm, .dv, .ac3, .opus, .asf, and .m4a.

Full details here:
[wiki.documentfoundation.org/ReleaseNotes/4.4](https://wiki.documentfoundation.org/ReleaseNotes/4.4)


(15-04-ubuntu-make-nee-developer-tools-centre)=
#### Ubuntu Make (nee Developer Tools Centre)

Ubuntu Make continues to add support for new platforms, bringing the total to 15 (from 1 last release).  This includes highlights such as:

* Android NDK support and bumped Android Studio to latest version

* Other new IDEs: IDEA (ultimate and community editions), pycharm (professional, educational and community editions), webstorm, rubymine, phpstorm and eclipse

* Golang compiler support

* Firefox developer edition

* Dartlang editor

* Stencyl game development platform

* Numerous usability improvements and accessibility (ppa, doc)

These new features are also available to LTS users.

We also rationalized 3rd party library managers so that they all behave the same and don't overwrite and/or mix with system libraries. Developers don't have to worry about messing up up their installation if they want to install PyPI, npm, rubygem libraries.


(15-04-ubuntu-server)=
### Ubuntu Server


(15-04-openstack-2015-1)=
#### OpenStack 2015.1

At the point of 15.04 release, all OpenStack projects are at the latest Kilo release candidate for 2015.1 - the final 2015.1 release versions will be delivered as a stable release update post 15.04 release.

* OpenStack Identity - Keystone
* OpenStack Imaging - Glance
* OpenStack Block Storage - Cinder
* OpenStack Networking - Neutron
* OpenStack Telemetry - Ceilometer
* OpenStack Orchestration - Heat
* OpenStack Dashboard - Horizon
* OpenStack Object Storage - Swift

Ubuntu 15.04 includes Swift 2.2.2; this is not the final release version of Swift for OpenStack Kilo as this introduced new dependencies to support Erasure coding which it was not possible to support for 15.04 release.

For OpenStack 2015.1, Ubuntu is only tracking the decomposition of Neutron FWaaS, LBaaS and VPNaaS from Neutron core in the Ubuntu archive; we expect to add additional packages for other Neutron ML2 mechanism drivers and plugins early during the Liberty/15.10 development cycle - we'll provide these as backports to OpenStack Kilo users as and when they become available.

* OpenStack Database as a Service - Trove
* OpenStack DNS as a Service - Designate
* OpenStack Bare-metal Compute Driver - Ironic
* OpenStack Filesystem - Manila

OpenStack 2015.1 is also provided via the [Ubuntu Cloud Archive](https://wiki.ubuntu.com/ServerTeam/CloudArchive) for OpenStack Kilo for Ubuntu 14.04 LTS users.

Ubuntu 15.04 also includes the first Ubuntu release of of the Nova Compute driver for LXD ('nova-compute-lxd'). This driver should not be considered ready for production use and is provided for experimentation and early testing at this point in time.

**WARNING**: Upgrading an OpenStack deployment is a non-trivial process and care should be taken to plan and test upgrade procedures which will be specific to each OpenStack deployment.

Make sure you read the [OpenStack Charm Release Notes](https://wiki.ubuntu.com/ServerTeam/OpenStackCharms/ReleaseNotes1504) for more information about how to deploy Ubuntu OpenStack using Juju.


(15-04-lxc)=
#### LXC

The LXC container manager was updated to the latest upstream version, 1.1. More specifically the 1.1.2 bugfix release. This brings full systemd support, both on the host and in the container as well as new features such as checkpoint/restore using CRIU, openvswitch support and support for qcow2 backed containers.

More details on the new LXC release can be found at: [linuxcontainers.org/lxc/news/](https://linuxcontainers.org/lxc/news/)

This new version of LXC also comes with a new helper filesystem called LXCFS. That filesystem exposes the container resource limits into the container so that tools like free, top, ... report them properly. It's also a vital part of making Systemd work properly in containers.

More details on the new LXCFS release can be found at: [linuxcontainers.org/lxcfs/news/](https://linuxcontainers.org/lxcfs/news/)

CGManager, the LXC CGroup manager was also updated to version 0.36, fixing many bugs and introducing some new features that were needed for LXCFS.

More details on the new CGManager release can be found at: [linuxcontainers.org/cgmanager/news/](https://linuxcontainers.org/cgmanager/news/)


(15-04-lxd)=
#### LXD

Ubuntu 15.04 is the first Ubuntu release to feature LXD.

LXD has been developped to provide a fast, reliable and scalable way to manage system containers across the network.
It's entirely image based, secure by default, supports snapshots, live migration and offers a simple yet powerful REST API.

LXD ships with two clients:

 - lxc, a command line client for small and medium size deployments where the operator doesn't mind or prefers manual control.

 - nova-compute-lxd, an OpenStack Nova plugin which makes managing containers as simple as managing virtual machines.

Ubuntu 15.04 ships with LXD 0.7. This is the result of an intense 6 months of development and while not ready for production workloads, it's definitely ready for experimentation.

More details on LXD can be found at: [linuxcontainers.org/lxd](https://linuxcontainers.org/lxd)


(15-04-juju)=
#### Juju

Juju, the service orchestration tool for Ubuntu, has been updated to the latest current stable release, 1.20.10. See the upstream [release notes](https://juju.ubuntu.com/docs/reference-release-notes.html) for full details of all new features and improvements in this release.


MySQL has been updated to 5.6 and remains in main. In universe, Percona XtraDB Cluster has been updated to 5.6, MariaDB to 10.0 and Percona Server 5.6 has been added.

With the switch to systemd, process limits such as the maximum number of open files can now be controlled by tuning the unit configuration file, and MySQL and variant daemons are already limited by systemd defaults. If you are already tuning these values, we recommend that you remove any open_files_limit type configuration settings from my.cnf and configure everything from the systemd unit file instead in order to avoid conflicts between configurations in both locations. See [bug 1434758](https://launchpad.net/bugs/1434758) for details.


(15-04-libvirt-1-2-12)=
#### libvirt 1.2.12

Libvirt has been updated to the 1.2.12 release.  A profile script has been added to automatically set the default URI on a xen system.


(15-04-qemu-2-2)=
#### qemu 2.2

Qemu has been updated to the 2.2 release.  The default vga device has been switched to stdvga.  If this is an issue, the old default can be explicitly requested using '-vga cirrus'.

See [wiki.qemu.org/ChangeLog/2.2](http://wiki.qemu.org/ChangeLog/2.2) for details.


(15-04-open-vswitch-2-3-1)=
#### Open vSwitch 2.3.1

Ubuntu 15.04 includes the latest release of Open vSwitch, 2.3.1.  For this release DKMS packages are no longer provided as part of Ubuntu as kernels since 3.13 provide sufficiently new in-tree openvswitch modules.


(15-04-ceph-0-94-1)=
#### Ceph 0.94.1

Ubuntu 15.04 includes the latests stable release of Ceph, 0.94.1 'Hammer'.

For full details on the Ceph Hammer release, please refer to the [upstream release notes](http://ceph.com/docs/master/release-notes/).


(15-04-cloud-init-0-7-7)=
#### cloud-init 0.7.7

Cloud-init now uses Python 3, and uses systemd.  It supports running on Digital Ocean and base64 encoded user-data on Google Compute.  Chef support is also improved.


(15-04-docker-1-5-0)=
#### docker 1.5.0

The release notes describing the features available in docker 1.5 are located here: [docs.docker.com/v1.5/release-notes/](https://docs.docker.com/v1.5/release-notes/)

In addition to the features outlined above, we have provided experimental support for ppc64el and arm64.


(15-04-ha-related-package-updates)=
#### HA related package updates

* corosync 2.3.4
* haproxy 1.5.0
* pacemaker 1.1.12


(15-04-amazon-aws-i386-amis-deprecated)=
#### Amazon AWS i386 AMI's Deprecated

Starting with Ubuntu 15.04, i386 AMI's are now deprecated. Users are advised to migrate new workloads to 64-bit HVM instance types. i386 Cloud Images will continue to be published at [cloud-images.ubuntu.com/releases/vivid/current](http://cloud-images.ubuntu.com/releases/vivid/current) for the foreseeable future.


(15-04-ubuntu-core-snappy)=
### Ubuntu Core (Snappy)

15.04 is the first release that includes snappy Ubuntu Core, a new Ubuntu rendition that uses a new, transactional packaging system: snappy.

‘Snappy’ Ubuntu Core is the smallest and most secure edition of Ubuntu. It is a super-lean, transactionally updated version of Ubuntu, perfect for inventors, technologists and the active and growing Ubuntu developer community, for cloud container hosts and smart, connected devices. It powers drones, robots, network switches, mobile base stations, industrial gateways, and IoT home hubs.

All developers and system builders need to know about the details of this new Ubuntu rendition and how to start using snappy Ubuntu Core 15.04 can be found on [developer.ubuntu.com/snappy](http://developer.ubuntu.com/snappy).


(15-04-known-issues)=
## Known issues

As is to be expected, with any release, there are some significant known bugs that users may run into with this release of Ubuntu 15.04.  The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:



(15-04-boot-installation-and-post-install)=
### Boot, installation and post-install

* The amd64 (Intel x86 64bit) images specifically targeted at Apple hardware (amd64+mac) are no longer produced. Most Apple computers are now capable of booting the amd64 image directly using the EFI (not legacy) boot method so long as their firmware is up to date. If for some reason your hardware doesn't boot properly using the amd64 image, make sure you don't have a pending EFI update and if that still doesn't work, then  patch the 64-bit ISO using the software in [bug #1298894](https://bugs.launchpad.net/ubuntu-cdimage/+bug/1298894/comments/16) (tested working on Macbook 2,1). Alternatively, simply use the i386 (32bit) image instead.

* Due to changes in syslinux, it is not currently possible to use usb-creator from 14.04 and earlier releases to write USB images for 14.10; we believe that it is also not possible to use usb-creator from a 14.10 system to write USB images for earlier releases.  For now the workaround is to use a matching release of Ubuntu to write the images, but we intend to issue updates soon to work around this incompatibility.  [Bug:1325801](https://help.ubuntu.com/community/Bug:1325801)

* In Virtualbox, the installer currently has a bug where after the installation is complete, the installation medium will eject, but you will be unable to press ENTER to reboot. Powering off and back on should boot you into your installed system. This is being tracked in bug Bug:1447038

* On OEM installations, after the end user configuration in a different language than the default initial OEM installation, extra language packs are not installed (Bug:1446539) You can install extra language packs by selecting "Language Support" in "System Settings". A dialog will prompt you to install missing language packs.

_ During installation on a _blank disk* on a UEFI system, if the user creates custom partitions, the installer displays a 'Force UEFI installation?' dialog while there is no pre-installed system (Bug:1447256). This dialog is not displayed if the custom partitioner is not used. This message is harmless since no previous installation exists on the system and you can proceed with the installation.

* Systems running multipath with a very large number of paths might experience long delays and issues during boot (for example, failure to mount the root filesystem or other filesystems); for details and work-around see bug Bug:1467989.


(15-04-upgrade)=
### Upgrade

* If several keyboard layouts are configured before upgrade, the wrong layout might be selected after upgrade (Bug:1447157) Re-select the keyboard layout of your choice from the keyboard indicator or system-settings to make it the default. This setting will then persist upon reboot.








(15-04-official-flavours)=
## Official flavours

The release notes for the official flavours can be found at the following links:

* Kubuntu [wiki.ubuntu.com/VividVervet/ReleaseNotes/Kubuntu](https://wiki.ubuntu.com/VividVervet/ReleaseNotes/Kubuntu)

* Lubuntu [wiki.ubuntu.com/VividVervet/ReleaseNotes/Lubuntu](https://wiki.ubuntu.com/VividVervet/ReleaseNotes/Lubuntu)

* Ubuntu GNOME [wiki.ubuntu.com/VividVervet/ReleaseNotes/UbuntuGNOME](https://wiki.ubuntu.com/VividVervet/ReleaseNotes/UbuntuGNOME)

* Ubuntu Kylin [wiki.ubuntu.com/VividVervet/ReleaseNotes/UbuntuKylin](https://wiki.ubuntu.com/VividVervet/ReleaseNotes/UbuntuKylin)

* Ubuntu MATE [wiki.ubuntu.com/VividVervet/ReleaseNotes/UbuntuMATE](https://wiki.ubuntu.com/VividVervet/ReleaseNotes/UbuntuMATE)

* Ubuntu Studio [wiki.ubuntu.com/VividVervet/ReleaseNotes/UbuntuStudio](https://wiki.ubuntu.com/VividVervet/ReleaseNotes/UbuntuStudio)

* Xubuntu [wiki.ubuntu.com/VividVervet/ReleaseNotes/Xubuntu](https://wiki.ubuntu.com/VividVervet/ReleaseNotes/Xubuntu)


(15-04-more-information)=
## More information


(15-04-reporting-bugs)=
### Reporting bugs

Your comments, bug reports, patches and suggestions will help fix bugs and improve the quality of future releases. Please [report bugs using the tools provided](http://help.ubuntu.com/community/ReportingBugs).

If you want to help out with bugs, the [Bug Squad](http://wiki.ubuntu.com/BugSquad) is always looking for help.


(15-04-participate-in-ubuntu)=
### Participate in Ubuntu


If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

[www.ubuntu.com/community/get-involved](http://www.ubuntu.com/community/get-involved)


(15-04-more-about-ubuntu)=
### More about Ubuntu

You can find out more about Ubuntu on the [Ubuntu website](http://www.ubuntu.com) and [Ubuntu wiki](http://wiki.ubuntu.com).

To sign up for future Ubuntu development announcements, please subscribe to Ubuntu's development announcement list at:

[lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce](http://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce)
