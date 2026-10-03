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

### Development features

#### Toolchain upgrades

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

### System features

#### Linux kernel \<VERSION\>

#### systemd \<VERSION\>

#### 100% Rust `coreutils`

The default core utilities now run entirely on the Rust-based `uutils`
implementation. The remaining GNU utilities (`cp`, `mv`, and `rm`), previously
retained due to compatibility issues, have now been migrated.


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
