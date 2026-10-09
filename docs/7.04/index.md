---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/7.04Tour -->

(ubuntu-7-04-release-notes)=
# Ubuntu 7.04 release notes

## Introduction

The Ubuntu community have been working to bring you the latest and greatest software the Open Source Community has to offer. This is Ubuntu 7.04 and it comes packed with a host of new features including data migration from Windows, new and easier ways to install multimedia codecs, binary drivers, as well as networking improvements and of course, GNOME 2.18, the 2.6.20 kernel and more.

## Ubuntu Desktop

Ubuntu 7.04 is the most user-friendly Ubuntu to date and includes a ground-breaking Windows migration assistant, excellent wireless networking support and improved multimedia support.

### Migrate your data

Windows migration tool - The new migration tool recognises Internet Explorer favorites, Firefox bookmarks, desktop wallpaper, AOL IM contacts, Yahoo IM contacts and imports them in Ubuntu. This offers easier and faster migration for new users of Ubuntu and individuals wanting to run a dual partition.  In addition to single accounts, you can migrate several users' settings in Ubuntu.

### Easy installation of multimedia codecs

Playing an MP3 or other media file just got a lot easier. If the required pieces are not yet installed, 7.04 will get the correct codecs for you, no more searching and no need for long and complicated instructions.

### Desktop Effects

Stunning new desktop effects are available as a technology preview for users who choose to enable them. They remain turned off by default, for the benefit of users with older or less powerful chips and certain non-supported graphics cards.

### Networking Improvements

#### Easier connection to wireless networks

New in 7.04 is Network Manager, a simple way to find and connect to wireless and wired networks. With a single click, view all the available wireless networks and their strengths. For those on a secured network, WPA support is built in right out of the box.

#### Zeroconf for instant networks

For those times without a router or any existing network, 7.04 includes the ability to connect instantly, via Avahi, a free Zeroconf implementation. It allows programs to publish and discover services and hosts running on a local network with no configuration. It also allows easy connection to network printers, music shares, and much more.

### Easier install of proprietary drivers

The new Restricted Drivers Manager allow users to easily install and manage proprietary drivers for wireless and video graphics cards and other hardware that may not have completely Free drivers.

### New Artwork

Ubuntu 7.04 features all new artwork; check out the new Desktop Background image, and a boot-up splash image that has more 'bling'. The new theme also includes a polished icon set.

### Easy Third Party Installation

Installation of popular third party software has never been easier. With a click of a button you can now install Java, Flash and other commonly-requested applications.

### Better debugging of crashes

For those times when programs crash, 7.04 builds in a new tool to catch the data about that crash and make certain all the right information gets to the developers, making a better Ubuntu experience for all.

### Xorg 7.2 included

Keeping in step with the cutting edge mentality, X11R7.2, the third release of the modular X Window system, is used in this release.  X11R7.2 comes with significant stability and correctness fixes, including improved auto-configuration heuristics, enhanced support for GL-based compositing managers such as Compiz and Beryl, and improved support for PCI systems with multiple domains. It also incorporates the new, more extensible XACE security policy framework.

### New Games: Sudoku and Chess

