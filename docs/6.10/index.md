---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/EdgyReleaseNotes -->

(ubuntu-6-10-release-notes)=
# Ubuntu 6.10 release notes


The Ubuntu developers are moving very quickly to bring you the absolute latest and greatest software the Open Source Community has to offer. With the Ubuntu 6.10 release comes a whole host of excellent new features. Improvements have been made all around, such as faster system boot up times, faster GNOME start up times, improvements to the user interface, a shiny new optimized kernel, GNOME 2.16, and much, much more.

## Installation

Get it while it's hot. CD images for installation and live demonstration are available for direct download and via BitTorrent.  A list of mirrors can be found on the official [download page](http://www.ubuntu.com/products/GetUbuntu/download).

## Upgrade from 6.06 LTS

If you want to upgrade from 6.06 LTS to 6.10, run the following command (either via ALT-F2 or a terminal):

```
gksu "update-manager -c"
```

The "-c" switch instructs Update Manager to look for upgrades. By default, the Ubuntu 6.06 LTS release will not offer that automatically because of its long support cycle and high stability.

If you have a working network connection, it should then inform you about a new release and offer to upgrade your system.

## Upgrades with apt-get

If the upgrade is performed on a system without update-manager (e.g. on a server), the upgrade must be performed in two steps. The first run of `apt-get dist-upgrade` will upgrade everything except for upstart. After that, a second `apt-get dist-upgrade` will finish the upgrade.

## New Features

### New Startup Screen

All the improvements in usplash have begun to pay off, as the new theme has landed. The usplash will now scale to larger screens and many different resolutions.

### GNOME 2.16

Ubuntu 6.10 comes with the latest GNOME release, GNOME 2.16. After Dapper, a large number of bugfixes and feature additions have gone into GNOME. Release 2.16 is the culmination of all the hard work that has made GNOME more secure, faster and stable. Many applications also have been updated or added.

### Tomboy

It is a wikiwiki world out there, and now your desktop does not have to be left behind.  Edgy comes with Tomboy pre-installed, allowing easy note taking and linking.

### F-spot

With Ubuntu 6.10 comes a replacement of gthumb, the photo manager, in the form of a new Mono application, F-spot. F-spot allows easy tagging, editing and uploading to various online photo websites, including Flickr.

### Evolution

New Evolution 2.8.0, updated in GNOME 2.16. New features include vertical message panes:

### Firefox 2.0

Fitting the theme of Edgy's new applications, Firefox 2 is included. New features in 2.0 include inline spell checking support in web forms, restoring sessions that crashed, built-in phishing detectors, enhanced search engine management with built-in OpenSearch support, improved tab support with "undo close tab" support, better support for previewing and subscribing to web feeds, and much more.

### OpenOffice 2.0.4

OpenOffice.org 2.0.4 is also included. This is mostly a security and bugfix release, dealing with specific issues regarding sandboxing of Java applets and macros.

### Gaim 2.0 beta 3.1

Gaim 2.0 beta 3.1 is a large leap forward, including a great many tweaks to the graphical user interface, Yahoo Doodles, ICQ file transfer, SIP support and much more.

### Orca

Replacing the venerable Gnopernicus is the new Orca, a scriptable screenreader for the GNOME desktop, further enhancing accessibility features in Ubuntu. Expect some great things from this in the coming months and years. Best of all, it is written in Ubuntu's favourite language, Python.

### New Theme

The new Edgy Theme brings together the best of the art team: A new login page, new desktop wallpaper, and new sounds.

### Rounded window borders

With Ubuntu 6.10, we've enabled rounded window borders for all corners of the window.

### Upstart - init redone

The new init system, upstart, has now been turned on by default. For most users, this change will go totally unnoticed. However, upstart offers some very clear advantages, such as a cleaner design and the ability to make booting faster, all of which can be read on the [Replacement Init wiki page](https://wiki.ubuntu.com/ReplacementInit).

### New translations

New language-packs were uploaded to Ubuntu this week, pulling the latest work out of Rosetta. If you want to help the translations teams out, head over to [Rosetta](https://launchpad.net/rosetta) and dive in.

### Crash Reports

Reporting crashes is now easier thanks to automated problem reports. When a userspace application experiences a crash, an automated problem report will be generated. This means that users do not have to create a *debug version* of applications, and they will no longer have to spend hours trying to re-create the crash.  To learn more, please visit:

[wiki.ubuntu.com/Apport](https://wiki.ubuntu.com/Apport)

## Known Issues

The following notable bugs are known to exist in the final release:

* Power management may behave inappropriately on systems with multiple batteries. [Bug #60442](https://launchpad.net/bugs/60442)
* When shutting down or rebooting the AMD64 or PowerPC LiveCD: If it does not automatically power off or reboot when you press ENTER, use your computer's power or reset buttons.  It is safe to do so at this point. [Bug #58503](http://launchpad.net/bugs/58503)
* The advanced partitioning mode of the installer on the Desktop CD cannot create new HFS bootstrap partitions on Power Macintosh systems. This affects only Power Macintosh systems without existing GNU/Linux installations. Possible workarounds are to use automatic partitioning first, which will create the HFS bootstrap partition, and then do a second installation with manual partitioning if necessary, or to use the alternate install CD rather than the desktop CD. [Bug #68243](https://launchpad.net/bugs/68243)
* The advanced partitioning mode of the installer on the Desktop CD has trouble re-using an existing root file system, and will incorrectly claim "No root file system". Since you must reformat the root file system for use by the installer in any case, you can easily work around this problem by deleting and re-creating the partition in question in the advanced partitioner. [Bug #67130](https://launchpad.net/bugs/67130)
* The installer may crash if language packs are uninstallable in certain ways. If this happens to you, you can work around it by installing in English or by disconnecting from the network during installation. [Bug #61912](https://launchpad.net/bugs/61912)
* The "Start Ubuntu in safe graphics mode" option in the CD boot menu is not working correctly. See EdgyKnownIssues for a workaround.

The default system shell (`/bin/sh`) changed to `dash` in this release, which may break some incorrectly-written third-party scripts. See DashAsBinSh for a discussion of the issues and what you can do if you encounter problems.

### Problems on Sun T2000 systems

SUN T2000 users should upgrade their ALOM/OBP to at least 123482-02 before upgrading to Ubuntu 6.10. Upgrade procedures are provided by Sun at the following URL:
[sunsolve.sun.com/search/document.do?assetkey=1-21-123482-02](http://sunsolve.sun.com/search/document.do?assetkey=1-21-123482-02)

Rationale: The new kernel in Ubuntu 6.10 potentially triggers a HyperVisor bug in handling IRQs which results in a machine halt/poweroff (ERROR: HV Abort: JBI Error (22) - PowerDown) during reboots.
The machine needs to be re-powered on in order to resume normal operation (including a complete POST) which may result in long out-of-service and unscheduled downtime.

## Reporting Bugs

Your comments, bug reports, patches and suggestions will help fix bugs and improve future releases.  Please report bugs through Malone:

[bugs.ubuntu.com/](http://bugs.ubuntu.com/)

If you want to help out with those bugs, the [Bug Squad](http://wiki.ubuntu.com/BugSquad) is accepting volunteers.

## Participate in Ubuntu

If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

[www.ubuntu.com/community/participate/](http://www.ubuntu.com/community/participate/)

## More Information

You can find out more about Ubuntu on our website, IRC channel and wiki. If you're new to Ubuntu, please visit:

[www.ubuntu.com/](http://www.ubuntu.com/)

To sign up for future Ubuntu development announcements, please subscribe to Ubuntu's development announcement list at:

[lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce](http://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce)

---
All comments, suggestions, etc... can be fired, out of a cannon, at: [Corey Burger](mailto:corey.burger@ubuntu.com)
