---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/RaringRingtail/ReleaseNotes -->

(ubuntu-13-04-release-notes)=
# Ubuntu 13.04 release notes

(13-04-introduction)=
## Introduction

The Ubuntu developers are moving quickly to bring you the absolute latest and greatest software the Open Source community has to offer. The Ubuntu 13.04 Release is the next version of Ubuntu.


(get-ubuntu-13-04)=
## Get Ubuntu 13.04


(13-04-upgrading-from-ubuntu-12-10)=
### Upgrading from Ubuntu 12.10

To upgrade from Ubuntu 12.10 on a desktop system:

* Open Software Sources.

* Press Alt+F2 and type in "update-manager" (without the quotes) into the command box.

* Update Manager should open up and tell you: New distribution release '13.04' is available.

* Click Upgrade and follow the on-screen instructions.

To upgrade from Ubuntu 12.10 on a server system:

* Install the `update-manager-core` package if it is not already installed.

* Launch the upgrade tool with the command `sudo do-release-upgrade`.

* Follow the on-screen instructions.
Note that the server upgrade will use GNU screen and automatically re-attach in case of e.g. dropped connection problems.

Offline upgrade options via alternate CDs are no longer offered for Ubuntu Desktop and Ubuntu Server. Please ensure you have network connectivity to one of the official mirrors or to a locally accessible mirror and follow the instructions above.


(13-04-upgrading-from-other-releases)=
### Upgrading from other releases

Users of other Ubuntu releases need to upgrade first to 12.10, and then to 13.04.

