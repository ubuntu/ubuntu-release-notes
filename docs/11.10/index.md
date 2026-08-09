---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/OneiricOcelot/ReleaseNotes -->

(ubuntu-11-10-release-notes)=
# Ubuntu 11.10 release notes

(11-10-introduction)=
## Introduction

These release notes for Ubuntu 11.10 (Oneiric Ocelot) provide an overview of the release and document the known issues with Ubuntu 11.10 and its variants.


(11-10-release-overview)=
## Release Overview

Oneiric Ocelot includes new releases of all major flavors of Ubuntu: desktop, server, cloud, Kubuntu, Xubuntu, Lubuntu, Edubuntu, Mythbuntu, and Ubuntu Studio. For Ubuntu, this release provides a full Unity experience, even without 3D hardware acceleration, promoting Unity 2D to the primary fallback shell. LightDM steps forward as the login manager for Ubuntu, Edubuntu, Xubuntu, Mythbuntu, and Ubuntu Studio. It also includes a customized Unity greeter. Kubuntu showcases the best and the newest features of the KDE Platform, Plasma Workspaces, and Applications (including the Muon Software Centre). Ubuntu Server introduces a technical preview of Juju - a modern approach to service deployment and orchestration on cloud and bare metal environments, and support for the ARM architecture.


(11-10-ubuntu)=
### Ubuntu


(11-10-new-features)=
#### New Features


(11-10-lenses-and-interface-changes)=
##### Lenses and Interface Changes

