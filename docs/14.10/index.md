---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/UtopicUnicorn/ReleaseNotes -->

(ubuntu-14-10-release-notes)=
# Ubuntu 14.10 release notes

(14-10-introduction)=
## Introduction

These release notes for **Ubuntu 14.10** (Utopic Unicorn) provide an overview of the release and document the known issues with Ubuntu 14.10 and its flavors.


(14-10-support-lifespan)=
### Support lifespan

Ubuntu 14.10 will be supported for 9 months for Ubuntu Desktop, Ubuntu Server, Ubuntu Core, Kubuntu, Ubuntu Kylin along with all other flavours.


(14-10-official-flavour-release-notes)=
### Official flavour release notes

Find the links to release notes for official flavors [here](https://wiki.ubuntu.com/Official_flavours).


(get-ubuntu-14-10)=
## Get Ubuntu 14.10


(download-ubuntu-14-10)=
### Download Ubuntu 14.10

Images can be downloaded from a location near you.
##
**Note:** The Ubuntu Desktop images are now bigger than a standard CD, and you should use a USB or DVD for installation.

You can download ISOs from:

[releases.ubuntu.com/14.10/](http://releases.ubuntu.com/14.10/) (Ubuntu Desktop and Server)

[cloud-images.ubuntu.com/releases/14.10/release/](http://cloud-images.ubuntu.com/releases/14.10/release/) (Ubuntu Cloud Server)

[cdimage.ubuntu.com/netboot/14.10/](http://cdimage.ubuntu.com/netboot/14.10/) (Ubuntu Netboot)

[cdimage.ubuntu.com/ubuntu-core/releases/14.10/release/](http://cdimage.ubuntu.com/ubuntu-core/releases/14.10/release/) (Ubuntu Core)

[cdimage.ubuntu.com/kubuntu/releases/14.10/release/](http://cdimage.ubuntu.com/kubuntu/releases/14.10/release/) (Kubuntu)

[cdimage.ubuntu.com/lubuntu/releases/14.10/release/](http://cdimage.ubuntu.com/lubuntu/releases/14.10/release/) (Lubuntu)

[cdimage.ubuntu.com/ubuntustudio/releases/14.10/release/](http://cdimage.ubuntu.com/ubuntustudio/releases/14.10/release/) (Ubuntu Studio)

[cdimage.ubuntu.com/ubuntu-gnome/releases/14.10/release/](http://cdimage.ubuntu.com/ubuntu-gnome/releases/14.10/release/) (Ubuntu GNOME)

[cdimage.ubuntu.com/ubuntukylin/releases/14.10/release/](http://cdimage.ubuntu.com/ubuntukylin/releases/14.10/release/) (UbuntuKylin)

[cdimage.ubuntu.com/xubuntu/releases/14.10/release/](http://cdimage.ubuntu.com/xubuntu/releases/14.10/release/) (Xubuntu)

[cdimage.ubuntu.com/mythbuntu/releases/14.10/release/](http://cdimage.ubuntu.com/mythbuntu/releases/14.10/release/) (Mythbuntu)

##[cdimage.ubuntu.com/kubuntu-active/releases/14.10/release/](http://cdimage.ubuntu.com/kubuntu-active/releases/14.10/release/) (Kubuntu Active)



(14-10-upgrading-from-ubuntu-14-04-lts)=
### Upgrading from Ubuntu 14.04 LTS

To upgrade on a desktop system:

* Open the "Software & Updates" Setting in Systemsettings.

* Select the 3rd Tab called "Updates".

* Set the "Notify me of a new Ubuntu version" dropdown menu to "For any new version".

* Press Alt+F2 and type in "update-manager" (without the quotes) into the command box.

* Update Manager should open up and tell you: New distribution release '14.10' is available.

* Click Upgrade and follow the on-screen instructions.

To upgrade on a server system:

* Install the `update-manager-core` package if it is not already installed.

* Make sure the /etc/update-manager/release-upgrades is set to normal.

* Launch the upgrade tool with the command `sudo do-release-upgrade`.

* Follow the on-screen instructions.
Note that the server upgrade will use GNU screen and automatically re-attach in case of dropped connection problems.

There are no offline upgrade options for Ubuntu Desktop and Ubuntu Server. Please ensure you have network connectivity to one of the official mirrors or to a locally accessible mirror and follow the instructions above.


(new-features-in-14-10)=
## New features in 14.10

Please see the [Utopic blueprint list](https://blueprints.launchpad.net/ubuntu/utopic/+specs) for details.

Please test and report any bugs you find:

[help.ubuntu.com/community/ReportingBugs](http://help.ubuntu.com/community/ReportingBugs)


(14-10-updated-packages)=
### Updated Packages

As with every new release, packages--applications and software of all kinds--are being updated at a rapid pace. Many of these packages came from an automatic sync from [Debian](http://www.debian.org)'s unstable branch; others have been explicitly pulled in for Ubuntu 14.10.

For a list of all packages being accepted for Ubuntu 14.10, please subscribe to [utopic-changes](https://lists.ubuntu.com/mailman/listinfo/utopic-changes).


(14-10-linux-kernel-3-16)=
#### Linux kernel 3.16

The Ubuntu 14.10 release delivers a v3.16 based kernel.  This brings a significant number of bug fixes and new hardware support including expanded architecture support for Power 8 and arm64 platforms.  It also includes support for Intel Cherryview, Haswell, Broadwell and Merrifield systems, and initial support for Nvidia GK20A and GK110B GPU’s.  There is improved graphics performance on many Nvidia, Intel and ATI Radeon devices and also audio improvements with support for the Radeon .264 video encoder.  Expanded platform support is enabled via support for 64 bit EFI boot on 32 bit EFI BIOS.  This release also brings performance improvements in suspend/resume times.

For developers we see significant improvements in tracing and debugging with new triggers for kernel trace points, and expansion of uprobe support.  This release also brings a new experimental deadline CPU scheduler.

For servers we see better support for bursty workloads, improved resident set tracking, and a better NUMA migration strategy.  Filesystem support is also improved with faster file allocations for database use and several filesystems show performance improvements including XFS and Btrfs.  XFS now has stabilized its v5 format and sports expanded direct I/O support.  Btrfs now supports per directory switchable compression modes.  raid5 performance is also improved. This release also brings improvements to networking, including a new packet scheduler for high latency links, and efforts to bring IPv6 support in line with IPv4.  We see performance improvements for openvswitch and VTI tunneling.  As always, various new pieces of hardware are now supported including Intel AVX-512 and Intel MXP.

On cloud we see Hyper-V, XEN, and KVM networking performance improvements.  Hyper-V now supports the hypervisor driven file copy and reference time services.  For KVM we see improved support for passing through new x86 vector instructions.

On the security front we see full Kernel Address Space Layout Randomisation applied to the kernel and its modules, plus the closure of a number of information leaks in /proc.  We also see additional support for cryptographic devices.


(14-10-apparmor)=
#### AppArmor

AppArmor added support for fine-grained mediation of unix(7) abstract and anonymous sockets and also added various policy updates and bug fixes. AppArmor policy has been adjusted for packages that ship it to work with these changes, but local policy may need to be adjusted unix rules. See `man 5 apparmor.d` for details.


(14-10-oxide)=
#### Oxide

Oxide has been updated to use the latest Chromium Content API and includes numerous bug fixes and features to better support webbrowser-app, webapps and apps using UbuntuWebViews. Oxide is a webview based on Chromium to deliver web content. Oxide allows us to better support 3rd party developers and applications within the Ubuntu archive by providing a fast, secure and up to date webengine library for the duration of this release. While other web content libraries such as those based on webkit are available, their maintenance will be limited to new upstream minor version releases only, and application developers are encouraged to use Oxide instead.


(14-10-ubuntu-desktop)=
### Ubuntu Desktop

The general theme for 14.10 on the desktop is one of bug fixes and
incremental quality improvements.


(14-10-unity)=
#### Unity

Unity has had many bugs fixed and features improved support for High-DPI
displays.


(14-10-general)=
#### General

Firefox is updated to version 33 and Chromium is updated to version 38.

Gtk updated to version 3.12.
Qt updated to version 5.3.

Support for IPP Everywhere printers is added, and printers shared from
Ubuntu can emulate IPP Everywhere printers.  IPP printers require no
configuration under Ubuntu.  More information about IPP Everywhere is
available here:  [www.pwg.org/ipp/everywhere.html](http://www.pwg.org/ipp/everywhere.html)


(14-10-libreoffice)=
#### LibreOffice

LibreOffice 4.3 brings a lot of improvements including improved PDF
support, new features in Writer, Calc and Impress (word processor,
spreadsheet and presentations).  Full details here:
[wiki.documentfoundation.org/ReleaseNotes/4.3](https://wiki.documentfoundation.org/ReleaseNotes/4.3)


(14-10-ubuntu-developer-tools-centre)=
#### Ubuntu Developer Tools Centre

This new tool allows developers to quickly and easily setup a variety of
development environments on their Ubuntu Desktop.  More information here:
[blog.didrocks.fr/post/Ubuntu-loves-Developers](http://blog.didrocks.fr/post/Ubuntu-loves-Developers)


(14-10-xorg)=
#### Xorg

With Xorg 1.16, we have better support for non-pci devices. Xephyr now
supports DRI3. The mesa 10.3 update has support for AMD Hawaii GPU's,
improved support for dri3 offloading, the freedreno open source driver,
and preliminary support for using nouveau on maxwell devices.


(14-10-ubuntu-server)=
### Ubuntu Server


(14-10-openstack-2014-1)=
#### OpenStack 2014.1

Ubuntu 14.10 includes the OpenStack 2014.2 (Juno) release of the following projects in Ubuntu main:

* OpenStack Compute - Nova
* OpenStack Identity - Keystone
* OpenStack Imaging - Glance
* OpenStack Block Storage - Cinder
* OpenStack Networking - Neutron
* OpenStack Object Storage - Swift
* OpenStack Telemetry - Ceilometer
* OpenStack Orchestration - Heat
* OpenStack Dashboard - Horizon

**WARNING**: Upgrading an OpenStack deployment is a non-trivial process and care should be taken to plan and test upgrade procedures which will be specific to each OpenStack deployment.

Make sure you read the [OpenStack Charm Release Notes](https://wiki.ubuntu.com/UtopicUnicorn/ReleaseNotes/OpenStackCharms) for more information.


(14-10-libvirt-1-2-8)=
#### Libvirt 1.2.8

Containers launched with libvirt-lxc can now be apparmor-protected.

Libvirt now provides cgmanager support allowing use of libvirt inside containers without cgroups mounted.

Migration of pc-1.0 VMs from a 12.04 host must be done first to a 14.04 host, to the pc-1.0-precise machine type.  From there, they may be converted to a new machine type, such as pc-i440fx-trusty, and migrated to a 14.10 host.


(14-10-qemu-2-1)=
#### Qemu 2.1

Kvm is now supported on the ppc64le architecture.


(14-10-cgmanager-0-32)=
#### Cgmanager 0.32

Cgmanager now has a new compiled client tool, and supports new methods including Prune, ListTasksRecursive, and ListControllers.  It now supports the features needed for systemd-shim to properly close sessions.


(14-10-lxc-1-1)=
#### LXC 1.1

This includes container checkpoint and restart as a tech preview.


(14-10-cloud-init-0-7-6)=
#### cloud-init 0.7.6

Cloud-init 0.7.6 brings several bug fixes along with support for booting ubuntu with systemd. Also featured is improvements when using vendor-data on OpenStack.


(14-10-bcache)=
#### bcache

bcache support is now included as a technology preview, enabled in the kernel and via the userspace package bcache-tools, but without installer support. We highly recommend that you take full system backups before experimenting with it. It has been enabled with a focus on server use cases. Some desktop use cases should also work, but we have observed some issues when attempting to combine bcache use with LVM and md.


(14-10-juju)=
#### Juju

Juju, the service orchestration tool for Ubuntu, has been updated to the latest current stable release, 1.22.1. See the upstream [release notes](https://juju.ubuntu.com/docs/reference-release-notes.html) for full details of all new features and improvements in this release.


(14-10-docker)=
#### Docker

Docker 1.2 is released in Utopic.  For the absolute latest upstream version of Docker, please follow the instructions here [docs.docker.com/installation/ubuntulinux/](https://docs.docker.com/installation/ubuntulinux/) titled "If you'd like to try the latest version of Docker"


(14-10-maas)=
#### MAAS

MAAS has been updated to the latest current beta release, 1.7-beta8. Many new features have been added, and lots of bugfixes too. Full [release notes](http://maas.ubuntu.com/docs/changelog.html) will be available shortly.


(14-10-known-issues)=
## Known issues

As is to be expected, with any release, there are some significant known bugs that users may run into with this release of Ubuntu 14.10.  The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:



(14-10-boot-installation-and-post-install)=
### Boot, installation and post-install

* The amd64 (Intel x86 64bit) images specifically targeted at Apple hardware (amd64+mac) are no longer produced. Most Apple computers are now capable of booting the amd64 image directly using the EFI (not legacy) boot method so long as their firmware is up to date. If for some reason your hardware doesn't boot properly using the amd64 image, make sure you don't have a pending EFI update and if that still doesn't work, then  patch the 64-bit ISO using the software in [bug #1298894](https://bugs.launchpad.net/ubuntu-cdimage/+bug/1298894/comments/16) (tested working on Macbook 2,1). Alternatively, simply use the i386 (32bit) image instead.

* Due to changes in syslinux, it is not currently possible to use usb-creator from 14.04 and earlier releases to write USB images for 14.10; we believe that it is also not possible to use usb-creator from a 14.10 system to write USB images for earlier releases.  For now the workaround is to use a matching release of Ubuntu to write the images, but we intend to issue updates soon to work around this incompatibility.  [Bug:1325801](https://help.ubuntu.com/community/Bug:1325801)

* Machines with ATI/AMD video cards may be getting blank or entirely turned off screen at boot. The screen will switch on when the X server starts. If you need it to turn on prior to that, for example to unlock an encrypted harddisk hitting ESC twice should reset the video card to a working state.

* An update to shim in 14.10 introduces a bug where, when booting on a UEFI system with SecureBoot disabled, the boot is delayed for two seconds and a message "Booting in insecure mode" is displayed on the screen.  This message does not indicate a security problem with Ubuntu and does not interfere with the operation of the system except for introducing this boot delay.  As a workaround to avoid this boot delay, users can enable SecureBoot if enabled on their hardware, or if they do not intend to use SecureBoot at all they can uninstall the shim-signed package and then rerun the `grub-install` command. [Bug:1384973](https://help.ubuntu.com/community/Bug:1384973)


(14-10-upgrade)=
### Upgrade


(14-10-power-management)=
### Power Management


(14-10-desktop)=
### Desktop


(14-10-migration)=
### Migration


(14-10-graphics-and-display)=
### Graphics and Display


(14-10-networking)=
### Networking


(14-10-kernel)=
### Kernel

* When booting virtual machines installed with encrypted root and using "VGA" as the video adapter it may not be possible to enter the unlock password.  Switching Video to QXL will allow booting of these instance.  (See LP:1383851 for details.)


_For a listing of more known issues, please refer to the Utopic Unicorn [bug tracker](https://bugs.launchpad.net/ubuntu/utopic/+bugs) in Launchpad._


(14-10-official-flavours)=
## Official flavours

The release notes for the official flavours can be found at the following links:

* Kubuntu [wiki.ubuntu.com/UtopicUnicorn/ReleaseNotes/Kubuntu](https://wiki.ubuntu.com/UtopicUnicorn/ReleaseNotes/Kubuntu)

* Lubuntu [wiki.ubuntu.com/UtopicUnicorn/ReleaseNotes/Lubuntu](https://wiki.ubuntu.com/UtopicUnicorn/ReleaseNotes/Lubuntu)

* Mythbuntu [wiki.ubuntu.com/UtopicUnicorn/ReleaseNotes/Mythbuntu](https://wiki.ubuntu.com/UtopicUnicorn/ReleaseNotes/Mythbuntu)

* Ubuntu GNOME [wiki.ubuntu.com/UtopicUnicorn/ReleaseNotes/UbuntuGNOME](https://wiki.ubuntu.com/UtopicUnicorn/ReleaseNotes/UbuntuGNOME)

* Ubuntu Kylin [wiki.ubuntu.com/UtopicUnicorn/ReleaseNotes/UbuntuKylin](https://wiki.ubuntu.com/UtopicUnicorn/ReleaseNotes/UbuntuKylin)

* Ubuntu Studio [wiki.ubuntu.com/UtopicUnicorn/ReleaseNotes/UbuntuStudio](https://wiki.ubuntu.com/UtopicUnicorn/ReleaseNotes/UbuntuStudio)

* Xubuntu [wiki.ubuntu.com/UtopicUnicorn/ReleaseNotes/Xubuntu](https://wiki.ubuntu.com/UtopicUnicorn/ReleaseNotes/Xubuntu)


(14-10-more-information)=
## More information


(14-10-reporting-bugs)=
### Reporting bugs

Your comments, bug reports, patches and suggestions will help fix bugs and improve the quality of future releases. Please [report bugs using the tools provided](http://help.ubuntu.com/community/ReportingBugs).

If you want to help out with bugs, the [Bug Squad](http://wiki.ubuntu.com/BugSquad) is always looking for help.


(14-10-participate-in-ubuntu)=
### Participate in Ubuntu


If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

[www.ubuntu.com/community/get-involved](http://www.ubuntu.com/community/get-involved)


(14-10-more-about-ubuntu)=
### More about Ubuntu

You can find out more about Ubuntu on the [Ubuntu website](http://www.ubuntu.com) and [Ubuntu wiki](http://wiki.ubuntu.com).

To sign up for future Ubuntu development announcements, please subscribe to Ubuntu's development announcement list at:

[lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce](http://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce)
