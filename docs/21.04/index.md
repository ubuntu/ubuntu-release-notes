---
tocdepth: 3
---

<!-- SOURCE: https://discourse.ubuntu.com/t/hirsute-hippo-draft-release-notes/19221 -->

(ubuntu-21-04-release-notes)=
# Ubuntu 21.04 release notes

## Introduction

These release notes for **Ubuntu 21.04** (Hirsute Hippo) provide an overview of the release and document the known issues with Ubuntu and its flavours.

## Dedication

Subscribers to the `ubuntu-announce` mailing list and long term participants in the Ubuntu community will have come across Adam Conrad’s work. Adam, known in the community as *infinity*, was a long-term member of the release team and colleague to many of us at Canonical. As a member of the release team, Adam was responsible for devising many of the processes and tools which we use today, and (whether he wanted to or not) teaching his fellow members the ropes. Adam passed away earlier this year after being unwell for some time. The Ubuntu Release Team dedicates 21.04 “Hirsute Hippo” to our colleague and friend *infinity*. He is missed and will live in our hearts forever.

## Support lifespan

Ubuntu 21.04 will be supported for 9 months until January 2022. If you need Long Term Support, it is recommended you use [Ubuntu 20.04 LTS](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes/) instead.

## Get Ubuntu 21.04

## Download Ubuntu 21.04

Images can be downloaded from a location near you.

