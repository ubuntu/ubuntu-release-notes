---
tocdepth: 3
---

(ubuntu-26.04-lts-changes-since-25.10)=
# Ubuntu 26.04 LTS changes since 25.10

If you're upgrading to Ubuntu 26.04 LTS from the previous interim release, Ubuntu 25.10 (Questing Quokka), the following changes apply to you.

:::{warning}
Ubuntu 26.04 LTS is currently in development, scheduled to be released in April 2026. See the {ref}`release schedule <resolute-raccoon-schedule>`.
:::

## New features and improvements

### System features

#### cloud-init v. 26.1

Cloud-init features introduced beyond v. 25.3 in Questing:

* Add support for s390x platform detection on LXD
* Add support for Tilaa cloud platform detection.
* Fix LXD Snap installs on Plucky and newer
* Scaleway cloud to support exposing regions and availability zones, drop private IP handling
* Add network v1 support for bonds, bridges and VLANs
* Allow `network-config` to express `allow_accept_ra` for bonds, bridges and VLANsOpenStack `network_data.json` support of bond names

See [cloud-init’s release notes for more details](https://github.com/canonical/cloud-init/releases).

#### fwupd

Systems running TPM/FDE will now prompt for the recovery key before firmware updates that may require the recovery key upon reboot.

#### Linux kernel 7.0 🐧

* `cgroupfs` is now mounted with `nsdelegate,memory_recursiveprot,memory_hugetlb_accounting`

#### Netplan v1.1.2 🌐

...

#### Package Management: APT 3.0

...

#### sudo-rs

Password feedback is now enabled by default in order to improve the user experience of `sudo`.
If the previous behavior is preferred, password feedback can be disabled using the following steps:

1. Edit sudoers using `sudo visudo` in the terminal
2. Add the option `Defaults !pwfeedback` to the configuration file

#### systemd 259.5

The `systemd` service manager has been updated to version 259. For a complete list of changes, see the [changelog](https://github.com/systemd/systemd/releases/tag/v259).

Also, refer to the removed and deprecated functionality:

* {ref}`cgroup-v1-removed`
* {ref}`system-v-scripts-deprecated`

#### TPM/FDE

...

#### Ubuntu Insights integration with the release upgrader

When Ubuntu Insights is available and configured, the release upgrader will now use Ubuntu Insights at the end of a release upgrade to generate a report based on the existing consent state. Note, this change does not prevent the Ubuntu Report-based collection that may be triggered by a release upgrade.

This change only affects Desktop and WSL since presently, these are the only platforms that include Ubuntu Insights.

(ibm-z15-level)=
#### IBM Z and LinuxONE (s390x)

The following provides an overview of selected and significant s390x-specific enhancements and improvements that landed in Ubuntu Server 26.04 for IBM Z and LinuxONE.

On the IBM Z (s390s) architecture, the architectural level set (ALS) was raised to build for IBM Z generation z15 (LinuxONE Emperor III) with the `march=z15` and `mtune=z16` compiler options ([LP: #2126577](https://launchpad.net/bugs/2126577)). This brings performance improvements on the later generations

{ref}`ibm-z14-support-removed`.

With every new Ubuntu Server release the `s390-tools` package was gradually upgraded to its latest available release v2.41 ([LP: #2141945](https://launchpad.net/bugs/2141945)), that now:

* adds a `udev` rule to set `none` as default I/O scheduler for `virtio-blk` devices ([LP: #2138886](https://launchpad.net/bugs/2138886))
* adds a `udev` rule to disable the `rotational` attribute for `virtio-blk` (especially important for swapping or paging) ([LP: #2138887](https://launchpad.net/bugs/2138887))
* introduces the new `pvverify` tool, that allows to verify host key documents in the context of Secure Execution (SE) ([LP: #2138888](https://launchpad.net/bugs/2138888))
* and the `pvimg info` command was enhanced to display additional SE image information ([LP: #2141952](https://launchpad.net/bugs/2141952))

KVM enhancements arrived by adding zVDT Parallel Sysplex support ([LP: #2142654](https://launchpad.net/bugs/2142654)) and by rewriting `gmap` using MMU notifiers ([LP: #2142682](https://launchpad.net/bugs/2142682)).

In the area of cryptography the following updates and improvements happened:

* `zkey` support for `dm-integrity` with HMAC was added to the `s390-tools` package ([LP: #2096889](https://launchpad.net/bugs/2096889)) and to the kernel ([LP: #2138650](https://launchpad.net/bugs/2138650))
* PHMAC was added to `cryptsetup` ([LP: #2138512](https://launchpad.net/bugs/2138512)), and required also `systemd` ([LP: #2138511](https://launchpad.net/bugs/2138511)) updates.
* The default use of clear keys by PAES and PHMAC in-kernel crypt modules was disabled ([LP: #2139610](https://launchpad.net/bugs/2139610)), but they can still be explicitly allowed with a module parameter.
* An overwrite function was added to the `zcrypt` driver, allowing the configuring of the device driver on a per APQN basis ([LP: #2138854](https://launchpad.net/bugs/2138854))
* The upgrade to `opecryptoki` v3.26 ([LP: #2135123](https://launchpad.net/bugs/2135123)) added ML-KEM and ML-DSA support for `ep11` token ([LP: #2138514](https://launchpad.net/bugs/2138514)) and `cca` token ([LP: #2138515](https://launchpad.net/bugs/2138515)) and BLS support for `ep11` token ([LP: #2138804](https://launchpad.net/bugs/2138804)).
* The upgrade of `libzpc` to v1.4.1 ([LP: #2136312](https://launchpad.net/bugs/2136312)) removed a protected key verification pattern mismatch, now allowing to support Live Guest Relocation ([LP: #2140342](https://launchpad.net/bugs/2140342))

The kernel also received selected improvements, like support for 128 KB tape block sizes ([LP: #2141569](https://launchpad.net/bugs/2141569)) and support for dynamic (de)configuration of hot-pluggable memory ([LP: #2142862](https://launchpad.net/bugs/2142862)).

Finally several packages were updated to their latest upstream version to pick up s390x-specific upstream fixes and improvements. For example:

* `valgrind`, for full z17 support ([LP: #2139096](https://launchpad.net/bugs/2139096))
* `libdfp`, mainly fixes ([LP: #2122325](https://launchpad.net/bugs/2122325))
* `smc-tools` for fixes and additional statistics output ([LP: #2142098](https://launchpad.net/bugs/2142098))

#### Updated cryptography libraries

Cryptography libraries have been updated to recent versions:

* OpenSSL has been updated to the latest upstream LTS [3.5.6](https://launchpad.net/ubuntu/+source/openssl) version
* GnuTLS to version 3.8.12
* NSS to version [3.120](https://launchpad.net/ubuntu/+source/nss/2:3.120-1ubuntu2)
* `libgcrypt` to version 1.12.0
* `libsodium` to version 1.0.18 (includes security fixes from [1.0.21](https://github.com/jedisct1/libsodium/releases/tag/1.0.21-RELEASE))

### Desktop features

#### GNOME 50

The GNOME desktop environment has been updated to version 50.

#### GStreamer 1.28

The GStreamer multimedia framework has been updated to [version 1.28](https://gstreamer.freedesktop.org/releases/1.28/).

#### Added graphical Ubuntu Insights management controls to Settings

Graphical controls to finely control Ubuntu Insights consent states as well as to preview reports have been added to Settings. They can be found under *Privacy & Security* within the *Telemetry* panel, which also replaces the *Diagnostics* panel.

#### Prompt for Ubuntu Insights consent on release upgrades

After a release upgrade, you'll be prompted for consent to collect system information via Ubuntu Insights. This prompt only appears if Ubuntu Insights consent isn't already set or if it's deemed necessary to re-prompt due to any other reason.

This change is part of creating a new release upgrade mode for GNOME Initial Setup.

### Server features

#### Chrony 4.8

Chrony was updated to version 4.8, which adds support for limiting the selection of unreachable sources, fixes `refclock` handling on newer kernels and more.

For more information about the 4.8 release or all the other changes since version 4.5 that was in Noble please have a look at [Chrony’s news page](https://chrony-project.org/news.html).

#### Exim4

The Exim4 update to 4.99.1 improves handling many messages to a single host by using fewer forks & execs. New options like `dkim_verify_minimal` avoid calling the DKIM ACL after the first good verify and fix various bugs.

For a detailed list of changes please refer to the [upstream changelog](https://github.com/Exim/exim/blob/master/doc/doc-txt/ChangeLog#L84). The minor .1 in 4.99.1 ensures that recent re-occurring security issues of CVE-2025-26794 and CVE-2025-67896 are closed right away.

#### Kerberos

Kerberos has been configured to observe the `/etc/krb5.conf.d/` directory by default. This introduces support for third-party packages that need to add Kerberos configuration.

* If you have existing configuration snippets in `/etc/krb5.conf.d/`, but do not include them, they will now be included in the `krb5.conf` file.
* If you already include `/etc/krb5.conf.d/` in your `krb5.conf` file, either active or commented out, no changes will be made.
* If your existing `krb5.conf` file is a symbolic link, no changes will be made.

MIT Kerberos and Heimdal are both supported, but use different orderings for the include directive. MIT Kerberos uses alphanumerical order, while Heimdal uses the unpredictable order of the `readdir()` system call ([LP: #2140967](https://bugs.launchpad.net/ubuntu/+source/heimdal/+bug/2140967))

#### `multipath-tools` 0.12.2

Updated from version 0.11.1 to 0.12.2. See the 0.12 series in the [upstream changelog](https://github.com/opensvc/multipath-tools/blob/0.12.2/NEWS.md).

#### OpenLDAP

New version [2.6.10](https://launchpad.net/ubuntu/+source/openldap).

* Running in [AppArmor enforce mode](https://documentation.ubuntu.com/server/how-to/security/apparmor/) now.
* Added patch to support changing `pbkdf2` iteration count (see task [#2125685](https://bugs.launchpad.net/ubuntu/+source/openldap/+bug/2125685))

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
* NetBios is disabled by default in the configuration file `/etc/samba/smb.conf` for fresh installs

(26.04-sssd-2.12)=
#### SSSD

```{include} /reuse/26.04/sssd-2.12-features.txt
```

See also {ref}`26.04-sssd-changes`.

Other changes of importance are listed upstream:

* https://sssd.io/release-notes/sssd-2.11.0.html
* https://sssd.io/release-notes/sssd-2.12.0.html

#### Squid

```{include} /reuse/26.04/squid-7.2-features.txt
```

See also {ref}`26.04-squid-removals`.

For a list of all changes and fixes, please check the [upstream releases page](https://github.com/squid-cache/squid/releases).

#### SoS (`sosreport`)

SoS was updated to 4.10.2. This upgrade introduces new plugins and also adds new features to existing plugins.

For more information see the [4.10.1](https://github.com/sosreport/sos/releases/tag/4.10.1) and [4.10.2](https://github.com/sosreport/sos/releases/tag/4.10.2) upstream release notes.

#### Colored output with `strace` 6.19

```{include} /reuse/26.04/strace-6.19.txt
```

#### Container stack

For the `containerd` and `runc` packages, we established a pattern to either keep the regular updates to the latest version or to opt for slower, more stable updates throughout the time the release is active. For more please read [Ubuntu Server Gazette - Issue 8 - Containers: Steady paths for agile stacks](https://discourse.ubuntu.com/t/ubuntu-server-gazette-issue-8-containers-steady-paths-for-agile-stacks/68680).

#### containerd 2.2.2

The `containerd` packages (`src:containerd-app`, `src:containerd-stable`) were updated to version 2.2.2 Version 2 includes the stabilization of new features added in the last 1.x release as well as the removal of features which were deprecated in 1.x, meaning you should expect breaking changes here.

For further details on such changes, please refer to the `containerd` 2.0 [upstream release notes](https://github.com/containerd/containerd/blob/main/docs/containerd-2.0.md) and check the notes for [individual point releases](https://github.com/containerd/containerd/releases).

#### runc 1.4.0

The `runc` package (`src:runc-app`) was updated to version 1.4.0. The most noteworthy change here is that the handling of `pids.limit` has been updated to match the newer guidance from the OCI runtime specification. In particular, now a maximum limit value of 0 will be treated as an actual limit (it will be treated the same as a limit value of 1). We only expect users that explicitly set `pids.limit` to 0 will see a behavior change.

For more details on this new release, please [check the upstream release notes](https://github.com/opencontainers/runc/releases/tag/v1.4.0).

#### Docker 29

[docker.io](http://docker.io) was updated to version 29. This release includes several improvements and breaking changes.

There is a new experimental support for `nftables` which can be enabled by setting Docker daemon’s firewall-backend option to `nftables`.

The `containerd` image store is now the default for **fresh installs**. This doesn’t apply to daemons configured with `userns-remap` or for users upgrading from a previous [docker.io](http://docker.io) version.

The `docker image ls` command output has changed to use a new view (like `--tree` but collapsed) by default.

For a comprehensive list of changes, please check the [upstream release notes](https://docs.docker.com/engine/release-notes/29/).

#### Virtualization stack

The virtualization stack got various updates and to provide more flexibility an additional
hardware enablement option was added that will in addition allow to switch to the
virtualization stack of the following interim releases while otherwise staying on the LTS.

#### libvirt

The libvirt package was upgraded to version 12.0.0. Here is the important changes since Ubuntu Questing:

* Several new features have been added into the `bhyve` driver:

* Experimental NAT networking support using the Packet Filter (`pf`) firewall.

* Querying domain block, interface, and memory statistics. Not all statistics fields are supported though.

* SLIRP networking support

* NVMe device support

* `virtio-scsi` support

* Initial ARM64 support

* Multi-GPU: Add support for NUMA affinity of PCI devices

To support NVIDIA Multi-Instance GPU (MIG) configurations, `libvirt` now handles QEMU’s `acpi-generic-initiator` device internally. MIG enables partitioning a physical GPU into multiple isolated instances, each associated with one or more virtual NUMA nodes.

* Hyper-V:

  * Introduce Hyper-V host-model mode

* Hyper-V `virttype` support for Qemu domains

For more details, please see the [upstream changelog](https://libvirt.org/news.html#v12-0-0-2026-01-15)

Some additional notable changes:

* The detection of the CPU MSR (Model Specific Register) features has been improved by enabling the `msr` kernel module load and fixing `vmx-*` features detection issue.

* Use `sysusers` to manage users and groups

#### QEMU

The QEMU package was upgraded to version 10.2.1. Here is the important changes since Ubuntu Questing:

Upgrading Windows 11 makes the VM stop working and to fix this issue and ensure the migration path, we added new machine types for Resolute and old Ubuntu releases:

* `pc-i440fx-questing-v2` Ubuntu 25.10 PC v2 (i440FX + PIIX, + 10.1 machine, 1996)

* `pc-i440fx-noble-v2`   Ubuntu 24.04 LTS PC v2 (i440FX + PIIX, `arch-caps` fix, 1996)

* `pc-q35-noble-v2`      Ubuntu 24.04 LTS PC v2 (Q35 + ICH9, `arch-caps` fix, 2009)

Other notable new features:

* ARM

  * New board model: `amd-versal2-virt`

  * New CPU architectural features emulated: `FEAT_TCR2`, `FEAT_CSSC`, `FEAT_SCTLR2`.

* RISC-V

  * Add `riscv64` to `FirmwareArchitecture`

  * Implement MonitorDef HMP API

* X86

  * Support for a new accelerator, MSHV, which lets you create VMs from a Hyper-V guest without using nested virtualization.

* Migration:

  * Supported new `cpr-exec` migration mode

  * Supported `mapped-ram` on snapshot save/load

For more details, please see related upstream [changelog](https://wiki.qemu.org/ChangeLog/10.2) and the general log on [removed features](https://qemu-project.gitlab.io/qemu/about/removed-features.html)

#### EDK2

The package has been updated to version **2025.11**. Below are the most significant changes since Ubuntu Questing:

OVMF packaging rework

: * OVMF has been split into the following packages:

    * `ovmf-generic`

    * `ovmf-amdsev`

    * `ovmf-inteltdx`

  * The `ovmf` package is now a **metapackage** that depends on the above variants.
    This allows users to install only the OVMF firmware compatible with their CPU.

`ovmf-inteltdx` changes

: * `OVMF.inteltdx.fd` has been removed.

  * `OVMF.inteltdx.secboot.fd` has been renamed to `OVMF.inteltdx.ms.fd`.

Removed components

: * `qemu-efi-arm`

  * `ovmf-ia32`

  * The `loongarch64` target is no longer built.

Secure Boot improvements

: * NX is now enabled in all Secure Boot variants.

  * The `strictnx` variant has been dropped.

New package

: * Introduced `ovmf-legacy`, providing `OVMF.legacy.fd` with PVSCSI support.

Further details on new features and bug fixes are available in the upstream changelogs:

* [edk2-stable202505](https://github.com/tianocore/edk2/releases/tag/edk2-stable202505)

* [edk2-stable202508](https://github.com/tianocore/edk2/releases/tag/edk2-stable202508)

* [edk2-stable202511](https://github.com/tianocore/edk2/releases/tag/edk2-stable202511)

#### DocumentDB

```{include} /reuse/26.04/documentdb-0.108-0-features.txt
```

#### MariaDB is fully supported

MariaDB was updated to the latest LTS version 11.8.6.
For more information on the MariaDB LTS, see the [upstream release notes](https://mariadb.com/docs/release-notes/community-server/11.8).

Starting with 26.04, MariaDB will now be provided with [full support in Ubuntu main](https://bugs.launchpad.net/ubuntu/+source/mariadb/+bug/2122095).

MariaDB was updated to the latest LTS version 11.8.6. For more information on the MariaDB LTS, [see the upstream release notes](https://mariadb.com/docs/release-notes/community-server/11.8).

The MySQL and MariaDB servers are mutually exclusive on Ubuntu for now.

#### MySQL

MySQL’s current LTS version 8.4 is provided in Ubuntu 26.04 LTS, starting with version 8.4.8. Future security fixes will be provided by 8.4.x version updates. For more information see the [upstream release notes](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/).

#### MySQL Shell

MySQL Shell was updated to the latest LTS version, 8.4.8, to match MySQL’s version. See the [upstream release notes](https://dev.mysql.com/doc/relnotes/mysql-shell/8.4/en/) for more information.

#### Percona Toolkit

Percona Toolkit was updated to the latest version, 3.7.1, and now includes additional tools for managing your MySQL, MariaDB, or PostgreSQL server. This includes `pt-galera-log-explainer`, `pt-k8s-debug-collector`,  and `pt-pg-summary` among others.

#### PostgreSQL

```{include} /reuse/26.04/postgresql-18-features.txt
```

#### Valkey

```{include} /reuse/26.04/valkey-9.0-features.txt
```

#### fence-agents

`fence-agents` is updated to version 4.17.0. This version includes a few new agents, like `aws_vpc_net` and `hetzner_cloud`, and enhancements to the existing ones.

In terms of security, the `azure_arm` agent replaced the dependency on `msrestazure` (deprecated) to `azure-identity`.

For a list of all changes, please refer to the [upstream changes](https://github.com/ClusterLabs/fence-agents/compare/v4.16.0...v4.17.0).

#### resource-agents

`resource-agents` is updated to version 4.17.0. This version includes several new agents, like `aws-datasync-*` and `tickle-*`, and enhancements to the existing ones.

For a list of all changes, please refer to the [upstream release notes](https://github.com/ClusterLabs/resource-agents/blob/main/ChangeLog).

#### HAProxy

HAProxy was updated to the latest upstream LTS release, 3.2, which introduces performance and efficiency improvements, faster and more reliable QUIC protocol support, and more. For further details on this new release, please check the HAProxy 3.2 [upstream announcement](https://www.mail-archive.com/haproxy@formilux.org/msg45917.html).

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

To overcome the former issues around password-changing functionality it will now utilize sha512_crypt of python3-passlib to be compatible with python 3.13 that removed crypt.

For further details on the changes in this update, please refer to the upstream release notes:

* [v2.12.0.2](https://github.com/Azure/WALinuxAgent/releases/tag/v2.12.0.2)
* [v2.13.1.1](https://github.com/Azure/WALinuxAgent/releases/tag/v2.13.1.1)
* [v2.14.0.1](https://github.com/Azure/WALinuxAgent/releases/tag/v2.14.0.1)
* [v2.15.0.1](https://github.com/Azure/WALinuxAgent/releases/tag/v2.15.0.1)

#### OpenStack 2026.1 Gazpacho

OpenStack has been updated to the [2026.1 Gazpacho](https://releases.openstack.org/gazpacho/index.html) release. Gazpacho is a [SLURP](https://releases.openstack.org/) release, supporting direct upgrades from the previous SLURP release (2025.1 Epoxy). This includes packages for Aodh, Barbican, Ceilometer, Cinder, Designate, Glance, Heat, Horizon, Ironic, Keystone, Magnum, Manila, Masakari, Mistral, Neutron, Nova, Octavia, Placement, Swift, Watcher, and Zaqar.

Eventlet migration
: Multiple projects completed or advanced the migration from Eventlet to native Python threading, including Cyborg, Designate, Manila (technology preview), Nova (experimental), and Watcher. This long-running effort modernizes OpenStack's concurrency model for long-term sustainability. Operators should review per-service concurrency configuration before upgrading.

Nova (Compute)
: Parallel live migrations improve memory transfer speed via multi-connection support. `IOThread` is now enabled by default for QEMU instances, offloading disk I/O from vCPU threads. Live migration of instances with vTPM devices is now supported in host secret security mode. The volume-attach API is asynchronous starting from microversion 2.101, and UEFI firmware selection is now delegated to `libvirt`. Full OpenAPI schema coverage has been achieved across all Nova API endpoints.

Neutron (Networking)
: A new network IP availability details API extension provides richer subnet and allocation pool usage information. OVN BGP capabilities have been integrated into the Neutron OVN driver, and ML2/OVN now supports North/South routing for external (SR-IOV, bare metal) ports as well as allowed address pairs with virtual MAC addresses. Additional OVN configuration options improve scalability.

Ironic (Bare Metal)
: NFS and CIFS/SMB transport protocols are now supported for Redfish Virtual Media boot. Two new deploy interfaces have been added: `autodetect` (selects the best interface automatically) and `noop` (marks nodes active without deploying an OS). A new standalone networking service enables physical switch management without Neutron, and VXLAN/Geneve overlay networks are now supported for bare metal nodes.

Manila (Shared File Systems)
: QoS type support allows administrators to define throughput and IOPS limits via share type extra-specs or dedicated QoS type entities. Share replica metadata, custom export locations during share management, and new back-end drivers for HPE Alletra MP B10000 are included.

Horizon (Dashboard)
: Live migration with Nova microversion 2.30 is now supported, and the Key Pairs page has been rewritten from AngularJS to Python/Django. A new configuration option avoids full container listings in the Swift panel, reducing resource consumption.

For the full list of [upstream release highlights](https://releases.openstack.org/gazpacho/highlights.html), see the OpenStack 2026.1 Gazpacho documentation.

### Development features

#### Toolchain upgrades 🛠️

* `glibc` 2.42 now ships non-UTF8 encodings as `libc-gconv-modules-extra`.
* LLVM 21 is the default LLVM toolchain.
* Rust 1.93.1 is the default Rust toolchain.

#### OpenJDK

OpenJDK 25 package is the default and is TCK (Technology Compatibility Kit) certified on AMD64, ARM64, S390X, PPC64EL. The Java TCK is the most comprehensive test suite that covers all aspects of Java SE specification including language features, libraries and APIs. This guarantees interoperability and conformance to standard.

#### .NET

...

#### Rust + cargo-auditable

Rust packages built on Launchpad now have opt-in [cargo-auditable](https://github.com/ubuntu/ubuntu-release-notes) support.
If enabled, binaries will include JSON-formatted metadata in a header section of the binary expressing the dependencies used to compile the binary.
If a CVE is discovered in a popular Rust crate, this dependency metadata lets users and sysadmins immediately check if a binary is compromised.

For example, the dependency metadata for {manpage}`sudo-rs(1)` looks like this:

```json
{
  "format": 1,
  "packages": [
    {
      "name": "glob",
      "source": "crates.io",
      "version": "0.3.2"
    },
    {
      "name": "libc",
      "source": "crates.io",
      "version": "0.2.174"
    },
    {
      "name": "log",
      "source": "crates.io",
      "version": "0.4.27"
    },
    {
      "dependencies": [0, 1, 2],
      "name": "sudo-rs",
      "root": true,
      "source": "local",
      "version": "0.2.8"
    }
  ]
}
```

```{admonition} Pretty printed
This has been pretty-printed for ease of readability. In real life the data is minified and compressed.
```

We have enabled cargo-auditable support for a few well-known Rust packages:
- `alacritty`
- `bat`
- `du-dust`
- `eza`
- `fd-find`
- `hyperfine`
- `ripgrep`
- `sd`
- `sudo-rs`

We encourage developers to turn on cargo-auditable support for their own packages!

For more information, including how to opt in, see the [Ubuntu project documentation](https://documentation.ubuntu.com/project/contributors/language-specific/rust/cargo-auditable/).

## Backwards-incompatible changes

### System changes

(cgroup-v1-removed)=
#### `cgroup` v1 support has been removed

`systemd` version 259 no longer supports `cgroup` v1 (`legacy` and `hybrid`) hierarchies. As a result:

  * Ubuntu installations running `cgroup` v1 will not be allowed to upgrade to Ubuntu 26.04 LTS.
  * Ubuntu 26.04 LTS container workloads will not run on a host booted with `cgroup` v1.
  * Ubuntu 26.04 LTS hosts do not support container workloads that require `cgroup` v1: for example, Ubuntu earlier than 18.04 LTS.

This change was made in `systemd` version 258. See the [changelog](https://github.com/systemd/systemd/releases/tag/v258) for more information.

#### Removable media are mounted under `/run/media`

In previous Ubuntu releases, removable media were mounted under the `/media` directory. Starting with Ubuntu 26.04 LTS, `/run/media` is now the mount directory instead. This has several benefits:

- Better support for read-only root file systems
- Better alignment with other distributions and upstream defaults
- Not requiring special cleanup routines because `/run` is hosted on a virtual memory file system (`tmpfs`)

If you rely on the specific directory path for media access, check that your setup still works. For example, test your existing scripts.

[LP#2130110](https://bugs.launchpad.net/ubuntu/+source/udisks2/+bug/2130110)

(ibm-z14-support-removed)=
#### Ubuntu no longer supports IBM Z generations z14 or older

On the IBM Z (s390s) architecture, the architectural level set (ALS) was raised to build for IBM Z generation z15 ([LP: #2126577](https://launchpad.net/bugs/2126577)). As a result, Ubuntu 26.04 LTS no longer works on IBM Z generations z14 (LinuxONE II) or older. You can't install Ubuntu 26.04 LTS on this hardware or upgrade to it. The `ubuntu-release-upgrader` prevents you from performing the upgrade.

IBM Z generation z14 (LinuxONE II) is still supported by Ubuntu Server 24.04 LTS for up to 15 years in total.

### Desktop changes

#### Google Drive integration in Files has been removed

The GNOME Online Accounts (GOA) service has removed Google Drive integration. As a result, you can no longer mount your Google Drive storage in the Files app.

The feature was removed because the `libgdata` library, which enabled the integration, has been unmaintained and posed a security risk.

You can still access Google Drive through your web browser.

### Server changes

#### TLS 1.0 and 1.1 disabled in Apache

The Debian changes for the new version of Apache have disabled TLS 1.0 and 1.1, following RFC 8996. These should be already disabled by default in OpenSSL, and now Apache follows the same. See [the fixed bug](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=943415).

#### NFS

The `blkmapd` and `nfs-blkmap` services have been removed. From the `NEWS` file:

> pNFS block layout is deprecated in favor of pNFS SCSI layout. This is  because block layout could easily result in data loss, as documented in <https://linux-nfs.org/wiki/index.php/PNFS_block_server_setup>.
>
> Users of pNFS are advised to move to the revised SCSI/NVMe layouts  that are safe to use and don't require the use of blkmapd.

(26.04-sssd-changes)=
#### Breaking changes in SSSD

```{include} /reuse/26.04/sssd-2.12-changes.txt
```

Other changes of importance are listed upstream:

* https://sssd.io/release-notes/sssd-2.11.0.html
* https://sssd.io/release-notes/sssd-2.12.0.html

#### Breaking changes in PHP

* It is no longer possible to use `array` and `callable` as class alias names in `class_alias()`.

Other breaking changes and new features can be seen in the [full upstream changelog](https://www.php.net/ChangeLog-8.php#PHP_8_5).

(26.04-squid-removals)=
#### Removed options and directives in Squid

```{include} /reuse/26.04/squid-7.2-removals.txt
```

For a list of all changes and fixes, please check the [upstream releases page](https://github.com/squid-cache/squid/releases).

#### Kerberos removes deprecated algorithms from its default lists

MIT Kerberos no longer includes the `arcfour-hmac-md5` and the `des3-cbc-sha1` algorithms in its default encryption algorithm list (the `openssh` and `krb5` lists). They are weak, deprecated algorithms. Before, `krb5` would include them in its default algorithm lists when users do not specify a list with algorithms to be used.

Note that we did not remove support for those algorithms. Instead we just dropped them from the default list that the client will try in case the user do not specify any algorithms in their configuration file in the `permitted_enctypes` directive in the `libdefaults` section in `/etc/krb5.conf`.

#### PostgreSQL is no longer available on i386

PostgreSQL 18 in Ubuntu 26.04 LTS no longer builds for the i386 architecture. Therefore, it no longer produces the `libpq-dev` and `libpq5` binary packages for that architecture. This means that any package depending on those libraries will also not be available in i386.

See [LP: #2142320](https://bugs.launchpad.net/ubuntu-release-notes/+bug/2142320) for more information.

#### Replaced agents in `resource-agents`

The `oracledb` and `zabbixagent` agents were replaced by the `oracle` and `zabbix-agent`, respectively. You might need to adjust your existing configuration.

#### Microsoft Azure

`Azure Disk Encryption` (ADE) is scheduled for retirement on September 15, 2028. A number of packages were historically pre-installed on Azure images to allow the enablement of ADE without requiring additional package installations. Due to its impending retirement, Ubuntu on Azure will no longer maintain the enablement of ADE without additional package installations. Accordingly, the following packages have been removed from one or more Ubuntu image-lines on Azure:

`python3-parted`
: This package is largely unsupported by its maintainers, imposing a potential security risk into the future. Its only known use was for the enablement of ADE. It is no longer pre-installed on any Ubuntu image on Azure.

`python3-six`
: The only known use of this package was for the enablement of ADE. It is no longer pre-installed on any Ubuntu image on Azure.

`lsscsi`
: This package was initially introduced to support ADE. It has been removed from all minimal Ubuntu image-lines to maintain the minimal footprint assertion. However, it remains a pre-installed package for all non-minimized Ubuntu images on Azure since it is a valuable debugging tool for individual instances and server deployments.

#### Google Cloud

As all `AMD64` images are now built with `AMD64v3` the following CPU platforms (available on `N1` machine types only) are no longer supported:
* Intel Ivy Bridge
* Intel Sandy Bridge

<!--
### Development changes

### Enterprise changes
-->

#### Removed features in OpenStack

The Manila V1 API and the Manila shell utility have been removed.

For details, see the Manila [release highlights](https://releases.openstack.org/gazpacho/highlights#manila) and [release notes](https://docs.openstack.org/releasenotes/manila/2026.1.html).

<!--
### Security changes
-->

## Deprecated features

### System deprecations

(system-v-scripts-deprecated)=
#### Legacy System V service scripts are deprecated

Ubuntu 26.04 LTS is the last release that supports System V service scripts compatibility in `systemd`. Migrate your legacy System V scripts to native `systemd` unit files.

`systemd` version 260 [has already dropped support](https://github.com/systemd/systemd/releases/tag/v260), so this change will take effect in Ubuntu 26.10.

### Desktop deprecations

...

### Server deprecations

#### PHP

* Deprecation of the backtick operator
* Non-canonical cast names (boolean), (integer), (double), and (binary) have been deprecated. (bool), (int), (float), and (string) need to be used instead.
* Using null as an array offset or when calling array_key_exists() is now deprecated - now an empty string is needed.

Other breaking changes and new features can be seen in the [full upstream changelog](https://www.php.net/ChangeLog-8.php#PHP_8_5).

<!--
### Development deprecations

### Enterprise deprecations

### Cloud deprecations

### Security deprecations

### Hardware support deprecations
-->

## Bug fixes

### Desktop fixes

...

### Server fixes

#### Apache 2.4.65

Apache has been updated to upstream version 2.4.65. For more details, see the [upstream release notes](https://www.apachelounge.com/Changelog-2.4.html).

#### Nginx 1.28.2

Nginx was updated to version 1.28.2, which includes fixes for various bugs. See the [1.28 series upstream release notes](https://nginx.org/en/CHANGES-1.28).

#### Django 5.2.9

Django was updated to LTS version 5.2.9. For more information, see the [Django 5.2 release notes](https://docs.djangoproject.com/en/6.0/releases/5.2/).

#### OpenSSH 10.2

OpenSSH was updated to version 10.2, which is a bugfix release on top of 10.1 present in the Ubuntu Questing 25.10 release.

As per RFC 8732, gss-group14-sha1- and gss-gex-sha1- are considered deprecated algorithms and should not be used. Therefore, we dropped those deprecated algorithms from the Ubuntu GSS-API support patch. This does not mean those algorithms are no longer supported. Instead, they were removed from the default list that the client or the server will try for GSS key exchange in case the user does not specify any algorithms in their configuration file.

#### Dovecot 2.4.2

Updated to 2.4.2. See the [upstream announcement](https://dovecot.org/mailman3/archives/list/dovecot@dovecot.org/thread/XTMMPVQ3QKQMYDZ3CZZCXPNHN7OXKS3L/).

#### Postfix 3.10.6

Postfix was updated to version 3.10.6. See the [upstream announcement](https://www.postfix.org/announcements/postfix-3.10.6.html).

A noteworthy change in the packaging of Postfix is that **by default it is no longer installed in a `chroot`, and only limited `chroot` support is available from now on**.

#### `unbound` 1.24.2

Update to version 1.24.2. See the [upstream changelog](https://github.com/NLnetLabs/unbound/releases/tag/release-1.24.2).

<!--
### Development fixes

### Enterprise fixes

### Cloud fixes

### Security fixes

### Hardware support fixes

### Common fixes
-->


## Known issues

As is to be expected with any release, there are some significant known bugs that users may encounter with this release of Ubuntu. The ones we know about at this point (and some of the workarounds) are documented here, so you don’t need to spend time reporting these bugs again:

### System issues

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

* The new `gnome-initial-setup` has issues preventing it from working properly:
  - The selected key layout does not persist ([LP: #2127782](https://launchpad.net/bugs/2127782))
  - Time zone input dropdown can "wobble" ([LP: #2084611](https://launchpad.net/bugs/2084611))
  - The hostname change is mandatory ([LP: #2093132](https://launchpad.net/bugs/2093132))

* During boot on the server image, if your `cloud-init` configuration (in `user-data` on the boot partition) relies upon networking (importing SSH keys, installing packages, etc.) you *must* ensure that at least one network interface is required (`optional: false`) in `network-config` on the boot partition. This is due to Netplan changes to the `wait-online` service (~~[LP: #2060311](https://launchpad.net/bugs/2060311)~~). Furthermore, a current issue may cause `cloud-init` to run before the network is ready ([LP: #2144891](https://launchpad.net/bugs/2144891))

* With the removal of the `crda` package in 22.04, the method of setting the WiFi regulatory domain (editing `/etc/default/crda`) no longer operates. On server images, use the `regulatory-domain` option in the Netplan configuration. On desktop images, append `cfg80211.ieee80211_regdom=GB` (substituting `GB` for the relevant country code) to the kernel command line in the `cmdline.txt` file on the boot partition  ([LP: #1951586](https://launchpad.net/bugs/1951586)).

* Colors appear incorrectly in the Ubuntu App Center ([LP: #2076919](https://launchpad.net/bugs/2076919))

* On server images, re-authentication to WiFi APs when regulatory domain is set result in `dmesg` spam to the console ([LP: #2063365](https://launchpad.net/bugs/2063365))

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



### Desktop issues

#### Localization

The Live Session of the new Ubuntu Desktop installer is not localized. It is still possible to perform a non-English installation using the new installer, but internet access at install time is required to download the language packs. ([LP: #2013329](https://bugs.launchpad.net/ubuntu-release-notes/+bug/2013329))

#### Screen reader support

Screen reader support is present with the new desktop installer, but is incomplete ([LP: #2061015](https://launchpad.net/bugs/2061015), [LP: #2061018](https://launchpad.net/bugs/2061018), [LP: #2036962](https://launchpad.net/bugs/2036962), [LP: #2061021](https://launchpad.net/bugs/2061021))

#### OEM installs

OEM installs are not supported yet. ([LP: #2048473](https://launchpad.net/bugs/2048473))

#### Virtualized GTK 4 apps

GTK 4 apps (including the desktop wallpaper) do not display correctly with VirtualBox or VMWare with 3D Acceleration ([LP: #2061118](https://launchpad.net/bugs/2061118)).

#### Limitations of TPM-backed full disk encryption

TPM-backed full disk encryption (TPM/FDE) has been introduced to enhance data security. The following are its known issues and limitations as of the Ubuntu 26.04.0 LTS release:

* Some potentially eligible systems might be detected as **ineligible** for TPM/FDE.

* At boot, the PIN or passphrase prompt is set to the **keyboard layout** even if you set a custom layout on your system. To fix this problem, update to `snapd` 2.75.

* If you **forget the passphrase or PIN** and you boot your system with the recovery key, you can't remove or replace the passphrase or PIN anymore. On subsequent boots, you have to continue using your recovery key.

* **Disk re-encryption** is currently not supported.

* Certain **self-healing and reparation options** for defective systems after installation are currently missing.

* TPM/FDE requires a specific kernel snap which may not include certain **kernel modules** necessary for some hardware functionalities. A notable example is the `vmd` module required for **NVMe RAID** configurations.

    In scenarios where such specific kernel modules are needed, you might have to disable the hardware feature (such as RAID) in the firmware to ensure the continued availability of the affected hardware post-installation. If disabling in the firmware is not an option, the related hardware will not be available post-installation with TPM/FDE enabled.

    **Nvidia drivers** are the only out-of-tree kernel drivers supported by TPM/FDE. You can't install other third-party drivers using DKMS.

For other known issues, see [FDE specific bug reports](https://bugs.launchpad.net/bugs/+bugs?field.searchtext=&orderby=-importance&field.status%3Alist=NEW&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.tag=fde&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search).

#### Resuming from suspend on Nvidia

Resuming from suspend on Nvidia desktops (where Nvidia is the primary GPU so generally not laptops)  will exhibit visual corruption and freezes using the default Wayland session  ([LP#1876632](https://bugs.launchpad.net/bugs/1876632)). If you need suspend/resume support then the simplest solution is to select ‘Ubuntu on Xorg’ at the login screen.

#### Classic fonts

Installing `ubuntu-fonts-classic` results in a non-Ubuntu font being displayed ([LP#2083683](https://bugs.launchpad.net/bugs/2083683)). To resolve this, install `gnome-tweaks` and set ‘Interface Text’ to ‘Ubuntu’.

### Server issues

#### Apache2 security hardening breaks the `mod-php` JIT

The Apache2 `systemd` service unit now sets the `MemoryDenyWriteExecute=yes` option by default as a security hardening measure. This prevents simultaneously writable and executable memory mappings. However, it breaks PHP's JIT compiler when using the `libapache2-mod-php` module, producing warnings such as the following:

```text
Warning: preg_match(): Allocation of JIT memory failed, PCRE JIT will be disabled.
```

We recommend that you switch from `mod-php` to the `php-fpm` service, which isn't affected by the change.

If you want to continue using `mod-php`, override the setting by editing the Apache2 `systemd` unit:

1. Open the editor:

    ```
    sudo systemctl edit apache2
    ```

2. Uncomment and edit the following line and save:

    ```ini
    [Service]
    MemoryDenyWriteExecute=no
    ```

3. Restart Apache2:

    ```bash
    sudo systemctl restart apache2
    ```

See [LP: #2144455](https://bugs.launchpad.net/ubuntu-release-notes/+bug/2144455) and the [systemd.exec documentation](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html#MemoryDenyWriteExecute=) for more information.

#### PostgreSQL

As reported in a [Linux mailing list](https://lore.kernel.org/lkml/20260403191942.21410-1-dipiets@amazon.it/) thread, a change introduced in Linux 7.0 may cause a significant throughput and latency regression on PostgreSQL. As discussed in that [same thread](https://lore.kernel.org/lkml/yr3inlzesdb45n6i6lpbimwr7b25kqkn37qzlvvzgad5hfd7ut@xv4cihno76wu/), systems using huge pages are not affected. Hence, ensure your PostgreSQL deployments have huge pages on. Please refer to the PostgreSQL upstream documentation to ensure your system have [huge pages set](https://www.postgresql.org/docs/current/kernel-resources.html#LINUX-HUGE-PAGES), and that the [huge_pages configuration](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-HUGE-PAGES) is set to `on`.

<!--
#### Openstack

Currently, Nova Compute is non-functional because of a python3.13 incompatibility ([LP:#2103413](https://bugs.launchpad.net/ubuntu/+source/nova/+bug/2103413)).
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

### Cloud issues

#### Google cloud

On first boot, 26.04 images may be slowed by up to 30s due to an outstanding issue with `cloud-init` and `systemd` [(LP: #2148619)](https://bugs.launchpad.net/ubuntu/+source/systemd/+bug/2148619)

## Official flavors

Find the release notes for the official flavors at the following links:

* [Edubuntu Release Notes](https://discourse.ubuntu.com/t/edubuntu-26-04-beta-released/)
* [Kubuntu Release Notes](https://wiki.ubuntu.com/PluckyPuffin/ReleaseNotes/Kubuntu)
* [Lubuntu Release Notes](https://lubuntu.me/lubuntu-25-04-p-p-released/)
* [Ubuntu Budgie Release Notes](https://ubuntubudgie.org/blog/ubuntu-budgie-2604-lts-release-notes/)
* [Ubuntu MATE Release Notes](https://ubuntu-mate.org/blog/ubuntu-mate-p-p-release-notes/)
* [Ubuntu Studio Release Notes](https://discourse.ubuntu.com/t/ubuntu-studio-26.04-release-notes/)
* [Ubuntu Unity Release Notes](https://ubuntuunity.org/posts/ubuntu-unity-2504-released/)
* [Xubuntu Release Notes](https://wiki.xubuntu.org/releases/25.04/release-notes)
* [Ubuntu Kylin Release Notes](https://ubuntukylin.com/news/ubuntukylin2504-en.html)
* [Ubuntu Cinnamon Release Notes](https://ubuntucinnamon.org/?p=1348)
