---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/SaucySalamander/ReleaseNotes -->

(ubuntu-13-10-release-notes)=
# Ubuntu 13.10 release notes

(13-10-introduction)=
## Introduction

The Ubuntu developers are moving quickly to bring you the absolute latest and greatest software the Open Source community has to offer.


(get-the-ubuntu-13-10)=
## Get the Ubuntu 13.10


(13-10-upgrading-from-ubuntu-13-04)=
### Upgrading from Ubuntu 13.04

To upgrade from Ubuntu 13.04 on a desktop system:

* Open Software Sources.

* Press Alt+F2 and type in "update-manager" (without the quotes) into the command box.

* Update Manager should open up and tell you: New distribution release '13.10' is available.

* Click Upgrade and follow the on-screen instructions.

To upgrade from Ubuntu 13.04 on a server system:

* Install the `update-manager-core` package if it is not already installed.

* Launch the upgrade tool with the command `sudo do-release-upgrade`.

* Follow the on-screen instructions.
Note that the server upgrade will use GNU screen and automatically re-attach in case of dropped connection problems.

Offline upgrade options via alternate CDs are no longer offered for Ubuntu Desktop and Ubuntu Server. Please ensure you have network connectivity to one of the official mirrors or to a locally accessible mirror and follow the instructions above.


(13-10-upgrading-from-other-releases)=
### Upgrading from other releases

Users of other Ubuntu releases need to upgrade first to 13.04, and then to 13.10.

