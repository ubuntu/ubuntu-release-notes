---
tocdepth: 3
---

(ubuntu-26.04-lts-summary)=
# Ubuntu 26.04 LTS summary

If you’re upgrading **from Ubuntu 24.04 LTS (Noble Numbat)**, you receive the changes that happened in all the interim releases between Ubuntu 24.04 LTS and 26.04 LTS, as well as the most recent changes since Ubuntu 25.10.

For details, see the complete interim release notes: {ref}`24.10 <ubuntu-24.10-release-notes>`, {ref}`25.04 <ubuntu-25.04-release-notes>` and {ref}`25.10 <ubuntu-25.10-release-notes>`. Finally, review the latest {ref}`ubuntu-26.04-lts-changes-since-25.10`.

The following is an overview of the major changes.

## Desktop

### Updated applications

* Firefox 🔥🦊 has been updated [to version 149](https://www.firefox.com/en-US/firefox/148.0/releasenotes/) / [150](https://www.firefox.com/en-US/firefox/148.0/releasenotes/).
* LibreOffice 📚 has been updated from version 24.2 [to 25.8](https://wiki.documentfoundation.org/ReleaseNotes/25.8).
* Thunderbird 🌩️🐦 has been updated [to version 140 "Eclipse"](https://blog.thunderbird.net/2025/07/welcome-to-thunderbird-140-eclipse/).
* GNU Image Manipulation Program 🖼️ has received a major update from version 2.10 [to 3.0](https://www.gimp.org/news/2025/03/16/gimp-3-0-released/).

### GNOME 50

The GNOME desktop environment has been updated to version 50. Notable changes since GNOME 46 found in Ubuntu 24.04 LTS include the following:

:::{rubric} From GNOME 47
:::

* Support for small screens has been enhanced. Dialog windows are also more usable on narrow screens.
* Screen recording can be hardware-accelerated.
* Application rendering is now more responsive on slower devices.
* Remote login sessions persist if you disconnect.
* The file selection dialog is now based on the Files app, enabling more features.
* The Files app improves the navigation of network resources and other locations. It also shows more information on your search progress.
* Accessibility settings add the *Activate windows on hover* option.
* Keyboard settings show a preview of your keyboard layout in the add dialog.
* Power settings add new suspend timers for mobile devices.
* The Web app can automatically fill forms, comes with a redesigned bookmarks sidebar and provides a privacy report.
* In the Calendar app, the event details popover has been redesigned.

:::{rubric} From GNOME 48
:::

* Notifications are now grouped by application to prevent the list from getting too long.
* GNOME now includes the [triple buffering](https://discourse.ubuntu.com/t/triple-buffering-a-debrief/56314) feature from Ubuntu, improving responsiveness.
* Certain core GNOME components now use less CPU and memory.
* The image viewer now supports simple image editing.
* Digital Wellbeing features are now available, including screen time limits and break reminders.
* A new battery health preservation option is available.
* The Calendar app now supports managing events across multiple timezones.
* High Dynamic Range (HDR) output is now available for displays that support it.
* The design of the Text Editor app has been improved.
* Apps can now set up system-wide keyboard shortcuts.
* New windows are now placed in the center of the screen by default.
* Screen reader shortcuts, such as the {kbd}`CapsLock` Orca modifier, now function correctly in the Wayland session.

:::{rubric} From GNOME 49
:::

* The calendar app is now fully accessible when using the keyboard.
* The Web app improves ad-blocking, estimates page reading time, enhances security options and improves search.
* The remote desktop solution now supports multi-touch input for touch screens, relative mouse input for gaming, and extended virtual monitors.
* Media playback controls are now displayed on the lock screen.
* The accessibility menu is now easier to find on the login screen.

:::{rubric} From GNOME 50
:::

```{include} /reuse/26.04/gnome-50-news.txt
```

:::{rubric} Other major highlights
:::

* You can now set an application to start automatically after login in {menuselection}`Settings --> Apps`.
* Fractional scaling is now enabled by default. Fractional scaling factors have been optimized so as to minimize blur.
* The default monospace font size has been reduced to match the default user interface font size. The monospace font is used in terminals and similar applications.
* The [Sysprof](https://apps.gnome.org/Sysprof/) app is installed by default as a new system utility. This makes it easier to discover performance issues in your apps.

For details, see the upstream release notes: [GNOME 47](https://release.gnome.org/47/), [GNOME 48](https://release.gnome.org/48/), [GNOME 49](https://release.gnome.org/49/) and [GNOME 50](https://release.gnome.org/50/).

### Added a GNOME Shell search provider for snap applications
:::{versionadded} 26.04
:::

```{include} /reuse/26.04/snap-search-provider.txt
```

### Added a GNOME Shell search provider for web search
:::{versionadded} 26.04
:::

```{include} /reuse/26.04/web-search-provider.txt
```

### Accessibility improvements and fixes
:::{versionadded} 26.04
:::

```{include} /reuse/26.04/gnome-accessibility-improvements.txt
```

### Yaru theme updates
:::{versionadded} 26.04
:::

```{include} /reuse/26.04/yaru-updates.txt
```

### Improved integration with snap applications
:::{versionadded} 26.04
:::

```{include} /reuse/26.04/snap-desktop-integration.txt
```


### New document viewer
:::{versionchanged} 25.04
:::

The Document Viewer app for viewing PDFs is now provided by Papers instead of Evince. Papers started with the Evince codebase but it has been updated to use GTK4 and partially rewritten in Rust.

### New image viewer
:::{versionchanged} 25.10
:::

The Image Viewer app is now provided by [Loupe](https://apps.gnome.org/Loupe/) instead of Eye of GNOME (EOG). Loupe is written in Rust and powered by the [Glycin](https://gitlab.gnome.org/GNOME/glycin) library.

### New terminal emulator
:::{versionchanged} 25.10
:::

The Terminal app is now provided by [Ptyxis](https://gitlab.gnome.org/chergert/ptyxis/-/blob/main/README.md?ref_type=heads) instead of GNOME Terminal.

Some of its major features:

* Quick access to containers through `podman`, `toolbox` or `distrobox`
* Session-save to restore tabs in their directory as well as their container after re-opening the app
* Light and dark theme support with color palettes that extend into the window itself

### New system monitor

```{include} /reuse/26.04/gnome-resources.txt
```

### New default video player

The default video player is now [Showtime](https://apps.gnome.org/Showtime/), replacing Totem.

### New video and audio thumbnailers

Previously, video and audio thumbnails were generated by the Totem video thumbnailer. Now, the [`gst-thumbnailers`](https://salsa.debian.org/gnome-team/gst-thumbnailers) project handles the same functionality.

The new thumbnailers are written using the Rust GStreamer bindings and rely on the [Glycin](https://gitlab.gnome.org/GNOME/glycin) library for image handling. They do a better job at finding "interesting" frames than the previous Totem thumbnailers.

### Tracker Miners updated to LocalSearch

The Tracker Miners indexer has been renamed to LocalSearch. See the [upstream announcement](https://blogs.gnome.org/carlosg/2024/07/14/goodbye-tracker-hello-tinysparql-and-localsearch/). Ubuntu 26.04 LTS ships a substantial update of this tool from version 3.8.2 to 3.11.

For LocalSearch to be able to index audio files, video files, ISO files and certain zip-compressed office files, you need to select {guilabel}`Install third-party software for graphics and Wi-Fi hardware and additional media formats` during the Ubuntu installation. You can also install the extractors manually after installation with the following command:

```bash
sudo apt install localsearch-extractor-{ffmpeg,iso,office}
```

### Wayland session
:::{versionchanged} 25.10
:::

The *Ubuntu Desktop* session now runs only on the Wayland back end, because GNOME Shell can [no longer run as an X\.org session](https://discourse.ubuntu.com/t/ubuntu-25-10-drops-support-for-gnome-on-xorg/62538).

You can still run applications developed for X\.org through the XWayland compatibility layer.

Other desktop sessions, such as [KDE on X11](https://kde.org/), [Xfce](https://www.xfce.org/), [MATE](https://mate-desktop.org/), [`i3`](https://i3wm.org/) and many others, can still be launched using an X\.org session.

Machines using Nvidia graphics now fully support Wayland.

### Software & Updates app

Ubuntu Desktop no longer includes the Software & Updates settings app by default. For more details, see [the Discourse announcement](https://discourse.ubuntu.com/t/why-we-re-saying-goodbye-to-software-updates/76783).

The app is still available in the Ubuntu repository and it's been updated to use the GTK 4 toolkit.

You can install the app manually with the following command:

```bash
sudo apt install software-properties-gtk
```

### App Center enhancements
:::{versionadded} 24.10
:::

The App Center now includes improvements, including:

* Installs in progress
* Improved self-update handling
* Messaging for running snaps
* Direct uninstall of snaps from the manage page
* Scrolling support for touch screens
* Third party Deb installation

### Security Center
:::{versionadded} 24.10
:::

A new Security Center is included. It features the ability to easily enable or disable a new experimental [permissions prompting](https://discourse.ubuntu.com/t/ubuntu-desktop-s-24-10-dev-cycle-part-5-introducing-permissions-prompting/47963/1) feature for Home directory permissions.

### Permission prompting
:::{versionadded} 24.10
:::

Prompting is also supported by an additional seeded snap, `prompting-client`, for permissions prompt handling.

### Better power optimization
:::{versionadded} 24.10
:::

Power Profiles Manager [has been improved and optimized](https://gitlab.freedesktop.org/upower/power-profiles-daemon/-/releases/#0.23) to support better newer hardware features (especially AMD), can now support multiple optimization drivers and is now battery-aware to automatically increase the optimization levels when running on battery only.

### Performance improvements in Windows games
:::{versionadded} 25.04
:::

A new NTSYNC driver that emulates WinNT sync primitives is available, delivering better performance potential for Windows games running on Wine and Proton (Steam Play).

### New ARM64 Desktop image
:::{versionadded} 25.04
:::

There is now an official generic ARM64 Desktop ISO targeting VMs, ACPI + EFI platforms and Snapdragon based WoA devices.

Initial hardware enablement work for the Snapdragon X Elite platform is included in the Desktop ISO.

### Dual boot enhancements
:::{versionadded} 25.04
:::

Improved dual boot user experience, with a focus on BitLocker protected Windows systems:

* Added the option to install Ubuntu alongside existing BitLocker partitions if enough unallocated  space (or a sufficiently large and resizable partition) is available
* Made encrypted installations and other 'advanced options' available for dual boot scenarios

### JPEG XL support
:::{versionadded} 25.04
:::

The JPEG XL format is now supported without needing to install any additional packages

### VA-API accelerated video encoding and decoding by default

By default, hardware-accelerated video encoding and decoding are now provided for AMD and Intel users via the Video Acceleration API (VA-API).

### Updated optional media codecs
:::{versionadded} 25.10
:::

The additional packages that you can enable during the Ubuntu installation have been updated. The updated package set now includes the non-free AAC codec for supported Bluetooth headsets.

To install these codecs, select {guilabel}`Install third-party software for graphics and Wi-Fi hardware and additional media formats` in the Ubuntu installer.

### New update notifications
:::{versionadded} 25.10
:::

When system updates are available, the Software Updater window no longer pops up unprompted, stealing the keyboard focus. Instead, a notification shows up with options to open the Software Updater or to install all updates directly.

An icon in the system tray reminds you that updates are available even after dismissing the notification. It also provides a quick way to apply all the updates or inspect them in the Software Updater.

### Installer accessibility
:::{versionadded} 25.10
:::

The Ubuntu installer has received plenty of accessibility fixes for screen reader users.

### Ubuntu Insights
:::{versionadded} 25.10
:::

[Ubuntu Insights](https://github.com/ubuntu/ubuntu-insights) is being developed as a replacement for [Ubuntu Report](https://github.com/ubuntu/ubuntu-report) and gives you more control over the non-personally identifying system metrics that you choose to share with Canonical. The metrics collection is opt-in.

:::{note}
Any consent that you previously granted to Ubuntu Report will not be carried over to Ubuntu Insights.
:::

### `PreLogin` and `PostSession` scripts have been removed
:::{versionremoved} 26.04
:::

```{include} /reuse/26.04/session-scripts-removed.txt
```


## Server


### OpenSSH

The upgrade from Ubuntu 24.04 LTS, which had OpenSSH 1:9.6p1, to OpenSSH 1:10.2p1 includes major changes. Note the following:

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

### Chrony

* Chrony is now used as the default time daemon replacing `systemd-timesyncd` for new installations.

    To migrate existing systems after the upgrade to Ubuntu 26.04 LTS, use the following commands:

    ```bash
    apt-mark auto systemd-timesyncd
    apt install chrony
    ```

* NTS (authenticated & encrypted NTP) by default uses Ubuntu time servers.

* Ubuntu's NTP servers are defined in a [new snippet](https://discourse.ubuntu.com/t/improving-chrony-time-source-configuration-in-ubuntu/47850) in `/etc/chrony/sources.d/ubuntu-ntp-pools.sources`.

    If you edited `/etc/chrony/chrony.conf`, ensure that the servers defined in `/etc/chrony/sources.d/ubuntu-ntp-pools.sources` are not used twice.

* Specific release notes since Chrony version 4.5, which was found in Ubuntu 24.04 LTS, are at <https://chrony-project.org/news.html#_27_aug_2025_chrony_4_8_released>.

### ClamAV

Updated to 1.4.3 with many new features

* Scanning attachments found in Microsoft OneNote section files
* Extracting Universal Disk Format (UDF) partitions
* Extracting embedded images in HTML CSS `<style>` blocks
* Extracting `alz` and `lha`/`lzh` archives
* Toggle for image fuzzy hashing
* Improvements for VBA extraction in office documents
* Custom clean file cache size with `--cache-size` (uses more RAM)
* A `systemd.timer` unit for running `freshclam`
* Better limit handling for large files
* Client certificates for authentication to a private Freshclam mirror
* Virus database minimal age

For complete details of all changes leading up to 1.4.3, please see the upstream release notes at <https://blog.clamav.net/>.

### Django
:::{versionadded} 25.10
:::

Django has been updated to the latest LTS release 5.2 from 4.2, which includes many new features and bug fixes. All Django middleware provided in Ubuntu has also been updated to be compatible with the new version. See the [5.0 release notes](https://docs.djangoproject.com/en/5.2/releases/5.0/) for features and updates added with the major version change and the [5.2 release notes](https://docs.djangoproject.com/en/5.2/releases/5.2/) for the changes made leading up to the LTS release.

### PHP

PHP was updated to version 8.5. Among other enhancements and bugfixes, the highlighted changes since Ubuntu Noble 24.04 are:

* Property hooks
* Asymmetric visibility
* Updated DOM API
* A new URI Extension
* The Pipe Operator
* Clone With functionality
* The `#[\NoDiscard]` Attribute
* Closures and First-Class Callables in Constant Expressions
* Persistent `cURL` Share Handles
* `array_first()` and `array_last()` functions

For more details, breaking changes and other features, see the upstream release notes:

* [PHP 8.4](https://www.php.net/releases/8.4/en.php)
* [PHP 8.5](https://www.php.net/releases/8.5/en.php)

### Dovecot

Updated to 2.4.2. Version 2.4 introduced many changes to the Dovecot configuration format!

Coming from Ubuntu 24.04 LTS, please follow [dovecot’s 2.3 upgrade documentation](https://doc.dovecot.org/2.4.2/installation/upgrade/2.3-to-2.4.html).

When you’re coming from other versions, follow [the upgrade overview](https://doc.dovecot.org/2.4.2/installation/upgrade/overview.html).

### Postfix

Specific release notes for major version releases since Ubuntu 24.04 LTS (Noble Numbat) are:

* 3.9.0: https://www.postfix.org/announcements/postfix-3.9.0.html
* 3.10.0: https://www.postfix.org/announcements/postfix-3.10.0.html

A noteworthy change in the packaging of Postfix is that **by default it is no longer installed in a `chroot`, and only limited `chroot` support is available from now on**.

### RabbitMQ

```{include} /reuse/26.04/rabbitmq-upgrade.txt
```

### Samba

Samba has been updated to the new upstream 4.23 version. Changes since Ubuntu Noble 24.04:

* SMB3 Unix Extensions enabled by default
* NetBios is disabled by default in the configuration file /etc/samba/smb.conf for fresh installs
* SMB3 Directory Leases
* Netlogon Ping over LDAP and LDAPS
* Experimental Himmelblaud Authentication in Samba
* AD DC schema upgrade and provision performance improvements
* LDAP TLS/SASL [channel binding support](https://www.samba.org/samba/history/samba-4.20.3.html)
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

#### Samba on i386

Samba version 4.21.x added a dependency to the python3-samba package: python3-cryptography. Unfortunately, python3-cryptography was last built for i386 for Ubuntu Bionic 18.04, and is no longer available for that architecture, making this new dependency unsatisfiable.

For Ubuntu Plucky 25.04 and later, the python3-samba package is no longer built for i386. Please see [LP: #2099895](https://bugs.launchpad.net/ubuntu/+source/samba/+bug/2099895) for details. The main consequence is that the samba-tool script (part of that package) is no longer available for i386.

#### Upgrading an AD/DC from previous Ubuntu releases

If you have deployed a Samba Active Directory Domain Controller *without* having installed the `samba-ad-dc` package, you should install it before doing a release upgrade to Ubuntu 26.04 LTS (Resolute Raccoon). If `samba-ad-dc` is not installed prior to the release upgrade, the Active Directory Domain Controller functionality will not work on the upgraded system due to many missing components.

See [LP: #2101838](https://bugs.launchpad.net/ubuntu/+source/samba/+bug/2101838) for more information

### Squid

```{include} /reuse/26.04/squid-7.2-features.txt
```

```{include} /reuse/26.04/squid-7.2-removals.txt
```

For a list of all changes and fixes, please check the [upstream releases page](https://github.com/squid-cache/squid/releases).

### SSSD

```{include} /reuse/26.04/sssd-2.12-features.txt
```

```{include} /reuse/26.04/sssd-2.12-changes.txt
```

* https://sssd.io/release-notes/sssd-2.10.0.html
* https://sssd.io/release-notes/sssd-2.11.0.html
* https://sssd.io/release-notes/sssd-2.12.0.html

### strace

```{include} /reuse/26.04/strace-6.19.txt
```

### HAProxy
:::{versionchanged} 26.04
:::

HAProxy was updated to the latest upstream LTS release, 3.2, which introduces performance and efficiency improvements, faster and more reliable QUIC protocol support, and more. For further details on this new release, please check the HAProxy 3.2 [upstream announcement](https://www.mail-archive.com/haproxy@formilux.org/msg45917.html).

For users coming from HAProxy 2, breaking changes include detection of accidental multiple commands sent to the Runtime API, rejecting the enabled keyword for dynamic servers, stricter parsing of non-standard URIs and renaming of `tune.ssl.ocsp-update` to `tune.ocsp-update`.

You can learn more at [Announcing HAProxy 3.0](https://www.haproxy.com/blog/announcing-haproxy-3-0). A complete list of changes is available in the [upstream changelog](https://www.haproxy.org/download/3.0/src/CHANGELOG).

### DocumentDB
:::{versionadded} 26.04
:::

```{include} /reuse/26.04/documentdb-0.108-0-features.txt
```

### MySQL
:::{versionadded} 25.04
:::

MySQL was updated from 8.0 to 8.4 LTS, starting with 8.4.8 in Ubuntu 26.04 LTS. This is MySQL's first official long term support release, including various internal improvements, new features, and some important configuration changes.

Upstream release notes are available in the [Mysql 8.4 documentation library](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/). For more information about the transition from MySQL 8.0 to 8.4, see the [MySQL 8.4 overview](https://dev.mysql.com/doc/refman/8.4/en/mysql-nutshell.html).

Due to upstream policy, support for 32-bit MySQL Server has been removed. However, Ubuntu will continue to provide a MySQL client and client library for 8.4 on armhf and i386.

### MySQL Shell
:::{versionadded} 25.04
:::

MySQL Shell was updated from major version 8.0 to 8.4 to coincide with MySQL 8.4. It adds support for MySQL 8.4 servers, and provides additional improvements for interacting with MySQL 8.0 servers. For a list of features, see the [MySQL Shell 8.4 documentation](https://dev.mysql.com/doc/mysql-shell/8.4/en/). Release notes for MySQL Shell 8.4 can be found [here](https://dev.mysql.com/doc/relnotes/mysql-shell/8.4/en/).

### PostgreSQL
:::{versionadded} 26.04
:::

```{include} /reuse/26.04/postgresql-18-features.txt
```

### Valkey
:::{versionadded} 26.04
:::

```{include} /reuse/26.04/valkey-9.0-features.txt
```

### Container stacks
:::{versionadded} 25.10
:::

For the `containerd` and `runc` packages, we established a pattern to either keep the regular updates to the latest version or to opt for slower, more stable updates throughout the time the release is active. For more please read [Ubuntu Server Gazette - Issue 8 - Containers: Steady paths for agile stacks](https://discourse.ubuntu.com/t/ubuntu-server-gazette-issue-8-containers-steady-paths-for-agile-stacks/68680).

### Virtualization stack

A stack as active as that of `qemu`, `libvirt`, `edk2`, and `seabios` had too
many great new features and fixes to list them all. The upgrades between each
interim release like {ref}`libvirt@24.10 <libvirt-24.10>`,
{ref}`qemu@25.10 <qemu-25.04>`, or {ref}`edk2@25.10 <edk2-25.10>`
are already so huge they can only cover a selected high-level summary.
Each version adds various new emulated instructions, new CPU types and
virtualized platforms, which would be beyond the scope of release notes.
Here are just a few to motivate you to check out all the other
per-release changes and the related upstream announcements.

:::{versionadded} 26.04
:::

* libvirt: Better firmware selection
* libvirt More statistics for block devices on QEMU domains
* libvirt: Support for NUMA affinity of PCI devices
* libvirt+qemu: Support for NVIDIA Multi-Instance GPU (MIG) configurations
* qemu: Hyper-V host model mode
* qemu: The HPET device does not take the big QEMU lock anymore
* qemu: Support for loading multiple x509 cert+key identities (for transition to post-quantum cryptography)

:::{versionadded} 26.04
:::

```{include} /reuse/26.04/virt-hwe-feature.txt
```

:::{versionadded} 25.10
:::

* libvirt: ppc64 POWER11 processor support
* libvirt: Control over QEMU TLS priority strings
* libvirt: Support for NVMe disks
* libvirt: Support for AMD IOMMU device
* libvirt+qemu+edk2: Support for Intel TDX
* qemu: Support for the [RVA23 Profile](https://riscv.org/blog/risc-v-rva23-a-major-milestone/)
* qemu: Support for s390x generation 17 mainframe CPUs
* qemu: Support for true `virtio-scsi` multiqueue

:::{versionadded} 25.04
:::

* libvirt: Zero block detection for non-shared-storage migration
* libvirt: Support for versioned qemu CPU models
* libvirt+qemu+edk2: Support for AMD `SEV-SNP`
* qemu: Support for RISC-V privilege 1.13 spec
* qemu: Support for MTE on ARM KVM-based VMs

:::{versionadded} 24.10
:::

* qemu: `virtio-blk` device has gained true multiqueue support where different queues of a single disk can be processed by different I/O threads. This can improve scalability in cases where the guest submitted enough I/O to saturate the host CPU running a single I/O thread processing the virtio-blk requests. Multiple I/O threads can be configured using the new `iothread-vq-mapping` property.
* qemu: Support for emulating various new RISC-V instructions like the `Zacas`, `Zaamo`, `Zalrsc`, and `Ztso` extensions
* libvirt: Support for clusters in CPU topology.
* libvirt: New `dynamicMemslots` attribute for virtio-mem

### High availability and clustering

* The **`kpartx-boot`** package has been discontinued to align with Debian. Originally introduced to support `dmraid` booting, its functionality is preserved, as the `kpartx` package now includes everything previously provided by `kpartx-boot`.

    :::{versionremoved} 24.10
    :::

* The **`dmraid`** package has been removed. The rationale for its removal is outlined in bug [LP#2073677](https://bugs.launchpad.net/bugs/2073677), primarily due to its removal from Debian unstable and minimal upstream support. If you require this functionality, consider using alternatives like `mdadm`.

    :::{versionremoved} 24.10
    :::

* Pacemaker was updated to version 3. All new features and breaking changes are described in the [upstream release notes](https://projects.clusterlabs.org/w/projects/pacemaker/pacemaker_3.0_changes/).

## WSL

### Ubuntu Insights

[Ubuntu Insights](https://github.com/ubuntu/ubuntu-insights) is introduced as a successor to [Ubuntu Report](https://github.com/ubuntu/ubuntu-report), providing enhanced user control over the submission of non-personally identifying system metrics to Canonical. This opt-in metrics collection is now integrated into Ubuntu on WSL. 

Users initializing a WSL instance for the first time will be prompted for system metrics collection consent. This consent is persisted on the Windows host, eliminating repeated prompts for subsequent WSL instance setups. Consent management is also available on an individual per-instance basis.

 For additional information on data collection for Ubuntu on WSL, refer to the [documentation](https://documentation.ubuntu.com/wsl/latest/explanation/data-collection/).

### Chrony

:::{versionchanged} 25.10
:::

Ubuntu on WSL follows the platform-wide migration from `systemd-timesyncd` to `chrony` for network time synchronization that was implemented during the 25.10 cycle. Further details on this change in the WSL context are provided in the [documentation on time synchronization within WSL](https://documentation.ubuntu.com/wsl/latest/explanation/time-sync/).

### systemd-binfmt.service

:::{versionchanged} 25.10 
:::

`Binfmt` miscellaneous registrations are integral to Windows binary interoperability within WSL. Previously, the `systemd-binfmt.service` unit was disabled to mitigate against various potential issues. As of WSL 2.5.7, this system override is no longer necessary because the platform now incorporates a robust fix utilizing `systemd generators`.

Users relying on `systemd-binfmt.service` to apply new registrations when installing packages, for example, will now find it works without compromising the binary interoperability. To learn more, please check out [our docs about `binfmt`](https://documentation.ubuntu.com/wsl/stable/explanation/binfmt/).

### User setup

:::{versionchanged} 25.10
:::

Enhancements were implemented for Windows username processing during the initial WSL instance setup:

* Addressed an issue that resulted in the erroneous removal of uppercase letters from the Windows username before generating the suggested Linux username. See [LP: \#2122047](https://bugs.launchpad.net/ubuntu/+source/wsl-setup/+bug/2122047).
* Resolved failures occurring when the Windows username included non-ASCII characters. See [LP: \#2118617](https://bugs.launchpad.net/ubuntu/+source/wsl-setup/+bug/2118617).

### Ubuntu Pro for WSL version 1.0 released

**Ubuntu Pro for WSL** is a dedicated Windows application that streamlines the management of Ubuntu Pro subscriptions across WSL instances. 

For individual users, it eliminates the necessity of manually attaching each new Ubuntu instance to Ubuntu Pro for access to security benefits. For enterprise deployments, the application provides automated Pro-attachment and registration with Landscape, facilitating large-scale device fleet management. 

Documentation and download resources are available in [the documentation](https://documentation.ubuntu.com/wsl/stable/tutorials/getting-started-with-up4w) and [the download page](https://ubuntu.com/wsl/organizations).

## Development

* GCC 🐄 has been updated from version 14 to 15.2, `binutils` from 2.42 to 2.46, and `glibc` from 2.39 to 2.43.
* Python 🐍 has been updated from version 3.12 to 3.14.
* LLVM 🐉 has been updated from version 18 to 21.
* Rust 🦀 has been updated from version 1.75 to 1.93, while 1.91 and 1.92 are also available.
* Golang 🐀 has been updated from version 1.22 to 1.25.
* Zig ⚡ is now available in Ubuntu. It defaults to version 0.14.1.
* OpenJDK has been updated from version 21 to 25, while LTS versions 8, 11, 17, 21 are also available. OpenJDK 26, and OpenJDK 27 previews are also included.
* Ubuntu Toolchains has a new [homepage](https://ubuntu.com/toolchains).

### OpenJDK 25 and TCK certification
:::{versionadded} 25.10
:::

OpenJDK 25 package is available and is TCK (Technology Compatibility Kit) certified on AMD64, ARM64, S390X, PPC64EL. The Java TCK is the most comprehensive test suite that covers all aspects of Java SE specification including language features, libraries and APIs. This guarantees interoperability and conformance to standard.

### OpenJDK 21 and TCK certification
:::{versionadded} 24.10
:::

OpenJDK 21 and OpenJDK 17 packages are now TCK (Technology Compatibility Kit) certified on AMD64, ARM64, s390x, ppc64el. The Java TCK is the most comprehensive test suite that covers all aspects of Java SE specification including language features, libraries and APIs. This guarantees interoperability and conformance to standard.

### Spring® snaps
:::{versionadded} 25.04
:::

We are excited to announce the [devpack-for-spring](https://snapcraft.io/devpack-for-spring) snap and a set of Spring® [content snaps](https://snapcraft.io/devpack-for-spring-manifest) that will serve as development tools for Spring® projects.

Developers can now quickly build Ubuntu ROCK images for their Java applications using the [Gradle and Maven plugins for Rockcraft](https://github.com/rockcrafters/java-rockcraft-plugins).

### GraalVM snap
:::{versionadded} 25.04
:::

GraalVM Community Edition for JDK versions 21, 24 and 25 is now available as a [snap](https://snapcraft.io/graalvm-jdk). Java developers now have a choice to build and deploy their applications with standard OpenJDK, with OpenJDK-CRaC or as a GraalVM native image.


### .NET 10

.NET has been updated from version 8 to 10.

We have also expanded .NET support to the IBM Power platform, further broadening the platform’s reach.

### .NET snap
:::{versionadded} 24.10
:::

We are excited to introduce the new and improved [.NET Snap](https://snapcraft.io/dotnet), allowing developers to seamlessly install any supported version of .NET on any Ubuntu system.

### PowerShell snap on more architectures
:::{versionadded} 25.10
:::

Support for the PowerShell snap has been expanded to include the `arm64`, `s390x`, and `ppc64el` architectures, broadening its availability across platforms.


## Enterprise

### authd

[authd](https://github.com/ubuntu/authd), Ubuntu's cloud authentication solution, is now available from an official Ubuntu repository and has a range of new features. Changes since 24.04 are detailed below:

- authd can be installed directly from the Ubuntu archive (universe). For more information [read the blog](https://discourse.ubuntu.com/t/authd-enters-the-ubuntu-archive-in-26-04-lts/78193)
- The new [Google broker](https://snapcraft.io/authd-google) supports authentication through Google IAM
- Device registration is supported when authenticating with Microsoft Entra ID
- `authctl` is provided as a command line tool for managing authd
- A generic OpenID Connect (OIDC) broker for authd is available. For more information [read the blog](https://ubuntu.com/blog/more-identity-providers-ubuntu-generic-broker)
- Device ownership support lets you automatically assign a device owner and restrict login access
- A new setting allows you to enforce an access check with the identity provider during login
- New pages on [security](https://documentation.ubuntu.com/authd/stable-docs/explanation/security/), [deployment](https://documentation.ubuntu.com/authd/stable-docs/reference/#deployment), and [authctl](https://documentation.ubuntu.com/authd/stable-docs/reference/cli/) were added to the [docs](https://documentation.ubuntu.com/authd/en/stable-docs/)

### ADSys

The Active Directory Group Policy client for Ubuntu has been updated since 24.04 to:

- Fix invalid headers for newer polkit versions
- Allow searching GPO list by `userPrincipalName`
- Include a new [tutorial](https://documentation.ubuntu.com/adsys/latest/tutorial/getting-started/) and [glossary](https://documentation.ubuntu.com/adsys/latest/reference/glossary/)

## Cloud

On all cloud providers, `AMD64` based images are now built with `AMD64v3` by default. This effort begins with 26.04 Resolute Racoon images and will continue with future releases.

### Google Cloud

All Resolute 26.04 images are now built with `AMD64v3` by default. However, this means that the following CPU platforms available on `N1` machine types are no longer supported:
* Intel Ivy Bridge
* Intel Sandy Bridge

Automatic in-place upgrades to Ubuntu Pro will be fixed in [ubuntu-pro-client](https://github.com/canonical/ubuntu-pro-client/pull/3532) (to be included in the next point release)

### Amazon Web Services (AWS)

This transition impacts several Previous Generation Instance families. While AWS maintains these for legacy optimizations, they do not meet the microarchitecture requirements for Resolute Raccoon.

The following instance families are no longer supported starting with version 26.04:
* General Purpose: M1, M2, M3, M4
* Compute Optimized: C1, C3, C4
* Memory Optimized: R3, R4
* Storage/Accelerated: I2, G3, P2, P3, P3dn

Learn more about the [AWS Previous Generation Instances](https://docs.aws.amazon.com/ec2/latest/instancetypes/pg.html) to identify migration paths to current-generation instances


## Security

### New AppArmor sandboxing profiles
:::{versionadded} 25.04
:::

As part of a profile writing effort to improve overall system security, the AppArmor package now includes many new profiles for applications. This improved sandboxing can help mitigate the impact of any exploit in the confined applications.

:::{dropdown} Report bugs
These profiles may cause breakage for unanticipated uses of those applications, and we encourage users to file a bug on [Launchpad](https://bugs.launchpad.net/ubuntu/+source/apparmor/+filebug) for AppArmor-induced breakage in common use cases. When AppArmor denies an action, it usually generates a log entry describing the denial, which will help us investigate the bug, but which can also be used to add additional rules for customization or to work around the denials. AppArmor log entries can be read in the auditd logs, if auditd is installed, or in the `syslog` otherwise. [This page](https://gitlab.com/apparmor/apparmor/-/wikis/denial_quick_guide) describes how the information contained in the denial log can be used to update a local override.
:::

### TPM-backed full-disk encryption

You can now secure your Ubuntu Desktop installation using TPM-backed full-disk encryption (TPM/FDE).

With TPM/FDE, the encryption keys for your disk are automatically generated and stored safely in your computer’s Trusted Platform Module (TPM). Your disk unlocks automatically at boot when the TPM verifies that your system hasn't been tampered with. Optionally, you can add a PIN or passphrase for an extra layer of security.

For a complete description of TPM/FDE features, refer to [Hardware-backed disk encryption](https://documentation.ubuntu.com/desktop/en/26.04/explanation/hardware-backed-disk-encryption/) in the Ubuntu Desktop documentation.

You can enable TPM/FDE during the Ubuntu installation. See [Encrypt your disk with TPM](https://documentation.ubuntu.com/desktop/en/26.04/how-to/encrypt-your-disk-with-tpm/).

Some limitations remain: see {ref}`resolute-tpm-fde-limitations`.

### Post-quantum cryptography support
:::{versionadded} 25.10
:::

The OpenSSL library comes with several notable updates since Ubuntu 24.04:

* QUIC client and server support
* Support for post-quantum cryptography (PQC) algorithms (ML-KEM, ML-DSA and SLH-DSA)
* Broader EVP coverage
* Various performance improvements

For more information, see [Post Quantum Support in the upcoming 26.04 LTS](https://discourse.ubuntu.com/t/post-quantum-support-in-the-upcoming-26-04-lts/76840).

### Intel® Trusted Domain Extensions (TDX) host support
:::{versionadded} 25.10
:::

Intel® Trusted Domain Extensions (TDX) is a hardware-based confidential computing technology that isolates virtual machines into secure Trusted Domains (TDs). TDX protects guest workloads from the hypervisor, host OS, and other VMs by encrypting memory and enforcing strong, hardware-level isolation.

TDX is designed for cloud and virtualized environments where workload confidentiality must be preserved in shared, multi-tenant infrastructure.

Benefits for the user:

- Isolated multi-tenant compute: Ensures VM memory and data remain confidential even in shared cloud environments.
- Secure cloud migration: Enables customers to move sensitive workloads from on-premises environments to the cloud with confidence.
- Reduced data-breach risk: Hardware-based isolation significantly limits attack surface exposure.

Supported use cases:

- Confidential cloud workloads
- Secure telco and enterprise virtual machines
- Financial and healthcare secure workloads

Ubuntu supports Intel TDX for both host and guest operating systems. Guest support is available from Ubuntu 24.04 LTS onwards, while host support began with Ubuntu 25.10.

To learn how to use Intel TDX, see [Confidential Computing with Intel Trust Domain Extensions (TDX)](https://ubuntu.com/server/docs/how-to/virtualisation/intel-tdx/).

### cargo-auditable
:::{versionadded} 25.10
:::

Rust packages built on Launchpad now have opt-in support for [cargo-auditable](https://github.com/ubuntu/ubuntu-release-notes).
If enabled, binaries will include JSON-formatted metadata in a header section of the binary expressing the dependencies used to compile the binary.
If a CVE is discovered in a popular Rust crate, this dependency metadata lets users and sysadmins immediately check if a binary is compromised.

For details, see the [Ubuntu project documentation](https://documentation.ubuntu.com/project/contributors/language-specific/rust/cargo-auditable/).

## Hardware support

### NVIDIA Dynamic Boost
:::{versionadded} 25.04
:::

This release enabled NVIDIA Dynamic Boost by default on supported laptops with NVIDIA GPUs.

NVIDIA Dynamic Boost is a feature of the NVIDIA drivers that dynamically shifts power between CPU and GPU depending on the workload on the system. While gaming, this allows extracting more performance by granting more power to the GPU.

Dynamic Boost will be active only when the laptop is powered by AC and there is enough load on the GPU. It will not be engaged when the system is running on battery.

For more details refer to [NVIDIA's documentation](https://download.nvidia.com/XFree86/Linux-x86_64/570.133.07/README/dynamicboost.html).

### Support for new Intel® integrated and discrete GPUs

This release brings full support for the following Intel® Arc™ “Battlemage” and “Celestial” GPUs:

* Integrated:
  * Intel® Core™ Ultra Xe2 and Xe3
* Discrete:
  * Intel® Arc™ 5 B570 and B580
  * Intel® Arc™ Pro B50, B60, B65, and B70

Moreover, the following features are also included:

:::{versionadded} 25.04
:::

* Improved GPU and CPU ray tracing rendering performance in applications with Intel Embree support, such as Blender (v4.2+). Ray tracing hardware acceleration on the GPU improves frame rendering by 20-30%, due to a 2-4x speed-up for the ray tracing component.
* Full hardware accelerated video encoding of AVC, JPEG, HEVC, and AV1 on “Battlemage” devices.
* Introduction of the new CCS optimization in Intel® Compute Runtime.
* Enable debugging support for Intel Xe GPUs.
* oneAPI Level Zero Ray Tracing improves AI/ML workload speeds via Embree on SYCL

:::{versionadded} 25.10
:::

Via the [Linux kernel](https://launchpad.net/ubuntu/+source/linux) version 6.17
: - Initial support for Intel’s next-gen client platform codenamed Panther Lake.
  - Enhanced IOMMU and PCIe subsystem for improved GPU virtualization and passthrough.
  - Improved multi-GPU configuration support for Intel hardware.

Via [Mesa](https://launchpad.net/ubuntu/+source/mesa) version 25.2.3
: - `VK_KHR_shader_bfloat16` enabled in Intel ANV Vulkan driver for Battlemage and Panther Lake (GFX125+).
  - Completed OpenCL 2.0 coarse grain buffer SVM support in Iris driver.
  - Improved color fast-clear handling and multi-engine surface usage for Intel Vulkan (ANV) driver.

Via [`intel-media-driver`](https://launchpad.net/ubuntu/+source/intel-media-driver) version 25.3.0
: - Panther Lake Upstream decoding and VP9 encoding support.

Via [`intel-compute-runtime`](https://launchpad.net/ubuntu/+source/intel-compute-runtime) version 25.31
: - Enabling a Level Zero device unified shared memory (USM) pool as a performance change.
  - A performance-minded change for Xe2 graphics to ensure Level Zero events are always allocated in the local device memory.
 
Via [`level-zero`](https://launchpad.net/ubuntu/+source/level-zero) version 1.24
: - Update Level Zero Loader and Headers to support v1.13.1 of L0 Spec

Via [`level-zero-raytracing`](https://launchpad.net/ubuntu/+source/level-zero-gpu-raytracing) version 1.1.0
: - Ray Tracing Acceleration Structure (RTAS) Extensions

### Suspend with Nvidia
:::{versionadded} 25.10
:::

Suspend-resume support is now enabled in the proprietary Nvidia driver so as to prevent corruption and freezes when waking an Nvidia desktop.

### ARM desktop platforms
:::{versionadded} 25.10
:::

The `linux-generic` kernel for ARM64 provides broader compatibility for ARM64 desktop platforms that utilize UEFI for booting ([LP#2121352](https://bugs.launchpad.net/ubuntu/+source/linux-signed/+bug/2121352)).

### A new boot layout for Raspberry Pi
:::{versionadded} 25.10
:::
:::{versionchanged} 26.04
:::

A new layout of the boot partition is introduced to enhance the reliability of the boot process ([LP: #2116266](https://launchpad.net/bugs/2116266)). This will automatically "test" new boot assets written to the boot partition before committing them as the current "known good" set. See the [call for testing](https://discourse.ubuntu.com/t/call-for-testing-a-b-boot-on-raspberry-pi/64173) for more information, or [the blog post](https://waldorf.waveform.org.uk/2025/pull-yourself-up-by-your-bootstraps.html) covering the feature for the full details (including advice on how to opt-out of this feature, where required). The {manpage}`piboot-try(1)` man-page may also be consulted for advanced operations.

:::{warning}
Please note that, due to the new boot process, the boot firmware on your Pi *must* be up to date.

For Pi 3, 3+, CM3+, and Zero 2W
: No action required, the boot firmware is in the image itself.

For Pi 4, 400, CM4
: Your boot firmware *must* be dated no earlier than **2022-11-25**.

For Pi 5, 500, CM5
: Your boot firmware *must* be dated no earlier than **2025-02-11**.

To check, run `sudo rpi-eeprom-update`. If your firmware is dated earlier, using Ubuntu 24.04 LTS (Noble Numbat) or later, run `sudo rpi-eeprom-update -a` and reboot.
:::

### Raspberry Pi is based on the minimal image
:::{versionchanged} 25.10
:::

The Ubuntu desktop images for Raspberry Pi are now based upon the `desktop-minimal` seed rather than `desktop` ([LP: #2103808](https://launchpad.net/bugs/2103808)). This greatly reduces the default set of applications installed on the images (saving approximately 777MB of space on the uncompressed image, and thus on user's systems).

:::{dropdown} The list of applications removed from the image

  - `deja-dup` (backup service)
  - `file-roller` (archive handler)
  - `gnome-calendar`
  - `gnome-snapshot` (camera application)
  - `libreoffice-*`
  - `remmina` (remote desktop client)
  - `rhythmbox` (music player)
  - `shotwell` (photo catalogue)
  - `simple-scan` (flat-bed scanner application)
  - `thunderbird` (email client)
  - `showtime` (video player)
  - `transmission-gtk` (bittorrent client)
:::

The applications mentioned above will *not* be automatically removed for upgraders as the `ubuntu-desktop` meta-package remains manually installed in this circumstance. If you wish to remove these applications (in bulk), you may do so with:

```{terminal}
:user:
:host:
:dir:
sudo apt purge ubuntu-desktop --autoremove
```

If you wish to keep specific applications, simply "install" them with `apt` first. This marks them as "manually installed", excluding them from automatic removal.

### Swap is created with `cloud-init` on Raspberry Pi
:::{versionchanged} 25.10
:::

The creation of the swap file on the desktop images is now handled by [`cloud-init`](https://cloudinit.readthedocs.io/en/latest/) ([LP: #2116275](https://launchpad.net/bugs/2116275)). You may customize the size of the swap file by editing `user-data` on the boot partition prior to first boot (commented examples are included in the image).

(resolute-new-risc-v-requirements)=
### New RISC-V requirements
:::{versionchanged} 25.10
:::

The RISC-V version of Ubuntu 26.04 LTS only supports hardware that implements the RVA23S64 ISA profile. You can't run Ubuntu 26.04 LTS on systems that don't satisfy this requirement. Ubuntu 24.04 LTS continues to support boards with the earlier RVA20 processor cores.

As of April 2026, no RVA23S64 hardware is available yet. The only supported RISC-V platform is the QEMU virtualization with the `-cpu rva23s64` CPU profile.

### IBM Z requirements raised to z15
:::{versionchanged} 26.04
:::

On the IBM Z (s390s) architecture, Ubuntu 26.04 LTS now requires the z15 architectural level at minimum. As a result, you can't install Ubuntu 26.04 LTS on IBM Z generation z14 (LinuxONE II) or older.

The performance on IBM Z generation z15 (LinuxONE III) and newer has improved.

For more information, refer to the following release notes:

- {ref}`ibm-z15-level`
- {ref}`ibm-z14-support-removed`

## Common changes

### `sudo-rs`
:::{versionadded} 25.10
:::

The `sudo-rs` tool is now the default `sudo` provider.

The `sudo` tool (the original `sudo` maintained by Todd C. Miller) has been renamed to `sudo.ws`. Additionally, the `sudo-ldap` package has been removed: please switch to using LDAP authentication via PAM.

See [Ubuntu Server Docs](https://documentation.ubuntu.com/server/how-to/security/user-management/#sudo-rs) for configuring your default `sudo` provider and for the differences between `sudo-rs` and `sudo.ws`.


### `rust-coreutils`
:::{versionadded} 25.10
:::

The core utilities of the operating system are now provided by the [`rust-coreutils`](https://launchpad.net/ubuntu/+source/rust-coreutils) package. Among other things, this brings significant performance improvements, such as in the `base64` tool.

Because `rust-coreutils` are not fully compatible yet, we continue to provide the classic GNU utilities as well. These are accessed by running `gnu` prefixed to the desired command. For example:

```none
gnuls
```

Alternatively, you can switch between the two sets of utilities by running the following commands:

To switch to GNU coreutils:
:  

  ```none
  sudo apt install coreutils-from-gnu --allow-remove-essential
  ```

To switch back to rust-coreutils:
:  

  ```none
  sudo apt install coreutils-from-uutils --allow-remove-essential
  ```

Because of unresolved bugs, the `cp`, `mp`, and `rm` utilities are still from GNU in `rust-coreutils`.
For more information, see [An update on rust-coreutils](https://discourse.ubuntu.com/t/an-update-on-rust-coreutils/80773).


### Architecture variants and `amd64v3`
:::{versionadded} 25.10
:::

Ubuntu now has the ability balance hardware compatibility and fuller utilization of modern hardware by building multiple versions or "variants" of a package. The first variant we are introducing is `amd64v3`, which is optimized for the `x86-64-v3` [microarchitecture level](https://en.wikipedia.org/wiki/X86-64#Microarchitecture_levels).

For maximum compatibility, this variant is opt-in by default. If you are running on compatible hardware (and if your AMD64 machine was built in the last 10 years or so, you probably are) you can upgrade to `amd64v3` packages with the following commands:

```bash
echo 'APT::Architecture-Variants "amd64v3";' | sudo tee /etc/apt/apt.conf.d/99enable-amd64v3
sudo apt update
sudo apt upgrade
```

For details, see the announcement: [Introducing architecture variants: amd64v3 now available in Ubuntu 25.10](https://discourse.ubuntu.com/t/introducing-architecture-variants-amd64v3-now-available-in-ubuntu-25-10/71312).

### Linux kernel 7.0

For users running the GA generic stack, the Linux kernel has been updated from version 6.8 to 7.0. For users running the Hardware Enablement (HWE) stack, the Linux kernel has been updated from version 6.17 (25.10 backport) to 7.0.

* Crash dumps are now [enabled by default](https://documentation.ubuntu.com/server/how-to/software/kernel-crash-dump/#kdump-enabled-by-default) for desktop and server installations.

    :::{versionadded} 24.10
    :::

* Kernel developers can now make use of a [new scheduling system](https://canonical.com/blog/crafting-new-linux-schedulers-with-sched-ext-rust-and-ubuntu), `sched_ext`, which provides a mechanism to implement scheduling policies as eBPF programs. This enables developers to defer scheduling decisions to standard user-space programs and implement fully functional hot-swappable Linux schedulers, using any language, tool, library, or resource accessible in user-space.

    :::{versionadded} 25.04
    :::

* After the generic kernel gained the ability to [tune responsiveness at boot time](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2051342), the `linux-lowlatency` binary package has been retired in favor of a combination of `linux-generic` and a new user-space `lowlatency-kernel` package, responsible of tuning the GRUB command line.

    :::{versionadded} 25.04
    :::

* The RISC-V kernel supports only architectures compliant with the RVA23S64 ISA profile.

    For details, see {ref}`resolute-new-risc-v-requirements`.

    :::{versionchanged} 25.10
    :::

* `linux-generic` for arm64 provides via `stubble` broader compatibility for arm64 desktop platforms that utilize UEFI for booting ([LP: #2121352](https://bugs.launchpad.net/ubuntu/+source/linux-signed/+bug/2121352)).

    :::{versionadded} 25.10
    :::

* Upstream Linux kernel 7.0 delivers improved support for Intel® Core™ Ultra Series 3 processors (codenamed Panther Lake), introducing targeted optimizations for Intel Xe3 integrated graphics and the integrated NPU (Neural Processing Unit).

    :::{versionadded} 26.04
    :::

* Integrated IgH EtherCAT module and Generic driver ([LP: #2138621](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2138621)). These modules provide real-time performance for industrial EtherCAT networks.

    :::{versionadded} 26.04
    :::

* The real-time linux kernel is available in the main archive (outside of Ubuntu Pro) in 26.04. Following the `PREEMPT_RT` patches being upstreamed, the 26.04 release of the real-time kernel is available for free for anyone to use.

    :::{versionadded} 26.04
    :::

* Kernel Livepatch now supports the ARM64 architecture.

    :::{versionadded} 26.04
    :::

* DOCA-OFED 26.01 kernel modules are available for the Ubuntu generic and select derivative kernels.

    :::{versionadded} 26.04
    :::


### `systemd` 259

The `systemd` service manager has been updated from version 255 to 259.

* Ubuntu 26.04 LTS is the last release that supports System V service scripts compatibility in `systemd`. Migrate your legacy System V scripts to native `systemd` unit files.

* Support for `cgroup` version 1 (`legacy` and `hybrid` hierarchies) has been removed. For details, see {ref}`cgroup-v1-removed`.

    :::{versionremoved} 26.04
    :::

* Ubuntu now comes with the upstream `tmp.mount` unit by default. As a result, the `/tmp` directory is now a `tmpfs` file system by default.

    :::{versionchanged} 24.10
    :::

### Netplan 1.2

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

### Package Management: APT 3

APT has been updated from version 2.7 to 3.1.

The new dependency solver is now automatically used if the classic solver cannot find a solution to either find a solution or add more context to the failure, and in other cases to [evaluate its performance](https://discourse.ubuntu.com/t/evaluating-the-new-apt-solver-in-25-04/55618).

APT has switched from GnuTLS and gcrypt to the OpenSSL library for TLS connections and file hashing, which should improve compatibility and reduces the footprint of minimal installations.

An automatic pager has been added to `apt(8)` for commands such as show and list, similar to `git log` and `journalctl`.

The `apt-key` command has been removed. Signature verification now makes direct use of `gpgv`. Some packages and system administration scripts may need adjustment for managing keys directly, advice can be found in the `apt-secure(8)` manual page.

#### History management in APT
:::{versionadded} 25.10
:::

APT now provides an interface for viewing and manipulating its command history.

- **List** changes:

    ```none
    $ apt history-list
    ID   Command line             Date and Time          Action    Changes

    0    install cowsay           2026-04-23  17:00:00   Install   1
    1    upgrade                  2026-04-23  18:15:00   Upgrade   25
    2    build-dep .              2026-04-24  18:30:00   Install   4
    ```

- **Inspect** changes:

    ```none
    $ apt history-info 0
    Transaction ID: 0
    Start time: 2026-04-23  17:00:00
    End time: 2026-04-23  17:00:05
    Requested by: raccoon (1000)
    Command line: apt install cowsay
    Packages changed:
        Install cowsay:amd64 (3.03+dfsg2-8build1)
    ```

- **Undo** changes:

    ```none
    $ sudo apt history-undo 0
    REMOVING:
    cowsay

    Summary:
    Upgrading: 0, Installing: 0, Removing: 1, Not Upgrading: 0
    Freed space: 89.1 kB

    Continue? [Y/n]
    ```

- **Redo** changes:

    ```none
    $ sudo apt history-redo 0
    cowsay is already the newest version (3.03+dfsg2-8build1).
    Summary:
    Upgrading: 0, Installing: 0, Removing: 0, Not Upgrading: 0
    ```

- **Rollback** to a specific change:

    ```none
    $ sudo apt history-rollback 1
    REMOVING:
    libtext-unidecode-perl  tex-common  texinfo  texinfo-lib

    Summary:
    Upgrading: 0, Installing: 0, Removing: 4, Not Upgrading: 0
    Freed space: 8119 kB
    ```

### Dracut
:::{versionchanged} 25.10
:::

Ubuntu now uses Dracut as its default initial ramdisk infrastructure, replacing `initramfs-tools`. Dracut uses `systemd` in the initial ramdisk and supports new features like Bluetooth and NVM Express over Fabrics (NVMe-oF).

The original `initramfs-tools` remains supported and you can switch between the two implementations if required.

For details about the switch, see [the specification](https://discourse.ubuntu.com/t/spec-switch-to-dracut/54776).


## More details

You can find the {ref}`resolute-known-issues` in this release on a separate page.

For a complete list of changes in Ubuntu 26.04 LTS, refer to the following documents, depending on the Ubuntu release that you're upgrading from:

- {ref}`ubuntu-24.10-release-notes`
- {ref}`ubuntu-25.04-release-notes`
- {ref}`ubuntu-25.10-release-notes`
- {ref}`ubuntu-26.04-lts-changes-since-25.10`
