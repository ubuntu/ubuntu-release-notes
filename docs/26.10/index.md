---
tocdepth: 3
---

(ubuntu-26.10-release-notes)=
# Ubuntu 26.10 release notes

These release notes cover new features and changes in Ubuntu 26.10 (Stonking Stingray).

For the release schedule of Ubuntu 26.10, refer to the {ref}`release schedule <stonking-stingray-schedule>`.

:::{toctree}
:maxdepth: 1
:hidden:

Release schedule <schedule>
:::

## Support lifespan

Ubuntu 26.10 was released on 15 October 2026. It will be supported for 9 months, until July 2027.

For details, see [Ubuntu release cycle](https://ubuntu.com/about/release-cycle).

## Upgrades

To upgrade from a previous Ubuntu release, refer to the [Ubuntu Desktop](https://ubuntu.com/desktop/docs/en/latest/how-to/upgrade-ubuntu-desktop/) or [Ubuntu Server](https://ubuntu.com/server/docs/how-to/software/upgrade-your-release/) guide.

## New features and improvements

### Desktop features

#### GNOME 51

Highlights across the desktop include:

* **Performance:** many enhancements to bring a smoother, more responsive desktop.
* **Displays** remembers monitor brightness across reboots and HDR changes. Frame scheduling improvements make animations smoother under load, and monitor arrangement uses improved center-aligned snapping.
* **Settings** adds an automatic screen rotation and orientation lock on devices with an accelerometer, improves display arrangement, and can disable the touchpad automatically when a mouse is connected. Network settings now support DNS search domains, and fingerprint enrollment has an improved interface.
* **Files** gives a count when dragging multiple files, improves selection behavior, groups file notifications, and performs some file operations more responsively.
* **Calendar** is more responsive, especially in Month view, and uses less data when syncing.
* **Remote Desktop** supports remote smartcard use and Kerberos authentication. Remote Login also supports SSH socket-activated servers.
* **Papers** can add visual signatures to documents. These are annotations and do not cryptographically verify a document's authenticity.

For more information, see the [GNOME 51 release notes](https://release.gnome.org/51/).

#### Accessibility improvements and fixes

Accessibility has been improved across GNOME, App Center, the desktop shell and the Flutter toolkit.

GNOME 51 comes with many accessibility enhancements:

* The Reduced Motion setting has been extended to more parts of the desktop.
* Users can adjust screenshot selections with the keyboard
* Orca announcements and app-grid navigation have been improved.
* The Accessibility settings gain an option to disable the focus-ring timeout.

#### New desktop wallpapers

Ubuntu 26.10 includes new Stonking Stingray wallpapers, including designs selected through the community wallpaper competition. See the [wallpaper announcement](https://ubuntu.com/blog/grace-on-the-currents-stonking-stingray).

#### Ubuntu Certified hardware status in Settings

Settings can show whether a computer is certified for Ubuntu.

The status is checked using the Ubuntu Hardware API, with caching to avoid unnecessary repeated checks. The `hwctl` client is included as a snap.

For information about hardware data used for certification checks, see the [System Information Notice](https://canonical.com/legal/systems-information-notice#metrics-collected-by-ubuntu-certified-client).

#### A unified app-details view in App Center

App Center now presents Snap and Debian package details in a unified app-details view. It brings information such as the publisher, ratings, permissions, version, package size, screenshots, and description together, with the relevant install, open, or uninstall action.

#### Driver management in App Center

App Center adds a dedicated Drivers page where you can review the available graphics drivers, including NVIDIA driver branches.

Driver choices are presented with clearer metadata to help you compare the options. Available choices depend on the system's hardware and enabled software sources.

#### On-demand multimedia codecs

App Center can install the codecs needed for one-time playback when a media file uses a codec that is not installed. Some high-quality codecs are proprietary and are not included in the default installation.

#### Myna speech-to-text preview

Myna is an early speech-to-text preview for Ubuntu Desktop.

Hold a configurable key to dictate into the focused app. The transcription runs locally, with no audio sent to a network service.

Myna is not preinstalled, and its features may change before stable release.

Read the [Myna technology preview announcement](https://ubuntu.com/blog/myna-speech-to-text-technology-preview-available).

#### TPM-backed FDE without a hardware root of trust

Computers without a hardware root of trust can now be installed with TPM-backed full disk encryption (FDE), provided that a PIN or passphrase is also set on the TPM-backed key.

This was already backported in Ubuntu Desktop 26.04.1. For reference, see [Hardware-backed disk encryption requirements](https://ubuntu.com/desktop/docs/en/latest/reference/hardware-backed-disk-encryption-requirements/).

#### Upgrade support on the horizon for systems running under TPM-backed FDE

While systems running under TPM-backed FDE will not be able to upgrade from Ubuntu 26.04 LTS to Ubuntu 26.10 on release, we anticipate enabling these upgrades during the Ubuntu 26.10 lifecycle.

#### System-level opt-out for Ubuntu Insights

Administrators can now opt out of anonymous Ubuntu Insights system report collection for the entire system. Enabling the configuration overrides individual opt-ins such that they are instead interpreted as opt-outs. Users with sufficient permissions can change this setting, either in the Settings application or by using Ubuntu Insights' command-line interface.

#### New window tiling interface

Ubuntu Desktop now shows a new popup when dragging a window to offer tiling layout options. ([ubuntu/Tiling-Assistant#451](https://github.com/ubuntu/Tiling-Assistant/issues/451))

#### D-Bus is now provided by `dbus-broker`

D-Bus is a message bus that lets processes communicate on a Linux system. The default D-Bus implementation has changed from `dbus-daemon` to `dbus-broker`.

Both the system bus and the per-user session bus are now provided by `dbus-broker`.

Thanks to its asynchronous, event-driven architecture, `dbus-broker` offers better accounting, reliability and scalability than `dbus-daemon`.

For details, refer to [Ubuntu 26.10 is switching to dbus-broker](https://discourse.ubuntu.com/t/ubuntu-26-10-is-switching-to-dbus-broker/84060).

### Server features

#### FreeRADIUS 3.2.10

The FreeRADIUS software was updated to version 3.2.10. Highlights include:

 * Initial implementation of Protocol-Failure as per IETF draft
 * Suppress secrets by default in new installations (`supress_secrets=true`)
 * Many other improvements and bug fixes.

Please refer to the [FreeRADIUS release notes](https://www.freeradius.org/release_notes/) for more details.

#### FRRouting 10.7.1

The FRRouting (`frr`) software was updated to version 10.7.1. Highlights include:

 * BFD authentication with keychain support (10.7.0)
 * BGP IPv6 VTEP support for EVPN (10.6.0)
 * BGP graceful restart for EVPN (10.6.0)
 * And many more improvements and bug fixes.

Refer to the respective release notes for more information:

 * [FRRouting 10.7.0 release notes](https://frrouting.org/release/10.7.0/) and [FRRouting 10.7.1 release notes](https://frrouting.org/release/10.7.1/)
 * [FRRouting 10.6.0 release notes](https://frrouting.org/release/10.6.0/) and [FRRouting 10.6.1 release notes](https://frrouting.org/release/10.6.1/)

#### HAProxy 3.4.2

[HAProxy](https://launchpad.net/ubuntu/+source/haproxy) jumped two feature releases, from 3.2 to upstream version 3.4.2. HAProxy 3.4 is an LTS branch, supported upstream until 2031-Q2.

Some defaults were changed:

* The default load balancing algorithm changed from `roundrobin` to `random` (power of two choices).
* `cpu-policy` now defaults to `performance`, and the number of threads is no longer capped at 64.
* Backends in `mode http` now enable `option abortonclose` by default.

See the [HAProxy 3.3](https://www.haproxy.com/blog/announcing-haproxy-3-3) and [HAProxy 3.4](https://www.haproxy.com/blog/announcing-haproxy-3-4) announcements for the complete list of changes.

#### iPXE 2.0.0

[iPXE](https://launchpad.net/ubuntu/+source/ipxe) was updated from `1.21.1+git` to 2.0.0. Highlights of [changes](https://github.com/ipxe/ipxe/blob/master/CHANGELOG.md):
 * support UEFI secure boot
 * support RISC-V and LoongArch64
 * download & boot `autoexec.ipxe`
 * EAPoL, port authentication, LLDP, initrd-style CPIO, DHC/ECDHE kex, GCM cipher, X25519, P-256/P-384 EC, ECDSA certs
 * dynamically created interactive forms
 * many new device drivers
 * reproducible builds

#### `libp11` 0.4.20

[`libp11`](https://launchpad.net/ubuntu/+source/libp11) was updated from 0.4.18 to upstream version 0.4.20. Highlights include:

 * Post-quantum cryptography support (ML-DSA, SLH-DSA, and FALCON key generation, signing, and verification).
 * OpenSSL 4.x support and a more complete PKCS#11 provider.
 * Memory-safety and concurrency fixes.
 * And many other improvements and bug fixes.

See the [0.4.19](https://github.com/OpenSC/libp11/releases/tag/libp11-0.4.19) and [0.4.20](https://github.com/OpenSC/libp11/releases/tag/libp11-0.4.20) upstream release notes for full details.

#### Postfix 3.11.7

Postfix in Ubuntu Server 26.10 has been updated to version 3.11.7.

Several tools now support JSON output: `postconf`, `postalias`, `postmap`, and `postmulti`.

See the [Postfix 3.11.0 announcement](https://www.postfix.org/announcements/postfix-3.11.0.html) for the full list of changes.

#### Samba 4.24.7

Samba in Ubuntu Server 26.10 has been updated to version 4.24.7. Important changes include:

 * New audit logging classes for some Active Directory attributes.
 * `vfs_streams_xattr` can hold larger streams.
 * Support for remote password management for Entra ID SSPR and Key cloak.
 * Kerberos PKINIT KeyTrust logon support.
 * Support for Windows Strong and Flexible key mappings as outlined in KB5014754: Certificate-based authentication changes on Windows domain controllers.
 * Domain encryption types changed to AES by default.
 * And many other improvements and bug fixes.

Please see the [Samba 4.24.0 release notes](https://www.samba.org/samba/history/samba-4.24.0.html) for the full list of changes.

#### MySQL

MySQL was updated from 8.4 LTS to 9.7 LTS, starting with 9.7.2. This is MySQL's latest long term support release, including new features such as the Hypergraph Optimizer, full JSON Duality Views support, and the Telemetry component.

Upstream release notes are available in the [Mysql 9.7 documentation library](https://dev.mysql.com/doc/relnotes/mysql/9.7/en/). For more information about the transition from MySQL 8.4 to 9.7, see the [MySQL 9.7 overview](https://dev.mysql.com/doc/refman/9.7/en/mysql-nutshell.html).

The `mysql_native_password` authentication plugin has been removed upstream. If
you previously enabled it in your MySQL server configuration (for example by
adding `mysql_native_password=ON` under `[mysqld]` in
`/etc/mysql/mysql.conf.d/mysqld.cnf`, as suggested in the 26.04 release notes),
remove that entry and migrate any accounts that still use the plugin before
upgrading:

```
    ALTER USER 'user'@'host' IDENTIFIED WITH 'caching_sha2_password' BY 'password';
```

The Ubuntu release upgrader will detect accounts or a configuration still using
`mysql_native_password` and block upgrading until this migration is done.

Note that adding `mysql_native_password=ON` while still on Ubuntu 24.04 LTS or
25.x will prevent MySQL 8.0 from restarting; apply the workaround only on
26.04 or later, and prefer migrating accounts instead.


#### MySQL Shell

MySQL Shell was updated to 9.7.1 to support the new MySQL LTS version. See the [upstream release notes](https://dev.mysql.com/doc/relnotes/mysql-shell/9.7/en/) for more information.

#### Valkey

Valkey was updated to the latest major release 9.1, starting with 9.1.2. This includes various performance and security threat model improvements.

For more information on the new version, see the [Valkey 9.1 blog post](https://valkey.io/blog/valkey-9-1-delivers-improvements-in-security-performance-and-more/). Release notes are available on the [Valkey project GitHub](https://github.com/valkey-io/valkey/releases).

#### ssl-cert 1.2.0

`ssl-cert` is a simple wrapper around OpenSSL. It provides the
`make-ssl-cert` helper script and generates the "snakeoil" self-signed
TLS certificate/key pair (`/etc/ssl/certs/ssl-cert-snakeoil.pem` and
`/etc/ssl/private/ssl-cert-snakeoil.key`) used by services that need a
default certificate out of the box (e.g. Apache, Postfix, Dovecot). It
also manages the `ssl-cert` system group that grants read access to
private keys.

 * Increased the default generated key length from 2048 to 3072 bits, while leaving existing
   2048-bit keys untouched.
 * Allowed separate key/cert file paths even outside the `generate-default-snakeoil` mode.
 * Added the ability to override the certificate's CN and SubjectAltName from the command line.

#### net-snmp 5.9.5.2

`net-snmp` provides the suite of applications used to implement the Simple
Network Management Protocol (SNMP v1, v2c, v3), including `snmpd` (the
agent/daemon), `snmptrapd` (trap receiver), command-line query tools
(`snmpget`, `snmpwalk`, etc.), and the development libraries (`libsnmp-dev`)
used by monitoring software to query and manage network devices and hosts.

- **snmplib**
  - Added support for `IPV6_RECVPKTINFO`.
  - Ported the SSH domain transport to FreeBSD.
- **MIBs**
  - `EtherLike-MIB`: optimized the Linux implementation to use netlink
    statistics.
  - `LM-SENSORS-MIB`: added support for negative temperatures.
  - `SNMP-TLS-TM-MIB`: updated to RFC 9456 and allowed TLS protocols higher
    than TLS 1.0.
  - `HOST-RESOURCES-MIB`: added support for RPM SQLite DB background.

#### rdma-core 64.0

`rdma-core` provides the userspace components for the Linux RDMA
(Remote Direct Memory Access) subsystem used to configure and use
InfiniBand/RoCE/iWARP networking and storage (NVMe-oF, SRP, etc.) devices.

- **mlx5 provider**
  - Added DMA-buf heap and Confidential-Computing (CoCo) shared-memory
    allocation support, including a new internal DMA-buf heap allocator
    library in `libibverbs` and per-buffer dmabuf UMEM attribute
    passthrough to the kernel.
  - Introduced `mlx5dv_devx_uar_export_dmabuf_fd()` and DM export DMABUF
    fd support.
  - Enabled ST64B for BlueFlame writes (with aarch64 `mmio_memcpy_x64`
    support).
- **bnxt_re provider**: added support for QP rate limiting
  (`ibv_modify_qp_rate_limit`) and reporting of rate-limit capabilities.
- **efa provider**: added a new completion status for feature mismatch;
  added QP generation to the device request ID; removed unused `cur_qp`
  caching in `efa_poll_sub_cq`.
- **mana provider**: added Unreliable-Connection (UC) QP support, robust
  `udata` handling, and fixed lost CQ notifications when re-arming
  without polling (the `cqid-check` fix that Ubuntu had carried as a local
  patch in 61.0-2ubuntu3 is included upstream as of 63.0-1).
- **ionic provider**: fixed `sq_sig_all` handling for signaled
  completions.
- **pyverbs**: numerous enhancements — WR property getters, ParentDomain
  CC unprotected allocation, CoCo DMA bounce device capability flag,
  `ibv_buf` provider-aware buffer support, fixed a `MREx.close()`
  deallocation crash, replaced unsafe `WeakSet.pop()` usage, and other
  cleanup/robustness fixes.
- **rc_pingpong**: added unprotected memory allocation for CoCo guests,
  buffer-allocation ordering fix, and preference for IPv6 wildcard when
  binding the control channel.

#### libmail-dmarc-perl 1.20260306

`libmail-dmarc-perl` is a Perl implementation of DMARC (Domain-based Message
Authentication, Reporting and Conformance). It is used by MTAs and filtering
tools (e.g. SpamAssassin) to:

- Validate that incoming messages align with the purported sender's SPF/DKIM
  policy (`Mail::DMARC::PurePerl->validate`).
- Receive, store and view DMARC aggregate/forensic reports from other mail
  servers (report store with SQLite/MySQL/PostgreSQL backends, CLI, and web
  viewers).
- Send DMARC reports to author domains as an MTA operator.

Between Ubuntu 26.04 LTS (Resolute Raccoon) and Ubuntu 26.10 (Stonking Stingray), `libmail-dmarc-perl` moved from upstream
`1.20250805` to `1.20260306`, bringing new report-handling robustness
(gzip/zip ingestion, error-tolerant archive parsing), a modernized web
reporting UI (DataTables), new filtering/CLI options for `dmarc_view_reports`,
and a new SQLite-MySQL migration helper.

- New `dmarc_sqlite_to_mysql` migration script.
- MySQL: enable SSL for newer MySQL; fixed schema for new imports.
- `dmarc_receive`: `eval` `unzip`/`ungzip`, so imperfect archives no longer interrupt
  the processing loop.
- `dmarc_receive`: support for gzip, zip, and XML report files (#277).

#### strongswan 6.0.7

`strongswan` is a complete, open-source **IKEv1/IKEv2 IPsec** implementation
for Linux (and other UNIX-like systems). It provides the `charon` and
`starter` daemons, the `swanctl`/`ipsec` command-line tools, and a large set
of plugins (EAP methods, PKCS#7/PKCS#11, X.509, RADIUS, TNC, etc.) used to
build site-to-site VPNs, remote-access VPNs, and host-to-host IPsec
connections.

- Added support for forwarding certain ICMP errors on Linux 6.9+ even when
  the source address doesn't match traffic selectors.
- `dhcp` plugin now tracks leases across make-before-break
  reauthentications.
- `charon-cmd` gained childless IKE SA initiation and IKEv2 PSK
  authentication support.
- **6.0.6**
  - Fixed CVE-2026-35328 (libtls `supported_versions` → infinite loop).
  - Fixed CVE-2026-35329 (pkcs7/libstrongswan encrypted PKCS#7 → crash).
  - Fixed CVE-2026-35330 (libsimaka EAP-SIM/AKA attributes → infinite
    loop/heap overflow, potential RCE).
  - Fixed CVE-2026-35331 (constraints plugin: certificates violating X.509
    name constraints could be accepted).
  - Fixed CVE-2026-35332 (libtls ECDH public values on TLS < 1.3 → crash).
  - Fixed CVE-2026-35333 (libradius RADIUS attributes → infinite
    loop/out-of-bounds read).
  - Fixed CVE-2026-35334 (gmp plugin RSA decryption → crash).
  - Made Botan RNG types configurable in the botan plugin.
- **6.0.7**
  - Fixed CVE-2026-47895 (libstrongswan identity cloning → double-free,
    potential RCE).
  - Validity of pre-trusted self-signed certificates (and the last
    certificate in an incomplete trust chain) is now enforced.
  - `list-conn` event now includes IKE/IPsec proposals.
  - New `--ike` filter option for `swanctl --list-conns`.
  - Enabled mixed-family IPComp configs on Linux 6.3+.

#### Subiquity 26.10

The Subiquity Ubuntu installer has been updated to version 26.10. New features include the following:

- New `/boot` storage requirements in preparation for signed GRUB
- Experimental TPM/FDE use-gap support (development feature)
- New `accepted-errors` autoinstall directive for TPM/FDE installations
- Support for the `no-hardware-root-of-trust` `snapd` error kind
- Btrfs resize support
- Multi-layout keyboard configurations now documented

For details, bug fixes, and known issues, refer to the [26.10 release notes](https://github.com/canonical/subiquity/releases/tag/26.10) post on GitHub.

#### edk2 2026.05

`edk2` is the open-source reference implementation of UEFI/PI firmware. In Ubuntu it provides the `ovmf`
family of virtual-machine firmware packages (`ovmf`, `ovmf-generic`, `ovmf-legacy`,
`ovmf-amdsev`, `ovmf-inteltdx`), architecture-specific QEMU firmware
(`qemu-efi-aarch64`, `qemu-efi-riscv64`, `qemu-efi-loongarch64`), and standalone UEFI shells
(`efi-shell-x64`, `efi-shell-aa64`, `efi-shell-riscv64`, `efi-shell-loongarch64`). These are
used as firmware for QEMU/KVM and confidential-computing (AMD SEV-SNP, Intel TDX) virtual
machines.

* `OvmfPkg/PlatformPei`: do not enable S3 support for confidential VMs.
  - `OvmfPkg/BaseMemEncryptSevLib`: treat IGVM data HOB ranges as prevalidated.
  - `OvmfPkg/IgvmSecureBootDxe`: do not return early with CustomMode enabled.
  - `OvmfPkg/PlatformInitLib`: add `SoftReserved` memory type support; redefine
    low memory; reserve the IGVM parameter area.
  - `OvmfPkg/IntelTdx`: add a toggle to disable the firmware UI; README fix for
    the build command.
  - `OvmfPkg`: set `PcdRequireSelfSignedPk` to `FALSE`; flip the default for
    `EnableLegacyLoader` to false in `X86QemuLoadImageLib`; page-align DXE/UEFI
    driver image sections; disable lockbox functionality for StandaloneMm;
    enable memory debug log for AmdSev and Microvm.
  - `UefiCpuPkg, MdeModulePkg, OvmfPkg`: use 256 IDT descriptors in SEC/PEI/SMM.
* **LoongArch64**: `OvmfPkg/LoongArchVirt` gained Secure Boot support, FPDT
  enablement, a fix for misuse of `ExtractGuidedSectionLib`, and moved
  `FirmwarePerformancePei` to the PEI driver region; LoongArch64 support was
  also extended to `BaseRngLib`, `EmbeddedPkg`, `NetworkPkg` RNG mapping,
  `RedfishPkg`, and `MdePkg` IOVT structures; exception-handling/vector fixes
  in `UefiCpuPkg`.
* **ArmVirt**: increased firmware size; `ArmPlatformLibQemu` now supports an
  early ID map on LPA2-capable CPUs (the fix Ubuntu's earlier LPA2 reverts
  were waiting for); `ArmVirtQemu` exposes `DEBUG_TO_MEM` as a build option;
  bug fixes for ArmVirtKvmtool guest firmware (Arm CCA v5 s1).
* **Security hardening** (`SecurityPkg`, `BaseTools`, `NetworkPkg`):
  - `BaseTools`: fixed potential security issues in `VfrCompiler` and others.
  - `SecurityPkg/Tcg2Smm`: hardened NVS/SMI state initialization.
  - `SecurityPkg/AuthVariableLib`: handle empty signature lists.
  - `SecurityPkg`: fixed `Tcg2SubmitCommand` behavior in TPM field-upgrade and
    general scenarios; fixed a TPM-over-FFA ACPI table endianness error;
    updated bundled `libspdm` to 3.7.0.
  - A new **software TPM library** was introduced in `TcgTpmPkg` for
    software-based TPM implementations.

#### libvirt 12.6.0

libvirt is a toolkit and daemon for managing virtualization platforms. It provides
a stable API, the `virsh` CLI and `libvirtd`/modular daemons. Its main drivers are
QEMU/KVM, LXC, Xen, Cloud Hypervisor, and others. Features include storage pools,
virtual networks, live migration, snapshots, and security confinement (AppArmor, SELinux).

* The QEMU driver is dropped on 32-bit architectures, since they are no longer supported
  as QEMU 11.0 hosts.
* Group-based socket access is **dropped**. Ubuntu now follows the upstream/Debian default
  of **polkit**. `d/NEWS` documents the migration.
* libvirt's secrets are now encrypted. A new one-shot systemd service is created to
  provision the encryption keys. On upgrade, the existing non encrypted secrets are still
  available but remain non encrypted.

#### qemu 11.0

QEMU is a generic machine emulator and virtualizer. With KVM it runs guests at near-native speed.
It also offers full system emulation for many architectures (x86, ARM, RISC-V, s390x, ppc64, ...)
and user-mode emulation. The packages include `qemu-system-*`, `qemu-utils` (qemu-img, qemu-nbd),
`qemu-guest-agent` and `qemu-block-extra`.

* 32-bit host builds are dropped (armhf, i386). Only 64-bit hosts are supported.
  This cause the removal of qemu-system and qemu-user packages on 32-bits.
* `qemu-system-microblazeel` is removed. `qemu-system-microblaze -M endianness=big/little` replaces it.
* `ipxe-qemu` and `seabios` are now `Depends` of every `qemu-system-ARCH`.
* Dropped the dependency on deprecated `edk2` armhf firmware.

#### rabbitmq-server 4.3.2

RabbitMQ is an open-source message broker written in Erlang/OTP. It supports AMQP 0-9-1 and
AMQP 1.0, and also MQTT, STOMP and streams (through plugins).

* Migrated to Erlang 29
* Initial Support for AMQP 1.0 Filter Expressions
* Mnesia and Parition Handling Strategies are Removed
* Classic Queues v1 Storage (CQv1) is Removed

#### dovecot 2.4.4

Dovecot is a secure, high-performance IMAP and POP3 mail server. It supports Maildir/mdbox storage,
Sieve filtering (Pigeonhole) and LMTP delivery. It also has full-text search (FTS) plugins,
many authentication backends (PAM, SQL, LDAP, Lua, GSSAPI), and TLS. The packages
include `dovecot-core`, `dovecot-imapd`, `dovecot-pop3d`, `dovecot-sieve`, `dovecot-managesieved`,
`dovecot-lmtpd` and the database driver plugins.

* There are experimental features in 2.4, one is enabled with --enable-experimental-mail-utf8,
and another with --enable-experimental-imap4rev2, and you also need to set
mail_utf8_extensions=yes and imap4rev2_enabled=yes to enable them in config.
* `login` is no longer part of the default `auth_mechanisms`.
* Improve UTF-8 support for mail storage.
* auth: Add default auth-token UNIX socket for token-based authentication.
* lib-sql: Support parameterized queries.
* lmtp: Support XCLIENT DESTADDR and DESTPORT
* pop3-login: proxy - Add support for XCLIENT DESTIP and DESTPORT
* submission-login: proxy - Add support for XCLIENT DESTIP and DESTPORT

### exim4 4.99.4

Exim is a mail transfer agent (MTA) for Unix systems. It is highly configurable, with
a flexible ACL and routing language. It supports TLS, DKIM, DMARC, PROXY protocol,
SMTP AUTH, and lookups in SQL/LDAP/DBM backends. Debian and Ubuntu package it as
`exim4-base`, `exim4-config`, `exim4-daemon-light`, `exim4-daemon-heavy`, the new
`exim4-daemon-mod` and `exim4-dev`.

 * **4.99.2** fixes CVE-2026-40684, CVE-2026-40685, CVE-2026-40686 and CVE-2026-40687.
  These are a musl DNS crash, OOB read/write on JSON, UTF-8 and SPA authenticator input.
* **4.99.3** fixes CVE-2026-45185, a use-after-free in GnuTLS BDAT/CHUNKING.
  The same release includes the earlier fix for a one-byte write into a freed buffer (LP: #2152202).
* **4.99.4** fixes CVE-2026-48840, an uninitialised-stack disclosure in the PROXYv2 parser.

### Development features

#### Toolchain upgrades

| Toolchain | Version | Notes |
|-----------|---------|-------|
| GCC 🐄 | 15.2.0 | Includes latest patches for the GCC 15 series as well as support for C++ modules. [Release Notes](https://gcc.gnu.org/gcc-15/changes.html) |
| .NET 🦄 | 10.0.112 | Updated .NET runtimes with latest security fixes and toolchain capabilities. [Release Notes](https://github.com/dotnet/core/blob/main/release-notes/10.0/10.0.12/10.0.112.md) |
| Go 🐀 | 1.27 | Go 1.27 supports for generic methods and GODEBUG settings. [Release Notes](https://go.dev/doc/go1.27) |
| LLVM 🐉 | 22.1.8 | LLVM 22 adds support for newer Arm, RISC-V, and x86 CPUs and extensions, improves vectorization and ThinLTO, expands WebAssembly debugging in LLDB, and updates LLVM IR and APIs with some compatibility-breaking changes. [Release Notes](https://releases.llvm.org/22.1.0/docs/ReleaseNotes.html) |
| OpenJDK ☕ | 25.0.4 | OpenJDK release with many stability improvements and patches. [Release Notes](https://mail.openjdk.org/archives/list/jdk-updates-dev@openjdk.org/thread/BRREMPN6BLLC2CYAKLXGRHHNMCIQQSR5/) |
| Python 🐍 | 3.14.7 | Python 3.14.7 is the seventh maintenance release of 3.14, containing numerous bugfixes and improvements. [Release Notes](https://www.python.org/downloads/release/python-3147/) |
| Rust 🦀 | 1.97.1 | Rust 1.97 stable toolchain with LLVM miscompilation fixes. [Release Notes](https://blog.rust-lang.org/2026/07/16/Rust-1.97.1/) |
| Zig ⚡ | 0.16 | Zig is a general-purpose programming language and toolchain for maintaining robust, optimal, and reusable software. [Release Notes](https://ziglang.org/download/0.16.0/release-notes.html)|

#### OpenJDK

- OpenJDK 27 is available in the `openjdk-27` package.
- Ubuntu OpenJDK [JRE](https://hub.docker.com/r/ubuntu/jre) and [JDK](https://hub.docker.com/r/ubuntu/jdk) rock images are available for OpenJDK 25.

### Enterprise features

#### authd 0.7.1

- Users can now [sign in with their Microsoft Entra ID password](https://discourse.ubuntu.com/t/microsoft-entra-id-password-and-mfa-sign-in-comes-to-ubuntu/88342) and complete the MFA challenge on the desktop, in terminal and SSH sessions, and in Polkit dialogs using Microsoft Authenticator approvals or one-time codes from authenticator apps. See how to [enable the new Entra authentication flow](https://ubuntu.com/docs/authd/stable-docs/howto/configure-authd/?broker=msentraid#ref-config-auth-flows).
- The new Entra authentication flow also supports passwordless sign-in with FIDO2 security keys, Microsoft Authenticator or Temporary Access Passes.
- New [`authctl` commands](https://ubuntu.com/docs/authd/stable-docs/reference/cli/) were added to change a user's home directory, change their login shell, and delete users and groups.
- New [how-to guides](https://ubuntu.com/docs/authd/stable-docs/howto/index-user-management/) cover common user management tasks, such as onboarding, locking, offboarding and local password changes.
- The GNOME keyring unlocks automatically at login.
- authd identifies local accounts by a stable provider ID instead of the email address.
- Broker configuration checks reject unknown settings and unsafe file permissions, while configurations from earlier releases keep working.
- When the broker fails to start, logins fail immediately with an actionable message instead of a long timeout.
- Managed users stay visible on the desktop login screen after reboot.
- Administrators can configure delays after failed authentication per PAM service in `/etc/authd/authd.yaml`.

#### ADSys 0.17.0

- Machines can now enroll certificates [directly against Active Directory Certificate Services](https://ubuntu.com/docs/adsys/latest/how-to/certificates/) over LDAP and MS-ICPR. The client no longer needs certmonger or CEPCES, and the Windows server needs no Certificate Enrollment web service.
- Added `adsysctl certificate` commands to inspect and manage enrolled certificates; `verify --online` performs a best-effort revocation check.
- Added [dynamic placeholders](https://ubuntu.com/docs/adsys/latest/explanation/dynamic-values/), such as `${USER}`, `${HOSTNAME}` or `${DOMAIN}`, to GPO values, expanded locally when the policy is applied.
- The Global Catalog is now queried for group membership, so policies apply to users and computers in groups from another domain of the forest, such as Enterprise Admins in the forest root.
- dconf policies are restored for users logging in with their short name when SSSD is configured with `use_fully_qualified_names = False` ([LP: #2107971](https://bugs.launchpad.net/ubuntu/+source/adsys/+bug/2107971)), and `dconf update` failures that leave the policy databases missing or stale are now reported rather than silently ignored; a broken database outside ADSys only logs a warning and does not block AD logins.
- Fall back to the next server in the SSSD `ad_server` list when a domain controller is unreachable, so GPO lookups succeed.
- Apply scripts and AppArmor profiles authored on Windows with CRLF line endings or a UTF-8 BOM.
- Reject unsupported Kerberos credential cache types, such as `KCM:` or `KEYRING:`, with a clear error instead of treating them as file paths.
- Allow greeter sessions running as a dynamic user, and keep the greeter's vendor defaults.
- Match certificate auto-enrollment settings case-insensitively, so GPOs that store the registry keys with a different casing are no longer silently ignored ([LP: #2169074](https://bugs.launchpad.net/ubuntu/+source/adsys/+bug/2169074)).
- Retry policy scripts the kernel still reports as busy, so they are no longer skipped.
- Fixed a deadlock that could hang `adsysctl service cat` and the daemon output forwarding.
- Added the missing `python3-requests` dependency for the CEPCES certificate enrollment script.
- Install binaries, systemd units and the PAM module in their canonical `/usr` locations instead of the aliased `/sbin` and `/lib` directories ([LP: #2139162](https://bugs.launchpad.net/ubuntu/+source/adsys/+bug/2139162)).

### Cloud features

* GCE minimal images no longer have recommends installed, making them even smaller.
* OKE (Oracle Kubernetes Engine) 1.36 support added.
* AppArmor feature support added for 7.2 and 7.3 kernels ([LP: #2167455](https://bugs.launchpad.net/ubuntu/+source/livecd-rootfs/+bug/2167455) and [LP: #2168878](https://bugs.launchpad.net/ubuntu/+source/livecd-rootfs/+bug/2168878)).

### Security features

#### An oxidized OpenPGP

Ubuntu 26.10 adopts the Rust-based Sequoia PGP into the main archive,
providing an officially supported, modern, and memory-safe OpenPGP
implementation.

The goal is for Sequoia PGP to become Ubuntu's default OpenPGP toolchain, with
`sq` and `sqv` serving as counterparts to the traditional `gpg` and `gpgv`
utilities, respectively. By adopting Sequoia, Ubuntu can maintain OpenPGP
interoperability while moving its core implementation toward a more
maintainable and memory-safe foundation.

:::{note}
`gpg` and `gpgv` are still available in the main repository as of Ubuntu 26.10.
:::

#### OpenSSL 4

OpenSSL 4 introduces Encrypted Client Hello (ECH), expanded QUIC support, continued post-quantum cryptography improvements, and further API and architectural cleanup. It also includes various security and bug fixes through the 4.0.3 release, along with improved support for modern TLS features and hardware.

See the [4.0.0](https://github.com/openssl/openssl/releases/tag/openssl-4.0.0), [4.0.1](https://github.com/openssl/openssl/releases/tag/openssl-4.0.1), [4.0.2](https://github.com/openssl/openssl/releases/tag/openssl-4.0.2), and [4.0.3](https://github.com/openssl/openssl/releases/tag/openssl-4.0.3) upstream release notes for full details.

### Hardware support features

#### Support for new RISC-V platforms

Ubuntu 26.10 introduces official support for multiple RVA23 RISC-V platforms:

- The SpacemiT K3 boards (Pico-ITX, CoM260 kit)
- The SiFive BigSky platform

Documentation on how to install on the SpacemiT K3 boards is available: <https://ubuntu.com/hardware/docs/boards/how-to/ubuntu_supported/spacemit-k3/>.

Ubuntu Desktop and Xubuntu Minimal RISC-V desktop images are provided with support for the SpacemiT K3 and QEMU.

#### Improvements in IBM Z and LinuxONE support

Early IBM Z (s390x) core platform operations for `s390-tools` receive critical updates with Secure Execution (SEL) instrumentation. An SEL `initramfs` image can now be customized during early boot ([LP: #2139601](https://launchpad.net/bugs/2139601)), supported by a new tool to build basic SEL-`qcow2` images ([LP: #2139602](https://launchpad.net/bugs/2139602)). Memory operations were also improved with `s390`/`sclp` architectural support for dynamic configuration and deconfiguration of hot-pluggable memory ([LP: #2142862](https://launchpad.net/bugs/2142862)).

Updates have been landed to modernize I/O architectures and hardware monitoring telemetry on the IBM Z platform. This introduces support for new PCI adapter notification actions for Spyre and NVMe storage subsystems ([LP: #2160042](https://launchpad.net/bugs/2160042)). Storage tracking accuracy is reinforced by adding NVMe SMART data health monitoring protocols directly into the background `zpcimon` management service within `s390-tools` ([LP: #2160048](https://launchpad.net/bugs/2160048)).

The IBM Z security architecture has been enhanced with Quantum-Safe cryptography optimizations. Namely, the openCryptoki infrastructure brings robust PKCS #11 V3.2 specification coverage across multiple tokens:

Soft token
: Introduces full support for ML-DSA and ML-KEM schemes ([LP: #2160146](https://launchpad.net/bugs/2160146))

EP11 token
: Integrates ML-DSA and ML-KEM algorithms ([LP: #2160204](https://launchpad.net/bugs/2160204))

CCA token
: Introduces formal cryptographic support for ML-DSA ([LP: #2160205](https://launchpad.net/bugs/2160205))

Underlying low-level cryptographic libraries have been advanced too: `libica4` has migrated to version 4.4.2 ([LP: #2160677](https://launchpad.net/bugs/2160677)). Concurrently, the runtime ecosystem for protected cryptographic keys sees significant structural packaging and utility evolution:

- The new `zpckey` management utility orchestrates Ultravisor (UV) retrievable secrets directly within the local `zpc` provider ([LP: #2160140](https://launchpad.net/bugs/2160140)).
- `libzpc` (version 1) was updated to the latest branch ([LP: #2160138](https://launchpad.net/bugs/2160138)).
- At the same time the next generation `libzpc2` library ([LP: #2160132](https://launchpad.net/bugs/2160132)) with provider support was added.

The `virt-stack` gains performance resilience, architecture agility, and hardening protocols. Secure execution benefits from Quantum Safe SE Header modifications and localized tooling integrations across both the `s390-tools` utility space ([LP: #2160225](https://launchpad.net/bugs/2160225)) and the base Linux kernel subsystem ([LP: #2160226](https://launchpad.net/bugs/2160226)). Virtualization performance features also gain the VSIE SIGP Interpretation Facility inside KVM environments ([LP: #2160277](https://launchpad.net/bugs/2160277)), architectural memory mapping extensions allowing KVM to host 4K memslots natively ([LP: #2163132](https://launchpad.net/bugs/2163132)), and core SWIOTLB bounce-buffer optimization enhancements for `virtio-ccw` channel I/O frameworks ([LP: #2163133](https://launchpad.net/bugs/2163133)).

### System features

#### Linux kernel 7.3 🐧

Ubuntu 26.10 ships with the Linux kernel 7.3. Because the final upstream 7.3 release is due after GA, the kernel in the release images (`7.3.0-9.9`) is based on `7.3-rc6`.

Notable Ubuntu kernel changes since Ubuntu 26.04 LTS:

* Snapdragon laptops and desktops ([LP: #2167217](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2167217), [LP: #2144643](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2144643), [LP: #2121477](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2121477)):
  * Early support for Snapdragon X2 Elite laptops: Asus Zenbook A14 (UX3407NA), HP EliteBook X G2q 14 AI, and Lenovo Yoga Slim 7x Gen 11.
  * Support for more Snapdragon X Elite and X Plus devices: Lenovo IdeaCentre Mini 01Q8X10 (Snapdragon X Plus model), Lenovo IdeaPad Slim 5x 14Q8X9, HP EliteBook 6 G1q, Acer Swift 14 AI (SF14-11), and Acer Swift Go 14 AI (SFG14-01).
  * Support for the built-in cameras of several Snapdragon X Elite laptops, including the Lenovo ThinkPad T14s, Lenovo Yoga Slim 7x, Dell XPS 13 9345, Dell Inspiron 14 7441, and Asus Zenbook A14.
* Enablement for upcoming AMD Zen 6 client platforms: HSMP client interface ([LP: #2167555](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2167555)), CPPC boost frequencies ([LP: #2167550](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2167550)), EPP tuning ([LP: #2167558](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2167558)), fTPM ([LP: #2167552](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2167552)), and the Sensor Fusion Hub ([LP: #2167219](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2167219)).
* Intel platforms:
  * Support for the TI TAC5xx2 audio codec on Intel Nova Lake platforms ([LP: #2167689](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2167689)).
  * Support for the Samsung S5K3J1 camera sensor on Intel MIPI camera platforms ([LP: #2121852](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2121852)).
  * An additional 900 MHz link frequency for the OmniVision OV05C10 camera sensor ([LP: #2147409](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2147409)).
* The amd64 and arm64 kernels now ship SPDX Software Bills of Materials (SBOM). The `linux-buildinfo-*` package of each kernel installs `sbom-source.spdx.json.zst`, `sbom-build.spdx.json.zst`, and `sbom-output.spdx.json.zst` under `/usr/lib/linux/<version>-<flavour>/`.
* GPIB (IEEE 488) instrument drivers are now built for amd64 ([LP: #2152714](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2152714)).
* EROFS page cache sharing between files with identical content (experimental) is enabled ([LP: #2158501](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2158501)).
* Prebuilt out-of-tree kernel modules:
  * ZFS has been updated to 2.4.4.
  * DOCA-OFED 3.5 kernel modules are available.
  * Lustre 2.17.58 kernel modules are now prebuilt for the generic kernel on amd64.
* NVIDIA drivers:
  * Prebuilt kernel modules are available for the 580 and 615 driver series, including the `-server` variants.
  * The 615 series replaces 595 and 610, including their `-server` variants. On upgrade, transitional packages move systems that use them to 615, for both the DKMS packages and the prebuilt kernel modules.
  * The 615 series ships only the open kernel modules, which support Turing and newer GPUs: `nvidia-driver-615` and `nvidia-driver-615-server` are now transitional packages for `nvidia-driver-615-open` and `nvidia-driver-615-server-open`. The 580 series still ships both the proprietary and the open kernel modules.

#### systemd 261.3

The `systemd` service manager has been updated to version 261. For a complete list of changes, see the [changelog](https://github.com/systemd/systemd/releases/tag/v261).

See also {ref}`support-for-legacy-system-v-scripts-removed`.

#### cloud-init v. 26.2

Cloud-init features introduced beyond v. 26.1 in Ubuntu 26.04 LTS (Resolute Raccoon):

* mounts: escape special characters in `fstab` mount paths
* net: add `route-metric` support in NetworkManager renderer
* azure: allow disable network `set-name`, report missing customdata, experimental `skip_ready_report`
* cloudstack: get `vr` information from network manager leases
* opennebula: support network configuration for global `SEARCH_DOMAIN` and `ETHx_ROUTES` static routes
* oracle: detect iSCSI root via iBFT for dracut images
* security: harden Jinja template rendering with sandboxing

See [cloud-init’s release notes for more details](https://github.com/canonical/cloud-init/releases).

#### 100% Rust `coreutils`

The default core utilities now run entirely on the Rust-based `uutils`
implementation. The remaining GNU utilities (`cp`, `mv`, and `rm`), previously
retained due to compatibility issues, have now been migrated.

To switch between the Rust and GNU implementations of coreutils, refer to {ref}`resolute-rust-coreutils`.

#### AMD ROCm 10.0

The AMD ROCm software stack in the Universe repository has been updated from version 7.1.0, shipped in Ubuntu 26.04 LTS, to version 10.0. The whole stack was upgraded in lockstep, including the compiler, the HIP and HSA runtimes, the system management tools, and the math, AI and communication libraries.

Highlights since ROCm 7.1.0 include:

- ROCm is now built and released upstream through [TheRock](https://github.com/ROCm/TheRock), its unified build system, since ROCm 7.14.
- The ROCm compiler is now provided by the `llvm-toolchain-rocm` source package, the AMD fork of the LLVM toolchain. It ships `clang-rocm`, `lld-rocm`, `hipcc-rocm`, the device libraries, Comgr and OpenMP offloading support. The whole ROCm stack is now built with this compiler instead of the standard Ubuntu LLVM toolchain.
- The libraries are additionally built for the `gfx10-3-generic` and `gfx11-generic` targets. This extends support to more RDNA 2 and RDNA 3 GPUs and APUs that don't have a dedicated build target, such as the Radeon RX 6600, RX 6700 and RX 7600 Series.
- Added the `gfx950` target for AMD Instinct MI350 Series GPUs.
- New libraries: `composable-kernel`, `hipfort`, `hipsparselt` and `migraphx`.
- HIP adds cooperative groups inclusive and exclusive scan APIs, `hipMemGetDefaultMemPool`, and faster `hipEventRecord`.
- The ROCr runtime can generate GPU core dumps while a debugger is attached.
- rocSPARSE and hipSPARSE add Blocked ELL format support, and CSC format support for sparse triangular solves.
- rocPRIM adds parallel top-K algorithms.
- RCCL extends symmetric memory support with a Reduce-Scatter kernel.

:::{dropdown} Supported hardware
The ROCm libraries are built for the following GPU architectures:

| GFX ISA | Hardware family |
|---|---|
| `gfx908` | Instinct™ MI100 |
| `gfx90a` | Instinct MI210, MI250 |
| `gfx942` | Instinct MI300, MI325 |
| `gfx950` | Instinct MI350, MI355 |
| `gfx1030` | Navi21 / Radeon™ RX 6800, RX 6900 Series, PRO V620 |
| `gfx10-3-generic` | Other RDNA 2 GPUs and APUs (`gfx1030` to `gfx1036`), such as Radeon RX 6600, RX 6700 Series |
| `gfx1100` | Navi31 / Radeon RX 7900 Series |
| `gfx1101` | Navi32 / Radeon RX 7700, RX 7800 Series |
| `gfx11-generic` | Other RDNA 3 and RDNA 3.5 GPUs and APUs (`gfx1100` to `gfx1103`, `gfx1150` to `gfx1153`), such as Radeon RX 7600 Series |
| `gfx1151` | Strix Halo / Ryzen™ AI MAX 300 Series (Radeon 8040S, 8050S, 8060S) |
| `gfx1200` | Navi44 / Radeon RX 9050, RX 9060 Series |
| `gfx1201` | Navi48 / Radeon RX 9070 Series, AI PRO R9700 |
:::

::::{dropdown} ROCm libraries
The following ROCm source packages are included at version 10.0:

:::{hlist}
:columns: 3

- `amdsmi`
- `composable-kernel`
- `hipblas`
- `hipblas-common`
- `hipblaslt`
- `hipcub`
- `hipfft`
- `hipfort`
- `hipify`
- `hiprand`
- `hipsolver`
- `hipsparse`
- `hipsparselt`
- `llvm-toolchain-rocm`
- `migraphx`
- `miopen`
- `rccl`
- `rocalution`
- `rocblas`
- `rocdbgapi`
- `rocfft`
- `rocm`
- `rocm-cmake`
- `rocm-core`
- `rocm-hipamd`
- `rocm-smi-lib`
- `rocminfo`
- `rocprim`
- `rocr-runtime`
- `rocrand`
- `rocsolver`
- `rocsparse`
- `rocthrust`
- `roctracer`
- `rocwmma`
:::
::::

:::{dropdown} Install the ROCm software stack
In most scenarios, you don't have to install these packages directly: the individual libraries are installed as dependencies of applications as needed. However, if you want to install the ROCm stack yourself, you can do it in two ways:

- Install the complete ROCm software stack, including binaries and header files:

    ```bash
    apt install rocm
    ```

- Install only the development libraries and header files for developing ROCm-enabled applications:

    ```bash
    apt install rocm-dev
    ```

:::

ROCm 10.0 includes some API and ABI changes. The AMD SMI library SONAME changed to `libamd_smi.so.27`, so software using it has to be rebuilt, and several deprecated AMD SMI APIs were removed. The deprecated `rocsparse_indextype_u16` type was also removed from rocSPARSE.

For details, see the [ROCm 10.0.0 release notes](https://rocm.docs.amd.com/en/docs-10.0.0/about/release-notes.html).

### WSL features

The Ubuntu Pro for WSL app is now published for both AMD64 and ARM64.

## Backwards-incompatible changes

### Desktop changes

#### WEP Wi-Fi security is no longer supported in Settings

GNOME 51 removes support in Settings for connecting to Wi-Fi networks that use Wired Equivalent Privacy (WEP).

WEP is an obsolete and insecure wireless security standard. Use a network configured with a modern security protocol instead.

### Server changes

#### OpenSSH split between two packages

OpenSSH in Ubuntu Server 26.10 has been split into two source packages: [`openssh`](https://launchpad.net/ubuntu/+source/openssh) and [`openssh-gssapi`](https://launchpad.net/ubuntu/+source/openssh-gssapi). The main difference between them is that [`openssh`](https://launchpad.net/ubuntu/+source/openssh) produces binary packages **without GSSAPI/Kerberos support**. That support has been moved to [`openssh-gssapi`](https://launchpad.net/ubuntu/+source/openssh-gssapi).

[`openssh-gssapi`](https://launchpad.net/ubuntu/+source/openssh-gssapi) produces:

 * `openssh-gssapi-server`: the server-side OpenSSH daemon with GSSAPI/Kerberos support.
 * `openssh-gssapi-client`: the client-side OpenSSH with GSSAPI

Whereas [openssh](https://launchpad.net/ubuntu/+source/openssh) produces:

 * `openssh-server` - the server-side OpenSSH daemon without GSSAPI/Kerberos support.
 * `openssh-client` - the client-side OpenSSH without GSSAPI/Kerberos support.
 * All the other regular `openssh` binary packages.

The `-gssapi` variants of these binary packages conflict with the non-`gssapi` ones. If one is installed, the other is removed.

This split was done to reduce the security exposure of the OpenSSH server and client binaries, as GSSAPI/Kerberos support is not required for many users. As explained in [#1141274](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1141274), the GSSAPI/Kerberos support includes a sizeable patch that was never included by the upstream project, but is still very useful to users of such deployments, and relied upon. This package split allows users to install the OpenSSH server and client without GSSAPI/Kerberos support, while still allowing those who need it to install the GSSAPI/Kerberos-enabled versions.

On top of that, the Ubuntu packaging of [`openssh-gssapi`](https://launchpad.net/ubuntu/+source/openssh-gssapi) also includes the `ccache` patch (see [LP: #1889548](https://bugs.launchpad.net/ubuntu/+source/openssh-gssapi/+bug/1889548). This allows for forwarded credentials to be stored according to the `default_ccache_name` setting in `/etc/krb5.conf` on the target host, instead of forcing a randomly named file in `/tmp`.

The Ubuntu release upgrader tool (see [How to upgrade your Ubuntu release](https://ubuntu.com/server/docs/how-to/software/upgrade-your-release/)) will check the system being upgraded for indications that GSSAPI/Kerberos is being used with `openssh`, and automatically select `openssh-server-gssapi` or `openssh-client-gssapi` for installation, if appropriate. Fresh installs of Ubuntu 26.10, however, will default to the non-GSSAPI/Kerberos versions of the OpenSSH server and client binaries.

Both `openssh` and `openssh-gssapi` are now on version 10.5, containing various bug fixes and security fixes. See the [upstream release notes](https://www.openssh.org/releasenotes.html).

#### `cyrus-sasl2` on i386 no longer supports PostgreSQL

Since Ubuntu 26.04 LTS, the binary `libsasl2-modules-sql` package no longer supports the PostgreSQL database on the i386 architecture. On all the other supported architectures, this package continues to support PostgreSQL.

See bug [LP: #2142320](https://bugs.launchpad.net/ubuntu/+source/cyrus-sasl2/+bug/2142320) for more details.

#### The PKCS#11 provider replaces the PKCS#11 engine

Since Ubuntu now ships OpenSSL 4, which no longer supports engines, the `libengine-pkcs11-openssl` package only ships the PKCS#11 provider, installed under `ossl-modules/`. The OpenSSL `ENGINE` has been removed.

Configurations still referencing the `pkcs11` engine need to be migrated to the provider.

See [LP: #2155023](https://bugs.launchpad.net/ubuntu/+source/libp11/+bug/2155023).

#### Removed or deprecated features in HAProxy

* The `program` section was removed, and the `master-worker` global directive, `dispatch` and `option transparent` were deprecated.
* Duplicate `frontend`, `backend`, `listen`, `defaults` and `log-forward` section names, as well as duplicate server names inside a backend, are now rejected as errors instead of warnings.
* `http-send-name-header` can no longer target the `connection`, `content-length`, `host` or `transfer-encoding` headers, and multiple `-m` match types in a single ACL are no longer accepted.

See the [HAProxy 3.3](https://www.haproxy.com/blog/announcing-haproxy-3-3) and [HAProxy 3.4](https://www.haproxy.com/blog/announcing-haproxy-3-4) announcements for the complete list of changes.

<!-- ### Development changes -->

### Cloud changes

* pollinate dropped from server-cloud-minimal seed and therefore from Stonking cloud images.
* GKE 1.28, 1.29, and 1.30 support dropped as EOL; newer GKE version support added.
* Anthos vSphere/VMWare 1.35 and 1.36 support added.

<!-- ### OpenStack -->

<!-- ### Platforms -->

### System changes


(support-for-legacy-system-v-scripts-removed)=
#### Support for legacy System V scripts removed

As announced in previous {ref}`release notes <ubuntu-26.04-lts-release-notes>`, the component `systemd-sysv-generator` for creating systemd services from `/etc/init.d` scripts at runtime has been removed. Packages in the Ubuntu Archive that were previously relying on this component either now ship a systemd service, or have been removed if they were no longer maintained.


## Deprecated features

### Server deprecations

#### BerkeleyDB deprecated in Postfix

BerkeleyDB support has been deprecated in Postfix. This affects the `hash:` and `btree:` map types. These types are still available, but their use will issue a deprecation warning. Such maps should be migrated to other formats.

See [Postfix Non-Berkeley-DB migration](https://www.postfix.org/NON_BERKELEYDB_README.html) for more information.

<!-- ### Development deprecations -->

### Cloud deprecations

* pollinate dropped from server-cloud-minimal seed ([LP: #2158262](https://bugs.launchpad.net/ubuntu/+source/ubuntu-meta/+bug/2158262)).
  * `xxd` dropped from minimal images as it was a dependency of pollinate

<!-- ### Security deprecations -->

<!-- ### Hardware support deprecations -->

<!-- ### System deprecations -->


## Bug fixes

### Desktop fixes

#### Fixes to updates and package details in App Center

App Center filters out phased updates that are not yet available to a system, avoiding misleading update entries. Debian package details also open more reliably when the PackageKit service has stopped and restarted.

#### Desktop icons remain visible after a release upgrade

Fixed an issue where desktop icons sometimes disappeared after upgrading Ubuntu. See [LP: #2164884](https://bugs.launchpad.net/bugs/2164884).

#### Improved rendering with fractionally scaled monitors

Fixed a Mutter issue that could cause a black screen or invalid page flips when using vertically arranged monitors with fractional scaling. See [Mutter merge request 3786](https://gitlab.gnome.org/GNOME/mutter/-/merge_requests/3786).

#### Faster loading of desktop icons

Fixed an issue that could leave icons blank or make them take several seconds to appear. See [LP: #2162035](https://bugs.launchpad.net/bugs/2162035).

#### Correctly apply the desktop theme

Fixed an issue where the selected theme was not applied correctly. See [LP: #2161877](https://bugs.launchpad.net/bugs/2161877).

#### Local password sign-in after device authentication

Fixed a GNOME Shell issue where the local password entry could fail to appear after device authentication. Users can now continue signing in with their local password when required. See [LP: #2160622](https://bugs.launchpad.net/ubuntu/+source/gnome-shell/+bug/2160622).

#### Active Directory setup in autoinstall

Previously, an automatic installation (autoinstall) with an interactive identity and Active Directory sections sometimes failed to ask for the Active Directory password. As a consequence, the computer didn't join to the domain. With this fix, the installer now presents the required Active Directory step. See [LP: #2065109](https://bugs.launchpad.net/subiquity/+bug/2065109).

### Server fixes

#### apache2 2.4.68

[apache2](https://launchpad.net/ubuntu/+source/apache2) was updated from 2.4.66 to upstream version 2.4.68. While this is mostly a security-driven update, the 2.4.67 and 2.4.68 releases together fix around 25 CVEs, affecting `mod_http2`, `mod_proxy_ajp`, `mod_proxy_ftp`, `mod_proxy_html`, `mod_ssl`, `mod_ldap`, `mod_dav_fs`, `mod_dav_lock`, `mod_md`, `mod_xml2enc`, `mod_authn_socache`, `mod_auth_digest`, `mod_rewrite` and the server core.

Besides the security fixes, the package was rebuilt against OpenSSL 4 and Lua 5.5. `mod_ssl` and `ab` now support OpenSSL 4.

The complete list of changes is available in the [upstream changelog](https://downloads.apache.org/httpd/CHANGES_2.4).

#### OpenLDAP 2.6.13

Updated from 2.6.10 to 2.6.13, which contains various bugfixes. See the [2.6 series upstream release notes](https://git.openldap.org/openldap/openldap/-/blob/OPENLDAP_REL_ENG_2_6/CHANGES)

#### PHP 8.5.9

[`php8.5`](https://launchpad.net/ubuntu/+source/php8.5) was updated from 8.5.4 to upstream version 8.5.9. These are bugfix and security point releases, with no new language features. Among the fixed issues are a heap corruption in `openssl_encrypt()` with AES-WRAP-PAD, an out-of-bounds write in `bccomp()`, an SQL injection through `E'...'` escape sequences, and two vulnerabilities in the bundled `uriparser` library.

Two packaging changes are worth noting:

* The `php-fpm` systemd unit was aligned with the hardening options provided upstream, and `PrivateTmp=true` was removed from it.
* The obsolete PID file is no longer created, and `php-fpm-reopenlogs` no longer depends on it.
* The package was rebuilt against OpenSSL 4.

See the [upstream changelog](https://www.php.net/ChangeLog-8.php#PHP_8_5) for the full list of changes.

#### squid 7.7

[squid](https://launchpad.net/ubuntu/+source/squid) was updated from 7.2 to upstream version 7.7. There are no new features in this range, but there is a long list of security and robustness fixes, which makes upgrading advisable:

* Nine upstream security advisories were addressed, covering ICP packet and URI validation, an out-of-bounds read while generating FTP directory listings, a heap overflow in cache digest handling, and base64 encoding buffer protection.
* Squid no longer creates world-readable directories, and the ICMP helper and the LDAPS authentication helpers were hardened.
* FTP handling is stricter: excessively large control replies are rejected, `reply_header_max_size` is honored for control responses, and commands containing CR or LF characters are refused.
* `Transfer-Encoding: identity` is now prohibited in HTTP/1.1 messages, as required by the specification. Clients or servers still using it will be rejected.

The details for each release are available in the [upstream release notes](https://github.com/squid-cache/squid/releases).

On the packaging side, squid now builds against OpenSSL 4.

#### sssd 2.12.0

[sssd](https://launchpad.net/ubuntu/+source/sssd) received some fixes in version 2.12.0:

* Two security issues were fixed: a denial of service in the PAM responder caused by missing validation of the authentication token length, and a use-after-free crash in `sssd_pam` while processing `p11_child` results with slow smartcards (see [LP: #2162577](https://bugs.launchpad.net/ubuntu/+source/sssd/+bug/2162577)).
* SSSD was made compatible with OpenSSL 4 and with GDM 51.

<!-- ### Development fixes -->

### Cloud fixes

* Grub config regeneration fixed for AWS EC2 images for both amd64 and arm64.
* Excluded GPU/RDMA NICs from networkd-wait-online in accelerator images.

<!-- ### Security fixes -->

<!-- ### Hardware support fixes -->

<!-- ### System fixes -->

### WSL fixes

#### Ubuntu Pro for WSL

[CVE-2026-102371](https://ubuntu.com/security/CVE-2026-102371) was disclosed
and fixed in `wsl-pro-service`. Previous versions of that service attach the
instance to Ubuntu Pro by executing the pro client with the Ubuntu Pro token
passed as a command-line argument (`pro attach <token>`). On systems where
`/proc` is mounted without process-hiding mitigations (such as `hidepid`),
which is the default in WSL, an unprivileged local user or process in the same
WSL instance can read the token from `/proc/<pid>/cmdline` while the attach
process is running. That's fixed in all LTS versions of Ubuntu on WSL and in
Stonking Stingray as well.

## Known issues

### Desktop issues

#### Some upgrades might stop on a dangling `/lib32` symlink

On systems with a dangling `/lib32` symbolic link, the upgrade might stop while installing the `base-files` package.

This has been reported on systems upgraded from older Ubuntu releases, including during an upgrade to 26.04.

The `ubuntu-release-upgrader` fix for Stonking is still in progress. The exact impact on upgrades from 26.04 to 26.10 is not yet clear. See [LP: #2131303](https://bugs.launchpad.net/bugs/2131303).

#### Future upgrades might be blocked for unsupported `/boot` configurations

In a future Ubuntu release, the boot loader will drop support for some less-common `/boot` configurations, including encrypted `/boot`, RAID-5/6, Apple partition tables, and file systems such as Btrfs, HFS+, XFS, and ZFS.

If you use such a `/boot` configuration, future Ubuntu releases might not be able to start on your system.

Work is under way to have the release upgrader detect affected systems and block an unsafe upgrade. See [LP: #2170211](https://bugs.launchpad.net/bugs/2170211).

#### Legacy GRUB changes might prevent booting with TPM-backed full-disk encryption

On systems using [TPM-backed full-disk encryption](https://ubuntu.com/desktop/docs/en/latest/explanation/hardware-backed-disk-encryption/) (TPM/FDE), the `snapd` service manages the boot configuration. Running `update-grub` after applying conventional GRUB customizations might leave your system unable to boot. The Stonking fix is still in progress. See [LP: #2157702](https://bugs.launchpad.net/bugs/2157702).

#### TPM-backed encrypted autoinstall might fail in virtual machines

When you run an automatic installation (autoinstall) with TPM-backed full-disk encryption in a virtual machine, the `accepted-errors: running-in-vm` option might fail with an installer error. The fix is in progress. See [LP: #2170594](https://bugs.launchpad.net/bugs/2170594).

#### Display freezes on some AMD dual-GPU laptops

On some laptops with both AMD integrated graphics and a discrete GPU, the built-in display might freeze when panel self-refresh is active, particularly when an external display is connected. See [LP: #2162904](https://bugs.launchpad.net/bugs/2162904).

#### Wi-Fi instability on some Intel AX211 systems

Some systems with Intel Wi-Fi 6E AX211 might experience firmware crashes and dropped Wi-Fi connections. The issue is hardware-specific and remains under investigation for Stonking. See [LP: #2157682](https://bugs.launchpad.net/bugs/2157682).

#### Keyboard might not work on some Snapdragon X Elite laptops

Due to a regression in Linux 7.3, the kernel sometimes selects an incorrect keyboard clock rate on some Snapdragon X2 Elite laptops. As a consequence, the built-in keyboard is unusable, including in the live installer. Users are advised to perform the installation with an external USB keyboard plugged in. A fix is being investigated. See [LP: #2169765](https://bugs.launchpad.net/bugs/2169765).

#### Wifi doesn't come back after suspend on some Snapdragon X Elite laptops

A kernel bug ([LP: #2169326](https://bugs.launchpad.net/bugs/2169326)) is preventing the Wifi to come back online after suspend. A workaround is available in the bug, and the proper fix will be delivered through the regular update mechanism.

#### Intel IPU cameras might fail during early boot or suspend

On some systems with Intel IPU6 or IPU7 cameras, necessary firmware might not be included in the `initramfs` image when the driver is loaded early. As a consequence, the camera driver fails to start.

Some Dell systems using the Intel IPU7 camera stack might also fail to suspend after camera activity.

These issues apply only to systems using the affected camera drivers. See [LP: #2164611](https://bugs.launchpad.net/bugs/2164611) and [LP: #2158228](https://bugs.launchpad.net/bugs/2158228).

#### Subtitles might not work in Showtime

The Showtime video player might not display subtitles, and video playback might stall when you change subtitle playback. The issue is being addressed in the GStreamer base plugins. See [LP: #2119649](https://bugs.launchpad.net/bugs/2119649).

#### RISC-V missing the App Center

The App Center is currently not installed by default on the Ubuntu 26.10 RISC-V desktop image.
Users should be able to install it if needed: `sudo snap install snap-store`.

### Server issues

#### OpenSSH package purge can break openssh

Do not purge an openssh package that is in "`rc`" state until the update in bug [LP: #2169738](https://bugs.launchpad.net/ubuntu/+source/openssh/+bug/2169738) is released.

The OpenSSH package was split into GSSAPI/Kerberos and non-GSSAPI/Kerberos variants, and they conflict with each other:
 * `openssh-server` conflicts with `openssh-server-gssapi`
 * `openssh-client` conflicts with `openssh-client-gssapi`

When switching from one package to its counterpart, the conflicted package will be removed (not purged), and stay in the "`rc`" state. This is correct and expected.

For example, if you had `openssh-server` installed, and switched to `openssh-server-gssapi`, this is how both packages would be listed:

```text
rc  openssh-server         ...
ii  openssh-server-gssapi  ...
```

If, however, while in this state, the removed package is **purged**, that will break the openssh configuration due to the removal of essential files still needed by the counterpart package, and **remote access may be lost**. This is the case for both server and client openssh packages.

This is being tracked in bug [LP: #2169738](https://bugs.launchpad.net/ubuntu/+source/openssh/+bug/2169738). For the Stonking release, only [openssh-gssapi](https://launchpad.net/ubuntu/+source/openssh-gssapi) was fixed, while [openssh](https://launchpad.net/ubuntu/+source/openssh) will be available as an SRU. Once that update lands, the purge action will work correctly and no longer break the existing configuration that is needed by the counterpart package.

<!-- ### Development issues -->

<!-- ### Security issues -->

### Hardware support issues

#### Raspberry Pi

* On the CM5 particularly, but potentially on other Pi 5 models, there appears to be a significantly larger power draw at boot time. If you experience issues during boot, and are *not* using an official (5A capable) power supply, please try using one before debugging further.

* The new `gnome-initial-setup` has issues preventing it from working properly:
  - Time zone input dropdown can "wobble" ([LP: #2084611](https://launchpad.net/bugs/2084611)).

* During boot on the server image, if your `cloud-init` configuration (in `user-data` on the boot partition) relies upon networking (importing SSH keys, installing packages, etc.) you *must* ensure that at least one network interface is required (`optional: false`) in `network-config` on the boot partition.
  - This is due to Netplan changes to the `wait-online` service ([LP: #2060311](https://launchpad.net/bugs/2060311)).
  - A current issue may still cause `cloud-init` to run before the network is ready ([LP: #2144891](https://launchpad.net/bugs/2144891)).
  - Another issue prevents the wifi wlan0 adapter from activating on first boot ([LP: #2170885](https://launchpad.net/bugs/2170885)); once booted, `sudo netplan apply` can be used to bring the network up but if you are relying on a cloud-init configuration requiring networking, this will fail.

* With the removal of the `crda` package in 22.04, the method of setting the WiFi regulatory domain (editing `/etc/default/crda`) no longer operates. On server images, use the `regulatory-domain` option in the Netplan configuration. On desktop images, append `cfg80211.ieee80211_regdom=GB` (substituting `GB` for the relevant country code) to the kernel command line in the `cmdline.txt` file on the boot partition  ([LP: #1951586](https://launchpad.net/bugs/1951586)).

* On server images, re-authentication to WiFi APs when regulatory domain is set result in `dmesg` spam to the console ([LP: #2063365](https://launchpad.net/bugs/2063365)).

#### SpacemiT K3

While initial support for the SpacemiT K3 platform landed in 26.10, some specific hardware support is missing:
* The second PCIe slot on K3 platforms, like the M.2 B Key on the Pico-ITX, will not work
* DisplayPort and HDMI audio are not supported
* GPU, VPU and G2D hardware nodes, for 3D graphics, video decode and 2D graphics acceleration are not supported
* Power balance elements (managing CPU frequency, thermals, power domains) are not supported

Installing an image on the K3 can be slow, please be patient and retry if you encounter an unexplained error with the installer.

Any issue can be reported as a bug on Launchpad targeting the affected packages.

<!-- ### System issues -->


## Official flavors

Find the release notes for the official flavors at the following links:

* [Ubuntu Budgie Release Notes](https://ubuntubudgie.org/blog/ubuntu-budgie-2610-release-notes/)
* [Ubuntu Cinnamon Release Notes](https://ubuntucinnamon.org/ubuntu-cinnamon-26-10-stonking-stingray-release-notes/)
* [Ubuntu Kylin Release Notes](https://www.ubuntukylin.com/news/ubuntukylin2610-en.html)
* [Ubuntu Unity Release Notes](https://ubuntuunity.org/posts/ubuntu-unity-2610-release-notes/)
* [Ubuntu MATE Release Notes](https://ubuntu-mate.org/blog/ubuntu-mate-stonking-stingray-release-notes/)
* [Xubuntu Release Notes](https://xubuntu.org/releasedocs/26.10/release-notes/)

## More information

Refer to {ref}`release-policy-and-schedule` and {ref}`project-and-community`.
