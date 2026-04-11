---
tocdepth: 3
---

<!-- SOURCE: https://discourse.ubuntu.com/t/kinetic-kudu-release-notes/27976 -->

(ubuntu-22-10-release-notes)=
# Ubuntu 22.10 release notes

## Introduction

These release notes for **Ubuntu 22.10** (Kinetic Kudu) provide an overview of the release and document the known issues with Ubuntu and its flavours.

## Support lifespan

Ubuntu 22.10 will be supported for 9 months until July 2023. If you need Long Term Support, it is recommended you use [Ubuntu 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes/) instead.

## New features in 22.10

## Updated Packages

### Linux kernel 🐧

Ubuntu 22.10 is shipped with the new 5.19 Linux kernel that brings the following (most relevant) features (in addition to many other new features, new drivers, improvements and fixes):

* The new `futex_waitv()` syscall that can speed up games by letting them wait for multiple futexes with a single system call.
* Support in the task scheduler for CPU clusters that share L2/L3 cache (spreading tasks between clusters will bring more memory bandwidth and decrease cache contention).
* Support for Intel® AMX (Advanced Matrix Extensions) instructions.
* CO-RE support that makes compiled BPF programs more portable.
* A faster random number generator (entropy extractor switched from SHA1 to BLAKE2s).
* Support for proactive reclaim in memory control groups.
* Support for Intel® Trust Domain Extensions (TDX).

### systemd v251.4

