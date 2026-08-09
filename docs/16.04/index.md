---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/XenialXerus/ReleaseNotes -->

(ubuntu-16-04-lts-release-notes)=
# Ubuntu 16.04 LTS release notes

(16-04-lts-introduction)=
## Introduction

These release notes for **Ubuntu 16.04.7 LTS** (Xenial Xerus) provide an overview of the release and document the known issues with Ubuntu 16.04 LTS and its flavours.  For details of the changes applied since 16.04, please see the [16.04.7 change summary](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/ChangeSummary/16.04.7).  The release notes for [16.04](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/16.04), [16.04.1](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/16.04.1), [16.04.2](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/16.04.2), [16.04.3](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/16.04.3), [16.04.4](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/16.04.4), [16.04.5](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/16.04.5) and [16.04.6](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/16.04.6) are available as well.

Please refer to Change Summary notes for [16.04.7](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/ChangeSummary/16.04.7) if interested in the latest 16.04.7 release.


(16-04-lts-support-lifespan)=
### Support lifespan

Ubuntu 16.04 LTS will be supported for 5 years for Ubuntu Desktop, Ubuntu Server, Ubuntu Core, and Ubuntu Kylin. All other flavours will be supported for 3 years.


(16-04-lts-official-flavour-release-notes)=
### Official flavour release notes