For further information on upgrading to 12.10, please see its [upgrade instructions](https://help.ubuntu.com/community/QuantalUpgrades).


(13-04-ubuntu-downloader-for-windows-discontinued)=
### Ubuntu downloader for Windows discontinued

Due to various bugs in Wubi that have not been addressed in time for the final release, the Ubuntu team will not be releasing the Wubi installer with 13.04.  You can read more about this decision [here](https://lists.ubuntu.com/archives/ubuntu-devel/2013-April/036993.html).  Users who wish to try out Ubuntu without repartitioning a Windows system are encouraged to use a live system instead, booted from either a DVD or a USB disk.


(13-04-support-lifespan-reduced)=
### Support lifespan reduced

Ubuntu 13.04 will only be supported for 9 months. Previous non-LTS releases were supported for 18 months. For more information, please read the announcements [here](http://fridge.ubuntu.com/2013/03/19/changes-in-ubuntu-releases-decided-by-the-ubuntu-technical-board/) or [here](http://fridge.ubuntu.com/2013/03/19/ubuntu-technical-board-looks-at-shuttleworths-proposal-for-release-management-methodology/).


(download-ubuntu-13-04)=
### Download Ubuntu 13.04

13.04 images can be downloaded from a location near you.
##
**Note:** The Ubuntu Desktop images are now bigger than a standard CD, and you should use a USB or DVD for installation.

You can download 13.04 ISOs from:

[releases.ubuntu.com/13.04/](http://releases.ubuntu.com/13.04/) (Ubuntu Desktop and Server)

[cloud-images.ubuntu.com/releases/13.04/release/](http://cloud-images.ubuntu.com/releases/13.04/release/) (Ubuntu Cloud Server)

[cdimage.ubuntu.com/netboot/13.04/](http://cdimage.ubuntu.com/netboot/13.04/) (Ubuntu Netboot)

[cdimage.ubuntu.com/ubuntu-core/releases/13.04/release/](http://cdimage.ubuntu.com/ubuntu-core/releases/13.04/release/) (Ubuntu Core)

[cdimage.ubuntu.com/edubuntu/releases/13.04/release/](http://cdimage.ubuntu.com/edubuntu/releases/13.04/release/) (Edubuntu DVD)

[cdimage.ubuntu.com/kubuntu/releases/13.04/release/](http://cdimage.ubuntu.com/kubuntu/releases/13.04/release/) (Kubuntu)

[cdimage.ubuntu.com/lubuntu/releases/13.04/release/](http://cdimage.ubuntu.com/lubuntu/releases/13.04/release/) (Lubuntu)

[cdimage.ubuntu.com/ubuntustudio/releases/13.04/release/](http://cdimage.ubuntu.com/ubuntustudio/releases/13.04/release/) (Ubuntu Studio)

[cdimage.ubuntu.com/ubuntu-gnome/releases/13.04/release/](http://cdimage.ubuntu.com/ubuntu-gnome/releases/13.04/release/) (Ubuntu-GNOME)

[cdimage.ubuntu.com/ubuntukylin/releases/13.04/release/](http://cdimage.ubuntu.com/ubuntukylin/releases/13.04/release/) (UbuntuKylin)

[cdimage.ubuntu.com/xubuntu/releases/13.04/release/](http://cdimage.ubuntu.com/xubuntu/releases/13.04/release/) (Xubuntu)

##[cdimage.ubuntu.com/kubuntu-active/releases/13.04/release/](http://cdimage.ubuntu.com/kubuntu-active/releases/13.04/release/) (Kubuntu Active)


(new-features-in-13-04)=
## New features in 13.04

Please see the [Raring blueprint list](https://blueprints.launchpad.net/ubuntu/raring/+specs) for details.

Please test and report any bugs you find:

[help.ubuntu.com/community/ReportingBugs](http://help.ubuntu.com/community/ReportingBugs)


(13-04-updated-packages)=
### Updated Packages

As with every new release, packages--applications and software of all kinds--are being updated at a rapid pace. Many of these packages came from an automatic sync from [Debian](http://www.debian.org)'s unstable branch; others have been explicitly pulled in for 13.04 Raring Ringtail.

For a list of all packages being accepted for 13.04 Raring Ringtail, please subscribe to [raring-changes](https://lists.ubuntu.com/mailman/listinfo/raring-changes).


(13-04-linux-kernel-3-8-8)=
#### Linux kernel 3.8.8

Ubuntu 13.04 includes the [3.8.0-19.29 Ubuntu Linux kernel](https://launchpad.net/ubuntu/+source/linux/3.8.0-19.29) which was based on the [v3.8.8 upstream Linux kernel](http://www.kernel.org/pub/linux/kernel/v3.x/linux-3.8.8.tar.bz2).


(13-04-unity-7)=
#### Unity 7

Unity 7 brings a lot of performance improvements, reduced memory consumption and a great number of small UI fixes to bring a better overall shell experience. Those are like being typo-tolerant in the dash when searching for an application, using the mouse scroll wheel on a launcher icon to switch between applications or better available third party devices handling. You will notice as well some new icons themes to continue on lead of bringing design as the central Ubuntu experience.

You will notice that only one workspace is available by default on any new installation. If you want to bring back workspaces, you can find an option in the Appearance panel of System Settings under the Behavior tab. You can as well enable "Show desktop" button on the Launcher.


(13-04-upstart-1-8)=
#### Upstart 1.8

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


(13-04-libreoffice-4-0)=
#### LibreOffice 4.0

for all details, see: [wiki.documentfoundation.org/ReleaseNotes/4.0](https://wiki.documentfoundation.org/ReleaseNotes/4.0)


(13-04-core)=
##### Core

* New Widget layout technique for dialog windows introduced

* Support for Firefox Personas in LibreOffice

* Document Management Systems Integration for Alfresco, Nuxeo, SharePoint via libcmis

* Less Java dependencies: e.g. more Wizards available even in the default install

* moved completely from Python 2.6 to Python 3.3 internally

* PDF Import, the Presenter Console, and the Python Scripting Provider are core features now

* **dropping legacy binfilter and a lot of obsolete UNO-API interfaces**


(13-04-writer)=
##### Writer

* The "Apply Style" combo box in the toolbar now features previews of the styles to choose.

* Import ink annotations from DOCX and RTF documents

* Import / export support for native RTF math expressions


(13-04-calc)=
##### Calc

* Various performance improvements of ODS document import
* Increased size limit on (uncompressed) ODF documents from 2Gb to 4Gb
* XML Source dialog to quickly import arbitrary XML content


(13-04-impress-draw)=
##### Impress/Draw

* **Impress Remote control** for controling presentations via Bluetooth/Wifi from a Smartphone

* Import for MS Publisher files

* Import for _all_ Visio file formats, even MS Office 2013

* various PPTX import fixes

* hyperlinks/fields wrapping

* RTL support for the Presenter Console


(13-04-base)=
##### Base

* Native support (mork driver) for accessing Thunderbird address books


(13-04-cups-1-6-2-and-cups-filters-1-0-34)=
#### CUPS 1.6.2 and cups-filters 1.0.34

We had already switched to CUPS 1.6.x in Quantal (12.10) but had to apply a huge, awkward Ubuntu-specific patch to avoid regressions. Now we are up to all new standards without needing to do anything Ubuntu-specific.

Most important change here is the way how network printing works. Formerly, a CUPS-specific mechanism was used. The server broadcasted information about the printers it shares and the clients listen to these broadcasts making the printers available on the client side, looking like local print queues for the applications.

Recently, the [Printer Working Group (PWG)](http://www.pwg.org/), an association of printer and software industry for developing standards related to digital printing, has created a standard for broadcasting information about shared printers. This standard is broadcasting the information via Bonjour, a protocol also used for many other network services, like shared files systems, screens, music/video servers, ...

CUPS has adopted this standard in 1.6.x, but only broadcasts and does not listen to broadcasts of CUPS daemons (or generally print servers using Bonjour) on other machines, letting remote printers not automatically get available locally. CUPS also dropped the old broadcasting protocol without transition period.

To overcome the problems and keeping network printing as easy as before (this is why 10 years ago the distros switched to CUPS) the cups-filters project of OpenPrinting introduced cups-browsed, an extra daemon which by default listens to Bonjour broadcasts of remote CUPS daemons (of IPP printers coming soon) and automatically creates local print queues pointing to the shared printers making pure CUPS 1.6.x networks working out-of-the-box.

If your network still contains machines running CUPS 1.5.x and older, cups-browsed also has legacy support for the old CUPS broadcasting, browsing (listening), and BrowsePoll. Please see the comments in /etc/cups/cups-browsed.conf, edit the file appropriately, and restart cups-browsed ("sudo restart cups-browsed") or reboot. When upgrading to Raring, BrowsePoll directives are overtaken from CUPS to cups-browsed automatically.

For everyone developing embedded or mobile systems based on Ubuntu, the CUPS package is split up into more binary packages to get a minimum client-only printing stack, of the packages cups-daemon, libcups2, and cups-browsed, occupying only ~1 MB. This only listens for Bonjour broadcasts (legacy CUPS broadcasts and BrowsePoll optional) of remote CUPS servers and makes the printers available locally. No drivers and filters for locally connected printers are available then.

Another thing to mention which was available before but never told about in release notes: When sharing local printers they are automatically available also for Apple's iOS devices (iPhone, iPad, iPod touch).


(13-04-python-3-3)=
#### Python 3.3

We eventually intend to ship only [Python 3](http://docs.python.org/py3k/whatsnew/3.0.html) with the Ubuntu desktop image, not Python 2.  The Ubuntu 13.04 image continues this process, although we will not be able to convert everything to Python 3 for Ubuntu 13.04 final image.

If you have your own programs based on Python 2, fear not!  Python 2 will continue to be available (as the `python` package) for the foreseeable future.  However, to best support future versions of Ubuntu you should consider porting your code to Python 3.  [Python/3](https://help.ubuntu.com/community/Python/3) has some advice and resources on this.


(13-04-general)=
### General

Automatic Apport crash reporting has been enabled by default again to catch problems early on. It now [checks for duplicates on the client side](http://www.piware.de/2011/11/apport-1-90-client-side-duplicate-checking/), which will avoid uploading debug data and creating Launchpad bug reports unnecessarily in many cases now.


(13-04-software-updater)=
#### Software Updater

Software Updater in 13.04 has a simplified details panel that most prominently shows applications and manually-installed packages.  Libraries and packages that belong to the base system are collected under a single item.


(13-04-ubuntu)=
### Ubuntu


(13-04-upstart-user-sessions-technology-preview)=
#### Upstart User Sessions (technology preview)

This Ubuntu release includes a "tech preview" of Upstart User Sessions, which allow Upstart to supervise a user's desktop session. This feature is disabled by default for Ubuntu 13.04, but can be manually enabled for testing.

To enable Upstart User Sessions for all users:

1. Uncomment "`ubuntu`" in file `/etc/upstart-xsessions`.
1. Logout of any desktop sessions.
1. Login to the default Unity session.

To disable, simply comment out "`ubuntu`", logout and log back in again.

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


(13-04-friends)=
#### Friends

Social networking for 13.04 is now handled by the Friends service, which replaces the backend Gwibber provided in previous Ubuntu releases.  There is no transition required, if you have social networking accounts setup in Ubuntu Online Accounts, the Friends service will just work.  The Gwibber lens in Unity has been replaced with a Friends lens and works in much the same way.  The Gwibber client application is no longer included by default, for similar functionality friends-app can be installed from Software Center.


(13-04-ubuntu-server)=
### Ubuntu Server


(13-04-openstack-grizzly)=
#### OpenStack Grizzly

Ubuntu 13.04 includes the Grizzly release of Openstack. OpenStack projects supported in 13.04 include: Nova, Glance, Swift, Keystone, Horizon, Cinder and Quantum. Ceilometer is also included in 13.04 in Ubuntu Universe.

Openstack Grizzly is also available for Ubuntu Server 12.04 LTS in the [Ubuntu Cloud Archive](https://wiki.ubuntu.com/ServerTeam/CloudArchive).

OpenStack continues to be deployable using Juju Charms; for the Grizzly release this also includes deploying OpenStack in a highly avaliable configuration as demonstrated at the OpenStack Summit in Portland. See the [OpenStack HA Reference architecture](https://wiki.ubuntu.com/ServerTeam/OpenStackHA) documentation for more details.


(13-04-juju)=
#### Juju

Ubuntu 13.04 includes the 0.7 release of Python Juju ('juju' package).

The initial release (1.10.0) of the Go rewrite of Juju ('juju-core' package) is available in the -backports repository, this package is co-installable with the 0.7 version.

You can revert to the default (0.7) version by using the following:

```none
$ sudo update-alternatives --set juju /usr/lib/juju-0.7/bin/juju
```

or to the new 1.10.0 release using:

```none
$ sudo update-alternatives --set juju /usr/lib/juju-1.10.0/bin/juju
```

Please note that the 1.10.0 (Go version) release is not yet end-user feature complete compared to 0.7 - for example, the LXC local provider is not yet implemented in 1.10.0; if you install both you will get 0.7 by default.

See the [Juju documentation](http://juju.ubuntu.com/docs) for full details of these changes.


(13-04-maas)=
#### MAAS

Ubuntu 13.04 includes the latest MAAS release (1.3). This new upstream release includes various bug fixes and improvements in comparison to older MAAS releases. New features include:

* Customizable kernel command lines for each node via tags.
* Installation path for Image Based Installations.
* Improved IPMI detection, with support most recent iLO versions.
* Support for Multiple Juju Environments (one per MAAS user).


(13-04-simple-streams)=
#### Simple Streams

There is now machine formated JSON data describing all downloadable content for Ubuntu cloud images.  The data format is called "simple streams", and can be found at [cloud-images.ubuntu.com/releases/streams/](http://cloud-images.ubuntu.com/releases/streams/) . There is a sample client included in Ubuntu in the 'simplestreams' package.  The client can be used to keep cloud or local downloads in sync with what is available from Ubuntu.


(13-04-ceph-0-56-4)=
#### Ceph 0.56.4

Ubuntu 13.04 includes the latest Ceph Bobtail LTS release (0.56.4). OpenStack Keystone integration has been implemented in the RADOS Gateway for this release, providing a drop-in replacement for Swift.

Ceph continues to be deployable using Juju Charms; notable changes include:

* Underlying default disk format for OSD's is now XFS; this can be changed using a configuration option in the ceph and ceph-osd charms.

* ceph-radosgw charm now supports the keystone integration implemented in bobtail.

For full details on upgrading please see the Ceph [release notes](http://ceph.com/docs/master/release-notes/#v0-56-4-bobtail).


(13-04-mongodb-2-2-4)=
#### MongoDB 2.2.4

Ubuntu 13.04 includes MongoDB 2.2.4; for this release SSL support has been enabled to support secured use of MongoDB (primarily to support Juju 2.0). The ARM support has also been improved during the 13.04 development cycle.

This release of MongoDB will also be provided as an official backport for 12.04 and 12.10.


(13-04-openvswitch-1-9-0)=
#### OpenvSwitch 1.9.0

Ubuntu 13.04 includes the latest stable release of OpenvSwitch 1.9.0, featuring full upstream support for Linux 3.8.  As of this release, the bridge compatibility module is officially deprecated - users should start planning to migrate away from this feature. For full details of this release please see the upstream [release notes](http://openvswitch.org/releases/NEWS-1.9.0).


(13-04-kubuntu)=
### Kubuntu


(13-04-xubuntu)=
### Xubuntu

Starting with 13.04, Xubuntu targets a 1GB USB. For more information about Xubuntu 13.04, read the [Xubuntu release announcement](http://xubuntu.org/news/13-04-release).


(13-04-edubuntu)=
### Edubuntu

* Ubiquity step indicator is inaccurate. As you progress through the installation steps, the total progress bar indicator at the bottom will either appear to be ahead or behind. [LP: #1172626](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1172626)


(13-04-lubuntu)=
### Lubuntu

Please read the [Release notes](https://wiki.ubuntu.com/RaringRingtail/ReleaseNotes/Lubuntu) for information.


(13-04-ubuntu-studio)=
### Ubuntu Studio

For information about the Ubuntu Studio Beta release, please see [RaringRingtail/UbuntuStudio](https://help.ubuntu.com/community/RaringRingtail/UbuntuStudio).


(13-04-ubuntukylin)=
### UbuntuKylin

[UbuntuKylin](https://help.ubuntu.com/community/UbuntuKylin) has had several bug fixes applied to chinese-calendar and
indicator-china-weather, made fcitx as default and improved the theme since
Beta 1. For information about the UbuntuKylin Beta release, please see [UbuntuKylin/1304-ReleaseNotes](https://help.ubuntu.com/community/UbuntuKylin/1304-ReleaseNotes).


(13-04-ubuntu-gnome)=
### Ubuntu GNOME

* In coordination with the Ubuntu Desktop Team, we have decided to stick with GNOME 3.6 for Ubuntu 13.04. For an overview of what's new in GNOME 3.6, please see the [Release Notes](https://help.gnome.org/misc/release-notes/3.6/).

* The [GNOME3 PPA](https://launchpad.net/~gnome3-team/+archive/gnome3/) offers an early look at GNOME 3.8 for Ubuntu. Please note that you need to do a dist-upgrade instead of a regular upgrade or else GDM or GNOME Shell won't run after upgrading. In case of problems, please make yourself familiar with ppa-purge before using the GNOME3 PPAs.

* There are some additional GNOME 3.8 apps in the [GNOME3 Staging PPA](https://launchpad.net/~gnome3-team/+archive/gnome3-staging/) but these apps have known bugs, some of which are serious or critical bugs.

* Default apps have changed since Ubuntu GNOME Remix 12.10.

* Firefox instead of GNOME Web (Epiphany)

* Ubuntu Software Center and Update Manager instead of GNOME Software (gnome-packagekit)

* LibreOffice instead of Abiword and Gnumeric

* The other apps are still available for install; they just aren't included in the default install.




(13-04-known-issues)=
## Known issues

As is to be expected, at this stage of the release process, there are some significant known bugs that users may run into with the Ubuntu 13.04 release.  The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:


(13-04-boot-installation-and-post-install)=
### Boot, installation and post-install

* When using installer to upgrade or reinstall an existing installation with encrypted swap, the installer may fail to reuse the partition. A warning will be shown, however the installation can be completed. The installed system will not have swap activated and users are advised to recreate swap on their systems. Please see advice about adding and activating swap at: [help.ubuntu.com/community/SwapFaq](https://help.ubuntu.com/community/SwapFaq) ([LP: #1172002](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1172002))

* Installs on very small memory systems may fail to start or exit without completing with no error. It is recommended that swap be created before install for such systems. Please see advice about adding and activating swap at: [help.ubuntu.com/community/SwapFaq](https://help.ubuntu.com/community/SwapFaq) ([LP: #1172161](https://bugs.launchpad.net/ubuntu-release-notes/+bug/1172161))

_ When using unattended reboots (preseeded), casper will still wait for ENTER to be preseed by the user. This can be worked around by calling "sed -i 's/eject -p -m._/&; ["$prompt"] || return 0/' /etc/init.d/casper" before rebooting the machine (as a late_command for example). ([LP: #1172653](https://bugs.launchpad.net/bugs/1172653))

* In rare circumstances the 'Next' button on the installer 'Install Type' screen is non-functional.  This is intermittent and may be resolved by hitting 'Back' and retrying.  ([LP: #1172572](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1172572))


(13-04-migration)=
### Migration


(13-04-graphics-and-display)=
### Graphics and Display


(13-04-desktop)=
### Desktop

* The official Google Chrome installer is built against libudev0 instead of the libudev1 available in Ubuntu 13.04. This should be fixed with Chrome 28 which is still in testing. We recommend that you install the open source chromium-browser from the Ubuntu Software Center until Google releases the fix for this issue. ([Google: #226002](https://code.google.com/p/chromium/issues/detail?id=226002))


(13-04-kernel)=
### Kernel

* There are reports of non-functional HDMI audio on various machines, even with proprietary drivers. In some cases analog built-in audio is affected too. Typically the the audio device does not show up in sound settings at all.  ([LP: #1169984](https://bugs.launchpad.net/bugs/1169984))


(13-04-ubuntu-server-2)=
### Ubuntu Server

* OpenStack Nova includes a new component, nova-conductor, which is used over RPC by nova-compute nodes instead of all compute nodes directly accessing the underlying nova database.  nova-conductor is typically deployed separately to nova-compute - this needs to be done manually during the upgrade process. [LP: #1168757](https://launchpad.net/bugs/1155327)


(13-04-maas-2)=
#### MAAS

* MAAS Server install fails without a network connection during install of maas-region-controller ([LP: #1172566](https://launchpad.net/bugs/1172566))





##




(13-04-ubuntu-gnome-2)=
### Ubuntu GNOME

* The "Install Alongside" option doesn't work (Bug:1164592).

* There are two Online Accounts entries in System Settings. One is the GNOME tool which you can use for Contacts, Documents, and Evolution. The other is Ubuntu's tool for Empathy, Gwibber, Shotwell, and if you install it, Unity. (Bug:1040193)

---

**For a listing of more known issues, please refer to the Raring Ringtail [bug tracker](https://bugs.launchpad.net/ubuntu/raring/+bugs) in Launchpad.**


(13-04-reporting-bugs)=
## Reporting bugs

It should come as no surprise that this release of Ubuntu 13.04 contains other bugs. Your comments, bug reports, patches and suggestions will help fix bugs and improve the quality of future releases. Please [report bugs using the tools provided](http://help.ubuntu.com/community/ReportingBugs).

If you want to help out with bugs, the [Bug Squad](http://wiki.ubuntu.com/BugSquad) is always looking for help.


(13-04-ubuntu-project-contributors)=
## Ubuntu Project Contributors

Ubuntu 13.04 would not be possible without the contributions of our
[developers](https://wiki.ubuntu.com/RaringRingtail/ReleaseNotes/Credits/Developers),
[testers](https://wiki.ubuntu.com/RaringRingtail/ReleaseNotes/Credits/Testers),
[release team members](https://wiki.ubuntu.com/RaringRingtail/ReleaseNotes/Credits/ReleaseTeam),
[documentation writers](https://wiki.ubuntu.com/RaringRingtail/ReleaseNotes/Credits/DocsTeam),
[translators](https://wiki.ubuntu.com/RaringRingtail/ReleaseNotes/Credits/Translators),
[bug analysts](https://wiki.ubuntu.com/RaringRingtail/ReleaseNotes/Credits/BugImprovers) and our
[users who take the time to file bugs](https://wiki.ubuntu.com/RaringRingtail/ReleaseNotes/Credits/BugReporters).
Ubuntu is based on [Debian](http://www.debian.org), [the Linux Kernel](http://www.kernel.org) and our many other excellent upstream projects.  Thank you!


(13-04-participate-in-ubuntu)=
## Participate in Ubuntu


If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

[www.ubuntu.com/community/get-involved](http://www.ubuntu.com/community/get-involved)


(13-04-more-information)=
## More information

You can find out more about Ubuntu on the [Ubuntu website](http://www.ubuntu.com) and [Ubuntu wiki](http://wiki.ubuntu.com).

To sign up for future Ubuntu development announcements, please subscribe to Ubuntu's development announcement list at:

[lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce](http://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce)
