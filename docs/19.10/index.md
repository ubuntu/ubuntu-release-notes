---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/EoanErmine/ReleaseNotes -->

(ubuntu-19-10-release-notes)=
# Ubuntu 19.10 release notes

(19-10-introduction)=
## Introduction

These release notes for **Ubuntu 19.10** (Eoan Ermine) provide an overview of the release and document the known issues with Ubuntu 19.10 and its flavours.


(19-10-support-lifespan)=
### Support lifespan

Ubuntu 19.10 will be supported for 9 months until [July 2020](https://wiki.ubuntu.com/Releases). If you need Long Term Support, it is recommended you use [Ubuntu 18.04 LTS](https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes) instead.


(19-10-official-flavour-release-notes)=
### Official flavour release notes

Find the links to release notes for official flavors [here](https://wiki.ubuntu.com/Official_flavours).


(get-ubuntu-19-10)=
## Get Ubuntu 19.10


(download-ubuntu-19-10)=
### Download Ubuntu 19.10

Images can be downloaded from a location near you.

You can download ISOs and flashable images from:

[releases.ubuntu.com/19.10/](http://releases.ubuntu.com/19.10/) (Ubuntu Desktop and Server for AMD64)

[cdimage.ubuntu.com/ubuntu/releases/19.10/release/](http://cdimage.ubuntu.com/ubuntu/releases/19.10/release/) (Less Frequently Downloaded Ubuntu Images)

[cloud-images.ubuntu.com/daily/server/eoan/current/](http://cloud-images.ubuntu.com/daily/server/eoan/current/) (Ubuntu Cloud Images)

[cdimage.ubuntu.com/netboot/19.10/](http://cdimage.ubuntu.com/netboot/19.10/) (Ubuntu Netboot)

[cdimage.ubuntu.com/kubuntu/releases/19.10/release/](http://cdimage.ubuntu.com/kubuntu/releases/19.10/release/) (Kubuntu)

[cdimage.ubuntu.com/lubuntu/releases/19.10/release/](http://cdimage.ubuntu.com/lubuntu/releases/19.10/release/) (Lubuntu)

[cdimage.ubuntu.com/ubuntu-budgie/releases/19.10/release/](http://cdimage.ubuntu.com/ubuntu-budgie/releases/19.10/release/) (Ubuntu Budgie)

[cdimage.ubuntu.com/ubuntukylin/releases/19.10/release/](http://cdimage.ubuntu.com/ubuntukylin/releases/19.10/release/) (Ubuntu Kylin)

[cdimage.ubuntu.com/ubuntu-mate/releases/19.10/release/](http://cdimage.ubuntu.com/ubuntu-mate/releases/19.10/release/) (Ubuntu MATE)

[cdimage.ubuntu.com/ubuntustudio/releases/19.10/release/](http://cdimage.ubuntu.com/ubuntustudio/releases/19.10/release/) (Ubuntu Studio)

[cdimage.ubuntu.com/xubuntu/releases/19.10/release/](http://cdimage.ubuntu.com/xubuntu/releases/19.10/release/) (Xubuntu)


(19-10-upgrading-from-ubuntu-19-04)=
### Upgrading from Ubuntu 19.04

To upgrade on a desktop system:

* Open the "Software & Updates" application.

* Select the 3rd Tab called "Updates".

* Set the "Notify me of a new Ubuntu version" dropdown menu to "For any new version".

* Press Alt+F2 and type in "update-manager -c -d" (without the quotes) into the command box.

* Update Manager should open up and tell you: New distribution release '19.10' is available.

* If not you can also use "/usr/lib/ubuntu-release-upgrader/check-new-release-gtk"

* Click Upgrade and follow the on-screen instructions.

To upgrade on a server system:

* Install the `update-manager-core` package if it is not already installed.

* Make sure the `Prompt` line in /etc/update-manager/release-upgrades is set to `Prompt=normal`.

* Launch the upgrade tool with the command `do-release-upgrade`.

* Follow the on-screen instructions.
Note that the server upgrade will use GNU screen and automatically re-attach in case of dropped connection problems.

There are no offline upgrade options for Ubuntu Desktop and Ubuntu Server. Please ensure you have network connectivity to one of the official mirrors or to a locally accessible mirror and follow the instructions above.


(19-10-upgrades-on-i386)=
#### Upgrades on i386

Users of the i386 architecture will not be presented with an upgrade to Ubuntu 19.10.  Support for i386 as a host architecture is dropped in 19.10.


(new-features-in-19-10)=
## New features in 19.10



(19-10-updated-packages)=
### Updated Packages


(19-10-linux-kernel)=
#### Linux kernel 🐧

Ubuntu 19.10 is based on the Linux release series **5.3**. It adds a variety of new hardware support since the 5.0 kernel from 19.04, including support for AMD Navi GPUs, new ARM SoCs, ARM Komeda display, and Intel Speed Select on Xeon servers. Significant developer-facing features include pidfd support for avoiding races cause by pid reuse, a new mount api, and the io_uring interface for asynchronous I/O. To help improve boot speed the default kernel compression algorithm was changed to lz4 on most architectures, and the default initramfs compression algorithm was changed to lz4 on all architectures.


(19-10-toolchain-upgrades)=
#### Toolchain Upgrades 🛠️

Ubuntu 19.10 comes with refreshed state-of-the-art toolchain including new upstream releases of glibc 2.30, ☕ OpenJDK 11, rustc 1.37, GCC 9.2, updated 🐍 Python 3.7.5, Python 3.8.0 (interpreter only), 💎 ruby 2.5.5, php 7.3.8, 🐪 perl 5.28.1, golang 1.12.10. There are new improvements on the cross-compilers front as well with POWER and AArch64 toolchain enabled to cross-compile for ARM, PPC64 LE, S390X and RISCV64 targets.



(19-10-security-improvements)=
### Security Improvements 🔒

Ubuntu 19.10 comes with additional default hardening options enabled in GCC, including support for both stack clash protection and control-flow integrity protection. All packages in main have been rebuilt to take advantage of this, with a few exceptions.


(19-10-ubuntu-desktop)=
### Ubuntu Desktop


(19-10-gnome-3-34-desktop)=
#### GNOME 3.34 Desktop

19.10 includes GNOME 3.34 which includes a lot of bug fixes, some new features and a significant improvement in responsiveness and speed.

* You can group icons in the Activities overview by dragging and dropping on to other icons or groups

* Improved wallpaper settings

* Improved wifi settings

* You can read the 3.34 release notes here: [help.gnome.org/misc/release-notes/3.34/](https://help.gnome.org/misc/release-notes/3.34/)

* Xwayland apps [are now supported running as root/sudo](https://bugs.launchpad.net/bugs/1652282).

* Improved performance:

  * Consistently higher and smoother frame rates

  * Lower output latency in Xorg sessions (by one frame) for most graphics drivers

  * Lower input latency for some devices such as touchpad scrolling and keyboards

  * Lower CPU usage


(ubuntu-19-10-new-features)=
#### Ubuntu 19.10 New Features

* Plug in a USB drive and access it directly from the dock

* New themes:  Yaru light and dark variants are now available.  Install GNOME Tweaks to easily switch your default.

* Support for DLNA sharing is now available by default.  Share you videos to your smart TV.

* Added support for WPA3

* The Chromium browser is only available as a snap in 19.10.  [This blog post has more details.](https://ubuntu.com/blog/chromium-in-ubuntu-deb-to-snap-transition)


(19-10-zfs-on-root)=
#### ZFS on root

* Support for ZFS as the root filesystem is added as an experimental feature in 19.10

* Create the ZFS file system and partitioning layout automatically direct from the installer

* You can read more details on Didrocks' blog [here](https://didrocks.fr/2019/08/06/ubuntu-zfs-support-in-19.10-introduction/) and [here](https://didrocks.fr/2019/10/11/ubuntu-zfs-support-in-19.10-zfs-on-root/).


(19-10-nvidia-specific-improvements)=
#### NVIDIA-specific Improvements

* The driver is now included in the ISO

* Improved startup reliability when the NVIDIA driver is in use ([1](https://bugs.launchpad.net/bugs/1798790), [2](https://bugs.launchpad.net/bugs/1705369))

* Improved rendering smoothness and frame rates [specifically for NVIDIA](https://gitlab.gnome.org/GNOME/mutter/merge_requests/602)


(19-10-updated-applications)=
#### Updated Applications

* LibreOffice 6.3
* Firefox 69
* Thunderbird 68


(19-10-updated-subsystems)=
#### Updated Subsystems

* [PulseAudio 13.0](https://www.freedesktop.org/wiki/Software/PulseAudio/Notes/13.0/)


(19-10-ubuntu-server)=
### Ubuntu Server


(19-10-images)=
#### Images

The ppc64el and arm64 live-server ISO images are now considered production ready and are the preferred media to install Ubuntu Server on bare metal on the two architectures.


(19-10-qemu)=
#### QEMU

QEMU was updated to 4.0 release.

See the [4.0](http://wiki.qemu.org/ChangeLog/4.0) change log for major changes since Ubuntu 19.04.

Migrations from former versions are supported just as usual. When upgrading it is always recommended to [upgrade the machine types](https://wiki.ubuntu.com/QemuKVMMigration#Upgrade_machine_type) allowing guests to fully benefit from all the improvements and fixes of the most recent version.

Qemu now has [virglrenderer](https://virgil3d.github.io/) enabled which allows to create a virtual 3D GPU inside qemu virtual machines. That is inferior to GPU passthrough, but can be handy if the platform used lacks the capability for classic [PCI passthrough](https://www.linux-kvm.org/page/How_to_assign_devices_with_VT-d_in_KVM) as well as more modern [mediated devices](https://www.kernel.org/doc/Documentation/vfio-mediated-device.txt).


(19-10-libvirt)=
#### libvirt

libvirt was updated to version 5.6. See the upstream [change log](https://libvirt.org/news.html) for details since version 5.0 that was in Ubuntu 19.04.

Among many other changes worth to mention is the ability to enable QEMUs ability to use [parallel connections for migration](http://manpages.ubuntu.com/manpages/eoan/man1/virsh.1.html) which can help to speed up migrations if one doesn't saturate your network yet.


(19-10-dpdk)=
#### dpdk

Ubuntu includes the latest release 18.11.2 of the 18.11.x latest stable series of DPDK. The very latest (non-stable) version being 19.08 was not chosen for downstream projects of DPDK (like Open vSwitch) not being compatible yet.

See the [18.11.1](https://doc.dpdk.org/guides-18.11/rel_notes/release_18_11.html#release-notes) and [18.11.2](https://doc.dpdk.org/guides-18.11/rel_notes/release_18_11.html#id1) release notes for details.


(19-10-open-vswitch)=
#### Open vSwitch

Open vSwitch has been updated to 2.12.

Please read the [release notes](http://openvswitch.org/releases/NEWS-2.12.0) for more detail.


(19-10-mysql-8-0)=
#### MySQL 8.0

MySQL has been updated to 8.0. See [What Is New in MySQL 8.0](https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html) for upstream documentation on the changes introduced in MySQL 8, including features that have been deprecated or removed. The packaging also introduces [MySQL Router](https://dev.mysql.com/doc/mysql-router/8.0/en/) in the mysql-router package in universe for additional HA and scalability capabilities, with a view towards introducing it into main in the next Ubuntu release.


(19-10-php-7-3)=
#### PHP 7.3

PHP 7.3 brings some refinements to the language: Flexible heredoc and newdoc syntaxes, JSON_THROW_ON_ERROR, list() reference assignment, and several new functions.  Case-insensitive constants and several functions have been deprecated and/or removed, so developers moving to 7.3 may find it help to review the [7.2 to 7.3 migration guide](https://www.php.net/manual/en/migration73.php).





(19-10-raspberry-pi)=
#### Raspberry Pi 🍓

Our Ubuntu 19.10 Raspberry Pi 32-bit and 64-bit preinstalled images (raspi3) now support the Raspberry Pi 4 platform out-of-the-box. With this, our images now support almost all modern flavors of the Raspberry Pi family of devices (Pi 2B, Pi 3B, Pi 3A+, Pi 3B+, CM3, CM3+, Pi 4B).




(19-10-openstack-train)=
#### OpenStack Train

Ubuntu 19.10 includes the latest OpenStack release, Train, including the following components:

* OpenStack Identity - Keystone
* OpenStack Imaging - Glance
* OpenStack Block Storage - Cinder
* OpenStack Compute - Nova
* OpenStack Networking - Neutron
* OpenStack Telemetry - Ceilometer, Aodh, Gnocchi, and Panko
* OpenStack Orchestration - Heat
* OpenStack Dashboard - Horizon
* OpenStack Object Storage - Swift
* OpenStack Database as a Service - Trove
* OpenStack DNS as a Service - Designate
* OpenStack Bare-metal - Ironic
* OpenStack Filesystem - Manila
* OpenStack Key Manager - Barbican



**WARNING**: Upgrading an OpenStack deployment is a non-trivial process and care should be taken to plan and test upgrade procedures which will be specific to each OpenStack deployment.

Make sure you read the [OpenStack Charm Release Notes](https://docs.openstack.org/charm-guide/latest/1910.html) for more information about how to deploy Ubuntu OpenStack using Juju.


(19-10-cloud-init)=
#### cloud-init

The version was updated from 18.5 to [19.2](https://launchpad.net/cloud-init/trunk/19.2). Notable new features include:

* Add new Exoscale datasource

* DataSourceOracle: configure secondary NICs on Virtual Machines

* net: add rfc3442 (classless static routes) to EphemeralDHCP (Bug:1821102)

* cloud-init analyze reporting on boot events.

* Azure now supports waking from preprovision state via netlink messages.

* New cli command 'cloud-id' to display what cloud on which an instance is running.

* write_files config module now supports appending to a file

* Allow identification of OpenStack by Asset Tag (Bug:1669875)

* instance-data.json standardized platform and subplatform values

* select ubuntu archive mirror for armel, armhf, and arm64

* Azure datasource telemetry, network configuration and ssh key hardening

* new config module for interacting with third party drivers on Ubuntu

* EC2 Classic instance support for network config changes across reboot

* Add support for the com.vmware.guestInfo OVF transport.

* Scaleway: Support ssh keys provided inside an instance tag.

* Better NoCloud support for case-insensitive fs labels.

**_NOTE_**: Cloud-init frequently publishes updates to the **eoan-updates** apt repository pocket with updated versions of cloud-init per the [cloud-init stable release update process (SRU)](https://wiki.ubuntu.com/CloudinitUpdates).  Machines with [unattended upgrades configured](https://help.ubuntu.com/lts/serverguide/automatic-updates.html) will automatically get those cloud-init updates.


(19-10-curtin)=
#### curtin

The version was updated from [19.2](https://launchpad.net/curtin/trunk/19.2). Notable new features include:

* Add opportunistic zkey encryption (s390x)

* block-discover cli/API for exporting existing storage devices to config

* add subcommand schema for storage-config validation

* Add support for s390 DASD devices

* Support for multi-layers images fsimage-layered:// URI

* storage_config: interpret value, not presence, of DM_MULTIPATH_DEVICE_PATH [Michael Hudson-Doyle]

* block-discover: handle multipath disks (Bug:1839915)

* vmtests: significant performance improvements in test configuration, scheduling and image syncs

* vmtests: enable arm64 testing


(19-10-s390x)=
#### s390x

IBM Z and LinuxONE / s390x-specific enhancements (since 19.04) include (partly not limited to s390x):

* Enhanced support for existing and especially new hardware (Bug:1830742), (Bug:1842774) is a primary task, not only with kernel focus - new hardware CPU models got introduced (Bug:1830239), enhanced hardware diagnose added (Bug:1829270), the diagnose data for the Linux kernel enhanced (Bug:1829270), but also with virtualization/KVM focus - with IO enhancements introduced for KVM guests (Bug:1834533), DASD pass-through support added (Bug:1843892) and again the new hardware models for Qemu/KVM (Bug:1830238), (Bug:1836066) and (Bug:1828038).

* Based on the new IBM z15 and LinuxONE III hardware generation secure boot (IPL) was introduced for zFCP/SCSI disks. This affects not only the kernel (Bug:1829027), (Bug:1830617), (Bug:1843960), (Bug:1843961), but also the installer and QEMU/KVM (Bug:1830243).

* The s390-tools upgrade to v2.11.0 comes with several enhancements, not limited to secure boot (IPL) support for SCSI (Bug:1825351), (Bug:1843879) as well as zkey improvements (Bug:1836907).

* The CPU_MF hardware counters were significantly enhanced as well - this work concerned again several components like the kernel (Bug:1834201), (Bug:1836739), (Bug:1836340), but also perf (Bug:1837051) and libpfm (Bug:1837016).

* In addition virt-manager was updated (Bug:1827069) as well as boot configuration override added (Bug:1826856).

* There is now also improved hardware support for zlib to gain performance improvements (Bug:1823157).

* Patches got included for optimized s390x zlib compression (Bug:1825350) and to increase gzip performance (Bug:1839123), (Bug:1841052). This allows to make use of hardware-accelerated deflate, offered by the Integrated Accelerator for zEDC on z15 and LinuxONE III.

* The kernel compression method was changed to LZ4 to improve boot speed (Bug:1840934), (Bug:1841193).

* Version bump to new upstream release of libhugetlbfs v2.21 (Bug:1825216).

* smc-tools got upgraded to latest v1.2.1 (Bug:1825217).

* Upgrade to latest upstream valgrind v3.15 with some improvements and s390x fixes (Bug:1828219).

* Updated tool-chain to latest gcc 9.2 (Bug:1825346) and LLVM 9.0 (Bug:1836343).

* And with lifting glibc to 2.30 new instructions support were added that leads to performance improvements (Bug:1825349).

* The upgrade of libdfp to v1.0.14 introduces significant s390x decimal floating-point hardware improvements and exploitation (Bug:1836532).

* libatlas libraries are not available in optimized versions for selected s390x hardware - z13 and z14 (Bug:1837577).

* The PCI subsystem obtained some modifications and fixes for MIO (Bug:1825352), (Bug:1844668) and directed interrupt support (Bug:1825353).

* SIMD accelerated implementations for poly1305 (Bug:1736704) and chacha20 (Bug:1736705) were added to openssl.

* On top openssl-ibmca was lifted to the very latest v2.1.0 (Bug:1826198), (Bug:1836865) as well as libica(3) to v3.6.0 (Bug:1826194), (Bug:1836866).

* With the upgrade of opencryptoki to v3.11.1 (Bug:1826193), that includes various bug fixes, support for the opencryptoki ica tokens CKM_SHA256_RSA_PKCS_PSS, CKM_SHA384_RSA_PKCS_PSS and CKM_SHA512_RSA_PKCS_PSS was added (Bug:1835048) - especially in regard to TLS 1.3 and it's GSKit support.

* Further cryptography improvements include libp11 upgrade to v0.4.10 (Bug:1830730) in support of OpenSC, zcryptstats added to the s390-tools package to introduce support for measurements of crypto hardware (Bug:1821918) and kernel crypto modification on the seeding of PRNG with (on-chip CPACF-based) TRNG (Bug:1835553) and the concurrent handling (add and remove events) of AP facilities (Bug:1835554).

* Finally several security and integrity aspects got addressed, for example with the introduction of KASLR (kernel address space layout randomization) - to support the load of the kernel to a random location in protection against certain attacks (Bug:1832626) and the splitting of DIF and DIX boot time controls (Bug:1836608) that now allows hardware-based DIF data integrity checking between FCP channel and target LUNs without the need of the (partly considered unstable) DIX feature.


(19-10-cloud-images)=
### Cloud Images ☁


(19-10-kvm-optimized-guest-images)=
#### KVM-optimized guest images

A new amd64 qcow2 image has been added.  The [daily eoan builds](https://cloud-images.ubuntu.com/eoan/current/) are named eoan-server-cloudimg-amd64-disk-kvm.img and contain the [linux-kvm](https://launchpad.net/ubuntu/+source/linux-kvm) kernel.

This image aims to provide an experience specific for the KVM hypervisor. This image does not have initramfs, and it offers multiple performance enhancements targeted at virtualized environments. Users should expect a shorter boot time when using the new KVM hypervisor image compared to traditional images.


(19-10-known-issues)=
## Known Issues

As is to be expected, with any release, there are some significant known bugs that users may run into with this release of Ubuntu 19.10.  The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:


(19-10-desktop)=
### Desktop


(19-10-enabling-wayland-support-with-the-nvidia-proprietary-driver)=
#### Enabling Wayland support with the NVIDIA proprietary driver

This is not something we recommend due to [a number of bugs](https://bugs.launchpad.net/ubuntu/+bugs?field.tag=nvidia-drm.modeset). But if you want to try it out then a new step is required in 19.10:

1. Add kernel parameter `nvidia-drm.modeset=1`

 2. Comment out the nvidia line in `/usr/lib/udev/rules.d/61-gdm.rules`

 3. As step 2 may have reintroduced [an old bug](https://bugs.launchpad.net/bugs/1705369) you might need to disable the integrated graphics/GPU in your BIOS.


(19-10-fractional-scaling-in-xorg-sessions)=
#### Fractional scaling in Xorg sessions

If you enable fractional scaling in Xorg sessions then you may encounter reduced performance and screen tearing. There are two possible workarounds:

* Only use scaling factors that are multiples of 100%; or

* Log into "Ubuntu on Wayland" instead.


(19-10-live-session-can-take-a-long-time-to-start)=
#### Live Session can take a long time to start

On older hardware with a slow install medium (e.g. older USB drive) the live session can take a few minutes to start while seeding the default snaps finishes.


(19-10-ext4-instead-of-zfs-displayed-in-confirmation-dialog)=
#### ext4 instead of ZFS displayed in confirmation dialog

When the user continues after having selected to install the system with ZFS, the "Write to change disks" message prints that an ext4 partition will be created. This is technically correct but confusing to the user. (Bug:1847719)


(19-10-unable-to-shutdown-or-restart-from-the-log-in-screen)=
#### Unable to shutdown or restart from the log in screen

The restart and shutdown options no longer work in the log in screen. This is being tracked in (Bug:1847896).


(19-10-wrong-bootloader-device-with-2-or-more-drives)=
#### Wrong Bootloader Device with 2 or more drives

When installing a system with more than one drive, drive selection and bootloader selection may end up out of sync when choosing a non-first drive. [LP #1847898](https://bugs.launchpad.net/bugs/1847898)

To ensure the correct boot loader device perform the following steps:

* Select the last "Something Else" option
* Select desired boot loader device from the drop-down
* Click back
* Select guided partitioning option
* Select desired installation device
* Continue installation

This will ensure that the desired device is used both for the boot loader and root filesystem.






(19-10-raspberry-pi-2)=
### Raspberry Pi


(19-10-pimoroni-fan-shim-pauses-boot)=
#### Pimoroni Fan Shim pauses boot

The [Pimoroni Fan Shim](https://pinout.xyz/pinout/fan_shim#) for the Raspberry Pi 4 re-uses the serial console pins, pins 8 and 10 (GPIO14 and GPIO15 respectively), on the GPIO header to control its RGB LED. This results in "noise" on the serial line which stops u-boot during startup (as it thinks a key has been pressed). Adding the following line to `/boot/firmware/syscfg.txt` disables the serial console permitting the boot sequence to complete:

```none
enable_uart=0
```


(19-10-official-flavours)=
## Official flavours

The release notes for the official flavours can be found at the following links:

* Kubuntu [wiki.ubuntu.com/EoanErmine/ReleaseNotes/Kubuntu](https://wiki.ubuntu.com/EoanErmine/ReleaseNotes/Kubuntu)

* Lubuntu [lubuntu.me/eoan-released/](https://lubuntu.me/eoan-released/)

* Ubuntu Budgie [ubuntubudgie.org/blog/2019/10/17/19-10-ubuntu-budgie-released](https://ubuntubudgie.org/blog/2019/10/17/19-10-ubuntu-budgie-released)

* Ubuntu Kylin [www.ubuntukylin.com/news/1910_released-en.html](http://www.ubuntukylin.com/news/1910_released-en.html)

* Ubuntu MATE [ubuntu-mate.org/blog/ubuntu-mate-19-10-eoan-ermine-release/](https://ubuntu-mate.org/blog/ubuntu-mate-19-10-eoan-ermine-release/)

* Ubuntu Studio [wiki.ubuntu.com/EoanErmine/ReleaseNotes/UbuntuStudio](https://wiki.ubuntu.com/EoanErmine/ReleaseNotes/UbuntuStudio)

* Xubuntu [wiki.xubuntu.org/releases/19.10/release-notes](https://wiki.xubuntu.org/releases/19.10/release-notes)


(19-10-more-information)=
## More information


(19-10-reporting-bugs)=
### Reporting bugs

Your comments, bug reports, patches and suggestions will help fix bugs and improve the quality of future releases. Please [report bugs using the tools provided](http://help.ubuntu.com/community/ReportingBugs).

If you want to help out with bugs, the [Bug Squad](http://wiki.ubuntu.com/BugSquad) is always looking for help.


(19-10-participate-in-ubuntu)=
### Participate in Ubuntu


If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

[community.ubuntu.com/contribute](https://community.ubuntu.com/contribute)


(19-10-more-about-ubuntu)=
### More about Ubuntu

You can find out more about Ubuntu on the [Ubuntu website](https://www.ubuntu.com) and [Ubuntu wiki](https://wiki.ubuntu.com).

To sign up for future Ubuntu development announcements, please subscribe to Ubuntu's development announcement list at:

[lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce](https://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce)