With a change of maintainers in gnome-games, the plea for new and more exciting games was heard. After [two surveys](http://www.gnome.org/projects/gnome-games/survey.html), one to figure out which game to remove and another to determine to which one to add, two winners emerged: [gnome-sudoku](http://live.gnome.org/GnomeSudoku) and [glchess](http://live.gnome.org/glChess). Both of these games have now been added to gnome-games 2.17 and you can find them under **Applications > Games > Chess** or **Sudoku**. Of course, one game did get axed. Sadly Ataxx, a game similar to Reversi and Othello, didn't make it.

### Quick diagnostic tools

Disk Usage Analyzer allows you to easily view disk usage statistics in a more intuitive manner.

### Help Center

In order to make Help more accessible, 7.04 features a brand new Help Center with an easier to use interface that is more stylish.

### Support for more hardware, including Intel Macs

As with every new release, 7.04 comes with support for new hardware, including better support for laptops and newer peripherals. Printing support has also been updated, to support more features and newer printers.

## Server Edition

Ubuntu 7.04 Server Edition adds support for hardware facilities that speed up the use of virtual machines as well as other improved hardware support, making it an excellent choice as a web, database, mail, file and print server, the fastest growing area of Linux server use.

### Kernel

Virtualization support: KVM (the Kernel-based Virtual Machine) is included in Ubuntu 7.04, which takes advantage of the virtualization capabilities of recent Intel and AMD processors. Each virtual machine has private virtualized hardware: a network card, disk, graphics adapter, and so on.

The 7.04 kernel is also VMI enabled, for improved performance when running on VMware hypervisors. VMI paravirtualization can be enabled in VMware Workstation 6.0 beta.

### LTSP 5.0

With 7.04 comes LTSP 5.0, the new version of LTSP originally written for Ubuntu from 5.04 onwards.  The new LTSP allows for easier client deployment and management. Improvements include easier software installation, GUI client management and much more, leaving a highly integrated system that is easier to use.

### Mail Server Improvements

Postfix has been updated to the current 2.3 series release, 2.3.8 and 7.04 also includes support for queuegraph, a mail statistics RRDtool front end for Postfix that produces daily, weekly, monthly and yearly graphs of Postfix's active, deferred, incoming and bounce queues and python-policyd-spf and postfix-policyd-spf-perl, Sender Policy Framework (SPF) servers.

### New Apache 2.2

7.04 comes with the new Apache 2.2, containing improvements to caching and configuration, larger file support, more graceful stopping and much more.

### The latest SQL databases

For those using PostgreSQL or MySQL, 7.04 includes PostgreSQL 8.2 and MySQL 5.0.38. Both feature a heavy focus on performance and administration improvements. The full release notes for PostgreSQL 8.2 can be read at [www.postgresql.org/docs/8.2/static/release-8-2.html](http://www.postgresql.org/docs/8.2/static/release-8-2.html) and MySQL 5.0.38 can be read at [dev.mysql.com/doc/refman/5.0/en/releasenotes-es-5-0-38.html](http://dev.mysql.com/doc/refman/5.0/en/releasenotes-es-5-0-38.html)

### Installer for SPARC64

With 7.04 comes improvements to Ubuntu's support for the SPARC architecture, including the ability to automatically install an OpenSSH server in the installation process and support in the boot loader for other operating systems.

### Suggestions for uninstalled commands

If the package needed for a specific command is not found, 7.04 will now prompt you with the needed package, even if it is part of a larger metapackage.

## Download 7.04

Get it while it's hot. ISO CD images and torrents are available at:

* [releases.ubuntu.com/feisty/](http://releases.ubuntu.com/feisty/) (Ubuntu)
* [releases.ubuntu.com/kubuntu/feisty/](http://releases.ubuntu.com/kubuntu/feisty/) (Kubuntu)
* [releases.ubuntu.com/edubuntu/feisty/](http://releases.ubuntu.com/edubuntu/feisty/) (Edubuntu)
* [cdimage.ubuntu.com/xubuntu/releases/feisty/](http://cdimage.ubuntu.com/xubuntu/releases/feisty/) (Xubuntu)
* [cdimage.ubuntu.com/ports/releases/feisty/](http://cdimage.ubuntu.com/ports/releases/feisty/) (PowerPC, IA-64, SPARC)

### Reporting Bugs & Testing

Feisty Fawn has bugs! Your comments, bug reports, patches and suggestions will help fix bugs and improve future releases. After reading [help.ubuntu.com/community/ReportingBugs](https://help.ubuntu.com/community/ReportingBugs) please report bugs through Malone.

If you want to help out with those bugs, the Bug Squad team in Launchpad is always looking for help.

### Get Involved in Ubuntu

If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

* [www.ubuntu.com/community/participate/](http://www.ubuntu.com/community/participate/)

### More Information

You can find out more about Ubuntu on our [website](http://ubuntu.com) and [wiki](http://wiki.ubuntu.com).

To sign up for future Ubuntu development announcements, please subscribe to Ubuntu's development announcement list at:

* [lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce](http://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce)

### Feedback