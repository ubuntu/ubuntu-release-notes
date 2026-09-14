---
tocdepth: 3
---

<!-- SOURCE: https://discourse.ubuntu.com/t/groovy-gorilla-release-notes/15533 -->

(ubuntu-20-10-release-notes)=
# Ubuntu 20.10 release notes

## Introduction

These release notes for **Ubuntu 20.10** (Groovy Gorilla) provide an overview of the release and document the known issues with Ubuntu and its flavours.

## Support lifespan

Ubuntu 20.10 will be supported for 9 months until July 2021. If you need Long Term Support, it is recommended you use [Ubuntu 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes/) instead.

<!--
## Get Ubuntu 20.10

## Download Ubuntu 20.10

Images can be downloaded from a location near you.

You can download ISOs and flashable images from:

  * [Ubuntu Desktop and Server for 64-bit x86 (AMD64) ](http://releases.ubuntu.com/20.10/)
  * [Less Frequently Downloaded Ubuntu Images](http://cdimage.ubuntu.com/ubuntu/releases/20.10/release/)
  * [Ubuntu Cloud Images](http://cloud-images.ubuntu.com/daily/server/groovy/current/)
  * [Ubuntu Netboot](http://cdimage.ubuntu.com/netboot/20.10/)
  * [Lubuntu](http://cdimage.ubuntu.com/lubuntu/releases/20.10/release/)
  * [Kubuntu](http://cdimage.ubuntu.com/kubuntu/releases/20.10/release/)
  * [Ubuntu Budgie](http://cdimage.ubuntu.com/ubuntu-budgie/releases/20.10/release/)
  * [Ubuntu Kylin](http://cdimage.ubuntu.com/ubuntukylin/releases/20.10/release/)
  * [Ubuntu MATE](http://cdimage.ubuntu.com/ubuntu-mate/releases/20.10/release/)
  * [Ubuntu Studio](http://cdimage.ubuntu.com/ubuntustudio/releases/20.10/release/)
  * [Xubuntu](http://cdimage.ubuntu.com/xubuntu/releases/20.10/release/

== Upgrading from Ubuntu 20.04 ==

To upgrade on a desktop system:

  * Open the "Software & Updates" Setting in System Settings.
  * Select the 3rd Tab called "Updates".
  * Set the "Notify me of a new Ubuntu version" dropdown menu to "For any new version".
  * Press <kbd>Alt</kbd>+ <kbd>F2</kbd> and type in `update-manager -c` into the command box.
    * Update Manager should open up and tell you: **"New distribution release '20.10' is available."**
  * If not you can also use `/usr/lib/ubuntu-release-upgrader/check-new-release-gtk`
  * Click Upgrade and follow the on-screen instructions. 

To upgrade on a server system:

  * Install the `update-manager-core package` if it is not already installed.
  * Make sure the Prompt line in `/etc/update-manager/release-upgrades` is set to normal.
  * Launch the upgrade tool with the command `sudo do-release-upgrade`.
  * Follow the on-screen instructions. 

Note that the server upgrade will use GNU screen and automatically re-attach in case of dropped connection problems.

There are no offline upgrade options for Ubuntu Desktop and Ubuntu Server. Please ensure you have network connectivity to one of the official mirrors or to a locally accessible mirror and follow the instructions above.

-->

## New features in 20.10

## Updated Packages

### Linux kernel 🐧

Ubuntu 20.10 includes the __5.8__ Linux kernel. This includes numerous updates and added support since the 5.4 Linux kernel released in Ubuntu 20.04 LTS. Some notable examples include:

* Airtime Queue limits for better WiFi connection quality
* Btrfs RAID1 with 3 and 4 copies and more checksum alternatives
* USB 4 (Thunderbolt 3 protocol) support added
* X86 Enable 5-level paging support by default
* Intel Gen11 (Ice Lake) and Gen12 (Tiger Lake) graphics support
* Initial support for AMD Family 19h (Zen 3)
* Thermal pressure tracking for systems for better task placement wrt CPU core
* XFS online repair
* OverlayFS pairing with VirtIO-FS
* General Notification Queue for key/keyring notification, mount changes, etc.
* Active State Power Management (ASPM) for improved power savings of PCIe-to-PCI devices
* Initial support for POWER10

## Toolchain Upgrades 🛠️

Ubuntu 20.10 comes with refreshed state-of-the-art toolchain including new upstream releases of glibc 2.32, ☕ OpenJDK 11, rustc 1.41, GCC 10, LLVM 11, 🐍 Python 3.8.6, 💎 ruby 2.7.0, php 7.4.9, 🐪 perl 5.30, golang 1.13.

## Security Improvements 🔒

nftables is now the default backend for the firewall.

## Ubuntu Desktop

Ubuntu 20.10 is the first Ubuntu release to feature [desktop images for the Raspberry Pi 4](https://ubuntu.com/raspberry-pi/desktop).

### GNOME 👣

Ubuntu 20.10 includes the latest version of GNOME, version 3.38, with an enhanced Activities Overview, User Experience improvements, better performance, and more.

### Updated Applications
 
 * Firefox 🔥🦊 version 81
 * LibreOffice 📚 version 7.0.2
 * Thunderbird 🌩🐦 version 78.3.2

### Updated Subsystems
 
  * BlueZ 5.55
  * NetworkManager 1.26.2

## Ubuntu Server

### Noteworthy changes
 * squid: the NIS basic authentication helper was removed ([LP: #1895694](https://bugs.launchpad.net/ubuntu/+source/squid/+bug/1895694))
 * adcli and realmd: many upstream fixes were applied to these packages, improving on the compatibility with current Active Directory changes
 * [samba 4.12](https://www.samba.org/samba/history/samba-4.12.0.html) has switched to GnuTLS for most of its cryptographic operations and that has a huge performance improvement in SMB3 encryption
* QEMU was updated to the 5.0 release. See the upstream [changes](https://wiki.qemu.org/ChangeLog/5.0) for an overview of the many improvements.
  * One noteworthy new feature is [virtiofs](https://www.qemu.org/docs/master/interop/virtiofsd.html) which allows better sharing of host file systems to the guest compared to the older [9p fs](https://www.kernel.org/doc/Documentation/filesystems/9p.txt) based approach.
* Libvirt has been updated to version 6.6. See the upstream [Changelogs](https://libvirt.org/news.html) for the many improvements and fixes since version 6.0 that was in [Focal](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes#Ubuntu_Server).
  * Libvirt 6.6 also supports the new [virtiofs](https://libvirt.org/kbase/virtiofs.html) that was mentioned in the QEMU section above.
* Dovecot’s mail-stack-delivery transitional package was deprecated in focal, and dropped entirely in groovy. (LP: #1771524, #1876564)
  * Dovecot itself is updated from focal’s 2.3.7 to 2.3.11.  This adds SSL/STARTTLS support for proxied doveadm connections, IMAP transaction batching, enhanced event reporting, and numerous other fixes.  Postfix socketmap support is dropped.  See https://dovecot.org/doc/NEWS for the full list of changes.
* [liburing](https://github.com/axboe/liburing) support has been added. This is a new mechanism for asynchronous I/O in the linux kernel. For the time being, we have qemu and samba using this support.
  * Samba added uring support in the [4.12.0 release](https://wiki.samba.org/index.php/Samba_4.12_Features_added/changed#.27io_uring.27_vfs_module) in the form of a VFS module. It’s part of the samba-vfs-modules package.
  * Qemu added uring support in the [5.0 release](https://wiki.qemu.org/ChangeLog/5.0#Block_device_backends_and_tools), it can be used with the file-posix driver like aio=io_uring.
* Groovy introduces the [telegraf](https://www.influxdata.com/time-series-platform/telegraf/) [package](https://launchpad.net/ubuntu/groovy/+source/telegraf), part of a well known logging, monitoring, and alerting stack (LMA). Together with [prometheus](https://prometheus.io/), [prometheus alert-manager](https://prometheus.io/docs/alerting/latest/alertmanager/), and [grafana](https://grafana.com/), this trio forms the basis of a strong and reliable monitoring and alerting solution that can be deployed on Ubuntu systems.
  * Grafana: feature rich metrics dashboard and graph editor, available as a snap at https://snapcraft.io/grafana
  * Prometheus and alert manager: monitoring system and time series database, available as both a snap at https://snapcraft.io/prometheus and as a deb package in Groovy
  * Telegraf: agent for collecting and sending metrics and events from databases, systems, and IoT sensors. Available as a deb package in Groovy. 

### OpenStack

Ubuntu 20.10 includes the latest OpenStack release, Victoria, including the                                                                  
following components:                                                                                                                        
                                                                                                                                             
  • OpenStack Identity - Keystone                                                                                                            
                                                                                                                                             
  • OpenStack Imaging - Glance                                                                                                               
                                                                                                                                             
  • OpenStack Block Storage - Cinder                                                                                                         
                                                                                                                                             
  • OpenStack Compute - Nova                                                                                                                 
                                                                                                                                             
  • OpenStack Networking - Neutron                                                                                                           
                                                                                                                                             
  • OpenStack Telemetry - Ceilometer, Aodh, Gnocchi, and Panko                                                                               
                                                                                                                                             
  • OpenStack Orchestration - Heat                                                                                                           
                                                                                                                                             
  • OpenStack Dashboard - Horizon                                                                                                            
                                                                                                                                             
  • OpenStack Object Storage - Swift                                                                                                         
                                                                                                                                             
  • OpenStack DNS - Designate                                                                                                                
                                                                                                                                             
  • OpenStack Bare-metal - Ironic                                                                                                            
                                                                                                                                             
  • OpenStack Filesystem - Manila                                                                                                            
                                                                                                                                             
  • OpenStack Key Manager - Barbican                                                                                                         
                                                                                                                                             
  • OpenStack Load Balancer - Octavia                                                                                                        
                                                                                                                                             
  • OpenStack Instance HA - Masakari                                                                                                         
                                                                                                                                             
Please refer to the [OpenStack Victoria release notes](https://releases.openstack.org/victoria/) for full details of this                                                                
release of OpenStack.                                                                                                                        
                                                                                                                                             
OpenStack Victoria is also provided via the [Ubuntu Cloud Archive](https://wiki.ubuntu.com/OpenStack/CloudArchive) for OpenStack                                                               
Victoria for Ubuntu 20.04 LTS users.                                                                                                         
                                                                                                                                             
WARNING: Upgrading an OpenStack deployment is a non-trivial process and care                                                                 
should be taken to plan and test upgrade procedures which will be specific to                                                                
each OpenStack deployment.                                                                                                                   
                                                                                                                                             
Make sure you read the [OpenStack Charm Release Notes](https://docs.openstack.org/charm-guide/latest) for more information about                                                              
how to deploy Ubuntu OpenStack using Juju.     

## Platforms

### Cloud Images ☁

* To improve boot time, images with cloud-specific and KVM kernels boot without an initramfs by default. Cloud images with the generic kernel will continue to boot with an initramfs by default.
* An additional boot time improvement comes with snap pre-seeding optimizations. These changes will greatly improve first-boot speeds in the clouds. Users can find additional timing information from the `snap debug seeding` and checking the `seed-completion` commands to see how long snap seeding took on the first boot. Feedback from users would be appreciated.

### Raspberry Pi 🍓

* **New Desktop Image!** Please note this is only built for the arm64 architecture, and only supported for Pi4 models with at least 4Gb of RAM. The image may still boot on smaller, or earlier models but these are not supported platforms.
* **Compute Module 4 support.** Both Server and Desktop images are fully supported on the new CM4 platform. However, for the Desktop image please note that only models with 4Gb of RAM or greater are supported, and further that the size of the image exceeds 8Gb and thus 16Gb eMMC is the smallest supported model (or Lite models with equivalent SD card storage).
* With the removal of U-Boot from the default boot process, USB and network boot is now enabled on all Pi models via [the same procedure as Raspbian](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bootmodes/README.md). U-Boot will remain as an *option* this cycle (it is still installed on the boot partition and can still be selected with `config.txt` options) but is considered deprecated.
* Upgraders from Ubuntu 20.04 LTS will not be implicitly switched away from U-Boot. However, you can switch to a U-Boot-less sequence quite simply. The [Groovy Boot Modes](https://waldorf.waveform.org.uk/2020/groovy-boot-modes.html) post has details on moving between the two options.

### s390x

IBM Z and LinuxONE / s390x-specific enhancements since 20.04 (partially not limited to s390x):

 * Log FCP link EDIF capability introduced ([LP: #1830732](https://bugs.launchpad.net/bugs/1830732) and [LP: #1884773](https://bugs.launchpad.net/bugs/1884773)) and EDIF related FCP errors (FSF_SECURITY_ERRORS) added ([LP: #1830733](https://bugs.launchpad.net/bugs/1830733)).

 * SCSI IPL normal ([LP: #1884737](https://bugs.launchpad.net/bugs/1884737)) and IPL for NVMe device support added ([LP: #1886792](https://bugs.launchpad.net/bugs/1886792)), incl. installer support ([LP: #1884769](https://bugs.launchpad.net/bugs/1884769)).

 * Updated cryptography stack: libica 3.7.0 ([LP: #1878650](https://bugs.launchpad.net/bugs/1878650)), openssl RNG support ([LP: #1799928](https://bugs.launchpad.net/bugs/1799928)), openssl-ibmca 2.1.1 ([LP: #1884763](https://bugs.launchpad.net/bugs/1884763)) openCryptoki 3.14 incl. Dilithium signing in openCryptoki EP11 tokens ([LP: #1886777](https://bugs.launchpad.net/bugs/1886777)), key management tool improvements ([LP: #1884751](https://bugs.launchpad.net/bugs/1884751) and [LP: #1884755](https://bugs.launchpad.net/bugs/1884755)) as well as PIN conversion tool improvements ([LP: #1854944](https://bugs.launchpad.net/bugs/1854944) and [LP: #1893216](https://bugs.launchpad.net/bugs/1893216)).

 * Enhancements of the hardware assisted compression support, especially DEFLATE ([LP: #1884514](https://bugs.launchpad.net/bugs/1884514)) and NXU exploitation.

 * Further s390x-related packages updates: s390-tools 2.14 ([LP: #1884721](https://bugs.launchpad.net/bugs/1884721)), smc-tools 1.3.0 ([LP: #1884508](https://bugs.launchpad.net/bugs/1884508)), libdfp 1.0.15 ([LP: #1887900](https://bugs.launchpad.net/bugs/1887900)), perftest 4.0-29 ([LP: #1888377](https://bugs.launchpad.net/bugs/1888377)), pacemaker fence agent for LPARs ([LP: #1889070](https://bugs.launchpad.net/bugs/1889070)) and OpenBlas 0.3.10 with optimizations ([LP: #1884519](https://bugs.launchpad.net/bugs/1884519) and [LP: #1893653](https://bugs.launchpad.net/bugs/1893653)).

 * KVM virtualization stack updates and s390x specific modifications: kvm_stat sampling and logging ([LP: #1884784](https://bugs.launchpad.net/bugs/1884784)), transparent CCW IPL from DASD ([LP: #1887935](https://bugs.launchpad.net/bugs/1887935) and [LP: #1887936](https://bugs.launchpad.net/bugs/1887936)), transparent channel path handling for vfio-ccw ([LP: #1887930](https://bugs.launchpad.net/bugs/1887930) and [LP: #1887931](https://bugs.launchpad.net/bugs/1887931)).

 * Further s390x specific enhancements: vector enhancements in gcc ([LP: #1888653](https://bugs.launchpad.net/bugs/1888653)) and in binutils ([LP: #1889742](https://bugs.launchpad.net/bugs/1889742) and [LP: #1888654](https://bugs.launchpad.net/bugs/1888654)), CPU topology alignment ([LP: #1884782](https://bugs.launchpad.net/bugs/1884782)), OSA Express performance enhancements in qeth driver ([LP: #1853294](https://bugs.launchpad.net/bugs/1853294)) and SMC-R failover ([LP: #1853151](https://bugs.launchpad.net/bugs/1853151)) as well as SMC-D v2 toleration support ([LP: #1887942](https://bugs.launchpad.net/bugs/1887942)).


## Known Issues

As is to be expected, with any release, there are some significant known bugs that users may run into with this release of Ubuntu. The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:

### General

* [LP: #1899632](https://bugs.launchpad.net/ubuntu-cdimage/+bug/1899632) - It is no longer possible to use "Easy Install" with VMWare Player.

### Linux kernel

 * The latest NVIDIA 455 graphics drivers were not included on the initial release of groovy. These will be available as a stable release update (SRU) shortly after release. The NVIDIA 455 drivers are necessary for support of the GeForce RTX 3080, RTX 3090 and MX450.

### Ubuntu Desktop

 * [LP :#1900722](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1900722) - Reinstall Ubuntu fails.
 * [LP: #1897224](https://bugs.launchpad.net/ubuntu/+source/snapd/+bug/1897224) - Graphical snaps broken on GNOME Wayland sessions
* [LP: #1901043](https://bugs.launchpad.net/ubuntu-release-notes/+bug/1901043) - No sound in Try/Install Ubuntu (ubiquity-dm) when "Safe graphics mode" is selected (nomodeset)

### Ubuntu Server

Nothing yet.

## Platforms

### Cloud Images ⛈️

* On Google Compute Engine (GCE), the google-guest-agent package has introduced a [regression (LP: #1901033)](https://bugs.launchpad.net/google-guest-agent/+bug/1901033) for the google-startup-script service. Users making use of [startup scripts](https://cloud.google.com/compute/docs/startupscript) on GCE can see scripts run before cloud-init and snapd seeding have completed until the regression is addressed. Without waiting for cloud-final and snapd.seeded, startup scripts may not be presented with a consistent system that have archive mirrors set up, GCE's google-cloud-sdk snap installed, users in the proper groups, or other customizations owned by those services. As a work-around users can add `cloud-init status --wait` to the beginning of their startup script (as cloud-init does wait for snap seeding to complete).

### Raspberry Pi

* [LP: #1899962] - On the desktop image, the wrong audio output device is selected on each boot. A workaround is available in the bug report.
* [LP: #1899953] - Audio output is "crackly". A workaround (tsched=0) is detailed in the bug report.
* [LP: #1900904] - Auxilliary (e.g. USB attached) ethernet ports will not be automatically configured. A workaround is present in the bug report.
* On the Pi4, we recommend you install the [rpi-eeprom] package with `sudo apt install rpi-eeprom` to keep your boot EEPROM up to date. This is also required if you wish to experiment USB or netboot on this platform. This should be included in the image in future releases.
* On the Pi Foundation's IO Board for the Compute Module 4, the USB ports are routed to the DWC2 USB2 controller (which is attached to the USB-C port on the Pi 4). This is not in host-mode by default meaning that keyboards (and other devices) will not work. Add the following line to the `config.txt` in order to enable the USB ports on the IO board:

      dtoverlay=dwc2,dr_mode=host

  A commented out instance of this line can be found in `config.txt` by default.

[LP: #1899962]: https://bugs.launchpad.net/ubuntu/+source/pulseaudio/+bug/1899962
[LP: #1899953]: https://bugs.launchpad.net/ubuntu/+source/pulseaudio/+bug/1899953
[LP: #1900904]: https://bugs.launchpad.net/ubuntu/+source/cloud-init/+bug/1900904
[rpi-eeprom]: https://launchpad.net/ubuntu/+source/rpi-eeprom

### ppc64el

 * [LP: #1878041](https://bugs.launchpad.net/bugs/1878041) - In case of multipath systems with huge amounts of paths, the installer may hit a timeout.

### s390X

 * [LP: #1900900](https://bugs.launchpad.net/bugs/1900900) - If doing an installation on previously used zFCP/SCSI multipath disk storage, the installer might fail removing a previous configuration. Workaround is to wipe the config manually in an installer shell. Fix will be included in future installer updates.

## Official flavours

The release notes for the official flavours can be found at the following links:

  * [Kubuntu Release Notes](https://kubuntu.org/)
  * [Lubuntu Release Notes](https://lubuntu.me)
  * [Ubuntu Budgie Release Notes](https://ubuntubudgie.org/2020/09/ubuntu-budgie-20-10-release-notes/)
  * [Ubuntu Kylin Release Notes](https://www.ubuntukylin.com/news/2010ReleaseNotes-en.html)
  * [Ubuntu MATE Release Notes](https://ubuntu-mate.org/blog/ubuntu-mate-groovy-gorilla-release-notes/)
  * [Ubuntu Studio Release Notes](https://wiki.ubuntu.com/GroovyGorilla/ReleaseNotes/UbuntuStudio)
  * [Xubuntu Release Notes](https://wiki.xubuntu.org/releases/20.10/release-notes)