11.10 includes a new release of [compiz](http://www.compiz.org) and [Unity](http://unity.ubuntu.com).   Highlights of this release are:

* A new Alt+Tab switcher.

* "Places" are renamed to "Lenses". This feature now also integrates multiple sources and advanced filtering options like ratings, range, and categories.

* The Dash has a new music lens, linked to Banshee, that searches your personal and online music collections.

* Better performance of launchers and panel, ported to GTK 3 and GTK 3-based indicator stack.

* Full support for Chinese, Japanese, Korean, and other script languages.

Unity 2D reduces the delta with Unity, shares more code with it, and has an almost completed [accessibility support](http://ubuntuaccessibility.wordpress.com/2011/10/13/oneiric-ocelot) set of features. See [known issues](https://wiki.ubuntu.com/Known_issues) for the missing accessibility parts.

The indicators got a visual refresh that includes a refactoring of the session indicator and a new power indicator.

The [Ubuntu Font Family](http://font.ubuntu.com/), developed under the guidance of the [Dalton Maag](http://www.daltonmaag.com) type foundry and the [Canonical design team](http://design.canonical.com), has been expanded with Ubuntu Mono and Ubuntu Condensed.


(11-10-ubuntu-software-center-5-0)=
##### Ubuntu Software Center 5.0

11.10 includes Ubuntu Software Center 5.0, featuring a completely revamped interface that provides a simpler and more enjoyable experience for browsing, searching, and managing your software. The navigation tree view pane from previous Ubuntu Software Center versions has been replaced by a much cleaner toolbar approach for navigating between views.  Top-rated applications are now displayed prominently in the main view as well as in category views, leveraging the extensive database of excellent review data that has been provided over the past year by the Ubuntu community.

Application list views can now be dynamically sorted by top-rated, by name, and also by the date the application appeared in the Center. A dynamic banner has been added to the main view that will serve to highlight interesting new applications as well as themed collections. These banners will be updated regularly, and this, along with the dynamic What's New and Top Rated sections, should help to ensure an interesting and fun experience each time you open Software Center.

Last but not least, OneConf is now built in to keep your installed applications in sync between multiple computers. To activate it, use "File → Sync between computers…".


(11-10-new-arm-subarchitectures)=
##### New ARM subarchitectures

Ubuntu 11.10 introduces two new desktop images for ARM subarchitectures: armel+ac100 for the Toshiba ac100
netbook (NVIDIA Tegra 2 SoC), and armel+mx5 targeted at the Freescale i.MX53 Quick Start development board.  Both of these images are "best-effort" community-supported images aimed at developer and hobbyist use.


(11-10-revised-dvd-content)=
##### Revised DVD content

In Ubuntu 11.10 there is now a revised, smaller (in size) DVD based on community feedback over the last few cycles.  This new DVD has a more manageable size of 1.5G, and is an extension of our current CD image that includes all the language packs and some other useful applications, such as Inkscape, GIMP, Pitivi, and a more complete LibreOffice suite.  All the packages that used to be on the DVD are still available from the archive.


(11-10-new-app-developer-site)=
##### New App Developer Site

Coinciding with the Ubuntu 11.10 release, a significant milestone in the ongoing effort of making Ubuntu a target for application developers has also been reached: the Ubuntu App Developer site launch.

[developer.ubuntu.com](http://developer.ubuntu.com) should now be the central point of reference for any topics related to Ubuntu application development, from creation to publication: porting, sharing, contributing, and finding information. This site should grow organically to provide the tools, share knowledge, and act as the springboard for fostering application proliferation and developer community growth.

Read more in the [official announcement](http://developer.ubuntu.com/2011/09/announcing-the-ubuntu-app-developer-site/).


(11-10-new-localized-iso-tools)=
##### New Localized ISO Tools

Ubuntu now provides a set of tools for Ubuntu LoCo teams to create custom images to provide an experience even closer to the culture of the region they cover. After setting the foundations in Ubuntu 11.10, in the next cycle we plan to work with the community on expanding community usage. [Learn more](https://wiki.ubuntu.com/LocalizedImagesRollout).


(11-10-updated-applications)=
#### Updated Applications

[Thunderbird](http://www.mozilla.org/thunderbird/) is included as the default email client. This now includes menu and launcher integration via Unity.

Backups are easy in Ubuntu 11.10 now that [Déjà Dup](http://live.gnome.org/DejaDup) is included as the default backup tool. Securely store copies of your important data on a separate hard drive, cloud server, or even Ubuntu One.

The new [Gwibber](http://gwibber.com/) landed in Ubuntu 11.10, bringing improved performance and a new interface using the most recent GNOME technologies.

[GNOME 3.2](http://library.gnome.org/misc/release-notes/3.2/) is included and is a major upgrade from GNOME 2.32 included in Ubuntu 11.04.  GNOME Classic is no longer installed by default, but can be enabled after installation completes by installing `gnome-panel`. Note that the indicator status menus have not yet been ported to the new gnome-panel and the default upstream panel layout is used instead of the heavy Ubuntu customizations. GNOME Shell is also available for install.

Ubuntu now uses the  [LightDM](http://www.freedesktop.org/wiki/Software/LightDM) login manager with the Unity greeter.

Synaptic and Pitivi are no longer included in the default install but are still available in the Ubuntu repositories.


(11-10-ubuntu-server)=
### Ubuntu Server


(11-10-new-features-2)=
#### New Features

[Juju](http://juju.ubuntu.com) is available in Ubuntu 11.10 as a technical preview. Juju is a service deployment and orchestration framework developed by Canonical and used to deploy and manage services both on bare-metal and in the cloud. Through the use of what we call [charms](http://juju.ubuntu.com/Charms), juju provides you with shareable, re-usable, and repeatable expressions of DevOps best practices. You can use them unmodified, or easily change and connect them to fit your needs. Deploying a charm is similar to installing a package on Ubuntu: ask for it and it’s there, remove it and it’s completely gone.

[Orchestra](http://wiki.ubuntu.com/ServerTeam/Orchestra) is a collection of the best free software services for provisioning, deploying, hosting, managing, and orchestrating datacenter services.  Instead of manually setting up a complex network installation environment, users can now leverage Orchestra to rapidly deploy new servers into production. The process is standardized and fully automated, and thus minimizes manual intervention and ensures consistency. This solution is provided as a response to all user requests that we received for making multiple installs and deployments easier. The core component of Orchestra provisioning is [Cobbler](https://fedorahosted.org/cobbler/) and Juju.

Ubuntu Server 11.10 is the first release with support for the ARM architecture.  In this last cycle, the Ubuntu Server team worked closely with the Ubuntu ARM team to deliver a technical preview of ARM server support in Ubuntu Server 11.10.


(11-10-updated-applications-2)=
#### Updated Applications

Former UEC components (including Eucalyptus) are no longer part of the CD image and are no longer included in the security-supported `main` component of the archive. An upgrade path is provided from from 11.04.

The [Xen hypervisor](http://xen.org/) has now been reintroduced as an option in Ubuntu Server.


(11-10-ubuntu-cloud)=
### Ubuntu Cloud

Ubuntu 11.10 introduces the new Ubuntu Cloud Infrastructure and Ubuntu Cloud Guest images.  The [Cloud Infrastructure images](https://cloud-images.ubuntu.com) are the successor of the Ubuntu Enterprise Cloud and provide a ready to deploy Infrastructure-as-a-Services (IaaS) based on the [Openstack Diablo release](http://wiki.openstack.org/ReleaseNotes/Diablo).
Ubuntu Cloud Guest was previously known as JeOS or UEC-image. This Ubuntu Server image is specially tailored for use in a public or private cloud instance.
ARM cloud images are also being built. However, currently no cloud infrastructure can consume ARM cloud images properly. Therefore, these images are available on a best effort basis.

More information is available at [cloud-images.ubuntu.com](https://cloud-images.ubuntu.com).


(11-10-ubuntu-common-infrastructure)=
### Ubuntu Common Infrastructure


(11-10-hybrid-cd-usb-images-supported)=
#### Hybrid CD/USB images supported

All ISO images released with Ubuntu 11.10 are hybrid CD/USB images that can be written directly to a USB disk and booted without the use of special software.  Users who wish to enable persistent storage on a USB stick can still use the usb-creator tool to configure the USB stick.

(11-10-32-bit-compatibility-on-amd64-systems)=
#### 32-bit compatibility on amd64 systems

Ubuntu 11.10 provides "multiarch" support for installing 32-bit library and application packages on 64-bit systems.  For all amd64 installs and upgrades, select 32-bit software (like Skype and Flash), will now be installable directly using the same 32-bit packages that are used on i386 installations. You are not required to install the `ia32-libs` compatibility package.
For users, this change means that the 32-bit libraries will always be available at the same time as their 64-bit counterparts, even in the case of security updates, and users will only need to install those 32-bit libraries required by the user's application(s).


(11-10-linux-3-0-kernel)=
#### Linux 3.0 Kernel

Ubuntu 11.10 includes the 3.0.0-12.20 Ubuntu kernel which brings the 3.0 upstream kernel, the latest mainline release.  The Ubuntu kernel is based on the linux v3.0.4 [upstream stable kernel](http://kernel.org).

This kernel update brings a number of performance improvements both to ext4 (the default filesystem) and the process scheduler. This enhancement will improve interactive behavior and introduce support for newer hardware.

For the server, the kernel also brings the return of Xen dom0 support as a tech preview building towards full support for the 12.04 LTS Release.  It also has container and namespace improvements enabling full LXC support which is of particular interest on ARM platforms.  There are also a number of networking and netfilter improvements.

A note to application developers, the default number of file descriptors has been increased to simplify management of those programs that utilize very large numbers of files.

For the deeply technical, there are improvements to TCP and fragment identifier generations, btrfs has a number of significant improvements, ext4 has SMP scalability improvements, and the Big Kernel Lock is dead!


(11-10-upstart-1-3)=
#### Upstart 1.3

Ubuntu 11.10 features an update to [Upstart 1.3](http://upstart.at/2011/06/14/upstart-1-3-concordia-released/), with support for displaying boot-time status on servers and more reliable handling of legacy sysvinit scripts.


(11-10-gcc-4-6-toolchain)=
#### GCC 4.6 Toolchain

Ubuntu 11.10 includes gcc 4.6 as the default compiler.  The GCC packages are built from the 4.6-2011.07 [Linaro GCC](https://launchpad.net/gcc-linaro) release based on the [GCC 4.6.1 release](http://gcc.gnu.org/gcc-4.6/changes.html). See [ToolChain/CompilerFlags](https://wiki.ubuntu.com/ToolChain/CompilerFlags) for a summary of compiler defaults which are different from the upstream release.

The compiler passes by default two additional flags to the linker:

`-Wl,--no-copy-dt-needed-entries` is also known as `--no-add-needed`.  This option affects the treatment of dynamic libraries referred to by DT_NEEDED tags inside ELF dynamic libraries mentioned on the command line, and also has an effect on the resolution of symbols in dynamic libraries. This will be the default in the upcoming binutils-2.22 release.  This may result in build failures. More information and recipes how to fix such build failures can be found at
NattyNarwhal/ToolchainTransition and
[the corresponding Debian page](http://wiki.debian.org/ToolChain/DSOLinking#Not_resolving_symbols_in_indirect_dependent_shared_libraries).

`-Wl,--as-needed` with this option the linker will only add a DT_NEEDED tag for a dynamic library mentioned on the command line if if the library is actually used. A common build error with this option enabled is seen when libraries appear on the command line before objects that reference them.  More information and recipes how to fix such build errors can be found at NattyNarwhal/ToolchainTransition and
[the corresponding Debian page](http://wiki.debian.org/ToolChain/DSOLinking#Only_link_with_needed_libraries).


(11-10-python)=
#### Python

Default and available versions of Python have been updated as follows:

* Default: 2.7.2 (Ubuntu 11.04 had 2.7.1)
* Available: 2.6.7 (Ubuntu 11.04 had 2.6.6)
* Available: 3.2.2 (Ubuntu 11.04 had 3.2)

Python 3.1 has been removed (3.1.3 was available in Ubuntu 11.04).

The primary work done on Python this cycle was internal/developer-focused and not user visible.  We made the transition to [the dh_python2 helper](https://blueprints.launchpad.net/ubuntu/+spec/foundations-o-dhpython-transition) for packaging Python libraries and applications.  Previous Python helpers have all been deprecated in Debian, and in Ubuntu 11.10, all Python packages on all of our CD images now use the best-of-breed dh_python2.


(11-10-backports-are-now-more-easily-accessible)=
#### Backports are now more easily accessible

To enable users to more easily receive new versions of software, the Ubuntu Backports repository is now enabled by default. Packages from backports will not be installed by default — they must explicitly be selected in package management software. However, once installed, packages from backports will automatically be upgraded to newer versions.


(11-10-ubuntu-core)=
#### Ubuntu Core

Ubuntu Core is a new minimal rootfs for use in the creation of custom images for specific needs.  Developers will now be able to use Ubuntu Core as the basis for their application demonstrations, constrained environment deployments, device support packages, and other goals.  More information is available on the [Ubuntu Core wiki page](https://wiki.ubuntu.com/Core).


(11-10-ubuntu-one)=
### Ubuntu One

The new music lens in the Dash supports searching your personal and online music collections, as well as the Ubuntu One Music Store.

The [Déjà Dup](http://live.gnome.org/DejaDup) backup tool, shipped by default in Ubuntu, supports backing up to the Ubuntu One cloud.

Ubuntu One music collections are now streamed to Android and iOS devices, as well as supporting file sharing cross-platform compatibility with Windows.


(11-10-kubuntu)=
### Kubuntu

Kubuntu brings the latest and greatest from KDE and aims to provide a well-rounded  desktop suitable for all types of users.


(11-10-new-features-3)=
#### New Features

**Muon Software Center and Package Manager**, Kubuntu's new default appication management suite provides both user-friendly and power-user interfaces for package management.

**kubuntu-low-fat-settings** provides package which brings a collection of configuration settings that turn off some services, krunner plugins, and graphical effects which will allow Kubuntu to run on older, lower-end systems by reducing the memory footprint of the workspace.

**Technical Preview of OpenGL ES Powered Desktop Effects** For those adventurous and curious, Kubuntu 11.10 has packaged the work towards using a more compatible and reliable version of OpenGL, [OpenGL ES](http://en.wikipedia.org/wiki/OpenGL_ES).


(11-10-updated-applications-3)=
#### Updated Applications

**KDE 4.7.1** provides an entire selection updated software.

**Amarok 2.4.3** features native support for remote NFS and SMB/CIFS collections, a better looking user interface, support for gpodder.net, as well as vastly improved reliability.

**Kdepim 4.7.2** is the new Akonadi based pim suite that includes Kmail2. **Please see the [known issues section](https://wiki.ubuntu.com/OneiricOcelot/TechnicalOverview#Kubuntu-1) for problems relating to migrating pim data from previous versions to 11.10 and open issues associated with use of this re-engineered kdepim suite.**

**QtCreator 2.2.1** provides configurable mime types and code snippets, support for the Bazaar version control system as well as improved support for Qt Quick.

Please visit [kubuntu.org](http://kubuntu.org) for more information about Kubuntu, and see [Kubuntu's 11.10 release announcement](https://wiki.ubuntu.com/OneiricOcelot/Final/Kubuntu).


(11-10-xubuntu)=
### Xubuntu


(11-10-new-features-4)=
#### New Features

**gThumb** is now in the default Xubuntu 11.10 installation, to help users with image transformations and viewing.

**leafpad** is the new default text editor (instead of mousepad), and now includes the ability to print.

**pastebinit** is now included in Xubuntu 11.10 installations by default. If you need to use [paste.ubuntu.com/](http://paste.ubuntu.com/), you can use pastebinit in terminals to paste directly without copying and pasting the data.

**LightDM** is the new application that manages logins in Xubuntu 11.10.


(11-10-updated-applications-4)=
#### Updated Applications

**Onboard** (the onscreen keyboard) is now included in the default Xubuntu menus, under Accessories. For those who require an onscreen keyboard, this will be much easier to access using only a mouse or touchpad.

Xubuntu will continue to use **Synaptic Package Manager**, yet provides the Ubuntu Software Center for those who prefer it.

See the [Xubuntu 11.10 release announcement](https://wiki.ubuntu.com/Xubuntu/OneiricOcelot/Final).


(11-10-lubuntu)=
### Lubuntu

Lubuntu 11.10 is a brand new flavor of Ubuntu based on the Lightweight X11 Desktop Environment (LXDE) as its default GUI.  The goal is to provide a very lightweight distribution, with all the advantages of the Ubuntu world (repositories, support, etc.). Lubuntu is targeted at "normal" PC and laptop users running on low-specification hardware. The target user group for this flavor will be either those users who might not be proficient in using command line tools or those users who might not have enough resources for all the bells and whistles of the "full-featured" mainstream distributions.

With many LXDE components, [Lubuntu](http://lubuntu.net) also uses well-known applications, such as Chromium, Openbox, Pidgin, to name a few. The [Lubuntu project wiki](https://wiki.ubuntu.com/Lubuntu) contains more information on the project and the [applications used](https://wiki.ubuntu.com/Lubuntu/Applications).


(11-10-edubuntu)=
### Edubuntu

Edubuntu 11.10 inherits all the changes that occurred in the Ubuntu desktop.

This release of Edubuntu is better translated than ever before with all of our tools fully supporting translation.

If you want to try Edubuntu 11.10 without having to download our DVD, you can try it online on WebLive: [www.edubuntu.org/weblive](http://www.edubuntu.org/weblive)

To learn more about Edubuntu 11.10, go to: [www.edubuntu.org/](http://www.edubuntu.org/).


(11-10-new-features-5)=
#### New Features

There is a refreshed look and feel with new wallpaper and login screen.

The default desktop environment is now Unity with fallback to Unity 2D when the hardware doesn't support running the 3D version. Gnome 3 Fallback (which uses an updated gnome-panel) is available for those who want it as an option in the installer.


(11-10-updated-applications-5)=
#### Updated Applications

Updates in this release include:

* **gobby** was updated to gobby-0.5.
* **gbrainy** was updated to the latest and greatest version 2.

Default changes include:

* Nanny, Pessulus and Sabayon haven't been ported to Gnome 3.0/dconf yet and were consequently dropped from the default installation.


(11-10-mythbuntu)=
### Mythbuntu

11.10 is not a feature heavy release, but does bring in new HW support from the updated kernel and graphics stack.  It is leading up in preparation for the new Mythbuntu release strategy, LTS only releases starting with 12.04.


(11-10-new-features-6)=
#### New Features

**LightDM** is the new application that manages logins in Mythbuntu 11.10.

**Chromium** has been adapted by the Mythbuntu team to replace Firefox by default.

**Ubuntu Software Center** is now the default software installer instead of Synaptic, in line with the rest of Ubuntu.


(11-10-updated-applications-6)=
#### Updated Applications

**MythTV** has been updated to more recent builds. While MythTV is still on the 0.24 series, it has been growing more stable with each new build.


(11-10-ubuntu-studio)=
### Ubuntu Studio

Ubuntu Studio 11.10 is still working through our XFCE transition,  so some items or features might not be completely resolved yet.

More details can be found at: [UbuntuStudio/11.10release_notes](https://help.ubuntu.com/community/UbuntuStudio/11.10release_notes)


(11-10-new-features-7)=
#### New Features

**LightDM** is the new application that manages logins in Ubuntu Studio 11.10 and has a new background.

The menu will be different as the Ubuntu Studio team is moving towards a more DE agnostic way of handling categories and submenus.

The icon set has changed.


(11-10-updated-applications-7)=
#### Updated Applications

Many non-A/V/G specific applications, text editor for example, have changed to XFCE equivalent.  Unfortunately, because of low resource bandwidth the Ubuntu Studio Team was not able to complete the testing in this cycle and therefore deficiencies are expected and we apologize in advance.


(11-10-installation)=
## Installation


(11-10-overview)=
### Overview

Preparing your computer for Ubuntu is now much simpler, with a wider range of disk setup options. Each of these are detailed at length to provide you with a clear understanding of the actions that will take place with your selection.

You can now reinstall or upgrade an existing copy of Ubuntu with the Desktop CD installer, provided that your computer is connected to the Internet.


(11-10-download)=
### Download

Ubuntu 11.10 images can be downloaded from a location near you:

* [www.ubuntu.com/download](http://www.ubuntu.com/download) (Ubuntu and Ubuntu Server) .

In addition they can also be found at the following locations:

* [releases.ubuntu.com/11.10/](http://releases.ubuntu.com/11.10/) (Ubuntu, Ubuntu Server)

* [cloud-images.ubuntu.com/releases/11.10/](http://cloud-images.ubuntu.com/releases/11.10/) (Ubuntu Cloud Images)

* [cdimage.ubuntu.com/releases/11.10/](http://cdimage.ubuntu.com/releases/11.10/) (Ubuntu DVD, preinstalled ARM images, source)

* [cdimage.ubuntu.com/netboot/11.10/](http://cdimage.ubuntu.com/netboot/11.10/) (Ubuntu Netboot)

* [releases.ubuntu.com/kubuntu/11.10/](http://releases.ubuntu.com/kubuntu/11.10/) (Kubuntu)

* [cdimage.ubuntu.com/kubuntu/releases/11.10/](http://cdimage.ubuntu.com/kubuntu/releases/11.10/) (Kubuntu DVD)

* [cdimage.ubuntu.com/xubuntu/releases/11.10/](http://cdimage.ubuntu.com/xubuntu/releases/11.10/) (Xubuntu)

* [cdimage.ubuntu.com/edubuntu/releases/11.10/](http://cdimage.ubuntu.com/edubuntu/releases/11.10/) (Edubuntu)

* [cdimage.ubuntu.com/ubuntustudio/releases/11.10/](http://cdimage.ubuntu.com/ubuntustudio/releases/11.10/) (Ubuntu Studio)

* [cdimage.ubuntu.com/mythbuntu/releases/11.10/](http://cdimage.ubuntu.com/mythbuntu/releases/11.10/) (Mythbuntu)

* [cdimage.ubuntu.com/lubuntu/releases/11.10/](http://cdimage.ubuntu.com/lubuntu/releases/11.10/) (Lubuntu)


(11-10-system-requirements)=
### System Requirements

The minimum memory requirement for Ubuntu 11.10 is 384 MB of memory for Ubuntu Desktop.  Note that some of your system's memory may be unavailable due to being used by the graphics card. If your computer has only the minimum amount of memory, the installation process will take longer than normal; however, it will complete successfully, and the system will perform adequately once installed.

The minimum memory requirement for Ubuntu Server 11.10 is 128 MB of memory.

Systems with less memory may be able to select "Install Ubuntu" from the boot menu to run just the installer, rather than the whole desktop, or may be able to use the alternate install CD.


(11-10-upgrading)=
## Upgrading


(11-10-upgrading-from-ubuntu-11-04)=
### Upgrading from Ubuntu 11.04

To upgrade from Ubuntu 11.04 on a desktop system, press Alt+F2 and type in "update-manager -d" (sans quotes) into the command box. Update Manager should open up and display following message: "New distribution release '11.10' is available. Click Upgrade and follow the on-screen instructions".

To upgrade from Ubuntu 11.04 on a server system, follow the steps listed below:
Step 1: Install the `update-manager-core` package (if it is not already installed).
Step 2: Use following command `sudo do-release-upgrade -d` to launch the upgrade tool.
Step 3: Follow the on-screen instructions.
Note that the server upgrade is now more robust and will utilize GNU screen and automatically re-attach in case of dropped connection problems, for example.


(11-10-upgrading-from-other-releases)=
### Upgrading from Other Releases

Users of other Ubuntu releases need to upgrade first to 11.04, and then to 11.10.

For further information on upgrading to 11.04, please see the [Natty upgrade instructions](https://help.ubuntu.com/community/NattyUpgrades).


(downgrading-to-ubuntu-11-10)=
### Downgrading to Ubuntu 11.10

If you insert a bootable disk with Ubuntu 11.10 in a system running 12.04 and proceed through the installation process you will be presented with an option to "Upgrade from 12.04 to 11.10".  This option should not have appeared in the installer and it is not a recommended nor supported way to switch from a newer release of Ubuntu to an older one.  Additionally, no testing of this was performed during the development of 11.10.


(11-10-known-issues)=
## Known issues

The issues we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:


(11-10-boot-installation-and-post-installation)=
### Boot, installation, and post-installation

* Currently DVD support for the Macbook Pro (8,1) , (8,2) ,and (8,3) is unavailable, a fix is under investigation and possible workarounds are documented in the bug. (Bug:782389)

* When overwriting an existing installation in the Ubiquity desktop installer, it creates a new swap partition instead of re-using the already existing one. (Bug:782507)

* Ubiquity desktop installer proceeds to use free space without warning, if sufficient free space exists, and "install alongside" is selected, then clicking on the forward button just begins the installation without warning. (Bug:766265)

* omap3/omap4 netboot images are known to generate a too small boot partition. (Bug:806751)

* The "Memory test" mode is hanging indefinitely without any progress on some systems (confirmed on Dell Mini 10). (Bug:856055)

* Mac systems installed using manual partitioning may fail to boot if filesystem types other than ext2, ext3, or ext4 are used. (Bug:856763)

* A 'guided resize' partitioning leaves Mac systems unbootable.  The workaround is to boot using the live cd and choose the option to boot from the first disk, then install gpttools, run `gpttools /dev/sda`, and reboot. (Bug:856826)

* Chinese installs need to use the live environment instead of install only, to be able to type localized character. (Bug:871726)

* Selecting one of the stock images for the user picture will result in no user picture being set. (Bug:872966)

* Trying to install the ARM ac100 images from SD card to external USB key will fail, users wanting to use an external root filesystem should install from USB key to SD card instead (Bug:856278).

* Using the omap/omap4 netboot images you need to use the boot.img-[fb|serial].gz image file to actually get a proper bootloader partition (Bug:872525)

* In some corner cases the oem-config installer is not removed from ARM desktop images, it needs to be manually removed after system configuration has happened (Bug:856293)

* The images may show out of date, or inaccurate pending and security updates without first refreshing the cache with "sudo apt-get update".  This is due to the periodic check not being enabled.  It can be resolved by installing, "update-notifier-common" package. (Bug:870121)

* If you copy the Windows Installer for Ubuntu, wubi.exe, from an 11.10 disc to your Windows system and install from it, without having the 11.10 disc in your drive, 12.04 will be installed.  This issue exists on discs made by Canonical or on disc images that you may download for 11.10 and burn yourself.  This will not happen if you use wubi with the 11.10 CD in the drive.  (Bug:922330)


(11-10-upgrades)=
### Upgrades

* Ubuntu 11.10 has migrated away from /var/run, /var/lock and /dev/shm and now uses /run, /run/lock and /run/shm instead (respectively). While the Ubuntu AppArmor packages and shipped policy have been adjusted for this, custom policy may need to be updated. The following may be used to aid in migration (it allows both the old and the new paths):

```none

$ sed -i -e 's#/var/run#/{,var/}run#' -e 's#/var/lock#/{run,var}/lock#' -e 's#/dev/shm/#/{dev,run}/shm/#' <profile>
```

* In some cases,  update-manager crashed with RuntimeError in /usr/lib/python2.7/dist-packages/gi/overrides/Gtk.py: Gtk couldn't be initialized. (Bug:848915).

* Users of VMWare Workstation 8 or VMWare Player may experience boot problems. (Bug:858122)

* Any users who have updated to ubuntu 11.10 beta 1 and have not updated since then, may encounter the issue that 'apt-get update' returns non zero, although it does successfully update the Packages file.  In GUI tools, this translates to update-manager showing an error, but  it does display the updated apt and allow it to be installed. (Bug:871731)

* Users upgrading may encounter error messages from the installation of the new version of flashplugin-installer, due to some user connections (e.g. wifi, 3G) becoming unavailable during the upgrade process. It is recommended to proceed with upgrades while connected to a wired network to avoid this type of issue. (Bug:859373)

* Aptitude does not work on 64 bit systems without disabling multiarch in /etc/dpkg/dpkg.cfg.d/multiarch . (Bug:831768)


(11-10-graphics-and-display)=
### Graphics and Display

* We had to revert from unity-window-decorator to gtk-window-decorator for performance reasons. This means that the "1 px border" for resizing window is back temporarily.

* On Intel N10 Graphics, plugging in external monitor to VGA port makes both displays corrupted with thick slanted lines. (Bug:830949)

* Remote Desktop does not work with the -fglrx video driver, nor with the legacy nvidia drivers.  You can establish a connection but the remote screen does not update.  As a workaround use Unity2d, or switch to the free drivers or nvidia-current.  (Bug:772873)

* The Onboard window in Unity2d when maximized puts the window on top of everything and has no window controls when maximised as it refuses focus, and you can't double click the title bar to restore it. Once maximised your only real option is to switch to another workspace using a hard keyboard ctrl+alt+arrow keys then run gconf-editor and in the apps\onboard section change the height, or reboot into Unity3d and double click or drag down the top panel. (Bug:859288).

* Maximized windows can be accidentally closed from wrong monitor.(Bug:865701)

* Orca can't read what is going on with Unity3d. By default if you install using the screen reader you will boot into the Unity 2d desktop.

* For languages that are read right to left (arabic, hebrew), there is some inconsistency in display between the login screen (lightDM) and the desktop environment (unity). (Bug:871764)


(11-10-desktop)=
### Desktop

* The Skype website currently directs users to download a package for 64-bit Ubuntu 11.10 systems which is not compatible with multiarch.  Users are instead recommended to install the `skype` package via the Canonical partner archive using Software Center.  Alternatively, you can manually install this i386 package from the command line by running:` $ sudo apt-get install skype:i386 `

* Sometimes on Unity-2D gedit fails to start, this can be worked around by retrying to start it. (Bug:873027)

* Sometimes when locking the screen, a "num lock is on" warning may appear even though num lock isn't actually on. (Bug:841541)

* Banshee sadly does not work on the ARM desktop images, Rhythmbox is shipped alongside to enable music playing on this architecture (Bug:857299)


(11-10-kernel)=
### Kernel

* Sandy Bridge power regression from kernel 3.0.0-6 to 3.0.0-7 (30% more power at idle) (Bug:818830) -- Platforms affected by this power consumption regression are sixth generation i915 GPUs having the following PCI identifiers: 8086:0102, 8086:0112, 8086:0122, 8086:0106, 8086:0116, 8086:0126, 8086:010A. These displays are typically found in SandyBridge mobile and desktop platforms.

* On ARM omap imagesd the networking support for the Beagle XM board is broken (Bug:838200)


(11-10-ubuntu-server-2)=
### Ubuntu Server

* When running an i386 system under a virtual machine without enough memory allocated a kernel error is detected during installation. (Bug:790712)

* iSCSI root installation creates manual eth0 configuration and a slow boot. A fix for this is in development and will be available shortly. (Bug:870214)


(11-10-ubuntu-cloud-2)=
### Ubuntu Cloud

* Cloud instances and servers pre-seeded with cloud-init will have their FQDN written to /etc/hosts and pointed to the IP 127.0.1.1. This may cause issues for daemons which try to listen on their hostname, rather than 0.0.0.0, as they will now only be reachable locally, rather than on the network address that their FQDN resolves to.(Bug:871966)


(11-10-kubuntu-2)=
### Kubuntu

_ Kmail migration fails (Bug:857828). You will need to delete your ~/.kde/share/config/kmail-migratorrc file, and run the migrator manually - _kmail-migrator --interactive* or skip the migration tool and reconfigure Kmail from scratch.

* Shutdown in the live session under VirtualBox sometimes does not work and seems to just hang on the desktop. Just restart the computer with the power button in that case, there is no possibility of data loss. (Bug:805906)

* A window may retain a taskbar entry after closing the application. [(KDE Bug 275469)](https://bugs.kde.org/show_bug.cgi?id=275469):

* Kmail/Kontact cannot reliably retrieve email after a suspend resume cycle. Sometimes after resume, instead of displaying messages, "Retrieving folder contents, please wait" will be persistently displayed. If this occurs, use the Akonadi Server Configuration control module to restart Akonadi. That should resolve this issue. Restarting Kontact/Kmail will not. To access the control module use the search function in Kickoff (K menu) or Quicksand (alt-F2) to find it.(Bug:862483)


(11-10-xubuntu-2)=
### Xubuntu

* When using the new plymouth splash screen, occasionally using the desktop cd to install, the message "hit any key to continue" does not appear. Should you get a black screen with text and the sliding throbber, when the throbber stops moving and the cd ejects, remove the cd and hit enter on the keyboard to continue.(Bug:872472)

* There is no screen title or headings when choosing "Install Xubuntu"  from the CD menu (Bug:840094)

* When Gnome Services is checked, Onboard Keyboard will be started automatically as the user logs in. (Bug:872515)


(11-10-edubuntu-2)=
### Edubuntu

* As Edubuntu includes a standard Ubuntu desktop, most of the issues above also apply to Edubuntu

* Advanced package selection doesn't appear in some languages. As a workaround, simply remove the packages you don't want once your system is installed. (Bug:872727)


(11-10-ubuntu-core-2)=
### Ubuntu Core

* DRM libraries are always installed, even for users who are not enabling graphical environments (Bug:819802)


(11-10-lubuntu-2)=
### Lubuntu

* In some cases, Lubuntu desktop ISO boot to a terminal prompt instead of the desktop session. You can manually start the session by typing "sudo start lxdm" (Bug:854837)

* Ubiquity require more than 4 Gb of free space to install, please use alternate ISO if you are in this case (Bug:819538)

* Keyboard layout can't be saved using LXKeymap. Please run "sudo dpkg-reconfigure keyboard-configuration" (Bug:729880)

* On persistent mode, items created on the desktop are not displayed until next reboot. (Bug:837470)

**For a listing of more known issues, please refer to the Oneiric Ocelot [bug tracker](https://bugs.launchpad.net/ubuntu/oneiric/+bugs) in Launchpad.**


(11-10-reporting-bugs)=
## Reporting bugs

Your comments, bug reports, patches and suggestions will help fix bugs and improve the quality of future releases. Please [report bugs using the tools provided](http://help.ubuntu.com/community/ReportingBugs).

If you want to help out with bugs, the [Bug Squad](http://wiki.ubuntu.com/BugSquad) is always looking for help.


(11-10-participate-in-ubuntu)=
## Participate in Ubuntu

If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

[www.ubuntu.com/community/participate/](http://www.ubuntu.com/community/participate/)


(11-10-more-information)=
## More information

You can find out more about Ubuntu on the [Ubuntu website](http://www.ubuntu.com) and [Ubuntu wiki](http://wiki.ubuntu.com).

To sign up for future Ubuntu development announcements, please subscribe to Ubuntu's development announcement list at:

[lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce](http://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce)
