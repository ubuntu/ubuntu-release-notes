---
tocdepth: 3
---

(ubuntu-13-04-release-notes)=
# Ubuntu 13.04 "Raring Ringtail" Release Notes

<!-- Source: https://wiki.ubuntu.com/RaringRingtail/ReleaseNotes -->

## When adding features to this page, please add credits for the relevant upstream developers where appropriate.
||<tablestyle="float:right; width:40%; background:#F1F1ED; margin: 0 0 1em 1em;" style="padding:0.5em;">'''Table of Contents'''<<BR>> <<TableOfContents>>||

= Introduction =

The Ubuntu developers are moving quickly to bring you the absolute latest and greatest software the Open Source community has to offer. The Ubuntu 13.04 Release is the next version of Ubuntu.

= Get Ubuntu 13.04 =
== Upgrading from Ubuntu 12.10 ==

To upgrade from Ubuntu 12.10 on a desktop system:
 * Open Software Sources.
 * Press Alt+F2 and type in "update-manager" (without the quotes) into the command box.
 * Update Manager should open up and tell you: New distribution release '13.04' is available.
 * Click Upgrade and follow the on-screen instructions.

To upgrade from Ubuntu 12.10 on a server system:
 * Install the {{{update-manager-core}}} package if it is not already installed.
 * Launch the upgrade tool with the command {{{sudo do-release-upgrade}}}.
 * Follow the on-screen instructions.
Note that the server upgrade will use GNU screen and automatically re-attach in case of e.g. dropped connection problems.

Offline upgrade options via alternate CDs are no longer offered for Ubuntu Desktop and Ubuntu Server. Please ensure you have network connectivity to one of the official mirrors or to a locally accessible mirror and follow the instructions above.

== Upgrading from other releases ==

Users of other Ubuntu releases need to upgrade first to 12.10, and then to 13.04.

