(ubuntu-26.10-release-notes)=
# Ubuntu 26.10 release notes

These release notes cover new features and changes in Ubuntu 26.10 (Stonking Stingray).

:::{important}
Ubuntu 26.10 (Stonking Stingray) is currently in development, scheduled to be released in October 2026.
:::

For the release schedule of Ubuntu 26.10, refer to the {ref}`release schedule <stonking-stingray-schedule>`.

:::{toctree}
:maxdepth: 1
:hidden:

Release schedule <schedule>
:::

## Support lifespan

## Upgrades


## New features and improvements

### Desktop features

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

### Cloud features

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

#### 100% Rust `coreutils`

The default core utilities now run entirely on the Rust-based `uutils`
implementation. The remaining GNU utilities (`cp`, `mv`, and `rm`), previously
retained due to compatibility issues, have now been migrated.

To switch between the Rust and GNU implementations of coreutils, refer to {ref}`resolute-rust-coreutils`.


## Backwards-incompatible changes

### Desktop changes

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

### Development changes

### Enterprise changes

### Cloud changes

### OpenStack

### Platforms

### System changes


(support-for-legacy-system-v-scripts-removed)=
#### Support for legacy System V scripts removed

As announced in previous {ref}`release notes <ubuntu-26.04-lts-release-notes>`, the component `systemd-sysv-generator` for creating systemd services from `/etc/init.d` scripts at runtime has been removed. Packages in the Ubuntu Archive that were previously relying on this component either now ship a systemd service, or have been removed if they were no longer maintained.


## Deprecated features

### Desktop deprecations

### Server deprecations

#### BerkeleyDB deprecated in Postfix

BerkeleyDB support has been deprecated in Postfix. This affects the `hash:` and `btree:` map types. These types are still available, but their use will issue a deprecation warning. Such maps should be migrated to other formats.

See [Postfix Non-Berkeley-DB migration](https://www.postfix.org/NON_BERKELEYDB_README.html) for more information.

### Development deprecations

### Enterprise deprecations

### Cloud deprecations

### Security deprecations

### Hardware support deprecations

### System deprecations


## Bug fixes

### Desktop fixes

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

#### sssd 0.12.0

[sssd](https://launchpad.net/ubuntu/+source/sssd) received some fixes in version 0.12.0:

* Two security issues were fixed: a denial of service in the PAM responder caused by missing validation of the authentication token length, and a use-after-free crash in `sssd_pam` while processing `p11_child` results with slow smartcards (see [LP: #2162577](https://bugs.launchpad.net/ubuntu/+source/sssd/+bug/2162577)).
* SSSD was made compatible with OpenSSL 4 and with GDM 51.

### Development fixes

### Enterprise fixes

### Cloud fixes

### Security fixes

### Hardware support fixes

### System fixes


## Known issues

### Desktop issues

### Server issues

### Development issues

### Enterprise issues

### Cloud issues

### Security issues

### Hardware support issues

### System issues


## Official flavors

## More information