Find the links to release notes for official flavours [here](https://wiki.ubuntu.com/Official_flavours).


(get-ubuntu-16-04-7-lts)=
## Get Ubuntu 16.04.7 LTS


(download-ubuntu-16-04-7-lts)=
### Download Ubuntu 16.04.7 LTS

Images can be downloaded from a location near you.
##
**Note:** The Ubuntu Desktop images are now bigger than a standard CD, and you should use a USB or DVD for installation.

You can download images from:  [releases.ubuntu.com/xenial/](http://releases.ubuntu.com/xenial/)


##[releases.ubuntu.com/16.04.4/](http://releases.ubuntu.com/16.04.4/) (Ubuntu Desktop and Server)

##[cdimage.ubuntu.com/ubuntu/releases/16.04.4/release/](http://cdimage.ubuntu.com/ubuntu/releases/16.04.4/release/) (Less Popular Ubuntu Images)

##[cdimage.ubuntu.com/netboot/16.04.4/](http://cdimage.ubuntu.com/netboot/16.04.4/) (Ubuntu Netboot)

##[cdimage.ubuntu.com/ubuntu-base/releases/16.04.4/release/](http://cdimage.ubuntu.com/ubuntu-base/releases/16.04.4/release/) (Ubuntu Base)

##[cdimage.ubuntu.com/kubuntu/releases/16.04.4/release/](http://cdimage.ubuntu.com/kubuntu/releases/16.04.4/release/) (Kubuntu)

##[cdimage.ubuntu.com/lubuntu/releases/16.04.4/release/](http://cdimage.ubuntu.com/lubuntu/releases/16.04.4/release/) (Lubuntu)

##[cdimage.ubuntu.com/ubuntustudio/releases/16.04.4/release/](http://cdimage.ubuntu.com/ubuntustudio/releases/16.04.4/release/) (Ubuntu Studio)

##[cdimage.ubuntu.com/ubuntu-gnome/releases/16.04.4/release/](http://cdimage.ubuntu.com/ubuntu-gnome/releases/16.04.4/release/) (Ubuntu GNOME)

##[cdimage.ubuntu.com/ubuntukylin/releases/16.04.4/release/](http://cdimage.ubuntu.com/ubuntukylin/releases/16.04.4/release/) (Ubuntu Kylin)

##[cdimage.ubuntu.com/ubuntu-mate/releases/16.04.4/release/](http://cdimage.ubuntu.com/ubuntu-mate/releases/16.04.4/release/) (Ubuntu MATE)

##[cdimage.ubuntu.com/xubuntu/releases/16.04.4/release/](http://cdimage.ubuntu.com/xubuntu/releases/16.04.4/release/) (Xubuntu)

##[cdimage.ubuntu.com/mythbuntu/releases/16.04.4/release/](http://cdimage.ubuntu.com/mythbuntu/releases/16.04.4/release/) (Mythbuntu)



(16-04-lts-upgrading-from-ubuntu-14-04-lts-or-15-10)=
### Upgrading from Ubuntu 14.04 LTS or 15.10

To upgrade on a desktop system:

* Open the "Software & Updates" Setting in System Settings.

* Select the 3rd Tab called "Updates".

* Set the "Notify me of a new Ubuntu version" dropdown menu to "For any new version" if you are using 15.10, set it to "long-term support versions" if you are using 14.04 LTS.

* Press Alt+F2 and type in "update-manager" (without the quotes) into the command box.

* Software Updater should open up and tell you: New distribution release '16.04 LTS' is available.

* Click Upgrade and follow the on-screen instructions.

To upgrade on a server system:

* Install the `update-manager-core` package if it is not already installed.

* Make sure the /etc/update-manager/release-upgrades is set to normal if you are using 15.10, lts if you are using 14.04 LTS.

* Launch the upgrade tool with the command `sudo do-release-upgrade`.

* Follow the on-screen instructions.
Note that the server upgrade will use GNU screen and automatically re-attach in case of dropped connection problems.

There are no offline upgrade options for Ubuntu Desktop and Ubuntu Server. Please ensure you have network connectivity to one of the official mirrors or to a locally accessible mirror and follow the instructions above.


(new-features-in-16-04-lts)=
## New features in 16.04 LTS



(16-04-lts-snap-application-format)=
### Snap application format

Ubuntu 16.04 LTS introduces a new application format, the ‘snap’, which can be installed alongside traditional deb packages. These two packaging formats live quite comfortably next to one another and enable Ubuntu to maintain its existing processes for development and updates.
More information is available [here](https://insights.ubuntu.com/2016/04/20/canonical-unveils-6th-lts-release-of-ubuntu-with-16-04/).


(16-04-lts-updated-packages)=
### Updated Packages

As with every new release, packages--applications and software of all kinds--are being updated at a rapid pace. Many of these packages came from an automatic sync from [Debian](http://www.debian.org)'s unstable branch; others have been explicitly pulled in for Ubuntu 16.04.

For a list of all packages being accepted for Ubuntu 16.04, please subscribe to [xenial-changes](https://lists.ubuntu.com/mailman/listinfo/xenial-changes).


(16-04-lts-linux-kernel-4-4)=
#### Linux kernel 4.4

Ubuntu 16.04 LTS is based on the long-term supported Linux release series 4.4.


(16-04-lts-python-3)=
#### Python 3

Python2 is not installed anymore by default on the server, cloud and the touch images, long live Python3!
Python3 itself has been upgraded to the 3.5 series.

If you have your own programs based on Python 2, fear not! Python 2 will continue to be available (as the python package) for the foreseeable future. However, to best support future versions of Ubuntu you should consider porting your code to Python 3. [Python/3](https://help.ubuntu.com/community/Python/3) has some advice and resources on this.


(16-04-lts-vim-defaults-to-python3)=
#### VIM defaults to python3

The default VIM package has been built against python3 instead of python2. This means plugins that require a python2 interpreter support from VIM will not work anymore.
For this case alternative VIM packages are available that still use python2, for example vim-gnome-py2.
They can be made the default via the alternatives mechanism:

* `sudo update-alternatives --set vim /usr/bin/vim.gnome-py2`


(16-04-lts-golang-1-6)=
#### Golang 1.6

The golang toolchain was upgraded to the 1.6 series, and gccgo was upgraded to the GCC 6.1 release candidate 1. Thus the same level of standard library and compiler features are provided by both compilers on all fully supported architectures.


(16-04-lts-openssh-7-2p2)=
#### OpenSSH 7.2p2

Recent OpenSSH releases disable several pieces of weak, legacy, and/or unsafe cryptography.  If you are upgrading a system remotely over SSH, you should check that you are not relying on these to ensure that you will retain access after the upgrade.

* Support for the legacy SSH version 1 protocol is disabled by default at compile time.  Note that this also means that the `Cipher` keyword in [ssh_config(5)](http://manpages.ubuntu.com/manpages/xenial/en/man5/ssh_config.5.html) is effectively no longer usable; use `Ciphers` instead for protocol 2.  The [openssh-client-ssh1](https://packages.ubuntu.com/search?keywords=openssh-client-ssh1) package includes "ssh1", "scp1", and "ssh-keygen1" binaries which you can use if you have no alternative way to connect to an outdated SSH1-only server; please contact the server administrator or system vendor in such cases and ask them to upgrade.

* Support for the 1024-bit `diffie-hellman-group1-sha1` key exchange is disabled by default at run-time.  It may be re-enabled using the [upstream instructions](http://www.openssh.com/legacy.html).

_ Support for `ssh-dss`, `ssh-dss-cert-_` host and user keys is disabled by default at run-time.  These may be re-enabled using the [upstream instructions](http://www.openssh.com/legacy.html).

* Support for the legacy `v00` cert format has been removed.

* Several ciphers are disabled by default in `ssh`: `blowfish-cbc`, `cast128-cbc`, all `arcfour` variants and the `rijndael-cbc` aliases for AES.

* MD5-based and truncated HMAC algorithms are disabled by default in `ssh`.


(16-04-lts-gnu-toolchain)=
#### GNU toolchain

glibc was updated to the 2.23 release, binutils to the 2.26 release, and GCC to a recent snapshot from the GCC 5 branch (post GCC 5.3.0).


(16-04-lts-apt-1-2)=
#### Apt 1.2

Apt 1.2 includes the new privilege separation features introduced in Apt 1.1. Importantly, the unprivileged "_apt" user is now used when making outgoing network connections and parsing the results for the various apt transport methods (HTTP, HTTPS, FTP).


(16-04-lts-ubuntu-for-ibm-linuxone-and-z-systems)=
### Ubuntu for IBM LinuxONE and z Systems

Ubuntu 16.04 LTS includes a new port to 64-bit z/Architecture for IBM mainframe computers. This is a practically complete port of Ubuntu Server and Cloud with around 95% binary package availability. We are excited to enable OpenStack software, Juju, MAAS, LXD, and much more on this platform.

For more information about this port see [S390X](https://help.ubuntu.com/community/S390X) page.


(16-04-lts-ubuntu-desktop)=
### Ubuntu Desktop

The general theme for 16.04 on the desktop is one of bug fixes and incremental quality improvements.


(16-04-lts-general)=
#### General

* GNOME is mostly upgraded to 3.18.  GLib upgraded to to 2.48 (corresponding to GNOME 3.20)

* GNOME Software replaces Ubuntu Software Center.  This brings a faster store experience and moves our archive metadata in line with Debian.  It has been renamed "Ubuntu Software" to improve recognition for Ubuntu Software Center users.

* All default applications and libraries ported to use WebKit 2

* GNOME Calendar is now included by default

* Empathy and Brasero are removed from the default installation

* Chromium upgraded to version 48

* Firefox upgraded to version 45

* Online searches in the dash are now disabled by default

* Improved HiDPI support in the greeter

* Added more supported languages by default [More info](https://lists.ubuntu.com/archives/ubuntu-devel/2015-December/039028.html)

* Multiple bug fixes


(16-04-lts-unity-compiz)=
#### Unity & Compiz

* Improved launcher integration with file manager and devices
* Support for formatting removable devices from quicklist
* Improved support for gtk applications using headerbars
* Improvements to the switcher and spread backends
* Activate app spread by Super+Ctrl+W
* Unity control center option to always show menus
* Improvements to GNOME key grabbing
* New dash overlay scrollbars
* Better Dash theming support
* Support for scaling cursors in HiDPI environments
* Show icons launching state in launcher when apps launched elsewhere
* Launcher can be moved to the bottom


(16-04-lts-libreoffice)=
#### LibreOffice

LibreOffice 5.1 brings a lot of improvements to the entire package.  For more information on these improvements please see the LibreOffice release notes [available here](https://wiki.documentfoundation.org/ReleaseNotes/5.1).  You can see a video highlighting some of the new features [here](https://www.youtube.com/watch?v=LrWPfWSuLSA&list=PL0pdzjvYW9RHSwdRnZfaxAWICrkBrQl7k).


(16-04-lts-general-2)=
##### General

* LibreOffice defaults to the Breeze theme in Ubuntu

* Improvements in the Python scripting and language bindings [conference.libreoffice.org/assets/Conference/Aarhus/Slides/MatthewFrancisPyUNO.pdf](http://conference.libreoffice.org/assets/Conference/Aarhus/Slides/MatthewFrancisPyUNO.pdf)

* Support for WebDAV via HTTPS


(16-04-lts-writer-word-processor)=
##### Writer word processor

* Added support for whitespace hiding. A long standing feature request.

* Mailmerge in Writer can use spreadsheets as a data source [vmiklos.hu/blog/mail-merge-embedding.html](http://vmiklos.hu/blog/mail-merge-embedding.html)

* Spell check dialogue no longer auto closes


(16-04-lts-calc-spreadsheets)=
##### Calc spreadsheets

* Exponential and power trend lines handle negative Y values
* Performance improvements leveraging SSE3 for SUM functions
* Added support for PNG export
* Search for numbers as formatted/displayed


(16-04-lts-impress-presentations)=
##### Impress presentations

* Slide transitions use OpenGL 2.1+ and new transitions added
* Keyboard shortcuts for navigation and sorting
* Screensaver inhibiting for KDE, XFCE, Mate


(16-04-lts-ubuntu-server)=
### Ubuntu Server


(16-04-lts-general-3)=
#### General

New in 16.04, the kernel crash dump mechanism now supports remote kernel crash dumps. It is now possible to send kernel crash dumps to a remote server using the SSH or NFS protocols. Details of the new functionality are available in the [Ubuntu Server Guide](https://help.ubuntu.com/16.04/serverguide/kernel-crash-dump.html).

Since the release of 16.04.2, the server ISOs are now larger than a standard 700MB CD. The increase in size is due to the ability to run the installer with the use of the [Hardware Enablement (HWE) kernel](https://wiki.ubuntu.com/Kernel/RollingLTSEnablementStack). The HWE kernels enables newer platforms and components, which require functionality delivered in newer kernels, while allowing the continued use of an LTS release.


(16-04-lts-openstack-mitaka)=
#### OpenStack Mitaka

Ubuntu 16.04 includes  the latest OpenStack release, Mitaka, including the following components:

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

Please refer to the [OpenStack Mitaka release notes](http://releases.openstack.org/mitaka/) for full details of this release of OpenStack.

OpenStack Mitaka is also provided via the [Ubuntu Cloud Archive](https://wiki.ubuntu.com/ServerTeam/CloudArchive) for OpenStack Mitaka for Ubuntu 14.04 LTS users.

Ubuntu 16.04 also includes the first GA release of of the Nova driver for LXD ('nova-lxd').

**WARNING**: Upgrading an OpenStack deployment is a non-trivial process and care should be taken to plan and test upgrade procedures which will be specific to each OpenStack deployment.

Make sure you read the [OpenStack Charm Release Notes](https://wiki.ubuntu.com/OpenStack/OpenStackCharms/ReleaseNotes1604) for more information about how to deploy Ubuntu OpenStack using Juju.


(16-04-lts-libvirt-1-3-1)=
#### libvirt 1.3.1

Libvirt has been updated to the 1.3.1 release.


(16-04-lts-qemu-2-5)=
#### qemu 2.5

Qemu has been updated to the 2.5 release.

See [wiki.qemu.org/ChangeLog/2.5](http://wiki.qemu.org/ChangeLog/2.5) for details.


(16-04-lts-open-vswitch-2-5-0)=
#### Open vSwitch 2.5.0

Ubuntu 16.04 includes the latest release of Open vSwitch, 2.5.0.  This is also an LTS release of Open vSwitch.

Ubuntu 16.04 also includes support for Open vSwitch integrated with DPDK (Data Plane Development Kit) enabling fast packet processing through userspace usage of compatible networking cards - see the openvswitch-switch-dpdk package for more details.


(16-04-lts-ceph-jewel)=
#### Ceph Jewel

Ubuntu 16.04 includes the latest release candidate (10.1.2) of the Ceph Jewel stable release; An update to the final release version will be delivered as an SRU to Ubuntu 16.04.

For full details on the Ceph Jewel release, please refer to the [upstream release notes](http://ceph.com/docs/master/release-notes/).


(16-04-lts-nginx)=
#### Nginx

Ubuntu 16.04 includes version 1.9.15 of the Nginx web server, with an expectation to provide the next stable release of Nginx, 1.10.0, as an SRU after release (which will be virtually identical to 1.9.15). This version of Nginx also includes HTTP/2 support, which supersedes SPDY support previously provided in the Nginx packages.


(16-04-lts-lxd-2-0)=
#### LXD 2.0

Ubuntu 16.04 LTS includes LXD, a new, lightweight, network-aware, container manager offering a VM-like experience built on top of Linux containers.

LXD comes pre-installed with all Ubuntu 16.04 server installations, including cloud images and can easily be installed on the Desktop version too. It can be used standalone through its simple command line client, through Juju to deploy your charms inside containers or with OpenStack for large scale deployments.

All the LXC components - LXC, LXCFS and LXD - are at version 2.0 in Ubuntu 16.04 LTS.

Learn more about LXD here: [www.ubuntu.com/cloud/lxd/](http://www.ubuntu.com/cloud/lxd/)

And discover all the LXD 2.0 features with: [www.stgraber.org/2016/03/11/lxd-2-0-blog-post-series-012/](https://www.stgraber.org/2016/03/11/lxd-2-0-blog-post-series-012/)


(16-04-lts-docker-1-10)=
#### docker 1.10

docker was upgraded to version 1.10. Note that this requires migration of existing images to a new format which will be performed on the first start of the service. This migration can take a long time and put a high load on the system; see [docs.docker.com/engine/migration/](https://docs.docker.com/engine/migration/) for more information.


(16-04-lts-php-7-0)=
#### PHP 7.0

PHP was upgraded to 7.0. Note that this will require modifications to custom PHP extensions (https://wiki.php.net/phpng-upgrading) and may require modifications to PHP source code (http://php.net/manual/en/migration70.php).

* NGINX and PHP 7.0
  Upgrading from a prior version of Ubuntu with PHP5 FPM configurations and NGINX will require a manual configuration change (details at: [dark-net.net/nginx-http2-php7.0](http://dark-net.net/nginx-http2-php7.0)).

Most PHP-dependent packages were either rebuilt or upgraded for PHP7.0 support. Where that was not possible, packages may have been removed from the archive. There was one exception, Drupal7.

* Drupal7 did not pass upstream testing with PHP7.0 as of the 16.04 release (https://www.drupal.org/node/2656548) and therefore the Ubuntu package was uninstallable. Before Ubuntu 16.04.2, Drupal7 was updated and is now installable (LP:1582340).


(16-04-lts-mysql-5-7)=
#### MySQL 5.7

MySQL has been updated to 5.7. Some configuration directives have been changed or deprecated, so if you are upgrading from a previously customized configuration then you will need to update your customization appropriately. See [bug 1571865](https://bugs.launchpad.net/ubuntu/+source/mysql-5.7/+bug/1571865) for details.

Password behavior when the MySQL root password is empty has changed. Packaging now enables socket authentication when the MySQL root password is empty. This means that a non-root user can't log in as the MySQL root user with an empty password. For details, see the [NEWS](https://salsa.debian.org/mariadb-team/mysql/blob/1025a9fa9c6c112913c59138db49dbc94891d20f/debian/NEWS) file.


(16-04-lts-juju-2-0)=
#### Juju 2.0

Juju and Juju UI have been updated to 2.0beta4. The final Juju 2.0 release will come via an update post-release.  The package name is `juju-2.0`. Juju 1.25.5 is available in the `juju` package for existing production environments. Please read the [upgrade documentation](https://jujucharms.com/docs/devel/juju-upgrade) before moving to 2.0.

Juju now supports modeling workloads on AWS, Microsoft Azure, Google Cloud Engine, Rackspace, Joyent, LXD, MAAS, and manual deployments.

* The [Juju Charm Store](https://jujucharms.com/store) now has over 300 charms ready to deploy. Most of these workloads will deploy Trusty instances, but we expect 16.04 charms to start landing and being announced independent of Juju's release.

* [Juju Core Release Notes](https://jujucharms.com/docs/devel/temp-release-notes)

* [Juju GUI Release Notes](https://blog.jujugui.org/2016/04/15/juju-2-0-beta-4-now-with-embedded-gui/)


(16-04-lts-known-issues)=
## Known issues

As is to be expected, with any release, there are some significant known bugs that users may run into with this release of Ubuntu 16.04.  The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:



(16-04-lts-boot-installation-and-post-install)=
### Boot, installation and post-install


(16-04-lts-installing-xen-host-in-uefi-mode)=
#### Installing Xen host in UEFI mode

It is currently impossible to boot a Xen hypervisor from grub in UEFI mode. However the package does not detect this and will set the default boot to Xen mode. So for any machine in UEFI mode, **do not** install the Xen hypervisor (or enable legacy mode first). Please see this [bug report](https://bugs.launchpad.net/bugs/1520979) for more information.


(16-04-lts-upgrade)=
### Upgrade


(16-04-lts-kubuntu)=
#### Kubuntu

**WARNING**: LTS to LTS upgrade to Xerus is currently problematic and should not be attempted. Please install a fresh copy of 16.04 instead. To prevent messages about upgrading, change Prompt=lts to Prompt=normal or Prompt=never in the /etc/update-manager/release-upgrades file.


(16-04-lts-openssh)=
#### OpenSSH

The default of the "UseDNS" configuration option has changed from yes to no. This may cause users who use the "from=" functionality in authorized_keys to limit ssh access by host to be locked out, which is especially troublesome if upgrading remotely. See [bug 1588457](https://bugs.launchpad.net/bugs/1588457).


(16-04-lts-mysql)=
#### MySQL

Users with customised MySQL server configurations may hit a maintainer script error on upgrade due to changed configuration directives in MySQL 5.7. This will need to be fixed up manually. See the [general MySQL update notes](https://wiki.ubuntu.com/MySQL_5.7) for details and instructions on fixing one common case of this.


(16-04-lts-ibm-linuxone-and-z-systems-specific-known-issues)=
### IBM LinuxONE and z Systems specific known issues


(16-04-lts-fully-automated-preseed-install)=
#### Fully automated preseed install

Fully automated preseed installation is currently not possible with only DASD drives at the moment. For zfcp installation s390-zfcp/zfcp preseed key can be used. For more information please see [bug](https://bugs.launchpad.net/bugs/1572941) and [bug](https://bugs.launchpad.net/bugs/1564788).


(16-04-lts-zfcpdump-not-available-yet)=
#### zfcpdump not available yet

zfcpdump kernel is not available yet, and will be made available as an SRU at a later date. Please see this [bug](https://bugs.launchpad.net/bugs/1565841) for more information.


(16-04-lts-install-time-parameters-are-not-propagated-to-the-installed-system)=
#### Install-time parameters are not propagated to the installed system

If installation is performed with special kernel parameters, e.g. cio_ignore, these are not propagated to the installed system. Please edit `/etc/zipl.conf` to apply these and re-run `sudo zipl` to update the IPL. Please see this [bug](https://bugs.launchpad.net/bugs/1571561) for more information.


(16-04-lts-ipv6-with-pci-roce)=
#### IPv6 with PCI/RoCE

The Linux kernel has an issue in its IPv6 stack with PCI/RoCE cards. IPv4 with PCI/RoCE cards is fully supported. The Linux kernel needs an upgrade to the first SRU kernel post-release for complete IPv6 PCI/RoCE support. Please see this [bug](https://bugs.launchpad.net/bugs/1572291) for more information.


(16-04-lts-scsi-lun-detection-issues)=
#### SCSI LUN detection issues

Usage of SCSI LUNs on a DS8870 Storage server with μCode Bundles 87.51.xx.0 (LMC 7.7.51.xx) via NPIV enabled zfcp adaptors causes detection issues. Please see this [bug](https://bugs.launchpad.net/bugs/1567602) for more information.


(16-04-lts-z-edc-compression-cards)=
#### z/EDC compression cards

There is a known issue with z/EDC compression cards. Please see this [bug](https://bugs.launchpad.net/bugs/1559194) for more information.


(16-04-lts-ibm-power)=
### IBM POWER


(16-04-lts-pci-pass-through-with-qemu-kvm)=
#### PCI pass-through with QEMU-KVM

Running PCI pass-through with Ubuntu 16.04 kernel 4.4 and stock QEMU packages will lead to DI issues as soon as I/O starts on the pass-through adapter [bug](https://bugs.launchpad.net/ubuntu/+source/qemu/+bug/1801674). In such a case an update to a QEMU packages with DDW support is required.
Such packages are available via the following PPA:
[launchpad.net/~ibmpackages/+archive/ubuntu/ddw](https://launchpad.net/~ibmpackages/+archive/ubuntu/ddw)


(16-04-lts-cpu-hotplug-with-qemu-kvm)=
#### CPU Hotplug with QEMU-KVM

CPU hotplug on ppc64el was not yet supported with the QEMU and Libvirt versions available in Ubuntu 16.04. If required please consider upgrading to [18.04 (Bionic)](https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes).



(16-04-lts-desktop)=
### Desktop


(16-04-lts-unity-7)=
#### Unity 7

* Sometimes Gtk application menus go missing [bugs.launchpad.net/ubuntu/+source/unity/+bug/1532226](https://bugs.launchpad.net/ubuntu/+source/unity/+bug/1532226). You can workaround this by launching this from a terminal or `Alt+F2` dash view:

* `restart unity-panel-service`


(16-04-lts-ubuntu-software)=
#### Ubuntu Software

* Sometimes doesn't update apps to "Installed" after installation via search [bugs.launchpad.net/ubuntu/+source/gnome-software/+bug/1551599](https://bugs.launchpad.net/ubuntu/+source/gnome-software/+bug/1551599)

* Does some time-consuming operations without any indicator [bugs.launchpad.net/ubuntu/+source/gnome-software/+bug/1572606](https://bugs.launchpad.net/ubuntu/+source/gnome-software/+bug/1572606)

* Missing some details for apps that aren't installed [bugs.launchpad.net/ubuntu/+source/gnome-software/+bug/1564621](https://bugs.launchpad.net/ubuntu/+source/gnome-software/+bug/1564621) [bugs.launchpad.net/ubuntu/+source/gnome-software/+bug/1571414](https://bugs.launchpad.net/ubuntu/+source/gnome-software/+bug/1571414)

* Removing apps leaves dependencies installed [bugs.launchpad.net/ubuntu/+source/gnome-software/+bug/1552792](https://bugs.launchpad.net/ubuntu/+source/gnome-software/+bug/1552792)

* Doesn't recognize self-reviews [bugs.launchpad.net/ubuntu/+source/gnome-software/+bug/1564209](https://bugs.launchpad.net/ubuntu/+source/gnome-software/+bug/1564209)

* Review stars aren't clickable [bugs.launchpad.net/ubuntu/+source/gnome-software/+bug/1549555](https://bugs.launchpad.net/ubuntu/+source/gnome-software/+bug/1549555)

* Doesn't use full deb descriptions or translations [bugs.launchpad.net/ubuntu/+source/gnome-software/+bug/1559338](https://bugs.launchpad.net/ubuntu/+source/gnome-software/+bug/1559338)

* Upgrades from previous versions can result in two Software Center icons in the launcher.  One for the old Ubuntu Software Center and one for the new Ubuntu Software application.  The Ubuntu Software Center icon can be removed if required.


(16-04-lts-server)=
### Server


(16-04-lts-http-2-support-in-apache-httpd)=
#### HTTP/2 support in Apache httpd

HTTP/2 support is [considered an experimental feature](https://httpd.apache.org/docs/2.4/mod/mod_http2.html) by the Apache httpd upstream project, and so we do not consider it suitable or maintainable for the 5 year supported period of this LTS release. Therefore HTTP/2 support is not available in our builds of Apache httpd.

We expect to issue stable release updates enabling HTTP/2 support after the Apache httpd upstream considers this support to be non-experimental, although this will depend on our assessment of the risk of regression to existing Xenial users at that time.



(16-04-lts-graphics-and-display)=
### Graphics and Display


(16-04-lts-fglrx)=
#### fglrx

The fglrx driver is now deprecated in 16.04, and we recommend its open source alternatives (radeon and amdgpu). AMD put a lot of work into the drivers, and we backported kernel code from Linux 4.5 to provide a better experience.

When upgrading to Ubuntu 16.04 from a previous release, both the fglrx driver and the xorg.conf will be removed, so that the system is set to use either the amdgpu driver or the radeon driver (depending on the available hardware).

More information is available at [tjaalton.wordpress.com/2016/03/11/no-catalystfglrx-video-driver-in-ubuntu-16-04/](https://tjaalton.wordpress.com/2016/03/11/no-catalystfglrx-video-driver-in-ubuntu-16-04/)

(16-04-lts-6th-gen-intel-core-cpus-and-llvmpipe-software-rasterizer)=
#### 6th gen Intel Core CPUs and llvmpipe software rasterizer

LLVM-3.8 enables AVX512 on all 6th generation Intel Core CPUs ("Skylake") when it should be enabled only on server CPU's. This causes the user session to fail to start when Mesa llvmpipe driver is used. This should happen only when the system has a separate GPU which isn't natively supported by open source drivers.

This bug will be handled in a post-release update. In order to install a machine suffering from this remember to boot directly to the installer instead of live-session which doesn't start, and select the option to "Download updates while installing" to make sure updated packages are installed before logging in for the first time. [bugs.launchpad.net/ubuntu/+source/llvm-toolchain-3.8/+bug/1564156](https://bugs.launchpad.net/ubuntu/+source/llvm-toolchain-3.8/+bug/1564156)




(16-04-lts-official-flavours)=
## Official flavours

The release notes for the official flavours can be found at the following links:

* Kubuntu [wiki.ubuntu.com/XenialXerus/ReleaseNotes/Kubuntu](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/Kubuntu)

* Lubuntu [wiki.ubuntu.com/XenialXerus/ReleaseNotes/Lubuntu](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/Lubuntu)

* Ubuntu GNOME [wiki.ubuntu.com/XenialXerus/ReleaseNotes/UbuntuGNOME](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/UbuntuGNOME)

* Ubuntu Kylin [wiki.ubuntu.com/XenialXerus/ReleaseNotes/UbuntuKylin](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/UbuntuKylin)

* Ubuntu Kylin 中文 [wiki.ubuntu.com/XenialXerus/ReleaseNotes/UbuntuKylinChinese](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/UbuntuKylinChinese)

* Ubuntu Mate [ubuntu-mate.org/blog/ubuntu-mate-xenial-final-release/](https://ubuntu-mate.org/blog/ubuntu-mate-xenial-final-release/)

* Ubuntu Studio [wiki.ubuntu.com/XenialXerus/ReleaseNotes/UbuntuStudio](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/UbuntuStudio)

* Xubuntu [xubuntu.org/news/xubuntu-16-04-1-release](https://xubuntu.org/news/xubuntu-16-04-1-release)


* Mythbuntu [www.mythbuntu.org/home/news/mythbuntu1604released](http://www.mythbuntu.org/home/news/mythbuntu1604released)


(16-04-lts-more-information)=
## More information


(16-04-lts-reporting-bugs)=
### Reporting bugs

Your comments, bug reports, patches and suggestions will help fix bugs and improve the quality of future releases. Please [report bugs using the tools provided](http://help.ubuntu.com/community/ReportingBugs).

If you want to help out with bugs, the [Bug Squad](http://wiki.ubuntu.com/BugSquad) is always looking for help.


(16-04-lts-participate-in-ubuntu)=
### Participate in Ubuntu


If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

[www.ubuntu.com/community/get-involved](http://www.ubuntu.com/community/get-involved)


(16-04-lts-more-about-ubuntu)=
### More about Ubuntu

You can find out more about Ubuntu on the [Ubuntu website](http://www.ubuntu.com) and [Ubuntu wiki](http://wiki.ubuntu.com).

To sign up for future Ubuntu development announcements, please subscribe to Ubuntu's development announcement list at:

[lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce](http://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce)
