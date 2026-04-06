---
tocdepth: 3
---

(ubuntu-17-04-release-notes)=
# Ubuntu 17.04 "Zesty Zapus" Release Notes

<!-- Source: https://wiki.ubuntu.com/ZestyZapus/ReleaseNotes -->

## page was copied from YakketyYak/ReleaseNotes
## page was copied from XenialXerus/ReleaseNotes
## When adding features to this page, please add credits for the relevant upstream developers where appropriate.
||<tablestyle="float:right; width:40%; background:#F1F1ED; margin: 0 0 1em 1em;" style="padding:0.5em;">'''Table of Contents'''<<BR>> <<TableOfContents(3)>>||

'''WARNING: Release reached End of Life'''

'''This release is no longer supported, please see [[Releases]]'''

'''WARNING: Release reached End of Life'''


= Introduction =

These release notes for '''Ubuntu 17.04''' (Zesty Zapus) provide an overview of the release and document the known issues with Ubuntu 17.04 and its flavors.

=== Support lifespan ===
Ubuntu 17.04 was supported for 9 months until [[Releases|January 2018]]. 

=== Official flavour release notes ===
Find the links to release notes for official flavors [[#Official_flavours|here]].

<<BR>>
= Get Ubuntu 17.04 =
== Download Ubuntu 17.04 ==

Images can be downloaded from a location near you.

You can download ISOs and flashable images from from:

http://releases.ubuntu.com/17.04/ (Ubuntu Desktop and Server) <<BR>>
http://cdimage.ubuntu.com/ubuntu/releases/17.04/release/ (Less Popular Ubuntu Images) <<BR>>
http://cloud-images.ubuntu.com/releases/17.04/release/ (Ubuntu Cloud Server) <<BR>>
http://cdimage.ubuntu.com/netboot/17.04/ (Ubuntu Netboot) <<BR>>
http://cdimage.ubuntu.com/kubuntu/releases/17.04/release/ (Kubuntu) <<BR>>
http://cdimage.ubuntu.com/lubuntu/releases/17.04/release/ (Lubuntu) <<BR>>
http://cdimage.ubuntu.com/ubuntu-budgie/releases/17.04/release/ (Ubuntu Budgie) <<BR>>
http://cdimage.ubuntu.com/ubuntu-gnome/releases/17.04/release/ (Ubuntu GNOME) <<BR>>
http://cdimage.ubuntu.com/ubuntukylin/releases/17.04/release/ (Ubuntu Kylin) <<BR>>
http://cdimage.ubuntu.com/ubuntu-mate/releases/17.04/release/ (Ubuntu MATE) <<BR>>
http://cdimage.ubuntu.com/ubuntustudio/releases/17.04/release/ (Ubuntu Studio) <<BR>>
http://cdimage.ubuntu.com/xubuntu/releases/17.04/release/ (Xubuntu) <<BR>>
##http://cdimage.ubuntu.com/mythbuntu/releases/17.04/ (Mythbuntu) <<BR>>
##http://cdimage.ubuntu.com/edubuntu/releases/17.04/ (Edubuntu DVD) <<BR>>

== Upgrading from Ubuntu 16.10 ==
To upgrade on a desktop system:
 * Open the "Software & Updates" Setting in System Settings.
 * Select the 3rd Tab called "Updates".
 * Set the "Notify me of a new Ubuntu version" dropdown menu to "For any new version".
 * Press Alt+F2 and type in "update-manager -c" (without the quotes) into the command box.
 * Update Manager should open up and tell you: New distribution release '17.04' is available.
  * If not you can also use "/usr/lib/ubuntu-release-upgrader/check-new-release-gtk"
 * Click Upgrade and follow the on-screen instructions.

To upgrade on a server system:
 * Install the {{{update-manager-core}}} package if it is not already installed.
 * Make sure the {{{Prompt}}} line in /etc/update-manager/release-upgrades is set to normal.
 * Launch the upgrade tool with the command {{{sudo do-release-upgrade}}}.
 * Follow the on-screen instructions.
Note that the server upgrade will use GNU screen and automatically re-attach in case of dropped connection problems.

There are no offline upgrade options for Ubuntu Desktop and Ubuntu Server. Please ensure you have network connectivity to one of the official mirrors or to a locally accessible mirror and follow the instructions above.

<<BR>>
= New features in 17.04 =

## Please see the [[https://blueprints.launchpad.net/ubuntu/zesty/+specs|Zesty blueprint list]] for details.

 * For other changes since 16.04 LTS, see the [[YakketyYak/ReleaseNotes|16.10 Release Notes]].

== 32-bit PowerPC Support Dropped ==

  * The '''powerpc''' port is not included in the 17.04 release. See [[https://lists.ubuntu.com/archives/ubuntu-devel-announce/2016-December/001199.html|announcement]] for details.
  * '''ppc64el''' support support continues as previously.

== Networking ==

  * The default DNS resolver is now '''systemd-resolved'''.

== Swap ==

 * For new installs, a '''swap file''' will be used instead of a swap partition.

== Updated Packages ==

=== Linux kernel 4.10 ===

Ubuntu 17.04 is based on the Linux release series '''4.10'''.

== Driverless Printing ==

We now support printers which allow printing without printer-specific drivers. These printers are [[http://www.pwg.org/dynamo/eveprinters.php|IPP Everywhere]] and [[https://support.apple.com/en-us/HT201311|Apple AirPrint]] printers, but also some PDF, Postscript, and PCL printers work. This way connecting a printer gets as easy as connecting a USB stick.

 * The printers can get connected via network or USB.
 * The setup of IPP Everywhere and Apple Airprint printers should occur fully automatically. You only need to plug in your USB printer or connect your network printer to the local network.
 * If you do not want to set up IPP network printers automatically edit /etc/cups/cups-browsed.conf to have a line "CreateIPPPrinterQueues No", and if you also want suitable PDF, Postscript, or PCL printers automatically set up have a line "CreateIPPPrinterQueues All". Reboot after modifying /etc/cups/cups-browsed.conf.
 * For manual setup of driverless network printers with system-config-printer, choose the printer under the discovered network printers and then "IPP network printer via DNS-SD", or "Driverless IPP" in the "Connections" list (In the "Select Device" step). In the [[http://localhost:631|CUPS web interface]] look for "driverless" in the discovered network printers entries and also for "driverless" in the make/model/driver choice.
 * On driverless USB printers (IPP-over-USB) you find the web administration interface under [[http://localhost:60000/|http://localhost:60000/]] (if more than one printer is connected, the other ones are on port 60001, 60002, ...). It is highly recommended to access the interface with Firefox.
 * If you have a WiFi printer which does not allow to configure the WiFi access by its front panel, try to connect it via USB. If it is an IPP-over-USB printer you can configure it by its [[http://localhost:60000/|web interface]] now and then disconnect USB and use WiFi.
 * If you have an HP multi-function device with scanner, prefer using it with the HPLIP driver as you were used to. When using in driverless mode you will not be able to scan. system-config-printer takes automatically care of this.
 * If you have a multi-function device with scanner and the scanner is not supported by simple-scan/xsane/SANE, look for a scanning function in the web administration interface. Thanks to IPP-over-USB this will also be possible with many USB-connected devices.
 * Driverless printing is supported on both Ubuntu Desktop and Ubuntu Server.

== Ubuntu Desktop ==

 * '''!LibreOffice''' has been updated to [[https://wiki.documentfoundation.org/ReleaseNotes/5.3|5.3]].
 * Apps provided by GNOME have been updated to '''3.24'''. Exceptions are the Nautilus file manager (3.20), Terminal (3.20), Evolution (3.22), and Software (3.22).
 * The Calendar app now has a '''Week''' view.
 * '''gconf''' is no longer installed by default since it has long been superseded by gsettings. Note that statistics and preferences for the Aisleriot card games will be reset when upgrading to 17.04.
 * Unity 8 is available as an alternative session


== Ubuntu Server ==

=== qemu 2.8 ===

Qemu has been updated to the 2.8 release.

See the [[http://wiki.qemu.org/ChangeLog/2.8|Changelog]] for details.

=== libvirt 2.5 ===

Libvirt has been updated to version 2.5.
See the [[https://libvirt.org/news.html|Changelogs]] for details.

For administrators worth to consider is that depending on the system setup and huge page size availability the specification of a [[https://libvirt.org/formatdomain.html#elementsMemoryBacking|page size for hugepages]] in a guest xml can now be mandatory.

=== LXD 2.12 ===
[[https://www.ubuntu.com/containers/lxd|LXD]], now at [[https://linuxcontainers.org/lxd/news/|version 2.12]], introduces support for GPU passthrough, including [[https://insights.ubuntu.com/2017/03/28/nvidia-cuda-inside-a-lxd-container/|NVidia CUDA]]. A new [[https://github.com/lxc/lxd/blob/master/doc/storage-backends.md|storage API]] has also been added, allowing for the creation of multiple storage pools which can then be used to host containers or independent storage volumes.

And a number of [[https://images.linuxcontainers.org|new images]] have been added, including support for [[https://insights.ubuntu.com/2017/02/27/ubuntu-core-in-lxd-containers/|Ubuntu Core 16]].

=== DPDK ===

Ubuntu 17.04 includes the latest release of DPDK, 16.11.1.

See the [[http://dpdk.org/doc/guides/rel_notes/release_16_11.html|Release Notes]] as well as the stable release [[http://dpdk.org/ml/archives/dev/2017-March/058930.html|announcement]] for more detail.

As a tech preview DPDK is now also available for ppc64el. This includes the latest improvements made in version 16.11.1 in general, but also further improvements to enable the i40e PMD and vfio-pci scanning on spapr platforms.

=== OpenStack Ocata ===

Ubuntu 17.04 includes the latest !OpenStack release, Ocata, including the following components:

 * !OpenStack Identity - Keystone
 * !OpenStack Imaging - Glance
 * !OpenStack Block Storage - Cinder
 * !OpenStack Compute - Nova
 * !OpenStack Networking - Neutron
 * !OpenStack Telemetry - Ceilometer, Aodh and Gnochi
 * !OpenStack Orchestration - Heat
 * !OpenStack Dashboard - Horizon
 * !OpenStack Object Storage - Swift
 * !OpenStack Database as a Service - Trove
 * !OpenStack DNS - Designate
 * !OpenStack Bare-metal - Ironic
 * !OpenStack Filesystem - Manila
 * !OpenStack Key Manager - Barbican

Please refer to the [[http://releases.openstack.org/ocata/|OpenStack Ocata release notes]] for full details of this release of !OpenStack.

!OpenStack Ocata is also provided via the [[OpenStack/CloudArchive|Ubuntu Cloud Archive]] for !OpenStack Ocata for Ubuntu 16.04 LTS users.

'''WARNING''': Upgrading an !OpenStack deployment is a non-trivial process and care should be taken to plan and test upgrade procedures which will be specific to each !OpenStack deployment.

Make sure you read the [[http://docs.openstack.org/developer/charm-guide/1702.html|OpenStack Charm Release Notes]] for more information about how to deploy Ubuntu !OpenStack using Juju.

=== cloud-init ===
Cloud-init has been updated to be more strict when identifying the cloud
platform that it is running on and searching for datasources.
The driver for doing this is to:

 * Improve boot speed of Ubuntu images by quickly discarding datasources that are not present.
 * Avoid attempting to access network resources that may not be present.  That can result in timeouts or other unexpected behavior.
 * Entirely disable cloud-init if no datasource is present.

For more information see the [[https://lists.ubuntu.com/archives/ubuntu-server/2017-February/007475.html|mailing list post]] and [[https://bugs.launchpad.net/ubuntu/+source/cloud-init/+bug/1669675|bug 1669675]] for details.

Cloud-init can customize the network configuration of instances on certain clouds and datasources.  For more information on network configurations see the [[http://cloudinit.readthedocs.io/en/latest/topics/network-config.html|documentation]]

= Known issues =

As is to be expected, with any release, there are some significant known bugs that users may run into with this release of Ubuntu 17.04.  The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:

== Installation ==

 * Partitioning step allows to configure LVM across multiple devices without requiring to setup a separate /boot partition. This may lead to failure to install the bootloader at the end of the installation, and failures to boot the resultant installations. (Bug:1680101)

 * Partitioner does not support installation when multiple conflicting/identical volume groups have been detected. For example reinstalling Ubuntu with LVM across multiple disk drives that had individual LVM installations of Ubuntu. As a workaround, please format disk drives prior to installation, or from the built in shell provided in the installer. (Bug:1679184)

 * Installer by default no longer create swap partitions, and uses swapfiles. However, some filesystems can be used for rootfs which do not support swapfiles. Notably, btrfs. If one desires swap to be available with btrfs as rootfs one should perform manual partitioning and create a swap partition. (Bug:1656915)

== OpenVPN ==

OpenVPN 2.4 removed its [[https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=848024|tls-remote option]]. Current setups using that option will fail to work. Update your configuration to use verify-x509-name instead. 

== Upgrade ==

 * Sometimes DKMS modules are not built with the new kernel when upgrading. A workaround is to reinstall the module after rebooting into the new kernel. (Bug:1681566)

 * On s390x architecture, in KVM virtual machines interface names are not preserved on upgrade, and new predictable interface names are used. This will result in lack of network connectivity due to incorrect names in `/etc/network/interfaces`. An upgrade SRU to preserve `ethX` interface names is being prepared. (Bug:1682437)

##== Power Management ==

== Desktop ==

  * Some third-party .deb files are not installable in the Software app (Bug:1672424)

##== Graphics and Display ==

##== Networking ==

##== Kernel ==

<<BR>>
= Official flavours =

The release notes for the official flavours can be found at the following links:
## * Edubuntu [[https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/Edubuntu]]
 * Kubuntu [[https://wiki.ubuntu.com/ZestyZapus/ReleaseNotes/Kubuntu]]
 * Lubuntu [[https://wiki.ubuntu.com/ZestyZapus/ReleaseNotes/Lubuntu]]
## * Mythbuntu [[https://wiki.ubuntu.com/YakketyYak/ReleaseNotes/Mythbuntu]]
 * Ubuntu Budgie [[https://ubuntubudgie.org/blog/2017/04/11/17-04-release-notes]]
 * Ubuntu GNOME [[https://wiki.ubuntu.com/ZestyZapus/ReleaseNotes/UbuntuGNOME]]
 * Ubuntu Kylin [[https://wiki.ubuntu.com/ZestyZapus/ReleaseNotes/UbuntuKylin]]
 * Ubuntu MATE [[https://ubuntu-mate.org/blog/ubuntu-mate-zesty-final-release/]]
 * Ubuntu Studio [[https://wiki.ubuntu.com/ZestyZapus/ReleaseNotes/UbuntuStudio]]
 * Xubuntu [[http://wiki.xubuntu.org/releases/17.04/release-notes]]

<<BR>>
= More information =

=== Reporting bugs ===

Your comments, bug reports, patches and suggestions will help fix bugs and improve the quality of future releases. Please [[http://help.ubuntu.com/community/ReportingBugs|report bugs using the tools provided]].

If you want to help out with bugs, the [[http://wiki.ubuntu.com/BugSquad|Bug Squad]] is always looking for help.

=== Participate in Ubuntu ===

## These images were able to be made available to you thanks to the help of our [[https://wiki.ubuntu.com/SaucySalamander/TechnicalOverview/Beta1/Testers|QA Community]].

If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

 https://community.ubuntu.com/contribute

=== More about Ubuntu ===

You can find out more about Ubuntu on the [[https://www.ubuntu.com|Ubuntu website]] and [[https://wiki.ubuntu.com|Ubuntu wiki]].

To sign up for future Ubuntu development announcements, please subscribe to Ubuntu's development announcement list at:

 https://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce
