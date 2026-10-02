(ubuntu-26.10-release-notes)=
# Ubuntu 26.10 release notes

These release notes cover new features and changes in Ubuntu 26.10 (Stonking Stingray).

:::{important}
Ubuntu 26.10 (Stonking Stingray) is currently in development, scheduled to be released in October 2026.
:::

For the release schedule of Ubuntu 26.10, refer to:

:::{toctree}
:maxdepth: 1

Release schedule <schedule>
:::


## Support lifespan
## Upgrades
## New features in \<VERSION\>
### Updated Packages
### Linux kernel \<VERSION\> 🐧
### systemd \<VERSION\>
### Toolchain Upgrades 🛠️
| Toolchain | Version | Notes |
|-----------|---------|-------|
| GCC 🐄 | 15.2.0 | Includes latest patches for the GCC 15 series as well as support for C++ modules. [Release Notes](https://gcc.gnu.org/gcc-15/changes.html) |
| .NET 🦄 | 10.0.112 | Updated .NET runtimes with latest security fixes and toolchain capabilities. [Release Notes](https://github.com/dotnet/core/blob/main/release-notes/10.0/10.0.12/10.0.112.md) |
| Go 🐀 | 1.27 | Go 1.27 supports for generic methods and GODEBUG settings. [Release Notes](https://go.dev/doc/go1.27) |
| LLVM 🐉 | 22.1.6 | Includes targeted bug fixes and stability improvements with early support for C2y named loops and expanded SSE, AVX, AVX-512 intrinsics. [Release Notes](https://discourse.llvm.org/t/llvm-22-1-6-released/90838) |
| OpenJDK ☕ | 25.0.4 | OpenJDK release with many stability improvements and patches. [Release Notes](https://mail.openjdk.org/archives/list/jdk-updates-dev@openjdk.org/thread/BRREMPN6BLLC2CYAKLXGRHHNMCIQQSR5/) |
| Python 🐍 | 3.14.7 | Python 3.14.7 is the seventh maintenance release of 3.14, containing numerous bugfixes and improvements. [Release Notes](https://www.python.org/downloads/release/python-3147/) |
| Rust 🦀 | 1.97.1 | Rust 1.97 stable toolchain with LLVM miscompilation fixes. [Release Notes](https://blog.rust-lang.org/2026/07/16/Rust-1.97.1/) |
| Zig ⚡ | 0.16 | Zig is a general-purpose programming language and toolchain for maintaining robust, optimal, and reusable software. [Release Notes](https://ziglang.org/download/0.16.0/release-notes.html)|

### Default configuration changes ⚙️
### Ubuntu Desktop
### Ubuntu Foundations

#### 100% Rust coreutils

The default core utilities now run entirely on the Rust-based `uutils`
implementation. The remaining GNU utilities (`cp`, `mv`, and `rm`), previously
retained due to compatibility issues, have now been migrated.

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

### Ubuntu Server

#### cyrus-sasl2
Since Ubuntu 26.04 LTS, the binary libsasl2-modules-sql package no longer supports the PostgreSQL database on the i386 architecture ONLY. This package in all the other supported architectures in Ubuntu continues to support PostgreSQL. See bug [LP: #2142320](https://bugs.launchpad.net/ubuntu/+source/cyrus-sasl2/+bug/2142320) for more details.

#### freeradius
The FreeRADIUS software was updated to version 3.2.10. Highlights include:

 * Initial implementation of Protocol-Failure as per IETF draft
 * Suppress secrets by default in new installations (`supress_secrets=true`)
 * Many other improvements and bug fixes.

Please refer to the [FreeRADIUS release notes](https://www.freeradius.org/release_notes/) for more details.

#### frr

The FRRouting (frr) software was updated to version 10.7.1. Highlights include:
 * BFD authentication with keychain support (10.7.0)
 * BGP IPv6 VTEP support for EVPN (10.6.0)
 * BGP graceful restart for EVPN (10.6.0)
 * And many more improvements and bug fixes.

Please refer to the respective release notes for more information:

 * [FRRouting 10.7.0 release notes](https://frrouting.org/release/10.7.0/) and [FRRouting 10.7.1 release notes](https://frrouting.org/release/10.7.1/)
 * [FRRouting 10.6.0 release notes](https://frrouting.org/release/10.6.0/) and [FRRouting 10.6.1 release notes](https://frrouting.org/release/10.6.1/)

#### libp11
The libp11 package was updated to version 0.4.20. Highlights include:

 * Post-quantum cryptography support (ML-DSA, SLH-DSA, and FALCON key generation, signing, and verification).
 * OpenSSL 4.x support and a more complete PKCS#11 provider.
 * Memory-safety and concurrency fixes.
 * And many other improvements and bug fixes.

Please refer to the [libp11 release notes](https://github.com/OpenSC/libp11/releases) for more details.

#### openssh
OpenSSH in Ubuntu Server 26.10 has been split into two source packages: [openssh](https://launchpad.net/ubuntu/+source/openssh) and [openssh-gssapi](https://launchpad.net/ubuntu/+source/openssh-gssapi). The main difference between them is that [openssh](https://launchpad.net/ubuntu/+source/openssh) produces binary packages WITHOUT GSSAPI/Kerberos support. That support has been moved to [openssh-gssapi](https://launchpad.net/ubuntu/+source/openssh-gssapi).

[openssh-gssapi](https://launchpad.net/ubuntu/+source/openssh-gssapi) produces:

 * `openssh-gssapi-server` - the server-side OpenSSH daemon with GSSAPI/Kerberos support.
 * `openssh-gssapi-client` - the client-side OpenSSH with GSSAPI

Whereas [openssh](https://launchpad.net/ubuntu/+source/openssh) produces:

 * `openssh-server` - the server-side OpenSSH daemon without GSSAPI/Kerberos support.
 * `openssh-client` - the client-side OpenSSH without GSSAPI/Kerberos support.
 * and all the other regular openssh binary packages.

The `-gssapi` variants of these binary packages conflict with the non-gssapi ones. If one is installed, the other is removed.

This split was done to reduce the security exposure of the OpenSSH server and client binaries, as GSSAPI/Kerberos support is not required for many users. As explained in [#1141274](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1141274), the GSSAPI/Kerberos support includes a sizeable patch that was never included by the upstream project, but is still very useful to users of such deployments, and relied upon. This package split allows users to install the OpenSSH server and client without GSSAPI/Kerberos support, while still allowing those who need it to install the GSSAPI/Kerberos-enabled versions.

On top of that, the Ubuntu packaging of [openssh-gssapi](https://launchpad.net/ubuntu/+source/openssh-gssapi) also includes the ccache patch (see [LP: #1889548](https://bugs.launchpad.net/ubuntu/+source/openssh-gssapi/+bug/1889548). This allows for forwarded credentials to be stored according to the `default_ccache_name` setting in `/etc/krb5.conf` on the target host, instead of forcing a randomly named file in `/tmp`.

The Ubuntu release upgrader tool (see [How to upgrade your Ubuntu release](https://ubuntu.com/server/docs/how-to/software/upgrade-your-release/)) will check the system being upgraded for indications that GSSAPI/Kerberos is being used with openssh, and automatically select `openssh-server-gssapi` and/or `openssh-client-gssapi` for installation, if appropriate. Fresh installs of Ubuntu 26.10, however, will default to the non-GSSAPI/Kerberos versions of the OpenSSH server and client binaries.

#### postfix
Postfix in Ubuntu Server 26.10 has been updated to version 3.11.7. Important changes include:
 * BerkeleyDB support has been deprecated. This affects the `hash:` and `btree:` map types. These types are still available, but their use will issue a deprecation warning. Such maps should be migrated to other formats. Please see [Postfix Non-Berkeley-DB migration](https://www.postfix.org/NON_BERKELEYDB_README.html) for more information.
 * Several tools now support JSON output: `postconf`, `postalias`, `postmap`, and `postmulti`.

Please see the [Postfix 3.11.0 announcement](https://www.postfix.org/announcements/postfix-3.11.0.html) for the full list of changes.

#### samba
Samba in Ubuntu Server 26.10 has been updated to version 4.24.7. Important changes include:

 * New audit logging classes for some Active Directory attributes.
 * `vfs_streams_xattr` can hold larger streams.
 * Support for remote password management for Entra ID SSPR and Key cloak.
 * Kerberos PKINIT KeyTrust logon support.
 * Support for Windows Strong and Flexible key mappings as outlined in KB5014754: Certificate-based authentication changes on Windows domain controllers.
 * Domain encryption types changed to AES by default.
 * And many other improvements and bug fixes.

Please see the [Samba 4.24.0 release notes](https://www.samba.org/samba/history/samba-4.24.0.html) for the full list of changes.

### OpenStack
### Platforms

#### RISC-V

Ubuntu 26.10 introduces official support for multiple RVA23 RISC-V platforms:
- The SpacemiT K3 boards (Pico-ITX, CoM260 kit)
- The SiFive BigSky platform

Documentation on how to install on the SpacemiT K3 boards is available: https://ubuntu.com/hardware/docs/boards/how-to/ubuntu_supported/spacemit-k3/

Ubuntu Desktop and Xubuntu Minimal RISC-V desktop images are provided with support for the SpacemiT K3 and QEMU.

## Known Issues
### General
### Linux kernel
### Ubuntu Desktop
### Ubuntu Server
## Official flavors
## More information
