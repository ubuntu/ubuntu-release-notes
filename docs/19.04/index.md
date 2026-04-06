---
tocdepth: 3
---

(ubuntu-19-04-release-notes)=
# Ubuntu 19.04 "Disco Dingo" Release Notes

<!-- Source: https://wiki.ubuntu.com/DiscoDingo/ReleaseNotes -->

## page was copied from YakketyYak/ReleaseNotes
## page was copied from XenialXerus/ReleaseNotes
## page was copied from ZestyZapus/ReleaseNotes
## page was copied from ArtfulAardvark/ReleaseNotes
## page was copied from CosmicCuttlefish/ReleaseNotes

## When adding features to this page, please add credits for the relevant upstream developers where appropriate.
||<tablestyle="float:right; width:40%; background:#F1F1ED; margin: 0 0 1em 1em;" style="padding:0.5em;">'''Table of Contents'''<<BR>> <<TableOfContents(3)>>||
'''WARNING: Release reached End of Life'''

'''This release is no longer supported, please see [[Releases]]'''

'''WARNING: Release reached End of Life'''

= Introduction =

These release notes for '''Ubuntu 19.04''' (Disco Dingo) provide an overview of the release and document the known issues with Ubuntu 19.04 and its flavours.

=== Support lifespan ===
Ubuntu 19.04 will be supported for 9 months until [[Releases|January 2020]]. If you need Long Term Support, it is recommended you use [[BionicBeaver/ReleaseNotes/|Ubuntu 18.04 LTS]] instead.