For further information on upgrading to 13.04, please see its [upgrade instructions](https://help.ubuntu.com/community/RaringUpgrades).


(13-10-ubuntu-downloader-for-windows-discontinued)=
### Ubuntu downloader for Windows discontinued

Due to various bugs in Wubi that were not addressed for 13.04, the Wubi installer is again not releasing with 13.10.  You can read more about this decision [here](https://lists.ubuntu.com/archives/ubuntu-devel/2013-April/036993.html).  Users who wish to try out Ubuntu without repartitioning a Windows system are encouraged to use a live system instead, booted from either a DVD or a USB disk.


(13-10-support-lifespan)=
### Support lifespan

Ubuntu 13.10 will only be supported for 9 months. Non-LTS releases prior to Ubuntu 13.04 were supported for 18 months. For more information, please read the announcements [here](http://fridge.ubuntu.com/2013/03/19/changes-in-ubuntu-releases-decided-by-the-ubuntu-technical-board/) or [here](http://fridge.ubuntu.com/2013/03/19/ubuntu-technical-board-looks-at-shuttleworths-proposal-for-release-management-methodology/).


(download-ubuntu-13-10)=
### Download Ubuntu 13.10

Images can be downloaded from a location near you.
##
**Note:** The Ubuntu Desktop images are now bigger than a standard CD, and you should use a USB or DVD for installation.

You can download ISOs from:

[releases.ubuntu.com/13.10/](http://releases.ubuntu.com/13.10/) (Ubuntu Desktop and Server)

[cloud-images.ubuntu.com/releases/13.10/release/](http://cloud-images.ubuntu.com/releases/13.10/release/) (Ubuntu Cloud Server)

[cdimage.ubuntu.com/netboot/13.10/](http://cdimage.ubuntu.com/netboot/13.10/) (Ubuntu Netboot)

[cdimage.ubuntu.com/ubuntu-core/releases/13.10/release/](http://cdimage.ubuntu.com/ubuntu-core/releases/13.10/release/) (Ubuntu Core)

[cdimage.ubuntu.com/edubuntu/releases/13.10/release/](http://cdimage.ubuntu.com/edubuntu/releases/13.10/release/) (Edubuntu DVD)

[cdimage.ubuntu.com/kubuntu/releases/13.10/release/](http://cdimage.ubuntu.com/kubuntu/releases/13.10/release/) (Kubuntu)

[cdimage.ubuntu.com/lubuntu/releases/13.10/release/](http://cdimage.ubuntu.com/lubuntu/releases/13.10/release/) (Lubuntu)

[cdimage.ubuntu.com/ubuntustudio/releases/13.10/release/](http://cdimage.ubuntu.com/ubuntustudio/releases/13.10/release/) (Ubuntu Studio)

[cdimage.ubuntu.com/ubuntu-gnome/releases/13.10/release/](http://cdimage.ubuntu.com/ubuntu-gnome/releases/13.10/release/) (Ubuntu-GNOME)

[cdimage.ubuntu.com/ubuntukylin/releases/13.10/release/](http://cdimage.ubuntu.com/ubuntukylin/releases/13.10/release/) (UbuntuKylin)

[cdimage.ubuntu.com/xubuntu/releases/13.10/release/](http://cdimage.ubuntu.com/xubuntu/releases/13.10/release/) (Xubuntu)

##[cdimage.ubuntu.com/kubuntu-active/releases/13.10/release/](http://cdimage.ubuntu.com/kubuntu-active/releases/13.10/release/) (Kubuntu Active)

To install Ubuntu 13.10 for phones, follow the instructions found at [Touch/Install](https://help.ubuntu.com/community/Touch/Install) to download and flash an image to your device.


(new-features-in-13-10)=
## New features in 13.10

Please see the [Saucy blueprint list](https://blueprints.launchpad.net/ubuntu/saucy/+specs) for details.

Please test and report any bugs you find:

[help.ubuntu.com/community/ReportingBugs](http://help.ubuntu.com/community/ReportingBugs)


(13-10-updated-packages)=
### Updated Packages

As with every new release, packages--applications and software of all kinds--are being updated at a rapid pace. Many of these packages came from an automatic sync from [Debian](http://www.debian.org)'s unstable branch; others have been explicitly pulled in for Ubuntu 13.10.

For a list of all packages being accepted for Ubuntu 13.10, please subscribe to [saucy-changes](https://lists.ubuntu.com/mailman/listinfo/saucy-changes).


(13-10-linux-kernel-3-11)=
#### Linux kernel 3.11

Ubuntu 13.10 includes the [3.11.0-12.19 Ubuntu Linux kernel](https://launchpad.net/ubuntu/+source/linux/3.11.0-12.19) which was based on the [v3.11.3 upstream Linux kernel](http://www.kernel.org/pub/linux/kernel/v3.x/linux-3.11.3.tar.bz2).


(13-10-upstart-1-10)=
#### Upstart 1.10

This release provides a new bridge, the `upstart-file-bridge(8)` that allows jobs to react to filesystem changes. For example, to have a job start when a particular file is created:

```none
start on file FILE=/var/log/foo.log EVENT=create
```

Or to start a job when a file matching a glob pattern is _deleted_:

```none
start on file FILE=/var/app/*.foo EVENT=delete
```

See `upstart-file-bridge(8)` and `file-event(7)` for further details.

Additionally, a new `upstart-monitor(8)` tool is available that allows event flows to be observed in real-time. This tool can run as a graphical or console application.


(13-10-cups-1-7-cups-filters-1-0-40-ghostscript-9-10-cairo-1-12-16)=
#### CUPS 1.7, cups-filters 1.0.40, Ghostscript 9.10, Cairo 1.12.16

There are no big changes in the printing system this time, but many smaller bug fixes and improvements.

CUPS 1.7: Using old CUPS servers via client.conf is now possible by adding "/version=1.1" (specifying the server's IPP version) to the end of the server name in the "ServerName ..." line. This functionality is documented in the CUPS documentation and CUPS' command line tools give an appropriate hint if they fail to access the server and the "/version=1.1" option can solve the problem.

Printer-model-specific USB incompatibility workarounds are now defined in the /usr/share/cups/usb/org.cups.usb-quirks file and so new rules can be easily added by the user or system administrator. Please report a bug in the "cups" package if you have made a printer working by editing this file and tell us what you have changed.

If you had problems of disappearing CUPS configuration files in the past, this should be fixed now. If the problem still occurs, please check whether there is a "SyncOnClose Yes" line in /etc/cups/cups-files.conf.

cups-filters 1.0.40: Several improvements and bug fixes for better compatibility an reliability, like using Poppler for selected PostScript printer brands which do not work with Ghostscript's PostScript output, avoiding bogus filter chains, several memory leak fixes and more are done.

Thanks to Tim Waugh and Jiri Popelka from Red Hat for contributing numerous bug fixes.

Also activated both Bonjour and CUPS browsing by default to pick up shared printers from CUPS servers with any version of CUPS. You can adjust this in /etc/cups/cups-browsed.conf.

Cairo 1.12.16: The print job output of most GNOME applications based on the Cairo graphical library got optimized leading to a much better printing performance especially on PostScript printers.


(13-10-python-3-3)=
#### Python 3.3

We eventually intend to ship only [Python 3](http://docs.python.org/py3k/whatsnew/3.0.html) with the Ubuntu desktop image, not Python 2.  The Ubuntu 13.10 image continues this process, although we will not be able to convert everything to Python 3 for the Ubuntu 13.10 release.

If you have your own programs based on Python 2, fear not!  Python 2 will continue to be available (as the `python` package) for the foreseeable future.  However, to best support future versions of Ubuntu you should consider porting your code to Python 3.  [Python/3](https://help.ubuntu.com/community/Python/3) has some advice and resources on this.


(13-10-apparmor)=
#### AppArmor

AppArmor has a number of new features in Ubuntu 13.10. Notably:

* Support for fine-grained DBus mediation for bus, binding name, object path, interface and member/method (see `man 5 apparmor.d` for details)

* The return of named AF_UNIX socket mediation

* Native AppArmor support in Upstart

* Integration with several services as part of the [ApplicationConfinement](https://wiki.ubuntu.com/SaucySalamander/ReleaseNotes#Application_Confinement) work in support of click packages and the Ubuntu appstore

* Better support for policy generation via the `aa-easyprof` tool and `apparmor-easyprof-ubuntu` policy

AppArmor policy has been adjusted for packages that ship it to work with these changes, but local policy may need to be adjusted, especially for named AF_UNIX sockets where policy created after Ubuntu 8.04 LTS may have missing 'rw' rules allowing the access. For DBus policy, as a transitional step, existing policy for packages that use DBus will continue to have full access to DBus, but future Ubuntu releases may provide fine-grained DBus rules for this software.


(13-10-libreoffice)=
#### LibreOffice

LibreOffice has been updated to version 4.1.2~rc3 which misses no fixes from the upstream 4.1.2 final release. New features in LibreOffice 4.1 include:

* rotation of images in Writer

* font embedding in Writer, Calc and Impress documents should severely improve rendering fidelity across different machines and platforms

* Photo Album creator

* stepped lines charts

* lots of interoperability improvements with Mircosoft Office

* see [LibreOffice 4.1 New Features and Fixes](http://www.libreoffice.org/download/4-1-new-features-and-fixes/) for more details ...

(13-10-64-bit-arm-architecture)=
### 64-bit ARM architecture

Ubuntu 13.10 includes a new port to 64-bit ARM systems (the "arm64" architecture, also known as AArch64 or ARMv8) as a developer preview.  This is an incomplete port which we expect to develop further in the future, but it is useful today for development work and for experimenting with server workloads.  The Ubuntu Core arm64 image provides a root filesystem which may be booted in the [ARMv8 Foundation Model](http://www.arm.com/products/tools/models/fast-models/foundation-model.php), with the addition of a kernel (not provided in Ubuntu 13.10).

Due to time constraints, only a subset of the Ubuntu archive has been built for arm64; compared to armhf, 94% of the binary packages in the "main" component are available, and 69% of the binary packages in the archive as a whole.  We expect this to be much more complete for Ubuntu 14.04.


(13-10-ubuntu)=
### Ubuntu


(13-10-upstart-user-sessions)=
#### Upstart User Sessions

This Ubuntu release includes Upstart User Sessions by default, allowing Upstart to supervise a user's desktop session.

To see details of the running Upstart session, either `echo $UPSTART_SESSION` to see the D-Bus address the Session Init process is listening to, or run the following command which lists the process id of the Upstart session along with the value of `$UPSTART_SESSION`:

```none
$ initctl list-sessions
```

The normal suite of Upstart commands is available (such as `initctl`, `start`, and `stop`). For example, to list all session jobs, run:

```none
$ initctl list
```

To list _system_ jobs from within a user session, run one of the following two commands:

```none
$ initctl --system list
$ sudo initctl list
```

Session jobs are read from `/usr/share/upstart/sessions/` and `$XDG_CONFIG_HOME/upstart/` (or `$HOME/.config/upstart` if `$XDG_CONFIG_HOME` is not set).

Session job output is logged to `$XDG_CACHE_HOME/upstart/` (or `$HOME/.cache/upstart/` if `$XDG_CACHE_HOME` is not set).

See `init(5)` for full details.


(13-10-ubuntu-server)=
### Ubuntu Server


(13-10-openstack-2013-2-havana)=
#### OpenStack 2013.2 (Havana)

Ubuntu 13.10 includes the 2013.2 Havana release of OpenStack. OpenStack projects supported in 13.10 include: Nova, Glance, Swift, Keystone, Horizon, Cinder, Neutron and Ceilometer. Heat is also included in 13.10 in Ubuntu Universe.

Please note that Quantum (OpenStack Networking) has changed name to Neutron; package updates will install the required transitions - however configuration files under /etc/quantum must be manually transitioned to /etc/neutron with appropriate configuration review and updates.

OpenStack Havana is also available for Ubuntu Server 12.04 LTS in the [Ubuntu Cloud Archive](https://wiki.ubuntu.com/ServerTeam/CloudArchive).


(13-10-juju-1-16-0)=
#### Juju 1.16.0

Ubuntu 13.10 includes the 1.16.0 release of [Juju](http://juju.ubuntu.com).  This includes the following new features:

* Over 130 services ready to deploy on supported clouds; including support for [Node.js](https://juju.ubuntu.com/docs/howto-node.html) and [Rails](https://juju.ubuntu.com/docs/howto-rails.html) workflows.

* Support for AWS, HP Cloud, Azure, OpenStack, MAAS, and local deployments.

* New [graphical user interface](https://jujucharms.com/) that is deployable into any supported cloud.

* Entirely [new documentation](https://juju.ubuntu.com/docs/getting-started.html).

* MAAS LXC managed containers

* Ability to [deploy to specific machines](https://juju.ubuntu.com/docs/charms-deploying.html).

* [Mac and Windows clients](https://juju.ubuntu.com/install/) for users of alternative operating systems as clients but need to deploy to Ubuntu Server.

Currently its not possible to transition an environment built using Juju 0.7 to 1.16.0; for backwards compatibility, Juju 0.7 has been retained in the archive for 13.10.

You can revert to Juju 0.7 client tools by using the following:

```none
sudo update-alternatives --set juju /usr/lib/juju-0.7/bin/juju
```

or switch back to the new 1.16.0 release using:

```none
sudo update-alternatives --set juju /usr/lib/juju-1.16.0/bin/juju
```

See the [Juju documentation](http://juju.ubuntu.com/docs) for full details.

Juju 1.16.0 is also available for Ubuntu Server 12.04 LTS in the [Ubuntu Cloud Tools Archive](https://wiki.ubuntu.com/ServerTeam/CloudToolsArchive).


(13-10-maas-1-4)=
#### MAAS 1.4

Ubuntu 13.10 includes the latest MAAS release (1.4). This new upstream release includes various bug fixes and improvements. New features include:

* Network discovery during server commissioning using LLDP.

* Faster installations using the Curtin installer (a new alternative to the Debian Installer).

* Extensible templates for DHCP, power control, PXE and DNS under /etc/maas/templates.

* Support in the maas-cli for managing SSH keys and API credentials.

* Support for HP Moonshot systems (users will need to provide iLO credentials for power management manually).

For more information about the new features and bug fixes, please review the [MAAS ChangeLog](http://maas.ubuntu.com/docs/changelog.html).

MAAS 1.4 is also available for Ubuntu Server 12.04 LTS in the [Ubuntu Cloud Tools Archive](https://wiki.ubuntu.com/ServerTeam/CloudToolsArchive).


(13-10-lxc-1-0-alpha1)=
#### LXC 1.0~alpha1

After many years of development, LXC has now been promoted to main and will benefit from the attention of the Ubuntu Security team.

Ubuntu 13.10 includes LXC 1.0~alpha1 which is the first upstream snapshot of what will be the Ubuntu 14.04 LTS version of LXC. That version will come with 5 years of bug fixes and security updates provided by upstream LXC.

LXC 1.0~alpha1 provides the following new features:

* Improved API and language bindings.

* Flexible backing store system, container cloning and snapshot support.

* A more coherent set of of tools to control LXC containers.

* Improvements to the various LXC templates.  The ubuntu-cloud template now utilizes LXC's clone-hooks to allow user-data to be passed at clone time rather than create.

* Support for Android as both a host and container.

* Initial support for unprivileged containers.

More on [LXC's new website](http://linuxcontainers.org) or in the [Ubuntu Server guide](https://help.ubuntu.com/13.10/serverguide/lxc.html).


(13-10-virtualization)=
#### Virtualization

Ubuntu 13.10 includes Qemu 1.5.0 and libvirt 1.1.1.

Qemu 1.5.0 and libvirt 1.1.1 are also available for Ubuntu Server 12.04 LTS as part of the [Ubuntu Cloud Archive](https://wiki.ubuntu.com/ServerTeam/CloudArchive) for OpenStack Havana.


(13-10-apache-2-4-and-php-5-5)=
#### Apache 2.4 and PHP 5.5

Ubuntu 13.10 includes Apache 2.4 and PHP 5.5. Users of these packages should review their configuration prior to upgrade to ensure compatibility with Apache 2.4 directives and the new tooling and directory structure for managing configuration snippets in the Ubuntu packages.

For more details refer to the Apache 2.4 [upgrade guide](http://httpd.apache.org/docs/2.4/upgrading.html) and the PHP 5.5 [migration guide](http://php.net/manual/en/migration55.changes.php).


(13-10-ceph-0-67-4)=
#### Ceph 0.67.4

Ubuntu 13.10 includes the latest Ceph Dumpling LTS release (0.67.4), providing improved performance and efficiency and block device encryption.

For full details on upgrading please see the Ceph [release notes](http://ceph.com/docs/master/release-notes/#v0-67-4-dumpling).

Ceph Dumpling is also available for Ubuntu Server 12.04 LTS as part of the [Ubuntu Cloud Archive](https://wiki.ubuntu.com/ServerTeam/CloudArchive) for OpenStack Havana.


(13-10-open-vswitch-1-10-2)=
#### Open vSwitch 1.10.2

Ubuntu 13.10 includes Open vSwitch 1.10.2 with support for VXLAN overlay networks.

The Open vSwitch switch daemons are now controlled using Upstart configurations to allow Open vSwitch to be used early in the boot process; the 'force-reload-kmod' command from openvswitch-switch init script has been replaced with a new Upstart configuration 'openvswitch-force-reload-kmod' which can be used to force a full reload of the Open vSwitch kernel module and daemons:

```none
sudo start openvswitch-force-reload-kmod
```

As of this release, the bridge compatibility module has been removed - users must migrate to using the native Open vSwitch integration for Ubuntu network scripts - see the package [README](http://bazaar.launchpad.net/~ubuntu-branches/ubuntu/saucy/openvswitch/saucy/view/head:/debian/openvswitch-switch.README.Debian) for more details.

Open vSwitch 1.10.2 is also available for Ubuntu Server 12.04 LTS as part of the [Ubuntu Cloud Archive](https://wiki.ubuntu.com/ServerTeam/CloudArchive) for OpenStack Havana.


(13-10-cloud-init-0-7-3-and-cloud-images)=
#### Cloud-Init 0.7.3 and Cloud Images

Ubuntu 13.10 includes Cloud-Init 0.7.3, providing the following new features:

* Support for provisioning with user-data support on Microsoft Azure, Joyent Cloud (SmartOS) and OpenNebula

* Support for merging multipart cloud-config input via [JSONP](http://en.wikipedia.org/wiki/JSONP)

* Support for partitioning and creating filesystems ephemeral disks. Enabled by default for Microsoft Azure and Joyent Cloud (SmartOS)

Starting with 13.10, Joyent Cloud (SmartOS) is a supported target for the Ubuntu Cloud Images. Images will be delivered shortly after release. Cloud-init support for SmartOS includes user-data and user-scripts via the 'smartdc' tools. Users are advised to base64 encode their user-data.

Cloud Images available on Windows Azure are now provisioned completely with cloud-init. Previously images were provisioned with cloud-init and walinuxagent. walinuxagent has had all provisioning functions disabled and cloud-init handles all provisioning functions.


(13-10-puppet-3)=
#### Puppet 3

Ubuntu 13.10 includes Puppet 3.  This is a major version upgrade from previous Ubuntu releases and includes many changes which are not compatible with Puppet 2.7.x.

Please review the upstream [release notes](http://docs.puppetlabs.com/puppet/3/reference/release_notes.html#upgrade-warning-many-breaking-changes) to determine which breaking changes apply to your installation.


(13-10-ubuntu-for-phones)=
### Ubuntu for Phones

13.10 represents a major step forward for the Ubuntu project, because it features the first image to support phones. Furthermore, the Ubuntu phone images feature a set of new technologies that solve many of the longstanding difficulties with Ubuntu distros. Specifically:

* Image based updates

* A complete SDK

* Application Isolation

* Click packages and click installer with app store

* Mir Display Server and Window Manager

* Unity 8
For 13.10, Ubuntu primarily supports the Galaxy Nexus and Nexus 4 phones, though there are images available for other phones and tablets.


(13-10-kubuntu)=
### Kubuntu

Further notes about this release of Kubuntu can be found at:
[kubuntu.org/news/kubuntu-13.10](http://kubuntu.org/news/kubuntu-13.10)


(13-10-xubuntu)=
### Xubuntu

Further notes about this release of Xubuntu can be found at:
[wiki.ubuntu.com/SaucySalamander/ReleaseNotes/Xubuntu](https://wiki.ubuntu.com/SaucySalamander/ReleaseNotes/Xubuntu)


(13-10-edubuntu)=
### Edubuntu

Further notes about this release of Edubuntu can be found at:
[wiki.ubuntu.com/SaucySalamander/ReleaseNotes/Edubuntu](https://wiki.ubuntu.com/SaucySalamander/ReleaseNotes/Edubuntu)


(13-10-lubuntu)=
### Lubuntu

Further notes about this release of Lubuntu can be found at:
[wiki.ubuntu.com/SaucySalamander/ReleaseNotes/Lubuntu](https://wiki.ubuntu.com/SaucySalamander/ReleaseNotes/Lubuntu)


(13-10-ubuntu-studio)=
### Ubuntu Studio

Further notes about this release of Ubuntu Studio can be found at:
[wiki.ubuntu.com/SaucySalamander/ReleaseNotes/UbuntuStudio](https://wiki.ubuntu.com/SaucySalamander/ReleaseNotes/UbuntuStudio)


(13-10-ubuntukylin)=
### UbuntuKylin

Further notes about this release of UbuntuKylin can be found at:
[wiki.ubuntu.com/UbuntuKylin/1310-ReleaseNotes](https://wiki.ubuntu.com/UbuntuKylin/1310-ReleaseNotes)


(13-10-ubuntu-gnome)=
### Ubuntu GNOME

Please have a read at: [Ubuntu GNOME Release Notes](https://wiki.ubuntu.com/SaucySalamander/ReleaseNotes/UbuntuGNOME).




(13-10-known-issues)=
## Known issues

As is to be expected, at this stage of the release process, there are some significant known bugs that users may run into with this release of Ubuntu 13.10.  The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:


(13-10-boot-installation-and-post-install)=
### Boot, installation and post-install

* When deleting and recreating partitions in manual partitioning where the disk has many partitions the installer may hang when attempting to mark the partition to be formatted. Resetting and restarting the install will allow the installation to be completed.  (Bug:1240794)

* The desktop image installer cannot unlock existing encrypted (LUKS) volumes.  If you need to make use of existing encrypted volumes during partitioning, then use the "Try Ubuntu without installing" boot option to start a live session, open the encrypted volumes (for example, by clicking on their icons in the Unity launcher), enter your password when prompted to unlock them, close them again, and run `ubiquity` to start the installer.  (Bug:1066480)

* When using installer to upgrade or reinstall an existing installation with encrypted swap, the installer may fail to reuse the partition. A warning will be shown, however the installation can be completed. The installed system will not have swap activated and users are advised to recreate swap on their systems. Please see advice about adding and activating swap at: [help.ubuntu.com/community/SwapFaq](https://help.ubuntu.com/community/SwapFaq) (Bug:1172002)

* Installs on very small memory systems may fail to start or exit without completing with no error. It is recommended that swap be created before install for such systems. Please see advice about adding and activating swap at: [help.ubuntu.com/community/SwapFaq](https://help.ubuntu.com/community/SwapFaq) (Bug:1172161)

* In rare circumstances the 'Next' button on the installer 'Install Type' screen is non-functional.  This is intermittent and may be resolved by hitting 'Back' and retrying.  (Bug:1172572)

* In Microsoft Hyper-V Server 2008 R2 error in video driver. (Bug:1199345)

* In Windows Virtual PC can't boot 64-bit ISO. (Bug:1228086)


(13-10-migration)=
### Migration


(13-10-graphics-and-display)=
### Graphics and Display


(13-10-networking)=
### Networking

* When connecting to MPA2/PEAP/MSCHAPv2 wifi networks which do not have a CA Certificate network manager may incorrectly mark the CA certificate as needing verification and fail that verification. See the bug for workarounds.  (Bug:1104476)


(13-10-desktop)=
### Desktop

* Tab support has been removed from webapps as part of a transitional effort to run webapps in a standalone webapps container, instead of inside your existing browser window. (Bug:1230382)

* Gmail integration: message counters and labels support require an update to unity-webapps-gmail, which is available in a PPA: [launchpad.net/~webapps/+archive/staging](https://launchpad.net/~webapps/+archive/staging) (see Bug:1069576). The fix will be part of the next SRU batch.

* Sometimes ability to swith keyboard layout in X is lost. (Bug:1215826, Bug:1218322) One of possible workarounds is to remove indicator-keyboard package, kill corresponding process and configure layout usning `setxkbmap`. Also, hotkeys are broken in non-latin layouts (Bug:1226962).


(13-10-kernel)=
### Kernel


(13-10-ubuntu-for-phones-2)=
### Ubuntu for phones


(13-10-application-confinement)=
#### Application Confinement

An important part of Ubuntu for phones is running 3rd party software in a safe manner, and a lot of work in support of [ApplicationConfinement](https://wiki.ubuntu.com/SecurityTeam/Specifications/ApplicationConfinement) was completed. Specifically, when applications are installed on Ubuntu for phones via the Ubuntu appstore, they are installed using [click packaging and run under AppArmor](http://developer.ubuntu.com/publish/apps/security-policy-for-click-packages/). While a very meaningful level of isolation between apps is achieved in Ubuntu 13.10 for Ubuntu for phones, the work is not completed and will continue in 14.04. Specifically:

* Mir does not currently support a method for another process to display a confirmation dialog over the current foreground app (Bug:1224756). As such, users are not prompted for the following common services:

* location-service (GPS, Bug:1219164)

* pulseaudio recording (Bug:1224756)

* video recording (Bug:1230366)
 Other services like online accounts, calendar and contacts are also affected, but access to these services is reserved for applications on a case-by-case basis in 13.10

* AppStore apps with access to the audio policy group may trigger loading of pulseaudio system modules (Bug:1211380)

* Several shared memory files are not application-specific (Bug:1197060, Bug:1226569, Bug:1224751)

* Android services accessed via binder are not properly mediated (ie, apps are able to access the sensors and camera service when policy doesn't explicitly allow it, Bug:1197134)

* AppArmor mediation for [signals, ptrace, abstract sockets and some other forms of IPC](https://blueprints.launchpad.net/ubuntu/+spec/appdev-s-appisolation-signals-ipc-ptrace) for processes with the same UID is not yet implemented

* AppArmor mediation for process-specific files in /proc in not implemented which discloses more information to apps than is required

* AppArmor mediation of the environment is not implemented. Ubuntu 13.10 for phones AppArmor policy makes up for this by disallowing execution of less-restricted processes

* X is not mediated (ie, keyboard/mouse sniffing, drag and drop, screen grabs, xsettings module loading). This is not a problem for Ubuntu for phones since it uses Mir, but is listed for people wanting to use Ubuntu appstore apps on X (eg, Ubuntu Desktop)

* The YAMA kernel LSM is not available for Galaxy Nexus (maguro) and Nexus 7 (grouper) and not enabled on Nexus 4 (mako) and Nexus 10 (manta). As a result, kernel protections such as ptrace and link restrictions are not present.


(13-10-browser)=
#### Browser

* No support for hardware rendering when doing HTML5 video streaming playback (poor performance, due extra buffer copy)

* Replaying video crashes browser (Bug:1236599)

* Scrolling in webpages is very jumpy on maguro (Bug:1240881)


(13-10-calendar)=
#### Calendar

* Events can be added, but not edited (Bug:1240809)
* Reminder functionality is not implemented (Bug:1240539)


(13-10-camera)=
#### Camera

* Still photos only, no video recording


(13-10-clock)=
#### Clock

* Alarms functionality not completely implemented (cannot save, no notification)

* No detection of time zone change via settings. To detect the change, you’ll need to restart the app

* Location detection is not done by GPS but by geoip, which might provide not so accurate results


(13-10-dropping-letters)=
#### Dropping Letters

* No audio (music & effects) during game (Bug:1196865)


(13-10-language-and-shell)=
#### Language and shell

* After changing the system language, you need to reboot to get the shell picking your change (Bug:1240875)

* Keyboard does not allow input on the left handside in landscape mode (Bug:1236489)


(13-10-location)=
#### Location

* Devices take a long time to get a GPS satellite lock - no AGPS/SUPL support


(13-10-media-player)=
#### Media Player

* Software decode and rendering is currently not supported (Bug:1234722)
* Playing multiple videos in two different media players not supported
* Flickering video playback on maguro
* Replaying video crashes app (Bug:1236599)


(13-10-media-scanner)=
#### Media Scanner

* Maguro: incorrect color conversion when producing thumbnails (Bug:240264)
* Copying large files over mtp causes mediascanner to consume CPU.


(13-10-mir)=
#### Mir

* Unity8 display flickers and stop responding on grouper (Bug:1238695)

* Not supported on Manta (Nexus 10) (Bug:1203268)

* Setting a wallpaper from a taken photo produces black background on maguro (Bug:1227783)


(13-10-sdk-qt-creator)=
#### SDK - Qt Creator

* Screenshot from phone not working (Bug:1238839)


(13-10-telephony)=
#### Telephony

* No vibration on ring or sms


(13-10-shorts)=
#### Shorts

* Links in articles are not clickable (Bug:1217297). As a workaround, articles can easily be opened with the browser using the toolbar action in the single article view.


(13-10-software-store)=
#### Software Store

* Ratings and reviews are not yet implemented.
* Apps with “Architecture: all” are not visible on devices. (Bug:1239662)


(13-10-weather)=
#### Weather

* Location detection is not done by GPS but by geoip, which might provide not so accurate results


(13-10-platform)=
#### Platform

* Session upstart leaks memory on Ubuntu Touch (Bug:1235649)

* On maguro omapfb spams the system with uevents from the graphics driver (Bug:1234743)


(13-10-ubuntu-server-2)=
### Ubuntu Server


(13-10-maas)=
#### MAAS

* MAAS Server install fails without a network connection during install of maas-region-controller (Bug:1172566)

* Need to use generic kernel for highbank on ARM (Bug:1166994)

* Need to use generic-lpae kernel for midway on ARM  (Bug:1240183)


(13-10-openstack)=
#### OpenStack

* Neutron services need re-scheduling to renamed agents post upgrade from Grizzly (Bug:1236439)


(13-10-ubuntu-core)=
### Ubuntu Core



(13-10-kubuntu-2)=
### Kubuntu

* Network management crash on upgrade (Bug:1231360)

* USB installation media fails to boot if created with persistence enabled (Bug:1239833)


(13-10-xubuntu-2)=
### Xubuntu



(13-10-lubuntu-2)=
### Lubuntu



(13-10-ubuntu-studio-2)=
### Ubuntu Studio

##



(13-10-ubuntukylin-2)=
### UbuntuKylin


---

**For a listing of more known issues, please refer to the Saucy Salamander [bug tracker](https://bugs.launchpad.net/ubuntu/saucy/+bugs) in Launchpad.**


(13-10-reporting-bugs)=
## Reporting bugs

Your comments, bug reports, patches and suggestions will help fix bugs and improve the quality of future releases. Please [report bugs using the tools provided](http://help.ubuntu.com/community/ReportingBugs).

If you want to help out with bugs, the [Bug Squad](http://wiki.ubuntu.com/BugSquad) is always looking for help.


(13-10-participate-in-ubuntu)=
## Participate in Ubuntu


If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

[www.ubuntu.com/community/get-involved](http://www.ubuntu.com/community/get-involved)


(13-10-more-information)=
## More information

You can find out more about Ubuntu on the [Ubuntu website](http://www.ubuntu.com) and [Ubuntu wiki](http://wiki.ubuntu.com).

To sign up for future Ubuntu development announcements, please subscribe to Ubuntu's development announcement list at:

[lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce](http://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce)
