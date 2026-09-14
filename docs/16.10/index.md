---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/YakketyYak/ReleaseNotes -->

(ubuntu-16-10-release-notes)=
# Ubuntu 16.10 release notes

**WARNING: Release reached End of Life**

**This release is no longer supported, please see [Releases](https://help.ubuntu.com/community/Releases)**

**WARNING: Release reached End of Life**


(16-10-introduction)=
## Introduction

These release notes for **Ubuntu 16.10** (Yakkety Yak) provide an overview of the release and document the known issues with Ubuntu 16.10 and its flavors.


(16-10-support-lifespan)=
### Support lifespan

Ubuntu 16.10 was supported for 9 months until [July 2017](https://wiki.ubuntu.com/Releases).


(16-10-official-flavour-release-notes)=
### Official flavour release notes

Find the links to release notes for official flavors [here](https://wiki.ubuntu.com/Official_flavours).


(get-ubuntu-16-10)=
## Get Ubuntu 16.10


(download-ubuntu-16-10)=
### Download Ubuntu 16.10

Images can be downloaded from a location near you.

You can download ISOs and flashable images from from:

[releases.ubuntu.com/16.10/](http://releases.ubuntu.com/16.10/) (Ubuntu Desktop and Server)

[cdimage.ubuntu.com/ubuntu/releases/16.10/](http://cdimage.ubuntu.com/ubuntu/releases/16.10/) (Less Popular Ubuntu Images)

[cloud-images.ubuntu.com/releases/16.10/](http://cloud-images.ubuntu.com/releases/16.10/) (Ubuntu Cloud Server)

[cdimage.ubuntu.com/netboot/16.10/](http://cdimage.ubuntu.com/netboot/16.10/) (Ubuntu Netboot)

[cdimage.ubuntu.com/kubuntu/releases/16.10/](http://cdimage.ubuntu.com/kubuntu/releases/16.10/) (Kubuntu)

[cdimage.ubuntu.com/lubuntu/releases/16.10/](http://cdimage.ubuntu.com/lubuntu/releases/16.10/) (Lubuntu)

[cdimage.ubuntu.com/ubuntustudio/releases/16.10/](http://cdimage.ubuntu.com/ubuntustudio/releases/16.10/) (Ubuntu Studio)

[cdimage.ubuntu.com/ubuntu-gnome/releases/16.10/](http://cdimage.ubuntu.com/ubuntu-gnome/releases/16.10/) (Ubuntu GNOME)

[cdimage.ubuntu.com/ubuntukylin/releases/16.10/](http://cdimage.ubuntu.com/ubuntukylin/releases/16.10/) (Ubuntu Kylin)

[cdimage.ubuntu.com/ubuntu-mate/releases/16.10/](http://cdimage.ubuntu.com/ubuntu-mate/releases/16.10/) (Ubuntu MATE)

[cdimage.ubuntu.com/xubuntu/releases/16.10/](http://cdimage.ubuntu.com/xubuntu/releases/16.10/) (Xubuntu)

##[cdimage.ubuntu.com/mythbuntu/releases/16.10/](http://cdimage.ubuntu.com/mythbuntu/releases/16.10/) (Mythbuntu)

##[cdimage.ubuntu.com/edubuntu/releases/16.10/](http://cdimage.ubuntu.com/edubuntu/releases/16.10/) (Edubuntu DVD)


(16-10-upgrading-from-ubuntu-16-04-lts)=
### Upgrading from Ubuntu 16.04 LTS

To upgrade on a desktop system:

* Open the "Software & Updates" Setting in System Settings.

* Select the 3rd Tab called "Updates".

* Set the "Notify me of a new Ubuntu version" dropdown menu to "For any new version".

* Press Alt+F2 and type in "update-manager" (without the quotes) into the command box.

* Update Manager should open up and tell you: New distribution release '16.10' is available.

* If not you can also use "/usr/lib/ubuntu-release-upgrader/check-new-release-gtk"

* Click Upgrade and follow the on-screen instructions.

To upgrade on a server system:

* Install the `update-manager-core` package if it is not already installed.

* Make sure the `Prompt` line in /etc/update-manager/release-upgrades is set to normal.

* Launch the upgrade tool with the command `sudo do-release-upgrade`.

* Follow the on-screen instructions.
Note that the server upgrade will use GNU screen and automatically re-attach in case of dropped connection problems.

There are no offline upgrade options for Ubuntu Desktop and Ubuntu Server. Please ensure you have network connectivity to one of the official mirrors or to a locally accessible mirror and follow the instructions above.


(new-features-in-16-10)=
## New features in 16.10



(16-10-updated-packages)=
### Updated Packages


(16-10-linux-kernel-4-8)=
#### Linux kernel 4.8

Ubuntu 16.10 is based on the Linux release series 4.8.


(16-10-gpg)=
#### gpg

_ The _gpg* binary is now provided by [gnupg2](https://debian-administration.org/users/dkg/weblog/116).


(16-10-ubuntu-desktop)=
### Ubuntu Desktop

* **LibreOffice 5.2** has been updated to [5.2](https://wiki.documentfoundation.org/ReleaseNotes/5.2). Ubuntu now uses the [GTK3](https://caolanm.blogspot.com/2016/02/native-gtk3-menubar-in-libreoffice.html) version by default.

* Update Manager now shows changelog entries for **PPAs** too (Bug:253119).

* Apps provided by GNOME have been updated to at least **3.20**. Many apps have been updated to **3.22** also.

* The **Nautilus** file browser has been [updated](https://csorianognome.wordpress.com/2015/09/04/nautilus-3-18-comunicating-changes/) to [3.20](https://csorianognome.wordpress.com/2016/02/08/nautilus-3-20-and-looking-forward/).

* **systemd** is now used for [user sessions](https://lists.ubuntu.com/archives/ubuntu-devel/2016-July/039465.html). System sessions had already been provided by systemd in previous Ubuntu releases.


(16-10-ubuntu-server)=
### Ubuntu Server


(16-10-openstack-newton)=
#### OpenStack Newton

Ubuntu 16.10 includes  the latest OpenStack release, Newton, including the following components:

* OpenStack Identity - Keystone
* OpenStack Imaging - Glance
* OpenStack Block Storage - Cinder
* OpenStack Compute - Nova
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

Please refer to the [OpenStack Newton release notes](http://releases.openstack.org/newton/) for full details of this release of OpenStack.

OpenStack Newton is also provided via the [Ubuntu Cloud Archive](https://wiki.ubuntu.com/OpenStack/CloudArchive) for OpenStack Newton for Ubuntu 16.04 LTS users.

**WARNING**: Upgrading an OpenStack deployment is a non-trivial process and care should be taken to plan and test upgrade procedures which will be specific to each OpenStack deployment.

Make sure you read the [OpenStack Charm Release Notes](http://docs.openstack.org/developer/charm-guide/1610.html) for more information about how to deploy Ubuntu OpenStack using Juju.


(16-10-qemu-2-6-1)=
#### qemu 2.6.1

Qemu has been updated to the 2.6.1 release.

See the [Changelog](http://wiki.qemu.org/ChangeLog/2.6) for details.
This already includes a stable releases, more about that can be found at [2.6.1 stable release](https://lists.gnu.org/archive/html/qemu-devel/2016-08/msg03137.html).

Additionally this includes a backport to enable GPU Passthru for ppc64le.


(16-10-dpdk-16-07)=
#### DPDK 16.07

Ubuntu 16.10 includes the latest release of DPDK, 16.07.

See the [Release Notes](http://dpdk.org/doc/guides/rel_notes/release_16_07.html) for details.

Noteworthy for DPDK application developers is that upstream deprecated the old mechanism of a combined shared library.
libdpdk.so is now a linker script referring to the - individually packaged - sub-libraries librte-*.
Furthermore the DPDK related kernel modules are now provided as dkms based packages.


(16-10-libvirt-2-1)=
#### libvirt 2.1

Libvirt has been updated to version 2.1.
See the [Changelogs](https://libvirt.org/news.html) for details.

In order to reduce the Debian delta, the main libvirt service has been renamed to libvirtd.service. libvirt-bin.service becomes an alias to maintain backwards compatibility.


(16-10-open-vswitch)=
#### Open vSwitch

Open vSwitch has been updated to the latest release, 2.6.

See the Open vSwitch [News](http://openvswitch.org/releases/NEWS-2.6.0) for mroe details.

The enablement of openvswitch-switch-dpdk has changed upstream.
So if you are upgrading from a previously dpdk enabled configuration then you will need to update your enablement appropriately.
See associated Readme at /usr/share/doc/openvswitch-switch-dpdk/README.Debian for details.


(16-10-lxd-2-4-1)=
#### LXD 2.4.1

Ubuntu 16.10 ships with LXD 2.4.1. The main highlights for this new version of LXD are:

* Support for AppArmor profile stacking. This allows containers to load their own AppArmor profiles, further securing tasks running inside LXD containers.

* Building on the new AppArmor feature, it is now possible to install Snap packages inside LXD containers. For the time being, this is only possible with Ubuntu 16.10 containers that have the "squashfuse" package installed.

* New network management features have been added to LXD, allowing the creation and management of bridges, DHCP settings, tunnels, ... More information can be found from "lxc network help" and in the upstream [documentation](https://github.com/lxc/lxd/blob/master/doc/configuration.md#network-configuration).

A full changelog can be found at: [linuxcontainers.org/lxd/news/](https://linuxcontainers.org/lxd/news/)

LXD 2.4.1 can also be tried online at: [linuxcontainers.org/lxd/try-it/](https://linuxcontainers.org/lxd/try-it/)


(16-10-cloud-init)=
#### cloud-init

All of cloud-init's recent development has been brought back to 16.04,
so you've probably already used it in production!
Some recent improvements include:

* changes with systemd integration to better enforce order of boot which improve the reliability of configuring disks and network.

* bug fixes

* updated documentation on [http://cloudinit.readthedocs.io](http://cloudinit.readthedocs.io/en/latest/)

* new format for [configuring apt](https://git.launchpad.net/cloud-init/tree/doc/examples/cloud-config-apt.txt)

* support for [configuring ntp](http://cloudinit.readthedocs.io/en/latest/topics/modules.html#ntp)

* support for [configuring lxd](http://cloudinit.readthedocs.io/en/latest/topics/modules.html#lxd) 2.3+.

* Improvements and support for network configuration on Digital Ocean, SmartOS, NoCloud, ConfigDrive.


(16-10-docker-1-12-1)=
#### docker 1.12.1

The docker.io package has been updated to version 1.12.1.  See the associated upstream release notes: [github.com/docker/docker/releases/tag/v1.12.1](https://github.com/docker/docker/releases/tag/v1.12.1)


(16-10-ubuntu-on-ibm-linuxone-and-z-systems)=
### Ubuntu on IBM LinuxONE and z Systems

There are many improvements specific to the IBM mainframe s390x architecture, in addition to all of the above mentioned features:

* s390-tools updated to 1.36.1 with support for dasd quick format
* Addition of the numactl package
* Hardware acceleration enabled in OpenSSL
* zfcpdump kernel is now available

And many other general bugfixes and improvements.


(16-10-known-issues)=
## Known issues

As is to be expected, with any release, there are some significant known bugs that users may run into with this release of Ubuntu 16.10.  The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:


(16-10-boot-installation-and-post-install)=
### Boot, installation and post-install

* Wifi shows no ap in oem end user mode, work around reboot the machine and then everything should work as expected (Bug:1633012)

* Bluetooth driver on XPS13 9434 not functioning at all (Bug:1633019)


(16-10-powerpc)=
#### PowerPC

* Choosing an Entire Disk install on PowerPC will result in an un-bootable system. The work around is to manually partition your hard disk and create a 1GB `ext2` /boot partition. One also needs to move `/etc/yaboot.conf` to `/boot/etc/yaboot.conf` and symlink it back. (Bug:1606089)


(16-10-gcc)=
#### GCC

* We have modified GCC to by-default compile programs with [position independent executable support](https://en.wikipedia.org/wiki/Position-independent_code#PIE), on the amd64 and ppc64el architectures, to improve the security benefits provided by [Address Space Layout Randomization](https://en.wikipedia.org/wiki/Address_space_layout_randomization).

This may cause difficulty when trying to compile Linux kernels that [still need this patch applied.](https://patchwork.ozlabs.org/patch/616621/)

Other programs may experience other problems; some debugging guidelines are at [wiki.ubuntu.com/SecurityTeam/PIE](https://wiki.ubuntu.com/SecurityTeam/PIE)


(16-10-apparmor)=
#### AppArmor

* The Linux kernel recently changed how executables are run. AppArmor
  profiles that were developed on previous versions of the Linux kernel may
  require modification to allow the programs to work.

Error messages will be logged (to dmesg or to auditd, if that is installed) that look like this:

`... apparmor="DENIED" operation="file_mmap" ... profile="/usr/sbin/tcpdump" name="/usr/sbin/tcpdump" ... requested_mask="m" denied_mask="m" ...`

Often the profile and the name will match but this is not required.

The aa-logprof program from the apparmor-utils package can interactively prompt the user for previously-logged AppArmor messages. To run it, use `sudo aa-logprof`.




(16-10-desktop)=
### Desktop

* GTK+ 3.20 requires theme developers to make changes to their themes. Many (but not all) popular themes are now compatible with GTK+ 3.20.

* Unity 8 session sometimes locks up when you press Print Screen (Bug:1525285)

* Unity 8 session locks up when you press media meta keys such as play/pause. (Bug:1633046)

* Unity 8 Web Browser has no sound. (Bug:1632620)





(16-10-official-flavours)=
## Official flavours

The release notes for the official flavours can be found at the following links:

* Kubuntu [wiki.ubuntu.com/YakketyYak/ReleaseNotes/Kubuntu](https://wiki.ubuntu.com/YakketyYak/ReleaseNotes/Kubuntu)

* Lubuntu [wiki.ubuntu.com/YakketyYak/ReleaseNotes/Lubuntu](https://wiki.ubuntu.com/YakketyYak/ReleaseNotes/Lubuntu)

* Ubuntu GNOME [wiki.ubuntu.com/YakketyYak/ReleaseNotes/UbuntuGNOME](https://wiki.ubuntu.com/YakketyYak/ReleaseNotes/UbuntuGNOME)

* Ubuntu Kylin [wiki.ubuntu.com/YakketyYak/ReleaseNotes/UbuntuKylin](https://wiki.ubuntu.com/YakketyYak/ReleaseNotes/UbuntuKylin)

* Ubuntu MATE [ubuntu-mate.org/blog/ubuntu-mate-yakkety-final-release/](https://ubuntu-mate.org/blog/ubuntu-mate-yakkety-final-release/)

* Ubuntu Studio [wiki.ubuntu.com/YakketyYak/ReleaseNotes/UbuntuStudio](https://wiki.ubuntu.com/YakketyYak/ReleaseNotes/UbuntuStudio)

* Xubuntu [xubuntu.org/news/xubuntu-16-10-release](https://xubuntu.org/news/xubuntu-16-10-release)


(16-10-more-information)=
## More information


(16-10-reporting-bugs)=
### Reporting bugs

Your comments, bug reports, patches and suggestions will help fix bugs and improve the quality of future releases. Please [report bugs using the tools provided](http://help.ubuntu.com/community/ReportingBugs).

If you want to help out with bugs, the [Bug Squad](http://wiki.ubuntu.com/BugSquad) is always looking for help.


(16-10-participate-in-ubuntu)=
### Participate in Ubuntu


If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

[www.ubuntu.com/community/get-involved](http://www.ubuntu.com/community/get-involved)


(16-10-more-about-ubuntu)=
### More about Ubuntu

You can find out more about Ubuntu on the [Ubuntu website](http://www.ubuntu.com) and [Ubuntu wiki](http://wiki.ubuntu.com).

To sign up for future Ubuntu development announcements, please subscribe to Ubuntu's development announcement list at:

[lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce](http://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce)
