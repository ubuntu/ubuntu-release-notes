![ubuntu_logo-400|400x146, 50%](upload://sCHzlynRZef5eosuzaEYmwQ3K1S.png)

# Resolute Raccoon Release Notes (before migration)

<h1 id="heading--introduction">Introduction</h1>

These release notes for **Ubuntu 26.04 LTS** (Resolute Raccoon) provide an overview of the release and document the known issues with Ubuntu and its flavours.

## Support lifespan

Ubuntu 26.04 LTS will be supported for 5 years until April 2031.

## Upgrades

<h1 id="heading--new-features-in-26-04">New features in 26.04</h1>

## Updated Packages

## Linux kernel 7.0🐧

* `cgroupfs` is now mounted with `nsdelegate,memory_recursiveprot,memory_hugetlb_accounting`

## systemd v257.4

## Netplan v1.1.2 :globe_with_meridians:

## Toolchain Upgrades 🛠️

* glibc 2.42 now ships non-utf8 encodings as `libc-gconv-modules-extra`.
* LLVM 21 is the default LLVM toolchain.
* Rust 1.93.1 is the default Rust toolchain.

### OpenJDK

* OpenJDK 25 is the default Java toolchain

### .NET

## Default configuration changes :gear:

## Ubuntu Desktop

### New ARM64 Desktop Image

### Installer and Upgrades

### Enterprise

### GNOME :footprints:

### Default app changes

### Updated Applications

### Updated Subsystems

### Gaming

#### NVIDIA Dynamic Boost

### Support for new Intel® integrated and discrete GPUS

## Ubuntu Foundations

### Cryptography

### fwupd

Systems running TPM/FDE will now prompt for the recovery key before firmware updates that may require the recovery key upon reboot.

### sudo-rs

Password feedback is now enabled by default in order to improve the user experience of `sudo`.
If the previous behavior is preferred, password feedback can be disabled using the following steps:

1. Edit sudoers using `sudo visudo` in the terminal
2. Add the option `Defaults !pwfeedback` to the configuration file

#### Libraries

### Package Management: APT 3.0

## Ubuntu Server

Ubuntu Server users often come from using the former LTS - in this case 24.04 Noble, we want to remind you to pleace check out the release notes for the interim releases as well, because all the great things that happened in the meantime do apply for you as well.

* [24.10 Oracular Oriole Release notes](https://discourse.ubuntu.com/t/oracular-oriole-release-notes/44878)
* [25.04 Plucky Puffin](https://discourse.ubuntu.com/t/plucky-puffin-release-notes/48687)
* [25.10 Questing Quokka](https://discourse.ubuntu.com/t/questing-quokka-release-notes/59220)

### Container stacks

For the containerd and runc packages, we established a pattern to either keep the regular updates to the latest version or to opt for slower more stable updates throughout the time the release is active. For more please read[ Ubuntu Server Gazette - Issue 8 - Containers: Steady paths for agile stacks](https://discourse.ubuntu.com/t/ubuntu-server-gazette-issue-8-containers-steady-paths-for-agile-stacks/68680).

#### Containerd

The containerd packages (src:containerd-app, src: containerd-stable) were updated to version 2.2.1. Version 2 includes the stabilization of new features added in the last 1.x release as well as the removal of features which were deprecated in 1.x, meaning you should expect breaking changes here.

For further details on such changes, please refer to the containerd 2.0[upstream release notes](https://github.com/containerd/containerd/blob/main/docs/containerd-2.0.md) and check the notes for [individual point releases](https://github.com/containerd/containerd/releases).

#### runc

The runc package (src:runc-app) was updated to version 1.4.0. The most noteworthy change here is that the handling of pids.limit has been updated to match the newer guidance from the OCI runtime specification. In particular, now a maximum limit value of 0 will be treated as an actual limit (it will be treated the same as a limit value of 1). We only expect users that explicitly set pids.limit to 0 will see a behavior change.

For more details on this new release, please [check the upstream release notes](https://github.com/opencontainers/runc/releases/tag/v1.4.0).

#### Docker

[docker.io](http://docker.io) was updated to version 29. This release includes several improvements and breaking changes.

There is a new experimental support for nftables which can be enabled by setting Docker daemon’s firewall-backend option to nftables.

The containerd image store is now the default for **fresh installs**. This doesn’t apply to daemons configured with userns-remap or for users upgrading from a previous [docker.io](http://docker.io) version.

For a comprehensive list of changes, please check the [upstream release notes](https://docs.docker.com/engine/release-notes/29/).

### Virtualization

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

### Databases

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

### Ubuntu HA/Clustering

#### **fence-agents**

fence-agents is updated to version 4.17.0. This version includes a few new agents, like aws_vpc_net and hetzner_cloud, and enhancements to the existing ones. Security-wise, the azure_arm agent replaced the dependency on msrestazure (deprecated) to azure-identity.

For a list of all changes, please refer to the \[upstream changes\]( https://github.com/ClusterLabs/fence-agents/compare/v4.16.0...v4.17.0 )

#### **resource-agents**

resource-agents is updated to version 4.17.0. This version includes several new agents, like aws-datasync-\* and tickle-\*, and enhancements to the existing ones. oracledb and zabbixagent were replaced by the oracle and zabbix-agent, respectively, and may require adjustments to existing configuration.

For a list of all changes, please refer to the \[upstream release notes\]( https://github.com/ClusterLabs/resource-agents/blob/main/ChangeLog )

#### HAProxy

Haproxy was updated to the latest upstream LTS release, 3.2, which introduces performance and efficiency improvements, faster and more reliable QUIC protocol support, and more. For further details on this new release, please check the HAProxy 3.2 [upstream announcement](https://www.mail-archive.com/haproxy@formilux.org/msg45917.html).

For users coming from HAPRoxy 2, **breaking changes** include detection of accidental multiple commands sent to the Runtime API, rejecting the enabled keyword for dynamic servers, stricter parsing of non-standard URIs and renaming of tune.ssl.ocsp-update to tune.ocsp-update. You can learn more about it at[ https://www.haproxy.com/blog/announcing-haproxy-3-0](https://www.haproxy.com/blog/announcing-haproxy-3-0). A complete list of changes is avalilable at[ https://www.haproxy.org/download/3.2/src/CHANGELOG](https://www.haproxy.org/download/3.0/src/CHANGELOG).

### Further Server Packages

#### Apache2

Apache 2 has been upgraded to upstream version 2.4.65. This new release includes a security fix:

* [CVE-2025-54090](https://www.cve.org/CVERecord?id=CVE-2025-54090): Apache HTTP Server: ‘RewriteCond expr’ always evaluates to true in 2.4.64

For more details, see the [upsteam release notes](https://www.apachelounge.com/Changelog-2.4.html) and the list of [security fixes](https://httpd.apache.org/security/vulnerabilities_24.html).

The debian changes for the new version have also disabled TLS 1.0 and 1.1, following RFC 8996. These should be already disabled by default in OpenSSL, and now Apache2 follows the same. See [the fixed bug](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=943415).

#### Clamav

#### Django

Django was updated to LTS version 5.2.9, and will include security fixes for further point releases. For more information, see the [Django 5.2 release notes](https://docs.djangoproject.com/en/6.0/releases/5.2/).

#### Chrony

Chrony was updated to version 4.8, which adds support for limiting the selection of unreachable sources, fixes refclock handling on newer kernels and more.

For more information about the 4.8 release or all the other changes since version 4.5 that was in Noble please have a look at [Chrony’s news page ](https://chrony-project.org/news.html)

#### cloud-init v. 26.1

Cloud-init features introduced beyond v. 25.3 in Questing:

* Add support for s390x platform detection on LXD
* Add support for Tilaa cloud platform detection.
* Fix lxd snap installs on plucky and newer
* Scaleway cloud to support exposing regions and availability zones, drop private IP handling
* Add network v1 support for bonds, bridges and VLANs
* Allow `network-config` to express `allow_accept_ra` for bonds, bridges and VLANsOpenStack network_data.json support of bond names

See \[cloud-init’s release notes for more details\]( https://github.com/canonical/cloud-init/releases )

#### Exim4

The Exim4 update to 4.99.1 improves handling many messages to a single host by using fewer forks & execs. New options like dkim_verify_minimal avoid calling the DKIM ACL after the first good verify and fix various bugs. For a detailed list of changes please refer to the [upstream changelog](https://github.com/Exim/exim/blob/master/doc/doc-txt/ChangeLog#L84). The minor .1 in 4.99.1 ensures that recent re-occurring security issues of CVE-2025-26794 and CVE-2025-67896 are closed right away.

#### Kerberos

Kerberos has been configured to observe the `/etc/krb5.conf.d/` directory by default. This introduces support for third-party packages that need to add Kerberos configuration.

* If you have existing configuration snippets in `/etc/krb5.conf.d/`, but do not include them, they will now be included in the `krb5.conf` file.
* If you already include `/etc/krb5.conf.d/` in your `krb5.conf` file, either active or commented out, no changes will be made.
* If your existing `krb5.conf` file is a symbolic link, no changes will be made.

MIT Kerberos and Heimdal are both supported, but use different orderings for the include directive. MIT Kerberos uses alphanumerical order, while Heimdal uses the unpredictable order of the readdir() system call ([LP: #2140967](https://bugs.launchpad.net/ubuntu/+source/heimdal/+bug/2140967))

#### multipath-tools

Updated to version 0.12.2. See the [upstream changelog](https://github.com/opensvc/multipath-tools/releases/tag/0.12.2).

#### NFS

The `blkmapd` and `nfs-blkmap` services have been removed. From the NEWS file:
>  pNFS block layout is deprecated in favor of pNFS SCSI layout. This is  because block layout could easily result in data loss, as documented in <https://linux-nfs.org/wiki/index.php/PNFS_block_server_setup>.
>
 > Users of pNFS are advised to move to the revised SCSI/NVMe layouts  that are safe to use and don't require the use of blkmapd.


#### Nginx

Nginx was updated to version 1.28.2, which includes fixes for various bugs, including CVE-2026-1642 and CVE-2025-53859.

See the [2.8 series upstream release notes](https://nginx.org/en/CHANGES-1.28).

#### OpenLDAP

New version [2.6.10](https://launchpad.net/ubuntu/+source/openldap).

* Running in [AppArmor enforce mode](https://documentation.ubuntu.com/server/how-to/security/apparmor/) now.
* Added patch to support changing pbkdf2 iteration count (see task [#2125685](https://bugs.launchpad.net/ubuntu/+source/openldap/+bug/2125685))

See the [2.6 series upstream release notes](https://git.openldap.org/openldap/openldap/-/blob/OPENLDAP_REL_ENG_2_6/CHANGES).

#### Openssh

OpenSSH was updated to version 10.2, which is a bugfix release on top of 10.1 present in the Ubuntu Questing 25.10 release.

When upgrading from Ubuntu Noble 24.04, the following are relevant changes:

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
Postfix in Ubuntu 26.04 Resolute was updated to version 3.10.6. All the upstream release notes can be found at https://www.postfix.org/announcements.html.

Specific release notes for major version releases since Ubuntu Noble 24.04 are:
* 3.9.0: https://www.postfix.org/announcements/postfix-3.9.0.html
* 3.10.0: https://www.postfix.org/announcements/postfix-3.10.0.html

A noteworthy change in the packaging of Postfix is that **by default it is no longer installed in a chroot, and only limited chroot support is available from now on**.


#### PHP

PHP was updated to the 8.5.2 upstream version. The highlighted changes are:

* A new URI Extension
* The Pipe Operator
* Clone With functionality
* The #\[\\NoDiscard\] Attribute
* Closures and First-Class Callables in Constant Expressions
* Persistent cURL Share Handles
* array_first() and array_last() functions
  Among other enhancements and bugfixes.

There are also breaking changes and deprecations which should be taken into consideration:

* Deprecation of the backtick operator
* Non-canonical cast names (boolean), (integer), (double), and (binary) have been deprecated. (bool), (int), (float), and (string) need to be used instead.
* Using null as an array offset or when calling array_key_exists() is now deprecated - now an empty string is needed.
* It is no longer possible to use “array” and “callable” as class alias names in class_alias().

Other breaking changes and new features can be seen in the [full upstream changelog](https://www.php.net/ChangeLog-8.php#PHP_8_5).

#### Samba

Samba has been updated to the new upstream 4.23 version.

New features and important changes in 4.23:

* SMB3 Unix Extensions enabled by default
* NetBios is disabled by default in the configuration file /etc/samba/smb.conf for fresh installs

Other upstream changes since Ubuntu Noble 24.04:

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

##### **samba on i386**

Samba version 4.21.x added a dependency to the python3-samba package: python3-cryptography. Unfortunately, python3-cryptography was last built for i386 for Ubuntu Bionic 18.04, and is no longer available for that architecture, making this new dependency unsatisfiable.

For Ubuntu Plucky 25.04 and later, the python3-samba package is no longer built for i386. Please see [LP: #2099895](https://bugs.launchpad.net/ubuntu/+source/samba/+bug/2099895) for details. The main consequence is that the samba-tool script (part of that package) is no longer available for i386.

##### **Upgrading an AD/DC from previous Ubuntu releases**

If you have deployed a Samba Active Directory Domain Controller WITHOUT having installed the samba-ad-dc package, you should install it before doing a release upgrade to Ubuntu Plucky Puffin 25.04. If samba-ad-dc is not installed prior to the release upgrade, the Active Directory Domain Controller functionality will not work on the upgraded system due to many missing components.

See [LP: #2101838](https://bugs.launchpad.net/ubuntu/+source/samba/+bug/2101838) for more information

##### **Samba upstream release notes since Ubuntu Noble 24.04**

[https://www.samba.org/samba/history/samba-4.20.0.html](https://www.samba.org/samba/history/samba-4.20.0.html)

[https://www.samba.org/samba/history/samba-4.21.0.html](https://www.samba.org/samba/history/samba-4.21.0.html)

[https://www.samba.org/samba/history/samba-4.22.0.html](https://www.samba.org/samba/history/samba-4.22.0.html)

[https://www.samba.org/samba/history/samba-4.23.0.html](https://www.samba.org/samba/history/samba-4.23.0.html)

**Squid**

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

For a list of all changes and fixes, please check the \[upstream releases page\]( https://github.com/squid-cache/squid/releases )

#### SSSD

Now running under user `sssd` (instead of `root`)!

* Please make sure that sssd can still access secrets or integrations from its new user

Updated to version 2.12.

* The implicit files provider and domain was removed: https://sssd.io/docs/files-provider-deprecation.html

Other changes of importance are listed upstream:

* https://sssd.io/release-notes/sssd-2.11.0.html
* https://sssd.io/release-notes/sssd-2.12.0.html

#### unbound

Update to version 1.24.2. See the [upstream changelog](https://github.com/NLnetLabs/unbound/releases/tag/release-1.24.2).

### sos (sosreport)

Sos was updated from 4.10.2 to 4.10.2. This upgrade introduces new plugins and also adds new features to existing plugins.

For more information see the [4.10.1](https://github.com/sosreport/sos/releases/tag/4.10.1) and [4.10.2](https://github.com/sosreport/sos/releases/tag/4.10.2) upstream release notes.

## Ubuntu WSL

## OpenStack

### Ceph

### Open vSwitch (OVS) and Open Virtual Network (OVN)

### GRUB2

## Platforms

### Public Cloud / Cloud images

##### How to report any issues resulting from these changes

### Raspberry Pi 🍓

### arm64

### IBM Z and LinuxONE (s390x) ![image|32x32](upload://dZM0RRlelqCcZc6RhqJGMW8DMZr.png)

### IBM POWER (ppc64el)

### RISC-V

<h1 id="heading--known-issues">Known Issues</h1>

As is to be expected with any release, there are some significant known bugs that users may encounter with this release of Ubuntu. The ones we know about at this point (and some of the workarounds) are documented here, so you don’t need to spend time reporting these bugs again:

## General

* TPM FDE installs seem to fail to boot after the installation is complete ([LP: #2104316](https://bugs.launchpad.net/snap-pc/+bug/2104316)). This is an issue with the *beta* image, and it is projected to be fixed by the plucky release.
* There is a bug ([LP: #2104316](https://bugs.launchpad.net/ubuntu-power-systems/+bug/2104297)) in the *beta* images that prevents netboot installs in some scenarios.
* It has been reported that cloud-init may fails to upgrade properly in the Oracular to Pluck upgrade path, see [LP: #2104316](https://bugs.launchpad.net/ubuntu-power-systems/+bug/2104297).
* The Live Session of the new Ubuntu Desktop installer is not localized. It is still possible to perform a non-English installation using the new installer, but internet access at install time is required to download the language packs. ([LP: #2013329](https://bugs.launchpad.net/ubuntu-release-notes/+bug/2013329))
* ZFS with Encryption on Ubuntu 24.10 will [fail to activate the cryptoswap partition](https://bugs.launchpad.net/ubuntu/+source/subiquity/+bug/2084089).  This affects both new installs and upgrades.  We expect to address this post-release with an archive update.
* Some particular hardware (e.g. Thinkpad x201) might have issues ([general freeze](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2084055), [`desktop-security-center` not launching](https://github.com/canonical/desktop-security-center/issues/81)), when booted without `nomodeset` (Safe graphics). Follow these steps if you encounter such an issue:

1. At the GRUB boot menu, press `e` (keep `Shift` pressed during early boot if the menu doesn’t show up).
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

## Linux kernel

* A bug prevents the IO scheduler from being reset to “none” ([LP: #2083845](https://bugs.launchpad.net/bugs/2083845)): the fix is already in v6.11.2, and will be part of the first SRU kernel.
* Support for FAN networking has been dropped in the 6.11 release kernel. It will be re-introduced in the next 6.11 kernel update shortly.

## Ubuntu Desktop

* Screen reader support is present with the new desktop installer, but is incomplete ([LP: #2061015](https://launchpad.net/bugs/2061015), [LP: #2061018](https://launchpad.net/bugs/2061018), [LP: #2036962](https://launchpad.net/bugs/2036962), [LP: #2061021](https://launchpad.net/bugs/2061021))

* OEM installs are not supported yet ([LP: #2048473](https://launchpad.net/bugs/2048473))

* GTK4 apps (including the desktop wallpaper) do not display correctly with VirtualBox or VMWare with 3D Acceleration ([LP: #2061118](https://launchpad.net/bugs/2061118)).

* **Incompatibility between TPM-backed Full Disk Encryption and Absolute:** TPM-backed Full Disk Encryption (FDE) has been introduced to enhance data security. However, it’s important to note that this feature is incompatible with Absolute (formerly Computrace) security software. If Absolute is enabled on your system, the machine will not boot post-installation when TPM-backed FDE is also enabled. Therefore, disabling Absolute from the BIOS is recommended to avoid booting issues.

* **Hardware-Specific Kernel Module Requirements for TPM-backed Full Disk Encryption:** TPM-backed Full Disk Encryption (FDE) requires a specific kernel snap which may not include certain kernel modules necessary for some hardware functionalities. A notable example is the `vmd` module required for NVMe RAID configurations. In scenarios where such specific kernel modules are indispensable, the hardware feature may need to be disabled in the BIOS (such as RAID) to ensure the continued availability of the affected hardware post-installation. If disabling in the BIOS is not an option, the related hardware will not be available post-installation with TPM-backed FDE enabled.

* [FDE specific bug reports](https://bugs.launchpad.net/bugs/+bugs?field.searchtext=&orderby=-importance&field.status%3Alist=NEW&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.tag=fde&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search).

* Resuming from suspend on Nvidia desktops (where Nvidia is the primary GPU so generally not laptops)  will exhibit visual corruption and freezes using the default Wayland session  ([LP#1876632](https://bugs.launchpad.net/bugs/1876632)). If you need suspend/resume support then the simplest solution is to select ‘Ubuntu on Xorg’ at the login screen.

* Installing `ubuntu-fonts-classic` results in a non-Ubuntu font being displayed ([LP#2083683](https://bugs.launchpad.net/bugs/2083683)). To resolve this, install `gnome-tweaks` and set ‘Interface Text’ to ‘Ubuntu’.

## Ubuntu Server

### rabbitmq-server

RabbitMQ is not directly upgradable due to feature flags. To mitigate this, some manual steps are needed. For more information please read https://discourse.ubuntu.com/t/ubuntu-server-gazette-issue-12-upgrading-rabbitmq-across-ubuntu-releases/77271 .

### Bacula

Moved from our `main` repository to `universe`. All relevant Ubuntu changes are upstream now, so we directly sync this from Debian.

### Installer

On systems booting via U-Boot, U-Boot should be updated to the current Plucky version before installation as subiquity does not run flash-kernel and grub-update during the installation. So for first boot the device-tree from U-Boot will be used.

* In some situations, it is acceptable to proceed with an offline installation when the mirror is inaccessible. In this scenario, it is advised to use:

```
apt:
  fallback: offline-install
```

* Network interfaces left unconfigured at install time are assumed to be configured via dhcp4. If this doesn’t happen (for example, because the interface is physically not connected) the boot process will block and wait for a few minutes ([LP: #2063331](https://bugs.launchpad.net/subiquity/+bug/2063331)). This can be fixed by removing the extra interfaces from `/etc/netplan/50-cloud-init.conf` or by marking them as `optional: true`. Cloud-init is disabled on systems installed from ISO images, so settings will persist.

### Raspberry Pi

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

### Google Compute Platform

Nothing yet.

### Microsoft Azure

The `walinuxagent` package was updated to version `2.15.0.1`. This release brings several improvements to the Microsoft Azure Linux Guest Agent since Ubuntu Questing:

* **Extension Security**: Introduced support for extension signature validation and policy enforcement to improve the security of VM extensions.
* **Memory Management**: Implemented memory quota management using cgroups to ensure the agent maintains a predictable resource footprint.
* **Enhanced Reliability**: Improved telemetry and retry strategies for extension artifact downloads, along with more robust log collection handling.
* **Documentation**: Added a new `waagent` manpage for better local access to command-line documentation.

To overcome the former issues around password-changing functionality it will now utilize sha512_crypt of python3-passlib to be compatibly with python 3.13 that removed crypt.

For further details on the changes in this update, please refer to the upstream release notes:

* [v2.12.0.2](https://github.com/Azure/WALinuxAgent/releases/tag/v2.12.0.2)
* [v2.13.1.1](https://github.com/Azure/WALinuxAgent/releases/tag/v2.13.1.1)
* [v2.14.0.1](https://github.com/Azure/WALinuxAgent/releases/tag/v2.14.0.1)
* [v2.15.0.1](https://github.com/Azure/WALinuxAgent/releases/tag/v2.15.0.1)

### s390X

Nothing yet.

<h1 id="heading--official-flavours">Official flavours</h1>

Find the release notes for the official flavours at the following links:

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

<h1 id="heading--more-information">More information</h1>

## Reporting bugs

Your comments, bug reports, patches and suggestions help fix bugs and improve the quality of future releases. Please [report bugs using the tools provided](http://help.ubuntu.com/community/ReportingBugs). If you want to help with bugs, the [Bug Squad](http://wiki.ubuntu.com/BugSquad) is always looking for help.

## What happens if there is a high or critical priority CVE during release day?

Server, Desktop and Cloud plan to release in lockstep on release day, but there are some exceptions.

In the unlikely event that a critical or high-priority CVE is announced on release day, the release team have agreed on the following plan of action:

* For critical priority CVEs, the release of Server, Desktop and Cloud will be blocked until new images can be built addressing the CVE.

* For high-priority CVEs, the decision to block release will be made on a per-product (Server, Desktop and Cloud) basis and will depend on the nature of the CVE, which might result in images not being released on the same day.

This was discussed in the [ubuntu–release mailing list March/April 2023](https://lists.ubuntu.com/archives/ubuntu-release/2023-April/005610.html).

The mailing list thread also confirmed there is no technical or policy reason why a package cannot be pushed to the Updates or Security pocket to address high or critical-priority CVEs prior to the release.

## Participate in Ubuntu

If you would like to help shape Ubuntu, look at the list of ways you can participate at [community.ubuntu.com/contribute](https://community.ubuntu.com/contribute).

## More about Ubuntu

You can find out more about Ubuntu on the [Ubuntu website](https://ubuntu.com).

To sign up for future Ubuntu development announcements, subscribe to Ubuntu’s development announcement list at [ubuntu-devel-announce](https://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce).
