---
tocdepth: 3
---

<!-- SOURCE: https://discourse.ubuntu.com/t/impish-indri-release-notes/21951 -->

(ubuntu-21-10-release-notes)=
# Ubuntu 21.10 release notes

## Introduction

These release notes for **Ubuntu 21.10** (Impish Indri) provide an overview of the release and document the known issues with Ubuntu and its flavours.

## Support lifespan

Ubuntu 21.10 will be supported for 9 months until July 2022. If you need Long Term Support, it is recommended you use [Ubuntu 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes/) instead.

## Get Ubuntu 21.10

## Download Ubuntu 21.10

Images can be downloaded from a location near you.

You can download ISOs and flashable images from:

  * [Ubuntu Desktop and Server for 64-bit x86 (AMD64) ](http://releases.ubuntu.com/21.10/)
  * [Less Frequently Downloaded Ubuntu Images](http://cdimage.ubuntu.com/ubuntu/releases/21.10/release/)
  * [Ubuntu Cloud Images](http://cloud-images.ubuntu.com/daily/server/hirsute/current/)
  * [Lubuntu](http://cdimage.ubuntu.com/lubuntu/releases/21.10/release/)
  * [Kubuntu](http://cdimage.ubuntu.com/kubuntu/releases/21.10/release/)
  * [Ubuntu Budgie](http://cdimage.ubuntu.com/ubuntu-budgie/releases/21.10/release/)
  * [Ubuntu Kylin](http://cdimage.ubuntu.com/ubuntukylin/releases/21.10/release/)
  * [Ubuntu MATE](http://cdimage.ubuntu.com/ubuntu-mate/releases/21.10/release/)
  * [Ubuntu Studio](http://cdimage.ubuntu.com/ubuntustudio/releases/21.10/release/)
  * [Xubuntu](http://cdimage.ubuntu.com/xubuntu/releases/21.10/release/)

## Upgrading from Ubuntu 21.04

To upgrade on a desktop system:

  * Open the "Software & Updates" Setting in System Settings.
  * Select the 3rd Tab called "Updates".
  * Set the "Notify me of a new Ubuntu version" dropdown menu to "For any new version".
  * Press <kbd>Alt</kbd>+ <kbd>F2</kbd> and type in `update-manager -c` into the command box.
    * Update Manager should open up and tell you: **"New distribution release '21.10' is available."**
  * If not you can also use `/usr/lib/ubuntu-release-upgrader/check-new-release-gtk`
  * Click Upgrade and follow the on-screen instructions. 

To upgrade on a server system:

  * Install the `update-manager-core package` if it is not already installed.
  * Make sure the Prompt line in `/etc/update-manager/release-upgrades` is set to normal.
  * Launch the upgrade tool with the command `sudo do-release-upgrade`.
  * Follow the on-screen instructions. 

Note that the server upgrade will use GNU screen and automatically re-attach in case of dropped connection problems.

There are no offline upgrade options for Ubuntu Desktop and Ubuntu Server. Please ensure you have network connectivity to one of the official mirrors or to a locally accessible mirror and follow the instructions above.

### Upgrades on 32-bit x86 (i386)

Users of the i386 architecture will not be presented with an upgrade. Support for i386 as a host architecture is dropped in 19.10.

## New features in 21.10

## Updated Packages

### Linux kernel 🐧

[Linux 5.13](https://kernelnewbies.org/Linux_5.13) introduces support for new hardware and some less new:
 * Future Intel and AMD chips, such as Intel Alderlake S or AMD Adebaran.
 * [Microsoft Surface Laptops and tablets](https://github.com/linux-surface/linux-surface/wiki/Supported-Devices-and-Features#surface-laptops).
 * Rudimentary Apple M1 support.
 * See also [Linux 5.12 changes](https://kernelnewbies.org/Linux_5.12) for new features since 21.04.

As well as the usual plethora of bug fixes across the map.

## Toolchain Upgrades 🛠️

GCC was updated to the 11.2.0 release, binutils to 2.37, and glibc to 2.34. LLVM now defaults to version 13. golang defaults to version 1.17.x. rustc defaults to version 1.51.

OpenJDK 18 is now available (but not used for package builds).

## Security Improvements 🔒

nftables is now the default backend for the firewall.

## Base System
* systemd is being switched to the "unified" cgroup hierarchy (cgroup v2) by default. If for some reason you need to keep the legacy cgroup v1 hierarchy, you can select it via a kernel parameter at boot time: `systemd.unified_cgroup_hierarchy=0` ([bug 1850667](https://bugs.launchpad.net/ubuntu/+source/systemd/+bug/1850667))

## Ubuntu Desktop

* Wayland sessions are now available while using the Nvidia proprietary driver.
* [PulseAudio 15](https://www.freedesktop.org/wiki/Software/PulseAudio/Notes/15.0/) introduces support for Bluetooth LDAC and AptX codecs, as well as HFP Bluetooth profiles providing better audio quality.
  * The recovery key feature at installation time has been improved. The recovery key is now optional, stronger and editable.


### GNOME 👣

Ubuntu 21.10 includes [GNOME version 40](https://help.gnome.org/misc/release-notes/40.0/), including a new and improved Activities Overview design. Workspaces are now arranged horizontally, and the overview and app grid are accessed vertically. Each direction has accompanying keyboard shortcuts, touchpad gestures and mouse actions.

### Updated Applications
 
 * Firefox 🔥🦊 version 93 is now [seeded as a snap by default](https://discourse.ubuntu.com/t/feature-freeze-exception-seeding-the-official-firefox-snap-in-ubuntu-desktop/24210), instead of a deb package. The snap is jointly maintained by Mozilla (its publisher) and Canonical. The deb package remains available in the archive and will continue receiving updates for the lifetime of Ubuntu 21.10.
 * LibreOffice 📚 version 7.2.1
 * Thunderbird 🌩🐦 version 91.1.2

### Updated Subsystems
 
  * [PulseAudio version 15.0](https://www.freedesktop.org/wiki/Software/PulseAudio/Notes/15.0/)
  * [BlueZ version 5.60](http://www.bluez.org/release-of-bluez-5-60/)
  * [NetworkManager version 1.32.12](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/raw/08f5fdedb35c08e65028b72fa35b7b7b3daaee30/NEWS)

## Ubuntu Server

### OpenLDAP has been updated to 2.5.6

* A new OpenLDAP release, version 2.5.6, is available for Ubuntu Impish users. This release brings several changes, new features and deprecations/removals. A non-exhaustive list of things to be aware of during the upgrade process is:
  * The shell (`slapd-shell`), the BDB and the HDB backends have all been removed.
  * The `ppolicy` module now provides its own built-in schema. The external `ppolicy` schema has been removed.
  * The `nssov` module has been removed
* In certain situations, it is possible that the post-installation scripts will **not** be able to successfully migrate your current installation to new formats (e.g., when you are using an old backend like BDB/HDB). If this happens, you will be notified about the failure and the `slapd` server will **not** be (re)started; you will then have to take manual action in order to migrate your data and start the service. Please look at the [README.Debian](https://git.launchpad.net/ubuntu/+source/openldap/tree/debian/slapd.README.Debian?h=ubuntu/impish-devel) file (under `/usr/share/doc/slapd/`) for more information.

### Telegraf has been updated to 1.19.2

* This new version of Telegraf introduces some new features. It supports more SNMP v3 authentication protocols (including SHA-512); it also adds support for [DataDog distributions](https://docs.datadoghq.com/metrics/distributions/#counting-distribution-metrics) metric type.

### PHP now defaults to version 8.0.8

* Ubuntu has transitioned to the [PHP 8 runtime language](https://stitcher.io/blog/new-in-php-8), and updated the wider PHP ecosystem in Ubuntu 21.10 to use this version. New features include the JIT compiler, union types, attributes, and more.
* Users of PHP 7.4 should note that version 8.0 removes a [number of deprecated functionalities](https://wiki.php.net/rfc/deprecations_php_7_4) and when upgrading should be prepared to make the appropriate changes to their applications.

### Apache has been updated to 2.4.48

* Adds SSL related inquiry functions to the server API, to ease the identification and loading of the right SSL modules.
* Adds OCSP response provisioning as a core feature, allowing `mod_md` and `mod_ssl` to exchange X.509 digital certificate data with each other.

### QEMU was updated to the 6.0 release.

* This version adds the `ES` extension to AMD SEV which adds guest register state to the protected assets.
* Furthermore in regard to emulation RISC-V got many improvements and ARMv8.1M as well as several ARM extensions were added.
* The emulated NVMe controller is now compliant with NVMe version 1.4 and added subsystems, multipath and namespace sharing.
* See the upstream [changelog for 6.0](https://wiki.qemu.org/ChangeLog/6.0) for an overview of the many improvements and also a list of suggested replacement functionality for removed features and incompatible changes.

### Libvirt has been updated to version 7.6

* `virtio-pmem` `<memory/>` model.
* Sharing and hot-plugging of `<transient/>` disks with QEMU.
* More configurability for `virtiofs` use cases allowing an external `virtiofsd`.
* Older Hypervisor targets are no more supported dropping code for QEMU releases older than 2.11 and Xen releases older than 4.9.
* Specifying `s390-pv` as launch security type in an s390 domain prepares for running the guest in protected virtualization secure mode.
* See the upstream [Changelogs](https://libvirt.org/news.html) for the many further improvements and fixes since version 7.0 that was in [Ubuntu 21.04](https://discourse.ubuntu.com/t/hirsute-hippo-release-notes/19221).

### Open vSwitch has been updated to 2.16

* Removed support for 1024-bit Diffie-Hellman key exchange, which is now considered unsafe
* OVSDB Introduced new database service model named `relay`. Targeted to scale out read-mostly access (`ovn-controller`) to existing databases.
* Linux datapath: `ovs-vswitchd` will configure the kernel module using per-cpu dispatch mode (if available). This changes the way upcalls are delivered to user space in order to resolve a number of issues with per-vport dispatch.
* Further changes and improvements can be found in the [upstream changelog](https://www.openvswitch.org/releases/NEWS-2.16.0.txt).

### Chrony has been updated to version 4.1

* The more secure [NTS](https://ubuntu.com/server/docs/network-ntp) feature that was added in 4.0 in Ubuntu 21.04 now got various enhancements in regard to configure certificates.
* More details of what changed since version 4.0 can be found in the [upstream news page](https://chrony.tuxfamily.org/news.html).

### Bind9 has been updated to 9.16.15

* Ubuntu Impish’s BIND9 software received a [major update since hirsute’s 9.16.8](https://bind9.readthedocs.io/en/v9_16_15/notes.html#notes-for-bind-9-16-15), which includes performance improvements for zone queries, and better control over purging old keys and stale data.
* Of note, BIND9 now prefers the SPNEGO implementation from the system GSSAPI library rather than the prior ISC implementation.

### Containerd has been updated to version 1.5.5

* In this new version the support for the Node Resource Interface (NRI) was added, and it also has changes which may affect projects that import containerd. For instance, the CRI plugin moved into the main repository, and there are some API changes in the OCI library.
* More details about what changed since the former version 1.4.x can be found in the [upstream release page](https://github.com/containerd/containerd/releases) .

### Runc has been updated to version 1.0.1

* This is the first stable release of runc to be shipped in Ubuntu. As a consequence of this version update, there are some changes to the libcontainer API that break compatibility with older versions of the library.
* There are also a bunch of performance improvements and bug fixes. More details about what changed since the last Ubuntu release can be found in the [upstream release page](https://github.com/opencontainers/runc/releases).

### Corosync has been updated to version 3.1.2

* In this version, the default corosync configuration does not set the node name to `node1` as in the last Ubuntu release, instead it uses the output of `uname -n` command. If you want to keep the old behavior, check the configuration file and uncomment the needed lines.

### Fence-agents has been split into curated and non-curated agents

* There is no new upstream version in this Ubuntu release, however, the `fence-agents` package was split into `fence-agents-base` (curated agents) and `fence-agents-extra` (non-curated agents), and now `fence-agents` is a metapackage which installs all the agents. A curated agent means that the Ubuntu Server team has been validating it in a Continuous Integration system.
* For more information about the curated agents check the [Ubuntu Server guide](https://discourse.ubuntu.com/t/ubuntu-ha-pacemaker-fence-agents/24028).

### Resource-agents has been split into curated and non-curated agents

* There is no new upstream version in this Ubuntu release, however, the `resource-agents` package was split into `resource-agents-base` (curated agents) and `resource-agents-extra` (non-curated agents), and now `resource-agents` is a metapackage which installs all the agents. A curated agent means that the Ubuntu Server team has been validating it in a Continuous Integration system.
* For more information about the curated agents check the [Ubuntu Server guide](https://discourse.ubuntu.com/t/ubuntu-ha-pacemaker-resource-agents/24100).


### OpenStack

Ubuntu 21.10 includes the latest OpenStack release, Xena, including the following components:

* OpenStack Identity - Keystone
* OpenStack Imaging - Glance
* OpenStack Block Storage - Cinder
* OpenStack Compute - Nova
* OpenStack Networking - Neutron
* OpenStack Telemetry - Ceilometer, Aodh, Gnocchi
* OpenStack Orchestration - Heat
* OpenStack Dashboard - Horizon
* OpenStack Object Storage - Swift
* OpenStack DNS - Designate
* OpenStack Bare-metal - Ironic
* OpenStack Filesystem - Manila
* OpenStack Key Manager - Barbican
* OpenStack Load Balancer - Octavia
* OpenStack Instance HA - Masakari

Please refer to the [OpenStack Xena release notes](https://releases.openstack.org/xena/) for full details of this release of OpenStack.

OpenStack Xena is also provided via the [Ubuntu Cloud Archive](https://wiki.ubuntu.com/OpenStack/CloudArchive) for OpenStack Xena for Ubuntu 20.04 LTS users.

WARNING: Upgrading an OpenStack deployment is a non-trivial process and care should be taken to plan and test upgrade procedures which will be specific to each OpenStack deployment.

Make sure you read the [OpenStack Charm Release Notes](https://docs.openstack.org/charm-guide/latest) for more information about how to deploy and operate Ubuntu OpenStack using Juju.

## Platforms

### Cloud Images ☁

 * AWS EC2 AMIs use now chrony as a time sync service together with the [AWS provided timeserver](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-time.html) 
* query data EOL. Impish Indri is the last release to be contained in Cloud Images legacy querydata format. starting in 22.04, new Ubuntu versions will not be in query data. Scripts using query data should move to the currently supported file, [streams](https://cloud-images.ubuntu.com/releases/streams/v1/). Streams is supported by [simplestreams](https://code.launchpad.net/simplestreams), which is installable from source, [as a snap](https://snapcraft.io/simplestreams), or as a [debian package](https://packages.ubuntu.com/search?suite=impish&searchon=names&keywords=simplestreams).
* md5 checksum deprecation for Streams. This is a notice of the deprecation of MD5 checksums from Ubuntu Cloud Images Streams starting in 22.04. All streams currently produce sha256 checksums. Users should migrate scripts doing checksum validation to using sha256.
* MD5SUMS and SHA1SUMS file deprecation for images listed on https://cloud-images.ubuntu.com/ .  From 22.04 onwards, those files will no longer be generated. Please use the SHA256SUM files instead.

### Raspberry Pi 🍓

 * Sense HAT support added ([bug 1944450](https://bugs.launchpad.net/ubuntu/+bug/1944450) and [bug 1944449](https://bugs.launchpad.net/ubuntu/+bug/1944449)); `sudo apt install sense-hat` to install the required configuration and libraries. The Sense HAT desktop emulator is also available via `sudo apt install sense-emu-tools`.
 * u-boot removed from the boot sequence for upgraders ([bug 1936401](https://bugs.launchpad.net/ubuntu/+source/ubuntu-release-upgrader/+bug/1936401)); this also means that USB MSD boot is supported for both fresh installs *and* upgraders.
 * On server images, cloud-init now reliably operates over both ethernet and wifi ([bug 1870346](https://bugs.launchpad.net/ubuntu/+source/cloud-init/+bug/1870346)).

### s390x

Starting with Ubuntu 20.04, the minimal architectural level set was raised to z13; thus all IBM Z (and LinuxONE) hardware of generation z13 or newer, that were in service at that time, are supported. This also applies to all following Ubuntu releases (incl. 21.10), unless further notice. Support for additional future hardware might be added later on top.

IBM Z and LinuxONE / s390x-specific enhancements since 21.04 (partially not limited to s390x):

  * Like with every new Ubuntu release (respectively its kernel) the s390-tools package needs to be upgraded, this time to v2.17 ([bug 1929024](https://bugs.launchpad.net/bugs/1929024)), including zdsfs transparent data set conversion, allowing Linux to transparently read and write EBCDIC-encoded data sets as ASCII ([bug 1926749](https://bugs.launchpad.net/bugs/1926749)), the integration option for the zkey repository into an enterprise key-mangement system with a KMIP interface ([bug 1932521](https://bugs.launchpad.net/bugs/1932521)) and changes in the Secure Execution Header defaults for plaintext control flags, PCF ([bug 1932177](https://bugs.launchpad.net/bugs/1932177)).

  * In addition to moving to gcc 11.2 as default, further tool-chain updates where made, like updating to LLVM 13 (that derived s390x optimizations from 12 ([bug 1926709](https://bugs.launchpad.net/bugs/1926709)) and z15 support in Valgrind ([bug 1853271](https://bugs.launchpad.net/bugs/1853271)). 

  * And more predictable interface names for RoCE adapter were introduced, which requires kernel ([bug 1929185](https://bugs.launchpad.net/bugs/1929185)) as well as systemd changes ([bug 1929184](https://bugs.launchpad.net/bugs/1929184)).

  * Several KVM enhancements specific to s390x were picked up, like performance improvements due to Spinlock Yield Forwarding ([bug 1905021](https://bugs.launchpad.net/bugs/1905021)) and allowing KVM to let SIE interpret specification exceptions ([bug 1932157](https://bugs.launchpad.net/bugs/1932157)), adding support to indicate secure (execution) guests ([bug 1933173](https://bugs.launchpad.net/bugs/1933173)) and improved persistence in vfio-ccw device assignments in libvirt ([bug 1887929](https://bugs.launchpad.net/bugs/1887929)).

  * Another area of improvements is cryptography. With the upgrade of opencryptoki to 3.16 ([bug 1928767](https://bugs.launchpad.net/bugs/1928767)) cca token import and export of secure key objects is now supported ([bug 1913301](https://bugs.launchpad.net/bugs/1913301)), ep11 token support for attribute bound keys ([bug 1913303](https://bugs.launchpad.net/bugs/1913303)) and ep11 token protected key support ([bug 1914215](https://bugs.launchpad.net/bugs/1914215)) got added.
And with the upgrade to libica v3.8.0 ([bug 1928799](https://bugs.launchpad.net/bugs/1928799)) there are now software fallback calls to openSSL/libcrypto ([bug 1929176](https://bugs.launchpad.net/bugs/1929176)). cryptsetup got upgraded too, to v2.3.6 ([bug 1929046](https://bugs.launchpad.net/bugs/1929046)), as well as openssl-ibmca to v2.2.0 ([bug 1929052](https://bugs.launchpad.net/bugs/1929052)), that now makes the ibmca engine call libica without software fall backs (only register ibmca functions if libica confirms it as hardware function) and let ibmca do the fallback ([bug 1929175](https://bugs.launchpad.net/bugs/1929175)).
On the kernel level AP bus and zcrypt uevent extensions were added to the zcrypt driver ([bug 1933496](https://bugs.launchpad.net/bugs/1933496)) and CEX8 toleration included ([bug 1933805](https://bugs.launchpad.net/bugs/1933805)).

  * In addition preparation were included in the kernel ([bug 1932174](https://bugs.launchpad.net/bugs/1932174)) and qemu ([bug 1932175](https://bugs.launchpad.net/bugs/1932175)) for new IBM Z hardware.

  * The Query Capacity library (qclib) got bumped to it's latest version 2.3.0 ([bug 1926586](https://bugs.launchpad.net/bugs/1926586)), the upgraded glibc v2.34 library comes with several s390x related improvements ([bug 1927079](https://bugs.launchpad.net/bugs/1927079)), similar with the binutils update to v2.37 ([bug 1927080](https://bugs.launchpad.net/bugs/1927080)). On top zlib received CRC32 optimization for s390x ([bug 1932010](https://bugs.launchpad.net/bugs/1932010)) and also PCRE2 got performance and JIT improvements for s390x ([bug 1931857](https://bugs.launchpad.net/bugs/1931857)).
And upport for SMC statistics was introduced to the kernel ([bug 1853290](https://bugs.launchpad.net/bugs/1853290)) and the smc-tools package updated to it's latest v1.6.0, plus some fixes on top ([bug 1853301](https://bugs.launchpad.net/bugs/1853301)).

## Known Issues

As is to be expected, with any release, there are some significant known bugs that users may run into with this release of Ubuntu. The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:

### Linux kernel

* The version of the ZFS driver included in the 5.13.0-19 kernel [contains a bug](https://bugs.launchpad.net/bugs/1906476) that can result in filesystem corruption.  Users of ZFS are advised to wait until the first Stable Release Update of the kernel in 21.10 before upgrading. 


### Ubuntu Desktop

* The Ubuntu Desktop images can be slow to boot (taking up to 10 minutes) when booted from a USB drive on a BIOS system. The issue is being [investigated](https://bugs.launchpad.net/ubuntu/+source/casper/+bug/1922342). Once the system is installed this is not an issue.
* The Ubuntu Desktop images can be very slow to boot (taking up to 30 minutes) when booted from optical media (DVD) on a a BIOS or UEFI system. This is due to an integrity checker being run against the installation media. A workaround (setting "fsck.mode=skip") is documented in [the relevant bug](https://bugs.launchpad.net/ubuntu/+source/casper/+bug/1930880).
* A hang of the Ubuntu Desktop installer, Ubiquity, [has been observed](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1946828),  where it is scanning NTFS partitions to determine if they can be resized.  The symptom of this is a spinning ball cursor when attempting to continue past the installer 'Updates and other software' screen.  If this occurs, please reboot and try again.
* The firefox snap has [a known renderer process crash](https://bugs.launchpad.net/ubuntu/+source/firefox/+bug/1946599) when switching VTs or resuming from suspend. This is caused by the same issue that renders [WebGL non-functional in Wayland sessions](https://bugzilla.mozilla.org/show_bug.cgi?id=1732580). The problem is fixed in the upcoming 94.0 release (beta at the time impish is released), so a possible workaround is to temporarily switch the snap to the beta channel:

      snap refresh firefox --beta

* If you have Chromium and Firefox installed before upgrading to Ubuntu 21.10, your default browser (called via x-www-browser, x-gnome-browser, or sensible-browser) will be Chromium. For details on how to set your default browser to Firefox see [this forum post](https://forum.snapcraft.io/t/firefox-snap-cannot-be-set-as-default-browser/26636).

### Ubuntu Server

Nothing yet.

## Platforms

### Cloud Images

None
 
### Raspberry Pi

* On Ubuntu Desktop images for the Raspberry Pi there is an issue with the full KMS support that causes the HDMI output to stop working (this appears to be particularly prevalent on monitors with higher refresh rates, i.e. 100+ Hz) ([bug 1946368](https://bugs.launchpad.net/bugs/1946368)). To work around the issue:
  -  Insert the SD card in another machine
  - On the first (or only) partition labelled "system-boot" open the `config.txt` file in a text editor
  - Find the line: `dtoverlay=vc4-kms-v3d`
  - Change this line to: `dtoverlay=vc4-fkms-v3d` (i.e. change `kms` to `fkms`)
  - Save the file, and safely remove the SD card
  - Please be aware that other workarounds may be necessary under the `fkms` overlay (see [bug 1899953](https://bugs.launchpad.net/ubuntu/+source/pulseaudio/+bug/1899953) for example), depending on your desktop requirements
* Various kernel modules have been moved from the `linux-modules-raspi` package in order to reduce the initramfs size. This results in several applications (most notably Docker, [bug 1947601](https://bugs.launchpad.net/ubuntu/+source/linux-raspi/+bug/1947601)) failing due to missing kernel modules. To work around this:
  - `sudo apt install linux-modules-extra-raspi`
* The [Raspberry Pi Compute Module 3](https://www.raspberrypi.com/products/compute-module-3/) is no longer supported as of this release, due to a lack of storage capacity (the CM3 shipped with 4GB of on-board eMMC storage, and Ubuntu Server for Raspberry Pi images now exceed this size). The later [Compute Module 3+](https://www.raspberrypi.com/products/compute-module-3-plus/) models (for which the smallest storage capacity was 8GB of eMMC) are still supported.

### s390X

Nothing yet.

### General

* This is not an issue per-se, but enough visible to be release-note worthy. Starting with 20.04.3 useradd will not allow creating full-numeric usernames (e.g. 123, 1337). Such usernames cause issues with components such as systemd, so it was safer to disallow them altogether ([bug 1927078](https://bugs.launchpad.net/bugs/1927078)).
* After installing a Xubuntu system during the shutdown process you will not see a message about removing the installation media and pressing enter, instead you might just see a Xubuntu logo, a black screen with an underscore in the upper left hand corner, or just a black screen. If you press enter the system will reboot though. ([bug 1944519](https://bugs.launchpad.net/ubuntu-release-notes/+bug/1944519))

## Official flavours

The release notes for the official flavours can be found at the following links:

  * [Kubuntu Release Notes](https://wiki.ubuntu.com/ImpishIndri/Beta/Kubuntu)
  * [Lubuntu Release Notes](https://discourse.lubuntu.me/t/lubuntu-21-10-impish-indri-release-notes/2786)
  * [Ubuntu Budgie Release Notes](https://ubuntubudgie.org/2021/09/ubuntu-budgie-21-10-release-notes/)
  * [Ubuntu Kylin Release Notes](https://wiki.ubuntu.com/ImpishIndri/ReleaseNotes/UbuntuKylin)
  * [Ubuntu MATE Release Notes](https://ubuntu-mate.org/blog/ubuntu-mate-impish-indri-final-release/)
  * [Ubuntu Studio Release Notes](https://ubuntustudio.org/ubuntu-studio-21-10-release-notes/)
  * [Xubuntu Release Notes](https://wiki.xubuntu.org/releases/21.10/release-notes)