The init system was updated to systemd v251.4. Please refer to the upstream [changelog](https://github.com/systemd/systemd/releases/tag/v251) for more information about individual features. 

## Toolchain Upgrades 🛠️

### debuginfod support

Following the recent [announcement](https://lists.ubuntu.com/archives/ubuntu-devel-announce/2022-September/001320.html) of our [debuginfod instance](https://debuginfod.ubuntu.com), Ubuntu now automatically requests debug symbols from the service when GDB (or any other debuginfo-consuming application) is used.  Please refer to the [Ubuntu Server Guide on debuginfod](https://discourse.ubuntu.com/t/service-debuginfod/30534/10) for more information.

## Security Improvements 🔒

* AppArmor gained support for restricting access to unprivileged user namespaces. This allows a system administrator to configure their system so that only applications and services which are confined by an appropriate AppArmor profile can use this feature. 

## Base System

* [Netplan v0.105](https://github.com/canonical/netplan/releases/tag/0.105) gained support for VXLAN, VRF and InfiniBand devices

## Ubuntu Desktop
- The default audio server is now PipeWire instead of PulseAudio
- The default image apps now suport the _.webp_ format

### GNOME 👣
- GNOME has been updated to include new features and fixes from the latest GNOME release, [GNOME 43](https://release.gnome.org/43/)
- Many apps have been converted to GTK4 and libadwaita for improved performance and upgraded style.
- The default file manager Nautilus has switched to GTK4. The Nautilus Extensions API has changed which breaks all Nautilus extensions that have not been updated for the new release.
- The default text editor app is now GNOME Text Editor. _gedit_ is still available for install.
- The default terminal app is still GNOME Terminal but GNOME Console is available for install.
- The To Do app is no longer installed by default. It's still available for install but has been renamed to _Endeavour_ .
- The GNOME Books app is no longer available. The recommended replacement app is _Foliate_ .
- The Nautilus folder sharing extension is no longer installed by default. You can install it from a terminal with `sudo apt install nautilus-share`

### Updated Applications

* [Firefox](https://mozilla.org/firefox/releases/) 106 🔥🦊
* [LibreOffice 7.4 ](https://wiki.documentfoundation.org/ReleaseNotes/7.4) 📚
* Thunderbird 102 🌩️🐦

### Updated Subsystems

* [BlueZ 5.65 ](https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/ChangeLog?id=5.65)
* [CUPS 2.4 ](https://github.com/OpenPrinting/cups/blob/v2.4.2/CHANGES.md)
* [NetworkManager 1.40 ](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/blob/nm-1-40/NEWS)
* [Mesa 22 ](https://docs.mesa3d.org/relnotes/22.0.0.html)
* [Pipewire 0.3.58](https://gitlab.freedesktop.org/pipewire/pipewire/-/blob/0.3.57/NEWS)
* [Poppler 22.08](https://gitlab.freedesktop.org/poppler/poppler/-/blob/poppler-22.08.0/NEWS)
* [PulseAudio 16](https://www.freedesktop.org/wiki/Software/PulseAudio/Notes/16.0/)
* [xdg-desktop-portal 1.15](https://github.com/flatpak/xdg-desktop-portal/blob/1.15.0/NEWS)
* fonts-noto-color-emoji updated for Unicode 15

## Ubuntu Server

### Subiquity 22.10.1
The Ubuntu 22.10 Live Server includes Subiquity 22.10.1, which adds a variety of bugfixes and a few new features including enhancements to autoinstall, cloud-init integration, and keyboard handling.  Please see the Subiquity [release notes](https://discourse.ubuntu.com/t/subiquity-22-10-1-has-been-released-to-stable/31553) for more details.

### Socket-activated SSHd
In Ubuntu 22.10, openssh now uses systemd socket activation by default.  Read more about this new feature [here](https://discourse.ubuntu.com/t/sshd-now-uses-socket-based-activation-ubuntu-22-10-and-later/30189).

### SSSD

* All SSSD client libraries (`nss`, `pam`, etc.) won't serialize requests anymore by default, i.e. requests from multiple threads can be executed in parallel. The old behavior (serialization) can still be enabled by setting the environment variable `SSS_LOCKFREE` to `NO`.
* Added a new krb5 plugin `idp` and a new binary `oidc_child` which performs **OAuth2** authentication against FreeIPA. This, however, cannot be tested yet because this feature is still under development on the FreeIPA server side.

### Support for LDAP Channel Binding and Signing for Windows Integration
[`cyrus-sasl2`](https://launchpad.net/ubuntu/+source/cyrus-sasl2/) has been [patched](https://launchpad.net/ubuntu/+source/cyrus-sasl2/2.1.28+dfsg-6ubuntu2) to support [new requirements](https://support.microsoft.com/en-us/topic/2020-ldap-channel-binding-and-ldap-signing-requirements-for-windows-kb4520412-ef185fb8-00f7-167d-744c-f299a66fc00a) for Windows Server: [LDAP Channel Binding](https://support.microsoft.com/help/4034879) and [LDAP Signing](https://support.microsoft.com/help/935834).

When using GSSAPI/GSS-SPNEGO authentication over an encrypted transport like `ldaps://`, Microsoft recommends that Channel Binding be enabled. If Windows Server is configured to require this setting, then clients that do not enable Channel Binding over such connections will be rejected.

### Bind9

* Add support for remote TLS certificate verification, both to [`named`](https://bind9.readthedocs.io/en/v9_18_7/manpages.html#std-iscman-named) and [`dig`](https://bind9.readthedocs.io/en/v9_18_7/manpages.html#std-iscman-dig), making it possible to implement Strict and Mutual TLS authentication, as described in [**RFC 9103**](https://datatracker.ietf.org/doc/html/rfc9103.html), Section 9.3.

### Rsync

* A new form of argument protection was added that works similarly to the older `--protect-args` ([`-s`](https://github.com/WayneD/rsync/blob/master/rsync.1.md#options)) option, but in a way that avoids breaking things like `rrsync` (the restricted `rsync` script): `rsync` now uses backslash escaping for sending "shell-active" characters to the remote shell. This includes spaces, so fetching a remote file via a simple quoted filename value now works by default without any extra quoting:

    `rsync -aiv host:'a simple file.pdf' .`

    Wildcards are not escaped in filename arguments, but they are escaped in options like the [`--suffix`](https://github.com/WayneD/rsync/blob/master/rsync.1.md#options) and [`--usermap`](https://github.com/WayneD/rsync/blob/master/rsync.1.md#options) values. If your `rsync` script depends on the old arg-splitting behavior, either run it with the [`--old-args`](https://github.com/WayneD/rsync/blob/master/rsync.1.md#options) option or `export RSYNC_OLD_ARGS=1` in the script's environment. See also the [ADVANCED USAGE](https://github.com/WayneD/rsync/blob/master/rsync.1.md#advanced-usage) section of `rsync`'s manpage for how to use a more modern argument style.

### Resource agents 4.11.0

Improvements in many agents such as:

- IPaddr2: allow to disable Duplicate Address Detection for IPv6; and allow to send IPv6 Neighbor Advertisements in background.
- LVM-activate: disable VG autoactivation in `system_id access_mode`.

Those are some of the changes added to the resource-agent-base binary package which is in main, to check a full list of the changes see the [upstream changelog](https://github.com/ClusterLabs/resource-agents/blob/main/ChangeLog#L2-L136).

### Fence agents 4.11.0

`fence-virtd` and `fence-virt` were introduced as new binary packages in this version.

### OpenVPN 2.6.0 snapshot

OpenVPN 2.6.0 was not released yet, so Ubuntu Kinetic will ship a git snapshot instead. This new version contains some improvements regarding OpenSSL 3 support. Another important change that might impact users is the drop of the `--cipher` option in favor of the new `--data-ciphers`.  It is important to note that when `--data-ciphers` is not specific, the default will be `AES-256-GCM:AES-128-GCM:CHACHA20-POLY1305`.  This can impact users that are using old ciphers, like `AES-256-CBC`.  In this scenario, it is recommended that users migrate their certificates to the ciphers that are supported by default.  A workaround is possible by explicitly setting `--data-ciphers`.

For more details on cipher negotiation, please read the [upstream documentation](https://github.com/OpenVPN/openvpn/blob/master/doc/man-sections/cipher-negotiation.rst).

### Containerd 1.6.4

This contains some major release changes which can all be seen [here](https://github.com/containerd/containerd/releases). Now, it has support for shim plugins and added support for absolute path to shim binaries.

### Runc 1.1.2

This new version contains an important CVE fix and also a bunch of improvements, fixing bugs and improving the upstream CI system. For more detailed information please check the [upstream changelog](https://github.com/opencontainers/runc/blob/main/CHANGELOG.md).

### Docker.io 20.10.16

This new version contains fixes to avoid potential lock issues and update its dependencies internally. For more detailed information please check the [upstream changelog](https://docs.docker.com/release-notes/).

#### qemu

Qemu was updated to version v7.0.0 which brings many major and minor improvements. Among others this version includes:

 * Added support for Intel AMX
 * Support for various further RISC-V extensions, among them the hypervisor extension is no more marked experimental and now enabled by default
 * Fixes for various emulated s390x instructions
 * User-mode emulation (`linux-user`, `bsd-user`) will enforce guest alignment constraints and raise 
`SIGBUS` to the guest program as appropriate.
 * The `qemu-nbd` program has gained a new `--tls-hostname` parameter to allow TLS validation against a different hostname, such as when setting up TLS through a TCP tunnel, and now supports TLS over Unix sockets.
 * See the upstream [changelog for version 7.0](https://wiki.qemu.org/ChangeLog/7.0) for an overview of the many further improvements. These also contain a list of suggested alternatives for removed, deprecated and incompatible features.

#### libvirt

Tracking the releases of libvirt continuously version v8.6.0 is now provided in Ubuntu 22.10 which - among many other fixes, improvements and features - includes:

*  For example there have been many new features for qemu:
   * Support mode option for `dirtyrate` calculation.
   * Introduce manual disk snapshot mode.
   * Introduce memory allocation threads (handy for guests with large amounts of memory).
   * Introduce support for `virtio-iommu`.
   * ppc64 Power10 processor support.
   * Introduce absolute clock offset.
   * Add support for post-copy migration recovery.
 * See the [upstream changelogs](https://libvirt.org/news.html) for the many further improvements and fixes since version 8.0.0 that was in [Ubuntu 22.04](https://discourse.ubuntu.com/t/jammy-jellyfish-release-notes/24668).

#### openvswitch

The new version 3.0.0 of openvswitch is in Ubuntu 22.10 and provides a general update including the following changes:

 * Userspace datapath improved multi-thread scalability of the userspace connection tracking.
 * IPsec now has custom per-tunnel options.
 * Extended Flow Monitoring to support more OpenFlow versions.
 * OVSDB compaction was improved to run in a separate process (avoiding blocks) and is enabled by default to return unused memory to the system.
 * libopenvswitch API changes to fix the undefined compiler behavior will need users of libopenvswitch to double-check the use of loop macros like `LIST_FOR_EACH`.
 * [The OVS News](https://www.openvswitch.org/releases/NEWS-3.0.0.txt) page holds more details about the new version.


### OpenStack

Ubuntu 22.10 includes the latest OpenStack release, Zed, including the following components:

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

Please refer to the [OpenStack Zed release notes](https://releases.openstack.org/zed/) for full details of this release of OpenStack.

OpenStack Zed is also provided via the [Ubuntu Cloud Archive](https://wiki.ubuntu.com/OpenStack/CloudArchive) for OpenStack Zed for Ubuntu 22.04 LTS users.

WARNING: Upgrading an OpenStack deployment is a non-trivial process and care should be taken to plan and test upgrade procedures which will be specific to each OpenStack deployment.

Make sure you read the [OpenStack Charm Release Notes](https://docs.openstack.org/charm-guide/latest) for more information about how to deploy and operate Ubuntu OpenStack using Juju.

## Platforms

### Cloud Images ☁

* There will be no longer AWS Marketplace container images available for Kinetic and later releases. Please use the offerings from the [AWS ECR Public Gallery](https://gallery.ecr.aws/ubuntu) or other container registries.

### Raspberry Pi 🍓

* Ubuntu 22.10 includes support for several "embedded" displays on the Raspberry Pi, under both server and desktop configurations. Supported displays include the [official DSI display](https://www.raspberrypi.com/products/raspberry-pi-touch-display/) (though, see Known Issues below), the [Hyperpixel](https://github.com/pimoroni/hyperpixel4) and the range of [Inky displays](https://github.com/pimoroni/inky) ([bug 1992778](https://launchpad.net/bugs/1992778)). See [this post](https://waldorf.waveform.org.uk/2022/hyping-pixels.html) for full details on the Hyperpixel.

* Ubuntu 22.10 builds on existing support for the [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) by adding the [mpremote](https://pypi.org/project/mpremote/) utility to the archive ([bug 1992777](https://launchpad.net/bugs/1992777)), permitting easier development with [MicroPython](https://docs.micropython.org/en/latest/) environments with facilities including the ability to mount local directories on your attached MicroPython device.

* The 5.19 kernel in Ubuntu 22.10 disables the (long deprecated) [GPIO sysfs interface](https://docs.kernel.org/admin-guide/gpio/sysfs.html) ([bug 1918583](https://bugs.launchpad.net/bugs/1918583)). This means that several common GPIO libraries (including [RPi.GPIO](https://pypi.org/project/RPi.GPIO/)) cannot operate. A shim providing [compatibility with RPi.GPIO](https://rpi-lgpio.readthedocs.io/en/latest/) has been created and is available in Kinetic in the `python3-rpi-lgpio` package. See [this post](https://waldorf.waveform.org.uk/2022/the-one-where-dave-breaks-stuff.html) for full details.

* The webkit component in Gnome now works ([bug 1924251](https://bugs.launchpad.net/bugs/1924251)) with the result that the offline Help application, and Online Accounts settings now operate correctly.

* The `raspi-config` utility has been updated to partially work in Ubuntu ([bug 1972982](https://launchpad.net/bugs/1972982)). Some facilities (e.g. RealVNC support) do not work, but now correctly report they are not supported. Other facilities (e.g. overlayfs) work correctly.

* The `netplan` utility now supports selection of the wifi regulatory domain through its configuration, including on initial boot via `cloud-init`; examples on the boot partition have been updated accordingly ([bug 1951586](https://launchpad.net/bugs/1951586)).

### s390x

Starting with Ubuntu Server 20.04 LTS, the minimal architectural level set was raised to z13 (and LinuxONE Rockhopper / Emperor) - this still applies to Ubuntu Server 22.10 and support also includes all newer hardware that is in service as of today (22.10 release date). Support for additional future hardware might be added later.
Ubuntu Server 22.10 can be installed in LPAR (classic or DPM systems), as IBM z/VM guest, as KVM virtual machine and in different container environments, like LXD, docker or kubernetes.
It's available as ISO, Cloud or container images.

IBM Z and LinuxONE / s390x-specific enhancements since 22.04 (partially not limited to s390x):

* The s390-tools ([bug 1986991](https://bugs.launchpad.net/bugs/1986991)) are now at version 2.23, which incl. site-aware environment block support in zipl ([bug 1982368](https://bugs.launchpad.net/bugs/1982368)) and additional information provided to the SCLP CPI ([bug 1982390](https://bugs.launchpad.net/bugs/1982390)).

* Enhancements in Secure Execution with especially the new attestation tool ([bug 1959987](https://bugs.launchpad.net/bugs/1959987)) and the guest dump encryption with customer keys ([bug 1959940](https://bugs.launchpad.net/bugs/1959940)).

* And further dump enhancements with the NVMe stand-alone dump support ([bug 1929033](https://bugs.launchpad.net/bugs/1929033)).

* Support for latest hardware with adding IBM z16 Processor-Activity-Instrumentation Facility support (([bug 1982384](https://bugs.launchpad.net/bugs/1982384)) and ([bug 1982384](https://bugs.launchpad.net/bugs/1982384))), additional CPU-MF counters for new hardware for libpfm ([bug 1960118](https://bugs.launchpad.net/bugs/1960118)) and support for the latest IBM zSystems hardware generations in qclib ([bug 1982332](https://bugs.launchpad.net/bugs/1982332)).

* On top of the updated virtualization stack (see above), further virtualization improvements with crypto passthrough hotplug ([bug 1852741](https://bugs.launchpad.net/bugs/1852741)) and a new tool to persistently configure vfio-ap devices ([bug 1852736](https://bugs.launchpad.net/bugs/1852736)) landed.

* A multitude of enhancements in the area of cryptography, like the update of opencryptoki to version 3.18, with support for crypto profiles ([bug 1959549](https://bugs.launchpad.net/bugs/1959549)), additional crypto counters ([bug 1959551](https://bugs.launchpad.net/bugs/1959551)) and the PKCS #11 3.1 CKA_DERIVE_TEMPLATEs ([bug 1982842](https://bugs.launchpad.net/bugs/1982842)).
libica was updated to the latest bug fix version 4.0.3 ([bug 1986437](https://bugs.launchpad.net/bugs/1986437)), the openssl-ibmca package to 2.3.0, now with support for openSSL 3.0 provider ([bug 1959763](https://bugs.launchpad.net/bugs/1959763)), support for IBM specific mechanisms and attributes was added to p11-kit ([bug 1982841](https://bugs.launchpad.net/bugs/1982841)), BEAR enhancements for new IBM Z hardware ([bug 1960186](https://bugs.launchpad.net/bugs/1960186)) and (lib)nettle upgrade to latest upstream version, that now provides CPACF support ([bug 1959469](https://bugs.launchpad.net/bugs/1959469)).
In addition zcryptctl comes now with support for control domains (([bug 1982759](https://bugs.launchpad.net/bugs/1982759)) and ([bug 1982838](https://bugs.launchpad.net/bugs/1982838))) and a new tool is shipped that allows to display usage counters from the IBM z16 Processor Activity Instrumentation Facility ([bug 1982760](https://bugs.launchpad.net/bugs/1982760)).

* Eventually improvements in the area of RDMA/RoCE, with support for independent usage of secondary physical function (PF) of ConnectX-5/6 based RoCE adapters ([bug 1959542](https://bugs.launchpad.net/bugs/1959542)) was added and the enablement for MIO instructions, means usage of new PCI Load/Store instructions in rdma-core (([bug 1959543](https://bugs.launchpad.net/bugs/1959543)) and ([bug 1959544](https://bugs.launchpad.net/bugs/1959544))).

## Known Issues

As is to be expected, with any release, there are some significant known bugs that users may run into with this release of Ubuntu. The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:

### General

The option to install using zfs as a file system and encryption has been disabled due to a [bug](https://bugs.launchpad.net/ubuntu-manual-tests/+bug/1993318) with all of the file system not being mounted on first boot. If you'd like to have a system using zfs and encryption please install using Ubuntu 22.04.1 and then upgrade to Ubuntu 22.10.

The command-not-found indexes are out of date for some packages in the release pocket of the Ubuntu archive. This means that recommendations in the terminal with text like `Command 'kms-universal-planes' not found, but can be installed with:` may be incorrect. An example of this can be found in ([bug 1998001](https://bugs.launchpad.net/ubuntu/+source/command-not-found/+bug/1998001)). Unfortunately, this issue was found after the release of Kinetic and is not easily fixable.

### Linux kernel

The dkms package is not currently able to sign kernel modules which it builds. This will affect fresh installations of systems with a Broadcom  wireless device and that use secure boot. An update to dkms is currently in the works and [a workaround is available](https://discourse.ubuntu.com/t/dkms-package-support-extra-drivers-does-not-work-in-ubuntu-22-10-install-media/31655).

### Ubuntu Desktop

Nothing yet.

### Ubuntu Server

Nothing yet.

## Platforms

### Cloud Images

None
 
### Raspberry Pi

* While the official DSI display now produces output under the Full KMS graphics drivers, the touchscreen does not operate, and rotation of the screen is ignored. To enable rotation or touchscreen support, edit the `config.txt` file on your Raspberry Pi's boot partition and change the line `dtoverlay=vc4-kms-v3d` to `dtoverlay=vc4-fkms-v3d` to revert to the "Fake" KMS graphics stack ([bug 1970603](https://launchpad.net/bugs/1970603)).

* Various kernel modules have been moved from the `linux-modules-raspi` package in order to reduce the initramfs size. If you find an application failing due to missing kernel modules, please try `sudo apt install linux-modules-extra-raspi`

* The legacy camera stack (MMAL based) is no longer supported on arm64; [libcamera](https://www.raspberrypi.com/documentation/accessories/camera.html#libcamera-and-libcamera-apps) is the supported method of using the Pi Camera Module on the arm64 architecture (the boot-time configuration will automatically load overlays for official modules; unofficial camera modules need the relevant overlay added to `config.txt` on the boot partition)

* After initial user setup on the desktop image, several packages can still be autoremoved [bug 1925265](https://launchpad.net/bugs/1925265)); run `sudo apt autoremove --purge` to work around this

* Under the desktop image, while the new pipewire stack maintains the correct audio device across reboots on the Raspberry Pi ([bug 1877194](https://launchpad.net/bugs/1877194)), an invalid audio device is now selected by default on the Raspberry Pi 400 ([bug 1993316](https://launchpad.net/bugs/1993316)), and an inconvenient default is selected on the Raspberry Pi 4 ([bug 1993347](https://launchpad.net/bugs/1993347))

* With the removal of the `crda` package in 22.04, the method of setting the wifi regulatory domain (editing `/etc/default/crda`) no longer operates. Use the new `regulatory-domain` option in the netplan configuration ([bug 1951586](https://launchpad.net/bugs/1951586))

* Under the desktop image, the default totem video player will not open videos by default ([bug 1969512](https://launchpad.net/bugs/1969512)); `sudo apt install vlc` to install an alternate video player which operates correctly

### s390X

Nothing yet.



## Official flavours

The release notes for the official flavours can be found at the following links:

  * [Kubuntu Release Notes](https://kubuntu.org/news/kubuntu-22-10-kinetic-kudu-released/)
  * [Lubuntu Release Notes](https://lubuntu.me/kinetic-released/)
  * [Ubuntu Budgie Release Notes](https://ubuntubudgie.org/2022/09/ubuntu-budgie-22-10-release-notes/)
  * [Ubuntu MATE Release Notes](https://ubuntu-mate.org/blog/ubuntu-mate-kinetic-kudu-release-notes/)
  * [Ubuntu Studio Release Notes](https://ubuntustudio.org/ubuntu-studio-22-10-release-notes/)
  * [Ubuntu Unity Release Notes](https://ubuntuunity.org/blog/ubuntu-unity-22.10/)
  * [Xubuntu Release Notes](https://wiki.xubuntu.org/releases/22.10/release-notes)
