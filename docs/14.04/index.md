---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes -->

(ubuntu-14-04-lts-release-notes)=
# Ubuntu 14.04 LTS release notes

(14-04-lts-introduction)=
## Introduction

These release notes for **Ubuntu 14.04.6** (Trusty Tahr) provide an overview of the release and document the known issues with Ubuntu 14.04.6 and its flavors.  For details of the changes applied since 14.04.5, please see the [14.04.6 change summary](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes/ChangeSummary/14.04.6).  The release notes for [14.04](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes/14.04), [14.04.1](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes/14.04.1), [14.04.2](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes/14.04.2), [14.04.3](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes/14.04.3), [14.04.4](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes/14.04.4), and [14.04.5](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes/14.04.5) are available as well.


(14-04-lts-support-lifespan)=
### Support lifespan

Ubuntu 14.04 LTS will be supported for 5 years for Ubuntu Desktop, Ubuntu Server, Ubuntu Core, Kubuntu, Edubuntu, and Ubuntu Kylin.  All other flavours will be supported for 3 years.


(14-04-lts-official-flavour-release-notes)=
### Official flavour release notes

Find the links to release notes for official flavors [here](https://wiki.ubuntu.com/Official_flavours).


(get-ubuntu-14-04-lts)=
## Get Ubuntu 14.04 LTS


(download-ubuntu-14-04-lts)=
### Download Ubuntu 14.04 LTS

Images can be downloaded from a location near you.
##
**Note:** The Ubuntu Desktop images are now bigger than a standard CD, and you should use a USB or DVD for installation.

You can download ISOs from:

[releases.ubuntu.com/14.04.5/](http://releases.ubuntu.com/14.04.5/) (Ubuntu Desktop and Server)

[cloud-images.ubuntu.com/releases/14.04.5/release/](http://cloud-images.ubuntu.com/releases/14.04.5/release/) (Ubuntu Cloud Server)

[cdimage.ubuntu.com/netboot/14.04.5/](http://cdimage.ubuntu.com/netboot/14.04.5/) (Ubuntu Netboot)

[cdimage.ubuntu.com/ubuntu-base/releases/14.04.5/release/](http://cdimage.ubuntu.com/ubuntu-base/releases/14.04.5/release/) (Ubuntu Base)

[cdimage.ubuntu.com/edubuntu/releases/14.04.5/release/](http://cdimage.ubuntu.com/edubuntu/releases/14.04.5/release/) (Edubuntu DVD)

[cdimage.ubuntu.com/kubuntu/releases/14.04.5/release/](http://cdimage.ubuntu.com/kubuntu/releases/14.04.5/release/) (Kubuntu)

[cdimage.ubuntu.com/lubuntu/releases/14.04.5/release/](http://cdimage.ubuntu.com/lubuntu/releases/14.04.5/release/) (Lubuntu)

[cdimage.ubuntu.com/ubuntustudio/releases/14.04.5/release/](http://cdimage.ubuntu.com/ubuntustudio/releases/14.04.5/release/) (Ubuntu Studio)

[cdimage.ubuntu.com/ubuntu-gnome/releases/14.04.5/release/](http://cdimage.ubuntu.com/ubuntu-gnome/releases/14.04.5/release/) (Ubuntu GNOME)

[cdimage.ubuntu.com/ubuntukylin/releases/14.04.5/release/](http://cdimage.ubuntu.com/ubuntukylin/releases/14.04.5/release/) (UbuntuKylin)

[cdimage.ubuntu.com/xubuntu/releases/14.04.5/release/](http://cdimage.ubuntu.com/xubuntu/releases/14.04.5/release/) (Xubuntu)

[cdimage.ubuntu.com/mythbuntu/releases/14.04.5/release/](http://cdimage.ubuntu.com/mythbuntu/releases/14.04.5/release/) (Mythbuntu)



(14-04-lts-upgrading-from-ubuntu-12-04-lts-or-ubuntu-13-10)=
### Upgrading from Ubuntu 12.04 LTS or Ubuntu 13.10

To upgrade on a desktop system:

* Press Alt+F2 and type in "update-manager" (without the quotes) into the command box.

* Update Manager should open up and tell you: New distribution release '14.04 LTS' is available.

* Click Upgrade and follow the on-screen instructions.

To upgrade on a server system:

* Install the `update-manager-core` package if it is not already installed.

* Launch the upgrade tool with the command `sudo do-release-upgrade`.

* Follow the on-screen instructions.
Note that the server upgrade will use GNU screen and automatically re-attach in case of dropped connection problems.

Offline upgrade options via alternate CDs are no longer offered for Ubuntu Desktop and Ubuntu Server. Please ensure you have network connectivity to one of the official mirrors or to a locally accessible mirror and follow the instructions above.


(new-features-in-14-04-lts)=
## New features in 14.04 LTS

Please see the [Trusty blueprint list](https://blueprints.launchpad.net/ubuntu/trusty/+specs) for details.

Please test and report any bugs you find:

[help.ubuntu.com/community/ReportingBugs](http://help.ubuntu.com/community/ReportingBugs)


(14-04-lts-lts-hardware-enablement-stack)=
### LTS Hardware Enablement Stack

In an effort to support a wider variety of hardware on an existing LTS release, the 14.04.5 point release will ship with an updated kernel and X stack by default. This newer hardware enablement stack will be comprised of the kernel and X stack from the Xenial 16.04 release.  Those running virtual or cloud images should not need this newer hardware enablement stack and thus it is recommended they remain on the original Trusty stack.  To remain on the original Trusty stack, there are a few options:

* Install from a previous 14.04.0 or 14.04.1 point release and update. The previous 14.04.0 and 14.04.1 releases are archived at [old-releases.ubuntu.com/](http://old-releases.ubuntu.com/)

* Perform an update or upgrade to Trusty from a previous Ubuntu release. Only those installing from the 14.04.2 media or newer will automatically receive a newer hardware enablement stack by default.

* Perform a network install using the `netboot` images rather than the new `utopic-netboot`, `vivid-netboot`, `wily-netboot`, or `xenial-netboot` images.

Anyone wishing to opt into the hardware enablement stack for Trusty may do so by running following command which will install the linux-generic-lts-xenial and xserver-xorg-lts-xenial packages:

` sudo apt-get install --install-recommends linux-generic-lts-xenial xserver-xorg-core-lts-xenial xserver-xorg-lts-xenial xserver-xorg-video-all-lts-xenial xserver-xorg-input-all-lts-xenial libwayland-egl1-mesa-lts-xenial `

If you are on an amd64 system that boots with UEFI, you will also need the matching signed kernel:

` sudo apt-get install linux-signed-generic-lts-xenial `

For anyone interested, the specifics regarding the exact policies and procedures regarding the support, maintenance, and upgrade paths for the hardware enablement stack has been documented at the following location:

[wiki.ubuntu.com/Kernel/LTSEnablementStack](https://wiki.ubuntu.com/Kernel/LTSEnablementStack)


(fglrx-and-the-14-04-5-hwe-stack)=
#### fglrx and the 14.04.5 HWE stack

With 14.04.5, 14.04.2 through 14.04.4 have gone EOL. End-users may have previously used the proprietary fglrx driver, but as documented [here](https://help.ubuntu.com/community/RadeonDriver) fglrx will not work with the 14.04.5 kernel/X stack. If users want to continue using fglrx, the will need to use the 14.04.1 kernel/X stack:

` sudo apt-get install --install-recommends linux-generic xserver-xorg-core xserver-xorg xserver-xorg-video-all xserver-xorg-input-all libwayland-egl1-mesa libcheese-gtk23 libcheese7 libclutter-1.0.0 libclutter-gtk-1.0.0 libcogl15 libclutter-gst-2.0.0 gstreamer1.0-clutter `


(14-04-lts-updated-packages)=
### Updated Packages

As with every new release, packages--applications and software of all kinds--are being updated at a rapid pace. Many of these packages came from an automatic sync from [Debian](http://www.debian.org)'s unstable branch; others have been explicitly pulled in for Ubuntu 14.04 LTS.

For a list of all packages being accepted for Ubuntu 14.04 LTS, please subscribe to [trusty-changes](https://lists.ubuntu.com/mailman/listinfo/trusty-changes).


(14-04-lts-linux-kernel-4-4)=
#### Linux kernel 4.4

By default, the 14.04.5 point release will ship with a newer [4.4](https://launchpad.net/ubuntu/+source/linux-lts-xenial) Linux kernel from Ubuntu 16.04, and a matching X.org stack.  This is based on the [4.4.0](http://kernel.ubuntu.com/git?p=ubuntu/linux.git) [Extended Upstream Stable Kernel Release](https://wiki.ubuntu.com/Kernel/Dev/ExtendedStable).  The purpose of providing a newer kernel in the 14.04.5 point release is for hardware enablement.  For more information regarding the 14.04.5 LTS Hardware Enablement Stack, please refer to:

* [wiki.ubuntu.com/TrustyTahr/ReleaseNotes#LTS_Hardware_Enablement_Stack](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes#LTS_Hardware_Enablement_Stack)


(14-04-lts-python-3-4)=
#### Python 3.4

We eventually intend to ship only [Python 3](http://docs.python.org/py3k/whatsnew/3.0.html) with the Ubuntu desktop image, not Python 2.  The Ubuntu 14.04 LTS image continues this process, although we will not be able to convert everything to Python 3 for the Ubuntu 14.04 LTS release.

If you have your own programs based on Python 2, fear not!  Python 2 will continue to be available (as the `python` package) for the foreseeable future.  However, to best support future versions of Ubuntu you should consider porting your code to Python 3.  [Python/3](https://help.ubuntu.com/community/Python/3) has some advice and resources on this.


(14-04-lts-apparmor)=
#### AppArmor

AppArmor has a number of new features in Ubuntu 14.04 LTS LTS. Notably:

* Support for fine-grained mediation of signal(7)

* Support for fine-grained mediation of ptrace(2)

* Improved DBus mediation

* New abstractions for applications running under Unity

* Several new tunables supporting XDG user directories, dovecot and more

* Various policy updates in support of new features and bug fixes

* A new `@{profile_name}` variable to reference the current profile name within policy

* New Python and Python3 AppArmor libraries (python-apparmor and python3-apparmor)

AppArmor policy has been adjusted for packages that ship it to work with these changes, but local policy may need to be adjusted, especially for signal and ptrace rules. See `man 5 apparmor.d` for details.


(14-04-lts-oxide)=
#### Oxide

Oxide is a webview based on Chromium to deliver web content. Oxide allows us to better support 3rd party developers and applications within the Ubuntu archive by providing a fast, secure and up to date webengine library for the duration of the LTS. While other web content libraries such as those based on webkit are available, their maintenance will be limited to new upstream minor version releases only, and application developers are encouraged to use Oxide instead.


(14-04-lts-upstart-1-12-1)=
#### Upstart 1.12.1

Upstart has been upgraded to version 1.12.1. More details are available in the
[Upstart Technical Overview](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes/TechnicalOverviewUpstart).


(14-04-lts-ubuntu-desktop)=
### Ubuntu Desktop


(14-04-lts-unity)=
#### Unity

Unity Desktop has been streamlined for the 14.04 LTS release. Important new features include:

* Support for High-DPI screens and desktop scaling

* New screen saver and lock screen that matches the Unity greeter visual designs, with improved speed and security.

* The option (under Appearance settings) to show menus embedded in the window's title bar instead of the top menu bar

* The application spread (Super + W) has been redesigned, with new features including the ability to type in order to filter the displayed applications / windows

* New window decorations, with improved appearance and performance. Windows contents are now updated live as they are resized

* Dash scopes can now be enabled and disabled from Application lens, inside dash itself


(14-04-lts-general)=
#### General

The rest of the Ubuntu desktop also received many updates. Some important changes include:

* Nautilus now defaults to type-ahead find instead of intiating a search when you are looking for files within a directory

* Many default applications regained well-integrated menu bars under Unity

* New Ubuntu-specific settings application, derived from GNOME's control center


(14-04-lts-libreoffice)=
#### LibreOffice

The LibreOffice office suite has been updated to the latest and greatest version, 4.2.8, containing new features:

* General

  * A new [start center](https://wiki.documentfoundation.org/images/5/5e/UbuntuStartCenter.png) gives previews and easy access to recently used documents

  * A new [flat icon theme: sifr](http://skyfromme.files.wordpress.com/2014/01/cat.png), installable with apt-get install libreoffice-style-sifr

  * initial [HiDPI support](https://wiki.documentfoundation.org/Development/HiDpi)

  * Improved import and export filters

  * support for BCP 47 language tags

  * support for native MATE and XFCE file dialogs

* Writer

  * a new default document template

  * in-place editing of text fields

  * document search for right-to-left languages

  * spellcheck and change tracking consolidated

* Calc

  * trendline enhancements: multiple trendlines, force intercept, extrapolation, polynominals, moving averages

  * a new calculation engine, paving the way for high performance calculation on graphics cards with OpenCL

  * quick right-click context menu to switch between sheets

  * random number generation and statistic functions

  * functions to access web data (WEBSERVICE, FILTERXML)

  * new functions: LEFTB, LENB, MIDB, RIGHTB, COVARIANCE.P, COVARIANCE.S, STDEV.P, STDEV.S, VAR.P, VAR.S, BETA.DIST, BETA.INV, BINOM.DIST, BINOM.INV, CONFIDENCE.NORM, CONFIDENCE.T, F.DIST, F.DIST.RT, F.INV, F.INV.RT, F.TEST, EXPON.DIST, HYPGEOM.DIST, POISSON.DIST, WEIBULL.DIST, CHISQ.DIST, CHISQ.DIST.RT, CHISQ.INV, CHISQ.INV.RT,CHISQ.TEST, CRITBINOM

The full list of new features in LibreOffice 4.2 can be found [here](https://wiki.documentfoundation.org/ReleaseNotes/4.2).


(14-04-lts-xorg)=
#### Xorg

The Xorg display server and drivers have been updated to the 15.0.1 release and mesa has been updated to 10.1.


(14-04-lts-ubuntu-server)=
### Ubuntu Server


(14-04-lts-openstack-2014-1)=
#### OpenStack 2014.1

Ubuntu 14.04 LTS includes the OpenStack 2014.1 (Icehouse) release of the following projects in Ubuntu main:

* OpenStack Compute - Nova
* OpenStack Identity - Keystone
* OpenStack Imaging - Glance
* OpenStack Block Storage - Cinder
* OpenStack Networking - Neutron
* OpenStack Object Storage - Swift
* OpenStack Telemetry - Ceilometer
* OpenStack Orchestration - Heat
* OpenStack Dashboard - Horizon

The OpenStack Charms for deploying OpenStack using Juju have been updated to support deployment of Icehouse - see the charm [release notes](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes/OpenStackCharms) for full details.

**WARNING**: Upgrading an OpenStack deployment is a non-trivial process and care should be taken to plan and test upgrade procedures which will be specific to each OpenStack deployment.

Users of OpenStack 2012.1 (Essex) on Ubuntu 12.04 should note that several components have changed/been superseded over the last two years:

* Nova Volume has been replaced by Cinder.

* Neutron has been introduced alongside Nova Network (deprecated but not removed yet).

* The configuration file format has changed from a flags based format to a section based ini style format - configuration files should be reviewed and updated accordingly.

Existing OpenStack installations must be step upgraded through interim OpenStack releases (Folsom, Grizzly and Havana) using the [Ubuntu Cloud Archive](https://wiki.ubuntu.com/ServerTeam/CloudArchive) for Ubuntu 12.04.  The Ubuntu Cloud Archive also provides the Icehouse release for 12.04; Users may prefer to upgrade to this release on 12.04 prior to upgrading the base Ubuntu operating system to Ubuntu 14.04 LTS.

Please refer to the upstream [release notes](https://wiki.openstack.org/wiki/ReleaseNotes/) for full details of upgrading between OpenStack releases and the features introduced in each release.


(14-04-lts-puppet-3)=
#### Puppet 3

Ubuntu 14.04 LTS includes Puppet 3.  This is a major version upgrade from previous Ubuntu LTS releases and includes many changes which are not compatible with Puppet 2.7.x.

Please review the upstream [release notes](http://docs.puppetlabs.com/puppet/3/reference/release_notes.html#upgrade-warning-many-breaking-changes) to determine which breaking changes apply to your installation.


(14-04-lts-xen-4-4)=
#### Xen 4.4

Ubuntu 14.04 LTS includes Xen 4.4. This is a significant upgrade from the previous release.  Of particular note the xen hypervisor no longer supports 32bit only CPUs on the x86 architecture; 32bit Dom 0 running on the 64bit hypervisor is still supported.  The hypervisor will automatically be upgraded to the 64bit version (the Dom 0 does not need to change).  Ensure your host is 64bit capable _before_ upgrading.

Also the XM (xend) management stack has been deprecated since Xen 4.1 and will be removed in the next version of Xen (4.5). Therefore we urge all users to start using the new xl toolstack. For that reason the default toolstack setting (/etc/default/xen) is changed to xl.

The format of normal configuration files is mostly identical, only usage of Python inside the config file is [no longer supported](http://wiki.xenproject.org/wiki/MigrationGuideToXen4.1%2B#Toolstack_upgrade_notes). Also managed domains, which were managed by xend and stored in a different (sxpr) format will need to be migrated. When upgrading to Xen-4.4 an automatic migration of xend managed domains into xen and libvirt config files is attempted. However, due to many dependencies, this is failing more often than not. So when upgrade has been done and the host is running the new Xen hypervisor, the migration into xen config files can be started by calling "sudo /usr/lib/xen-4.4/bin/xen-migrate-xend-managed-domains". The resulting config files are written into /etc/xen and should be reviewed before usage.

Likewise, when libvirt is used to manage machines, the xend managed domains can be migrated into libvirt xml definitions by calling "sudo libvirt-migrate-xend-managed-domains". The resulting definitions should also get reviewed before usage (either virt-manager, virsh or looking in /etc/libvirt/libxl).

Once the new VM configs are working, it is recommended to remove the old ones (/var/lib/xend/domains/). This is not done automatically for safety reasons.


(14-04-lts-ceph-0-79)=
#### Ceph 0.79

Ubuntu 14.04 LTS includes Ceph 0.79; Ceph will be upgraded to the Firefly stable release via a stable release update when 0.80 is released upstream.  This release of Ceph includes efficient erasure coding of data for cold storage and tiered pooling. Please refer to the [upstream release notes](http://ceph.com/docs/master/release-notes/) for full details on upgrading.


(14-04-lts-qemu-2-0-0)=
#### Qemu 2.0.0

Ubuntu 14.04 LTS includes Qemu 2.0.0.  Due to incompatibilities in the emulated hardware, live migration of pc-1.0 KVM virtual machines created on 12.04 is limited.  To migrate such a VM, you must install the kvm-ipxe-legacy package, and use the "-M pc-1.0-precise" qemu option.  If using libvirtd, you must set the 'allow_incoming_qemukvm = 1" option in /etc/qemu/qemu.conf.  Such VMs cannot be migrated to releases later than 14.04 without first converting them to a newer machine type.

User emulation of arm64 binaries is now supported, and support for armhf and arm64 kvm-accelerated virtual machines is now available.

From 12.04 to 14.04, the default vmware vga memory size for machine type pc-1.0 has been reduced.  If you are using a desktop image and being placed in low graphics mode, then switching to a new machine type, for instance pc-1.2 pc-i440fx-1.7, should solve the problem.


(14-04-lts-open-vswitch-2-0-1)=
#### Open vSwitch 2.0.1

Ubuntu 14.04 LTS includes Open vSwitch 2.0.1.  See the upstream [release notes](https://github.com/openvswitch/ovs/blob/branch-2.0/NEWS) for details of all features included in this release.  Note that the openvswitch-datapath-dkms package is not compatible with the Linux 3.13 kernel shipped as default in 14.04 LTS; The native Open vSwitch module in the 3.13 kernel provides all the features of the dkms module apart from support for experimental LISP tunnelling and should be used instead.


(14-04-lts-libvirt-1-2-2)=
#### Libvirt 1.2.2

Ubuntu 14.04 LTS includes Libvirt 1.2.2 with full support for ceph and Xen 4.4


(14-04-lts-lxc-1-0)=
#### LXC 1.0

Ubuntu 14.04 LTS includes the newly released LXC 1.0, featuring fully unprivileged containers, a
new more flexible seccomp policy language, fast container clones using btrfs, overlayfs,
LVM or zfs backing stores, API bindings for python 3.0, go, ruby, lua and C, and SELinux
support.


(14-04-lts-maas-1-7)=
#### MAAS 1.7

Ubuntu 14.04 LTS contains [MAAS version 1.7](http://maas.ubuntu.com/docs1.7/).  In addition to bug fixes and minor improvements, MAAS version 1.7 contains the following major features:

* [Advanced Networking](http://maas.ubuntu.com/docs1.7/networks.html#networks): MAAS now supports multiple managed network interfaces in a single cluster, and has support for VLANs.

* [Zones](http://maas.ubuntu.com/docs1.7/physical-zones.html): A Zone is arbitrary grouping of nodes.  This grouping can then be used as a constraint for deployment.

* [Hardware Enablement Kernels](http://maas.ubuntu.com/docs1.7/hardware-enablement-kernels.html): MAAS now supports using kernels other than the default kernel for an Ubuntu release.  This includes enlistment, commissioning and deployment and is primarily focused on allowing users to use [Hardware Enablement Kernels](https://wiki.ubuntu.com/Kernel/LTSEnablementStack).

See the upstream [changelog](http://maas.ubuntu.com/docs1.5/changelog.html) for full change information.


(14-04-lts-juju-1-22-6)=
#### Juju 1.22.6

Ubuntu 14.04 LTS includes the latest stable release of Juju, the service orchestration tool for Ubuntu.  See the upstream [release notes](https://juju.ubuntu.com/docs/reference-release-notes.html) for full details of all new features and improvements in this release.  Existing 1.16.6 juju environments can be upgraded to 1.22.6 by running:

```none
juju upgrade-juju
```


(14-04-lts-strongswan)=
#### strongSwan

Ubuntu 14.04 LTS now includes official support for strongSwan IPSec. strongSwan is a [feature rich, modern IPSec solution](http://www.strongswan.org/). ipsec-tools, the supported IPSec solution in prior releases of Ubuntu, now receives community support and users are encouraged to migrate to strongSwan to maintain official support. For more information, please see [this page](https://help.ubuntu.com/community/strongSwan).


(14-04-lts-mysql)=
#### MySQL

Ubuntu 14.04 LTS continues to provide official support for MySQL 5.5. Three other community supported alternatives of MySQL are also included:

* MariaDB 5.5 - a drop in replacement for MySQL 5.5.
* Percona XtraDB Cluster 5.5 - a Galera based Active/Active MySQL solution.
* MySQL 5.6 - the next release of Oracle's MySQL.

Note that upgrading to MySQL 5.6 is an automatic one way process; it is possible to downgrade manually - see the [upstream documentation](http://dev.mysql.com/doc/refman/5.6/en/downgrading-to-previous-series.html) on details of how to perform this process.


(14-04-lts-apache-2-4)=
#### Apache 2.4

Ubuntu 14.04 LTS includes Apache 2.4; this is a major version upgrade from Apache 2.2 in Ubuntu 12.04 LTS and users should take care to read the [upgrade notes](http://sources.debian.net/src/apache2/2.4.9-1/debian/apache2.NEWS) included in the packaging and the upstream [upgrading](http://httpd.apache.org/docs/2.4/upgrading.html) documentation.


(14-04-lts-php-5-5)=
#### PHP 5.5

PHP has been updated to 5.5, which is a major upgrade from 5.3 as available in
the previous LTS. Upstream introduced some incompabilities in this update, and
recommend testing before upgrading production environments. For more details,
see the [PHP migration guide](http://php.net/manual/en/migration55.changes.php).

Due to licensing problems, Debian dropped the PHP-supplied json module in
[Debian bug 692613](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=692613),
replacing it with a compatible json module instead. Ubuntu is aligned with
Debian by default, and thus has picked up this change in 14.04 LTS, first
in 13.10. The upgrade process will automatically pull in the new module.
There have been claims of some edge case incompabilities in
[bug 1287726](https://bugs.launchpad.net/ubuntu/+source/php-json/+bug/1287726); testing is advised.


(14-04-lts-ubuntu-touch)=
### Ubuntu Touch

As part of the wider Ubuntu 14.04 release efforts the Ubuntu Touch team is proud to make the latest and greatest touch experience available to our enthusiast users and developers.

While this Ubuntu Touch release is still not a supported release, we feel it is important to hand out a relatively "stable" build for wider testing and feedback while we are continuing with high velocity towards our going-to-market milestone late this summer. Also, while not product quality yet, this image is a big step forward feature-wise compared to our initial release done in October 2013, so we hope you will enjoy using this on your phone and tablet.


(14-04-lts-devices)=
#### Devices

For this milestone we added tablets to the mix of devices we offer builds for. The set of devices with builds available is:

* Nexus 4 Phone (mako)
* Nexus 7 (2013) Tablet (flo)
* Nexus 10 Tablet (manta)

Unfortunately, we had to drop support for some platforms that previously had maintained builds to allow our engineering team to stay focussed on a small set of mobile hardware that are close to what we will have to support when going to market later this year. The following devices we stopped producing builds for:

* Galaxy Nexus Phone (maguro)
* Nexus 7 (2012) Tablet (grouper)


(14-04-lts-how-to-install-or-update)=
#### How to install or update

Our 14.04 release images are now available for consumption through our “stable” touch channel. Instructions on how to install Ubuntu Touch on those devices are available at [wiki.ubuntu.com/Touch/Install](https://wiki.ubuntu.com/Touch/Install). You can also proceed with a system update on the officially-supported devices running the latest stable image.


(14-04-lts-what-s-new)=
#### What’s new?


(14-04-lts-tablet-and-phone-form-factors-supported)=
##### Tablet and Phone form factors supported

This version features the tablet form-factor with the introduction of the side-stage when the screen size gives enough room to display it. You are able to set a phone-factor application into that side-stage and switch between the main and side stages. Multiple core applications as well have been extended to support and be responsive for various form factors and screen sizes in addition to getting a ton of new features and bug fixes.


(14-04-lts-a-new-scope-and-homescreen-experience)=
##### A new Scope and Homescreen experience

The home screen and scope experience has seen a complete overhaul, delivering an even better and more stunning experience than before. Users can now enable and disable scopes to get more control about what is searched and delivering more accurate answers and will surely see the attention to detail that our design and engineering team has put into bringing these main UI experiences to where we are now. Give it a try!


(14-04-lts-webapp-story-gets-upgraded-through-oxide-engine)=
##### Webapp story gets upgraded through oxide engine

The Web applications story just got boosted through integration of the oxide engine, a new web container featuring the V8 javascript engine and chromium rendering. With this we are now delivering an even faster web experience than before. Note that our browser is also using the same technology for a reliable and relaxing daily browsing experience.


(14-04-lts-plumbing-layer-comes-with-all-the-latest-from-ubuntu-and-android-4-4-and-qt-5-2)=
##### Plumbing layer comes with all the latest from Ubuntu and Android 4.4 and Qt 5.2

On top of the usual freshness of the core stack that comes with an Ubuntu release, we upgraded our UI toolkit to Qt 5.2, featuring the new v4 javascript engine, and also uplevelled our enablement stack to Android 4.4 to better support latest android devices.


(14-04-lts-developers-get-more-features-and-convenience)=
##### Developers get more features and convenience

On the developer side, a new layout framework and new facilities like tabulation title enhancement inherited by the new SDK release are available in our 14.04 framework. Also, developers can now use an emulator on their Ubuntu Desktop to do app and core system development.


(14-04-lts-and-more)=
##### And more ...

On top of the highlighted items above, there are many user noticeable improvements.  Here is a short list:

* support for multiple sim cards and simultaneous calls
* render optimizations through MIR and Qt
* working app lifecycle support so you never run out of memory
* geolocation support
* initial alarm system
* calendar and contact sync
* user notifications for system events such as available system images

Of course, this is just the tip of the iceberg. Just go ahead and experience it yourself. We are looking forward to your feedback and bugs!


(14-04-lts-notes-issues-we-are-tracking)=
#### Notes/Issues we are tracking

Here a list of issues we would like to point out for users that want to try installing or upgrading from Ubuntu 13.10:

* System upgrade dialog displays 13.10 while you are installing 14.04. However, you will be as expected on a 14.04-based Ubuntu Touch version after the upgrade. (Bug:1308980)

* After upgrading your 13.10 install to 14.04 your language setting will be forgotten; to workaround just go to the settings dialog after the upgrade and change it back to your preferred choice (Bug:1308888)

* After upgrading your 13.10 Ubuntu touch phone to 14.04 your crash reporting/diagnosis setting will be forgotten; to workaround just go to the settings dialog after the upgrade and change it back to your preferred choice  (Bug:1308917)

* Music and events like alarms won't be triggered if the device is sleeping for too long (Bug:1292306)

* New scopes cause some slowdown in UI responsiveness; while we fixed a good part of it in days before release, there is still a noticeable performance impact (Bug:1297197)

* Clock app crashes when trying to access a saved alarm (Bug:1309057)


(14-04-lts-getting-in-touch-with-ubuntu-touch-team)=
#### Getting in Touch with Ubuntu Touch Team

Learn more and get involved:

* For technical discussion: [launchpad.net/~ubuntu-phone](http://launchpad.net/~ubuntu-phone)

* For real-time chat: [webchat.freenode.net/?channels=ubuntu-touch](http://webchat.freenode.net/?channels=ubuntu-touch)

* Contribute: [wiki.ubuntu.com/Touch/Contribute](http://wiki.ubuntu.com/Touch/Contribute)

* Got questions? [askubuntu.com/questions/ask?tags=ubuntu-touch](http://askubuntu.com/questions/ask?tags=ubuntu-touch)

* If you develop apps for the phone: [developer.ubuntu.com](http://developer.ubuntu.com)


(14-04-lts-known-issues)=
## Known issues

As is to be expected, at this stage of the release process, there are some significant known bugs that users may run into with this release of Ubuntu 14.04.  The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:



(14-04-lts-boot-installation-and-post-install)=
### Boot, installation and post-install

* Automatic install is broken on drives that contain partitions that either do not have an operating system installed (eg. a user data partition like /home on Linux or D: on Windows), or partitions that have Windows 8 installed. Selecting automatic install (or upgrade) on these systems will result in the **whole drive being wiped and all existing data will be lost**. There are also problems dealing with systems with multiple drives. This bug is present in released media of 14.04 and 14.04.1, but is fixed for 14.04.2 and later. If you have a drive with any pre-existing partitions, or multiple drives, then you should use manual partitioning. Ensure you have backups. (Bug:1265192)

* The desktop image installer cannot unlock existing encrypted (LUKS) volumes.  If you need to make use of existing encrypted volumes during partitioning, then use the "Try Ubuntu without installing" boot option to start a live session, open the encrypted volumes (for example, by clicking on their icons in the Unity launcher), enter your password when prompted to unlock them, close them again, and run `ubiquity` to start the installer.  (Bug:1066480)

* When using installer to upgrade or reinstall an existing installation with encrypted swap, the installer may fail to reuse the partition. A warning will be shown, however the installation can be completed. The installed system will not have swap activated and users are advised to recreate swap on their systems. Please see advice about adding and activating swap at: [help.ubuntu.com/community/SwapFaq](https://help.ubuntu.com/community/SwapFaq) (Bug:1066342)

* Installs on very small memory systems may fail to start or exit without completing with no error. It is recommended that swap be created before install for such systems. Please see advice about adding and activating swap at: [help.ubuntu.com/community/SwapFaq](https://help.ubuntu.com/community/SwapFaq) (Bug:1172161)

* In rare circumstances the 'Next' button on the installer 'Install Type' screen is non-functional.  This is intermittent and may be resolved by hitting 'Back' and retrying.  (Bug:1172572)

* On some systems, after installation, pressing 'Enter' doesn't reboot the system and a hard reset is required (Bug:1297851)

* Live session starts with keyboard set to English US and time zone as UTC even if non-english languages are selected (Bug:1297234)

* In OEM mode, language packs are not installed when the end user selects a non-english language and there is no notification (Bug:1307983) To install additional languages, open "System Settings -> Language Support", the language support tool will the propose to install missing language packs.


(14-04-lts-upgrade)=
### Upgrade

* Automatic upgrade on drives containing user data partitions, including from other operating systems, and all Windows 8 systems, will result in the **whole drive being wiped and all existing data will be lost**. This bug is present in released media of 14.04 and 14.04.1, but is fixed for 14.04.2 and later. If you have a drive with any pre-existing partitions, or multiple drives, then you should use manual partitioning. Ensure you have backups. (Bug:1265192)

* When the system is upgraded from a previous release via the installer, the user has to re-enter their credentials. If the user's home directory is encrypted and the password differs from the password on the pre-upgrade system, the upgrade succeeds but the user cannot login (Bug:1308530)

* Configuration of the package tex-common fails when 12.04 LTS is upgraded to 14.04 LTS (Bug:1304972)

* Configuration of flightgear fails during upgrade from 12.04 LTS to 14.04 LTS (Bug:1308338)


(14-04-lts-power-management)=
### Power Management

* On some systems, when opening lid, there is a kerneloops with a suspend/resume failure message seen. (Bug:1054732)


(14-04-lts-desktop)=
### Desktop

* On rare occasions Unity's Dash doesn't display (nor search for) any applications (Bug:1308037)


(14-04-lts-migration)=
### Migration


(14-04-lts-graphics-and-display)=
### Graphics and Display


(14-04-lts-networking)=
### Networking

* In order to improve compatibility with other local nameserver packages, NetworkManager now assigns IP address 127.0.1.1 to the local nameserver process that it controls instead of 127.0.0.1. If the system's `/etc/resolv.conf` is absent or is a static file instead of the symbolic link to `../run/resolvconf/resolv.conf` installed by default then this static file will have to be updated by the administrator in order to continue using the NetworkManager-controlled nameserver.


(14-04-lts-apparmor-2)=
### AppArmor

* The major tools in apparmor-utils AppArmor 2.8.95 have been rewritten to improve maintainability. While this allows us to better support them and add fixes going forward, currently the aa-genprof and aa-logprof CLI tools contain several bugs (Bug:1294797, Bug:1296218) that affect their utility. These bugs should be fixed before release or in an SRU. It is recommended that people develop policy manually at this time. **Update**: these and other bugs with the python tools have been fixed and the new tools are expected to work better than tools in previous releases.


(14-04-lts-kernel)=
### Kernel

* Bug:1292467 - Some laptops (particularly netbook class) with older graphics can experience poor graphical performance when starting with a high resolution external monitor attached.  The reason for this is that some graphics cards (like the Intel 945GSE) cannot support accelerated 3D graphics when the combined width of both screens exceeds a certain threshold (typically 2048 pixels).  See the bug for appropriate workarounds.


_For a listing of more known issues, please refer to the Trusty Tahr [bug tracker](https://bugs.launchpad.net/ubuntu/trusty/+bugs) in Launchpad._


(14-04-lts-official-flavours)=
## Official flavours

The release notes for the official flavours can be found at the following links:

* Edubuntu [wiki.ubuntu.com/TrustyTahr/ReleaseNotes/Edubuntu](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes/Edubuntu)

* Kubuntu [wiki.ubuntu.com/TrustyTahr/ReleaseNotes/Kubuntu](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes/Kubuntu)

* Lubuntu [wiki.ubuntu.com/TrustyTahr/ReleaseNotes/Lubuntu](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes/Lubuntu)

* Mythbuntu [wiki.ubuntu.com/TrustyTahr/ReleaseNotes/Mythbuntu](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes/Mythbuntu)

* Ubuntu GNOME [wiki.ubuntu.com/TrustyTahr/ReleaseNotes/UbuntuGNOME](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes/UbuntuGNOME)

* Ubuntu Kylin [wiki.ubuntu.com/TrustyTahr/ReleaseNotes/Kylin](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes/Kylin)

* Ubuntu Studio [wiki.ubuntu.com/TrustyTahr/ReleaseNotes/UbuntuStudio](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes/UbuntuStudio)

* Xubuntu [wiki.ubuntu.com/TrustyTahr/ReleaseNotes/Xubuntu](https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes/Xubuntu)


(14-04-lts-more-information)=
## More information


(14-04-lts-reporting-bugs)=
### Reporting bugs

Your comments, bug reports, patches and suggestions will help fix bugs and improve the quality of future releases. Please [report bugs using the tools provided](http://help.ubuntu.com/community/ReportingBugs).

If you want to help out with bugs, the [Bug Squad](http://wiki.ubuntu.com/BugSquad) is always looking for help.


(14-04-lts-participate-in-ubuntu)=
### Participate in Ubuntu


If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

[www.ubuntu.com/community/get-involved](http://www.ubuntu.com/community/get-involved)


(14-04-lts-more-about-ubuntu)=
### More about Ubuntu

You can find out more about Ubuntu on the [Ubuntu website](http://www.ubuntu.com) and [Ubuntu wiki](http://wiki.ubuntu.com).

To sign up for future Ubuntu development announcements, please subscribe to Ubuntu's development announcement list at:

[lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce](http://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce)
