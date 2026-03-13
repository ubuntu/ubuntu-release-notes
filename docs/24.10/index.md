---
tocdepth: 3
---

(ubuntu-24.10-release-notes)=
# Ubuntu 24.10 release notes

These release notes for **Ubuntu 24.10** (Oracular Oriole) provide an overview of the release and document the known issues with Ubuntu and its flavors.

:::{toctree}
:maxdepth: 1
:hidden:

Release schedule <schedule>
:::

## Support lifespan

Ubuntu 24.10 will be supported for 9 months until July 2025. If you need long term support, we recommend you use [Ubuntu 24.04.1 LTS](https://ubuntu.com/download) which is supported until at least 2029.

## Upgrades

* Upgrades to to Ubuntu 24.10 will refresh seeded snaps to the appropriate snap channels, regardless of what was being tracked before. Snaps that are newly-seeded will be installed during the upgrade. In particular, the following snaps will be installed or refreshed on upgrade: 

  - `core24 latest/stable`
  - `desktop-security-center 1/stable/ubuntu-24.10`
  - `gnome-46-2404 stable/ubuntu-24.10`
  - `mesa-2404 stable/ubuntu-24.10`
  - `prompting-client 1/stable/ubuntu-24.10`
  - `firefox stable/ubuntu-24.10`
  - `thunderbird stable/ubuntu-24.10`
  - `snapd-desktop-integration stable/ubuntu-24.10`

  Early upgrades may wish to perform these updates manually.

(new-features-in-24-10)=
## New features in 24.10

### Updated Packages

#### OpenSSL 3.3

OpenSSL has been updated to version 3.3 with large performance and scalability improvements compared to openssl 3.0.
It is now also loading configuration dropins from `/etc/ssl/openssl.conf.d` for easier customisation.

### Linux kernel 🐧
Ubuntu 24.10 includes the new 6.11 Linux kernel that brings many new features.

Crash dumps are now enabled by default for desktop and server installations. Please refer to the [Ubuntu Server Kernel crash dump](https://documentation.ubuntu.com/server/how-to/software/kernel-crash-dump/#kdump-enabled-by-default) documentation for complete details.

Detailed changes are reported in the [Oracular Kernel Release Notes](https://discourse.ubuntu.com/t/introducing-kernel-6-11-for-the-24-10-oracular-oriole-release/47560) post.

### systemd v256.5

The init system was updated to systemd v256.5. See the [upstream changelog ](https://github.com/systemd/systemd/releases/tag/v256) for more information about individual features. To highlight a few things:

* Support for cgroup v1 ('legacy' and 'hybrid' hierarchies) is now
considered obsolete and systemd by default will refuse to boot under
it. To forcibly reenable cgroup v1 support,
`SYSTEMD_CGROUP_ENABLE_LEGACY_FORCE=1` must be set on kernel command
line.

* Support for System V service scripts is deprecated and will be
removed in a future release. Please make sure to update your software
*now* to include a native systemd unit file instead of a legacy
System V script to retain compatibility with future systemd releases.

* When `sshd` is installed on a system, a new systemd generator, `systemd-ssh-generator` binds a socket-activated SSH server to local `AF_VSOCK` and `AF_UNIX` sockets under certain conditions. See the [man page](https://www.freedesktop.org/software/systemd/man/devel/systemd-ssh-generator.html#) for more details. Note that this feature is different and indendent from `sshd-socket-generator` which is shipped in Ubuntu's `openssh-server` package.

* Ubuntu now ships upstream systemd's `tmp.mount` by default. In effect this means that `/tmp` is now a `tmpfs` by default.

*   cryptsetup tools such as `systemd-cryptsetup`, `systemd-cryptenroll`,
`systemd-veritysetup`, and more, have been split into a new `systemd-cryptsetup`
package to reduce dependencies pulled in by the main `systemd` package. This
new package is only listed as a `Suggests`, so if this functionality is used
ensure that either `Suggests` are installed or that it is
manually installed.

* Ubuntu's `systemd-networkd` no longer sets `UseDomains=true` for managed network interfaces. In effect, this means that search domains configured in DHCP leases will not be reflected in `/etc/resolv.conf` by default. This change aligns Ubuntu's default behavior with that of upstream. System administrators may choose to override this default on a global, or per-interface basis. See [`systemd.network`](https://www.freedesktop.org/software/systemd/man/256/systemd.network.html#UseDomains=) for details.

### Netplan v1.1 🌐
The new [version 1.1 of Netplan](https://github.com/canonical/netplan/releases/tag/1.1) introduces a custom `systemd-networkd-wait-online` logic, waiting for link-local addresses and one routable interface, as described in the https://discourse.ubuntu.com/t/spec-definition-of-an-online-system/27838. Besides improvements to the `embedded-switch-mode` setting for SR-IOV devices, the introduction of parser flag to skip broken configurations and fixes for ProtonVPN and Microsoft Azure Linux.

### Toolchain Upgrades 🛠️

* GCC 🐄 is updated to 14.2, binutils to 2.43.1, and glibc to 2.40.
* Python 🐍 is updated to 3.12.7
* LLVM 🐉 now defaults to version 19
* Rust 🦀 toolchain defaults to version 1.80
* Golang 🐀 is updated to 1.23
* .NET 9 🤖 now available, .NET 8 support extended to IBM Power
* OpenJDK ☕ versions 23 and 24 (early access snapshot) are now available

#### OpenJDK

OpenJDK 21 is still the default. OpenJDK 23 is included as an optional OpenJDK. An early access snapshot of OpenJDK 24  is also included. Support for OpenJDK LTS versions 17, 11 and 8 is being maintained.

OpenJDK 21 and OpenJDK 17 packages are now TCK (Technology Compatibility Kit) certified on amd64, arm64, s390x, ppc64el and armhf. The Java TCK is the most comprehensive test suite that covers all aspects of Java SE specification including language features, libraries and APIs. This guarantees interoperability and conformance to standard.

#### .NET

With the release of .NET 9, Ubuntu reinforces its commitment to supporting the .NET community. .NET 9 is fully supported on Ubuntu 24.10 and is also available for Ubuntu 24.04 LTS (Noble Numbat) and Ubuntu 22.04 LTS (Jammy Jellyfish) through the [.NET Backports PPA](https://launchpad.net/~dotnet/+archive/ubuntu/backports).

In addition, we have expanded .NET support to the IBM Power platform for both .NET 8 and .NET 9, further broadening the platform’s reach.

We are also excited to introduce the new and improved [.NET Snap](https://snapcraft.io/dotnet), allowing developers to seamlessly install any supported version of .NET on any Ubuntu system.


### Default configuration changes ⚙️

As always there are many changes to defaults, mostly by newer versions of
packages. But a few are worth spelling out if your former automation,
configuration and tuning relied on those settings being one or the other way.

### Ubuntu Desktop

#### Installer and Upgrades

* The desktop installer now support local file paths for autoinstall import.


* **Power Profiles Manager** [has been improved and optimized](https://gitlab.freedesktop.org/upower/power-profiles-daemon/-/releases/#0.23) to support better newer hardware features (especially AMD), can now support multiple optimization drivers and is now battery-aware to automatically increase the optimization levels when running on battery only.

* **fprintd** has been updated and [**libfprint** supports now many other fingerprint drivers and devices](https://gitlab.freedesktop.org/libfprint/libfprint/-/releases#v1.94.8).

#### Store

The App Center now includes improvements to the Manage page including:
* Installs in progress
* Improved self-update handling
* Messaging for running snaps
* Direct uninstall of snaps from the manage page
* Scrolling support for touch screens

Third party deb installation is now also supported.


#### Security Center

* A new Security Center is included. It features the ability to easily enable or disable a new experimental [permissions prompting](https://discourse.ubuntu.com/t/ubuntu-desktop-s-24-10-dev-cycle-part-5-introducing-permissions-prompting/47963/1) feature for Home directory permissions.
* More features will be added in future Ubuntu releases.
* Prompting is also supported by an additional seeded snap, `prompting-client`, for permissions prompt handling.

#### 20th Anniversary Celebration
20 years ago, the first version of Ubuntu was released, Ubuntu 4.10 "Warty Warthog". We are celebrating this monumental anniversary with several temporary flourishes
* The return of the original startup sound, which can be disabled via Settings > Sound
* A 'Warty' brown accent colour that can be enabled in Settings > Appearance > Style
* An anniversary logo

#### GNOME 👣

* GNOME has been updated to include new features and fixes from the latest GNOME release, [GNOME 47](https://release.gnome.org/47/).
* In GNOME Shell and Mutter, Ubuntu includes additional patches to enhance stability and performance, which have not yet been merged upstream.
* The Ubuntu dock now visualises snap refreshes and includes better handling for PWAs installed via the Chromium snap.

#### Default app changes
* The [Sysprof](https://apps.gnome.org/Sysprof/) app is installed by default as a new system utility. This makes it easier to discover performance issues in your apps. 

#### Updated Applications

* [Firefox](https://mozilla.org/firefox/releases/) 130 🔥🦊
* [LibreOffice 24.8](https://wiki.documentfoundation.org/ReleaseNotes/24.8) 📚
* [Thunderbird 128 "Supernova"](https://blog.thunderbird.net/2023/07/our-fastest-most-beautiful-release-ever-thunderbird-XY-supernova-is-here/) 🌩️🐦

#### Updated Subsystems
* [BlueZ 5.77](https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/ChangeLog?id=5.77) 💙
* [Cairo 1.18.2](https://cairographics.org/news/cairo-1.18.2/) 👁️⃤
* [Noto Color Emoji Font 2.047 with Unicode 16 support](https://blog.emojipedia.org/google-debuts-emoji-16-0-support/) 🥳
* [NetworkManager 1.48](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/blob/nm-1-48/NEWS) 🖧
* [Pipewire 1.2.4](https://gitlab.freedesktop.org/pipewire/pipewire/-/blob/1.2.4/NEWS) 🔊
* [Poppler 24.08](https://gitlab.freedesktop.org/poppler/poppler/-/blob/poppler-24.08.0/NEWS) 📝
* [xdg-desktop-portal 1.18](https://github.com/flatpak/xdg-desktop-portal/blob/1.18.4/NEWS) ⛩️

#### Nvidia

Ubuntu 24.10 now defaults to Wayland instead of Xorg on machines using Nvidia graphics. If you require Xorg instead then select 'Ubuntu on Xorg' from the session menu on the login screen.

### Ubuntu WSL

--

### Ubuntu Server

#### Apache2
Apache2 has been updated from Noble's 2.4.58 to the current 2.4.62, and some of the more noteworthy changes include:

  * htpasswd: Add support for passwords using SHA-2.
  * core: Allow mod_env to override system environment vars.
  * mod_xml2enc: Update check to accept any text/ media type or any XML media type per RFC 7303, avoiding corruption of Microsoft OOXML formats.
  * mod_ssl: SSLProxyMachineCertificateFile/Path may reference files which include CA certificates; those CA certs are treated as if configured with SSLProxyMachineCertificateChainFile.
  * mod_ssl: Improve compatibility with OpenSSL 3, including handling when OPENSSL_NO_ENGINE is set and support for loading certs/keys from pkcs11.
  * mod_proxy: Ignore (and warn about) enablereuse=on for ProxyPassMatch when some dollar substitution (backreference) happens in the hostname or port part of the URL.
  * mod_proxy: Add optional third argument for ProxyRemote, which configures Basic authentication credentials to pass to the remote proxy.
  * mod_md: Certificate renewals are triggerable using OCSP stapling information.

For more details, please see the [full set of changes](https://downloads.apache.org/httpd/CHANGES_2.4.59).


#### Clamav
Clamav is updated from version 1.0.5 to 1.3.1 in Oracular, bringing significant improvements and changes, including:

  * Added support for extracting and scanning attachments found in Microsoft OneNote section files.
  * Added support for extracting Universal Disk Format (UDF) partitions.
  * Added a --cache-size option to customize the size of ClamAV's clean file cache, which may improve scan performance at the expense of more RAM.
  * Introduced a customizable SystemD timer for running Freshclam updates, without sending Freshclam into the background.
  * Refined limit handling for large files
  * Added ability for Freshclam to use a client certificate PEM file and a private key PEM file for authentication to a private mirror
  * Added the ability to extract images embedded in HTML CSS `<style>` blocks.
  * Enhancements relating to VBA extraction from office documents
  * Added support for aborting on standup if virus database is older than a configured number of days.

For a comprehensive listing of changes included since Ubuntu Noble, please see the changelogs for [1.1.0](https://blog.clamav.net/2023/05/clamav-110-released.html), [1.2.0](https://blog.clamav.net/2023/08/clamav-120-feature-version-and-111-102.html), [1.3.0](https://blog.clamav.net/2023/11/clamav-130-122-105-released.html), and [1.3.1](https://blog.clamav.net/2024/04/clamav-131-123-106-patch-versions.html).

#### Chrony
The chrony package in Oracular was changed to no longer ship the default Ubuntu NTP pools in `/etc/chrony/chrony.conf`. A new snippet configuration file is created in `/etc/chrony/sources.d/ubuntu-ntp-pools.sources` defining those servers. The motivation for this change is explained in [LP: #2048876](https://bugs.launchpad.net/ubuntu/+source/chrony/+bug/2048876).

If you changed your `chrony.conf`, an upgrade to this version will stop at a dpkg config prompt, showing the differences between the installed file and the new one. If you chose to keep the existing `chrony.conf`, keep in mind that the Ubuntu NTP pools from `/etc/chrony/sources.d/ubuntu-ntp-pools.sources` will also be used.

@ankushpathak wrote a great post about this change:

https://discourse.ubuntu.com/t/improving-chrony-time-source-configuration-in-ubuntu/47850

#### cloud-init v. 24.3.1
Notable features beyond v. 24.1 present in Noble:

- Bootspeed improvement: support for socket-based shared python process
across cloud-init boot stages ([#5595](https://github.com/canonical/cloud-init/pull/5595))
- NoCloud support for FTP and FTP over TLS ([#4834](https://github.com/canonical/cloud-init/pull/4834))
- Add network-config seed support for nocloud datasource ([#5566](https://github.com/canonical/cloud-init/pull/5566))
- Network v2 schema validation ([#4892](https://github.com/canonical/cloud-init/pull/4892))
- Add support for disk setup of nvme devices ([#5263](https://github.com/canonical/cloud-init/pull/5263))
- Support remote URI sources write_files module ([#5505](https://github.com/canonical/cloud-init/pull/5055))
- provide option to set empty passwords and fix password unlock when
lock_passwd: False on Alpine/FreeBSD/OpenBSD/DragonflyBSD ([#5355](https://github.com/canonical/cloud-init/pull/5355))
- WSL support multi-part MIME config parts as well as landscape tags for
provisioning ([#5460](https://github.com/canonical/cloud-init/pull/5460), [#5538](https://github.com/canonical/cloud-init/pull/5538))
- Added support in cloudinit.features.DEPRECATION_INFO_BOUNDARY allowing stable downstream images to pin the original MAJOR.MINOR version of cloud-init released on that image. This avoids introduction of new deprecation messages (and potential exit 2 from cloud-init status) across cloud-init version upgrades.

Breaking Changes:

- Warning issued for systemd environments if cloud-init boot stages are
called by PIDs other than the root process. It is expected that boot
stages are only called by systemd units and not post-production scripts
or tools.
- Introduce a [performance optimization by sharing the python environment and setup costs across all four boot stages with a new cloud-init-main.service](https://discourse.ubuntu.com/t/announcement-cloud-init-perfomance-optimization-single-process/47505)

#### Containerd
The Containerd application was updated to version `1.7.19`. Some highlights of this update:

* Remove overlayfs volatile option on temp mounts (#10332)
* Update AppArmor template to allow confined runc to kill containers (#10129)
* Update AppArmor template to better support rootlesskit (#10116)

For more information, check the [upstream release notes](https://github.com/containerd/containerd/releases).

#### Django
Django was updated from Noble's 4.2.11 to 4.2.15, which brings several bug fixes. For more information, see the upstream changelogs: [4.2.12](https://docs.djangoproject.com/en/4.2/releases/4.2.12/), [4.2.13](https://docs.djangoproject.com/en/4.2/releases/4.2.13/), [4.2.14](https://docs.djangoproject.com/en/4.2/releases/4.2.14/), [4.2.15](https://docs.djangoproject.com/en/4.2/releases/4.2.15/)

#### Docker
The Docker application was updated to version `26.1.3`. Some highlights of this update:

* apparmor: Allow confined runc to kill containers
* Removal of AuFS, Legacy "overlay", and Device mapper storage drivers
* Removal of support for interacting with V1 registries

Watch out for deprecation or removal of features in this [upstream page](https://github.com/docker/cli/blob/v26.1.3/docs/deprecated.md).

#### unminimize

unminimize has been moved to a dedicated package which can be installed with `apt-get install -y unminimize` rather than being available by default in all minimal images.

#### Exim4
The Exim4 update in Oracular to 4.98 includes selected fixes from the upstream GIT repository.  This improves handling of new and old format message IDs, fixes certain crashes, refines memory usage for regexes, and avoids recording lookup credentials in the log files.  DKIM DNS record parsing is tightened up related to unexpected whitespace.

#### HAProxy
The HAProxy package was upgraded to version 2.9.9. This new version introduces performance improvements, better integration, more reliability, and a new reverse-http feature. You can learn more about it at https://www.haproxy.com/blog/announcing-haproxy-2-9.  A complete list of changes is avalilable at https://www.haproxy.org/download/2.9/src/CHANGELOG.

#### libvirt
The [libvirt](https://libvirt.org) package was upgraded to version 10.6.0.  Here are the changes since Ubuntu Noble:

  * network: Make virtual domains resolvable from the host.
  * qemu: Support clusters in CPU topology.
  * qemu: Introduce `dynamicMemslots` attribute for `virtio-mem`.
  * qemu: Support for driver type `mtp` in `<filesystem/>` devices.
  * qemu: Introduce `virDomainGraphicsReload` API.
  * qemu: Proper support for USB network device.
  * SSH proxy for VM.
  * Introduce `pstore` device.

For more details, please see [the upstream changelog](https://www.libvirt.org/news.html).

#### Nginx
Version 1.26.0 of NGINX was introduced in Oracular, bringing experimental HTTP/3 support, HTTP/2 on a per-server basis, virtual servers in the stream module, passing stream connections to listen sockets, and more.

#### OpenLDAP
The [OpenLDAP](https://openldap.org/) package was updated to version 2.6.8, which brings several bug fixes. For more details, please see [the upstream changelog](https://www.openldap.org/software/release/changes.html).

#### Openssh
Starting with 1:9.6p1-3ubuntu17, openssh server no longer reads `~/.pam_environment` of the target system upon login.

In [Linux-PAM version 1.5.0](https://github.com/linux-pam/linux-pam/releases/tag/v1.5.0), the
`pam_env.so` module [has deprecated](https://github.com/linux-pam/linux-pam/commit/ecd526743a27157c5210b0ce9867c43a2fa27784) the `user_readenv=1` parameter due to security concerns, and it will be removed by upstream in the future.

Following that change, `/etc/pam.d/sshd`'s invocation of `pam_env.so` [was changed](https://bugs.launchpad.net/ubuntu/+source/openssh/+bug/2059859/) to remove the `user_readenv=1` parameter.

Systems that were relying on that behavior need to adapt, possibly via the openssh `AcceptEnv` (on the server) and `SendEnv` (on the client) parameters.

Note that the default configuration in `/etc/ssh/sshd_config` and `/etc/ssh/ssh_config` is already set to send and receive locale variables, which is one of the scenarios in which `~/.pam_environment` was used in the past.

#### OpenVmTools
The new version 12.4.5 of open-vm-tools in oracular brings a handful of bug fixes; for details of these and existing known issues, please see the upstream release notes for [12.4.0](https://docs.vmware.com/en/VMware-Tools/12.4/rn/vmware-tools-1240-release-notes/index.html) and [12.4.5](https://docs.vmware.com/en/VMware-Tools/12.4/rn/vmware-tools-1245-release-notes/index.html).

#### Valkey
Valkey version 7.2.5 is available in Oracular. Since this version is a drop-in replacement for Redis (fully compatible), and with the [recent changes of Redis' license](https://redis.io/blog/redis-adopts-dual-source-available-licensing/), a way to migrate configuration and data from Redis to Valkey is implemented in a form of a new binary package. The `valkey-redis-compat` binary package will attempt a automatic configuration and data migration from Redis to Valkey. If you did not perform any drastic change to the configuration of your Redis service, it should work straight away.  However, if you performed some substantial changes or your setup is more complex, the automation may not work. Due to that, whenever the `valkey-redis-compat` binary package is installed and the migration is attempted, the file `/etc/valkey/REDIS_MIGRATION` will be created, and the services will not start automatically. This will avoid breaking the upgrade due to an incomplete migration. After the user has checked if the migration is OK, they need to remove the `/etc/valkey/REDIS_MIGRATION` file, then the Valkey services will be able to be started again.

#### Percona Xtrabackup
Xtrabackup was updated to the next minor version 8.0.35-31. It provides additional arm64 architecture support along with various bug fixes. For more details, see the [upstream release notes](https://docs.percona.com/percona-xtrabackup/8.0/release-notes/8.0/8.0.35-31.0.html).

#### PHP
PHP was upgraded to version 8.3.9, which is introduces several bug fixes.  You can read mothe about those in the upstream changelog at https://www.php.net/ChangeLog-8.php#8.3.9.

#### PostgreSQL
PostgreSQL was updated to version 16.4. Users running Ubuntu Noble will realize this version was also included there as part of our PostgreSQL upgrade policies. The new version introduces many bug and security fixes. More details on the changes introduced since Noble are available at https://www.postgresql.org/docs/release/16.4/ and https://www.postgresql.org/docs/release/16.3/

#### QEMU
The [QEMU](https://qemu.org/) package was updated to version 9.0.2. Here are the changes since Ubuntu Noble.

  * The behaviour of the `-serial none` option when used together with     other `-serial` options has been corrected. Previously when `-serial none` was followed by `-serial something` the `-serial none` was effectively ignored. Now it controls the existence of the first serial port, and the following `-serial` option controls the behaviour of the second serial port; this brings it in to line with how all other cases of multiple `-serial` options work. If you have a command line that was accidentally relying on the old behaviour, you can simply delete the unnecessary `-serial none`.
  * ARM
	* New `raspi4b` board type, the Raspberry Pi 4 Model B. Note that QEMU does not yet model PCI or ethernet; this will be implemented on a future QEMU release.
  * RISC-V
    * Add support for `Zacas`, `B`, `Zaamo`, `Zalrsc`, `Ztso` extensions.
    * Add `amocas.[w,d,q]` instructions.
    * `RVA22` profiles support.
    * Add RVV CSRs to KVM.
    * Implement optional CSR `mcontext` of debug `Sdtrig` extension.
    * Enable `xtheadsync` under user mode.
    * Use `zfa` instead of `Zfa`.
    * Move ratified/frozen extensions to non-experimental.
  * s390x
	* Fix access register handling in the emulation of the `LOAD ADDRESS EXTENDED` (`LAE`) instruction.
    * Add emulation of `CVDG`, `CVB`, `CVBY` and `CVBG` instructions.
  * The `virtio-blk` device has gained true multiqueue support where different queues of a single disk can be processed by different I/O threads. This can improve scalability in cases where the guest submitted enough I/O to saturate the host CPU running a single I/O thread processing the `virtio-blk` requests. Multiple I/O threads can be configured using the new `iothread-vq-mapping` property.
  * `usb-storage` doesn't ignore the properties `backend_defaults`, `logical_block_size`, `physical_block_size`, `min_io_size`, `opt_io_size` and `discard_granularity` any more.
  * Fixed `vhost-vdpa-device` to be compatible with `VDUSE` block exports again (this was broken in QEMU 8.2.0, in Ubuntu Noble).
  * Introduced an IOMMU interface backend for VFIO devices.
  * Introduced a new IOMMUFD backend for ARM, amd64 and s390x platforms.
  * The `sm4` cipher algorithm is now supported and can be used with the `luks` block driver.
  * QEMU 8.2 accidentally allowed for creation of memory backends with sizes that are not aligned to the (huge) page size. This has been fixed.
  * Fixed migration for SUSPENDED VM, where we used to ignore the `SUSPENDED` state and kick off the VM even if it was suspended before the migration.
  * New capability called `mapped-ram`. It allows efficient VM snapshots save/load by providing both (1) constant size of ultimate VM image rather than unlimited, and (2) multi-threading support so that save/load of snapshots can be faster.

For more details, please see related upstream changelogs:

  * [9.0](https://wiki.qemu.org/ChangeLog/9.0)

#### Ruby 3.3
The default Ruby version is now version 3.3. Some compatibility changes may arise from the upgrade from version 3.2, they are:

* `it` calls without arguments in a block with no ordinary parameters are deprecated. `it` will be a reference to the first block parameter in Ruby 3.4. [Feature #18980]
* `Regexp::new` now only accepts up to 2 arguments instead of 3. This was deprecated in Ruby 3.2. [Bug #18797]
* Environment variable `RUBY_GC_HEAP_INIT_SLOTS` has been deprecated and is a no-op. Please use environment variables `RUBY_GC_HEAP_{0,1,2,3,4}_INIT_SLOTS` instead. [Feature #19785]

For the complete list of changes in this new version, please check the [upstream release notes](https://www.ruby-lang.org/en/news/2023/12/25/ruby-3-3-0-released/) out.

#### Samba
Samba was updated to 4.20.4, and major changes in the 4.20.x series are documented in the [upstream release notes](https://www.samba.org/samba/history/samba-4.20.0.html).

Normally the point releases of samba in a stable series only contain bug fixes, but this time 4.20.3 added a nice new feature which is LDAP TLS/SASL channel binding support. Details are shown in the [4.20.3 release notes](https://www.samba.org/samba/history/samba-4.20.3.html).

In terms of packaging, the following changes have been done:

  * `samba-vfs-modules`: the VFS modules from this package were moved to the `samba` package, with the exception of the Ceph module, which got its own package: `samba-vfs-ceph`. The `samba-vfs-modules` package is now just a transitional package, and it can be safely removed after the release upgrade.
  * `samba-vfs-modules-extra`: this package used to contain the GlusterFS VFS module. This module was moved to a new package called `samba-vfs-glusterfs`, and `samba-vfs-modules-extra` became a transitional package. It can also be safely removed after the release upgrade.

#### Squid
Squid was upgraded to version 6.10. This new version includes several bug
fixes. A complete set of changes together with a comprehensive changelog
is available at
https://github.com/squid-cache/squid/compare/SQUID_6_6..SQUID_6_10.

#### SSSD
The [SSSD](https://sssd.io/) package was updated to version 2.9.5. Here are the changes since Ubuntu Noble.

  * Added `failover_primary_timeout` configuration option. This can be used to configure how often SSSD tries to reconnect to a primary server after a successful connection to a backup server. This was previously hardcoded to 31 seconds which is kept as the default value.

For more details, please see [the upstream changelog](https://sssd.io/release-notes/sssd-2.9.5.html).

#### Subiquity
A new version of the Subiquity server installer has been released. Please read the full [release notes for 24.04.1](https://github.com/canonical/subiquity/releases/tag/24.04.1) on GitHub.

#### Ubuntu HA/Clustering

##### multipath-tools
multipath-tools was updated to 0.9.9. Please visit https://github.com/opensvc/multipath-tools/blob/master/NEWS.md for notes on the changes.

##### kpartx-boot
Starting with the Oracular release, the kpartx-boot package has been discontinued to align with Debian. Originally introduced to support dmraid booting, its functionality is preserved, as the kpartx package now includes everything previously provided by kpartx-boot.

##### dmraid
The dmraid package has been removed from Oracular. The rationale for its removal is outlined in https://bugs.launchpad.net/bugs/2073677, primarily due to its removal from Debian unstable and minimal upstream support. If you require this functionality, consider using alternatives like mdadm.

##### Corosync
Corosync was upgraded to version 3.1.8. This release contains mostly smaller bugfixes and improvements of Rust bindings. You can learn more about it at https://github.com/corosync/corosync/releases.

##### pacemaker
Pacemaker was upgraded to version 2.1.8. This release includes a significant number of bug fixes and a few new features.  It also deprecates some obscure features and many C APIs in preparation for the next Pacemaker major release which will drop support for them.

##### fence-agents
fence-agents was upgraded to version 4.15.0. In this release, we are no longer shipping the transitional fence-agents package. You should now use either the fence-agents-base package with the agents available in main or the fence-agents-extra package with the agents in universe (or both, they are split based on the repository components they are available in). A complete list of upstream changes for this version is available at https://lists.clusterlabs.org/pipermail/developers/2024-July/003567.html.

##### resource-agents
resource-agents was upgraded to version 4.15.1. This new release introduces several bug fixes and enhancements including two new resource agents: outscale and powervs-subnet. Details on all changes introduced in this new version are available at https://lists.clusterlabs.org/pipermail/developers/2024-July/003570.html and https://lists.clusterlabs.org/pipermail/developers/2024-July/003572.html.

#### OpenStack
OpenStack has been updated to the [2024.2 (Dalmatian) release](https://releases.openstack.org/dalmatian/).  This includes packages for Aodh, Barbican, Ceilometer, Cinder, Designate, Glance, Heat, Horizon, Ironic, Keystone, Magnum, Manila, Masakari, Mistral, Neutron, Nova, Octavia, Swift, Vitrage, Watcher and Zaqar.

This release is also provided for Ubuntu 24.04 LTS via the Ubuntu Cloud Archive.

#### Ceph
[Ceph](http://ceph.com) has been updated to the 19.2.0 (Squid) release.

#### Open vSwitch (OVS) and Open Virtual Network (OVN)
[Open vSwitch](https://www.openvswitch.org/) has been updated to the 3.4.0 release.

[Open Virtual Network](https://www.ovn.org/) has been updated to the 24.09 release.

These releases are also provided for Ubuntu 24.04 LTS via the Ubuntu Cloud Archive.

#### GRUB2

Chainloading of non-NX compatible versions of Windows 10 from UEFI GRUB2 might be broken on a limited subset of machines. This is  being actively investigated but the root cause haven't been found yet. If you are experiencing this, please see the linked bug for updates
https://bugs.launchpad.net/ubuntu/+source/grub2/+bug/2084104.

### Platforms

#### Public Cloud / Cloud images

##### Public Images (cloud-images.ubuntu.com) images

* Release notes/image diff
  * Since 19th April 2024 we have introduced `.image_changelog.json` files to accompany published images @ https://cloud-images.ubuntu.com/. This is a JSON document listing all the package additions, removals and changes as well as noting the changelog entries for the package changes. It also highlights any CVEs addressed in those package updates. The tool used to generate these diffs is `ubuntu-cloud-image-changelog` available @ [github.com/canonical/ubuntu-cloud-image-changelog](http://github.com/canonical/ubuntu-cloud-image-changelog)
  * Diffs are generated between the image being published and the previous daily image, and also between the image being published and the previous release image.
  * These image diffs have been backported to previous published Ubuntu release too.

##### LXD Containers

LXD 24.10 Oracular Oriole containers have a more specific set of requirements for running due to changes in systemd 256.5. Starting in Oracular, systemd services (systemd-resolved, systemd-journald) have migrated to using systemd credentials. This change necessitated changes in LXD to properly run 24.10 Oracular Oriole containers. This change is landed in LXD snap channels latest/stable, 5.21/stable, and 5.0/edge. Release to 5.0/stable is planned in the near future..

Furthermore, there is a strict requirement in systemd 256.5 on cgroups v2. This means that the host operating system must be cgroups v2 enabled. For Ubuntu based hosts, this means that Oracular containers launched by LXD will operate on the following versions:

* 24.04 Noble , all kernels
* 22.04 Jammy Jellyfish, all kernels
* 20.04 Focal Fossa, HWE kernel

If you are running a Focal based host system, and require running Oracular containers, you must install the HWE kernel and ensure that cgroups v2 is enabled. If you are on a system with cgroupsv2 enabled and running on LXD 5.0/stable, it is possible to boot the containers by providing the following in your flag in your launch command

`-c security.nesting=true`

The inverse is also true – when running an older container that lacks cgroup v2 support, you will be unable to launch it on an Oracular host system. This affects anyone attempting to run older Ubuntu suites, from 18.04 Bionic Beaver and back. Note that these suites are in Extended Support, and for security reasons should only be used if they are attached to Ubuntu Pro. If you require running older Ubuntu versions, running inside a virtual machine of an older Ubuntu will guarantee compatibility.

This only affects containers launched with LXD. It does not affect virtual machines.


##### AWS EC2

* `/etc/ec2-version` will only show up on EC2 images

##### Microsoft Azure

* Canonical introduced a new way of publishing on Azure with Ubuntu 24.04 LTS, which will continue for 24.10. All Ubuntu Images for 24.10 will be available under the same offer: `ubuntu-24_10`. Derivative images, such as the minimized version of Ubuntu server are available as plans under this main offer.

* Starting in 24.10 (but also backported to 20.04, 22.04 and 24.04) the values for `net.core.rmem_max` and `net.core.rmem_default` have been increased to 1048576 (the Ubuntu default is 212992). This change will apply to all newly published Ubuntu images published on Azure for the given versions. This increase in the socket receive buffer size was made to reduce UDP packet loss for some workloads.

##### Google

* Resume/suspend issue from noble [LP: #2063315](https://bugs.launchpad.net/ubuntu/+source/linux-gcp/+bug/2063315) is resolved
* TDX support: Ubuntu images now support Confidential VMs with Intel TDX. This capability is advertised by the presence of “TDX_CAPABLE” guest OS feature flag in the image metadata. Intel TDX is now also supported on Ubuntu Jammy and Noble GCE images.

###### How to report any issues resulting from these changes

If you notice any unexpected changes or bugs in the minimal images, create a new bug in [cloud-images](https://bugs.launchpad.net/cloud-images).

#### arm64

The new arm64+largemem ISO includes a kernel with 64k page size. A larger page size can increase throughput, but comes at the cost of increased memory use, making this option more suitable for servers with plenty of memory. Typical use cases for this ISO include: machine learning, databases with many large entries, high performance computing.

#### IBM Z and LinuxONE ![image|32x32](upload://dZM0RRlelqCcZc6RhqJGMW8DMZr.png) 

* The key package 's390-tools' was step-by-step upgraded to latest version v2.34.1 ([LP: #2073786](https://launchpad.net/bugs/2073786)), which incl. lots of updates, new tools and features, especially in the area of ap_tools/ap-check and libap - the skipped v.2.33 brought on top several modification in the Rust code and libutil ([LP: #2067355](https://launchpad.net/bugs/2067355)).
* On top of the usual upgrade of the tool-chain, valgrind was also upgraded to it's latest v2.23, which includes support for IBM z16 hardware ([LP: #1982335](https://launchpad.net/bugs/1982335)).
* With the upgrade of openCryptoki to latest v3.23 ([LP: #2076450](https://launchpad.net/bugs/2076450)), support of protected keys for extractable keys (with EP11 tokens) was introduced ([LP: #2050018](https://launchpad.net/bugs/2050018)).
* And as usual a lot of s390x-specific packages (or package that are of special interest for s390x) got upgraded to it's latest version, like:
  * libzpc to v1.2.0 ([LP: #2076444](https://launchpad.net/bugs/2076444))
  * libzdnn to v1.0.1 ([LP: #2076445](https://launchpad.net/bugs/2076445))
  * qclib to v2.5.0 ([LP: #2076446](https://launchpad.net/bugs/2076446))
  * smc-tools to v1.8.3 ([LP: #2076447](https://launchpad.net/bugs/2076447))
  * openssl-ibmca to v2.4.1 ([LP: #2076448](https://launchpad.net/bugs/2076448))
  * libica to v4.3.0 ([LP: #2076449](https://launchpad.net/bugs/2076449))
* Kernel 6.11 move (via 6.10 code) the kernel image into vmalloc space, where random physical pages are used to map virtual pages ([LP: #2072661](https://launchpad.net/bugs/2072661)).
Even if kernel 6.11 is brand new, a patch set from the next kernel for 'Vertical CPU Polarization Support Stage 2" that esp. provides improved 'cpu capacity' support for the Linux scheduler ([LP: #2072760](https://launchpad.net/bugs/2072760)) was included.

#### IBM POWER (ppc64el)

* KVM running in IBM PowerVM LPARs:
  Ubuntu Server 24.04 has the required technology enablement and support for running KVM in a PowerVM LPAR.
  This technology enables expanded open-source based innovations and solutions for Ubuntu Server on the IBM Power platform.
  Below are the firmware and hardware requirements:
  * Firmware: FW1060.10
  * Hardware: IBM Power10
* KVM virtualization continues to be supported on POWER9 bare-metal / OPAL based systems.
* Ubuntu 24.10 includes so called 'Book3S HV nestedv2' support and fixes.

#### RISC-V

For an overview of supported boards see https://ubuntu.com/download/risc-v.

The RISC-V Ubuntu userland is compatible with all RVA20 hardware.


(24-10-known-issues)=
## Known Issues

As is to be expected with any release, there are some significant known bugs that users may encounter with this release of Ubuntu. The ones we know about at this point (and some of the workarounds) are documented here, so you don't need to spend time reporting these bugs again:

### General

* The Live Session of the new Ubuntu Desktop installer is not localized. It is still possible to perform a non-English installation using the new installer, but internet access at install time is required to download the language packs. ([LP: #2013329](https://bugs.launchpad.net/ubuntu-release-notes/+bug/2013329))
* ZFS with Encryption on Ubuntu 24.10 will [fail to activate the cryptoswap partition](https://bugs.launchpad.net/ubuntu/+source/subiquity/+bug/2084089).  This affects both new installs and upgrades.  We expect to address this post-release with an archive update.
* Some particular hardware (e.g. Thinkpad x201) might have issues ([general freeze](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2084055), [`desktop-security-center` not launching](https://github.com/canonical/desktop-security-center/issues/81)), when booted without `nomodeset` (Safe graphics). Follow these steps if you encounter such an issue:

1. At the GRUB boot menu, press `e` (keep `Shift` pressed during early boot if the menu doesn't show up).
2. Add `nomodeset` to `linux` line, like the example below:
```
linux /casper/vmlinuz nomodeset ---
```
3. Press `Ctrl-x` to continue the boot process
4. After installation is complete, reboot, use `nomodeset` again, like the example below:
```
linux /boot/vmlinuz-6.11.0-8-generic nomodeset root=UUID=c5605a23-05ae-4d9d-b65f-e47ba48b7560 ro
```
5. Add `nomodeset` to the GRUB config file, `/etc/default/grub`, like the example below:
```
GRUB_CMDLINE_LINUX="nomodeset"
```
6. Finally, run `sudo update-grub` to make the change take effect.


### Linux kernel

* A bug prevents the IO scheduler from being reset to "none" ([LP: #2083845](https://bugs.launchpad.net/bugs/2083845)): the fix is already in v6.11.2, and will be part of the first SRU kernel.
* Support for FAN networking has been dropped in the 6.11 release kernel. It will be re-introduced in the next 6.11 kernel update shortly.

### Ubuntu Desktop

* Screen reader support is present with the new desktop installer, but is incomplete ([LP: #2061015](https://launchpad.net/bugs/2061015), [LP: #2061018](https://launchpad.net/bugs/2061018), [LP: #2036962](https://launchpad.net/bugs/2036962), [LP: #2061021](https://launchpad.net/bugs/2061021))

* OEM installs are not supported yet ([LP: #2048473](https://launchpad.net/bugs/2048473))

* Application icons don't use the correct High Contrast theme when High Contrast is enabled [(LP: #2013107](https://launchpad.net/bugs/2013107))

* GTK4 apps (including the desktop wallpaper) do not display correctly with VirtualBox or VMWare with 3D Acceleration ([LP: #2061118](https://launchpad.net/bugs/2061118)).

* **Incompatibility between TPM-backed Full Disk Encryption and Absolute:** TPM-backed Full Disk Encryption (FDE) has been introduced to enhance data security. However, it's important to note that this feature is incompatible with Absolute (formerly Computrace) security software. If Absolute is enabled on your system, the machine will not boot post-installation when TPM-backed FDE is also enabled. Therefore, disabling Absolute from the BIOS is recommended to avoid booting issues.
* **Hardware-Specific Kernel Module Requirements for TPM-backed Full Disk Encryption:** TPM-backed Full Disk Encryption (FDE) requires a specific kernel snap which may not include certain kernel modules necessary for some hardware functionalities. A notable example is the `vmd` module required for NVMe RAID configurations. In scenarios where such specific kernel modules are indispensable, the hardware feature may need to be disabled in the BIOS (such as RAID) to ensure the continued availability of the affected hardware post-installation. If disabling in the BIOS is not an option, the related hardware will not be available post-installation with TPM-backed FDE enabled.
* [FDE specific bug reports](https://bugs.launchpad.net/bugs/+bugs?field.searchtext=&orderby=-importance&field.status%3Alist=NEW&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.tag=fde&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search).

* Some Nvidia desktops perform worse in Wayland sessions than Xorg ([LP#2081140](https://bugs.launchpad.net/bugs/2081140)). To work around this you can select ‘Ubuntu on Xorg’ from the login screen.

* Nvidia hybrid machines that have an external monitor connected to the discrete GPU (usually via the laptop’s HDMI port) may experience lower performance on that monitor in Wayland sessions ([LP#2064205](https://bugs.launchpad.net/bugs/2064205)). To work around this you may:
  - Plug all external monitors into the integrated GPU (such as by USB-C). The discrete GPU can still be used to launch apps.
  - Or select ‘Ubuntu on Xorg’ from the login screen.

* Installing `ubuntu-fonts-classic` results in a non-Ubuntu font being displayed ([LP#2083683](https://bugs.launchpad.net/bugs/2083683)). To resolve this, install `gnome-tweaks` and set ‘Interface Text’ to ‘Ubuntu’.

### Ubuntu Server

#### rabbitmq-server
Certain version hops may be unsupported due to feature flags, raising questions about how Ubuntu will maintain this package moving forward. We are currently exploring the use of snaps as a potential solution to enable smoother upgrades. For more information please read https://bugs.launchpad.net/bugs/2074309.

#### Installer

* In some situations, it is acceptable to proceed with an offline installation when the mirror is inaccessible. In this scenario, it is advised to use:

```
apt:
  fallback: offline-install
```

* Network interfaces left unconfigured at install time are assumed to be configured via dhcp4. If this doesn't happen (for example, because the interface is physically not connected) the boot process will block and wait for a few minutes ([LP: #2063331](https://bugs.launchpad.net/subiquity/+bug/2063331)). This can be fixed by removing the extra interfaces from `/etc/netplan/50-cloud-init.conf` or by marking them as `optional: true`. Cloud-init is disabled on systems installed from ISO images, so settings will persist.

#### samba apparmor profile
Due to [bug LP: #2063079](https://bugs.launchpad.net/ubuntu/+source/samba/+bug/2063079), the samba `smbd.service` unit file is no longer calling out to the helper script to dynamically create apparmor profile snippets according to the existing shares.

By default, the `smbd` service from samba is not confined. To be affected by this bug, users have to:
- install the optional `apparmor-profiles` package
- switch the `smbd` profile confinement from `complain` to `enforce`

Therefore, only users who have taken those steps and upgrade to Noble, will be affected by this bug. An SRU to fix it will be done shortly after release.


#### Docker

There is a AppArmor related bug where containers cannot be promptly stopped due to the recently added AppArmor profile for `runc`. The containers are always killed with `SIGKILL` due to the denials when trying to receive a signal. More details about this bug can be found [here](https://bugs.launchpad.net/ubuntu/+source/docker.io/+bug/2063099), and a workaround is described [here](https://bugs.launchpad.net/ubuntu/+source/docker.io/+bug/2063099/comments/4).

#### PPC64EL

* PMDK sees some hardware-specific failures in its test suite, which may make the software partially or fully inoperable on the ppc64el architecture. ([LP: #2061913](https://bugs.launchpad.net/ubuntu/+source/pmdk/+bug/2061913/))

#### Raspberry Pi

* Raspberry Pi 500 is missing an entry in the flash-kernel database ([LP: #2092216](https://launchpad.net/bugs/2092216))

* Raspberry Pi models with the 2712 D0 stepping (at time of release, only the Pi 5 2GB, but anticipated to become common on other models in future), are incompatible with the version of mesa used by snaps (Firefox, Thunderbird, and the Snap Store). This will be corrected post-release, but users on these models must run `sudo snap refresh` once, prior to launching these applications ([LP: #2082072](https://launchpad.net/bugs/2082072))

* During boot on the server image, if your `cloud-init` configuration (in `user-data` on the boot partition) relies upon networking (importing SSH keys, installing packages, etc.) you *must* ensure that at least one network interface is required (`optional: false`) in `network-config` on the boot partition. This is due to netplan changes to the wait-online service ([LP: #2060311](https://launchpad.net/bugs/2060311))

* The startup sound does not play before the initial setup process, hence users cannot currently rely on hearing this sound to determine if the system has booted ([LP: #2060693](https://launchpad.net/bugs/2060693))

* The seeded totem video player will not prompt users to install missing codecs when attempting to play a video requiring them ([LP: #2060730](https://launchpad.net/bugs/2060730))

* With some monitors connected to a Raspberry Pi, it is possible that a monitor powers off after a period of inactivity but then powers back on and shows a black screen. Investigation into the types of monitors affected is ongoing in [LP: #1998716](https://bugs.launchpad.net/ubuntu/+source/mutter/+bug/1998716).

* With the removal of the `crda` package in 22.04, the method of setting the wifi regulatory domain (editing `/etc/default/crda`) no longer operates. On server images, use the `regulatory-domain` option in the Netplan configuration. On desktop images, append `cfg80211.ieee80211_regdom=GB` (substituting `GB` for the relevant country code) to the kernel command line in the `cmdline.txt` file on the boot partition  ([LP: #1951586](https://launchpad.net/bugs/1951586)).

* The power LED on the Raspberry Pi 2B, 3B, 3A+, 3B+, and Zero 2W currently goes off and stays off once the Ubuntu kernel starts booting ([LP: #2060942](https://launchpad.net/bugs/2060942))

* libcamera support is currently broken; this will be a priority for next cycle and fixes will be SRU'd to noble as and when they become available ([LP: #2038669](https://bugs.launchpad.net/ubuntu/+source/libcamera/+bug/2038669))

* Colours appear incorrectly in the Ubuntu App Centre ([LP: #2076919](https://launchpad.net/bugs/2076919))

* On desktop images, changes in the home directory result in log spam from tracker-miner complaining about lack of landlock ([LP: #2066885](https://launchpad.net/bugs/2066885))

* On desktop images, on some systems the Wayland desktop option does not appear on first boot. Logging in, then logging out results in the default Wayland option being restored

* On server images, re-authentication to WiFi APs when regulatory domain is set result in dmesg spam to the console ([LP: #2063365](https://launchpad.net/bugs/2063365))

#### ARM64 Systems with NVIDIA GPUs

* The current versions of the NVIDIA GPU drivers may cause hangs or crashes ([LP: #2062380](https://launchpad.net/bugs/2062380)). This will be fixed in a future driver update.

#### Google Compute Platform 

Nothing yet.

#### Microsoft Azure

Nothing yet.

#### s390X

Nothing yet.

(24-10-official-flavors)=
## Official flavors

Find the release notes for the official flavors at the following links:

* [Edubuntu Release Notes](https://discourse.ubuntu.com/t/edubuntu-24-10-released/48647)
* [Kubuntu Release Notes](https://kubuntu.org/news/kubuntu-24-10-oracular-oriole-released/)
* [Lubuntu Release Notes](https://lubuntu.me/lubuntu-24-10-oracular-oriole-released/)
* [Ubuntu Budgie Release Notes](https://ubuntubudgie.org/2024/10/ubuntu-budgie-24-10-release-notes/)
* [Ubuntu MATE Release Notes](https://ubuntu-mate.org/blog/ubuntu-mate-oracular-oriole-release-notes/)
* [Ubuntu Studio Release Notes](https://ubuntustudio.org/ubuntu-studio-24-10-release-notes/)
* [Ubuntu Unity Release Notes](https://ubuntuunity.org/posts/ubuntu-unity-2410-released/)
* [Xubuntu Release Notes](https://wiki.xubuntu.org/releases/24.10/release-notes)
* [Ubuntu Kylin Release Notes](https://ubuntukylin.com/news/ubuntukylin2410-en.html)
* [Ubuntu Cinnamon Release Notes](https://ubuntucinnamon.org/?p=1348)


(24-10-more-information)=
## More information

Refer to {ref}`release-policy-and-schedule` and {ref}`project-and-community`.
