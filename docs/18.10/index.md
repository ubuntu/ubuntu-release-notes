---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/CosmicCuttlefish/ReleaseNotes -->

(ubuntu-18-10-release-notes)=
# Ubuntu 18.10 release notes

**WARNING: Release reached End of Life**

**This release is no longer supported, please see [Releases](https://help.ubuntu.com/community/Releases)**

**WARNING: Release reached End of Life**


(18-10-introduction)=
## Introduction

These release notes for **Ubuntu 18.10** (Cosmic Cuttlefish) provide an overview of the release and document the known issues with Ubuntu 18.10 and its flavours.


(18-10-support-lifespan)=
### Support lifespan

Ubuntu 18.10 was supported for 9 months until [July 2019](https://wiki.ubuntu.com/Releases). If you need Long Term Support, it is recommended you use [Ubuntu 18.04 LTS](https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes) instead.


(18-10-official-flavour-release-notes)=
### Official flavour release notes

Find the links to release notes for official flavors [here](https://wiki.ubuntu.com/Official_flavours).


(get-ubuntu-18-10)=
## Get Ubuntu 18.10


(download-ubuntu-18-10)=
### Download Ubuntu 18.10

Images can be downloaded from a location near you.

You can download ISOs and flashable images from:

[releases.ubuntu.com/18.10/](http://releases.ubuntu.com/18.10/) (Ubuntu Desktop and Server)

[cdimage.ubuntu.com/ubuntu/releases/18.10/release/](http://cdimage.ubuntu.com/ubuntu/releases/18.10/release/) (Less Popular Ubuntu Images)

[cloud-images.ubuntu.com/daily/server/cosmic/current/](http://cloud-images.ubuntu.com/daily/server/cosmic/current/) (Ubuntu Cloud Images)

[cdimage.ubuntu.com/netboot/18.10/](http://cdimage.ubuntu.com/netboot/18.10/) (Ubuntu Netboot)

[cdimage.ubuntu.com/kubuntu/releases/18.10/release/](http://cdimage.ubuntu.com/kubuntu/releases/18.10/release/) (Kubuntu)

[cdimage.ubuntu.com/lubuntu/releases/18.10/release/](http://cdimage.ubuntu.com/lubuntu/releases/18.10/release/) (Lubuntu and Lubuntu Alternate)

[cdimage.ubuntu.com/ubuntu-budgie/releases/18.10/release/](http://cdimage.ubuntu.com/ubuntu-budgie/releases/18.10/release/) (Ubuntu Budgie)

[cdimage.ubuntu.com/ubuntukylin/releases/18.10/release/](http://cdimage.ubuntu.com/ubuntukylin/releases/18.10/release/) (Ubuntu Kylin)

[ubuntu-mate.org/download/](https://ubuntu-mate.org/download/) (Ubuntu MATE)

[cdimage.ubuntu.com/ubuntustudio/releases/18.10/release/](http://cdimage.ubuntu.com/ubuntustudio/releases/18.10/release/) (Ubuntu Studio)

[cdimage.ubuntu.com/xubuntu/releases/18.10/release/](http://cdimage.ubuntu.com/xubuntu/releases/18.10/release/) (Xubuntu)


(18-10-upgrading-from-ubuntu-18-04)=
### Upgrading from Ubuntu 18.04

To upgrade on a desktop system:

* Open the "Software & Updates" Setting in System Settings.

* Select the 3rd Tab called "Updates".

* Set the "Notify me of a new Ubuntu version" dropdown menu to "For any new version".

* Press Alt+F2 and type in "update-manager -c" (without the quotes) into the command box.

* Update Manager should open up and tell you: New distribution release '18.10' is available.

* If not you can also use "/usr/lib/ubuntu-release-upgrader/check-new-release-gtk"

* Click Upgrade and follow the on-screen instructions.

To upgrade on a server system:

* Install the `update-manager-core` package if it is not already installed.

* Make sure the `Prompt` line in /etc/update-manager/release-upgrades is set to normal.

* Launch the upgrade tool with the command `sudo do-release-upgrade`.

* Follow the on-screen instructions.
Note that the server upgrade will use GNU screen and automatically re-attach in case of dropped connection problems.

There are no offline upgrade options for Ubuntu Desktop and Ubuntu Server. Please ensure you have network connectivity to one of the official mirrors or to a locally accessible mirror and follow the instructions above.


(18-10-upgrades-on-i386)=
#### Upgrades on i386

Users of the i386 architecture will not be allowed to upgrade to Ubuntu 18.10 as dropping support for that architecture is being evaluated and users of it should not be stranded on a release with a shorter support window than the release they are already running.


(new-features-in-18-10)=
## New features in 18.10



(18-10-updated-packages)=
### Updated Packages


(18-10-openssl-1-1-1)=
#### OpenSSL 1.1.1 🔒

OpenSSL, the secure communication library using TLS protocol, is upgraded to 1.1.1 long-term support series. It supports for the recently approved TLSv1.3 standard. Multiple client and server applications have been enabled to use TLSv1.3 by default in Ubuntu 18.10 with many more to come in the next release. The older 1.0.2 series OpenSSL is still available, however, it is expected to be removed from the next Ubuntu release.

The Ubuntu project is currently evaluating replacing OpenSSL 1.1.0 with backported OpenSSL 1.1.1 in Ubuntu 18.04 LTS. [Bug 1797386](https://bugs.launchpad.net/ubuntu/+source/openssl/+bug/1797386) 🤞


(18-10-linux-kernel)=
#### Linux kernel 🐧

Ubuntu 18.10 is based on the Linux release series **4.18**. It includes support for AMD Radeon RX Vega M graphics processor, complete support for the Raspberry Pi 3B and the 3B+, Qualcomm Snapdragon 845, many USB 3.2 and Type-C improvements, Intel Cannonlake graphics, significant power-savings improvements, P-State driver support for Skylake X servers, POWER memory protection keys support, KVM support for AMD Secure Encrypted Virtualization, enablement of Shared Memory Communications remote and direct (SMC-R/D), Open for Business (OFB), and zcrypt on IBM Z among with many other improvements since the v4.15 kernel shipped in 18.04 LTS.


(18-10-toolchain-upgrades)=
#### Toolchain Upgrades 🛠️

Ubuntu 18.10 comes with refreshed state of the art toolchain including new upstream releases of glibc 2.28, ☕ OpenJDK 11, boost 1.67, rustc 1.28, and updated GCC 8.2, 🐍 python 3.6.7 as default, python 3.7.1 as supported, 💎 ruby 2.5.1, php 7.2.10, 🐪 perl 5.26.2, golang 1.10.4. There are new improvements on the cross-compilers front as well with POWER toolchain enabled to cross-compile for ARM targets.



(18-10-ubuntu-desktop)=
### Ubuntu Desktop


(18-10-desktop-updates)=
#### Desktop Updates

18.10 ships with the latest GNOME desktop 3.30.  This brings performance improvements and new features.

* GNOME Disks now supports VeraCrypt

* Settings includes a panel to manage Thunderbolt devices and shows those panels only where the relevant hardware is detected.

* More shell components are cached in GPU RAM to reduce load and increase FPS count

* Desktop zoom is now a lot smoother

* Smoothing of window previews is now dependant on CPU/GPU availability so that busy applications don't impact the whole system when window previews are visible

* Added the option to automatically submit error reports to the error reporting dialog window

* Fingerprint libraries promoted to main to allow unlocking with fingerprints

* Added snap support to XDG Portals and landed support in Ubuntu

* The latest version of GS Connect is now packaged in the archive and easily installed

The latest releases of Firefox (63.0) and LibreOffice (6.1.2) are available and installed by default.


(18-10-yaru-theme-updates)=
#### Yaru Theme Updates

Yaru theme, the bold, the frivolous, yet distinctly Ubuntu saw further improvements and touchups. Integrates beautifully with GNOME v3.20 Desktop and improves usability with its careful use of semantic colors.


(18-10-ubuntu-server)=
### Ubuntu Server


(18-10-qemu)=
#### qemu

QEMU was updated to 2.12 release.

See the [change log](http://wiki.qemu.org/ChangeLog/2.12) for major changes since Bionic.

Migrations from former versions are supported just as usual. When upgrading it is always recommended to [upgrade the machine types](https://wiki.ubuntu.com/QemuKVMMigration#Upgrade_machine_type) allowing guests to fully benefit from all the improvements and fixes of the most recent version.


(18-10-libvirt)=
#### libvirt

libvirt was updated to version 4.6. See the upstream [change log](https://libvirt.org/news.html) for details since version 4.0 that was in Bionic.

Among many other changes administrators might like the ease of a new local include apparmor to the libvirt-qemu profile that allows local overrides for  special devices or paths matching your setup without conffile delta that has to be managed on later upgrades.


(18-10-dpdk)=
#### dpdk

Ubuntu includes 17.11.x the latest stable release branch of DPDK. The very latest (non-stable) version being 18.08 was not chosen for downstream projects of DPDK (like Openvswitch) not being compatible.

See the [release notes](http://dpdk.org/doc/guides/rel_notes/release_17_11.html) for details.


(18-10-open-vswitch)=
#### Open vSwitch

Open vSwitch has been updated to 2.10.

Please read the [release notes](http://openvswitch.org/releases/NEWS-2.10.0) for more detail.


(18-10-cloud-init)=
#### cloud-init

The version was updated to [18.4](https://launchpad.net/cloud-init/trunk/18.4). Notable new features include:

* Add datasource Oracle Compute Infrastructure (OCI).

* SmartOS: Support for re-reading metadata and re-applying on each boot (Mike Gerdts)

* Scaleway: Add network configuration to the DataSource (Louis Bouchard)

* Azure: allow azure to generate network configuration from IMDS per boot.

* Support access to platform meta-data in cloud-config and user-data via jinja rendering.

* OpenStack now runs at local time frame paving the way for network
   configuration in the next release.

* Fix utf-8 content in user-data [LP: #1768600](http://pad.lv/1768600)
* many SmartOS improvements


(18-10-curtin)=
#### curtin

The version was updated to 18.1.59. Notable new features include:

* Enable custom storage configuration and multi-distribution support

* Handle zpool/zfs clear when wiping disks

* Rescan for lvm devices after assembling raid arrays

* Add timing and logging functions

* Parse_dpkg_version: support non-numeric in version string

* Don't allow reads of /proc and modprobe zfs through

* block: use uuid4 (random) when auto-generating UUIDS for filesystems

* reread ptable after wiping disks with partitions

* Fix WorkingDir class to support already existing target directory. (LP: #1775622)

* Fix extraction of local filesystem image. (LP: #1775630)

* Fix tip-pyflakes imported but unused call to util.get_platform_arch

* subp: update return value of subp with combine_capture=True.

* Continuous Integration test improvements


(18-10-s390x)=
#### s390x

IBM Z and LinuxONE / s390x-specific enhancements (since 18.04) include:

* s390-tools package update to 2.6.0 (Bug:1776907), (Bug:1786460) that brings improvements for fast dump of early boot problems (Bug:1775632), adds NVMe related debug data to dbginfo script (Bug:1772876), protected key management tool (zkey) was added (Bug:1775627) (Bug:1794290) and more.

* Protected key infrastructural support was added and expanded for cryptsetup (Bug:781912), (Bug:1785610) and support for 4k sectors for fast clear key dm-crypt (crypttab) added (Bug:1776626).

* SMC (shared memory communications) support and exploitation was introduced in the kernel (Bug:1784647), SMC-Direct (Bug:1786902) and SMC-R/D (Bug:1789934) as well as a new SMC tools package introduced (Bug:1689782).

* The upgrade to libica (libica3) 3.3.3 brings several bug fixes as well as extended SIMD exploitation and elliptic-curve enhancements (Bug:1776194), (Bug:1764325).

* The qclib update (libqc1) to 1.4.1 brings SMT support and some bugfixes (Bug:1760803).

* openssl update to 1.1.1 with s390x assembly pack improvements and hardware-support for several cryptographic primitives (Bug:1737158) (Bug:1793092).

* libpfm4 rebase to 4.10 comes with various bug fixes and s390x updates (Bug:1776169).

* Update nvme-cli package to 1.6 to pick up latest fixes and enhancements (Bug:1784809).

* Configurable IFCC handling was added to the kernel (upstream since 4.17) (Bug:1776216).

* Upgrade of opencryptoki to 3.10 with elliptic curve support for libica and icatoken (Bug:1776210), (Bug:1776210).

* Upgrade of openssl-ibmca to 2.0.0 that comes with elliptic curve support (Bug:1776209), (Bug:1777641).

* Enhanced zcrypt driver (upstream with kernel 4.17) to support architectural limit of up to 255 crypto adapters (Bug:1777613) and to introduce APQN tags to support deterministic driver binding (Bug:1784331).

* Introduced support for the kexec_file_load system call in kernel (Bug:1783088) and kexec-tools (Bug:1783086).

* Version bump to gcc-8 (version 8.2) brings brings serveral s390x optimizations (Bug:1777835).

* Upgrade to LLVM 7.0 brings performance improvements, some new functions and improved support for z13/14 systems (Bug:1777869).

* qemu-kvm 2.12 upgrade to 2.12 (Bug: 1780772) with additional improvements to expose detailed guest crash information to the hypervisor (Bug:1780768), interactive bootloader support (Bug:1780769), support for CPU Model z14 ZR1 (Bug:1780773) and much more.

* Also upgrading to an adequate libvirt version 4.6.0 (now packages libvirt-daemon-system and libvirt-clients) (Bug:1786957).

* Added support to display FCP cards with 32GB line speed (upstream with kernel 4.18) (Bug:1784621).

* Added enhanced OSA support for IPv6 checksum offload (upstream with kernel 4.18) (Bug:1784645).

* Enabled kernel configuration ("CONFIG_SCLP_OFB") to support Open for Business (OFB) message (Bug:1787898).


(18-10-known-issues)=
## Known issues

As is to be expected, with any release, there are some significant known bugs that users may run into with this release of Ubuntu 18.10.  The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:


(18-10-desktop)=
### Desktop

* After installing Cosmic alongside Cosmic, the resized filesystem is corrupted (bug Bug:1798562) It has not been reported to happen if the original operating system is something else than Cosmic.

* When Ubuntu is reinstalled with preserving existing data, an error message is displayed due to "Could not get lock /target/var/cache/apt/archives/lock" (bug Bug:1798369). The packages installed originally are not reinstalled and must be reinstalled manually. Although the user data is preserved.

* The screen reader doesn't read the installer when executed from a live session (bug Bug:1797861), is not auto-enabled on first login even if it's been enabled during installation (bug Bug:1796275) and the pages of the first run wizard are not read properly (bug Bug:1797868)

* When disconnecting from VPNs, DNS resolution may become broken requiring a restart of resolved.  $ sudo systemctl restart systemd-resolved.service [Bug 1797415](https://bugs.launchpad.net/ubuntu/+source/systemd/+bug/1797415)
##* In some cases gdm may fail to start and you will be presented with a flashing cursor instead of a login screen.  Switching to vt 2 and then back to 1 (ctrl-alt-f2 & ctrl-alt-f1) will cause gdm to start and you can log in.  [Bug 1795637](https://bugs.launchpad.net/ubuntu/+source/gdm3/+bug/1795637)

* In an OEM installation, during user setup, the language selected is not taken into account (bug Bug:1798554)

* The gnome-initial-setup Quit option from the application menu in the top bar doesn't quit the application.  If you want to quit g-i-s use quit from the dock menu instead.

* The installer might produce systems where packages such as cryptsetup are autoremovable. Users on encrypted system should be especially cautious when running autoremove and mark such packages as manually installed using `apt-mark manual` (bug Bug:1801629)






(18-10-official-flavours)=
## Official flavours

The release notes for the official flavours can be found at the following links:

* Kubuntu [wiki.ubuntu.com/CosmicCuttlefish/ReleaseNotes/Kubuntu/](https://wiki.ubuntu.com/CosmicCuttlefish/ReleaseNotes/Kubuntu/)

* Lubuntu [lubuntu.me/cosmic-released](https://lubuntu.me/cosmic-released)

* Ubuntu Budgie [ubuntubudgie.org/blog/2018/09/27/18-10-release-notes](https://ubuntubudgie.org/blog/2018/09/27/18-10-release-notes)

* Ubuntu Kylin [www.ubuntukylin.com/news/shownews.php?lang=en&id=843](https://www.ubuntukylin.com/news/shownews.php?lang=en&id=843)

* Ubuntu MATE [ubuntu-mate.org/blog/ubuntu-mate-cosmic-final-release/](https://ubuntu-mate.org/blog/ubuntu-mate-cosmic-final-release/)

* Ubuntu Studio [wiki.ubuntu.com/CosmicCuttlefish/ReleaseNotes/UbuntuStudio](https://wiki.ubuntu.com/CosmicCuttlefish/ReleaseNotes/UbuntuStudio)

* Xubuntu [wiki.xubuntu.org/releases/18.10/release-notes](https://wiki.xubuntu.org/releases/18.10/release-notes)


(18-10-more-information)=
## More information


(18-10-reporting-bugs)=
### Reporting bugs

Your comments, bug reports, patches and suggestions will help fix bugs and improve the quality of future releases. Please [report bugs using the tools provided](http://help.ubuntu.com/community/ReportingBugs).

If you want to help out with bugs, the [Bug Squad](http://wiki.ubuntu.com/BugSquad) is always looking for help.


(18-10-participate-in-ubuntu)=
### Participate in Ubuntu


If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

[community.ubuntu.com/contribute](https://community.ubuntu.com/contribute)


(18-10-more-about-ubuntu)=
### More about Ubuntu

You can find out more about Ubuntu on the [Ubuntu website](https://www.ubuntu.com) and [Ubuntu wiki](https://wiki.ubuntu.com).

To sign up for future Ubuntu development announcements, please subscribe to Ubuntu's development announcement list at:

[lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce](https://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce)
