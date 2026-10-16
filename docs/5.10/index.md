---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/BreezyReleaseNotes -->

(ubuntu-5-10-release-notes)=
# Ubuntu 5.10 release notes

Ubuntu is a Linux distribution for your desktop or server, with a fast and easy install, regular releases, a tight selection of excellent applications installed by default, and almost any other software you can imagine available through the network. Ubuntu provides security updates for 18 months after each release, and professional technical support is available from many companies around the world.

These Release Notes cover new features in Ubuntu 5.10, download and installation notes, known issues, and frequently asked questions. Please read these notes before, during, and after installation and configuration of Ubuntu 5.10, and before reporting bugs in [Bugzilla](http://bugzilla.ubuntu.com).

We hope you enjoy Ubuntu 5.10.

---

## What's new

Ubuntu is released regularly and predictably. Since our April 2005 release (Ubuntu 5.04), we've made a lot of improvements to give you the best Linux experience possible. Here's what's new with Ubuntu 5.10:

### On the Desktop

* GNOME 2.12.1
* OpenOffice.org 2.0 beta 2
* X.org 6.8.2 with wider hardware support
* An enhanced tool for easily installing new applications (see *Add Applications* on the Applications menu)
* A new tool which makes it easy to install support for multiple languages (*Language Selector*)
* Editable GNOME menus with *SMEG* (Simple Menu Editor for GNOME)
* Applications are now linked into the Launchpad infrastructure (new entries on the Help menus for translation and support)
* Support for writing audio CDs (*Serpentine*)
* Graphical boot process with progress bar (*USplash*)
* New documentation (*Ubuntu 5.10 Starter Guide*)
* Language packs with updates from the Rosetta translation platform, which makes contribution of translations easy for everybody

### On the Server

* Plone 2.1 and Zope 2.8.1
* PHP5
* Support for installing directly onto LVM volumes
* Built-in thin client functionality produced in cooperation with the LTSP project
* Simple NFS root setup with automatic hardware detection through initramfs-tools
* Support for up to 4 gigabytes of RAM by default on 32-bit architectures
* Kernel support for cluster filesystems (OCFS2 and GFS)

### Hardware Support Improvements

* Linux 2.6.12.6 with many updated drivers from third parties
* Further enhancements to laptop support (hot keys, and working suspend/resume on more models)
* All-in-one printer/scanner devices from Hewlett-Packard (HP) are supported out of the box
* Bluetooth input devices (such as keyboards and mice) are supported out of the box
* Multiple audio devices are handled more gracefully (and one can easily select the default device)
* 64-bit kernel for PowerPC

### Installation

* A new OEM mode to simplify the process of preinstalling Ubuntu on computers for resale or redistribution
* Automatically makes existing hard drive partitions available to the desktop
* Simple "dual boot" configuration with automatic resizing of an existing installed OS
* The second stage of the installation now has a progress bar

### "Under the hood"

* GCC 4.0.1
* glibc 2.3.5
* New early userspace infrastructure based on initramfs-tools
* More modular X.org packaging
* Python 2.4.2

As always, Ubuntu includes the very best of the 100% free/libre application software world, and each new release incorporates countless new features and bugfixes from the global development community.

## Downloading and Installing

Ubuntu 5.10 supports three (3) major architectures: Intel x86, AMD64, and PowerPC. Depending on your needs, you might manage with less than some of the recommended hardware listed in the table below. However, most users risk being frustrated if they ignore these suggestions.

Table 1 Recommended Minimum Requirements

| **Install Type** | **RAM**       | **Hard Drive Space** |
| Desktop          | 128 megabytes | 2 gigabytes          |
| Server           | 64 megabytes  | 500 megabytes        |

Here are some common Ubuntu 5.10 system configurations. Once again, the size of the installation will greatly depend on the software you install during setup. For most users, the default applications are suitable enough for general use.

**Desktop**

A standard desktop box, including the X Window System, full desktop environment, sound, office suite, email clients, etc. You'll need about 2 gigabytes of hard drive space using the standard desktop task.

**Server**

This is a small server profile, which provides a common base for all sorts of server applications. It's minimal and designed to have the desired services added on top, such as file/print services, web hosting, email hosting, etc. For these services at least 500MB of disk space will suffice, but consider adding more space depending on the services you'd like to host with your server.

Remember that these sizes don't include all the other materials which are usually to be found, such as user files, mail, and data. It is always best to be generous when considering the space for your own files and data.

### Downloading Ubuntu 5.10

You can download Ubuntu 5.10 from the following mirrors located worldwide:

* United States: [us.releases.ubuntu.com/releases/5.10/](http://us.releases.ubuntu.com/releases/5.10/)
* Europe: [se.releases.ubuntu.com/5.10/](http://se.releases.ubuntu.com/5.10/)
* United Kingdom: [releases.ubuntu.com/5.10/](http://releases.ubuntu.com/5.10/)
* Rest of the World: [releases.ubuntu.com/5.10/](http://releases.ubuntu.com/5.10/)

You can also download all architecture types of Ubuntu 5.10 using BitTorrent and Jigdo.

### Requesting for Free Ubuntu 5.10 CDs

Ship-It will mail pressed CDs worldwide free of charge. To receive a complimentary copy of the Official Ubuntu 5.10 CD -- or a handful of them to give to your friends, your school or LUG -- place your request at:

[shipit.ubuntu.com/](http://shipit.ubuntu.com/)

### Installing Ubuntu

Once you have a copy of Ubuntu 5.10, follow these instructions to install:

**Default Mode**

The default installation mode provides the best computing experience with Ubuntu 5.10. You'll have a fully-functioning desktop with the default settings. Make sure your computer meets the recommended minimum requirements when installing in Default Mode.

1. Place the Ubuntu 5.10 Install CD in the CD-ROM Drive and power on the computer.
2. At **boot:**, press Enter.
3. The Ubuntu 5.10 installer will run. Follow the on-screen instructions to start the installation.
4. Once the installation is complete, the login screen will appear and you are able to log in to use Ubuntu 5.10

**Server Mode**

The Server Mode provides a base system suitable for installing server applications. You can add more services as needed after installation. Make sure your computer meets the recommended minimum requirements when installing in Server Mode.

1. Place the Ubuntu 5.10 Install CD in the CD-ROM Drive and power on the computer.
2. At **boot:**, type *server*, and press Enter.
3. The Ubuntu 5.10 installer will run. Follow the on-screen instructions to start the installation.
4. Once the installation is complete, you will be informed that Ubuntu 5.10 is ready for use.

**OEM Mode**

Ubuntu 5.10 can be pre-installed to computers for resale and redistribution. Make sure the computer meets the recommended minimum requirements when installing in OEM Mode.

1. Place the Ubuntu 5.10 Install CD in the CD-ROM Drive and power on the computer.
2. At **boot:**, type *oem* and press Enter.
3. The Ubuntu 5.10 installer will run. Follow the on-screen instructions to start the installation.
4. Once the installation is complete, you will be informed that Ubuntu 5.10 has been fully installed and the computer is ready for shipping.
5. You can also run a system test to check if the installation of Ubuntu 5.10 OEM mode went smoothly. The system test will run the Ubuntu Hardware Database and will check if your hardware is configured correctly.
6. You will now be presented with a login screen, at which you can log in as the **oem** user using the password you selected earlier in the installation, and make additional modifications to the system as required before shipping. Note that the **oem** user will be deleted on the end user's first boot.
7. On the first boot after installation, the end user will be asked to select a language, keyboard layout, time zone configuration, and create the first user account. The first user account created has administrative rights via sudo. Since Ubuntu 5.10 is a multi-user system, the end user can create more user accounts as needed.

## Known Issues

* Installations on powerpc with /boot on an XFS filesystem will fail to boot ([bug 14485](http://bugzilla.ubuntu.com/show_bug.cgi?id=14485)). To work around this, use a different filesystem for /boot, such as ext3.
* Upgrades from 5.04 (Hoary) using Swiss German or Swiss French keyboard layouts -- de_CH and fr_CH respectively -- in combination with other layouts, will result in a 'cannot set keyboard configuration' dialog, and a standard US PC-104 keymap will be used.  To work around this, go into the GNOME keyboard selector, and remove and re-add the offending layout.
* Attempting to use multiple layouts added from within the GNOME keyboard selector will fail ([bug 15372](http://bugzilla.ubuntu.com/show_bug.cgi?id=15372)).  To work around this, select another option than 'Both Alt keys together change group' in the 'Group Shift/Lock behaviour' group of the Layout Options tab in the keyboard selector, such as 'Both Ctrl keys together change group'.
* SDL and OpenAL audio will default to OSS output, which may cause audio output issues ([bug 16444](http://bugzilla.ubuntu.com/show_bug.cgi?id=16444)).  To work around this, install the libsdl1.2debian-alsa package from universe.

## Frequently Asked Questions

* Where did the Terminal go?
  * Not on the desktop context menu anymore. Install nautilus-open-terminal if you want it.
  * Menu entry has moved to 'Applications → Accessories'

* Where do I put my updated DSDT?
  * As of the Ubuntu 5.10 release, DSDT files are placed in /etc/mkinitramfs/DSDT.aml.
  * Run the command "sudo dpkg-reconfigure linux-image-$(uname -r)" to make this take effect.

You can read more in-depth FAQs in the Ubuntu 5.10 Starter Guide.

## Getting Help and Technical Support

Ubuntu 5.10 gives users an easy way to get help in most applications installed by default. Once you have an active internet connection, from an open application, just click on Help → Get Help Online  and you'll be directed to an online webpage that gives you help and support options for the application.

Technical Support for Ubuntu 5.10 is available from a variety of sources: from the community, from Canonical Ltd, from recognized organizations, and from developers directly through open web forums, mailing lists and IRC channels:

* [www.ubuntu.com/support](http://www.ubuntu.com/support)

If you have a question, or if you think you may have found a bug but aren't sure, first try asking on the #ubuntu IRC channel on Freenode, on the Ubuntu Users mailing list, or on the Ubuntu forums:

* [lists.ubuntu.com/mailman/listinfo/ubuntu-users](http://lists.ubuntu.com/mailman/listinfo/ubuntu-users)
* [www.ubuntuforums.org](http://www.ubuntuforums.org)

## Reporting Bugs

Your comments, bug reports, patches and suggestions will help fix bugs and improve future releases. Please report bugs through Bugzilla:

[bugzilla.ubuntu.com/](http://bugzilla.ubuntu.com/)

## Participate in Ubuntu

If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

[www.ubuntu.com/community/participate/](http://www.ubuntu.com/community/participate/)

## More Information

You can find out more about Ubuntu and about the 5.10 release on our website, IRC channel and wiki. If you're new to Ubuntu, please visit:

[www.ubuntu.com/](http://www.ubuntu.com/)

To sign up for future Ubuntu announcements, please subscribe to Ubuntu's announcement list at:

[lists.ubuntu.com/mailman/listinfo/ubuntu-announce](http://lists.ubuntu.com/mailman/listinfo/ubuntu-announce)
