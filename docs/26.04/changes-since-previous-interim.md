---
tocdepth: 3
---

(ubuntu-26.04-lts-changes-since-25.10)=
# Ubuntu 26.04 LTS changes since 25.10

If you're upgrading to Ubuntu 26.04 LTS from the previous interim release, Ubuntu 25.10 (Questing Quokka), the following changes apply to you.

## New features and improvements

### Desktop features

#### GNOME 50

The GNOME desktop environment has been updated to version 50.

### Server features

#### Apache2

Apache 2 has been upgraded to upstream version 2.4.65. This new release includes a security fix:

* [CVE-2025-54090](https://www.cve.org/CVERecord?id=CVE-2025-54090): Apache HTTP Server: ‘RewriteCond expr’ always evaluates to true in 2.4.64

For more details, see the [upsteam release notes](https://www.apachelounge.com/Changelog-2.4.html) and the list of [security fixes](https://httpd.apache.org/security/vulnerabilities_24.html).

The debian changes for the new version have also disabled TLS 1.0 and 1.1, following RFC 8996. These should be already disabled by default in OpenSSL, and now Apache2 follows the same. See [the fixed bug](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=943415).

#### Django

Django was updated to LTS version 5.2.9, and will include security fixes for further point releases. For more information, see the [Django 5.2 release notes](https://docs.djangoproject.com/en/6.0/releases/5.2/).

#### Chrony 4.8

Chrony was updated to version 4.8, which adds support for limiting the selection of unreachable sources, fixes `refclock` handling on newer kernels and more.

For more information about the 4.8 release or all the other changes since version 4.5 that was in Noble please have a look at [Chrony’s news page](https://chrony-project.org/news.html).

#### Exim4

The Exim4 update to 4.99.1 improves handling many messages to a single host by using fewer forks & execs. New options like dkim_verify_minimal avoid calling the DKIM ACL after the first good verify and fix various bugs. For a detailed list of changes please refer to the [upstream changelog](https://github.com/Exim/exim/blob/master/doc/doc-txt/ChangeLog#L84). The minor .1 in 4.99.1 ensures that recent re-occurring security issues of CVE-2025-26794 and CVE-2025-67896 are closed right away.

#### Kerberos

Kerberos has been configured to observe the `/etc/krb5.conf.d/` directory by default. This introduces support for third-party packages that need to add Kerberos configuration.

* If you have existing configuration snippets in `/etc/krb5.conf.d/`, but do not include them, they will now be included in the `krb5.conf` file.
* If you already include `/etc/krb5.conf.d/` in your `krb5.conf` file, either active or commented out, no changes will be made.
* If your existing `krb5.conf` file is a symbolic link, no changes will be made.

MIT Kerberos and Heimdal are both supported, but use different orderings for the include directive. MIT Kerberos uses alphanumerical order, while Heimdal uses the unpredictable order of the readdir() system call ([LP: #2140967](https://bugs.launchpad.net/ubuntu/+source/heimdal/+bug/2140967))

#### `multipath-tools` 0.12.2

Updated to version 0.12.2. See the [upstream changelog](https://github.com/opensvc/multipath-tools/releases/tag/0.12.2).

#### Nginx 1.28.2

Nginx was updated to version 1.28.2, which includes fixes for various bugs, including CVE-2026-1642 and CVE-2025-53859.

See the [2.8 series upstream release notes](https://nginx.org/en/CHANGES-1.28).

#### OpenLDAP

New version [2.6.10](https://launchpad.net/ubuntu/+source/openldap).

* Running in [AppArmor enforce mode](https://documentation.ubuntu.com/server/how-to/security/apparmor/) now.
* Added patch to support changing pbkdf2 iteration count (see task [#2125685](https://bugs.launchpad.net/ubuntu/+source/openldap/+bug/2125685))

See the [2.6 series upstream release notes](https://git.openldap.org/openldap/openldap/-/blob/OPENLDAP_REL_ENG_2_6/CHANGES).

#### PHP 8.5.2

PHP was updated to the 8.5.2 upstream version. Among other enhancements and bugfixes, the highlighted changes are:

* A new URI Extension
* The Pipe Operator
* Clone With functionality
* The `#[\NoDiscard]` Attribute
* Closures and First-Class Callables in Constant Expressions
* Persistent `cURL` Share Handles
* `array_first()` and `array_last()` functions

Other breaking changes and new features can be seen in the [full upstream changelog](https://www.php.net/ChangeLog-8.php#PHP_8_5).

#### Samba 4.23

Samba has been updated to the new upstream 4.23 version.

New features and important changes in 4.23:

* SMB3 Unix Extensions enabled by default
* NetBios is disabled by default in the configuration file /etc/samba/smb.conf for fresh installs

#### SoS (`sosreport`)

SoS was updated to 4.10.2. This upgrade introduces new plugins and also adds new features to existing plugins.

For more information see the [4.10.1](https://github.com/sosreport/sos/releases/tag/4.10.1) and [4.10.2](https://github.com/sosreport/sos/releases/tag/4.10.2) upstream release notes.

### Container features

#### Container stacks

For the `containerd` and `runc` packages, we established a pattern to either keep the regular updates to the latest version or to opt for slower, more stable updates throughout the time the release is active. For more please read [Ubuntu Server Gazette - Issue 8 - Containers: Steady paths for agile stacks](https://discourse.ubuntu.com/t/ubuntu-server-gazette-issue-8-containers-steady-paths-for-agile-stacks/68680).

#### `containerd` 2.2.1

The `containerd` packages (`src:containerd-app`, `src:containerd-stable`) were updated to version 2.2.1. Version 2 includes the stabilization of new features added in the last 1.x release as well as the removal of features which were deprecated in 1.x, meaning you should expect breaking changes here.

For further details on such changes, please refer to the `containerd` 2.0 [upstream release notes](https://github.com/containerd/containerd/blob/main/docs/containerd-2.0.md) and check the notes for [individual point releases](https://github.com/containerd/containerd/releases).

#### `runc` 1.4.0

The `runc` package (`src:runc-app`) was updated to version 1.4.0. The most noteworthy change here is that the handling of `pids.limit` has been updated to match the newer guidance from the OCI runtime specification. In particular, now a maximum limit value of 0 will be treated as an actual limit (it will be treated the same as a limit value of 1). We only expect users that explicitly set `pids.limit` to 0 will see a behavior change.

For more details on this new release, please [check the upstream release notes](https://github.com/opencontainers/runc/releases/tag/v1.4.0).

#### Docker 29

[docker.io](http://docker.io) was updated to version 29. This release includes several improvements and breaking changes.

There is a new experimental support for `nftables` which can be enabled by setting Docker daemon’s firewall-backend option to `nftables`.

The `containerd` image store is now the default for **fresh installs**. This doesn’t apply to daemons configured with `userns-remap` or for users upgrading from a previous [docker.io](http://docker.io) version.

For a comprehensive list of changes, please check the [upstream release notes](https://docs.docker.com/engine/release-notes/29/).

### Virtualization features

#### libvirt

The libvirt package was upgraded to version 12.0.0. Here is the important changes since Ubuntu Questing:

* Several new features have been added into the bhyve driver:

* experimental NAT networking support using the Packet Filter (pf) firewall.

* querying domain block, interface, and memory statistics. not all statistics fields are supported though.

* SLIRP networking support

* NVMe device support

* virtio-scsi support

* initial ARM64 support

* Multi-GPU: Add support for NUMA affinity of PCI devices

To support NVIDIA Multi-Instance GPU (MIG) configurations, libvirt now handles QEMU’s acpi-generic-initiator device internally. MIG enables partitioning a physical GPU into multiple isolated instances, each associated with one or more virtual NUMA nodes.

* Hyper-V:

  * Introduce Hyper-V host-model mode

* Hyper-V virttype support for Qemu domains

For more details, please see the [upstream changelog](https://libvirt.org/news.html#v12-0-0-2026-01-15)

Some additional notable changes:

* The detection of the CPU MSR (Model Specific Register) features has been improved by enabling he msr kernel module load and fixing vmx-\* features detection issue.

* Use sysusers to manage users and groups

#### QEMU

The QEMU package was upgraded to version 10.2.1. Here is the important changes since Ubuntu Questing:

Upgrading Windows 11 makes the VM stop working and to fix this issue and ensure the migration path, we added new machine types for Resolute and old Ubuntu releases:

* pc-i440fx-questing-v2 Ubuntu 25.10 PC v2 (i440FX + PIIX, + 10.1 machine, 1996)

* pc-i440fx-noble-v2   Ubuntu 24.04 PC v2 (i440FX + PIIX, arch-caps fix, 1996)

* pc-q35-noble-v2      Ubuntu 24.04 PC v2 (Q35 + ICH9, arch-caps fix, 2009)

Other notable new features:

* ARM

  * new board model: amd-versal2-virt

  * New CPU architectural features emulated: FEAT_TCR2, FEAT_CSSC, FEAT_SCTLR2 …

* RISC-V

  * Add riscv64 to FirmwareArchitecture

  * Update OpenSBI to v1.7

  * Implement MonitorDef HMP API

* X86

  * Support for a new accelerator, MSHV, which lets you create VMs from a Hyper-V guest without using nested virtualization.

* Migration:

  * Supported new cpr-exec migration mode

  * Supported mapped-ram on snapshot save/load

For more details, please see related upstream [changelog](https://wiki.qemu.org/ChangeLog/10.2) and the general log on [removed features](https://qemu-project.gitlab.io/qemu/about/removed-features.html)

#### EDK2

The package has been updated to version **2025.11**. Below are the most significant changes since **Ubuntu Questing**:

* **OVMF packaging rework**

  * OVMF has been split into the following packages:

    * `ovmf-generic`

    * `ovmf-amdsev`

    * `ovmf-inteltdx`

  * The `ovmf` package is now a **metapackage** that depends on the above variants.
    This allows users to install only the OVMF firmware compatible with their CPU.

* **`ovmf-inteltdx` changes**

  * `OVMF.inteltdx.fd` has been removed.

  * `OVMF.inteltdx.secboot.fd` has been renamed to `OVMF.inteltdx.ms.fd`.

* **Removed components**

  * `qemu-efi-arm`

  * `ovmf-ia32`

  * The `loongarch64` target is no longer built.

* **Secure Boot improvements**

  * NX is now enabled in all Secure Boot variants.

  * The `strictnx` variant has been dropped.

* **New package**

  * Introduced `ovmf-legacy`, providing `OVMF.legacy.fd` with PVSCSI support.

Further details on new features and bug fixes are available in the upstream changelogs:

* [edk2-stable202505](https://github.com/tianocore/edk2/releases/tag/edk2-stable202505)

* [edk2-stable202508](https://github.com/tianocore/edk2/releases/tag/edk2-stable202508)

* [edk2-stable202511](https://github.com/tianocore/edk2/releases/tag/edk2-stable202511)

### Database features

#### DocumentDB

DocumentDB is now available in Ubuntu for the release of 26.04, starting with version 0.108-0. It is a powerful, scalable, MongoDB compatible open-source document database built for modern applications, built on PostgreSQL. For more information see [documentdb.io](https://documentdb.io/).

#### MySQL and MariaDB

MySQL’s current LTS version 8.4 is provided in Ubuntu 26.04, starting with version 8.4.8. Future security fixes will be provided by 8.4.x version updates. For more information [see the upstream release notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/).

MariaDB was updated to the latest LTS version 11.8.6. Starting with 26.04, the package will now be provided with [full support in Ubuntu main](https://bugs.launchpad.net/ubuntu/+source/mariadb/+bug/2122095). For more information on the MariaDB LTS, [see the upstream release notes](https://mariadb.com/docs/release-notes/community-server/11.8).

The MySQL and MariaDB servers are mutually exclusive on Ubuntu for now.

#### MySQL Shell

MySQL Shell was updated to the latest LTS version, 8.4.8, to match MySQL’s version. See the [upstream release notes](https://dev.mysql.com/doc/relnotes/mysql-shell/8.4/en/) for more information.

#### Percona Toolkit

Percona Toolkit was updated to the latest version, 3.7.1, and now includes additional tools for managing your MySQL, MariaDB, or PostgreSQL server. This includes `pt-galera-log-explainer`, `pt-k8s-debug-collector`,  and `pt-pg-summary` among others.

#### PostgreSQL

PostgreSQL was updated to version 18. This new version improves performance for workloads of all sizes through a new I/O subsystem that has demonstrated up to 3× performance improvements when reading from storage, and also increases the number of queries that can use indexes. This release makes major-version upgrades less disruptive, accelerating upgrade times and reducing the time required to reach expected performance after an upgrade completes. Developers also benefit from PostgreSQL 18 features, including virtual generated columns that compute values at query time, and the database-friendly uuidv7() function that provides better indexing and read performance for UUIDs. PostgreSQL 18 makes it easier to integrate with single-sign on (SSO) systems with support for OAuth 2.0 authentication.

For further information, check the [upstream release announcement](https://www.postgresql.org/about/news/postgresql-18-released-3142/) and the [upstream release notes](https://www.postgresql.org/docs/18/release-18.html).

Note that Postgresql-18 in Ubuntu 26.04 LTS no longer builds for the i386 architecture. Therefore, it no longer produces the libpq-dev and libpq5 binary packages for that architecture. This means that any package depending on those libraries, will also not be available in i386. See [LP: #2142320](https://bugs.launchpad.net/ubuntu-release-notes/+bug/2142320) for more information.

#### Valkey

Valkey was updated to version 9.0, starting with 9.0.3. This includes various features and improvements beyond 8.x, such as atomic slot migrations and hash field expiration. For more information on the new version, see the [Valkey 9 blog post](https://valkey.io/blog/introducing-valkey-9/). Release notes are available on the [Valkey project GitHub](https://github.com/valkey-io/valkey/releases).

### High availability and clustering features

#### `fence-agents`

fence-agents is updated to version 4.17.0. This version includes a few new agents, like aws_vpc_net and hetzner_cloud, and enhancements to the existing ones. Security-wise, the azure_arm agent replaced the dependency on msrestazure (deprecated) to azure-identity.

For a list of all changes, please refer to the \[upstream changes\]( https://github.com/ClusterLabs/fence-agents/compare/v4.16.0...v4.17.0 )

#### `resource-agents`

resource-agents is updated to version 4.17.0. This version includes several new agents, like aws-datasync-\* and tickle-\*, and enhancements to the existing ones. oracledb and zabbixagent were replaced by the oracle and zabbix-agent, respectively, and may require adjustments to existing configuration.

For a list of all changes, please refer to the \[upstream release notes\]( https://github.com/ClusterLabs/resource-agents/blob/main/ChangeLog )

#### HAProxy

Haproxy was updated to the latest upstream LTS release, 3.2, which introduces performance and efficiency improvements, faster and more reliable QUIC protocol support, and more. For further details on this new release, please check the HAProxy 3.2 [upstream announcement](https://www.mail-archive.com/haproxy@formilux.org/msg45917.html).

For users coming from HAPRoxy 2, **breaking changes** include detection of accidental multiple commands sent to the Runtime API, rejecting the enabled keyword for dynamic servers, stricter parsing of non-standard URIs and renaming of tune.ssl.ocsp-update to tune.ocsp-update. You can learn more about it at[ https://www.haproxy.com/blog/announcing-haproxy-3-0](https://www.haproxy.com/blog/announcing-haproxy-3-0). A complete list of changes is avalilable at[ https://www.haproxy.org/download/3.2/src/CHANGELOG](https://www.haproxy.org/download/3.0/src/CHANGELOG).

### Development features

#### Toolchain upgrades 🛠️

* glibc 2.42 now ships non-utf8 encodings as `libc-gconv-modules-extra`.
* LLVM 21 is the default LLVM toolchain.
* Rust 1.93.1 is the default Rust toolchain.

#### OpenJDK

OpenJDK 25 is the default Java toolchain.

#### .NET

...

### Enterprise features

### Cloud features

#### cloud-init v. 26.1

Cloud-init features introduced beyond v. 25.3 in Questing:

* Add support for s390x platform detection on LXD
* Add support for Tilaa cloud platform detection.
* Fix lxd snap installs on plucky and newer
* Scaleway cloud to support exposing regions and availability zones, drop private IP handling
* Add network v1 support for bonds, bridges and VLANs
* Allow `network-config` to express `allow_accept_ra` for bonds, bridges and VLANsOpenStack network_data.json support of bond names

See [cloud-init’s release notes for more details](https://github.com/canonical/cloud-init/releases).

#### Microsoft Azure

The `walinuxagent` package was updated to version `2.15.0.1`. This release brings several improvements to the Microsoft Azure Linux Guest Agent since Ubuntu Questing:

Extension Security
: Introduced support for extension signature validation and policy enforcement to improve the security of VM extensions.

Memory Management
: Implemented memory quota management using cgroups to ensure the agent maintains a predictable resource footprint.

Enhanced Reliability
: Improved telemetry and retry strategies for extension artifact downloads, along with more robust log collection handling.

Documentation
: Added a new `waagent` manpage for better local access to command-line documentation.

To overcome the former issues around password-changing functionality it will now utilize sha512_crypt of python3-passlib to be compatibly with python 3.13 that removed crypt.

For further details on the changes in this update, please refer to the upstream release notes:

* [v2.12.0.2](https://github.com/Azure/WALinuxAgent/releases/tag/v2.12.0.2)
* [v2.13.1.1](https://github.com/Azure/WALinuxAgent/releases/tag/v2.13.1.1)
* [v2.14.0.1](https://github.com/Azure/WALinuxAgent/releases/tag/v2.14.0.1)
* [v2.15.0.1](https://github.com/Azure/WALinuxAgent/releases/tag/v2.15.0.1)

### Security features

### Hardware support features

### Common features

#### Linux kernel 7.0 🐧

* `cgroupfs` is now mounted with `nsdelegate,memory_recursiveprot,memory_hugetlb_accounting`

#### systemd v257.4

...

#### Netplan v1.1.2 🌐

...

#### fwupd

Systems running TPM/FDE will now prompt for the recovery key before firmware updates that may require the recovery key upon reboot.

#### sudo-rs

Password feedback is now enabled by default in order to improve the user experience of `sudo`.
If the previous behavior is preferred, password feedback can be disabled using the following steps:

1. Edit sudoers using `sudo visudo` in the terminal
2. Add the option `Defaults !pwfeedback` to the configuration file

#### Package Management: APT 3.0

...

## Backwards-incompatible changes

### Desktop changes

### Server changes

#### NFS

The `blkmapd` and `nfs-blkmap` services have been removed. From the `NEWS` file:

> pNFS block layout is deprecated in favor of pNFS SCSI layout. This is  because block layout could easily result in data loss, as documented in <https://linux-nfs.org/wiki/index.php/PNFS_block_server_setup>.
>
> Users of pNFS are advised to move to the revised SCSI/NVMe layouts  that are safe to use and don't require the use of blkmapd.

#### SSSD 2.12

SSSD has been updated to version 2.12.

SSSD now runs under user `sssd` (instead of `root`). Make sure that `sssd` can still access secrets or integrations from its new user.

The implicit files provider and domain was removed: see <https://sssd.io/docs/files-provider-deprecation.html>.

#### PHP

* It is no longer possible to use `array` and `callable` as class alias names in `class_alias()`.

Other breaking changes and new features can be seen in the [full upstream changelog](https://www.php.net/ChangeLog-8.php#PHP_8_5).

#### HAProxy

For users coming from HAProxy 2, **breaking changes** include detection of accidental multiple commands sent to the Runtime API, rejecting the enabled keyword for dynamic servers, stricter parsing of non-standard URIs and renaming of tune.ssl.ocsp-update to tune.ocsp-update. You can learn more about it at [https://www.haproxy.com/blog/announcing-haproxy-3-0](https://www.haproxy.com/blog/announcing-haproxy-3-0). A complete list of changes is available at [https://www.haproxy.org/download/3.2/src/CHANGELOG](https://www.haproxy.org/download/3.0/src/CHANGELOG).

### Development changes

### Enterprise changes

### Cloud changes

### Security changes

### Hardware support changes

### Common changes


## Deprecated features

### Desktop deprecations

### Server deprecations

#### PHP

* Deprecation of the backtick operator
* Non-canonical cast names (boolean), (integer), (double), and (binary) have been deprecated. (bool), (int), (float), and (string) need to be used instead.
* Using null as an array offset or when calling array_key_exists() is now deprecated - now an empty string is needed.

Other breaking changes and new features can be seen in the [full upstream changelog](https://www.php.net/ChangeLog-8.php#PHP_8_5).

### Development deprecations

### Enterprise deprecations

### Cloud deprecations

### Security deprecations

### Hardware support deprecations

### Common deprecations


## Bug fixes

### Desktop fixes

### Server fixes

#### OpenSSH 10.2

OpenSSH was updated to version 10.2, which is a bugfix release on top of 10.1 present in the Ubuntu Questing 25.10 release.

#### Dovecot 2.4.2

Updated to 2.4.2. See the [upstream announcement](https://dovecot.org/mailman3/archives/list/dovecot@dovecot.org/thread/XTMMPVQ3QKQMYDZ3CZZCXPNHN7OXKS3L/).

#### Postfix 3.10.6

Postfix was updated to version 3.10.6. See the [upstream announcement](https://www.postfix.org/announcements/postfix-3.10.6.html).

#### `unbound` 1.24.2

Update to version 1.24.2. See the [upstream changelog](https://github.com/NLnetLabs/unbound/releases/tag/release-1.24.2).

### Development fixes

### Enterprise fixes

### Cloud fixes

### Security fixes

#### Apache2

Apache 2 has been upgraded to upstream version 2.4.65. This new release includes a security fix:

* [CVE-2025-54090](https://www.cve.org/CVERecord?id=CVE-2025-54090): Apache HTTP Server: ‘RewriteCond expr’ always evaluates to true in 2.4.64

For more details, see the [upstream release notes](https://www.apachelounge.com/Changelog-2.4.html) and the list of [security fixes](https://httpd.apache.org/security/vulnerabilities_24.html).

The Debian changes for the new version have also disabled TLS 1.0 and 1.1, following RFC 8996. These should be already disabled by default in OpenSSL, and now Apache2 follows the same. See [the fixed bug](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=943415).

### Hardware support fixes

### Common fixes


## Known issues

As is to be expected with any release, there are some significant known bugs that users may encounter with this release of Ubuntu. The ones we know about at this point (and some of the workarounds) are documented here, so you don’t need to spend time reporting these bugs again:

### Desktop issues

#### Localization

The Live Session of the new Ubuntu Desktop installer is not localized. It is still possible to perform a non-English installation using the new installer, but internet access at install time is required to download the language packs. ([LP: #2013329](https://bugs.launchpad.net/ubuntu-release-notes/+bug/2013329))

#### Screen reader support

Screen reader support is present with the new desktop installer, but is incomplete ([LP: #2061015](https://launchpad.net/bugs/2061015), [LP: #2061018](https://launchpad.net/bugs/2061018), [LP: #2036962](https://launchpad.net/bugs/2036962), [LP: #2061021](https://launchpad.net/bugs/2061021))

#### OEM installs

OEM installs are not supported yet. ([LP: #2048473](https://launchpad.net/bugs/2048473))

#### Virtualized GTK 4 apps

GTK 4 apps (including the desktop wallpaper) do not display correctly with VirtualBox or VMWare with 3D Acceleration ([LP: #2061118](https://launchpad.net/bugs/2061118)).

#### Incompatibility between TPM-backed Full Disk Encryption and Absolute

TPM-backed Full Disk Encryption (FDE) has been introduced to enhance data security. However, it’s important to note that this feature is incompatible with Absolute (formerly Computrace) security software. If Absolute is enabled on your system, the machine will not boot post-installation when TPM-backed FDE is also enabled. Therefore, disabling Absolute from the BIOS is recommended to avoid booting issues.

#### Hardware-Specific Kernel Module Requirements for TPM-backed Full Disk Encryption

TPM-backed Full Disk Encryption (FDE) requires a specific kernel snap which may not include certain kernel modules necessary for some hardware functionalities. A notable example is the `vmd` module required for NVMe RAID configurations. In scenarios where such specific kernel modules are indispensable, the hardware feature may need to be disabled in the BIOS (such as RAID) to ensure the continued availability of the affected hardware post-installation. If disabling in the BIOS is not an option, the related hardware will not be available post-installation with TPM-backed FDE enabled.

#### Full-disk encryption

See [FDE specific bug reports](https://bugs.launchpad.net/bugs/+bugs?field.searchtext=&orderby=-importance&field.status%3Alist=NEW&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.tag=fde&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search).

#### Resuming from suspend on Nvidia

Resuming from suspend on Nvidia desktops (where Nvidia is the primary GPU so generally not laptops)  will exhibit visual corruption and freezes using the default Wayland session  ([LP#1876632](https://bugs.launchpad.net/bugs/1876632)). If you need suspend/resume support then the simplest solution is to select ‘Ubuntu on Xorg’ at the login screen.

#### Classic fonts

Installing `ubuntu-fonts-classic` results in a non-Ubuntu font being displayed ([LP#2083683](https://bugs.launchpad.net/bugs/2083683)). To resolve this, install `gnome-tweaks` and set ‘Interface Text’ to ‘Ubuntu’.

### Server issues

#### rabbitmq-server

RabbitMQ is not directly upgradable due to feature flags. To mitigate this, some manual steps are needed. For more information please read <https://discourse.ubuntu.com/t/ubuntu-server-gazette-issue-12-upgrading-rabbitmq-across-ubuntu-releases/77271>.

#### Bacula

Moved from our `main` repository to `universe`. All relevant Ubuntu changes are upstream now, so we directly sync this from Debian.

<!--
#### Openstack

Currently, Nova Compute is non-functional because of a python3.13 incompatiblity ([LP:#2103413](https://bugs.launchpad.net/ubuntu/+source/nova/+bug/2103413)).
The Openstack team and Upstream work on it and it will be resolved via an SRU later.

The Ubuntu Cloud Archive is not affected by this bug.
-->

#### Installer

On systems booting via U-Boot, U-Boot should be updated to the current Plucky version before installation as subiquity does not run flash-kernel and grub-update during the installation. So for first boot the device-tree from U-Boot will be used.

* In some situations, it is acceptable to proceed with an offline installation when the mirror is inaccessible. In this scenario, it is advised to use:

    ```yaml
    apt:
      fallback: offline-install
    ```

* Network interfaces left unconfigured at install time are assumed to be configured via dhcp4. If this doesn’t happen (for example, because the interface is physically not connected) the boot process will block and wait for a few minutes ([LP: #2063331](https://bugs.launchpad.net/subiquity/+bug/2063331)). This can be fixed by removing the extra interfaces from `/etc/netplan/50-cloud-init.conf` or by marking them as `optional: true`. Cloud-init is disabled on systems installed from ISO images, so settings will persist.

<!--
#### samba apparmor profile

Due to [bug LP: #2063079](https://bugs.launchpad.net/ubuntu/+source/samba/+bug/2063079), the samba `smbd.service` unit file is no longer calling out to the helper script to dynamically create apparmor profile snippets according to the existing shares.

By default, the `smbd` service from samba is not confined. To be affected by this bug, users have to:

* install the optional `apparmor-profiles` package
* switch the `smbd` profile confinement from `complain` to `enforce`

Therefore, only users who have taken those steps and upgrade to Noble, will be affected by this bug. An SRU to fix it will be done shortly after release.
-->

<!--
#### Docker

There is an AppArmor related bug where containers cannot be promptly stopped due to the recently added AppArmor profile for `runc`. The containers are always killed with `SIGKILL` due to the denials when trying to receive a signal. More details about this bug can be found [here](https://bugs.launchpad.net/ubuntu/+source/docker.io/+bug/2063099), and a workaround is described [here](https://bugs.launchpad.net/ubuntu/+source/docker.io/+bug/2063099/comments/4).
-->

### Development issues

### Enterprise issues

### Cloud issues

#### Microsoft Azure

The current version of walinuxagent relies on python3-legacycrypt for password changing functionality but it cannot be made a dependency due to a component mismatch ([LP: #2106484](https://launchpad.net/bugs/2106484)).

### Security issues

### Hardware support issues

#### Hardware requiring `nomodeset`

Some particular hardware (e.g. Thinkpad x201) might have issues ([general freeze](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2084055), [`desktop-security-center` not launching](https://github.com/canonical/desktop-security-center/issues/81)), when booted without `nomodeset` (Safe graphics). Follow these steps if you encounter such an issue:

1. At the GRUB boot menu, press `e` (keep `Shift` pressed during early boot if the menu doesn’t show up).
2. Add `nomodeset` to `linux` line, like the example below:

    ```text
    linux /casper/vmlinuz nomodeset ---
    ```

3. Press {kbd}`Ctrl-x` to continue the boot process
4. After installation is complete, reboot, use `nomodeset` again, like the example below:

    ```text
    linux /boot/vmlinuz-6.11.0-8-generic nomodeset root=UUID=c5605a23-05ae-4d9d-b65f-e47ba48b7560 ro
    ```

5. Add `nomodeset` to the GRUB config file, `/etc/default/grub`, like the example below:

    ```text
    GRUB_CMDLINE_LINUX="nomodeset"
    ```

6. Finally, run `sudo update-grub` to make the change take effect.

<!--
#### PPC64EL

PMDK sees some hardware-specific failures in its test suite, which may make the software partially or fully inoperable on the ppc64el architecture. ([LP: #2061913](https://bugs.launchpad.net/ubuntu/+source/pmdk/+bug/2061913/))
-->

#### Raspberry Pi

* The new gnome-initial-setup has some teething issues:

  * Time zone input dropdown can “wobble” ([LP: #2084611](https://launchpad.net/bugs/2084611))
  * The localization of the application fails ([LP: #2104148](https://launchpad.net/bugs/2104148))
  * The hostname change is mandatory ([LP: #2093132](https://launchpad.net/bugs/2093132))

* During boot on the server image, if your `cloud-init` configuration (in `user-data` on the boot partition) relies upon networking (importing SSH keys, installing packages, etc.) you *must* ensure that at least one network interface is required (`optional: false`) in `network-config` on the boot partition. This is due to netplan changes to the wait-online service (~~[LP: #2060311](https://launchpad.net/bugs/2060311)~~)

* The seeded totem video player will not prompt users to install missing codecs when attempting to play a video requiring them ([LP: #2060730](https://launchpad.net/bugs/2060730))

* With the removal of the `crda` package in 22.04, the method of setting the wifi regulatory domain (editing `/etc/default/crda`) no longer operates. On server images, use the `regulatory-domain` option in the Netplan configuration. On desktop images, append `cfg80211.ieee80211_regdom=GB` (substituting `GB` for the relevant country code) to the kernel command line in the `cmdline.txt` file on the boot partition  ([LP: #1951586](https://launchpad.net/bugs/1951586)).

* The power LED on the Raspberry Pi 2B, 3B, 3A+, 3B+, and Zero 2W currently goes off and stays off once the Ubuntu kernel starts booting ([LP: #2060942](https://launchpad.net/bugs/2060942))

* Colours appear incorrectly in the Ubuntu App Centre ([LP: #2076919](https://launchpad.net/bugs/2076919))

* On server images, re-authentication to WiFi APs when regulatory domain is set result in dmesg spam to the console ([LP: #2063365](https://launchpad.net/bugs/2063365))

### Common issues

#### TPM/FDE

TPM/FDE installs seem to fail to boot after the installation is complete ([LP: #2104316](https://bugs.launchpad.net/snap-pc/+bug/2104316)). This is an issue with the *beta* image, and it is projected to be fixed by the plucky release.

#### Netboot installs

There is a bug ([LP: #2104316](https://bugs.launchpad.net/ubuntu-power-systems/+bug/2104297)) in the *beta* images that prevents netboot installs in some scenarios.

#### cloud-init upgrade

It has been reported that cloud-init may fail to upgrade properly in the Oracular to Plucky upgrade path, see [LP: #2104316](https://bugs.launchpad.net/ubuntu-power-systems/+bug/2104297).

#### ZFS with cryptoswap

ZFS with Encryption on Ubuntu 24.10 will [fail to activate the cryptoswap partition](https://bugs.launchpad.net/ubuntu/+source/subiquity/+bug/2084089).  This affects both new installs and upgrades.  We expect to address this post-release with an archive update.

#### I/O scheduler

A bug prevents the I/O scheduler from being reset to “none” ([LP: #2083845](https://bugs.launchpad.net/bugs/2083845)): the fix is already in Linux v6.11.2, and will be part of the first SRU kernel.

#### FAN networking

Support for FAN networking has been dropped in the 6.11 release kernel. It will be re-introduced in the next 6.11 kernel update shortly.


## Official flavors

Find the release notes for the official flavors at the following links:

* [Edubuntu Release Notes](https://discourse.ubuntu.com/t/edubuntu-26-04-beta-released/)
* [Kubuntu Release Notes](https://wiki.ubuntu.com/PluckyPuffin/ReleaseNotes/Kubuntu)
* [Lubuntu Release Notes](https://lubuntu.me/lubuntu-25-04-p-p-released/)
* [Ubuntu Budgie Release Notes](https://ubuntubudgie.org/2025/04/ubuntu-budgie-25-04-release-notes/)
* [Ubuntu MATE Release Notes](https://ubuntu-mate.org/blog/ubuntu-mate-p-p-release-notes/)
* [Ubuntu Studio Release Notes](https://discourse.ubuntu.com/t/ubuntu-studio-26.04-release-notes/)
* [Ubuntu Unity Release Notes](https://ubuntuunity.org/posts/ubuntu-unity-2504-released/)
* [Xubuntu Release Notes](https://wiki.xubuntu.org/releases/25.04/release-notes)
* [Ubuntu Kylin Release Notes](https://ubuntukylin.com/news/ubuntukylin2504-en.html)
* [Ubuntu Cinnamon Release Notes](https://ubuntucinnamon.org/?p=1348)
