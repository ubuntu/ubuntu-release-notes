---
tocdepth: 3
---

<!-- SOURCE: https://discourse.ubuntu.com/t/lunar-lobster-release-notes/31910 -->

(ubuntu-23-04-release-notes)=
# Ubuntu 23.04 release notes

## Introduction

These release notes for **Ubuntu 23.04** (Lunar Lobster) provide an overview of the release and document the known issues with Ubuntu and its flavours.

## Support lifespan

Ubuntu 23.04 will be supported for 9 months until January 2024. If you need Long Term Support, it is recommended you use [Ubuntu 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes/) instead.

## New features in 23.04

## Updated Packages

### Linux kernel 🐧

Ubuntu 23.04 is shipped with the new 6.2 Linux kernel that brings many new features.

Notable Ubuntu kernel features:
 - Support to build and run [out-of-tree Rust 🦀 modules](https://discourse.ubuntu.com/t/ubuntu-kernel-is-getting-rusty-in-lunar/34977) with generic and lowlatency kernels
 - Newer LSM stacking and AppArmor patch set

Notable [upstream](https://kernelnewbies.org/Linux_6.2) kernel features:
 - Performance boost for Older Intel Skylake CPUs with Call Depth Tracking
 - Support for Intel Arc graphics DG2/Alchemist
 - New Intel TDX guest driver
 - Support for Sony DualShock 4 gamepads
 - Updated zstd compression code
 - Miscellaneous BPF improvements 
 - New hardware support, various performance and security improvements

### systemd v252.5

The init system was updated to systemd v252.5. Please refer to the upstream [changelog ](https://github.com/systemd/systemd/releases/tag/v252) for more information about individual features.

## Toolchain Upgrades 🛠️

### OpenJDK 
The default Java runtime and JDK were updated to OpenJDK v17. Java 17 is the latest LTS version.

### .Net
.Net v7 (7.0.105)runtime and related packages were added. .Net v6 packages were updated to the latest monthly release 6.0.116

### golang
The go language compiler was updated to v1.20, which the latest upstream stable version.

### Rust
The rustc compiler was updated to v1.67 and the cargo package manager was updated to 0.68

### Python
Python was updated to v3.11

### debuginfod service

A lot of work has been done during this cycle to improve our [debuginfod service](https://debuginfod.ubuntu.com).

* The service now indexes and serves source-code for a considerable number of packages (those that honor `dpkg-buildflags` during build time).  Ultimately, this means that users will not need to manually download a package's source-code (using `apt-get source`, for example), nor will they need to fiddle with GDB's `dir` or `set substitute-path` commands.  Source-code fetching will be done transparently by the debugger, which will save a considerable amount of time.

* The service is now able to index and service debugging artifacts from private PPAs.  Currently, it only indexes the [ESM](https://ubuntu.com/security/esm) PPAs.

* The rate at which the service indexes new `ddebs` and source-code has been improved.

### Ruby 

Ruby 💎 was updated from v3.0 to v3.1. More details in its section below.

## Security Improvements 🔒

The ca-certificates package has been updated to the 2.60 version of the Mozilla certificate authority bundle.

## Base System

### Netplan [v0.106](https://discourse.ubuntu.com/t/netplan-0-106-call-for-testing/33932)
- Slight change in behavior when matching a (physical) interface by using the `match.macaddress` stanza, using **PermanentMACAddress=** matching over simple **MACAddress=** matching, which might affect interface matching in certain containers or VMs.
- A new `netplan status` subcommand is implemented to query the systems current networking state.

## Ubuntu Desktop

### New Installer
- The default Ubuntu Desktop installer is now a Flutter app backed by subiquity and packaged as a snap
- The Minimal install is now faster than the Full install which wasn't true with the old installer.
- Installs the available security updates on the target system
- [MOK Enrollment](https://wiki.ubuntu.com/UEFI/SecureBoot#MOK_generation_and_signing_process) is not yet supported.  While `ubuntu-drivers` will be run if the "Install third-party software" checkbox is selected, drivers that also required MOK enrollment will need to do so after installation is complete.
- The legacy installer is [still available](https://cdimage.ubuntu.com/releases/23.04/) in case of issues with the new installer.

### GNOME 👣
- GNOME has been updated to include new features and fixes from the latest GNOME release, [GNOME 44](https://release.gnome.org/44/)

### Updated Ubuntu font

- The Ubuntu font has been updated

### Updated Applications
-  [Firefox](https://mozilla.org/firefox/releases/) 111 🔥🦊
- [LibreOffice 7.5.2 ](https://wiki.documentfoundation.org/ReleaseNotes/7.5.2) 📚
  LibreOffice is now available on RISC-V
- Thunderbird 102.10 🌩️🐦

### Updated Subsystems

* [BlueZ 5.66 ](https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/ChangeLog?id=5.66)
* [new cups-filters](https://openprinting.github.io/cups-filters-Second-Generation-First-Beta-Release/)
* [NetworkManager 1.42 ](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/blob/nm-1-42/NEWS)
* [Pipewire 0.3.65](https://gitlab.freedesktop.org/pipewire/pipewire/-/blob/0.3.65/NEWS)
* [Poppler 22.12](https://gitlab.freedesktop.org/poppler/poppler/-/blob/poppler-22.12.0/NEWS)
* [xdg-desktop-portal 1.16](https://github.com/flatpak/xdg-desktop-portal/blob/1.16.0/NEWS)

### New Active Directory features

Active Directory (AD) Integration is one of the most popular Ubuntu Desktop enterprise features and Ubuntu Desktop 22.04 LTS brought Active Directory integration to the next level through [ADsys](https://github.com/ubuntu/adsys). This client enables full **Group Policy support**, privilege escalation and remote script executions.

In Ubuntu 23.04 we’ve added support for **enterprise proxy**, **app confinement** and **network shares** to further expand its functionality before backporting them to Ubuntu 22.04 LTS and Ubuntu 20.04 LTS later this year.

## Ubuntu Server

### Apache2
  - mod_http2 has a partial rewrite of how connections and streams are handled in 2.4.55.  APR pollset and pipes do the monitoring instead of stuttered timed waits.  Resource handling for misbehaving clients is improved.
  - mod_proxy_hcheck detects AJP/CPING support correctly now.

### AppArmor updates
Two more packages now have AppArmor profiles defaulting to enforce mode: [`rsyslog`](https://launchpad.net/ubuntu/+source/rsyslog/8.2210.0-3ubuntu2) and [`isc-kea`](https://launchpad.net/ubuntu/+source/isc-kea/2.2.0-3).

Previously, `rsyslog` did have an apparmor profile, but it was disabled by default. This profile was examined and changed, and is a bit more dynamic now, adjusting itself to the `rsyslog` configuration. For example, if the MySQL rsyslog module is installed, then the profile adapts to allow a connection to a local MySQL server.

`isc-kea` was lacking an AppArmor profile, and we added one now that also defaults to enforce mode.

### Cloud images

* Cloud Images updated default fstab entry for ext4 root filesystem to use `commit=30 seconds` option, previously 30 seconds was implicit default on amd64 images with `linux-kvm` kernel flavour, and 5 seconds on all other cases. This improves performance and power efficiency at the expense of data-safety. See [bug](https://bugs.launchpad.net/bugs/2006511) and [merge proposal](https://code.launchpad.net/~ubuntu-core-dev/livecd-rootfs/+git/livecd-rootfs/+merge/436977) for further details.
* AWS amd64 images use now the new `uefi-preferred` boot mode. See [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html) for details.

### Cloud-init
cloud-init was updated from 22.4 to the 23.1 release. The new release includes the following highlights:
 * new datasource support: NWCS
 * Azure: fix device driver matching for NICs to match `hv_netvsc`
 * AliYun: support security token-based IMDS interaction
 * LXD:
   - support LXD  preseed in `#cloud-config`
   - opt-in network hotplug for LXD datasource
 * NoCloud: live installer support DMI variable expansion for kernel cmdline params
 * OpenStack: IPv6 detection of IMDS                                            
 * Netplan:
   - Direct pass-though of v2 network config in netplan systems
   - Render network config root-readonly to allow for security sensitive config 
   - add gateway on-link support
 * Ansible: Ansible galaxy install, control module and pip bootstrap
 * ssh: support config for multiple host certs
 * cloud-config schema
   - Allow jinja template and variable expansion of instance-data.json values in /etc/cloud
   - `cloud-init schema --system` validates user-data and vendor-data
 * machine-readable output --format yaml/json in `cloud-init status`
 * `cloud-init clean --machine-id` better support for installed image clone
 * docs: documentation overhaul, new howtos, restructure to diataxis framework

### Container runtimes

#### Docker

It was updated to version 20.10.21. This new version comes with many security and bug fixes, also library updates. For a more complete description of the changes refer to the [upstream release notes](https://docs.docker.com/engine/release-notes/20.10/#201021).

#### Containerd

It was updated to version 1.6.12. Some interesting changes are:

* Migrate from k8s.gcr.io to registry.k8s.io
* Add support for CAP_BPF and CAP_PERFMON
* Seccomp: Allow clock_settime64 with CAP_SYS_TIME
* Allow ptrace(2) by default for kernels >= 4.8

Plus some security fixes. For the complete list of changes please refer to the [upstream release page](https://github.com/containerd/containerd/releases).

#### Runc

It was updated to version 1.1.4. Some interesting changes are:

* Our seccomp -ENOSYS stub now correctly handles multiplexed syscalls on s390 and s390x. This solves the issue where syscalls the host kernel did not support would return -EPERM despite the existence of the -ENOSYS stub code (this was due to how s390x does syscall multiplexing).
* Retry on dbus disconnect logic in libcontainer/cgroups/systemd now works as intended; this fix does not affect runc binary itself but is important for libcontainer users such as Kubernetes.

All the improvements and bug fixes can be found in the [upstream release page](https://github.com/opencontainers/runc/releases).

### Dnsmasq

Several new options are included with the upgrade from 2.86 to 2.89, including --fast-dns-retry, --use-stale-cache, --conf-script, and --port-limit.  --nftset is like -ipset but for the newer nftables.

### Dpdk

Following the yearly flow of upstream DPDK LTS releases Ubuntu 23.04 contains the most recent DPDK LTS including a follow up stable release on this LTS stream now being at 22.11.1 in lunar.

That contains various new device drivers, fixes and optimizations. Even the rather huge [release notes](http://doc.dpdk.org/guides/rel_notes/release_22_11.html) is just about 22.11 itself. The Upstream changed from a four to a three release per year cadence, therefore compared to the former DPDK LTS 21.11 that shipped with Ubuntu 20.04, 21.04 and 21.10 you'd also want to read the DPDK release notes of [22.03](http://doc.dpdk.org/guides/rel_notes/release_22_03.html), [22.07](http://doc.dpdk.org/guides/rel_notes/release_22_07.html).

This new version of DPDK is now also built and available for riscv64.

### Frr
[frr](https://frrouting.org/) was updated to version 8.4.2, after having stayed at 8.1 for two full Ubuntu releases (since Jammy). There have been many bug fixes and improvements between these versions, please see the upstream release notes collection at https://github.com/FRRouting/frr/releases for details.

### HA/Clustering

#### Corosync

It was updated to version 3.1.7. This release contains important bugfixes and the knet_mtu (for more information please see corosync.conf(5)) feature. For more details, please, check out the [upstream release notes](https://github.com/corosync/corosync/releases).

#### Fence Agents

It was updated to version 4.12.1. It contains some fixes and improvements in various agents. For more details check the [upstream repository](https://github.com/ClusterLabs/fence-agents).

#### haproxy

haproxy was updated to the new upstream LTS series: 2.6. Many new features and performance improvements are present in this release, please see the announcement at https://www.mail-archive.com/haproxy@formilux.org/msg42371.html and the corresponding blog post at https://www.haproxy.com/blog/announcing-haproxy-2-6/ for details.

### Heimdal

Release 7.8 improves the Heimdal database (HDB) propagation feature to include progressive diff sending, partial writes, async I/O, and other associated refinements.

### ISC Kea (DHCP server)
Up until now, the Kea Control Agent service (`kea-ctrl-agent.service`) could be accessed on localhost (127.0.0.1:8000) without a password ([LP: #2007312](https://bugs.launchpad.net/ubuntu/+source/isc-kea/+bug/2007312)). Actions such as shutting down any of the Kea services, managing DHCP leases, or grabbing a copy of the current configuration, could be taken by any local user on the system.

Starting with version 2.2.0-5ubuntu2 of the package, a fresh install, or an upgrade from a previous version, will prompt the user to create a password for the `kea-api` user, or have the system generate a random one. The default action, which is taken for unattended installs, is to do nothing.

**If a password is not set, the Kea Control Agent will not start**. This situation can be detected in the status of the service:

    $ systemctl status kea-ctrl-agent.service
    ○ kea-ctrl-agent.service - Kea Control Agent
     Loaded: loaded (/lib/systemd/system/kea-ctrl-agent.service; enabled; preset: enabled)
     Active: inactive (dead)
    (...)
    2023-03-31T17:51:01.638484+00:00 l-kea-debconf systemd[1]: kea-ctrl-agent.service - Kea Control Agent was skipped because of an unmet condition check (ConditionFileNotEmpty=/etc/kea/kea-api-password).

In this case, you can use `dpkg-reconfigure kea-ctrl-agent` to revisit the choices given when the package was first installed and choose a password.
### Libvirt

Tracking the releases of libvirt continuously version v9.0.0 is now provided in Ubuntu 23.04 which - among many other fixes, improvements and features - includes:

 *  For example there have been many new features for qemu:
   * external snapshot deletion
   * external backend for swtpm
   * passing FDs instead of opening files for <disk>
   * Allow multiple nodes for preferred policy
   * Report Hyper-V Enlightenments in domcapabilities
   * Support for SGX EPC (enclave page cache)
   * Support migration of vTPM state of QEMU vms on shared storage
   * qemu: Core Scheduling support (not enabled by default)
   * qemu: Add support for specifying vCPU physical address size in bits
 * See the [upstream changelog](https://libvirt.org/news.html) for the many further improvements and fixes since version 8.6.0 that was in Ubuntu 22.10

### Net SNMP

In addition to a few security and stability fixes, support is now included for recognizing Docker's overlay filesystem (LP: #2007856), such as when running snmpwalk against a Docker container.

### Open vSwitch

The new version 3.1.0 of openvswitch is in Ubuntu 23.04 and provides a general update including the following changes:

   * Now also built and available for riscv64
   * ovs-vswitchd now detects changes in CPU affinity and adjusts the number of handler and revalidator threads if necessary.
   * Add support for DPDK 22.11.1.
   * For the QoS max-rate and STP/RSTP path-cost configuration OVS now assumes 10 Gbps link speed by default in case the actual link speed cannot be determined.
   * ovs-ctl: New option '--dump-hugepages' to include hugepages in core dumps. This can assist with postmortem analysis involving DPDK, but may also produce significantly larger core dump files.
   * Support for AF_XDP is now built by default.
   * [The OVS News](https://www.openvswitch.org/releases/NEWS-3.1.0.txt) page holds more details about the new version.

### OpenStack

Ubuntu 23.04 includes the latest OpenStack release, Antelope, including the following components:

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
* OpenStack Container Orchestration - Magnum

Please refer to the [OpenStack Antelope release notes](https://releases.openstack.org/antelope/) for full details of this release of OpenStack.

OpenStack Antelope is also provided via the Ubuntu Cloud Archive for OpenStack Antelope for Ubuntu 22.04 LTS users. The Ubuntu Cloud Archive for OpenStack Antelope can be enabled on Ubuntu 22.04 by running the following command:

> sudo add-apt-repository cloud-archive:antelope

WARNING: Upgrading an OpenStack deployment is a non-trivial process and care should be taken to plan and test upgrade procedures which will be specific to each OpenStack deployment.

Make sure you read the [OpenStack Charm Release Notes](https://docs.openstack.org/charm-guide/latest) for more information about how to deploy and operate Ubuntu OpenStack using Juju.

### PostgreSQL 15

PostgreSQL was updated to the new PostgreSQL 15 release. This new major release includes sort performance and compression improvements, support for the SQL MERGE command, and a new JSON logging format, which allows logs to be processed in structured logging systems.

### Qemu

Qemu was updated to version v7.2.0 which brings many major and minor improvements. Among others this version includes:

 * Arm
   * Emulation of arm Cortex-A76, Cortex-A35 and Neoverse-N1 CPUs
   * The virt board now supports emulation of the GICv4.0
   * Several new PCPU architecture features are now emulated as well
 * Risc-V
   * Add support for privileged spec version 1.12.0
   * Add support for the Zbkb, Zbkc, Zbkx, Zknd/Zkne, Zknh, Zksed/Zksh and Zkr extensions
   * Add support for Zmmul extension
   * Add TPM support to the virt board
   * virt machine device tree improvements
 * s390x
   * Emulate the s390x Vector-Enhancements Facility 2 with TCG
   * The s390-ccw bios has been fixed to also boot from drives with non-512 sector sizes that have a different geometry than the typical DASD drives
   * Fix emulation of LZRF, VISTR, SACF instructions
   * Enhanced zPCI interpretation support for KVM guests
   * Implement Message-Security-Assist Extension 5 (random number generation via PRNO instruction)
 * More
   * Support for zero-copy-send on Linux, which reduces CPU usage on the source host. Note that locked memory is needed to support this.
   * TCG performance improvements in full-system emulation
   * TCG support for AVX, AVX2, F16C, FMA3 and VAES instructions
 * There are many more changes, see the upstream [changelog for version 7.1](https://wiki.qemu.org/ChangeLog/7.1) and [version 7.2](https://wiki.qemu.org/ChangeLog/7.2) for an overview of those. These also contain a list of suggested alternatives for removed, deprecated and incompatible features.

### Rclone
The very feature rich and versatile [rclone](https://rclone.org/) package received an update after having stayed at version 1.53 for the last two Ubuntu releases. The new version 1.60.1 has many new features, backends, and bugfixes. Please see the upstream release notes collection at https://rclone.org/changelog/#v1-60-1-2022-11-17 for details on the changes in 1.60.1 and earlier.

### Ruby 3.1

The default Ruby interpreter was updated to version 3.1, it keeps compatibility with Ruby 3.0 and adds many features. In order to get an overview of what changed please check out the [Ruby 3.1 Release Announcement](https://www.ruby-lang.org/en/news/2021/12/25/ruby-3-1-0-released/).

An important thing to keep in mind is that the following gems are not bundled in the standard library:

* net-ftp
* net-imap
* net-pop
* net-smtp
* matric
* prime
* debug

One change that has impacted multiple projects is the Psych 4.0 change from `Psych.load` to `safe_load` by default, check it out when migrating to Ruby 3.1.

### Samba
The [samba](https://www.samba.org) package was updated to the 4.17.x series. Here are the upstream release notes: https://www.samba.org/samba/history/samba-4.17.0.html

Specially when compared with earlier releases, this series brings performance improvements in file operations which were previously impacted by security fixes for symlink attacks. Samba now uses less system calls when validating directory names, and has less wakeup events which previously led to massive latencies for some clients. See the release notes linked above for details.

### SSSD

Many new configuration options have been introduced in version 2.8.0.  You can see a list of them by looking at [upstream's release notes](https://sssd.io/release-notes/sssd-2.8.0.html#configuration-changes).

### Subiquity

Subiquity 23.04.2 has been released.  For full change details, please see the [Subiquity 23.04.2](https://github.com/canonical/subiquity/releases/tag/23.04.2) release post on Github.

### virglrenderer

In the upgrade from 0.9.1 to 0.10.4, Vulkan support has been implemented, which promises more efficient 3D performance on certain hardware.

## Platforms

### Raspberry Pi 🍓

* Ubuntu 23.04 updates the [libcamera](https://launchpad.net/ubuntu/+source/libcamera) package to 0.0.4 and includes support for all official Raspberry Pi camera modules *except* the v3 camera module. Specifically, the OV5647 based v1 (now out of production), the [IMX219 based v2](https://www.raspberrypi.com/products/camera-module-v2/), the [IMX477 based HQ camera](https://www.raspberrypi.com/products/raspberry-pi-high-quality-camera/), and the [IMX296 based global shutter camera](https://www.raspberrypi.com/products/raspberry-pi-global-shutter-camera/) all operate, but work on the [IMX708 based v3 module](https://www.raspberrypi.com/products/camera-module-3/) is still ongoing. [(bug 2009824)](https://bugs.launchpad.net/ubuntu/+source/libcamera/+bug/2009824)

* Ubuntu 23.04 updates the Firefox snap to a base of Core 22. This fixes various graphical hardware acceleration issues, including hardware compositing (see [this blog post](https://ubuntu.com/blog/firefox-snap-updates-and-upgrades) for more details).

* Ubuntu 23.04 Desktop for Raspberry Pi now leaves 16MB of slack space at the end when resizing the root file-system on first boot. This change enables much easier encryption of the root file-system if desired (see [this blog post](https://waldorf.waveform.org.uk/2023/playing-with-blocks-reluks.html) for instructions).

### IBM Z and LinuxONE

Starting with Ubuntu Server 20.04 LTS, the minimal architectural level set was raised to z13 (and LinuxONE Rockhopper / Emperor) - this still applies to Ubuntu Server 23.04 and support also includes all newer hardware that is in service as of today (23.04 release date) until announced otherwise. Support for additional future hardware might be added later.
Ubuntu Server 23.04 can be installed in an LPAR (classic or DPM systems), as IBM z/VM guest, as KVM virtual machine and in different container environments, such as LXD, docker or kubernetes.

* The key package for IBM Z and LinuxONE, the s390-tools package, got updated to 2.26.0 [(bug 2003284)](https://bugs.launchpad.net/bugs/2003284) and with that site-aware device configuration introduced [(bug 1982339)](https://bugs.launchpad.net/bugs/1982339) as well as vmconvert and zgetdump consolidated [(bug 2008785)](https://bugs.launchpad.net/bugs/2008785).

* Two larger and cross component features related to DASD disks that were added are:
  * support for transparent DASD PPRC (Peer-to-Peer Remote Copy) handling [(bug 1982341)](https://bugs.launchpad.net/bugs/1982341) & [(bug 2003281)](https://bugs.launchpad.net/bugs/2003281)
  * support for List-Directed IPL and re-IPL from ECKD DASD [(bug 2003393)](https://bugs.launchpad.net/bugs/2003393), [(bug 2003394)](https://bugs.launchpad.net/bugs/2003394) and [(bug 2003286)](https://bugs.launchpad.net/bugs/2003286)

* Virtualization is another area of constant improvement, and with this release 
  * storage key removal was implemented [(bug 1835549)](https://bugs.launchpad.net/bugs/1234567) and storage key handling for external processes enabled [(bug 1933177)](https://bugs.launchpad.net/bugs/1234567)
  * Secure Execution guest dump support added [(bug 2003680)](https://bugs.launchpad.net/bugs/1234567), incl. encryption with customer keys [(bug 1959966)](https://bugs.launchpad.net/bugs/1234567)
  * memory reclaiming for Secure Execution guests on z16 improved [(bug 2006604)](https://bugs.launchpad.net/bugs/1234567)
  * device busid for subchannels enabled in KVM [(bug 2004491)](https://bugs.launchpad.net/bugs/1234567) and
  * virtual CPU topology provided to KVM guests via libvirt [(bug 1983222)](https://bugs.launchpad.net/bugs/1234567)

* Cryptography is the next big area of improvement - with the upgrade to openCryptoki v3.20.0:
  * master key consistency for ep11 tokens was established [(bug 2003629)](https://bugs.launchpad.net/bugs/1234567)
  * ica and soft tokens in PKCS #11 3.0 now support AES_XTS [(bug 2003630)](https://bugs.launchpad.net/bugs/1234567) as well as ep11 tokens [(bug 2003632)](https://bugs.launchpad.net/bugs/1234567)
  * support for ep11 tokens on z16 was added [(bug 2003635)](https://bugs.launchpad.net/bugs/1234567)
  * support of new vendor specific key derivation function with ep11 7.2 tokens [(bug 2003638)](https://bugs.launchpad.net/bugs/1234567)
  * key generation with expected MKVP only on CCA and EP11 tokens [(bug 2003639)](https://bugs.launchpad.net/bugs/1234567) and
  * p11sak supports now Dilithium and Kyber keys [(bug 2003669)](https://bugs.launchpad.net/bugs/1234567)
  * openssl-ibmca was not only upgraded to 2.3.1 [(bug 2004529)](https://bugs.launchpad.net/bugs/1234567), but also to 2.4.0
  * the new libica 4.2.1 [(bug 2003849)](https://bugs.launchpad.net/bugs/1234567) is now FIPS 140-3 compliant [(bug 2003670)](https://bugs.launchpad.net/bugs/1234567)
  * and the zcrypt kernel device driver supports now AP command filtering [(bug 2003637)](https://bugs.launchpad.net/bugs/2003637) and [(bug 2007797)](https://bugs.launchpad.net/bugs/2007797)

* Further miscellaneous s390x specific updates and improvements are:
  * the added ECC support in libzpc [(bug 2003636)](https://bugs.launchpad.net/bugs/1234567)
  * driverctl now allows to list persisted definitions [(bug 2003678)](https://bugs.launchpad.net/bugs/1234567)
  * qclib was upgraded to latest v2.3.2 [(bug 2004526)](https://bugs.launchpad.net/bugs/1234567)
  * smc-tools upgraded to latest v1.8.2 [(bug 2004528)](https://bugs.launchpad.net/bugs/1234567)
  * PCI logging improved [(bug 2003390)](https://bugs.launchpad.net/bugs/1234567)
  * Reset DAT-Protection facility support for z16 added [(bug 1982378)](https://bugs.launchpad.net/bugs/1234567)
  * and finally glibc patched to allow influencing hwcaps/stfle via GLIBC_TUNABLES glibc.cpu.hwcaps [(bug 2007599)](https://bugs.launchpad.net/bugs/1234567)

## Known Issues

As is to be expected, with any release, there are some significant known bugs that users may run into with this release of Ubuntu. The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:

### General

* The option to install using zfs as a file system and encryption has been disabled due to a bug ([LP: #1993318](https://bugs.launchpad.net/ubuntu-manual-tests/+bug/1993318)) with all of the file system not being mounted on first boot. If you’d like to have a system using zfs and encryption please install using Ubuntu 22.04.1 and then upgrade to Ubuntu 23.04.

* The Live Session of the new Ubuntu Desktop installer is not localized. It is still possible to perform a non-English installation using the new installer, but Internet access at install time is required to download the language packs. Should this be an issue use the legagy installer images. ([LP: #2013329](https://bugs.launchpad.net/ubuntu-release-notes/+bug/2013329))

### Linux kernel

* There is a regression in support for SRIOV NVIDIA vGPU drivers compared to v5.15/v5.19 kernels. Canonical is working with NVIDIA to resolve this release regression in a future kernel SRU in Lunar. ([LP: #1988806](https://bugs.launchpad.net/bugs/1988806))
* For some Broadcom devices the b43 kernel module will be loaded but unusable due to the PHY being unsupported. Steps for disabling the b43 module and using bcmwl are documented in the relevant bug report. ([LP: 2013236](https://bugs.launchpad.net/ubuntu/+source/ubuntu-drivers-common/+bug/2013236))
* Network deployment is failing whilst exhibiting issues with udev & kernel unable to enumerate and load drivers in the initrd. This is being investigated in ([LP: #2016908](https://bugs.launchpad.net/maas-images/+bug/2016908))

### Ubuntu Desktop

- The Screen Reader is unable to read many parts of GTK4 apps ([LP: #2015760](https://launchpad.net/bugs/2015760)). Please use Ubuntu 22.04 LTS if you depend on screen reader support.
- The _Try Ubuntu_ environment is not translated with the new Desktop Installer ([LP: #2013329](https://launchpad.net/bugs/2013329))
- The broadcom-sta wireless driver, necessary for some Broadcom wireless devices, may not automatically be installed, however it is still installable via software-properties. ([LP: #2013236](https://bugs.launchpad.net/ubuntu/+source/ubuntu-drivers-common/+bug/2013236))
- If xdg-desktop-portal-gnome is installed on a non-GNOME system, the file chooser in confined apps like the Firefox snap takes a long time to open the first time ([LP: #2013116](https://launchpad.net/bugs/2013116))
- App icons aren't using the correct High Contrast theme when High Contrast is enabled [(LP: #2013107](https://launchpad.net/bugs/2013107))
- When opening Firefox the first time after login to a Wayland session, you may be met by a black window. If so, just close Firefox and try again. This issue will be fixed as a stable release update soon after the 23.04 release.


### Ubuntu Server

- In some situations, it is acceptable to proceed with an offline install when the mirror is inaccessible. In this scenario, it is advised to use:
```
apt:
  fallback: offline-install
```

## Platforms

### Cloud Images

None
 
### Raspberry Pi

* With some monitors connected to a Raspberry Pi it is possible that a monitor will power off after a period of inactivity but then power back on and show a black screen. Investigation into the types of monitors affected is ongoing in ([LP: #198716](https://bugs.launchpad.net/ubuntu/+source/mutter/+bug/1998716)).

* The [GPIO sysfs interface](https://docs.kernel.org/admin-guide/gpio/sysfs.html) is still disabled ([LP: #1918583](https://bugs.launchpad.net/bugs/1918583), [LP: #2004108](https://bugs.launchpad.net/ubuntu/+source/linux-raspi/+bug/2004108)). This means that several common GPIO libraries (including [RPi.GPIO](https://pypi.org/project/RPi.GPIO/)) cannot operate. A shim providing [compatibility with RPi.GPIO](https://rpi-lgpio.readthedocs.io/en/latest/) has been created and is available in Lunar in the `python3-rpi-lgpio` package. See [this post](https://waldorf.waveform.org.uk/2022/the-one-where-dave-breaks-stuff.html) for full details.

* The official DSI display requires `linux-modules-extra-raspi` to be installed to operate correctly, including rotation and touchscreen operation. To rotate the framebuffer console (e.g. for the server release), append `fbcon=rotate:2` to the kernel command line in `cmdline.txt` on the boot partition ([LP: #1970603](https://launchpad.net/bugs/1970603)).

* Various kernel modules have been moved from the `linux-modules-raspi` package in order to reduce the initramfs size. If you find an application failing due to missing kernel modules, please try `sudo apt install linux-modules-extra-raspi`.

* The legacy camera stack (MMAL based) is not supported on arm64; [libcamera](https://www.raspberrypi.com/documentation/accessories/camera.html#libcamera-and-libcamera-apps) is the supported method of using the Pi Camera Modules on the arm64 architecture (the boot-time configuration will automatically load overlays for official modules; unofficial camera modules need the relevant overlay added to `config.txt` on the boot partition).

* After initial user setup on the desktop image, several packages can still be autoremoved [LP: #1925265](https://launchpad.net/bugs/1925265)); run `sudo apt autoremove --purge` to work around this.

* Under the desktop image, while the pipewire stack maintains the correct audio device across reboots on the Raspberry Pi ([LP: #1877194](https://launchpad.net/bugs/1877194)), an invalid audio device is now selected by default on the Raspberry Pi 400 ([LP: #1993316](https://launchpad.net/bugs/1993316)), and an inconvenient default is selected on the Raspberry Pi 4 ([LP: #1993347](https://launchpad.net/bugs/1993347)).

* With the removal of the `crda` package in 22.04, the method of setting the wifi regulatory domain (editing `/etc/default/crda`) no longer operates. On server images, use the `regulatory-domain` option in the netplan configuration. On desktop images, append `cfg80211.ieee80211_regdom=GB` (substituting "GB" for the relevant country code) to the kernel command line in `cmdline.txt` on the boot partition  ([LP: #1951586](https://launchpad.net/bugs/1951586)).

* Under the desktop image, the default totem video player will not open videos by default ([LP: #1998782](https://launchpad.net/bugs/1998782)); `sudo apt install vlc` to install an alternate video player which operates correctly.


### s390X

Nothing yet.

## Official flavours

The release notes for the official flavours can be found at the following links:

  * [Edubuntu Release Notes](https://discourse.ubuntu.com/t/edubuntu-23-04-released/35281)
  * [Kubuntu Release Notes](https://wiki.ubuntu.com/LunarLobster/ReleaseNotes/Kubuntu)
  * [Lubuntu Release Notes](https://lubuntu.me/lunar-released/)
  * [Ubuntu Budgie Release Notes](https://ubuntubudgie.org/2023/04/ubuntu-budgie-23-04-release-notes/)
  * [Ubuntu MATE Release Notes](https://ubuntu-mate.org/blog/ubuntu-mate-lunar-lobster-release-notes/)
  * [Ubuntu Studio Release Notes](https://ubuntustudio.org/ubuntu-studio-23-04-release-notes/)
  * [Ubuntu Unity Release Notes](https://ubuntuunity.org/blog/ubuntu-unity-23.04/)
  * [Xubuntu Release Notes](https://wiki.xubuntu.org/releases/23.04/release-notes)
  * [Ubuntu Kylin Release Notes](https://www.ubuntukylin.com/news/ubuntukylin2304-en.html)
  * [Ubuntu Cinnamon Release Notes](https://ubuntucinnamon.org/ubuntu-cinnamon-23-04-lunar-lobster-released/)
