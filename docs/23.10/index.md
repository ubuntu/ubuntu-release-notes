---
tocdepth: 3
---

(ubuntu-23-10-release-notes)=
# Ubuntu 23.10 "Mantic Minotaur" Release Notes

<!-- Source: https://discourse.ubuntu.com/t/mantic-minotaur-release-notes/35534 -->

utkarsh | 2023-11-20 09:37:31 UTC | #1

# Mantic Minotaur Release Notes

# Table of Contents

- [Introduction](#heading--introduction)
- [New features in 23.10](#heading--new-features-in-23-10)
- [Known Issues](#heading--known-issues)
- [Official flavours](#heading--official-flavours)
- [More information](#heading--more-information)

<h1 id="heading--introduction">Introduction</h1>

These release notes for **Ubuntu 23.10** (Mantic Minotaur) provide an overview of the release and document the known issues with Ubuntu and its flavours.

## Support lifespan

Ubuntu 23.10 will be supported for 9 months until July 2024. If you need Long Term Support, we recommend you use [Ubuntu 22.04 LTS](https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes/) instead.

<h1 id="heading--new-features-in-23-10">New features in 23.10</h1>

## Updated Packages

* `add-apt-repository` now adds PPAs as deb822 `.sources` files (https://discourse.ubuntu.com/t/improvements-to-ppa-management-in-23-10/35783).

## Linux kernel 🐧

Ubuntu 23.10 includes the new 6.5 Linux kernel that brings many new features.

Notable upstream changes:

* Intel's "Topology Aware Register and PM Capsule Interface" (interface that provides better power-management features).
* arm64 permission-indirection extension (technology to set special memory permissions).
* RISC-V now supports ACPI.
* The Loongarch architecture now supports simultaneous multi-threading (SMT).
* Support for unaccepted memory (protocol by which secure guest systems accept memory allocated by the host - [Seeking an acceptable unaccepted memory policy](https://lwn.net/Articles/928328/).
* The io_uring subsystem can now store the rings and submission queue in user-space memory.
* Ability to mount a file system underneath an existing mount on the same mount point; useful in container scenarios ([Merge tag 'v6.5/vfs.mount' of git://git.kernel.org/pub/scm/linux/kernel/git/vfs/vfs](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=c0a572d9d32f)).
* New `cachestat()` system call (query the page-cache state of files and directories).
* Usual set of changes to support new hardware.

Notable Ubuntu-specific changes:

* zstd compressed modules ([LP: #2028568](https://bugs.launchpad.net/bugs/2028568)) to shorten boot time.
* New Apparmor/Stacking LSM patch set.
* Updated shiftfs patch set.
* Enabled multi-gen LRU page reclaiming by default ([LP: #2023629](https://bugs.launchpad.net/bugs/2023629)).
* `.config` tuning of the low-latency kernel for desktop-oriented tasks ([LP: #2028568](https://bugs.launchpad.net/bugs/2023007)).
* New zfs 2.2.0~rc3.
* Ceph support for idmapped mounts.

## systemd v253.5

The init system was updated to systemd v253.5. See the [upstream changelog](https://github.com/systemd/systemd/releases/tag/v253) for more information about individual features.

## Netplan v0.107
The network stack was updated to [Netplan v0.107](https://discourse.ubuntu.com/t/blog-netplan-developer-diaries/35932/6), introducing support for `dummy` and `veth` devices in addition to providing Python bindings to `libnetplan` in the **python3-netplan** package.

## Toolchain Upgrades 🛠️

* GCC was updated to the 13.2.0 release, binutils to 2.41, and glibc to 2.38.
* Python :snake: now defaults to version 3.11.6, and 3.12.0 is available in the archive.
* Perl :camel: at version 5.36.0.
* LLVM now defaults to version 16, and 17 is available in the archive.
* Rust :crab: toolchain defaults to version 1.71.

### OpenJDK

In addition to OpenJDK 17, OpenJDK 21 is now provided (but not used for package builds).

### .NET

.NET 7 packages were updated to 7.0.110, and .NET 6 packages were updated to 6.0.121

### golang

Go was updated to version 1.21. See the [upstream release notes](https://go.dev/doc/go1.21) for all the changes.

## Security Improvements 🔒

The Ubuntu kernel now has the ability to require programs to have an AppArmor profile in order to use unprivileged user namespaces ([unprivileged_userns_restriction](https://gitlab.com/apparmor/apparmor/-/wikis/unprivileged_userns_restriction)). This restriction is not currently enabled by default but when enabled affects all programs on the system that are unprivileged and unconfined. This affects programs that construct sandboxes ([LP: #2017980](https://bugs.launchpad.net/ubuntu/+source/linux-meta-nvidia-5.19/+bug/2017980)) or work with some styles of container workloads. This is the first step towards trying to mitigate the larger attack surface presented by unprivileged user namespaces.

To enable this new restriction:

  * Enable this restriction on the entire system for one boot by executing `echo 1 | sudo tee /proc/sys/kernel/apparmor_restrict_unprivileged_userns`. This setting is lost on reboot. 

  * Enable this restriction using a persistent setting by adding a new file (`/etc/sysctl.d/60-apparmor-namespace.conf`) with the following contents:
    ```
    kernel.apparmor_restrict_unprivileged_userns=1
    ```
    Reboot. 

There are several options if you run into problems:

  * Confine your applications with an AppArmor profile. Because this can be potentially onerous, a new `unconfined` profile mode/flag has been added to AppArmor. This designates the profile to essentially act like the unconfined mode for AppArmor where an application is not restricted, and it allows additional permissions to be added, such as the `userns,` permission. Such profile for, e.g. [Google Chrome](https://www.google.com/chrome/?platform=linux), would look like the following, and it would be located within the `/etc/apparmor.d/opt.google.chrome.chrome` file:
    ```
    abi <abi/4.0>,

    include <tunables/global>

    /opt/google/chrome/chrome flags=(unconfined) {
      userns,

      # Site-specific additions and overrides. See local/README for details.
      include if exists <local/opt.google.chrome.chrome>
    }
    ```
    Alternatively, a complete AppArmor profile for the application can be created (see the [AppArmor](https://ubuntu.com/server/docs/security-apparmor) documentation).

  * Launch your application in a way that doesn't use unprivileged user namespaces, e.g. `google-chrome-stable --no-sandbox`. This is not recommended. Use the `unconfined` profile mode described above instead.

  * Disable this restriction on the entire system for one boot by executing `echo 0 | sudo tee /proc/sys/kernel/apparmor_restrict_unprivileged_userns`. This setting is lost on reboot. This similar to the previous behaviour, but it does not mitigate against kernel exploits that abuse the unprivileged user-namespaces feature.

  * Disable this restriction using a persistent setting by adding a new file (`/etc/sysctl.d/60-apparmor-namespace.conf`) with the following contents:
    ```
    kernel.apparmor_restrict_unprivileged_userns=0
    ```
    Reboot. This is similar to the previous behaviour, but it does not mitigate against kernel exploits that abuse the unprivileged user-namespaces feature.

## Ubuntu Desktop

### Installer and Upgrades

* The default Ubuntu Desktop installation is now **minimal**. There is still an "Expanded installation" option for those who prefer to have applications like LibreOffice and Thunderbird installed for the first boot. (The "Full" option is still the default with the legacy Desktop installer.)

* We are reintroducing support for **ZFS guided installations**, enhancing the flexibility and choices available for your storage management needs. This is a new implementation in the Subiquity-based installers, and is without encryption by default. The encrypted ZFS guided option will be developed in a future release.

* Starting with Ubuntu 23.10, **TPM-backed full-disk encryption** (FDE) is introduced as an experimental feature, building on years of experience with Ubuntu Core. On supported platforms, you no longer need to enter passphrases at boot manually. Instead, the TPM securely manages the decryption key, providing enhanced security against physical attacks. This new feature streamlines the user experience and offers additional layers of security, especially in enterprise environments. However, the traditional passphrase-backed FDE is still available for those who prefer it. We invite users to experiment with this new feature, although caution is advised as it's still experimental. More details in the [TPM-backed Full Disk Encryption is coming to Ubuntu](https://ubuntu.com/blog/tpm-backed-full-disk-encryption-is-coming-to-ubuntu) blog post. Do not hesitate to [report bugs in Launchpad against the ubuntu-desktop-installer project](https://bugs.launchpad.net/ubuntu-desktop-installer/+filebug).

  Known limitations:

  * Requires TPM 2.0.
  * Only a limited set of hardware is supported.
  * No external kernel-modules support. For example, no support of NVIDIA graphics cards.

* The configuration file, `/etc/netplan/01-network-manager-all.yaml` (which specifies Network Manager as the Netplan renderer), has been moved to `/lib/netplan/00-network-manager-all.yaml` to reflect that it should not be edited. Also, it is now owned by the `ubuntu-settings` package. For upgraders, the move is be performed automatically and the old file removed if it was unchanged. If it was changed, the move still takes place, but a copy of the old file is left in `/etc/netplan/01-network-manager-all.yaml.dpkg-backup` ([LP: #2020110](https://bugs.launchpad.net/ubuntu/+source/ubuntu-settings/+bug/2020110)).

* **NetworkManager now uses Netplan** as its default settings-storage backend. On upgrade, all connection profiles from `/etc/NetworkManager/system-connections/` are transparently migrated to `/etc/netplan/90-NM-*.yaml` and become ephemeral, Netplan-rendered connection profiles in `/run/NetworkManager/system-connections/`. Backups of the original profiles are automatically created in `/var/lib/NetworkManager/backups/` (read more at [NetworkManager YAML settings backend](https://netplan.readthedocs.io/en/stable/netplan-everywhere) and [LP: #1985994](https://bugs.launchpad.net/netplan/+bug/1985994)).

* **ADSys Active Directory Certificates auto-enrollment:** Windows Server offers a solution for auto-enrolling certificates using Group Policies. This interacts with Certificate Enrollment Services by Microsoft and works seamlessly with Windows clients.

  ADSys introduces AD certificates auto-enrollment to streamline connecting to corporate Wi-Fi and VPN networks. Automated enrollment eliminates the need for manual interactions with the certificate authority, such as pre-creating certificates. This simplifies IT administration and minimises security risks associated with managing sensitive data.

* The installer is now able to update itself and will prompt the user to update in the very early stages of the installation if a newer version is available.

### New Store

* There is a brand new **Ubuntu App Center** that replaces the previous Snap Store. The application has been written from scratch using the Flutter toolkit.

* There is also a new standalone **Firmware Updater** application. This provides the possibility to update firmware without needing to have a full app store running continuously in the background.

### GNOME :footprints:

* GNOME has been updated to include new features and fixes from the latest GNOME release, [GNOME 45](https://release.gnome.org/45/).
* The **GNOME Clocks** application is installed by default.

### Updated Ubuntu font

* There is now a `fonts-ubuntu-classic` package. Install it if you prefer the style of the Ubuntu font before Ubuntu 23.04.

### Updated Applications

* [Firefox](https://mozilla.org/firefox/releases/) 118 :fire::fox_face:
  * Firefox is a native [Wayland application](https://discourse.ubuntu.com/t/firefox-snap-with-wayland-enabled-by-default-in-ubuntu-23-10-mantic-minotaur/38660) for this Ubuntu release.
* [LibreOffice 7.6](https://wiki.documentfoundation.org/ReleaseNotes/7.6) :books:
* [Thunderbird 115.2 "Supernova"](https://blog.thunderbird.net/2023/07/our-fastest-most-beautiful-release-ever-thunderbird-115-supernova-is-here/) :cloud_with_lightning::bird:

### Updated Subsystems

* [BlueZ 5.68](https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/ChangeLog?id=5.68)
* [Cairo 1.18](https://cairographics.org/news/cairo-1.18.0/)
* [NetworkManager 1.44](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/blob/nm-1-44/NEWS)
* [Pipewire 0.3.79](https://gitlab.freedesktop.org/pipewire/pipewire/-/blob/0.3.79/NEWS)
* [Poppler 23.08](https://gitlab.freedesktop.org/poppler/poppler/-/blob/poppler-23.08.0/NEWS)
* [xdg-desktop-portal 1.18](https://github.com/flatpak/xdg-desktop-portal/blob/1.18.0/NEWS)

## Ubuntu Server

### Apache2

apache2 has been upgraded from 2.4.55 to 2.4.57, which adds the `BCTLS` and `BNE` RewriteRule flags to `mod_rewrite` and fixes security issues and several bugs.

### Django

Django has been updated to the latest LTS release 4.2 from 3.2, which includes many new features and bug fixes. All Django middleware provided in Ubuntu has also been updated to be compatible with the new version. See the [4.0 release notes](https://docs.djangoproject.com/en/4.2/releases/4.0/) for features and updates added with the major version change and the [4.2 release notes](https://docs.djangoproject.com/en/4.2/releases/4.2/) for the changes made leading up to the LTS release.

### Dovecot

Dovecot received a micro-point update to 2.3.20 from 2.3.19, which contains mainly bugfixes. There is also a new `dsync_features=no-header-hashes` setting, which enables an optimization that assumes identical IMAP UIDs contain the same mail contents. This is useful on IMAP servers that don't cache the `Date/Message-ID` headers. There are also new Lua HTTP client settings and a new `doveadm replicator status` command.

### Monitoring Plugins

A micro-version release updates `monitoring-plugins` from 2.3.2 to 2.3.3. It provides one general new feature to use PRId64 and PRIu64 instead of `%ld` directly. See the [release notes](https://www.monitoring-plugins.org/news/release-2-3-3.html) for details on bugfixes and other enhancements.

### Nginx

Nginx is updated from version 1.22 to 1.24, which is predominantly comprised of bugfixes and a few minor features and refinements. See the [upstream changelog](https://nginx.org/en/CHANGES-1.24) for full details.

### Spamassassin

Spamassassin 4 introduced support for DMARC. However, this depends on Perl modules not yet available from the main Ubuntu repository, so it is not enabled by default. The dependencies all exist in the universe repository. To enable it, manually install `libmail-dmarc-perl` alongside your Spamassassin installation, and update your Spamassassin configuration accordingly (see [LP: #2023971](https://bugs.launchpad.net/ubuntu/+source/libmail-dmarc-perl/+bug/2023971)).

### Docker

The `docker.io` package has been updated to version 24.0.5, which includes changes that can be seen in the [upstream release notes](https://docs.docker.com/engine/release-notes/24.0/). There are also two new Docker CLI plugins available in the Ubuntu archive:

* `docker-buildx` version 0.11.2.
* `docker-compose-v2` version 2.20.2.

**NOTE**: The deprecated AUFS and legacy overlay storage drivers have been removed.

### Containerd

Containerd has been updated to version 1.7.2. See the [upstream release notes](https://github.com/containerd/containerd/releases/tag/v1.7.2) for all the changes.

### Runc

Runc has been updated to version 1.1.7. See the [upstream release notes](https://github.com/opencontainers/runc/blob/main/CHANGELOG.md#117---2023-04-26) for all the changes.

### Samba
The [samba ](https://www.samba.org/) package was updated to the 4.18.x series. Here are the upstream release notes: [https://www.samba.org/samba/history/samba-4.18.0.html ](https://www.samba.org/samba/history/samba-4.18.0.html)

Like was the case with the 4.17.x versions, this 4.18.x series further improves the performance of open/close operations and brings it back to the level of the 4.12 line, before a series of security fixes introduced this performance impact.

Please refer to the upstream release notes for more details on this and other changes.

### ISC Kea
The [ISC Kea DHCP server](https://kea.isc.org/) was updated to the [2.2.1 maintenance release](https://lists.isc.org/pipermail/kea-announce/2023-July/000100.html) which brings some bug fixes and other smaller improvements. Please see the [announcement](https://lists.isc.org/pipermail/kea-announce/2023-July/000100.html) for details.

The Ubuntu packaging is in sync with Debian and also got some translation updates and the AppArmor profile, introduced a few releases ago, received some tweaks.

### QEMU

The [QEMU](https://qemu.org) package was updated to the 8.0.x series, which brings many bug fixes and new features.

* Support for the Sapphire Rapids CPU model.
* System emulation on 32-bit x86 hosts has been deprecated. The QEMU project no longer considers 32-bit x86 host support for system emulation to be an effective use of its limited resources, and thus intends to discontinue. User mode emulation continues to be supported on 32-bit hosts.
* Support for `igb` device emulation.
* Many fixes and improvements to the RISC-V support.

For more details, please see [the upstream changelog](https://wiki.qemu.org/ChangeLog/8.0).

### libvirt

The [libvirt](https://www.libvirt.org) package was updated to version 9.6.0.  These are the noteworthy changes to this release.

* For QEMU:
  * Introduce support for `igb` network interface model.
  * Support compression for parallel migration
  * Add Sapphire Rapids CPU model
  * Support `removable` attribute for SCSI disk

For more details, please see [the upstream changelog](https://www.libvirt.org/news.html).

### OpenLDAP

The [OpenLDAP](https://openldap.org) package was updated to version 2.6.6, which brings several bug fixes.  For more details, please see [the upstream changelog](https://www.openldap.org/software/release/changes.html).

### sssd

The [sssd](https://sssd.io) package was updated to version 2.9.1, which brings several bug fixes and new features.

* `sss_simpleifp` library is deprecated and might be removed in further releases.
* "Files provider" (i.e. `id_provider = files`) is deprecated and might be removed in further releases. Consider using “Proxy provider” with `proxy_lib_name = files` instead.
* Add support for `ldapi://` URLs to allow connections to local LDAP servers.

For more details, please see [the upstream changelog](https://sssd.io/release-notes/sssd-2.9.1.html).

### Subiquity

A new version of the Subiquity server installer has been released.  Please read the full [release notes for 23.10.1](https://github.com/canonical/subiquity/releases/tag/23.10.1) on GitHub.

### OpenStack

Ubuntu 23.10 includes the latest OpenStack release, 2023.2 Bobcat, including the following components:

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

Please refer to the [OpenStack 2023.2 Bobcat release notes](https://releases.openstack.org/bobcat/) for full details of this release of OpenStack.

OpenStack 2023.2 Bobcat is also provided via the Ubuntu Cloud Archive for Ubuntu 22.04 LTS. The Ubuntu Cloud Archive for OpenStack 2023.2 Bobcat can be enabled on Ubuntu 22.04 by running the following command:

> sudo add-apt-repository cloud-archive:bobcat

WARNING: Upgrading an OpenStack deployment is a non-trivial process and care should be taken to plan and test upgrade procedures which will be specific to each OpenStack deployment.

Make sure you read the [OpenStack Charm Release Notes](https://docs.openstack.org/charm-guide/latest) for more information about how to deploy and operate Ubuntu OpenStack using Juju.

## Platforms

### Public Cloud
#### All
* separate /boot partition
  * Separate 1GB boot partition in all Ubuntu 23.10 cloud images
  * 6.5 kernel is now the default kernel in all Ubuntu 23.10 images
* All Minimal images use the new [Minimal Ubuntu cloud seed](https://ubuntu-archive-team.ubuntu.com/seeds/ubuntu.mantic/cloud-minimal). Read more about the qcow2 case below. 

#### AWS EC2
aws: the default volume type is now GP3 instead of GP2. See https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html for more details on the different volume types.

#### Minimal download/qcow2 cloud images

The Mantic Minotaur (Ubuntu 23.10) images available at https://cloud-images.ubuntu.com/minimal/ have undergone significant changes since the Lunar release in April 2023.

The main changes after 20230618 are:

* Move to the linux-generic kernel from the linux-kvm kernel.
  * Note this kernel change is *only* for the images on `cloud-images.ubuntu.com`. Partner clouds still use the cloud optimized kernels.
* Move to using minimal-cloud seed - see [Minimal Ubuntu cloud](https://ubuntu-archive-team.ubuntu.com/seeds/ubuntu.mantic/cloud-minimal).
* No longer installing the 'Recommends' packages.
  * This is during image build only and does not affect any subsequent package installations.
* No initramfs fallback for boot - only initramfsless boot.

This results in:
* Fewer packages
  * From package count 426 to 288 (diff: 138)
* Much smaller size
  * Taking download qcow2 images as an example the image size reduced from 337.19MiB to 226.75MiB (diff: 110.44MiB)

Mantic Minotaur (Ubuntu 23.10) is a devel release, so this is the perfect time to be making these changes.

##### How to report any issues resulting from these changes

If you notice any unexpected changes or bugs in the minimal images, create a new bug in [cloud-images](https://bugs.launchpad.net/cloud-images).

### Raspberry Pi 🍓

* Ubuntu 23.10 brings support for the new Raspberry Pi 5, incorporating upstream patches to the kernel, mesa, userland, EEPROM, and GPIO packages ([LP: #2037642](https://bugs.launchpad.net/ubuntu/+source/linux-raspi/+bug/2037642))

* The 32-bit (armhf) images do *not* support the Raspberry Pi 5 and will not boot on this platform. You may choose to run a 32-bit userland as a foreign architecture on the 64-bit (arm64) images (see the [Debian Multiarch page](https://wiki.debian.org/Multiarch/HOWTO) for further information), but the Raspberry Pi 5 does not support 32-bit kernels. Hence, the only Ubuntu images supported on the Pi 5 are the 64-bit images.

* The Raspberry Pi 5 changes the means by which the GPIO pins are accessed (they are no longer driven directly from the SoC, but from the RP1 "southbridge" chip). This in turn means that the traditional GPIO libraries ([RPi.GPIO](https://launchpad.net/ubuntu/+source/rpi.gpio) in particular) cannot work on the Pi 5. The GPIO Zero library was updated in prior releases to favor an alternate pin driver compatible with the Pi 5, but for those applications relying on the RPi.GPIO API, [rpi-lgpio](https://launchpad.net/ubuntu/+source/rpi-lgpio) has been updated to provide a compatibility shim. See the [rpi-lgpio documentation](https://rpi-lgpio.readthedocs.io/) for further information.

* Ubuntu 23.10 updates [libcamera](https://launchpad.net/ubuntu/+source/libcamera) to version 0.1 and includes support for all official Raspberry Pi camera modules, including the v3 camera with auto-focus. Additional patches are required for full compatibility with Raspberry Pi 5 ([LP: #2037642](https://bugs.launchpad.net/ubuntu/+source/linux-raspi/+bug/2037642)), which are planned to be delivered by SRU.

* Ubuntu 23.10 changes the default `cloud-init` configuration to disable password-based authentication with the SSH server. See the `ssh_pw_auth` setting in the `user-data` file on the boot partition if you still need password-based authentication.

* Ubuntu 23.10 disables the multipath daemon by default, saving approximately 24MB of memory at runtime (important on the smaller boards, including the Pi Zero 2W). Remove `multipath=off` from `cmdline.txt` on the boot partition if you still require the multipath daemon.

### RISC-V

#### StarFive VisionFive 2

* The Ubuntu Server live installer can be used to install to NVMe or USB with a current upstream U-Boot. See details on the [Ubuntu Wiki](https://wiki.ubuntu.com/RISC-V/StarFive%20VisionFive%202).
* StarFive VisionFive 2 v1.2A is not supported by the release kernel.

### IBM Z and LinuxONE ![image|32x32](upload://dZM0RRlelqCcZc6RhqJGMW8DMZr.png) 

* Significant update and changes in s390-tools, with the availability of a subset of tools for non-s390x platforms ([LP: #2025578](https://launchpad.net/bugs/2025578), [LP: #2025781](https://launchpad.net/bugs/2025781)), the Rust enablement (and needed vendored crates) ([LP: #2030316](https://launchpad.net/bugs/2030316)) and the inclusion of the 'pem' file in s390-tools-signed package ([LP: #2020469](https://launchpad.net/bugs/2020469)).

* Also updates in the cryptography stack, with openssl-ibmca v2.4.0 and patches on top ([LP: #2027809](https://launchpad.net/bugs/2027809)), libica upgrade to v4.2.2 ([LP: #2027803](https://launchpad.net/bugs/2027803)), openssl-ibmca v2.4.0+ with 'implicit rejection' ([LP: #2003671](https://launchpad.net/bugs/2003671)) and opencryptoki v3.21.0 ([LP: #2026732](https://launchpad.net/bugs/2026732)) with cca token: protected key support ([LP: #2025923](https://launchpad.net/bugs/2025923)), concurrent master key rotation for cca ([LP: #2025926](https://launchpad.net/bugs/2025926)) and ep11 ([LP: #2025917](https://launchpad.net/bugs/2025917)) token and pkcsslotd hardening ([LP: #2025922](https://launchpad.net/bugs/2025922)).
In addition changed in the area of pkey with support for EP11 API ordinal 6 for secure guests ([LP: #2029390](https://launchpad.net/bugs/2029390)) and the supporting the generation of keys of type PKEY_TYPE_EP11_AES ([LP: #2028937](https://launchpad.net/bugs/2028937)). 

* With KVM/SE environments IBK (item binding keys) secret injection is now supported - on a kernel level ([LP: #2003675](https://launchpad.net/bugs/2003675) and [LP: #2003634](https://launchpad.net/bugs/2003634)) and the s390-tools level ([LP: #2003676](https://launchpad.net/bugs/2003676) and [LP: #2003633](https://launchpad.net/bugs/2003633)), as well as support for AP Bindings in SE Header ([LP: #1983221](https://launchpad.net/bugs/1983221)).

* KVM enhancements in the area of KVM, by Providing Atomic Memop for Key-Checked Compare-and-swap ([LP: #2026213](https://launchpad.net/bugs/2026213)), enhanced CCW address translation architectural compliance ([LP: #2026211](https://launchpad.net/bugs/2026211)) and ECKD List Directed IPL (qemu virtio) ([LP: #2026209](https://launchpad.net/bugs/2026209)) and List-Directed dump from ECKD DASD ([LP: #2003397](https://launchpad.net/bugs/2003397)) and improved memory reclaiming for z15 Secure Execution guests ([LP: #2006743](https://launchpad.net/bugs/2006743) and [LP: #2006740](https://launchpad.net/bugs/2006740)).

* Further DASD auto-quiesce support landed in kernel ([LP: #1982370](https://launchpad.net/bugs/1982370)) and s390-tools ([LP: #2025576](https://launchpad.net/bugs/2025576)).

* Finally version bumps of the smc-tools ([LP: #2027825](https://launchpad.net/bugs/2027825)) and qclib ([LP: #2027670](https://launchpad.net/bugs/2027670)) to it's latest versions; libgmp now with s390x SIMD optimizations ([LP: #1926752](https://launchpad.net/bugs/1926752)) and support in gcc to preserve register arguments ([LP: #2025575](https://launchpad.net/bugs/2025575)).

<h1 id="heading--known-issues">Known Issues</h1>

As is to be expected with any release, there are some significant known bugs that users may encounter with this release of Ubuntu. The ones we know about at this point (and some of the workarounds) are documented here, so you don't need to spend time reporting these bugs again:

## General

* The Live Session of the new Ubuntu Desktop installer is not localized. It is still possible to perform a non-English installation using the new installer, but internet access at install time is required to download the language packs. Should this be an issue, use the legacy installer images. ([LP: #2013329](https://bugs.launchpad.net/ubuntu-release-notes/+bug/2013329))

* Systems where the `/boot` directory is located on the XFS file system may not boot correctly if they have many files in a single directory below `/boot`. This is being tracked in ([LP: #2039172](https://bugs.launchpad.net/debian/+source/grub2/+bug/2039172)).

* When upgrading to Mantic, it fails to install snap firmware-updater. The workaround is to install the snap after upgrade. ([LP: #2039268](https://bugs.launchpad.net/ubuntu/+source/ubuntu-release-upgrader/+bug/2039268)).

## Linux kernel

* Some newer servers with BMCs using an Aspeed GPU may appear to hang while booting the installer image when using an attached display or the virtual KVM ([LP: #2042850](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2042850)). The workaround is to add the `nomodeset` parameter to the kernel command-line. Follow these steps:

1. At the GRUB boot menu, press `e`
2. Add `nomodeset` to linux line, like the example below:
```
linux /casper/vmlinuz nomodeset ---
```
3. Press `Ctrl-x` to continue the boot process
4. After installation is complete, reboot, use `nomodeset` again, like the example below:
```
linux /boot/vmlinuz-6.5.0-10-generic nomodeset root=UUID=c5605a23-05ae-4d9d-b65f-e47ba48b7560 ro
```
5. Add `nomodeset` to the GRUB config file, `/etc/default/grub`, like the example below:
```
GRUB_CMDLINE_LINUX="nomodeset"
```
6. Finally, run `sudo update-grub` to make the change take effect.

## Ubuntu Desktop

* The Ubuntu Desktop images are labelled as 23.10.1 instead of 23.10 due to the installer translation incident as mentioned [here](https://discourse.ubuntu.com/t/announcement-ubuntu-desktop-23-10-release-image-translation-incident-now-resolved/39365). The contents of 23.10.1 are the same as any other image with the exception of shipping a newer ubuntu-desktop-installer.

* The _Try Ubuntu_ environment is not translated with the new Desktop Installer ([LP: #2013329](https://launchpad.net/bugs/2013329)).

* Screen-reader support is present with the new desktop installer, but is incomplete. We recommend that people who need screen-reader support to install Ubuntu continue to use the legacy installer ([#2343](https://github.com/canonical/ubuntu-desktop-installer/issues/2343)).

* Application icons don't use the correct High Contrast theme when High Contrast is enabled [(LP: #2013107](https://launchpad.net/bugs/2013107)).

* **Incompatibility between TPM-backed Full Disk Encryption and Absolute:** TPM-backed Full Disk Encryption (FDE) has been introduced to enhance data security. However, it's important to note that this feature is incompatible with Absolute (formerly Computrace) security software. If Absolute is enabled on your system, the machine will not boot post-installation when TPM-backed FDE is also enabled. Therefore, disabling Absolute from the BIOS is recommended to avoid booting issues.
* **Hardware-Specific Kernel Module Requirements for TPM-backed Full Disk Encryption:** TPM-backed Full Disk Encryption (FDE) requires a specific kernel snap which may not include certain kernel modules necessary for some hardware functionalities. A notable example is the `vmd` module required for NVMe RAID configurations. In scenarios where such specific kernel modules are indispensable, the hardware feature may need to be disabled in the BIOS (such as RAID) to ensure the continued availability of the affected hardware post-installation. If disabling in the BIOS is not an option, the related hardware will not be available post-installation with TPM-backed FDE enabled.
* [FDE specific bug reports](https://bugs.launchpad.net/bugs/+bugs?field.searchtext=&orderby=-importance&field.status%3Alist=NEW&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.tag=fde&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search).

* The installer re-launches itself with the version shipped on the ISO instead of the latest version after updating it through its refresh mechanism ([#2377](https://github.com/canonical/ubuntu-desktop-installer/issues/2377)). 

## Ubuntu Server

In some situations, it is acceptable to proceed with an offline installation when the mirror is inaccessible. In this scenario, it is advised to use:

```
apt:
  fallback: offline-install
```

### GRUB
GRUB 2.12 as included in mantic [regresses support for UEFI HTTP boot](https://bugs.launchpad.net/ubuntu/+source/grub2/+bug/2039081).  We anticipate this being corrected in a subsequent package update.  Since the netboot tarball provided in Ubuntu 23.10 does not include this functionality, users who need UEFI HTTP boot support are recommended to use the netboot tarball from Ubuntu 23.04 instead.

## Platforms

### Cloud Images

#### All

* A change in systemd [253.5-1ubuntu1](https://launchpad.net/ubuntu/+source/systemd/253.5-1ubuntu1) resulted in unexpected UDP listening port 5353

The work to no longer listen on this port is being tracked @ https://bugs.launchpad.net/cloud-images/+bug/2038894

#### Microsoft Azure
* On Azure arm64 instances, the systemd service systemd-modules-load.service sometimes fails to load on first boot due to a Timeout error. All the kernel modules appear to be correctly loaded and this issue doesn't seem to impact the OS. Users can manually reload this service by running systemctl restart systemd-modules-load.service in case they notice that something is wrong.
  * This is being actively investigated

#### ppcel64 images on cloud-images.ubuntu.com

* an issue in livecd-rootfs causes snaps to not be properly pre-seeded, causing slower boot times ([LP:2038957](https://bugs.launchpad.net/ubuntu/+source/livecd-rootfs/+bug/2038957))

### Raspberry Pi

* During the installation process on the desktop image, the slides shown during installation appear corrupted on the Pi 4 (but not the Pi 5). The issue is cosmetic and does not affect the installation itself ([LP: #2037015](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/2037015))

* With some monitors connected to a Raspberry Pi, it is possible that a monitor powers off after a period of inactivity but then powers back on and shows a black screen. Investigation into the types of monitors affected is ongoing in [LP: #1998716](https://bugs.launchpad.net/ubuntu/+source/mutter/+bug/1998716).

* Various kernel modules have been moved from the `linux-modules-raspi` package to reduce the initramfs size. If you find an application failing due to missing kernel modules, try `sudo apt install linux-modules-extra-raspi`.

* The legacy camera stack (MMAL based) is not supported on arm64; [libcamera](https://www.raspberrypi.com/documentation/accessories/camera.html#libcamera-and-libcamera-apps) is the supported method of using the Pi Camera Modules on the arm64 architecture (the boot-time configuration automatically loads overlays for official modules; unofficial camera modules need the relevant overlay added to the `config.txt` file on the boot partition). Additional patches required for Raspberry Pi 5 compatibility are planned for SRU after release ([LP: #2037642](https://bugs.launchpad.net/ubuntu/+source/linux-raspi/+bug/2037642)).

* With the removal of the `crda` package in 22.04, the method of setting the wifi regulatory domain (editing `/etc/default/crda`) no longer operates. On server images, use the `regulatory-domain` option in the Netplan configuration. On desktop images, append `cfg80211.ieee80211_regdom=GB` (substituting `GB` for the relevant country code) to the kernel command line in the `cmdline.txt` file on the boot partition  ([LP: #1951586](https://launchpad.net/bugs/1951586)).

* With the mantic release kernel, GPIO and PWM controlled fans spin full speed all the time due to a broken patch in the step-wise governor (which is the default fan-speed governor). A patched kernel is available in [ppa:waveform/fan-fix](https://launchpad.net/~waveform/+archive/ubuntu/fan-fix) and the fix should land in the next release of the mantic kernel ([LP: #2041741](https://bugs.launchpad.net/ubuntu/+source/linux-raspi/+bug/2041741)).

### RISC-V

* Wifi for the StarFive VisionFive board does not work in this image ([LP: #2037065](https://launchpad.net/bugs/2037065)).

* The unmatched image does not boot on Unmatched systems due to a missing bootloader. It is still provided as part of the beta for use under QEMU ([LP: #2037060](https://launchpad.net/bugs/2037060)).

### s390X

Nothing yet.

<h1 id="heading--official-flavours">Official flavours</h1>

Find the release notes for the official flavours at the following links:

* [Edubuntu Release Notes](https://discourse.ubuntu.com/t/edubuntu-23-10-released/39263)
* [Kubuntu Release Notes](https://wiki.ubuntu.com/ManticMinotaur/ReleaseNotes/Kubuntu)
* [Lubuntu Release Notes](https://lubuntu.me/mantic-released/)
* [Ubuntu Budgie Release Notes](https://ubuntubudgie.org/2023/09/ubuntu-budgie-23-10-release-notes/)
* [Ubuntu MATE Release Notes](https://ubuntu-mate.org/blog/ubuntu-mate-mantic-minotaur-release-notes/)
* [Ubuntu Studio Release Notes](https://ubuntustudio.org/ubuntu-studio-23-10-release-notes/)
* [Ubuntu Unity Release Notes](https://ubuntuunity.org/blog/ubuntu-unity-23.10/)
* [Xubuntu Release Notes](https://wiki.xubuntu.org/releases/23.10/release-notes)
* [Ubuntu Kylin Release Notes](https://www.ubuntukylin.com/news/ubuntukylin2310-en.html)
* [Ubuntu Cinnamon Release Notes](https://ubuntucinnamon.org/?p=1247/)

<h1 id="heading--more-information">More information</h1>

## Reporting bugs

Your comments, bug reports, patches and suggestions help fix bugs and improve the quality of future releases. Please [report bugs using the tools provided](http://help.ubuntu.com/community/ReportingBugs). If you want to help with bugs, the [Bug Squad](http://wiki.ubuntu.com/BugSquad) is always looking for help.

## What happens if there is a high or critical priority CVE during release day?

Server, Desktop and Cloud plan to release in lockstep on release day, but there are some exceptions.

In the unlikely event that a critical or high-priority CVE is announced on release day, the release team have agreed on the following plan of action:

* For critical priority CVEs, the release of Server, Desktop and Cloud will be blocked until new images can be built addressing the CVE.

* For high-priority CVEs, the decision to block release will be made on a per-product (Server, Desktop and Cloud) basis and will depend on the nature of the CVE, which might result in images not being released on the same day.

This was discussed in the [ubuntu--release mailing list March/April 2023](https://lists.ubuntu.com/archives/ubuntu-release/2023-April/005610.html).

The mailing list thread also confirmed there is no technical or policy reason why a package cannot be pushed to the Updates or Security pocket to address high or critical-priority CVEs prior to the release.

## Participate in Ubuntu

If you would like to help shape Ubuntu, look at the list of ways you can participate at [community.ubuntu.com/contribute](https://community.ubuntu.com/contribute).

## More about Ubuntu

You can find out more about Ubuntu on the [Ubuntu website](https://ubuntu.com).

To sign up for future Ubuntu development announcements, subscribe to Ubuntu's development announcement list at [ubuntu-devel-announce](https://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce).

-------------------------

bdmurray | 2023-05-03 14:39:10 UTC | #2



-------------------------

