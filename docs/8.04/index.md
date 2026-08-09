---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/HardyReleaseNotes -->

(ubuntu-8-04-lts-release-notes)=
# Ubuntu 8.04 LTS release notes

These release notes document known issues with Ubuntu 8.04 LTS and version 8.04 of Kubuntu and Xubuntu.


(8-04-lts-system-requirements)=
## System Requirements

The minimum memory requirement for Ubuntu 8.04 is 384MB of memory for desktop CDs, and 256MB for other installation methods. (Note that some of your system's memory may be unavailable due to being used for the graphics card.)

With only the minimum amount of memory available, the installation process will take longer than normal, but will complete successfully, and the system will perform adequately once installed. Low-memory systems may be able to use the desktop CD to install by selecting "Install Ubuntu" from the boot menu to run just the installer, rather than the whole desktop started by selecting "Try Ubuntu without any change to your computer".


(8-04-lts-installation)=
## Installation


(8-04-lts-openoffice-org-database-java-equation-editor-support)=
### OpenOffice.org database, Java, equation editor support

* For reasons of disk space, the database and equation editor components of OpenOffice.org, as well as Java integration support, are not included on the installation CDs.  To get the full OpenOffice.org suite after install, you can select "OpenOffice.org Office Suite" from the **Applications -> Add/Remove** menu, or install the `openoffice.org` metapackage using the package manager.


(8-04-lts-iscsi-partitions)=
### iSCSI partitions

* The open-iscsi package is now a maintained option in Ubuntu 8.04 LTS, and iSCSI NAS partitions can be configured right from the installer.  At this time, however, the root and boot filesystems should be placed on a local partition.


(8-04-lts-wubi)=
### Wubi

* When Wubi is installed from CD, the installation might fail while extracting the ISO file and you might see a message stating that the CD is in use and asking you to retry. To work around this, place Wubi.exe and the 8.04.1 desktop CD ISO image in a directory together and run Wubi from there. If you don't know which ISO to use, let Wubi download the appropriate ISO for you. Make sure that no CD is in the tray.

* Software RAID and encrypted disks are not supported by Wubi.


(8-04-lts-upgrading)=
## Upgrading

Users of Ubuntu 7.10 or Ubuntu 6.06 LTS can upgrade to Ubuntu 8.04 by a convenient automated process. Users of other Ubuntu releases should upgrade step by step (e.g. 6.10 -> 7.04 -> 7.10 -> 8.04 LTS). Complete instructions may be found at [www.ubuntu.com/getubuntu/upgrading](http://www.ubuntu.com/getubuntu/upgrading).


(8-04-lts-route-metrics)=
### Route metrics

* ifupdown now sets the default route metric to 100 for interfaces with no metric option set in /etc/network/interfaces. This change makes no difference for most users, but may affect a few users with complex networking requirements. If you rely on the previous default route metric of 0 (zero), edit /etc/network/interfaces and set the metric option explicitly for your interface, for example:

```none
iface eth0 inet static
        address 192.168.0.2
        network 192.168.0.0
        broadcast 192.168.0.255
        netmask 255.255.255.0
        gateway 192.168.0.1
        metric 0
```


(8-04-lts-network-manager)=
### Network Manager

* In Ubuntu 8.04, network-manager only manages interfaces that are marked for roaming. Thus, all interfaces that were previously managed by network-manager will be set to roaming mode during upgrade. Technically, this takes any interface stanzas using the `dhcp` method with no options and that are marked `auto`, and removes them from /etc/network/interfaces. If you rely on your interfaces being started by ifupdown when the system starts up, you need to re-enable them in /etc/network/interfaces manually, or disable roaming in **System** -> **Administration** -> **Network**.


(8-04-lts-nfs-mount-support)=
### NFS mount support

* To mount NFS filesystems, you must now install the `nfs-common` package.


(8-04-lts-bin-sh-is-now-dash)=
### /bin/sh is now dash

* To improve overall system performance, the /bin/sh shell in Ubuntu 6.10 and later is dash, rather than bash as it was in Ubuntu 6.06 LTS.  This may cause compatibility problems for local shell scripts.  Please see DashAsBinSh for more information.


(8-04-lts-powerpc-and-sparc-moved-to-ports-ubuntu-com)=
### PowerPC and SPARC moved to ports.ubuntu.com

* The PowerPC and SPARC architectures no longer receive commercial support from Canonical for new releases of Ubuntu (PowerPC [as of 7.04](https://lists.ubuntu.com/archives/ubuntu-announce/2007-February/000098.html), SPARC [as of 8.04](https://lists.ubuntu.com/archives/ubuntu-devel-announce/2008-March/000400.html)), and accordingly these architectures have been moved to ports.ubuntu.com. Users of these architectures should take care to update `/etc/apt/sources.list`. Old sources.list entries looked like this (perhaps using `<country>`.archive.ubuntu.com rather than archive.ubuntu.com):

```none
  deb http://archive.ubuntu.com/ubuntu gutsy main restricted
  deb http://security.ubuntu.com/ubuntu gutsy-security main restricted
```

while new entries should look like this:

```none
  deb http://ports.ubuntu.com/ubuntu-ports hardy main restricted
  deb http://ports.ubuntu.com/ubuntu-ports hardy-security main restricted
```


(8-04-lts-commercial-partner-repository)=
### Commercial/partner repository

* The "commercial" repository on `archive.canonical.com` has been renamed to "partner". If you upgrade directly from an earlier release to Ubuntu 8.04 using the documented upgrade procedure, then this will be handled automatically. However, if you upgraded manually, you will need to edit `/etc/apt/sources.list` by hand. The correct syntax is:

```none
deb http://archive.canonical.com/ubuntu hardy partner
```


(8-04-lts-ultrasparc-disk-label-changes)=
### UltraSPARC disk label changes

* Users upgrading to Ubuntu 8.04 LTS on UltraSPARC from Ubuntu 6.06 LTS should manually re-run fdisk on all disks. fdisk will warn if the disk label needs to be updated; follow its instructions. New installations of Ubuntu 8.04 will automatically use the new disk label format.


(8-04-lts-scim-hotkey-changes)=
### SCIM hotkey changes

* The default Shift+Space hotkey for the Smart Common Input Method (SCIM) has been removed, and Alt+``` (grave accent) has been added in its place. As before, other default hotkeys are Control+Space, Zenkaku_Hankaku, and Hangul. Hotkeys can be configured using the FrontEnd -> Global Setup section in SCIM Setup.


(8-04-lts-upgrading-from-evms-6-06-lts-systems)=
### Upgrading from EVMS 6.06 LTS Systems

* Since 7.10, EVMS support was dropped by upstream and moved to Universe in Ubuntu. Users from previous LTS Release should be aware of this issue and act accordingly as suggested at [wiki.ubuntu.com/Evms](https://wiki.ubuntu.com/Evms) and [bugs.edge.launchpad.net/bugs/115616](https://bugs.edge.launchpad.net/bugs/115616). The common solution is to remove evms from console.


(8-04-lts-other-known-issues)=
## Other known issues


(8-04-lts-dell-raid-firmware-compatibility)=
### DELL RAID firmware compatibility

* Ubuntu 8.04 LTS fails to run on some DELL PowerEdge servers with RAID controllers, such as the 3/Di controller in the DELL PowerEdge 1650, due to a bug in the RAID firmware.  To install or upgrade to Ubuntu 8.04 LTS on a system with the affected RAID controller, you will first need to upgrade your RAID firmware.


(8-04-lts-dual-screen-support-limitations-for-kubuntu)=
### Dual Screen Support Limitations for Kubuntu

* Support for dual screen is in many cases more limited for Kubuntu 8.04 than for Ubuntu 8.04 LTS. The Xinerama extension to X windows that was used in previous releases for dual screen support has largely been replaced by Xrandr. Updated KDE3 tools to support Xrandr are not available. Limited Xrandr support is available in KDE4. For most video drivers, dual screen can be set up only via the 'xrandr' command line tool and/or manual xorg.conf settings. See man xrandr for information on xrandr command line options. Additional information on X configuration can be found at [wiki.ubuntu.com/X/Config](https://wiki.ubuntu.com/X/Config).

* The following other options may be available, but have not been tested by the development team:

  - For Intel, the legacy -i810 driver supports Xinerama

  - ATI users can go back to Xinerama by installing the old 6.6.3 version of -ati

  - The binary drivers (-nvidia and -fglrx) may still support Xinerama, but they have their own multi-screen setup tools that should be used in preference to System Settings -> Display and Monitor (displayconfig)

* A new X windows recovery feature is available. If you are unable to boot after attempting changes, you can reboot, choose the restore option in the boot menu, and then select the 'xfix Try to fix X server' option on the Recovery Menu. This should restore your X windows configuration to a usable condition and allow you to boot normally.


(8-04-lts-gvfs-and-authenticated-smb-browsing)=
### GVFS and authenticated smb browsing

* The GVFS filesystem layer used in GNOME 2.22 did not support password authentication when browsing the list of shares on an SMB server, which could result in empty share lists in nautilus when connecting to Windows 2003 hosts in some configurations.  A fix for this issue is available in the packages nautilus 1:2.22.5.1-0ubuntu3 and gvfs 0.2.5-0ubuntu8, which are included in the 8.04.4 point release.


(8-04-lts-pidgin-and-icq)=
### Pidgin and ICQ

* The version of the Pidgin Internet Messenger included in Ubuntu 8.04.1 cannot connect to ICQ due to a recent change to the ICQ servers.  An update will be made available shortly after the 8.04.1 maintenance release.


(8-04-lts-totem-movie-player-and-pulseaudio-sound-server)=
### Totem movie player and PulseAudio sound server

* Some users report problems with video playback in the GNOME movie player, and audio playback in other applications, due to an error when connecting to the PulseAudio sound server.  Investigation of this possibly hardware-specific issue is ongoing.  A workaround is to enter the **System -> Preferences -> Sound** dialog and change the **Music and Movies** sound playback option from 'Autodetect' to 'ALSA'.


(8-04-lts-fontforge)=
### Fontforge

When "complex character input" is enabled, either by hand using the language-selector tool or as a result of using a CJK locale, fontforge does not respond to the keyboard.  It is believed that this is a bug in fontforge, not related to SCIM.  As a workaround, you can run fontforge from a terminal using the command _unset XMODIFIERS; fontforge_.