You can download ISOs and flashable images from:

  * [Ubuntu Desktop and Server for 64-bit x86 (AMD64) ](http://releases.ubuntu.com/21.04/)
  * [Less Frequently Downloaded Ubuntu Images](http://cdimage.ubuntu.com/ubuntu/releases/21.04/release/)
  * [Ubuntu Cloud Images](http://cloud-images.ubuntu.com/daily/server/hirsute/current/)
  * [Lubuntu](http://cdimage.ubuntu.com/lubuntu/releases/21.04/release/)
  * [Kubuntu](http://cdimage.ubuntu.com/kubuntu/releases/21.04/release/)
  * [Ubuntu Budgie](http://cdimage.ubuntu.com/ubuntu-budgie/releases/21.04/release/)
  * [Ubuntu Kylin](http://cdimage.ubuntu.com/ubuntukylin/releases/21.04/release/)
  * [Ubuntu MATE](http://cdimage.ubuntu.com/ubuntu-mate/releases/21.04/release/)
  * [Ubuntu Studio](http://cdimage.ubuntu.com/ubuntustudio/releases/21.04/release/)
  * [Xubuntu](http://cdimage.ubuntu.com/xubuntu/releases/21.04/release/)

<!--
2021-04-21 Release upgrades have not been enabled due to bug 1925010.

== Upgrading from Ubuntu 20.10 ==

To upgrade on a desktop system:

  * Open the "Software & Updates" Setting in System Settings.
  * Select the 3rd Tab called "Updates".
  * Set the "Notify me of a new Ubuntu version" dropdown menu to "For any new version".
  * Press <kbd>Alt</kbd>+ <kbd>F2</kbd> and type in `update-manager -c` into the command box.
    * Update Manager should open up and tell you: **"New distribution release '21.04' is available."**
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
-->

## New features in 21.04

## Updated Packages

### Linux kernel 🐧

Ubuntu 21.04 includes the **5.11** Linux kernel. This includes numerous updates and added support since the 5.8 Linux kernel released in Ubuntu 20.10. Some notable examples include:

* Better anonymous memory management to reduce swapping
* New cgroup slab controller which allows sharing of slab memory between cgroups
* Proactive memory compaction to reduce latency for huge-page allocations under fragmented memory conditions
* Support for running BPF programs on socket lookups
* FSGSBASE support to improve context switch performance on x86 processors
* Support for using Intel SGX to create encrypted enclaves
* Support for running SEV-ES guests under KVM to protect guest register state from the hypervisor
* Support for extended attributes in NFS
* fsync() performance improvements for ext4 and btrfs
* Btrfs performance and data recovery improvements
* io_uring restriction support to facilitate secure sharing of rings to less-trusted processes
* virtio-fs DAX support to improve performance and reduce memory consumption
* Intel Rocketlake and DG1 graphics support
* AMD Vangogh, Green Sardine, and Dimgrey Cavefish graphics support

## Toolchain Upgrades 🛠️

GCC was updated to the 10.3.0 release, binutils to 2.36.1, and glibc to 2.33. Python now ships at version 3.9.4, Perl at version 5.32.1. LLVM now defaults to version 12.  golang defaults to version 1.16.x. rustc defaults to version 1.50.

In addition to OpenJDK 11, OpenJDK 16 is now provided (but not used for package builds).

Ruby was updated from v2.7.0 to v2.7.2, and rubygems has been extracted from ruby2.7 source and is provided as a [separate package](https://launchpad.net/ubuntu/+source/rubygems/).

## Security Improvements 🔒

Secureboot on x86_64 (amd64) and AArch64 (arm64) have been improved to include SBAT capable shim, grub2, fwupd. For more details see [this discourse post](https://discourse.ubuntu.com/t/grub2-secureboot-bypass-2021-and-one-grub/21200).

nftables is now the default backend for the firewall.

## Ubuntu Desktop
 - Added support for smartcard authentication (via [`pam_sss`](http://manpages.ubuntu.com/manpages/bionic/man8/pam_sss.8.html))
 - Wayland is now the default on most configurations, which features better security and performance
 - The desktop view now properly handles drag and drop interactions, e.g. dragging from/to the file manager
 - The power profile mode can now be changed from the settings (on configuration where there is proper kernel support)
 - Pipewire support is now enabled which restore working screen recording and allow better audio handling for sandboxed applications
 - The installer includes support for specifying a recovery key, which can be used to decrypt the disk if the password is forgotten
 - The Active Directory integration has been improved. User authentication with GPO enabled works out of the box after installation. It also includes a [Group Policy client (ADSys)](https://github.com/ubuntu/adsys/) to configure various settings from a central AD controller.

### GNOME 👣

While the new shell version hasn't been included yet in Ubuntu the applications have been mostly updated to their GNOME 40 versions.

### Updated Applications
 
 * Firefox 🔥🦊 version 87
 * LibreOffice 📚 version 7.1.2-rc2
 * Thunderbird 🌩🐦 version 78.8.1

### Updated Subsystems

* PulseAudio 14
* BlueZ 5.56
* NetworkManager 1.30

## Ubuntu Server

### Rails 6

This release brings you Rails 6! For users coming from Ubuntu 20.04, they can now enjoy the newer version of Rails, moving from v5.2.3 to v6.0.3.5. Some of the exciting features include the new Action Mailbox, Action Text, Parallel Testing, Action Cable Testing, support for Host Authorization, and so on.

For more details, check the upstream’s [Rails 6 release notes](https://guides.rubyonrails.org/6_0_release_notes.html). And if you need help to upgrade your Ruby on Rails application, please take a look at their [upgrading Rails guide](https://guides.rubyonrails.org/upgrading_ruby_on_rails.html).





### QEMU was updated to the 5.2 release.

*   One noteworthy new feature is the addition of a first version of [virtio-mem](https://virtio-mem.gitlab.io/) which allows which allows fine-grained, NUMA-aware memory hot(un)plug for VMs, avoiding many limitations known from memory ballooning (virtio-balloon)
*   Furthermore RISC-V emulation made major steps adding various further CPU types.
*   See the upstream changelog for [5.1](https://wiki.qemu.org/ChangeLog/5.1) and [5.2](https://wiki.qemu.org/ChangeLog/5.2) for an overview of the many improvements.


### Libvirt has been updated to version 7.0.

*   Since Libvirt 6.10 TLS based connections will  do client TLS certificate validation by default for `chardev`, `migration`, and `backup` servers
*   Since 6.9.0 one can use transient disks and vdpa devices with the qemu hypervisor
*   Since 6.7.0 iSCSI passthrough devices can also configure an initiator
*   See the upstream [Changelogs](https://libvirt.org/news.html) for the many improvements and fixes since version 6.6 that was in [Groovy](https://discourse.ubuntu.com/t/groovy-gorilla-release-notes/15533).


### DPDK was updated to 20.11.1

*   Various new features and drivers can be found in the [20.11 release notes](http://doc.dpdk.org/guides/rel_notes/release_20_11.html)
*   Hirsute ships with [20.11.1](https://doc.dpdk.org/guides-20.11/rel_notes/release_20_11.html#release-notes) already being the first stable release of the 20.11 series.


### Open vSwitch has been updated to 2.15

*   The ovsdb transaction format in the database files has been changed. New ovsdb-server process will be able to read old database format, but old processes will *fail* to read database created by the new one. For cluster and active-backup service models follow upgrade instructions in 'Upgrading from version 2.14 and earlier to 2.15 and later' section of ovsdb(7).
*   Further changes and improvements can be found in the [changelog](https://www.openvswitch.org/releases/NEWS-2.15.0.txt)


### Chrony has been updated to version 4.0

*   Chronyd's configuration can now be fragmented. Please see
    /etc/chrony/conf.d/README for more information.
*   NTP sources can be specified in /etc/chrony/sources.d. Please see          
    /etc/chrony/sources.d/README for more information.
*   The seccomp filtering was further improved and is now enabled by default
*   Better security with AES-CMAC keys (AES128, AES256) via  Nettle and support for Network Time Security (NTS) authentication
*   More details what changed since the former version 3.5 can be found on the[ upstreams news page](https://chrony.tuxfamily.org/news.html).


### Strongswan has been updated to 5.9.1

*   AEAD algorithms are now preferred for ESP and therefore openvpn puts AES-GCM in a default AEAD proposal in front of the previous default proposal
*   Various fixes for the Networkmanager frontend and backend
*   These and more changes since the former 5.8.4 can be found in [the upstream changelog](https://wiki.strongswan.org/projects/strongswan/wiki/Changelog59)


### Openvpn has been updated to 2.5.1

*   Connection setup is now much faster
*   Improved TLS 1.3
*   Better Asynchronous (deferred) support for authentication, client-connect scripts and plugins
*   802.1q VLAN support on TAP servers
*   IPv6-only tunnels
*   These and many more changes since the 2.4.x series can be read in detail in [the upstream changelog of the 2.5 series](https://community.openvpn.net/openvpn/wiki/ChangesInOpenvpn25)


### Virt-manager has been updated to 3.2.0

*   Generally the UI flow has been streamlined (rare options got removed) but that isn’t dropping those features entirely - anything else that comes to mind can be addressed via the now stable builtin XML editor.
*   Details can be found on the [news page of the upstream project](https://github.com/virt-manager/virt-manager/blob/master/NEWS.md).


### Postgresql has been updated to v13.2

*   This update contains many new features and enhancements, including:
    *   Space savings and performance gains from de-duplication of B-tree index entries
    *   Improved performance for queries that use aggregates or partitioned tables
    *   Better query planning when using extended statistics
    *   Parallelized vacuuming of indexes
    *   Incremental sorting
*   These and a long list of further enhancements as well as bug fixes can be found in the release notes of [v13.0](https://www.postgresql.org/docs/release/13.0/), [v13.1](https://www.postgresql.org/docs/release/13.1/) and [v13.2](https://www.postgresql.org/docs/release/13.2/)


### Samba has been updated to 4.13.3

*   Samba’s original domain controller mode has been deprecated. Sites using Samba as a Domain Controller should upgrade from the NT4-like ‘classic’ Domain Controller to a Samba Active Directory Domain Controller to ensure full operation with modern Windows clients.
*   SMBv1-only protocol options have been deprecated. A number of smb.conf parameters for less-secure authentication methods which are only possible over SMBv1 are deprecated in this release.


### SSSD has been updated to 2.40

*   Support for libnss has been dropped.  SSSD now supports only openssl cryptography.


### Net-SNMP has been updated to 5.9

*   Support for OpenSSL 1.1.1 has been added.


### Rsyslog has been updated to 8.2102.0

*   A new module “imhttp” has been added, which allows rsyslog to receive log data via HTTP.


### Containerd has been updated to 1.4.4

*   Support cgroups v2
*   Improved SELinux support
*   Deprecate io.containerd.runtime.v1.* and io.containerd.runc.v1


### Runc has been updated to 1.0.0-rc93

*   Support cgroups v2
*   Special handling for seccomp profiles to avoid making new syscalls unusable for glibc
*   Various rootless containers improvements


### Docker.io has been updated to 20.10.2

*   Support cgroups v2
*   Deprecate aufs storage driver. For more deprecations take a look at [Deprecated Engine Features](https://docs.docker.com/engine/deprecated/)


### Targetcli-fb replaces tgt

*   Already in Ubuntu 20.10 [targetcli-fb](https://github.com/open-iscsi/targetcli-fb) which controls the [kernels LIO support](http://linux-iscsi.org/wiki/Main_Page) was fully supported. That was the first step to replace the aging [tgt](http://stgt.sourceforge.net/). Now in 21.04 the last remaining ties to tgt were cut (and thereby tgt got demoted) making targetcli-fb the single recommended tool to provide iSCSI targets.
*   Compared to tgt It provides better performance for iSCSI targets, full SCSI 3 reservations (for clustering) and a multitude of further features missing from the narrower implementation of tgt.


### Other noteworthy changes

* [needrestart](https://discourse.ubuntu.com/t/needrestart-for-servers/21552) is installed by default on Ubuntu Server.

 * The nginx lua module has been removed as the latest upstream version of this module no longer works with Nginx directly. See [bug 1893753](https://bugs.launchpad.net/ubuntu/+source/nginx/+bug/1893753) for details.


### OpenStack

Ubuntu 21.04 includes the latest OpenStack release, Wallaby, including the following components:

* OpenStack Identity - Keystone
* OpenStack Imaging - Glance
* OpenStack Block Storage - Cinder
* OpenStack Compute - Nova
* OpenStack Networking - Neutron
* OpenStack Telemetry - Ceilometer, Aodh, Gnocchi, and Panko
* OpenStack Orchestration - Heat
* OpenStack Dashboard - Horizon
* OpenStack Object Storage - Swift
* OpenStack DNS - Designate
* OpenStack Bare-metal - Ironic
* OpenStack Filesystem - Manila
* OpenStack Key Manager - Barbican
* OpenStack Load Balancer - Octavia
* OpenStack Instance HA - Masakari

Please refer to the [OpenStack Wallaby release notes](https://releases.openstack.org/wallaby/) for full details of this release of OpenStack.

OpenStack Wallaby is also provided via the [Ubuntu Cloud Archive](https://wiki.ubuntu.com/OpenStack/CloudArchive) for OpenStack Wallaby for Ubuntu 20.04 LTS users.

WARNING: Upgrading an OpenStack deployment is a non-trivial process and care should be taken to plan and test upgrade procedures which will be specific to each OpenStack deployment.

Make sure you read the [OpenStack Charm Release Notes](https://docs.openstack.org/charm-guide/latest) for more information about how to deploy and operate Ubuntu OpenStack using Juju.

<!--
### Kubernetes

tbc
-->

## Platforms

### Cloud Images ☁

The [AWS SSM Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) now provides a way for users to find the latest AMI for Ubuntu releases. See [this discourse post](https://discourse.ubuntu.com/t/finding-ubuntu-images-with-the-aws-ssm-parameter-store/15507/3) for more details.

Google Cloud Platform images now include the [Google OS Config Agent](https://cloud.google.com/compute/docs/os-config-management).

Azure images will use /dev/ptp_hyperv as the main PTP refclock, to avoid conflicts with other PTP devices. ([LP: #1913763](https://bugs.launchpad.net/ubuntu/groovy/+source/systemd/+bug/1913763))

### Raspberry Pi 🍓

* Support for accelerated Wayland-based desktop
* Support for GPIO via libgpiod and the new liblgpio ([bug 1916901](https://bugs.launchpad.net/ubuntu/+bug/1916901)), and an updated gpiozero library with liblgpio support integrated
* Support for WiFi and Bluetooth on the Compute Module 4 ([bug 1912905](https://bugs.launchpad.net/ubuntu/+source/linux-raspi/+bug/1912905) and [bug 1921915](https://bugs.launchpad.net/ubuntu/+source/pi-bluetooth/+bug/1921915))

### RISC-V 5️⃣

* HiFive SiFive Unleashed and HiFive SiFive Unmatched images are now available. See [wiki](https://wiki.ubuntu.com/RISC-V) for more details.
* Both image are usable in QEMU, however currently requires u-boot-qemu from Hirsute.

### s390x

IBM Z and LinuxONE / s390x-specific enhancements since 20.10 (partially not limited to s390x):

  * SMC-D v2 support was added to the kernel ([bug 1853291](https://bugs.launchpad.net/bugs/1853291)) which enables docker connectivity. The smc-tools were upgraded to 1.5.0 ([bug 1914034](https://bugs.launchpad.net/bugs/1914034)), SMC-R Link Group (LG) support added to the kernel ([bug 1905023](https://bugs.launchpad.net/bugs/1905023)) and the s390-tools ([bug 1887932](https://bugs.launchpad.net/bugs/1887932)), and wireshark was updated to include SMC support ([bug 1887933](https://bugs.launchpad.net/bugs/1887933)).

  * Support for HiperSockets/Ethernet Converged Interfaces was added to the kernel ([bug 1853286](https://bugs.launchpad.net/bugs/1853286)) and s390-tools ([bug 1891514](https://bugs.launchpad.net/bugs/1891514)), now allowing to form a single LAN based on HiperSockets and OSA/RoCE interfaces. The network configuration is simplified with a single network interface and provides the ability to communicate with z/OS hosts using HiperSockets Layer 2.

  * Several virtualization stack improvements were added like enablement for enhanced hardware diagnose data of guest kernel ([bug 1853313](https://bugs.launchpad.net/bugs/1853313)) and qemu ([bug 1853314](https://bugs.launchpad.net/bugs/1853314)), full implementation of zPCI function properties in kernel ([bug 1887923](https://bugs.launchpad.net/bugs/1887923)) and qemu ([bug 1887922](https://bugs.launchpad.net/bugs/1887922)), support for virtio-fs was added ([bug 1887924](https://bugs.launchpad.net/bugs/1887924)) as well as libvirt node device driver support for DASD ([bug 1904701](https://bugs.launchpad.net/bugs/1904701)) and for vfio-ap matrix device ([bug 1905019](https://bugs.launchpad.net/bugs/1905019)). In addition host key document verification for s390-tools genprotimg was added ([bug 1882807](https://bugs.launchpad.net/bugs/1882807)).

  * The NVMe support was expanded with IPL Load Normal support in kernel ([bug 1887921](https://bugs.launchpad.net/bugs/1887921)) and s390-tools ([bug 1887920](https://bugs.launchpad.net/bugs/1887920)) and stand-alone dump support again in kernel ([bug 1887940](https://bugs.launchpad.net/bugs/1887940)) and s390-tools ([bug 1892824](https://bugs.launchpad.net/bugs/1892824)).

  * Log DASD EDIF capability was added to the kernel ([bug 1853275](https://bugs.launchpad.net/bugs/1853275)) and s390-tools ([bug 1853276](https://bugs.launchpad.net/bugs/1853276)).

  * Valgrind was updated to v3.16.1 ([bug 1825343](https://bugs.launchpad.net/bugs/1825343)) with additional IBM Z support (z14).

  * The Server Time Protocol (STP) leap second handling was adjusted that required kernel ([bug 1902046](https://bugs.launchpad.net/bugs/1902046)) and s390-tools ([bug 1902047](https://bugs.launchpad.net/bugs/1902047)) changes.

  * The s390-tools were updated to latest version 2.16.0 ([bug 1914574](https://bugs.launchpad.net/bugs/1914574)), which includes zkey integration with EKMF stage1 ([bug 1887806](https://bugs.launchpad.net/bugs/1887806)) and zkey LUKS2 enhancements ([bug 1914214](https://bugs.launchpad.net/bugs/1914214)).

  * The zcrypt device driver was improved to provide indications that ap bus initialization and bindings are complete ([bug 1901674](https://bugs.launchpad.net/bugs/1901674)), additional state for 'offline due to error' was added to the kernel ([bug 1902866](https://bugs.launchpad.net/bugs/1902866)) and the s390-tools ([bug 1902865](https://bugs.launchpad.net/bugs/1902865)) and EP11 related enhancements for the pkey module and the zkey tool were done ([bug 1902862](https://bugs.launchpad.net/bugs/1902862)). Opencryptoki was bumped to the latest version 3.15.1 with patches on top ([bug 1906369](https://bugs.launchpad.net/bugs/1906369)), including PKCS #11 3.0 baseline provider support ([bug 1904558](https://bugs.launchpad.net/bugs/1904558)), enhanced EP11 token functionality ([bug 1904560](https://bugs.launchpad.net/bugs/1904560)) and improved key management tool support for key deletion ([bug 1904561](https://bugs.launchpad.net/bugs/1904561)).

  * qclib was upgraded to latest version 2.2.1 ([bug 1902870](https://bugs.launchpad.net/bugs/1902870)), that includes utility commands for displaying the virtualization stack and info about the hardware platform ([bug 1902874](https://bugs.launchpad.net/bugs/1902874)).

  * Additional s390x specific improvements were added to binutils v2.35.1 ([bug 1903874](https://bugs.launchpad.net/bugs/1903874)) and OpenBLAS v0.3.12 ([bug 1904194](https://bugs.launchpad.net/bugs/1904194)).

  * Missing kernel debug infos for the decompressor stage were added to the kernel-debug package ([bug 1905020](https://bugs.launchpad.net/bugs/1905020)) and some kernel config options were adjusted ([bug 1906370](https://bugs.launchpad.net/bugs/1906370)) and ([bug 1908414](https://bugs.launchpad.net/bugs/1908414)).

  * By making use of SCLP's 'extended-length-SCCB facility' to read SCP and CPU info, current 4k limitations are solved and the preparation for future hardware take its course ([bug 1925030](https://bugs.launchpad.net/bugs/1925030)).

  * Several installer enhancements were added (that largely also landed in 20.04.2), like DASD FBA fixes and support ([bug 1885890](https://bugs.launchpad.net/bugs/1885890)), ([bug 1876011](https://bugs.launchpad.net/bugs/1876011)) and ([bug 1899692](https://bugs.launchpad.net/bugs/1899692)), DASD ECKD pass over via virtio-blk support ([bug 1893775](https://bugs.launchpad.net/bugs/1893775)), low-level DASD ECKD format support ([bug 1887669](https://bugs.launchpad.net/bugs/1887669)), DASD ECKD ModA EAV ([bug 1887669](https://bugs.launchpad.net/bugs/1887669)) and EAV-II support ([bug 1878596](https://bugs.launchpad.net/bugs/1878596)), refinements in LVM handing ([bug 1905412](https://bugs.launchpad.net/bugs/1905412)) and installer update improvements ([bug 1921820](https://bugs.launchpad.net/bugs/1921820)).

## Phased updates in APT
APT now respects phased updates, see the [Phased updates in APT 21.04](https://discourse.ubuntu.com/t/phased-updates-in-apt-in-21-04/20345) thread for more details.

## popularity-contest
The package popularity-contest is no longer seeded and is not configured to submit information to popcon.ubuntu.com as the client and server have been broken for multiple releases of Ubuntu.


## Known Issues

As is to be expected, with any release, there are some significant known bugs that users may run into with this release of Ubuntu. The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:

### Linux kernel

 * [s390x KVM guests only] Hirsute KVM guests do not react correctly to the detachment of KVM disks initiated from the host, leaving stale block devices that can cause hung processes. It is advisable to defer upgrading s390x KVM guests to Hirsute until [bug 1925211](https://bugs.launchpad.net/ubuntu/+source/systemd/+bug/1925211) is fixed if disks are to be detached from the VM.

* KVM postcopy migration will - with the new default settings of kernel v5.11 - no more work out of the box. This is due to [userfaultfd: add user-mode only option to unprivileged_userfaultfd sysctl knob](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=d0d4730ac2) which for security reasons has a default that prohibits this kind of  migrations. If an admin wants to enable unrestricted userfaults he can do so via `sudo sysctl -w "vm.unprivileged_userfaultfd=1"` then postcopy migrations will work again.

### Ubuntu Desktop

* On a system which uses Broadcom wireless if you enable the wireless driver before installing Ubuntu then the drivers will not be available on the installed system. To workaround this do not enable the wireless driver before installation. ([bug 1923477](https://bugs.launchpad.net/ubuntu-release-notes/+bug/1923477))

*  Audio doesn't work on systems with Intel Soundwire. However HDMI, Bluetooth or USB devices work fine:
   * [No sound output/input available after installing 21.04](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1924685)
   * [Internal speaker doesn't work after plug in a headset](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1924717)
* [VMWare Player "Easy Install" stops on the "Prepare" page of the installer](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1925130). The user must click on "Continue" to continue the installation automatically. 

## Platforms

### Cloud Images

* When launching Azure Virtual Machines with accelerated networking enabled, public key(s) might not be deployed correctly on the instance. Please see [bug 1919177](https://bugs.launchpad.net/cloud-init/+bug/1919177) for more information.

### Container images

* Due to changes in glibc 2.33 Ubuntu 21.04 container images require updated container runtimes.
All widely used container runtimes shipped in supported versions of Ubuntu have been updated via the standard stable release updates procedure.
Container hosts running other operating systems may need manual updates. ([bug 1916485](https://bugs.launchpad.net/ubuntu/+source/libseccomp/+bug/1916485))

### Raspberry Pi

* After initial user setup on the desktop image, the desktop will be running X11. Restart to login to a Wayland session ([bug 1925483](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1925483))
* After initial user setup on the desktop image, several packages can still be autoremoved ([bug 1925265](https://bugs.launchpad.net/ubuntu/+source/ubuntu-meta/+bug/1925265)); run `sudo apt autoremove` to work around this
* The FKMS overlay has been switched to KMS on the desktop image to fix corruption of X11 applications; this affects the display functionality of the Raspberry Pi camera applications (`raspivid` and `raspistill` from the `libraspberrypi-bin` package). As a result the camera firmware is disabled in `config.txt` (and will be disabled, if found, for upgraders from Groovy). You may enable it again, and recording / capture functionality of these applications should work but be aware that preview will not
* On the desktop image, the wrong audio output device is selected on each boot. A workaround is available in the bug report ([bug 1899962](https://bugs.launchpad.net/ubuntu/+source/pulseaudio/+bug/1899962))
* On the desktop image, the default user does not belong to the "dialout" group with the result that they do not have non-root access to the GPIO pins ([bug 1923363](https://bugs.launchpad.net/ubuntu/+source/user-setup/+bug/1923363)); run `sudo adduser $USER dialout` then logout and login if you wish to work around this
* On the Pi Foundation’s IO Board for the Compute Module 4, the USB ports are routed to the DWC2 USB2 controller (which is attached to the USB-C port on the Pi 4). This is not in host-mode by default meaning that keyboards (and other devices) will not work. Add the following line to the `config.txt` in order to enable the USB ports on the IO board:
  ```
  dtoverlay=dwc2,dr_mode=host
  ```
  A commented out instance of this line can be found in `config.txt` by default.
* On the server image, the "overlay_map" device-tree is in the wrong location on the boot partition until the first run of "flash-kernel" ([bug 1922779](https://bugs.launchpad.net/ubuntu/+source/linux-raspi/+bug/1922779)); run `sudo flash-kernel` to work around this.

### RISC-V
* Reboot and shutdown commands do not currently work on the HiFive Unmatched. Power cycling requires physical access to the board. ([bug 1937055](https://bugs.launchpad.net/ubuntu/+source/opensbi/+bug/1937055))

## Official flavours

The release notes for the official flavours can be found at the following links:

  * [Kubuntu Release Notes](https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/Kubuntu)
  * [Lubuntu Release Notes](https://lubuntu.me/hirsute-released/)
  * [Ubuntu Budgie Release Notes](https://ubuntubudgie.org/2021/04/ubuntu-budgie-21-04-release-notes/)
  * [Ubuntu Kylin Release Notes](https://wiki.ubuntu.com/HirsuteHippo/ReleaseNotes/UbuntuKylin)
  * [Ubuntu MATE Release Notes](https://ubuntu-mate.org/)
  * [Ubuntu Studio Release Notes](https://ubuntustudio.org/21-04-release-notes/)
  * [Xubuntu Release Notes](https://wiki.xubuntu.org/releases/21.04/release-notes)