For further information on upgrading to 12.10, please see its [[https://help.ubuntu.com/community/QuantalUpgrades|upgrade instructions]].

== Ubuntu downloader for Windows discontinued ==
Due to various bugs in Wubi that have not been addressed in time for the final release, the Ubuntu team will not be releasing the Wubi installer with 13.04.  You can read more about this decision [[https://lists.ubuntu.com/archives/ubuntu-devel/2013-April/036993.html|here]].  Users who wish to try out Ubuntu without repartitioning a Windows system are encouraged to use a live system instead, booted from either a DVD or a USB disk.

== Support lifespan reduced ==
Ubuntu 13.04 will only be supported for 9 months. Previous non-LTS releases were supported for 18 months. For more information, please read the announcements [[http://fridge.ubuntu.com/2013/03/19/changes-in-ubuntu-releases-decided-by-the-ubuntu-technical-board/|here]] or [[http://fridge.ubuntu.com/2013/03/19/ubuntu-technical-board-looks-at-shuttleworths-proposal-for-release-management-methodology/|here]].

== Download Ubuntu 13.04 ==

13.04 images can be downloaded from a location near you.
## <<BR>>'''Note:''' The Ubuntu Desktop images are now bigger than a standard CD, and you should use a USB or DVD for installation.

You can download 13.04 ISOs from:

http://releases.ubuntu.com/13.04/ (Ubuntu Desktop and Server) <<BR>>
http://cloud-images.ubuntu.com/releases/13.04/release/ (Ubuntu Cloud Server) <<BR>>
http://cdimage.ubuntu.com/netboot/13.04/ (Ubuntu Netboot) <<BR>>
http://cdimage.ubuntu.com/ubuntu-core/releases/13.04/release/ (Ubuntu Core) <<BR>>
http://cdimage.ubuntu.com/edubuntu/releases/13.04/release/ (Edubuntu DVD) <<BR>>
http://cdimage.ubuntu.com/kubuntu/releases/13.04/release/ (Kubuntu) <<BR>>
http://cdimage.ubuntu.com/lubuntu/releases/13.04/release/ (Lubuntu) <<BR>>
http://cdimage.ubuntu.com/ubuntustudio/releases/13.04/release/ (Ubuntu Studio) <<BR>>
http://cdimage.ubuntu.com/ubuntu-gnome/releases/13.04/release/ (Ubuntu-GNOME) <<BR>>
http://cdimage.ubuntu.com/ubuntukylin/releases/13.04/release/ (UbuntuKylin) <<BR>>
http://cdimage.ubuntu.com/xubuntu/releases/13.04/release/ (Xubuntu) <<BR>>
##http://cdimage.ubuntu.com/kubuntu-active/releases/13.04/release/ (Kubuntu Active) <<BR>>

= New features in 13.04 =

Please see the [[https://blueprints.launchpad.net/ubuntu/raring/+specs|Raring blueprint list]] for details.

Please test and report any bugs you find:

  http://help.ubuntu.com/community/ReportingBugs

== Updated Packages ==

As with every new release, packages--applications and software of all kinds--are being updated at a rapid pace. Many of these packages came from an automatic sync from [[http://www.debian.org|Debian]]'s unstable branch; others have been explicitly pulled in for 13.04 Raring Ringtail.

For a list of all packages being accepted for 13.04 Raring Ringtail, please subscribe to [[https://lists.ubuntu.com/mailman/listinfo/raring-changes|raring-changes]].

=== Linux kernel 3.8.8 ===

Ubuntu 13.04 includes the [[https://launchpad.net/ubuntu/+source/linux/3.8.0-19.29|3.8.0-19.29 Ubuntu Linux kernel]] which was based on the [[http://www.kernel.org/pub/linux/kernel/v3.x/linux-3.8.8.tar.bz2|v3.8.8 upstream Linux kernel]].

=== Unity 7 ===

Unity 7 brings a lot of performance improvements, reduced memory consumption and a great number of small UI fixes to bring a better overall shell experience. Those are like being typo-tolerant in the dash when searching for an application, using the mouse scroll wheel on a launcher icon to switch between applications or better available third party devices handling. You will notice as well some new icons themes to continue on lead of bringing design as the central Ubuntu experience.

You will notice that only one workspace is available by default on any new installation. If you want to bring back workspaces, you can find an option in the Appearance panel of System Settings under the Behavior tab. You can as well enable "Show desktop" button on the Launcher.

=== Upstart 1.8 ===

This release provides a new bridge, the `upstart-file-bridge(8)` that allows jobs to react to filesystem changes. For example, to have a job start when a particular file is created:

{{{
start on file FILE=/var/log/foo.log EVENT=create
}}}

Or to start a job when a file matching a glob pattern is ''deleted'':

{{{
start on file FILE=/var/app/*.foo EVENT=delete
}}}

See `upstart-file-bridge(8)` and `file-event(7)` for further details.

Additionally, a new `upstart-monitor(8)` tool is available that allows event flows to be observed in real-time. This tool can run as a graphical or console application.

=== LibreOffice 4.0 ===
for all details, see: https://wiki.documentfoundation.org/ReleaseNotes/4.0

==== Core ====
 * New Widget layout technique for dialog windows introduced
 * Support for Firefox Personas in LibreOffice
 * Document Management Systems Integration for Alfresco, Nuxeo, SharePoint via libcmis
 * Less Java dependencies: e.g. more Wizards available even in the default install
 * moved completely from Python 2.6 to Python 3.3 internally
 * PDF Import, the Presenter Console, and the Python Scripting Provider are core features now
 * '''dropping legacy binfilter and a lot of obsolete UNO-API interfaces'''

==== Writer ====
 * The "Apply Style" combo box in the toolbar now features previews of the styles to choose.
 * Import ink annotations from DOCX and RTF documents
 * Import / export support for native RTF math expressions

==== Calc ====
 * Various performance improvements of ODS document import
 * Increased size limit on (uncompressed) ODF documents from 2Gb to 4Gb
 * XML Source dialog to quickly import arbitrary XML content

==== Impress/Draw ====
 * '''Impress Remote control''' for controling presentations via Bluetooth/Wifi from a Smartphone
 * Import for MS Publisher files
 * Import for _all_ Visio file formats, even MS Office 2013
 * various PPTX import fixes
 * hyperlinks/fields wrapping
 * RTL support for the Presenter Console

==== Base ====
 * Native support (mork driver) for accessing Thunderbird address books

=== CUPS 1.6.2 and cups-filters 1.0.34 ===
We had already switched to CUPS 1.6.x in Quantal (12.10) but had to apply a huge, awkward Ubuntu-specific patch to avoid regressions. Now we are up to all new standards without needing to do anything Ubuntu-specific.

Most important change here is the way how network printing works. Formerly, a CUPS-specific mechanism was used. The server broadcasted information about the printers it shares and the clients listen to these broadcasts making the printers available on the client side, looking like local print queues for the applications.

Recently, the [[http://www.pwg.org/|Printer Working Group (PWG)]], an association of printer and software industry for developing standards related to digital printing, has created a standard for broadcasting information about shared printers. This standard is broadcasting the information via Bonjour, a protocol also used for many other network services, like shared files systems, screens, music/video servers, ...

CUPS has adopted this standard in 1.6.x, but only broadcasts and does not listen to broadcasts of CUPS daemons (or generally print servers using Bonjour) on other machines, letting remote printers not automatically get available locally. CUPS also dropped the old broadcasting protocol without transition period.

To overcome the problems and keeping network printing as easy as before (this is why 10 years ago the distros switched to CUPS) the cups-filters project of OpenPrinting introduced cups-browsed, an extra daemon which by default listens to Bonjour broadcasts of remote CUPS daemons (of IPP printers coming soon) and automatically creates local print queues pointing to the shared printers making pure CUPS 1.6.x networks working out-of-the-box.

If your network still contains machines running CUPS 1.5.x and older, cups-browsed also has legacy support for the old CUPS broadcasting, browsing (listening), and BrowsePoll. Please see the comments in /etc/cups/cups-browsed.conf, edit the file appropriately, and restart cups-browsed ("sudo restart cups-browsed") or reboot. When upgrading to Raring, BrowsePoll directives are overtaken from CUPS to cups-browsed automatically.

For everyone developing embedded or mobile systems based on Ubuntu, the CUPS package is split up into more binary packages to get a minimum client-only printing stack, of the packages cups-daemon, libcups2, and cups-browsed, occupying only ~1 MB. This only listens for Bonjour broadcasts (legacy CUPS broadcasts and BrowsePoll optional) of remote CUPS servers and makes the printers available locally. No drivers and filters for locally connected printers are available then.

Another thing to mention which was available before but never told about in release notes: When sharing local printers they are automatically available also for Apple's iOS devices (iPhone, iPad, iPod touch).

=== Python 3.3 ===

We eventually intend to ship only [[http://docs.python.org/py3k/whatsnew/3.0.html|Python 3]] with the Ubuntu desktop image, not Python 2.  The Ubuntu 13.04 image continues this process, although we will not be able to convert everything to Python 3 for Ubuntu 13.04 final image.

If you have your own programs based on Python 2, fear not!  Python 2 will continue to be available (as the `python` package) for the foreseeable future.  However, to best support future versions of Ubuntu you should consider porting your code to Python 3.  [[Python/3]] has some advice and resources on this.

== General ==

Automatic Apport crash reporting has been enabled by default again to catch problems early on. It now [[http://www.piware.de/2011/11/apport-1-90-client-side-duplicate-checking/|checks for duplicates on the client side]], which will avoid uploading debug data and creating Launchpad bug reports unnecessarily in many cases now.

=== Software Updater ===

Software Updater in 13.04 has a simplified details panel that most prominently shows applications and manually-installed packages.  Libraries and packages that belong to the base system are collected under a single item.

== Ubuntu  ==
=== Upstart User Sessions (technology preview) ===
This Ubuntu release includes a "tech preview" of Upstart User Sessions, which allow Upstart to supervise a user's desktop session. This feature is disabled by default for Ubuntu 13.04, but can be manually enabled for testing.

To enable Upstart User Sessions for all users:

 1. Uncomment "`ubuntu`" in file `/etc/upstart-xsessions`.
 1. Logout of any desktop sessions.
 1. Login to the default Unity session.

To disable, simply comment out "`ubuntu`", logout and log back in again.

To see details of the running Upstart session, either `echo $UPSTART_SESSION` to see the D-Bus address the Session Init process is listening to, or run the following command which lists the process id of the Upstart session along with the value of `$UPSTART_SESSION`:

{{{
$ initctl list-sessions
}}}

The normal suite of Upstart commands is available (such as `initctl`, `start`, and `stop`). For example, to list all session jobs, run:

{{{
$ initctl list
}}}

To list ''system'' jobs from within a user session, run one of the following two commands:

{{{
$ initctl --system list
$ sudo initctl list
}}}

Session jobs are read from `/usr/share/upstart/sessions/` and `$XDG_CONFIG_HOME/upstart/` (or `$HOME/.config/upstart` if `$XDG_CONFIG_HOME` is not set).

Session job output is logged to `$XDG_CACHE_HOME/upstart/` (or `$HOME/.cache/upstart/` if `$XDG_CACHE_HOME` is not set).

See `init(5)` for full details.

=== Friends ===

Social networking for 13.04 is now handled by the Friends service, which replaces the backend Gwibber provided in previous Ubuntu releases.  There is no transition required, if you have social networking accounts setup in Ubuntu Online Accounts, the Friends service will just work.  The Gwibber lens in Unity has been replaced with a Friends lens and works in much the same way.  The Gwibber client application is no longer included by default, for similar functionality friends-app can be installed from Software Center.

== Ubuntu Server ==

=== OpenStack Grizzly ===

Ubuntu 13.04 includes the Grizzly release of Openstack. OpenStack projects supported in 13.04 include: Nova, Glance, Swift, Keystone, Horizon, Cinder and Quantum. Ceilometer is also included in 13.04 in Ubuntu Universe.

Openstack Grizzly is also available for Ubuntu Server 12.04 LTS in the [[ServerTeam/CloudArchive|Ubuntu Cloud Archive]].

OpenStack continues to be deployable using Juju Charms; for the Grizzly release this also includes deploying OpenStack in a highly avaliable configuration as demonstrated at the OpenStack Summit in Portland. See the [[ServerTeam/OpenStackHA|OpenStack HA Reference architecture]] documentation for more details.

=== Juju ===

Ubuntu 13.04 includes the 0.7 release of Python Juju ('juju' package). 

The initial release (1.10.0) of the Go rewrite of Juju ('juju-core' package) is available in the -backports repository, this package is co-installable with the 0.7 version. 

You can revert to the default (0.7) version by using the following:

{{{
$ sudo update-alternatives --set juju /usr/lib/juju-0.7/bin/juju
}}}

or to the new 1.10.0 release using:

{{{
$ sudo update-alternatives --set juju /usr/lib/juju-1.10.0/bin/juju
}}}

Please note that the 1.10.0 (Go version) release is not yet end-user feature complete compared to 0.7 - for example, the LXC local provider is not yet implemented in 1.10.0; if you install both you will get 0.7 by default.

See the [[http://juju.ubuntu.com/docs|Juju documentation]] for full details of these changes.

=== MAAS ===

Ubuntu 13.04 includes the latest MAAS release (1.3). This new upstream release includes various bug fixes and improvements in comparison to older MAAS releases. New features include:

 * Customizable kernel command lines for each node via tags.
 * Installation path for Image Based Installations.
 * Improved IPMI detection, with support most recent iLO versions.
 * Support for Multiple Juju Environments (one per MAAS user).

=== Simple Streams ===

There is now machine formated JSON data describing all downloadable content for Ubuntu cloud images.  The data format is called "simple streams", and can be found at http://cloud-images.ubuntu.com/releases/streams/ . There is a sample client included in Ubuntu in the 'simplestreams' package.  The client can be used to keep cloud or local downloads in sync with what is available from Ubuntu.

=== Ceph 0.56.4 ===

Ubuntu 13.04 includes the latest Ceph Bobtail LTS release (0.56.4). OpenStack Keystone integration has been implemented in the RADOS Gateway for this release, providing a drop-in replacement for Swift.

Ceph continues to be deployable using Juju Charms; notable changes include:

 * Underlying default disk format for OSD's is now XFS; this can be changed using a configuration option in the ceph and ceph-osd charms.
 * ceph-radosgw charm now supports the keystone integration implemented in bobtail.

For full details on upgrading please see the Ceph [[http://ceph.com/docs/master/release-notes/#v0-56-4-bobtail|release notes]].

=== MongoDB 2.2.4 ===

Ubuntu 13.04 includes MongoDB 2.2.4; for this release SSL support has been enabled to support secured use of MongoDB (primarily to support Juju 2.0). The ARM support has also been improved during the 13.04 development cycle.

This release of MongoDB will also be provided as an official backport for 12.04 and 12.10.

=== OpenvSwitch 1.9.0 ===

Ubuntu 13.04 includes the latest stable release of OpenvSwitch 1.9.0, featuring full upstream support for Linux 3.8.  As of this release, the bridge compatibility module is officially deprecated - users should start planning to migrate away from this feature. For full details of this release please see the upstream [[http://openvswitch.org/releases/NEWS-1.9.0|release notes]].

== Kubuntu ==

== Xubuntu ==

Starting with 13.04, Xubuntu targets a 1GB USB. For more information about Xubuntu 13.04, read the [[http://xubuntu.org/news/13-04-release|Xubuntu release announcement]].

== Edubuntu ==

 * Ubiquity step indicator is inaccurate. As you progress through the installation steps, the total progress bar indicator at the bottom will either appear to be ahead or behind. [[https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1172626|LP: #1172626]]

== Lubuntu ==

Please read the [[RaringRingtail/ReleaseNotes/Lubuntu|Release notes]] for information.

== Ubuntu Studio ==
For information about the Ubuntu Studio Beta release, please see [[RaringRingtail/UbuntuStudio]].

== UbuntuKylin ==
[[UbuntuKylin]] has had several bug fixes applied to chinese-calendar and
indicator-china-weather, made fcitx as default and improved the theme since
Beta 1. For information about the UbuntuKylin Beta release, please see [[UbuntuKylin/1304-ReleaseNotes]].

== Ubuntu GNOME ==

 * In coordination with the Ubuntu Desktop Team, we have decided to stick with GNOME 3.6 for Ubuntu 13.04. For an overview of what's new in GNOME 3.6, please see the [[https://help.gnome.org/misc/release-notes/3.6/|Release Notes]].
 * The [[https://launchpad.net/~gnome3-team/+archive/gnome3/|GNOME3 PPA]] offers an early look at GNOME 3.8 for Ubuntu. Please note that you need to do a dist-upgrade instead of a regular upgrade or else GDM or GNOME Shell won't run after upgrading. In case of problems, please make yourself familiar with ppa-purge before using the GNOME3 PPAs.
 * There are some additional GNOME 3.8 apps in the [[https://launchpad.net/~gnome3-team/+archive/gnome3-staging/|GNOME3 Staging PPA]] but these apps have known bugs, some of which are serious or critical bugs.
 * Default apps have changed since Ubuntu GNOME Remix 12.10.
  * Firefox instead of GNOME Web (Epiphany)
  * Ubuntu Software Center and Update Manager instead of GNOME Software (gnome-packagekit)
  * LibreOffice instead of Abiword and Gnumeric
  * The other apps are still available for install; they just aren't included in the default install.

## == Mythbuntu ==
## Not releasing in 13.04 per Mario

= Known issues =

As is to be expected, at this stage of the release process, there are some significant known bugs that users may run into with the Ubuntu 13.04 release.  The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:

== Boot, installation and post-install ==

 * When using installer to upgrade or reinstall an existing installation with encrypted swap, the installer may fail to reuse the partition. A warning will be shown, however the installation can be completed. The installed system will not have swap activated and users are advised to recreate swap on their systems. Please see advice about adding and activating swap at: https://help.ubuntu.com/community/SwapFaq ([[https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1172002 | LP: #1172002]])
 * Installs on very small memory systems may fail to start or exit without completing with no error. It is recommended that swap be created before install for such systems. Please see advice about adding and activating swap at: https://help.ubuntu.com/community/SwapFaq ([[https://bugs.launchpad.net/ubuntu-release-notes/+bug/1172161 | LP: #1172161]])
 * When using unattended reboots (preseeded), casper will still wait for ENTER to be preseed by the user. This can be worked around by calling "sed -i 's/eject -p -m.*/&; [ "$prompt" ] || return 0/' /etc/init.d/casper" before rebooting the machine (as a late_command for example). ([[https://bugs.launchpad.net/bugs/1172653 | LP: #1172653]])
 * In rare circumstances the 'Next' button on the installer 'Install Type' screen is non-functional.  This is intermittent and may be resolved by hitting 'Back' and retrying.  ([[https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1172572 | LP: #1172572]])
 
== Migration ==

== Graphics and Display ==

== Desktop ==
 * The official Google Chrome installer is built against libudev0 instead of the libudev1 available in Ubuntu 13.04. This should be fixed with Chrome 28 which is still in testing. We recommend that you install the open source chromium-browser from the Ubuntu Software Center until Google releases the fix for this issue. ([[https://code.google.com/p/chromium/issues/detail?id=226002 | Google: #226002]])

== Kernel ==

 * There are reports of non-functional HDMI audio on various machines, even with proprietary drivers. In some cases analog built-in audio is affected too. Typically the the audio device does not show up in sound settings at all.  ([[https://bugs.launchpad.net/bugs/1169984 | LP: #1169984]])

== Ubuntu Server ==
 * OpenStack Nova includes a new component, nova-conductor, which is used over RPC by nova-compute nodes instead of all compute nodes directly accessing the underlying nova database.  nova-conductor is typically deployed separately to nova-compute - this needs to be done manually during the upgrade process. [[https://launchpad.net/bugs/1155327 | LP: #1168757]]

=== MAAS ===
 * MAAS Server install fails without a network connection during install of maas-region-controller ([[https://launchpad.net/bugs/1172566 | LP: #1172566]])

##== Ubuntu Core ==
## * ...

##== Kubuntu ==
## * ...

##== Xubuntu ==
## * ...

##== Lubuntu ==
## * ...

##== Ubuntu Studio ==
##
## * ...

##== Mythbuntu ==
## * ...

##== UbuntuKylin ==
## * ...

== Ubuntu GNOME ==

 * The "Install Alongside" option doesn't work (Bug:1164592).

 * There are two Online Accounts entries in System Settings. One is the GNOME tool which you can use for Contacts, Documents, and Evolution. The other is Ubuntu's tool for Empathy, Gwibber, Shotwell, and if you install it, Unity. (Bug:1040193)

----

'''For a listing of more known issues, please refer to the Raring Ringtail [[https://bugs.launchpad.net/ubuntu/raring/+bugs|bug tracker]] in Launchpad.'''

= Reporting bugs =

It should come as no surprise that this release of Ubuntu 13.04 contains other bugs. Your comments, bug reports, patches and suggestions will help fix bugs and improve the quality of future releases. Please [[http://help.ubuntu.com/community/ReportingBugs|report bugs using the tools provided]].

If you want to help out with bugs, the [[http://wiki.ubuntu.com/BugSquad|Bug Squad]] is always looking for help.

= Ubuntu Project Contributors =

Ubuntu 13.04 would not be possible without the contributions of our 
[[RaringRingtail/ReleaseNotes/Credits/Developers|developers]], 
[[RaringRingtail/ReleaseNotes/Credits/Testers|testers]], 
[[RaringRingtail/ReleaseNotes/Credits/ReleaseTeam|release team members]], 
[[RaringRingtail/ReleaseNotes/Credits/DocsTeam|documentation writers]], 
[[RaringRingtail/ReleaseNotes/Credits/Translators|translators]], 
[[RaringRingtail/ReleaseNotes/Credits/BugImprovers|bug analysts]] and our 
[[RaringRingtail/ReleaseNotes/Credits/BugReporters| users who take the time to file bugs]].   
Ubuntu is based on [[http://www.debian.org|Debian]], [[http://www.kernel.org|the Linux Kernel]] and our many other excellent upstream projects.  Thank you!

= Participate in Ubuntu =

## These images were able to be made available to you thanks to the help of our [[https://wiki.ubuntu.com/RaringRingtail/TechnicalOverview/Beta1/Testers|QA Community]].

If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

 http://www.ubuntu.com/community/get-involved

= More information =

You can find out more about Ubuntu on the [[http://www.ubuntu.com|Ubuntu website]] and [[http://wiki.ubuntu.com|Ubuntu wiki]].

To sign up for future Ubuntu development announcements, please subscribe to Ubuntu's development announcement list at:

 http://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce
