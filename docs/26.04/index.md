---
tocdepth: 3
---

(ubuntu-26.04-lts-release-notes)=
# Ubuntu 26.04 LTS release notes

:::{rubric} 23 April 2026
:::

These release notes cover new features and changes in Ubuntu 26.04 LTS (Resolute Raccoon).

:::{toctree}
:hidden:
:maxdepth: 2

Changes since 25.10 <changes-since-previous-interim>
Release schedule <schedule>
:::

## Support lifespan

Ubuntu 26.04 LTS is designated as a long-term support release. This means it will continue to receive security updates and critical bug fixes for five years. Ubuntu 26.04 LTS will be supported until April 2031.

With an Ubuntu Pro subscription, access to ESM (Expanded Security Maintenance) updates will be available for ten years. 

See our {ref}`release-policy-and-schedule`.

## Requirements and compatibility

Ubuntu 26.04 LTS requires a 2 GHz dual-core processor or better, a minimum of 6GB RAM and 25 GB of free hard drive space.

You need either a USB port or a DVD drive for the installer media. An internet connection enables you to access more software and updates but you can install Ubuntu without it.

## Changes for interim users

If you're upgrading **from Ubuntu 25.10 (Questing Quokka)**, refer to {ref}`ubuntu-26.04-lts-changes-since-25.10`.

## Summary for LTS users

If you’re upgrading **from Ubuntu 24.04 LTS (Noble Numbat)**, you receive the changes that happened in all the interim releases between Ubuntu 24.04 LTS and 26.04 LTS, as well as the most recent changes since Ubuntu 25.10.

For details, see the complete interim release notes: {ref}`24.10 <ubuntu-24.10-release-notes>`, {ref}`25.04 <ubuntu-25.04-release-notes>` and {ref}`25.10 <ubuntu-25.10-release-notes>`. Finally, review the latest {ref}`ubuntu-26.04-lts-changes-since-25.10`.

The following is an overview of the major changes.

### Desktop

#### Updated applications

* Firefox 🔥🦊 has been updated [to version 149](https://www.firefox.com/en-US/firefox/148.0/releasenotes/) / [150](https://www.firefox.com/en-US/firefox/148.0/releasenotes/).
* LibreOffice 📚 has been updated from version 24.2 [to 25.8](https://wiki.documentfoundation.org/ReleaseNotes/25.8).
* Thunderbird 🌩️🐦 has been updated [to version 128 "Supernova"](https://blog.thunderbird.net/2023/07/our-fastest-most-beautiful-release-ever-thunderbird-XY-supernova-is-here/).
* GNU Image Manipulation Program 🖼️ has received a major update from version 2.10 [to 3.0](https://www.gimp.org/news/2025/03/16/gimp-3-0-released/).

#### GNOME 50

The GNOME desktop environment has been updated from version 46 to 50. Major highlights:

* You can now set an application to start automatically after login in {menuselection}`Settings --> Apps`.
* Fractional scaling factors are now optimized so as to minimize blur.
* The default monospace font size has been reduced to match the default user interface font size. The monospace font is used in terminals and similar applications.
* The [Sysprof](https://apps.gnome.org/Sysprof/) app is installed by default as a new system utility. This makes it easier to discover performance issues in your apps.

    :::{versionadded} 24.10
    :::

For details, see the upstream release notes: [GNOME 47](https://release.gnome.org/47/), [GNOME 48](https://release.gnome.org/48/), [GNOME 49](https://release.gnome.org/49/) and [GNOME 50](https://release.gnome.org/50/).

#### New document viewer
:::{versionchanged} 25.04
:::

The Document Viewer app for viewing PDFs is now provided by Papers instead of Evince. Papers started with the Evince codebase but it has been updated to use GTK4 and partially rewritten in Rust.

#### New image viewer
:::{versionchanged} 25.10
:::

The Image Viewer app is now provided by [Loupe](https://apps.gnome.org/Loupe/) instead of Eye of GNOME (EOG). Loupe is written in Rust and powered by the [Glycin](https://gitlab.gnome.org/GNOME/glycin) library.

#### New terminal emulator
:::{versionchanged} 25.10
:::

The Terminal app is now provided by [Ptyxis](https://gitlab.gnome.org/chergert/ptyxis/-/blob/main/README.md?ref_type=heads) instead of GNOME Terminal.

#### Wayland session
:::{versionchanged} 25.10
:::

The Ubuntu Desktop session now runs only on the Wayland back end. The [Ubuntu on X\.org session is no longer available](https://discourse.ubuntu.com/t/ubuntu-25-10-drops-support-for-gnome-on-xorg/62538) because GNOME Shell can no longer run as an X\.org session.

Machines using Nvidia graphics now also fully support Wayland.

#### App Center enhancements
:::{versionadded} 24.10
:::

The App Center now includes improvements, including:

* Installs in progress
* Improved self-update handling
* Messaging for running snaps
* Direct uninstall of snaps from the manage page
* Scrolling support for touch screens
* Third party Deb installation

#### Security Center
:::{versionadded} 24.10
:::

A new Security Center is included. It features the ability to easily enable or disable a new experimental [permissions prompting](https://discourse.ubuntu.com/t/ubuntu-desktop-s-24-10-dev-cycle-part-5-introducing-permissions-prompting/47963/1) feature for Home directory permissions.

#### Permission prompting
:::{versionadded} 24.10
:::

Prompting is also supported by an additional seeded snap, `prompting-client`, for permissions prompt handling.

#### Better power optimization
:::{versionadded} 24.10
:::

Power Profiles Manager [has been improved and optimized](https://gitlab.freedesktop.org/upower/power-profiles-daemon/-/releases/#0.23) to support better newer hardware features (especially AMD), can now support multiple optimization drivers and is now battery-aware to automatically increase the optimization levels when running on battery only.

#### Performance improvements in Windows games
:::{versionadded} 25.04
:::

A new NTSYNC driver that emulates WinNT sync primitives is available, delivering better performance potential for Windows games running on Wine and Proton (Steam Play).

#### New ARM64 Desktop image
:::{versionadded} 25.04
:::

There is now an official generic ARM64 Desktop ISO targeting VMs, ACPI + EFI platforms and Snapdragon based WoA devices.

Initial hardware enablement work for the Snapdragon X Elite platform is included in the Desktop ISO.

#### Dual boot enhancements
:::{versionadded} 25.04
:::

Improved dual boot user experience, with a focus on BitLocker protected Windows systems:

* Added the option to install Ubuntu alongside existing BitLocker partitions if enough unallocated  space (or a sufficiently large and resizable partition) is available
* Made encrypted installations and other 'advanced options' available for dual boot scenarios

#### JPEG XL support
:::{versionadded} 25.04
:::

The JPEG XL format is now supported without needing to install any additional packages

#### Accelerated video encoding and decoding
:::{versionadded} 25.10
:::

When you enable *Install third-party software for graphics and Wi-Fi hardware and additional media formats* during installation, video encoding and decoding will be hardware-accelerated for supported hardware using the Video Acceleration API (VA-API).

Notably, you can record your screen at the original screen rate. Without VA-API, your screen recording has a reduced frame rate because it's limited by the CPU.

You can also install the library after installation. See [Record the screen](https://documentation.ubuntu.com/desktop/en/latest/how-to/record-the-screen/) in the Ubuntu Desktop documentation.

#### New update notifications
:::{versionadded} 25.10
:::

When system updates are available, the Software Updater window no longer pops up unprompted, stealing the keyboard focus. Instead, a notification shows up with options to open the Software Updater or to install all updates directly.

An icon in the system tray reminds you that updates are available even after dismissing the notification. It also provides a quick way to apply all the updates or inspect them in the Software Updater.

#### Installer accessibility
:::{versionadded} 25.10
:::

The Ubuntu installer has received plenty of accessibility fixes for screen reader users.

#### Ubuntu Insights
:::{versionadded} 25.10
:::

[Ubuntu Insights](https://github.com/ubuntu/ubuntu-insights) is being developed as a replacement for [Ubuntu Report](https://github.com/ubuntu/ubuntu-report) and gives you more control over the non-personally identifying system metrics that you choose to share with Canonical. The metrics collection is opt-in.

:::{note}
Any consent that you previously granted to Ubuntu Report will not be carried over to Ubuntu Insights.
:::


### Server

Ubuntu Server users often come from using the former LTS -- in this case 24.04 Noble Numbat. We want to remind you to check out the release notes for the interim releases as well, because all the great things that happened in the meantime do apply for you as well.

- {ref}`ubuntu-24.10-release-notes`
- {ref}`ubuntu-25.04-release-notes`
- {ref}`ubuntu-25.10-release-notes`

#### OpenSSH

* Deprecation warning for SHA1 SSHFP DNS records
* Add a warning when the connection negotiates a non-post quantum key agreement algorithm.
* Removes support for the weak DSA signature algorithm.
* New `PerSourcePenalties` option that will penalise client addresses that for some reason do not complete authentication. New in version 9.8.
* Support for a new hybrid post-quantum key exchange algorithm, called “mlkem768x25519-sha256”. Described in https://datatracker.ietf.org/doc/html/draft-kampanakis-curdle-ssh-pq-ke-03, it’s available by default. New in version 9.8.
* New match option invalid-user, which can be used when the target username is not valid
* New `sshd.service` alias to `ssh.service`. Both names can now be used in `systemctl` commands.
* New binary packages called `openssh-client-gssapi` and `openssh-server-gssapi`. This is in preparation for a future split of the GSSAPI authentication mechanism into separate packages in the near future. For now, they just pull in their non-gssapi counterparts, if installed. See https://lists.debian.org/debian-devel/2024/04/msg00044.html for the detailed plan.
* Host DSA keys are no longer generated.
* Starting with 1:9.6p1-3ubuntu17, openssh server no longer reads `~/.pam_environment` of the target system upon login. See [LP: #2059859](https://bugs.launchpad.net/ubuntu/+source/openssh/+bug/2059859/) for details.

For full upstream release notes for all releases, please consult https://www.openssh.org/releasenotes.html

#### Dovecot

Updated to 2.4.2. Version 2.4 introduced many changes to the Dovecot configuration format!

Coming from Ubuntu 24.04, please follow [dovecot’s 2.3 upgrade documentation](https://doc.dovecot.org/2.4.2/installation/upgrade/2.3-to-2.4.html).

When you’re coming from other versions, follow [the upgrade overview](https://doc.dovecot.org/2.4.2/installation/upgrade/overview.html).

#### Postfix

Specific release notes for major version releases since Ubuntu 24.04 LTS (Noble Numbat) are:

* 3.9.0: https://www.postfix.org/announcements/postfix-3.9.0.html
* 3.10.0: https://www.postfix.org/announcements/postfix-3.10.0.html

A noteworthy change in the packaging of Postfix is that **by default it is no longer installed in a chroot, and only limited chroot support is available from now on**.

#### Samba

Samba has been updated to the new upstream 4.23 version. Changes since Ubuntu Noble 24.04:

* SMB3 Unix Extensions enabled by default
* NetBios is disabled by default in the configuration file /etc/samba/smb.conf for fresh installs
* SMB3 Directory Leases
* Netlogon Ping over LDAP and LDAPS
* Experimental Himmelblaud Authentication in Samba
* AD DC schema upgrade and provision performance improvements
* LDAP TLS/SASL channel binding support
* Group Managed Service Accounts
* Samba can now claim Functional Level 2012R2 support
* Some Samba public libraries made private by default
* Samba AD will rotate expired passwords on smartcard-required accounts
* Automatic keytab update after machine password change

Removed features:

* `nmbd proxy logon`
* `cldap port`
* `fruit:posix_rename`

Packaging changes when upgrading from Ubuntu Noble 24.04:

* samba-vfs-modules: the VFS modules from this package were moved to the samba package, with the exception of the Ceph module, which got its own package: samba-vfs-ceph. The samba-vfs-modules package is now just a transitional package, and it can be safely removed after the release upgrade.
* samba-vfs-modules-extra: this package used to contain the GlusterFS VFS module. This module was moved to a new package called samba-vfs-glusterfs, and samba-vfs-modules-extra became a transitional package. It can also be safely removed after the release upgrade.
* The dumpmscat binary is no longer built

Samba upstream release notes since Ubuntu 24.04 LTS (Noble Numbat):

- [https://www.samba.org/samba/history/samba-4.20.0.html](https://www.samba.org/samba/history/samba-4.20.0.html)
- [https://www.samba.org/samba/history/samba-4.21.0.html](https://www.samba.org/samba/history/samba-4.21.0.html)
- [https://www.samba.org/samba/history/samba-4.22.0.html](https://www.samba.org/samba/history/samba-4.22.0.html)
- [https://www.samba.org/samba/history/samba-4.23.0.html](https://www.samba.org/samba/history/samba-4.23.0.html)

##### Samba on i386

Samba version 4.21.x added a dependency to the python3-samba package: python3-cryptography. Unfortunately, python3-cryptography was last built for i386 for Ubuntu Bionic 18.04, and is no longer available for that architecture, making this new dependency unsatisfiable.

For Ubuntu Plucky 25.04 and later, the python3-samba package is no longer built for i386. Please see [LP: #2099895](https://bugs.launchpad.net/ubuntu/+source/samba/+bug/2099895) for details. The main consequence is that the samba-tool script (part of that package) is no longer available for i386.

##### Upgrading an AD/DC from previous Ubuntu releases

If you have deployed a Samba Active Directory Domain Controller *without* having installed the `samba-ad-dc` package, you should install it before doing a release upgrade to Ubuntu 26.04 LTS (Resolute Raccoon). If `samba-ad-dc` is not installed prior to the release upgrade, the Active Directory Domain Controller functionality will not work on the upgraded system due to many missing components.

See [LP: #2101838](https://bugs.launchpad.net/ubuntu/+source/samba/+bug/2101838) for more information

#### Squid

Squid was updated to upstream version 7.2. Coming from version 6, the main new options are:

* Add tls_key_log directive to log TLS master keys.

* Add key-extras format to external ACL helpers to pass transaction details.

* Add doh_query directive to send DNS queries over HTTPS.

* Add cache_peer option tls-client-cert-switch to select client certificates dynamically.

Several bugfixes for crash scenarios are also included in this major release.

Some directives and options were removed/deprecated:

* Removed client_delay_access directive.

* Removed ftp_epsv directive.

* Removed cache_peer option no-netdb-exchange.

* Removed client_persistent_connections and server_persistent_connections directives.

For a list of all changes and fixes, please check the [upstream releases page](https://github.com/squid-cache/squid/releases).

#### SSSD

SSSD now runs under user `sssd` (instead of `root`). Make sure that `sssd` can still access secrets or integrations from its new user.

The implicit files provider and domain was removed: see <https://sssd.io/docs/files-provider-deprecation.html>.

Other changes of importance are listed upstream:

* https://sssd.io/release-notes/sssd-2.11.0.html
* https://sssd.io/release-notes/sssd-2.12.0.html

### Development

* GCC 🐄 has been updated from version 14 to 15.2, `binutils` from 2.42 to 2.45, and `glibc` from 2.39 to 2.42.
* Python 🐍 has been updated from version 3.12 to 3.13.9, while 3.14 is also available.
* LLVM 🐉 has been updated from version 18 to 21.
* Rust 🦀 toolchain has been updated from version 1.75 to 1.88.
* Golang 🐀 has been updated from version 1.22 to 1.25.
* Zig ⚡ is now available in Ubuntu. It defaults to version 0.14.1.
* Ubuntu Toolchains has a new [homepage](https://ubuntu.com/toolchains).

#### OpenJDK 21 and TCK certification
:::{versionadded} 24.10
:::

OpenJDK defaults to 21 (LTS), while version 25 (LTS) and an early access snapshot of version 26 are now available.

OpenJDK 21 and OpenJDK 17 packages are now TCK (Technology Compatibility Kit) certified on AMD64, ARM64, s390x, ppc64el and armhf. The Java TCK is the most comprehensive test suite that covers all aspects of Java SE specification including language features, libraries and APIs. This guarantees interoperability and conformance to standard.

#### Spring® snaps
:::{versionadded} 25.04
:::

We are excited to announce the [devpack-for-spring](https://snapcraft.io/devpack-for-spring) snap and a set of Spring® [content snaps](https://snapcraft.io/devpack-for-spring-manifest) that will serve as development tools for Spring® projects.

Developers can now quickly build Ubuntu ROCK images for their Java applications using the [Gradle and Maven plugins for Rockcraft](https://github.com/rockcrafters/java-rockcraft-plugins).

#### GraalVM snap
:::{versionadded} 25.04
:::

GraalVM Community Edition for JDK versions 21, 24 and 25 is now available as a [snap](https://snapcraft.io/graalvm-jdk). Java developers now have a choice to build and deploy their applications with standard OpenJDK, with OpenJDK-CRaC or as a GraalVM native image.


#### .NET 10

.NET has been updated from version 8 to 10.

We have also expanded .NET support to the IBM Power platform, further broadening the platform’s reach.

#### .NET snap
:::{versionadded} 24.10
:::

We are excited to introduce the new and improved [.NET Snap](https://snapcraft.io/dotnet), allowing developers to seamlessly install any supported version of .NET on any Ubuntu system.

#### PowerShell snap on more architectures
:::{versionadded} 25.10
:::

Support for the PowerShell snap has been expanded to include the `arm64`, `s390x`, and `ppc64el` architectures, broadening its availability across platforms.


### Enterprise

#### Updated `authd`

[authd](https://github.com/ubuntu/authd), Ubuntu's cloud authentication solution, has been updated:

- Many fixes and improvements to the EntraID provider
- New Google provider
- Supports device registration with EntraID
- authctl is a new command line tool to manage authd
- Many improvements and important bug fixes such as UID/GID handling 

#### New `authd` documentation

New [authd documentation](https://documentation.ubuntu.com/authd/en/stable/) has been published.

#### Updated ADSys

The Active Directory Group Policy client for Ubuntu supports the latest Polkit and comes with improvements and bug fixes to certificates enrollment.


### Cloud


### Security

#### New AppArmor sandboxing profiles
:::{versionadded} 25.04
:::

As part of a profile writing effort to improve overall system security, the AppArmor package now includes many new profiles for applications. This improved sandboxing can help mitigate the impact of any exploit in the confined applications.

:::{dropdown} Report bugs
These profiles may cause breakage for unanticipated uses of those applications, and we encourage users to file a bug on [Launchpad](https://bugs.launchpad.net/ubuntu/+source/apparmor/+filebug) for AppArmor-induced breakage in common use cases. When AppArmor denies an action, it usually generates a log entry describing the denial, which will help us investigate the bug, but which can also be used to add additional rules for customization or to work around the denials. AppArmor log entries can be read in the auditd logs, if auditd is installed, or in the syslog otherwise. [This page](https://gitlab.com/apparmor/apparmor/-/wikis/denial_quick_guide) describes how the information contained in the denial log can be used to update a local override.
:::

#### TPM-backed full-disk encryption
:::{versionadded} 25.10
:::

New [TPM-backed disk encryption](https://canonical-ubuntu-desktop-documentation.readthedocs-hosted.com/en/latest/explanation/hardware-backed-disk-encryption/) is available for Ubuntu Desktop. Its features include:

* Passphrase support and management
* Regeneration of the recovery key 
* Better integration with firmware updates

For details, see [Hardware-backed disk encryption](https://documentation.ubuntu.com/desktop/en/latest/explanation/hardware-backed-disk-encryption/) in the Ubuntu Desktop documentation.

### Hardware support

#### NVIDIA Dynamic Boost
:::{versionadded} 25.04
:::

This release enabled NVIDIA Dynamic Boost by default on supported laptops with NVIDIA GPUs.

NVIDIA Dynamic Boost is a feature of the NVIDIA drivers that dynamically shifts power between CPU and GPU depending on the workload on the system. While gaming, this allows extracting more performance by granting more power to the GPU.

Dynamic Boost will be active only when the laptop is powered by AC and there is enough load on the GPU. It will not be engaged when the system is running on battery.

For more details refer to [NVIDIA's documentation](https://download.nvidia.com/XFree86/Linux-x86_64/570.133.07/README/dynamicboost.html).

#### Support for new Intel® integrated and discrete GPUS
:::{versionadded} 25.04
:::

This release brings full support for Intel® Core™ Ultra Xe2 integrated Intel® Arc™ graphics, and Intel® Arc™ B580 and B570 “Battlemage” discrete GPUs. 
Moreover, the following features are also included:

* Improved GPU and CPU ray tracing rendering performance in applications with Intel Embree support, such as Blender (v4.2+). Ray tracing hardware acceleration on the GPU improves frame rendering by 20-30%, due to a 2-4x speed-up for the ray tracing component. 
* Full hardware accelerated video encoding of AVC, JPEG, HEVC, and AV1 on “Battlemage” devices.
* Introduction of the new CCS optimization in Intel® Compute Runtime.
* Enable debugging support for Intel Xe GPUs. 
* oneAPI Level Zero Ray Tracing improves AI/ML workload speeds via Embree on SYCL
 
#### Suspend with Nvidia
:::{versionadded} 25.10
:::
 
Suspend-resume support is now enabled in the proprietary Nvidia driver so as to prevent corruption and freezes when waking an Nvidia desktop.

#### ARM desktop platforms
:::{versionadded} 25.10
:::

The `linux-generic` kernel for ARM64 provides broader compatibility for ARM64 desktop platforms that utilize UEFI for booting ([LP#2121352](https://bugs.launchpad.net/ubuntu/+source/linux-signed/+bug/2121352)).


#### New RISC requirements
:::{versionchanged} 25.10
:::

The Ubuntu RISC-V kernel (`linux-riscv`) only supports hardware that implements the RVA23S64 ISA profile. You can't run Ubuntu 26.04 LTS on systems that don't satisfy this requirement. The RISC-V kernel in Ubuntu 24.04 LTS continues to support boards with RVA20 processor cores.


### Common changes

#### `sudo-rs`
:::{versionadded} 25.10
:::

The `sudo-rs` tool is now the default `sudo` provider.

The `sudo` tool (the original `sudo` maintained by Todd C. Miller) has been renamed to `sudo.ws`. Additionally, the `sudo-ldap` package has been removed: please switch to using LDAP authentication via PAM.
    
See [Ubuntu Server Docs](https://documentation.ubuntu.com/server/how-to/security/user-management/#sudo-rs) for configuring your default `sudo` provider and for the differences between `sudo-rs` and `sudo.ws`.
    

#### `rust-coreutils`
:::{versionadded} 25.10
:::

The core utilities of the operating system are now provided by the [`rust-coreutils`](https://launchpad.net/ubuntu/+source/rust-coreutils) package. Among other things, this brings significant performance improvements, such as in the `base64` tool.

Since `rust-coreutils` are not necessarily fully compatible yet, we continue to provide the classic GNU utilities as well. You can switch back and forth between them.
    

#### Linux kernel 7.0

The Linux kernel has been updated from version 6.8 to 7.0.

* Crash dumps are now [enabled by default](https://documentation.ubuntu.com/server/how-to/software/kernel-crash-dump/#kdump-enabled-by-default) for desktop and server installations.

    :::{versionadded} 24.10
    :::

* Kernel developers can now make use of a [new scheduling system](https://canonical.com/blog/crafting-new-linux-schedulers-with-sched-ext-rust-and-ubuntu), `sched_ext`, which provides a mechanism to implement scheduling policies as eBPF programs. This enables developers to defer scheduling decisions to standard user-space programs and implement fully functional hot-swappable Linux schedulers, using any language, tool, library, or resource accessible in user-space.

    :::{versionadded} 25.04
    :::

* After the generic kernel gained the ability to [tune responsiveness at boot time](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2051342), the `linux-lowlatency` binary package has been retired in favor of a combination of `linux-generic` and a new user-space `lowlatency-kernel` package, responsible of tuning the GRUB command line.

    :::{versionadded} 25.04
    :::

#### `systemd` 259

The `systemd` service manager has been updated from version 255 to 259.

* Support for System V service scripts has been removed. Use native `systemd` unit files instead of legacy System V scripts.

    :::{versionremoved} 26.04
    :::

* Support for `cgroup` version 1 ('legacy' and 'hybrid' hierarchies) has been removed.

    :::{versionremoved} 26.04
    :::

* Ubuntu now comes with the upstream `tmp.mount` unit by default. As a result, the `/tmp` directory is now a `tmpfs` file system by default.

    :::{versionchanged} 24.10
    :::

#### Netplan 1.2

The Netplan network manager has been updated from version 1.0 to 1.2.

* Netplan introduces a custom `systemd-networkd-wait-online` logic, waiting for link-local addresses and one routable interface, as described in the [specification](https://discourse.ubuntu.com/t/spec-definition-of-an-online-system/27838).

    :::{versionadded} 24.10
    :::

* Besides improvements to the `embedded-switch-mode` setting for SR-IOV devices, Netplan introduces a parser flag to skip broken configurations and fixes for ProtonVPN and Microsoft Azure Linux.

    :::{versionadded} 24.10
    :::

* Adding support for `wpa-psk-sha256` WiFis and allowing to configure **routing-policy** on the NetworkManager backend (LP: [#2086544](https://launchpad.net/bugs/2086544)).

    :::{versionadded} 25.04
    :::

* Adds support non-standard OVS setups, e.g. inside snap environments.

    :::{versionadded} 25.10
    :::

#### Package Management: APT 3

APT has been updated from version 2.7 to 3.1.

The new dependency solver is now automatically used if the classic solver cannot find a solution to either find a solution or add more context to the failure, and in other cases to [evaluate its performance](https://discourse.ubuntu.com/t/evaluating-the-new-apt-solver-in-25-04/55618).

APT has switched from GnuTLS and gcrypt to the OpenSSL library for TLS connections and file hashing, which should improve compatibility and reduces the footprint of minimal installations.

An automatic pager has been added to `apt(8)` for commands such as show and list, similar to `git log` and `journalctl`.

The `apt-key` command has been removed. Signature verification now makes direct use of `gpgv`. Some packages and system administration scripts may need adjustment for managing keys directly, advice can be found in the `apt-secure(8)` manual page.

#### Dracut
:::{versionchanged} 25.10
:::

Ubuntu now uses Dracut as its default initial ramdisk infrastructure, replacing `initramfs-tools`. Dracut uses `systemd` in the initial ramdisk and supports new features like Bluetooth and NVM Express over Fabrics (NVMe-oF).

The original `initramfs-tools` remains supported and you can switch between the two implementations if required.

For details about the switch, see [the specification](https://discourse.ubuntu.com/t/spec-switch-to-dracut/54776).
