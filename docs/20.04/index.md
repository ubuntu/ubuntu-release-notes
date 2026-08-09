---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/FocalFossa/ReleaseNotes -->

(ubuntu-20-04-lts-release-notes)=
# Ubuntu 20.04 LTS release notes

(20-04-lts-introduction)=
## Introduction

These release notes for **Ubuntu 20.04 LTS** (Focal Fossa) provide an overview of the release and document the known issues with Ubuntu 20.04 LTS and its flavors. For details of the changes applied since 20.04, please see the [20.04.6 change summary](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes/ChangeSummary/20.04.6).  The release notes for [20.04](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes/20.04), [20.04.1](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes/ChangeSummary/20.04.1), [20.04.2](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes/ChangeSummary/20.04.2), [20.04.3](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes/ChangeSummary/20.04.3), [20.04.4](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes/ChangeSummary/20.04.4) and [20.04.5 change summary](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes/ChangeSummary/20.04.5) are available as well.


(20-04-lts-support-lifespan)=
### Support lifespan

Maintenance updates will be provided for 5 years until [April 2025](https://wiki.ubuntu.com/Releases) for Ubuntu Desktop, Ubuntu Server, Ubuntu Cloud, and Ubuntu Core. All the remaining flavours will be supported for 3 years. Additional security support is available with ESM (Extended Security Maintenance).


(20-04-lts-official-flavor-release-notes)=
### Official flavor release notes

Find the links to release notes for official flavors [here](https://wiki.ubuntu.com/Official_flavours).


(get-ubuntu-20-04-6-lts)=
## Get Ubuntu 20.04.6 LTS


(download-ubuntu-20-04-6-lts)=
### Download Ubuntu 20.04.6 LTS

Images can be downloaded from a location near you.

You can download ISOs and flashable images from:

[releases.ubuntu.com/20.04/](https://releases.ubuntu.com/20.04/) (Ubuntu Desktop and Server for AMD64)

[cdimage.ubuntu.com/ubuntu/releases/20.04/release/](http://cdimage.ubuntu.com/ubuntu/releases/20.04/release/) (Less Frequently Downloaded Ubuntu Images)

[cloud-images.ubuntu.com/daily/server/focal/current/](http://cloud-images.ubuntu.com/daily/server/focal/current/) (Ubuntu Cloud Images)

[cdimage.ubuntu.com/kubuntu/releases/20.04/release/](http://cdimage.ubuntu.com/kubuntu/releases/20.04/release/) (Kubuntu)

[cdimage.ubuntu.com/lubuntu/releases/20.04/release/](http://cdimage.ubuntu.com/lubuntu/releases/20.04/release/) (Lubuntu)

[cdimage.ubuntu.com/ubuntu-budgie/releases/20.04/release/](http://cdimage.ubuntu.com/ubuntu-budgie/releases/20.04/release/) (Ubuntu Budgie)

[cdimage.ubuntu.com/ubuntukylin/releases/20.04/release/](http://cdimage.ubuntu.com/ubuntukylin/releases/20.04/release/) (Ubuntu Kylin)

[ubuntu-mate.org/download/](https://ubuntu-mate.org/download/) (Ubuntu MATE)

[cdimage.ubuntu.com/ubuntustudio/releases/20.04/release/](http://cdimage.ubuntu.com/ubuntustudio/releases/20.04/release/) (Ubuntu Studio)

[cdimage.ubuntu.com/xubuntu/releases/20.04/release/](http://cdimage.ubuntu.com/xubuntu/releases/20.04/release/) (Xubuntu)


(20-04-lts-upgrading-from-ubuntu-18-04-lts-or-19-10)=
### Upgrading from Ubuntu 18.04 LTS or 19.10

* You can upgrade to Ubuntu 20.04 LTS from either Ubuntu 18.04 LTS or Ubuntu 19.10.

* Ensure that you have all updates installed for your current version of Ubuntu before you upgrade.

* Confirm that you also have a network connectivity to one of the official mirrors or to a locally accessible mirror as there are no offline upgrade options.

To upgrade on a desktop system:

* Open the "Software & Updates" Setting in System Settings.

* Select the 3rd Tab called "Updates".

* Set the "Notify me of a new Ubuntu version" drop down menu to "For any new version" if you are using 19.10; set it to "For long-term support versions" if you are using 18.04 LTS.

* Press Alt+F2 and type `update-manager -c` into the command box if you are using 19.10; type `update-manager -c -d` if you are using 18.04 LTS.

* Update Manager should open up and tell you that Ubuntu 20.04 LTS is now available.

* Click Upgrade and follow the on-screen instructions.

To upgrade on a server system:

* Install  `update-manager-core` if it is not already installed.

* Make sure the `Prompt` line in /etc/update-manager/release-upgrades is set to 'normal' if you are using 19.10, or 'lts' if you are using 18.04 LTS.

* Launch the upgrade tool with the command `sudo do-release-upgrade` on 19.10; use `sudo do-release-upgrade -d` if you are using 18.04 LTS.

* Follow the on-screen instructions.
Note that the server upgrade will use GNU screen and automatically re-attach in case of dropped connection problems.

The `-d` switch is necessary to upgrade from Ubuntu 18.04 LTS as upgrades have not yet been enabled and will only be enabled after the first point release of 20.04 LTS.


(20-04-lts-upgrades-on-i386)=
#### Upgrades on i386

Users of the i386 architecture will not be presented with an upgrade to Ubuntu 20.04 LTS.  Support for i386 as a host architecture was dropped in 19.10.


(new-features-in-20-04-lts)=
## New Features in 20.04 LTS


(20-04-lts-risc-v-image)=
### RISC-V image

RISC-V images for SiFive HiFive Unleashed and Unmatched boards are now available, which can also be used as a VM with QEMU on any Ubuntu 20.04 machine. For more details see [RISC-V](https://help.ubuntu.com/community/RISC-V) page.


(20-04-lts-updated-packages)=
### Updated Packages

As with every Ubuntu release, Ubuntu 20.04 LTS comes with a selection of the latest and greatest software developed by the free software community.


(20-04-lts-linux-kernel)=
#### Linux Kernel

Ubuntu 20.04 LTS is based on the long-term supported Linux release series **5.4**. HWE stack updated to Linux release series **5.8**.

**NOTE:** Users who installed from Ubuntu Desktop media should see the note about desktop tracking the rolling hardware enablement kernel series by default [here](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes#Ubuntu_Desktop).

Notable features and enhancements in 5.4 since 5.3 include:

* Support for new hardware including Intel Comet Lake CPUs and initial Tiger Lake platforms, AMD Navi 12 and 14 GPUs, Arcturus and Renoir APUs along with Navi 12 + Arcturus power features.

* Support has been added for the exFAT filesystem, virtio-fs for sharing filesystems with virtualized guests and fs-verity for detecting file modifications.

* Built in support for the WireGuard VPN.

* Enablement of lockdown in integrity mode.

Other notable kernel updates to **5.4** since version 4.15 released in 18.04 LTS include:

* Support for AMD Rome CPUs, Radeon RX Vega M and Navi GPUs, Intel Cannon Lake platforms.

* Support for raspberry pi (Pi 2B, Pi 3B, Pi 3A+, Pi 3B+, CM3, CM3+, Pi 4B)

* Significant power-saving improvements.

* Numerous USB 3.2 and Type-C improvements.

* A new mount API, the `io_uring` interface, KVM support for AMD Secure Encrypted Virtualization and `pidfd` support.

* Boot speed improvements through changing the default kernel compression algorithm to lz4 (in Ubuntu 19.10) on most architectures, and changing the default initramfs compression algorithm to lz4 on all architectures.


(20-04-lts-toolchain-upgrades)=
#### Toolchain Upgrades 🛠️

Ubuntu 20.04 LTS comes with refreshed state-of-the-art toolchain including new upstream releases of `glibc` 2.31, ☕ OpenJDK 11, `rustc` 1.41, GCC 9.3, 🐍 Python 3.8.2, 💎 ruby 2.7.0, PHP 7.4, 🐪 Perl 5.30, `golang` 1.13.


(20-04-lts-ubuntu-desktop)=
#### Ubuntu Desktop

* Ubuntu Desktop flavour now always tracks HWE (hardware enablement) kernel. It means that from January 2021 the Ubuntu Desktop will gain new major kernel versions every 6 months through to summer of 2022, even if you installed Ubuntu Desktop earlier than this.
  Read more about it on the Ubuntu discourse thread [Improvements for hardware support in Ubuntu Desktop installation media](https://discourse.ubuntu.com/t/improvements-for-hardware-support-in-ubuntu-desktop-installation-media).

* New graphical boot splash (integrates with the system BIOS logo).

* Refreshed [Yaru theme](https://ubuntu.com/blog/new-ubuntu-theme-in-development-for-20-04) 🎨

  * [Light/Dark theme switching](https://twitter.com/m_wimpress/status/1232246572479590401)

* GNOME 3.36

  * New lock screen design.

  * New system menu design.

  * New app folder design.

  * Smoother performance, lower CPU usage for [window and overview animations](https://bugs.launchpad.net/bugs/1725180), [JavaScript execution](https://gitlab.gnome.org/GNOME/gjs/issues/302), [mouse movement](https://bugs.launchpad.net/bugs/1848951) and [window movement (which also has lower latency now)](https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/724).

  * 10-bit [deep colour](https://en.wikipedia.org/wiki/Color_depth#Deep_color_(30/36/48-bit)) support.

  * X11 fractional scaling.

* [Mesa](https://www.mesa3d.org/) 20.0 OpenGL stack

* [BlueZ](http://www.bluez.org/) 5.53

* [PulseAudio](https://www.freedesktop.org/wiki/Software/PulseAudio/) 14.0 (prerelease)

* [Firefox 75.0](https://www.mozilla.org/en-US/firefox/75.0/releasenotes/)

* [Thunderbird 68.7.0](https://www.thunderbird.net/en-US/thunderbird/68.7.0/releasenotes/)

* [LibreOffice 6.4](https://wiki.documentfoundation.org/ReleaseNotes/6.4)



(20-04-lts-network-configuration)=
### Network configuration

With this Ubuntu release, [netplan.io](https://netplan.io/) has grown multiple new features, some of which are:

* Basic support for configuring SR-IOV network devices. Starting with netplan.io 0.99, users can declare Virtual Functions for every SR-IOV Physical Function, configure those as any other networking device and set hardware VLAN VF filtering on them.

* Support for GSM modems via the NetworkManager backend via the `modems` section.

* Adding WiFi flags for `bssid`/`band`/`channel` settings.

* Adding ability to set `ipv6-address-generation` for the NetworkManager backend and `emit-lldp` for networkd.


(20-04-lts-storage-file-systems)=
### Storage/File Systems


(20-04-lts-zfs-0-8-3)=
#### ZFS 0.8.3

Continuing with what started in the Eoan release, Ubuntu Focal ships zfs 0.8.3. Compared to what was available in the previous LTS release, zfs 0.8 brings many new features. Highlights include:

* Native Encryption (with hardware acceleration enabled in Focal)
* Device removal
* Pool TRIM
* Sequential scrub and resolver (performance)

Upstream 0.8.0 release notes: [github.com/openzfs/zfs/releases/tag/zfs-0.8.0](https://github.com/openzfs/zfs/releases/tag/zfs-0.8.0)

Also checkout [0.8.1](https://github.com/openzfs/zfs/releases/tag/zfs-0.8.1), [0.8.2](https://github.com/openzfs/zfs/releases/tag/zfs-0.8.2) and [0.8.3](https://github.com/openzfs/zfs/releases/tag/zfs-0.8.3) for more details.


(20-04-lts-other-base-system-changes-since-18-04-lts)=
### Other base system changes since 18.04 LTS


(20-04-lts-python3-by-default)=
#### Python3 by default

In 20.04 LTS, the python included in the base system is Python 3.8.  Python 2.7 has been moved to universe and is not included by default in any new installs.

Remaining packages in Ubuntu which require Python 2.7 have been updated to use /usr/bin/python2 as their interpreter, and `/usr/bin/python` is not present by default on any new installs.  On systems upgraded from previous releases, `/usr/bin/python` will continue to point to `python2` for compatibility.  Users who require `/usr/bin/python` for compatibility on newly-installed systems are encouraged to install the `python-is-python3` package, for a `/usr/bin/python` pointing to `python3` instead.

Due to this transition the legacy `python` and `python-minimal` packages might be removed during an upgrade, being replaced by the `python2` and `python2-minimal` packages as dependencies of the `python-is-python2` package.


(20-04-lts-snap-store)=
#### Snap Store

The Snap Store (snap-store) replaces ubuntu-software as the default tool for finding and installing packages and snaps.


(20-04-lts-ubuntu-server)=
### Ubuntu Server


(20-04-lts-installer)=
#### Installer

The live server installer is now the preferred media to install Ubuntu
Server on all architectures.

Besides architecture support, the main user visible new features are
[support for automated installs](https://wiki.ubuntu.com/FoundationsTeam/AutomatedServerInstalls) and being able to install the bootloader to
multiple disks (for a more resilient system).

There have been many other fixes under the hood to make using
encryption easier, better support installing to multipath disks, more
reliable installation onto disks that have been used in various ways
and allowing failures to be reported more usefully.

Starting from Ubuntu Server 20.04.2 the ISO images can optionally boot the installer using the HWE kernel. In this case the installed system will automatically make use of the HWE stack.


(20-04-lts-qemu)=
#### QEMU

QEMU was updated to 4.2 release.
There is so much that it is hard to select individual improvements to highlight, here just a few:

* free page hinting through virtio-balloon to avoid migrating unused pages which can speed up migrations

* PPC: NVIDIA V100 GPU/NVLink2 passthrough for `spapr` using VFIO PCI

* Many speed improvements for LUKS backend

* pmem/nvdimm support

* ...

Therefore please see the full change logs [4.2](http://wiki.qemu.org/ChangeLog/4.2) and [4.1](http://wiki.qemu.org/ChangeLog/4.1) for major changes since Ubuntu 19.10.

For Upgraders from Ubuntu 18.04 please also check out [4.0](http://wiki.qemu.org/ChangeLog/4.0), [3.1](http://wiki.qemu.org/ChangeLog/3.1), [3.0](http://wiki.qemu.org/ChangeLog/3.0) and [2.12](http://wiki.qemu.org/ChangeLog/2.12).

When upgrading it is always recommended to [upgrade the machine types](https://wiki.ubuntu.com/QemuKVMMigration#Upgrade_machine_type) allowing guests to fully benefit from all the improvements and fixes of the most recent version.


(20-04-lts-upgrading-from-19-10)=
##### upgrading from 19.10

For trimmed down container like isolation use-cases the new `qemu` has the [microvm](https://github.com/bonzini/qemu/blob/master/docs/microvm.rst) machine type which can be combined with the [`qboot`](https://github.com/bonzini/qboot) ROM (available as `bios-microvm.bin`) to provide a reduced feature set at a much faster startup time. To further emphasize that you can use the package `qemu-system-x86-microvm` which provides an alternative QEMU binary stripped of all features not needed these use cases as suggested by the [`qboot`](https://github.com/bonzini/qboot) ROM.

The VMX related features can now be controlled individually instead of just `vmx` on/off. Due to that the VMX-subfeatures of certain CPU types might have slightly changed (matching those of the selected CPU type now instead of almost randomly depending on the underlying hardware). In general it is - and always was - recommended to use a well defined cpu type when defining a guest, this is also what almost all higher level management tools from `virt-manager` to OpenStack will do. But if you want the most generic and compatible cpu but also enable VMX please use the type `kvm64` instead of `qemu64` now.

People that like to work or experiment with NVDIMMs and persistent memory QEMU now has [pmem](https://docs.pmem.io/persistent-memory/getting-started-guide/creating-development-environments/virtualization/qemu) and [nvdimm](https://github.com/qemu/qemu/blob/master/docs/nvdimm.txt) support enabled in Ubuntu Focal Fossa.


(20-04-lts-upgrading-from-18-04)=
##### upgrading from 18.04

QEMU now has [`virglrenderer`](https://virgil3d.github.io/) enabled which allows to create a virtual 3D GPU inside QEMU virtual machines. That is inferior to GPU passthrough, but can be handy if the platform used lacks the capability for classic [PCI passthrough](https://www.linux-kvm.org/page/How_to_assign_devices_with_VT-d_in_KVM) as well as more modern [mediated devices](https://www.kernel.org/doc/Documentation/vfio-mediated-device.txt).

The graphical QEMU back-end is now based on GTK instead of SDL. That provides much better Desktop integration and is often faster.


(20-04-lts-libvirt)=
#### libvirt

`libvirt` was updated to version 6.0. See the upstream [change log](https://libvirt.org/news.html) for details since version 5.6 that was in Ubuntu 19.04 or further back since `verison` 4.0 that was in Ubuntu 18.04.


(20-04-lts-upgrading-from-19-10-2)=
##### upgrading from 19.10

Among many improvements worth to mention might be the features:

* to access NVMe disks directly now allowing a speed oriented setup that still supports migration.

* Mediated GPU devices are now supported as boot display.

* Support kvm-hint-dedicated performance hint allowing the guest to enable optimizations when running on dedicated vCPUs

* ...see the detailed changelog linked above for much more


(20-04-lts-upgrading-from-18-04-2)=
##### upgrading from 18.04

Worth mentioning is that `libvirt` can now enable QEMU's ability to use [parallel connections for migration](http://manpages.ubuntu.com/manpages/eoan/man1/virsh.1.html) which can help to speed up migrations if one doesn't saturate your network yet.

Administrators might like the ease of a new local include AppArmor to the `libvirt-qemu` profile that allows local overrides for special devices or paths matching your setup without conffile delta that has to be managed on later upgrades.

Added the ability to have GL enabled graphics as well as mediated devices to be configured while still being guarded by custom apparmor profiles generated per guest. This is required for the use of gpu based mediated devices as well as VirGL mentioned above in the qemu section.


(20-04-lts-transition-libvirt-bin-libvirt-clients-libvirt-daemon-libvirt-daemon-system)=
##### Transition libvirt-bin ->  libvirt-clients / libvirt-daemon / libvirt-daemon-system

Already in Ubuntu 18.04 the package was split from an almost single monolithic package _libvirt-bin_ into three main components:

* **libvirt-daemon-system** - system integration of the daemon with config and systemd service files (this is the most similar single package to the old libvirt-bin)

_ **libvirt-clients** - cli tools to interact with libvirt like _virsh*

* **libvirt-daemon** - just the libvirt daemon, without services/configuration

In a similar fashion rarely used and less supported sub-features like `virtualbox` and `xen` control, as well as uncommon storage options are broken out into various `libvirt-daemon-driver-*` packages. That allows to reduce the install footprint and active code in the majority of installations.

Packages and project had plenty of time to transition, so now the empty compatibility package `libvirt-bin` that was pulling in `libvirt-daemon-system` + `libvirt-clients` was finally dropped. If you happen to have scripts or third party components referring to the old name use the list above to select which new package makes most sense to you.


(20-04-lts-dpdk)=
#### dpdk

Ubuntu 20.04 LTS includes the latest stable release 19.11.1 of the latest LTS series 19.11.x.
The very latest (non-stable) version being 20.02 was not chosen for downstream projects of DPDK (like Open vSwitch) not being compatible yet.

See the [19.11](https://doc.dpdk.org/guides-19.11/rel_notes/release_19_11.html) and [19.11.1](https://doc.dpdk.org/guides-19.11/rel_notes/release_19_11.html#release-notes) release notes for details.


(20-04-lts-upgrading-from-18-04-3)=
##### upgrading from 18.04

DPDK dependencies were reorganized into more or less common/tested components. Due to that most DPDK installations will now have a smaller installation footprint and less potentially active code to care about.


(20-04-lts-open-vswitch)=
#### Open vSwitch

Open vSwitch has been updated to 2.13.

Please read the [2.13 release notes](https://www.openvswitch.org/releases/NEWS-2.13.0.txt) for more detail.

Upgraders from 18.04 might also want to take a look at release notes of:

* [2.12 release notes](https://www.openvswitch.org/releases/NEWS-2.12.0.txt)
* [2.11 release notes](https://www.openvswitch.org/releases/NEWS-2.11.0.txt)
* [2.10 release notes](https://www.openvswitch.org/releases/NEWS-2.10.0.txt)


(20-04-lts-chrony)=
#### Chrony

Chrony been updated to [version 3.5](https://chrony.tuxfamily.org/news.html) which provides plenty of improvements in accuracy and controls. Furthermore it also adds additional isolation for non-x86 by enabling syscall filters on those architectures as well.

To further allow feeding [Hardware time into Chrony](https://gpsd.gitlab.io/gpsd/gpsd-time-service-howto.html) the package [GPSD](https://gpsd.gitlab.io/gpsd/index.html) is now also fully supported.

But still for simple time-sync needs the base system already comes with systemd-timesyncd. Chrony is only needed to act as a time server or if you want the advertised more accurate and efficient syncing.


(20-04-lts-cloud-init)=
#### cloud-init

Cloud-init was updated to version 20.1-10. Notable features include:


(20-04-lts-cloud-platform-features)=
##### Cloud platform features

* New datasource detection/support: e24cloud, Exoscale, Zstack

* Azure dhcp6 support, fix runtime error on cc_disk_setup, add support for byte-swapped instance-id

* EC2: render IPv4 and IPv6 network on all NICs, IMDSv2 session-based API tokens and add secondary IPs as static

* Scaleway: Fix DatasourceScaleway network rendering when unset

* LRU cache frequently used utils for improved performance
* Drop python2 support


(20-04-lts-networking-features)=
##### Networking features

* Prioritize netplan rendering above /etc/network/interfaces even when both
   are present

* Read network config from initramfs
* net: support network-config:disabled on the kernel command line
* Add physical network type: cascading to openstack helpers
* net/cmdline: correctly handle static ip= config


(20-04-lts-config-module-features)=
##### Config module features

* distros: drop leading/trailing hyphens from mirror URL labels
* cc_disk_setup: add swap filesystem force flag
* cloud-init query surfaces merged_cfg and system_info dictionaries for use in
   Jinja-templated cloud-config when opinionated based on series, platform

* use SystemRandom when generating random password.


(20-04-lts-php-7-4)=
#### PHP 7.4

PHP 7.4 is a new feature update, bringing typed properties, arrow functions, weak references, and unpacking inside arrays among other things. For more information on the new features and improvements, see the [PHP 7.4 Release Announcement](https://www.php.net/releases/7_4_0.php).

For more details about deprecated functionality, and suggested replacements, see the [PHP 7.4 Deprecated Features](https://www.php.net/manual/en/migration74.deprecated.php) page.  [Migration guides to 7.4 from 7.3](https://www.php.net/manual/en/migration74.php) or earlier versions of PHP are also available in the PHP Manual.  Users coming from Ubuntu 18.04 will be moving from 7.2 to 7.4, so should also refer to the [Migration guides to 7.3 from 7.2](https://www.php.net/manual/en/migration73.php).


(20-04-lts-ruby-2-7)=
#### Ruby 2.7

The default Ruby interpreter was updated to version 2.7. It comes with some nice features and improvements like: Pattern Matching, REPL improvement, Compaction GC, Separation of positional and keyword arguments and much more. To have a broad overview about the cool features and improvements check the [Ruby 2.7 Release Announcement](https://www.ruby-lang.org/en/news/2019/12/25/ruby-2-7-0-released/).

Users coming from previous Ubuntu releases (from 18.04 on) will be moving from Ruby 2.5 to 2.7, in this case the [Ruby 2.6 Release Announcement](https://www.ruby-lang.org/en/news/2018/12/25/ruby-2-6-0-released/) might be useful as well. An important thing to keep in mind is that some libraries are not bundled anymore in Ruby. If you need them please install them separately:

* `CMath`
* `Scanf`
* `Shell`
* `Synchronizer` (`ruby-sync`)
* `ThreadsWait` (`ruby-thwait`)
* `E2MM` (`ruby-e2mmap`)

For more information check out this [blog post](https://discourse.ubuntu.com/t/ruby-2-7-in-focal/15020).


(20-04-lts-ruby-on-rails-5-2-3)=
#### Ruby on Rails 5.2.3

Ruby on Rails was updated to version 5.2.3. From users coming from Ubuntu 18.04 is a major change, moving from version 4.2.10 to 5.2.3. Some highlights are: addition of Action Cable framework, option to create slimmed down API-only applications, Active Record attributes API and so on. Check the Ruby on Rails [5](https://guides.rubyonrails.org/5_0_release_notes.html) and [5.2](https://guides.rubyonrails.org/5_2_release_notes.html) Release Notes for an overview.

If you need to upgrade your Ruby on Rails application please take a look at the
[upstream upgrading guide](https://guides.rubyonrails.org/upgrading_ruby_on_rails.html).


(20-04-lts-ubuntu-ha-clustering)=
#### Ubuntu HA/Clustering


(20-04-lts-kronosnet)=
##### Kronosnet

kronosnet (or `knet` for short) is the new underlying network protocol for Linux
HA components (`corosync`), that features the ability to use multiple links
between nodes, active/active and active/passive link failover policies,
automatic link recovery, FIPS compliant encryption (NSS and/or OpenSSL),
automatic PMTUD and in general better performance compared to the old network
protocol.

Main NEW features:

* Up to 8 links dynamically reconfigured without restart of `corosync`
* MTU auto-configuration
* Support for NSS or OpenSSL encryption of packets
* Compression
* Higher throughput and lower latency
* Support for RDMA and Upstart is gone


(20-04-lts-corosync)=
##### Corosync

From Corosync 3 release notes:

Corosync 3.0 contains many interesting features mostly related to usage of
Kronosnet (https://kronosnet.org/) as a default (and preferred) network
transport.


(20-04-lts-pacemaker)=
##### Pacemaker

From Pacemaker 2.0 release notes:

The main goal of the 2.0 release was to remove support for deprecated syntax,
along with some small changes in default configuration behavior and tool
behavior. Highlights: Only Corosync version 2 and greater is now supported as
the underlying cluster layer. Support for Heartbeat and Corosync 1 (including
CMAN) is removed.

Rolling upgrades from Pacemaker versions earlier than 1.1.11 are not possible,
even if the underlying cluster stack is corosync 2 or greater. Other rolling
upgrades, from newer versions on top of corosync 2 or greater, should be
possible with little to no change.

* [wiki.clusterlabs.org/wiki/Pacemaker_2.0_Configuration_Changes](https://wiki.clusterlabs.org/wiki/Pacemaker_2.0_Configuration_Changes)

* [wiki.clusterlabs.org/wiki/Pacemaker_2.0_Daemon_Changes](https://wiki.clusterlabs.org/wiki/Pacemaker_2.0_Daemon_Changes)

* [wiki.clusterlabs.org/wiki/Pacemaker_2.0_Tool_Changes](https://wiki.clusterlabs.org/wiki/Pacemaker_2.0_Tool_Changes)

* [wiki.clusterlabs.org/wiki/Pacemaker_2.0_API_Changes](https://wiki.clusterlabs.org/wiki/Pacemaker_2.0_API_Changes)


(20-04-lts-resource-agents)=
##### Resource Agents

Cluster Resource Agents (RAs), compliant with the Open Cluster Framework (OCF)
specification, used to interface with various services in a High Availability
environment managed by the Pacemaker resource manager.

Complete Changelog:

* [github.com/ClusterLabs/resource-agents/blob/master/ChangeLog](https://github.com/ClusterLabs/resource-agents/blob/master/ChangeLog)


(20-04-lts-fence-agents)=
##### Fence Agents

Fence Agents is a collection of scripts to handle remote power management for
several devices. They allow failed or unreachable nodes to be forcibly restarted
and removed from the cluster.


(20-04-lts-keepalived)=
##### keepalived

Failover and monitoring daemon for LVS clusters, used for monitoring real
servers within a Linux Virtual Server (LVS) cluster. It can be configured to
remove real servers from the cluster pool if they stop responding, as well as
send a notification email to make the admin aware of the service failure.


(20-04-lts-isc-kea-1-6-stable-track)=
#### isc-kea 1.6 stable track

Even though it's a Universe package, isc-kea is a promising new dhcp server from the same upstream that created Bind and isc-dhcp. For Focal, we updated it to the 1.6.x stable series.

Upstream 1.6.0 release notes: [downloads.isc.org/isc/kea/1.6.0/Kea160ReleaseNotes.txt](https://downloads.isc.org/isc/kea/1.6.0/Kea160ReleaseNotes.txt)

Upstream 1.6.2 release notes (version currently in Focal): [downloads.isc.org/isc/kea/1.6.2/Kea162ReleaseNotes.txt](https://downloads.isc.org/isc/kea/1.6.2/Kea162ReleaseNotes.txt)


(20-04-lts-bind-9-16)=
#### Bind 9.16

Bind has been updated to the new stable release series from upstream: 9.16.x.

Important packaging changes are:

* no `-dev` package at the moment, as upstream discourages linking with its libraries. See a bit of a discussion about that here: [gitlab.isc.org/isc-projects/bind9/-/merge_requests/3089#note_111299](https://gitlab.isc.org/isc-projects/bind9/-/merge_requests/3089#note_111299). Debian just added the `dev` package back (2020-04-16), we might follow with an SRU: [bugs.debian.org/954906](https://bugs.debian.org/954906)

* `bind-libs` 9.11.x package: used for software projects that do not yet work with the new 9.16 version, like isc-dhcp.

* `bind-dyndb-ldap` has not yet been ported to bind9 9.16.x

* `geoip` legacy support was removed and replaced with `geoip2` (`libmaxminddb`)

Upstream blog post about major changes in `bind9` 9.16.0: [www.isc.org/blogs/bind9.16.0_released/](https://www.isc.org/blogs/bind9.16.0_released/)

More detailed release notes: [downloads.isc.org/isc/bind9/9.16.0/RELEASE-NOTES-bind-9.16.0.html](https://downloads.isc.org/isc/bind9/9.16.0/RELEASE-NOTES-bind-9.16.0.html)

Presentation about the development of `bind9` culminating in this new release: [youtu.be/5math9Oy97s?t=46](https://youtu.be/5math9Oy97s?t=46)


(20-04-lts-openssh-updates-with-u2f-support)=
#### OpenSSH updates with U2F Support

OpenSSH 8.2 added support for U2F/FIDO hardware devices to allow easy hardware-based two factor authentication. It is as simple as:

```none
# plug device in and:

$ ssh-keygen -t ecdsa-sk
Generating public/private ecdsa-sk key pair.
You may need to touch your authenticator to authorize key generation. <-- touch device
Enter file in which to save the key (/home/ubuntu/.ssh/id_ecdsa_sk):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/ubuntu/.ssh/id_ecdsa_sk
Your public key has been saved in /home/ubuntu/.ssh/id_ecdsa_sk.pub
The key fingerprint is:
SHA256:V9PQ1MqaU8FODXdHqDiH9Mxb8XK3o5aVYDQLVl9IFRo ubuntu@focal
```

Now just transfer the public part to the server to `~/.ssh/authorized_keys` and you are ready to go:

```none
$ ssh -i .ssh/id_ecdsa_sk ubuntu@focal.server
Confirm user presence for key ECDSA-SK SHA256:V9PQ1MqaU8FODXdHqDiH9Mxb8XK3o5aVYDQLVl9IFRo <-- touch device
Welcome to Ubuntu Focal Fossa (development branch) (GNU/Linux 5.4.0-21-generic x86_64)
(...)
ubuntu@focal.server:~$
```

:::{warning}
If you don't see the prompt asking for the user presence confirmation, then you are affected by

  - `block-discover` supports multipath discovery
  - `vmtest` add ppc64le/arm64 architectures
:::

Upstream development of OpenSSH 8.2 in Debian has [added support for an 'Includes' keyword](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=631189) in configuration files.  This allows including additional configuration files via glob(3) patterns.  By default the system sshd config (/etc/ssh/sshd_config) now [includes files under /etc/ssh/sshd_config.d/*.conf](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=952427).  For each keyword encountered in configuration files, the first obtained value will be used.  This is used in various [Cloud Images](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes#Cloud_Images_.2BJgE-) to apply cloud-specific tuning while avoiding debconf prompts on package upgrade.

The effective configuration of sshd can be validated by running 'sudo sshd -T'. This reads and validates the config file(s) and prints the effective configuration before exiting.

See the upstream release notes for more details: [www.openssh.com/txt/release-8.2](https://www.openssh.com/txt/release-8.2)


(20-04-lts-haproxy-2-0)=
#### HAProxy 2.0

First introduced in Ubuntu Eoan 19.10, HAProxy in Focal is tracking the upstream LTS 2.0 branch. This series has many new features when compared to the previous 1.8 stable branch, and all are detailed in this blog post: [www.haproxy.com/blog/haproxy-2-0-and-beyond/](https://www.haproxy.com/blog/haproxy-2-0-and-beyond/)


(20-04-lts-apache-tlsv1-3-client-cert-auth)=
#### Apache, TLSv1.3, client cert auth

Apache has been built with TLSv1.3 support, and depending on the server configuration, this might require clients performing certificate authentication to support Post Handshake Authentication (PHA). Not all TLSv1.3 capable clients can perform PHA, and will fail. Telltale signs of this being the error include these messages in the Apache server logs:

```none
AH: verify client post handshake
AH10158: cannot perform post-handshake authentication
SSL Library Error: error:14268117:SSL routines:SSL_verify_client_post_handshake:extension not received
```

In this case, if there is no updated client version, you should preferably disable TLSv1.3 on the affected client.

Chromium bug: [bugs.chromium.org/p/chromium/issues/detail?id=911653](https://bugs.chromium.org/p/chromium/issues/detail?id=911653)

Firefox bug: [bugzilla.mozilla.org/show_bug.cgi?id=1511989](https://bugzilla.mozilla.org/show_bug.cgi?id=1511989) (fixed, can be enabled by toggling security.tls.enable_post_handshake_auth)

Python `httplib` should enable post-handshake authentication for TLS 1.3: [bugs.python.org/issue37440](https://bugs.python.org/issue37440)


(20-04-lts-samba-4-11)=
#### Samba 4.11

Focal ships with Samba 4.11.x which introduces a number of changes. Of note we have:

* SMB1 disabled by default: can still be enabled via a `/etc/samba/smb.conf` config change;

* python2 no longer supported

Detailed upstream release notes for 4.11.0 can be seen here: [www.samba.org/samba/history/samba-4.11.0.html](https://www.samba.org/samba/history/samba-4.11.0.html)


(20-04-lts-postgresql-12)=
#### PostgreSQL 12

Focal is shipping postgresql-12, which has many improvements:

* improved query performance, particularly over larger data sets
* SQL/JSON path expression support
* generated columns
* pluggable table storage interface

Upstream announcement: [www.postgresql.org/about/news/1976/](https://www.postgresql.org/about/news/1976/)

Upstream release notes: [www.postgresql.org/docs/12/release-12.html](https://www.postgresql.org/docs/12/release-12.html)


(20-04-lts-nginx)=
#### nginx

Starting in Focal Fossa, `nginx-core` no longer ships with the legacy `geoip` module enabled by default. If you are using the legacy `geoip` module in nginx, you may run into upgrade issues if you do not deactivate the `geoip` module in your configuration. This was done as part of the deprecation of GeoIP legacy support.

Here are some scenarios you might encounter:

* Since `nginx-core` dropped the dependency on `libnginx-mod-http-geoip`, an `apt autoremove` might suggest that `libnginx-mod-http-geoip` can be removed. If this happens, and there are still `geoip` configuration directives, nginx will fail to restart. Note that this would also happen had we replaced `libnginx-mod-http-geoip` with `libnginx-mod-http-geoip2`, as the configuration directives are different

* If someone has just main enabled, with `nginx-code` and `libnginx-mod-http-geoip` installed, and release upgrades to Focal, `libnginx-mod-http-geoip` won't be updated because it's in `focal/universe`.


(20-04-lts-squid-4-x)=
#### Squid 4.x

When upgrading from the previous LTS Ubuntu Bionic 18.04, the squid proxy cache will be at version 4. Among other changes, if you used custom logging format, be aware the redefining the build-in formats no longer works (upstream bug: [bugs.squid-cache.org/show_bug.cgi?id=4905](https://bugs.squid-cache.org/show_bug.cgi?id=4905)).

For example, if you were redefining the `squid` log format to change the timestamp, like this:

```none
logformat squid  %tg{%F %H:%M:%S %z} %6tr %>a %Ss/%03>Hs %<st %rm %ru %[un %Sh/%<a %mt
```

You now have to use another name, and specify that it should be used, like this:

```none
logformat custom-squid  %tg{%F %H:%M:%S %z} %6tr %>a %Ss/%03>Hs %<st %rm %ru %[un %Sh/%<a %mt
access_log daemon:/var/log/squid/access.log custom-squid
```


(20-04-lts-s390x)=
#### s390x

IBM Z and LinuxONE / s390x-specific enhancements since 19.10 (partly not limited to s390x):

* Starting with Ubuntu Server 20.04 LTS the architectural level set was changed to z13 (Bug:1836907). This has a significant impact: Ubuntu Server for s390x now benefits from improved and more instructions that got introduced with z13 hardware; at the same time support for zEC12/zBC12 got dropped and the minimum supported hardware is now IBM z13 and LinuxONE Rockhopper (I) and LinuxONE Emperor (I).

* Secure Execution, a Trusted Execution Environment (TEE) for IBM Z and LinuxONE is now supported. It required adaptations in the kernel (Bug:1835531), qemu (Bug:1835546) and s390-tools (Bug:1834534). It can only be used with IBM z15 and LinuxONE III. With Secure Execution (or the upstream name 'protected virtualization' aka `protvirt`) workloads can run virtualized in full isolation with protection for both internal and external threats, using hardware assisted key based encryption for the guest memory.

* The toolchain was significantly upgraded to gcc 9.3 - making sure that fixes like (Bug:1862342) are included, even moved to gdb 9.1 (Bug:1825344), that includes latest s390x hardware support - similar with LLVM, that was upgraded to v10 (Bug:1853145), again to have the latest s390x hardware enhancements included (Bug:1853269).

* The KVM virtualization stack got updated to qemu 4,2 and libvirt 6.0, and with that CPU model comparison and baselining got enabled (Bug:1853315), CCW IPL support added to qemu (Bug:1853316) and libvirt (Bug:1853317) and several issue fixed, like (Bug:1861125), (Bug:1867109) and (Bug:1866207). In addition KVM crypto pass-through is now included (Bug:1852737), (Bug:1852738) and (Bug:1852744).

* Support for new CEX7S crypto express hardware (Bug:1853304) and (Bug:1856831) was added, as well as CPACF MSA 6 in-kernel crypto support for SHA3 (Bug:1853105) and a lot of CPACF crypto co-processor (largely assembly based) optimizations and fixes in OpenSSL (Bug:1853150) and (Bug:1853312), incl. but not limited to ECDSA.

* Performance tests showed (Bug:1868113) that it is beneficial to use 'Striding RQ' with RoCE Express 2 and 2.1 PCIe cards (ConnectX-4) on IBM z14 and LinuxONE Rockhopper II / Emperor II and newer - but this is not the default. Hence if one has RoCE 2 or 2.1 hardware plugged in to such a system, the enablement of 'Striding RQ' should be considered, like: '`ethtool --set-priv-flags <ifname> rx_striding_rq on`'. For the reason of persistence one may also create a service or udev-rule that sets this at boot time.


(20-04-lts-openstack-ussuri)=
#### OpenStack Ussuri

Ubuntu 20.04 LTS includes the latest OpenStack release, Ussuri, as a preview with final release coming in the 20.04.1 LTS, including the following components:

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

Please refer to the [OpenStack Ussuri release notes](http://releases.openstack.org/ussuri/) for full details of this release of OpenStack.

OpenStack Ussuri is also provided via the [Ubuntu Cloud Archive](https://wiki.ubuntu.com/OpenStack/CloudArchive) for OpenStack Ussuri for Ubuntu 18.04 LTS users.

**WARNING**: Upgrading an OpenStack deployment is a non-trivial process and care should be taken to plan and test upgrade procedures which will be specific to each OpenStack deployment.

Make sure you read the [OpenStack Charm Release Notes](https://docs.openstack.org/charm-guide/latest) for more information about how to deploy Ubuntu OpenStack using Juju.


(20-04-lts-ceph)=
#### Ceph

Ceph was updated to the 15.2.1 release, Ceph Octopus. Please refer to the [Ceph Octopus release notes](https://docs.ceph.com/docs/master/releases/octopus/) for full details of this release.

This release of Ceph is also provided via the [Ubuntu Cloud Archive](https://wiki.ubuntu.com/OpenStack/CloudArchive) for use with OpenStack Ussuri for Ubuntu 18.04 LTS users.


(20-04-lts-cloud-images)=
### Cloud Images ☁


(20-04-lts-amazon-web-services-aws)=
#### Amazon Web Services (AWS)

* Amazon Machine Images (AMIs) have the [ec2-instance-connect](https://launchpad.net/ubuntu/+source/ec2-instance-connect) package installed and enabled by default starting in Focal.  AWS' [Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html) feature uses AWS Identity and Access Management (IAM) policies and principals to control SSH access to your instances.


(20-04-lts-google-compute-engine)=
#### Google Compute Engine

* The existing sshd config overrides that were written to /etc/ssh/sshd_config have been moved to /etc/ssh/sshd_config.d/50-cloudimg-settings.conf, see [OpenSSH Includes Keyword](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes#OpenSSH_Includes_Keyword) above.


(20-04-lts-microsoft-azure)=
#### Microsoft Azure

* Azure instances now use chrony to manage time synchronization, and they are configured by default to use highly accurate Stratum 1 devices hosted in the Azure cloud. See more information: [Time sync for Linux VMs in Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/time-sync)

* The existing sshd config overrides that were written to /etc/ssh/sshd_config have been moved to /etc/ssh/sshd_config.d/50-cloudimg-settings.conf, see [OpenSSH Includes Keyword](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes#OpenSSH_Includes_Keyword) above.


(20-04-lts-vagrant)=
#### Vagrant

* Vagrant boxes are 40G by default instead of 10G. [(LP: #1580596)](https://bugs.launchpad.net/cloud-images/+bug/1580596)


(20-04-lts-raspberry-pi)=
### Raspberry Pi

Since the release of Ubuntu 19.10 Raspberry Pi 32-bit and 64-bit preinstalled images (renamed to raspi) support the Raspberry Pi 4 platform out-of-the-box. With this, our images now support almost all modern flavors of the Raspberry Pi family of devices (Pi 2B, Pi 3B, Pi 3A+, Pi 3B+, CM3, CM3+, Pi 4B). Starting from Ubuntu Server 20.04.2, support for the CM4 (all variants) and the Pi 400 has been added too.


(20-04-lts-known-issues)=
## Known issues

As is to be expected, with any release, there are some significant known bugs that users may run into with this release of Ubuntu 20.04 LTS.  The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:


(20-04-lts-installer-and-live-session)=
### Installer and live session

* **Systems with an nVidia graphics card**: These systems boot the live session by default with the open source video driver 'nouveau'. On some hardware this driver may crash which results in a freeze of the graphical session of the installer. If it happens, on the boot menu, select a 'Safe graphics mode' entry. Then in the installer, on the 'Preparing to install ...' page, select 'Install third party software ...' and continue. This option will install the nVidia proprietary drivers on the target system. Upon installation the proprietary drivers for your card will be loaded and the graphical session should work properly with optimized drivers. (Bug:1871562)

* During the desktop installation process it is possible for the keyboard layout to revert to an English one, to mitigate issues when entering your password there is now an option to view your password when entering it. Investigation into the root cause and fixing the bug is on going. ([bug 1875062](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1875062))

* Ubuntu now defaults to checking the integrity of the medium in use when booting into live sessions. This can be skipped by hitting Ctrl-C, but due to a bug the message that tells you to hit this key is not shown in some flavours. ([bug 1870018](https://bugs.launchpad.net/ubuntu/+source/casper/+bug/1870018))

* When selecting to install 3rd party drivers there can be a long pause before the next step is available. ([bug 1824905](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1824905))

* With certain Broadcom wireless cards if you choose to install third party software during the installation process your wifi will disconnect. ([bug 1867465](https://bugs.launchpad.net/bugs/1867465))



(20-04-lts-distribution-upgrades)=
### Distribution Upgrades

* For Ubuntu 18.04 systems with clang-6.0 and pocl-opencl-icd it is not possible for the release upgrader to calculate the upgrade to Ubuntu 20.04. ([bug 1886748](https://bugs.launchpad.net/bugs/1886748)) It is possible to workaround this by removing clang-6.0 or libomp5 and then upgrading.


(20-04-lts-desktop)=
### Desktop

* Fractional scaling does not work with the NVIDIA proprietary driver ([bug 1870736](https://bugs.launchpad.net/bugs/1870736), [bug 1873403](https://bugs.launchpad.net/bugs/1873403)).

* Automatic login does not work with the NVIDIA proprietary driver ([bug 1845801](https://bugs.launchpad.net/bugs/1845801)).

* After upgrading audio device selection in Settings is sometimes ignored ([bug 1866194](https://bugs.launchpad.net/bugs/1866194)).

* ZFS installation fails to boot if there are existing pools named `bpool` or `rpool` on a second drive ([bug 1867007](https://bugs.launchpad.net/bugs/1867007)).

* Due to database format changes fprintd will remove all saved fingerprints, please ensure you have another mechanism for logging in ([launchpad.net/bugs/1865824](http://launchpad.net/bugs/1865824)).


(20-04-lts-raspberry-pi-2)=
### Raspberry Pi

* The [Pimoroni Fan Shim](https://pinout.xyz/pinout/fan_shim#) for the Raspberry Pi 4 re-uses the serial console pins on the GPIO header to control its RGB LED. This results in "noise" on the serial line which stops u-boot during startup (as it thinks a key has been pressed). Adding `enable_uart=0` to `/boot/firmware/syscfg.txt` disables the serial console permitting the boot sequence to complete ([bug 1873520](https://launchpad.net/bugs/1873520))

* For 20.04.1 and later, HDMI is used for audio output by default if it is connected. To force output over the headphone jack, create a file called '.asoundrc' in the user's home directory with the following contents:

```none
    defaults.pcm.card 1
    defaults.ctl.card 1

```


(20-04-lts-risc-v)=
### RISC-V

* Reboot and shutdown commands do not currently work on the HiFive Unmatched. Power cycling requires physical access to the board. ([bug 1937055](https://bugs.launchpad.net/ubuntu/+source/opensbi/+bug/1937055))


(20-04-lts-server)=
### Server

* `gdisk`/`sgdisk` versions older than 1.0.8 erroneously write partition labels byte-swapped on big endian architectures. This is non critical and on s390x mainly affects virtio and FCP/SCSI disk partition labels (so any non-DASD-ECKD) - in case they were written by `gdisk`. Since this was always wrong - but written and read the same swapped way - it worked so far. Hence old releases just stay that way, but starting with 1.0.8 in Impish this is solved and even allows to fix/convert old broken labels. Newly created partitions and label with `gdisk` 1.0.8 will be correct; existing ones that were created with older `gdisk` version (that maybe re-used after a `dist-upgrade` etc.) need to be fixed/converted. ([bug 1931243](https://bugs.launchpad.net/bugs/1931243)).

* With Ubuntu Server 20.04.2 on IBM Z and LinuxONE (s390x) it is currently not possible to boot/IPL from NVMe devices that are represented as multipath devices. In case NVMe devices are used on s390x that are multipath capable, the multipath option needs to be switched off with the help of the kernel parameter `nvme-core.multipath=0`, otherwise `chreipl` will not work properly and the post-install reboot fails ([bug 1902179](https://bugs.launchpad.net/bugs/1902179)).


(20-04-lts-general)=
### General

* This is not an issue per-se, but enough visible to be release-note worthy. Starting with 20.04.3 `useradd` will not allow creating full-numeric usernames (e.g. 123, 1337). Such usernames cause issues with components such as systemd, so it was safer to disallow them altogether ([bug 1927078](https://bugs.launchpad.net/bugs/1927078)).


(20-04-lts-official-flavours)=
## Official flavours

The release notes for the official flavors can be found at the following links:

* Lubuntu [lubuntu.me/focal-released/](https://lubuntu.me/focal-released/)

* Kubuntu [wiki.ubuntu.com/FocalFossa/ReleaseNotes/Kubuntu](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes/Kubuntu)

* Ubuntu Budgie [19.10 Upgraders](https://ubuntubudgie.org/2020/04/02/ubuntu-budgie-20-04lts-release-notes/) / [18.04 Upgraders](https://ubuntubudgie.org/2020/04/21/ubuntu-budgie-20-04lts-release-notes-for-18-04-upgraders/)

* Ubuntu MATE [ubuntu-mate.org/blog/ubuntu-mate-focal-fossa-release-notes/](https://ubuntu-mate.org/blog/ubuntu-mate-focal-fossa-release-notes/)

* Ubuntu Studio [wiki.ubuntu.com/FocalFossa/ReleaseNotes/UbuntuStudio](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes/UbuntuStudio)

* Xubuntu [wiki.xubuntu.org/releases/20.04/release-notes](https://wiki.xubuntu.org/releases/20.04/release-notes)

* Ubuntu Kylin [www.ubuntukylin.com/news/2004ReleaseNotes-en.html](https://www.ubuntukylin.com/news/2004ReleaseNotes-en.html)


(20-04-lts-more-information)=
## More information


(20-04-lts-reporting-bugs)=
### Reporting bugs

Your comments, bug reports, patches and suggestions will help fix bugs and improve the quality of future releases. Please [report bugs using the tools provided](http://help.ubuntu.com/community/ReportingBugs).

If you want to help out with bugs, the [Bug Squad](http://wiki.ubuntu.com/BugSquad) is always looking for help.


(20-04-lts-participate-in-ubuntu)=
### Participate in Ubuntu


If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

[community.ubuntu.com/contribute](https://community.ubuntu.com/contribute)


(20-04-lts-more-about-ubuntu)=
### More about Ubuntu

You can find out more about Ubuntu on the [Ubuntu website](https://www.ubuntu.com) and [Ubuntu wiki](https://wiki.ubuntu.com).

To sign up for future Ubuntu development announcements, please subscribe to Ubuntu's development announcement list at:

[lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce](https://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce)