=== Official flavour release notes ===
Find the links to release notes for official flavors [[#Official_flavours|here]].

<<BR>>
= Get Ubuntu 19.04 =
== Download Ubuntu 19.04 ==

Images can be downloaded from a location near you.

You can download ISOs and flashable images from:

http://releases.ubuntu.com/19.04/ (Ubuntu Desktop and Server) <<BR>>
http://cdimage.ubuntu.com/ubuntu/releases/19.04/release/ (Less Popular Ubuntu Images) <<BR>>
http://cloud-images.ubuntu.com/daily/server/disco/current/ (Ubuntu Cloud Images) <<BR>>
http://cdimage.ubuntu.com/netboot/19.04/ (Ubuntu Netboot) <<BR>>
http://cdimage.ubuntu.com/kubuntu/releases/19.04/release/ (Kubuntu) <<BR>>
http://cdimage.ubuntu.com/lubuntu/releases/19.04/release/ (Lubuntu) <<BR>>
http://cdimage.ubuntu.com/ubuntu-budgie/releases/19.04/release/ (Ubuntu Budgie) <<BR>>
http://cdimage.ubuntu.com/ubuntukylin/releases/19.04/release/ (Ubuntu Kylin) <<BR>>
http://cdimage.ubuntu.com/ubuntu-mate/releases/19.04/release/ (Ubuntu MATE) <<BR>>
http://cdimage.ubuntu.com/ubuntustudio/releases/19.04/release/ (Ubuntu Studio) <<BR>>
http://cdimage.ubuntu.com/xubuntu/releases/19.04/release/ (Xubuntu)

== Upgrading from Ubuntu 18.10 ==
To upgrade on a desktop system:
 * Open the "Software & Updates" application.
 * Select the 3rd Tab called "Updates".
 * Set the "Notify me of a new Ubuntu version" dropdown menu to "For any new version".
 * Press Alt+F2 and type in "update-manager -c" (without the quotes) into the command box.
 * Update Manager should open up and tell you: New distribution release '19.04' is available.
  * If not you can also use "/usr/lib/ubuntu-release-upgrader/check-new-release-gtk"
 * Click Upgrade and follow the on-screen instructions.

To upgrade on a server system:
 * Install the {{{update-manager-core}}} package if it is not already installed.
 * Make sure the {{{Prompt}}} line in /etc/update-manager/release-upgrades is set to normal.
 * Launch the upgrade tool with the command {{{do-release-upgrade}}}.
 * Follow the on-screen instructions.
Note that the server upgrade will use GNU screen and automatically re-attach in case of dropped connection problems.

There are no offline upgrade options for Ubuntu Desktop and Ubuntu Server. Please ensure you have network connectivity to one of the official mirrors or to a locally accessible mirror and follow the instructions above.

=== Upgrades on i386 ===
Users of the i386 architecture will not be allowed to upgrade to Ubuntu 19.04 as dropping support for that architecture is being evaluated and users of it should not be stranded on a release with a shorter support window than the release they are already running.

<<BR>>
= New features in 19.04 =

## * For other changes since 16.04 LTS, see the [[ZestyZapus/ReleaseNotes|17.04 Release Notes]] and [[YakketyYak/ReleaseNotes|16.10 Release Notes]].

== Updated Packages ==

=== Linux kernel 🐧 ===

Ubuntu 19.04 is based on the Linux release series '''5.0'''. It includes support for AMD Radeon RX Vega M graphics processor, complete support for the Raspberry Pi 3B and the 3B+, Qualcomm Snapdragon 845, many USB 3.2 and Type-C improvements, Intel Cannonlake graphics, significant power-savings improvements, P-State driver support for Skylake X servers, POWER memory protection keys support, KVM support for AMD Secure Encrypted Virtualization, enablement of Shared Memory Communications remote and direct (SMC-R/D), Open for Business (OFB), and zcrypt on IBM Z among with many other improvements since the v4.15 kernel shipped in 18.04 LTS.

=== Toolchain Upgrades 🛠️ ===

Ubuntu 19.04 comes with refreshed state-of-the-art toolchain including new upstream releases of glibc 2.29, ☕ OpenJDK 11, boost 1.67, rustc 1.31, and updated GCC 8.3, optional GCC 9, 🐍 Python 3.7.3 as default, 💎 ruby 2.5.5, php 7.2.15, 🐪 perl 5.28.1, golang 1.10.4. There are new improvements on the cross-compilers front as well with POWER and AArch64 toolchain enabled to cross-compile for ARM, S390X and RISCV64 targets.

##=== Network configuration ===

== Ubuntu Desktop ==

=== Desktop Updates ===

Ubuntu 19.04 ships with the latest GNOME desktop 3.32.  This brings performance improvements, a host of bug fixes and some important new features.

 * Desktop upgraded to GNOME 3.32
  * Numerous performance improvements.  GNOME Shell now feels faster and more responsive. [[https://discourse.ubuntu.com/t/gnome-3-32-performance-ubuntu-19-04/10208|More technical details here]]
  * Fractional Scaling support.
   * The Wayland session can now be scaled between 100% and 200% in 25% increments.
   * Experimental support in the Xorg session can be enabled to achieve the same.  Read more  [[https://community.ubuntu.com/t/x11-hidpi-scaling-available-for-testing-on-disco/10293|here]]
  * New sound configuration panel making it easier to select your input and output devices
  * Changes to GNOME Initial Setup to add more settings up front and make it easier to enable location services (for example, to allow automatic timezone switching)
 * Tracker is now included by default.  This allows the desktop to keep track of recently used files and improves searching.
 * Right click handling is now "area" by default.  This allows both two-finger right clicking and clicking in the bottom right corner of the touchpad
 * alt-tab handling now switches windows by default.  Switching applications by default can be done with super-tab
 * Preview order of windows in the dock is now static and based on the order in which the windows were added
 * IWD can now be enabled for use with Network Manager.  IWD is a new alternative to wpa supplicant and is in testing for consideration in the future.
 * Installing Ubuntu Desktop on vmware will now automatically install the open-vm-tools package to improve integration.
 * The Yaru theme has seen further refinement and updates and includes a new icon theme.
 * Safe Graphics Mode.  A new option is added to the Grub menu which will boot with "NOMODESET" on.  This may help you resolve issues on certain graphics cards and allow you to boot and install any propriatary drivers needed by your system.
 * The latest releases of Firefox (66.0) and !LibreOffice (6.2.2) are available and installed by default.



== Ubuntu Server ==

=== qemu ===

QEMU was updated to 3.1 release.

See the [[http://wiki.qemu.org/ChangeLog/3.0|3.0]] and [[http://wiki.qemu.org/ChangeLog/3.1| 3.1]] change log for major changes since Cosmic.

Migrations from former versions are supported just as usual. When upgrading it is always recommended to [[https://wiki.ubuntu.com/QemuKVMMigration#Upgrade_machine_type|upgrade the machine types]] allowing guests to fully benefit from all the improvements and fixes of the most recent version.

Qemu now has [[https://virgil3d.github.io/|virglrenderer]] enabled which allows to create a virtual 3D GPU inside qemu virtual machines. That is inferior to GPU passthrough, but can be handy if the platform used lacks the capability for classic [[https://www.linux-kvm.org/page/How_to_assign_devices_with_VT-d_in_KVM|PCI passthrough]] as well as more modern [[https://www.kernel.org/doc/Documentation/vfio-mediated-device.txt|mediated devices]].

=== libvirt ===

libvirt was updated to version 5.0. See the upstream [[https://libvirt.org/news.html|change log]] for details since version 4.6 that was in Cosmic.

Among many other changes worth to mention is the ability to have [[https://libvirt.org/formatdomain.html#elementsGraphics|GL enabled graphics]] as well as [[https://libvirt.org/formatdomain.html#elementsHostDevSubsys|mediated devices]] to be configured while still being guarded by custom apparmor profiles generated per guest. This is required for the use of gpu based [[https://libvirt.org/formatdomain.html#elementsHostDevSubsys|mediated devices]] as well as [[https://libvirt.org/formatdomain.html#elementsVideo|VirGL]] mentioned above in the qemu section.

=== dpdk ===

Ubuntu includes 18.11.x the latest stable release branch of DPDK. The very latest (non-stable) version being 19.02 was not chosen for downstream projects of DPDK (like Open vSwitch) not being compatible.

DPDK dependencies were reorganized into more or less common/tested components. Due to that most DPDK installations will now have a smaller installation footprint and less potentially active code to care about.

See the [[http://dpdk.org/doc/guides/rel_notes/release_18_11.html|release notes]] for details.

=== samba ===
Samba was updated to version 4.10.x, and one of the big changes here is python3 support. In Disco, samba and its dependencies are all python3 only now, with the exception of tdb. tdb still builds a python2 package, namely python-tdb, but all the others, including samba itself, are python3 only.

=== open-vm-tools ===

To run well integrated as VMware guest Ubuntu 19.04 comes with the latest open-vm-tools version 10.3.10. Details about the changes can be found in the upstream [[https://raw.githubusercontent.com/vmware/open-vm-tools/stable-10.3.10/open-vm-tools/ChangeLog|changelog]]

=== Raspberry Pi 🥧 ===

Ubuntu 19.04 comes with an easy way of enabling Bluetooth support on the raspi3 ubuntu-server preinstalled images; install the pi-bluetooth package (now available in multiverse) with `sudo apt install pi-bluetooth`.

Please note that supported Pi devices which have Bluetooth (at the time of writing, the Raspberry Pi 3B, 3B+, and 3A+) can have either serial console or Bluetooth support enabled at any given time (not both). With the pi-bluetooth package installed, edit `/boot/firmware/config.txt` and set `enable_uart=1` to enable serial console, or `enable_uart=0` to enable Bluetooth. The change will take effect after the next reboot.

=== OpenStack Stein ===

Ubuntu 19.04 includes the latest !OpenStack release, Stein, including the following components:

 * !OpenStack Identity - Keystone
 * !OpenStack Imaging - Glance
 * !OpenStack Block Storage - Cinder
 * !OpenStack Compute - Nova
 * !OpenStack Networking - Neutron
 * !OpenStack Telemetry - Ceilometer, Aodh, Gnocchi, and Panko
 * !OpenStack Orchestration - Heat
 * !OpenStack Dashboard - Horizon
 * !OpenStack Object Storage - Swift
 * !OpenStack Database as a Service - Trove
 * !OpenStack DNS as a Service - Designate
 * !OpenStack Bare-metal - Ironic
 * !OpenStack Filesystem - Manila
 * !OpenStack Key Manager - Barbican

Please refer to the [[http://releases.openstack.org/stein/|OpenStack Stein release notes]] for full details of this release of !OpenStack.

!OpenStack Stein is also provided via the [[OpenStack/CloudArchive|Ubuntu Cloud Archive]] for !OpenStack Stein for Ubuntu 18.04 LTS users.

'''WARNING''': Upgrading an !OpenStack deployment is a non-trivial process and care should be taken to plan and test upgrade procedures which will be specific to each !OpenStack deployment.

Make sure you read the [[https://docs.openstack.org/charm-guide/latest/19.04.html|OpenStack Charm Release Notes]] for more information about how to deploy Ubuntu !OpenStack using Juju.

=== Open vSwitch ===

Open vSwitch has been updated to 2.11.

Please read the [[http://openvswitch.org/releases/NEWS-2.11.0|release notes]] for more detail.


##=== dpdk ===

##Ubuntu includes 18.11.x the latest stable release branch of DPDK. The very latest (non-stable) version being 18.08 was not chosen for downstream projects of DPDK (like Openvswitch) not being compatible.

##See the [[http://dpdk.org/doc/guides/rel_notes/release_17_11.html|release notes]] for details.


##=== cloud-init ===

##The version was updated to [[https://launchpad.net/cloud-init/trunk/18.4|18.4]]. Notable new features include:

## * Add datasource Oracle Compute Infrastructure (OCI).
## * SmartOS: Support for re-reading metadata and re-applying on each boot (Mike Gerdts)
## * Scaleway: Add network configuration to the DataSource (Louis Bouchard)
## * Azure: allow azure to generate network configuration from IMDS per boot.
## * Support access to platform meta-data in cloud-config and user-data via jinja rendering.
## * OpenStack now runs at local time frame paving the way for network
##   configuration in the next release.
## * Fix utf-8 content in user-data [[http://pad.lv/1768600|LP: #1768600]]
## * many SmartOS improvements

##=== curtin ===

##The version was updated to 18.1.59. Notable new features include:

## * Enable custom storage configuration and multi-distribution support
## * Handle zpool/zfs clear when wiping disks
## * Rescan for lvm devices after assembling raid arrays
## * Add timing and logging functions
## * Parse_dpkg_version: support non-numeric in version string
## * Don't allow reads of /proc and modprobe zfs through
## * block: use uuid4 (random) when auto-generating UUIDS for filesystems
## * reread ptable after wiping disks with partitions
## * Fix WorkingDir class to support already existing target directory. (LP: #1775622)
## * Fix extraction of local filesystem image. (LP: #1775630)
## * Fix tip-pyflakes imported but unused call to util.get_platform_arch
## * subp: update return value of subp with combine_capture=True.
## * Continuous Integration test improvements

=== s390x ===

IBM Z and LinuxONE / s390x-specific enhancements (since 18.10) include:

 * Since s390x supports 1M huge pages (as well as 2GB huge pages, if requested) the support for libhugetlbfs (v2.19) was added for native s390x (Bug:1823132) as well as for KVM (Bug:1803315), so that customers running workloads with large memory footprints can benefit from improved memory performance.
 * Now, having the kernel infrastructure (since 4.17) as well as the s390-tool in place, the I/O device auto-configuration feature is ready to use. (Bug:1776631)
 * With (Bug:1784643) Ubuntu Server is now prepared (with lib-zfcp-hbaapi) for port speed capabilities of 32GB line speed.
 * The pass through capabilities for cryptographic resources got enhanced (Bug:1787405).
 * The upgrade to qemu 3.1+ (Bug:1786956) and the current kernel allows to make use of the latest KVM features for s390x.
 * For example, but not limited, to PCI passthrough support for KVM (Bug:1799446) and support for configurable virtio-crypto (Bug:1802514).
 * The enablement for virtio-gpu for s390x (Bug:1799467) and (Bug:1799472) now allows to better administer KVM virtual machines with UI based tools.
 * PCI Virtual function enablement and s390x-specific modifications were added as well (Bug:1814684).
 * Valgrind now has support for z13 (incl. SIMD) (Bug:1799696).
 * And a new PCI error reporting tool with support for NVMe was added to the s390-tools package (Bug:1802499).
 * zKey was enhanced in regards to error messages about missing CCA library (Bug:1808520) and the folder handling fixed (Bug:1803958).
 * With the upgrade to opencryptoki 3.11 the performance for EP11 tokens was improved (Bug:1804020), z14 functions were enhanced (Bug:1804257) and CPACF hashes are now used in EP 11 tokens (Bug:1803994).
 * libica upgrade to 3.4.0 came with expanded SHA support (Bug:1803962).
 * The upgrade to binutils 2.32 (Bug:1803998), plus patches on top (Bug:1824097), helped to fix instruction changes in z13 abi and provides now partial relro support (Bug:1783294).
 * Upgrading openssl-ibmca to 2.0.2 (Bug:1804233) fixes a failure in case a libica symbol cannot be resolved.
 * With (Bug:1804408) LUKS2 support for pam_mount was introduced (while still retaining support for LUKS1) for PAM.
 * Changes to clean up stacks for KASAN, the KernelAddressSANitizer, were picked up (Bug:1804645).
 * Kernel enhancements (that came with 4.20) will now create CPU-MF auxiliary trace data files for s390 (Bug:1805428).
 * AP queues (APQN) were extended (Bug:1805429), (Bug:1804019), tags were added (Bug:1800867), and vfio/vfio-ap got enhanced (Bug:1818854), (Bug:1805414).
 * The python-zhmcclient is now packaged and available via universe (Bug:1805367).
 * smc-tools are upgraded to 1.2.0, now including smc_rnics and smc_dbg (Bug:1815425).
 * The support for TSO (TCP Segmentation Offload) in ipv4 and ipv6 for Layer2 was extended (Bug:1805793).
 * efi-lockdown was fixed to restrict debugfs when the kernel is locked down (Bug:1807686).
 * Support to allow the protected key AES (paes) module to derive protected keys from clear keys (Bug:1811354).
 * DIF and DIF+DIX integrity protection mechanisms in FCP can now be separately configured (Bug:1814537).
 * Application can now access new data sets that were created after zdsfs was mounted - without the need to remount zdsfs (Bug:1814538).
 * Zone awareness changes for lsmem / chmem in util-linux were picked-up (Bug:1814765).
 * qeth performance (OSA and Hipersockets) got improved by general code changes (Bug:1814899) and link speed enhancements were made in kernel (Bug:1814891) and on the tooling side (Bug:1814892) - in preparation for future network hardware.
 * New instruction support was added to binutils, leading to improved performance with that enhanced instruction support (Bug:1815040).
 * The new glibc version 2.29 (Bug:1817523) has several minor improvements for s390x, and with that vx and vxe are now marked as important hwcap, to be able to provide differently tuned shared libraries (Bug:1821200).
 * The upgrade of cryptsetup to 2.1.0 comes with several fixes, like for the on-disk header size calculation for the LUKS2 format (Bug:1814769), (Bug:1815484).
 * That said s390-tools were upgraded to 2.8.0.
 * And finally support was added for automatic usage of zkey and pervasive encryption by the installer (Bug:1766865). Now when doing an (LPAR or z/VM guest) installation and selecting "Guided - use entire disk and setup encrypted LVM" zkey will be automatically used - in case a CryptoExpress domain is available with a master key set.


= Known issues =

As is to be expected, with any release, there are some significant known bugs that users may run into with this release of Ubuntu 19.04.  The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:

== Desktop ==

  * When selecting 3rd party drivers during install there is a long pause before install proceeds.  This is the ubuntu-drivers tool refreshing it's cache. Please wait a couple of minutes and install will continue normally.  (bug Bug:1824905)
  * For secure-boot enabled systems with Broadcom wireless, even after selecting the proprietary drivers during the installation, the bcmwl dkms module can end up left uninstalled after reboot (resulting in no working wifi).  This is caused by a dkms tooling regression.  As a workaround the bcmwl-kernel-source package needs to be reinstalled on the target system `sudo apt-get install --reinstall bcmwl-kernel-source`. (bug Bug:1821823)

##  * When Ubuntu is reinstalled with preserving existing data, an error message is displayed due to "Could not get lock /target/var/cache/apt/archives/lock" (bug Bug:1798369). The packages installed originally are not reinstalled and must be reinstalled manually. Although the user data is preserved.
##  * The screen reader doesn't read the installer when executed from a live session (bug Bug:1797861), is not auto-enabled on first login even if it's been enabled during installation (bug Bug:1796275) and the pages of the first run wizard are not read properly (bug Bug:1797868)
##  * When disconnecting from VPNs, DNS resolution may become broken requiring a restart of resolved.  $ sudo systemctl restart systemd-resolved.service [[https://bugs.launchpad.net/ubuntu/+source/systemd/+bug/1797415|Bug 1797415]]
##  * In an OEM installation, during user setup, the language selected is not taken into account (bug Bug:1798554) 

##  * The installer might produce systems where packages such as cryptsetup are autoremovable. Users on encrypted system should be especially cautious when running autoremove and mark such packages as manually installed using `apt-mark manual` (bug Bug:1801629)

  * The installer may not use the EFI partition you expect it to use (Bug:1396379). If you've experienced this, this bug comment has advice to repair the situation: https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1396379/comments/8

##== Server ==

##== Graphics and Display ==

##== Networking ==

##== Kernel ==

<<BR>>
= Official flavours =

The release notes for the official flavours can be found at the following links:
 * Kubuntu [[https://wiki.ubuntu.com/DiscoDingo/ReleaseNotes/Kubuntu]]
 * Lubuntu [[https://lubuntu.me/disco-released]]
 * Ubuntu Budgie [[https://ubuntubudgie.org/blog/2019/03/27/19-04-release-notes]]
 * Ubuntu Kylin [[http://www.ubuntukylin.com/news/shownews.php?lang=en&id=923]]
 * Ubuntu MATE [[https://ubuntu-mate.org/blog/ubuntu-mate-disco-final-release/]]
 * Ubuntu Studio [[https://wiki.ubuntu.com/DiscoDingo/ReleaseNotes/UbuntuStudio]]
 * Xubuntu [[https://wiki.xubuntu.org/releases/19.04/release-notes]]

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
