---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/DapperReleaseNotes -->

(ubuntu-6-06-lts-release-notes)=
# Ubuntu 6.06 LTS release notes

## Ubuntu 6.06 LTS Release Notes

Ubuntu is a Linux distribution for your desktop or server, with a fast and easy install, regular releases, a tight selection of excellent applications installed by default, and almost any other software you can imagine available through the network. Ubuntu 6.06 LTS (Long Term Support) will be supported with security updates for 5 years on the server and 3 years on the desktop after its release, and professional technical support is available from many companies around the world.

These Release Notes cover new features in Ubuntu 6.06 LTS, download and installation notes, known issues, and frequently asked questions. Please read these notes before, during, and after installation and configuration of Ubuntu 6.06 LTS, and before reporting bugs in [Launchpad](https://launchpad.net/malone/distros/ubuntu).
We hope you enjoy Ubuntu.

---


(6-06-lts-whats-new)=
### What's new

Ubuntu is released regularly and predictably. Since our October 2005 release (Ubuntu 5.10), we've made a lot of improvements to give you the best Linux experience possible. Here's what's new with Ubuntu 6.06 LTS:


(6-06-lts-on-the-desktop-cd)=
#### On the Desktop CD

* A new, very fast, graphical installer based on the Live CD

* Faster system startup and login

* Simplified menu organization

* Graphical shutdown process

* Easy access to power management settings with GNOME Power Manager

* Improved support for video playback

* Optional NetworkManager for convenient roaming between different
    wireless and wired networks

* GNOME 2.14.1, OpenOffice.org 2.0.2, X.org 7.0


(6-06-lts-on-the-server)=
#### On the Server

* New kernels targeted at server platforms. The server kernels are
    tuned differently than the desktop kernels (providing better
    performance for server applications).

* There are both low-end, and "big iron" server kernels. The low-end
    server kernel is generic, and should work on the same equipment
    that the desktop kernel runs on. The highend server kernel is
    geared towards systems with greater than 8 CPUs (ES7000 / Summit
    / BIGSMP).

* Turn-key LAMP installation for this common deployment scenario

* Improved support for clusters and SANs

* Numerous thin client enhancements, including faster client startup,
    graphical boot process, reduced memory requirements, and sound
    device support


(6-06-lts-localization)=
#### Localization

* Automatic setup of non-Latin input methods

* Menu item translations included in language packs, for faster
    integration of new and updated translations provided through
    Rosetta


(6-06-lts-installation-and-upgrades)=
#### Installation and Upgrades

* Ubuntu can now be installed to USB devices, such as removable
    hard drives and flash memory, using the text-mode installer

* A new upgrade tool is available, for simple, clean and reliable
    upgrades from one Ubuntu release to the next, starting with
    Ubuntu 5.10

* The alternate installer now runs in a single stage, rebooting
    straight into the complete system. This makes it faster,
    simpler, and more reliable.


(6-06-lts-under-the-hood)=
#### "Under the hood"

* GCC 4.0.3

* glibc 2.3.6

* Linux 2.6.15.6

* New live CD infrastructure for improved performance, usability and
    space-efficiency

* Greatly improved infrastructure for automatic hardware detection and activation

* The system PATH is now set in exactly one place, /etc/environment, for
    convenient administration

As always, Ubuntu includes the very best of the 100% Free / Libre
application software world, and each new release incorporates
countless new features and bugfixes from the global development
community.


(6-06-lts-downloading-and-installing)=
### Downloading and Installing

Ubuntu 6.06 LTS supports three (3) major architectures: Intel x86, AMD64, and PowerPC. Depending on your needs, you might manage with less than some of the recommended hardware listed in the table below. However, most users risk being frustrated if they ignore these suggestions. These notes are guides. For step by step upgrade instructions please see DapperUpgrades.

Table 1 Recommended Minimum Requirements

**Install Type** **RAM** **Hard Drive Space**
Desktop 256 megabytes 3 gigabytes
Server 64 megabytes 500 megabytes

Here are some common Ubuntu system configurations. Once again, the size of the installation will greatly depend on the software you install during setup. For most users, the default applications are suitable enough for general use.

**Desktop**

A standard desktop box, including a full desktop environment, sound, office suite, email clients, etc. You'll need about 3 gigabytes of hard drive space.

**Server**

This is a small server profile, which provides a common base for all sorts of server applications. It's minimal and designed to have the desired services added on top, such as file/print services, web hosting, email hosting, etc. For these services at least 500MB of disk space will suffice, but consider adding more space depending on the services you'd like to host with your server.


(6-06-lts-known-issues)=
#### Known Issues

* A number of problems have been reported with the installer on the Desktop CD; the [list of known issues in Ubiquity](https://wiki.ubuntu.com/DapperReleaseNotes/UbiquityKnownIssues) outlines some of these that can easily be avoided or worked around. Some of these will be corrected in later updates. In the meantime, if you cannot work around an installer problem with the Desktop CD, the alternate install CD remains available.

* Server images for the SPARC architecture are undergoing final quality assurance and testing; release images will be published as soon as certifications on T1000 and T2000 are complete.

* `redhat-cluster-suite` [fails to install properly](https://launchpad.net/bugs/47645) due to changed error reporting from `ccs_test`. A workaround is to install `ccs` first, provide a valid configuration for it, and install the rest of the suite later. See `/usr/share/doc/gfs-tools/min-gfs.txt` in the `gfs-tools` package for details. Updated packages are available via dapper-updates.

* Upgrades from Ubuntu 5.10 on certain Dell desktop models may hang while upgrading a legacy support package for the PCMCIA subsystem.  An update has been published in the `dapper-updates` repository to correct this problem.

* Systems that have been upgraded from Ubuntu 5.04 (or earlier) [may have to manually delete linux-image-2.6.10 packages before the upgrade](https://launchpad.net/bugs/47537).

* The bug referenced (47537) doesn't appear to have anything to do with the **linux-image** package, but instead deals with problems installing additional languages. In addition, I couldn't find any bug that made reference to install problems due to old linux-image packages having previously been installed. Can anyone shed some more light on this issue?

* If you want to use the packages from an alternate install CD when doing a upgrade, please add the CD to the system with `synaptic` and start `update-manager`. It will open a initial dialog and complain about packages it can't upgrade. This is a [bug](https://launchpad.net/bugs/46340) and can be ignored.

* If you upgrade (whatever method) and have the `nvidia-glx` and `nvidia-settings` packages installed, please remove `nvidia-settings`, otherwise `nvidia-glx` [will be removed on upgrade](https://launchpad.net/bugs/47017). The settings utility is now provided by the `nvidia-glx` package.

* Areca Raid controllers on AMD64 (ARC-1110, 1220, and perhaps others) has file file corruption issues (see Bug #45679). Fixed in Feisty. If require LTS then use Hardy.


(6-06-lts-getting-help-and-technical-support)=
### Getting Help and Technical Support

Ubuntu 6.06 LTS gives users an easy way to get help in most applications installed by default. Once you have an active internet connection, from an open application, just click on Help → Get Help Online  and you'll be directed to an online webpage that gives you help and support options for the application.

Technical Support for Ubuntu is available from a variety of sources: from the community, from Canonical Ltd, from recognized organizations, and from developers directly through open web forums, mailing lists and IRC channels:

* [www.ubuntu.com/support](http://www.ubuntu.com/support)

If you have a question, or if you think you may have found a bug but aren't sure, first try asking on the #ubuntu IRC channel on Freenode, on the Ubuntu Users mailing list, or on the Ubuntu forums:

* [lists.ubuntu.com/mailman/listinfo/ubuntu-users](http://lists.ubuntu.com/mailman/listinfo/ubuntu-users)

* [www.ubuntuforums.org](http://www.ubuntuforums.org)


(6-06-lts-reporting-bugs)=
### Reporting Bugs

Your comments, bug reports, patches and suggestions will help fix bugs and improve future releases. Please report bugs through Malone:

[launchpad.net/distros/ubuntu/+bugs/](https://launchpad.net/distros/ubuntu/+bugs/)


(6-06-lts-participate-in-ubuntu)=
### Participate in Ubuntu

If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

[www.ubuntu.com/community/participate/](http://www.ubuntu.com/community/participate/)


(6-06-lts-more-information)=
### More Information

You can find out more about Ubuntu on our website, IRC channel and wiki. If you're new to Ubuntu, please visit:

[www.ubuntu.com/](http://www.ubuntu.com/)

For the release notes for Kubuntu visit [wiki.ubuntu.com/DapperReleaseNotes/Kubuntu](http://wiki.ubuntu.com/DapperReleaseNotes/Kubuntu)

To sign up for future Ubuntu announcements, please subscribe to Ubuntu's announcement list at:

[lists.ubuntu.com/mailman/listinfo/ubuntu-announce](http://lists.ubuntu.com/mailman/listinfo/ubuntu-announce)

---
This document is maintained by the Ubuntu Documentation Team. Please feel free to contact us regarding any concerns or suggestions by either sending an email to [ubuntu-doc@lists.ubuntu.com](mailto:ubuntu-doc@lists.ubuntu.com) or by using any of the other methods on the [Ubuntu Documentation Team Contact Information Page](https://wiki.ubuntu.com/DocumentationTeam/Contact).
