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

<!--
:::{rubric} GNOME 50
:::

The GNOME desktop environment has been updated to version 50:

* New application
* Improved rendering

:::{versionadded} 26
:::
-->

#### Gaming

:::{versionadded} 25.04
A new NTSYNC driver that emulates WinNT sync primitives is available, delivering better performance potential for Windows games running on Wine and Proton (Steam Play).
:::

### Server

### Development

* GCC 🐄 is updated to 15.2, binutils to 2.45, and glibc to 2.42
* Python 🐍 is updated to 3.13.7 while 3.14 is now available
* LLVM 🐉 defaults to version 20 while 21 is now available
* Rust 🦀 toolchain defaults to version 1.85 while 1.88 is now available
* Golang 🐀 is updated to 1.24
* Zig ⚡ is available for the first time in Ubuntu, defaults to version 0.14.1.
* And Ubuntu Toolchains has a new [homepage](https://ubuntu.com/toolchains)

:::{versionadded} 25.04
The `bpftools` and `linux-perf` tools have been decoupled from the kernel version, making dependency management easier for developers working with containers. These tools are now shipped in their own packages.
:::

#### OpenJDK

OpenJDK ☕ defaults to 21 (LTS), while version 25 (LTS) and an early access snapshot of version 26 are now available.

:::{versionadded} 24.10
OpenJDK 21 is still the default. OpenJDK 23 is included as an optional OpenJDK. An early access snapshot of OpenJDK 24  is also included. Support for OpenJDK LTS versions 17, 11 and 8 is being maintained.

OpenJDK 21 and OpenJDK 17 packages are now TCK (Technology Compatibility Kit) certified on amd64, arm64, s390x, ppc64el and armhf. The Java TCK is the most comprehensive test suite that covers all aspects of Java SE specification including language features, libraries and APIs. This guarantees interoperability and conformance to standard.
:::

:::{versionadded} 25.04
OpenJDK 21 is still the default. OpenJDK 24 is included as an optional OpenJDK. An early access snapshot of OpenJDK 25 is also included. Support for OpenJDK LTS versions 17, 11 and 8 is being maintained. OpenJDK with CRaC versions 17 and 21 also continue to be supported.

We are excited to announce the [devpack-for-spring](https://snapcraft.io/devpack-for-spring) snap and a set of Spring® [content snaps](https://snapcraft.io/devpack-for-spring-manifest) that will serve as development tools for Spring® projects. Developers can now quickly build Ubuntu ROCK images for their Java applications using the [Gradle and Maven plugins for Rockcraft](https://github.com/rockcrafters/java-rockcraft-plugins).

Additionally, GraalVM Community Edition for JDK versions 21, 24 and 25ea is now available as a [snap](https://snapcraft.io/graalvm-jdk). Java developers now have a choice to build and deploy their applications with standard OpenJDK, with OpenJDK-CRaC or as a GraalVM native image.
:::

:::{versionadded} 25.10
OpenJDK 21 is still the default. OpenJDK 25 (LTS) is now available. An early access snapshot of OpenJDK 26 is also included. Support for OpenJDK LTS versions 17, 11 and 8 is being maintained. OpenJDK with CRaC version 25 is also made available, while versions 17 and 21 continue to be supported. 

The [devpack-for-spring snap](https://snapcraft.io/devpack-for-spring) now supports development environment setup, by automating the installation and configuration of development tools (OpenJDK, container runtime, IDEs etc.) selected by the user. The [Maven and Gradle plugins for Rockcraft](https://github.com/rockcrafters/java-rockcraft-plugins) have been extended to support native images compiled by GraalVM. 

GraalVM Community Edition v25 is available through the graalvm-jdk [snap](https://snapcraft.io/graalvm-jdk), while GraalVM CE v21 continues to be supported. The snap is now available on arm64 too. 
:::

#### .NET

.NET 10 🦄 is now available.

:::{versionadded} 24.10
With the release of .NET 9, Ubuntu reinforces its commitment to supporting the .NET community. .NET 9 is fully supported on Ubuntu 24.10 and is also available for Ubuntu 24.04 LTS (Noble Numbat) and Ubuntu 22.04 LTS (Jammy Jellyfish) through the [.NET Backports PPA](https://launchpad.net/~dotnet/+archive/ubuntu/backports).

In addition, we have expanded .NET support to the IBM Power platform for both .NET 8 and .NET 9, further broadening the platform’s reach.

We are also excited to introduce the new and improved [.NET Snap](https://snapcraft.io/dotnet), allowing developers to seamlessly install any supported version of .NET on any Ubuntu system.
:::

:::{versionadded} 25.10
.NET versions 8 and 9 continue to be supported.

The .NET 10 RC1 SDK and runtimes are now included. Following its general availability in November, the final release will be provided as a subsequent package update.

Alternatively, .NET 10 is available on the `latest/beta` channel of the official .NET snap. It will be promoted to the `latest/stable` channel upon final release in November.

Support for the PowerShell snap has been expanded to include the `arm64`, `s390x`, and `ppc64el` architectures, broadening its availability across platforms.
:::

### Cloud

### Security

### Hardware support

:::{versionadded} 25.10
The `linux-generic` kernel for ARM64 provides broader compatibility for ARM64 desktop platforms that utilize UEFI for booting ([LP#2121352](https://bugs.launchpad.net/ubuntu/+source/linux-signed/+bug/2121352)).
:::

:::{versionchanged} 25.10
The Ubuntu RISC-V kernel (`linux-riscv`) only supports hardware that implements the RVA23S64 ISA profile. You can't run Ubuntu 26.04 LTS on systems that don't satisfy this requirement. The RISC-V kernel in Ubuntu 24.04 LTS continues to support boards with RVA20 processor cores.
:::

### Common changes

#### Linux kernel 🐧

The Linux kernel has been updated from version 6.8 to 7.0.

:::{versionadded} 24.10
Crash dumps are now [enabled by default](https://documentation.ubuntu.com/server/how-to/software/kernel-crash-dump/#kdump-enabled-by-default) for desktop and server installations.
:::

:::{versionadded} 25.04
Kernel developers can now make use of a [new scheduling system](https://canonical.com/blog/crafting-new-linux-schedulers-with-sched-ext-rust-and-ubuntu), "sched_ext", which provides a mechanism to implement scheduling policies as eBPF programs. This enables developers to defer scheduling decisions to standard user-space programs and implement fully functional hot-swappable Linux schedulers, using any language, tool, library, or resource accessible in user-space.
:::

:::{versionadded} 25.04
After the generic kernel gained the ability to [tune responsiveness at boot time](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2051342), the `linux-lowlatency` binary package has been retired in favor of a combination of `linux-generic` and a new user-space `lowlatency-kernel` package, responsible of tuning the GRUB command line.
:::

#### `systemd`

The `systemd` service manager has been updated from version X to Y.

:::{versionchanged} 24.10
Support for System V service scripts is deprecated and will be
removed in a future release. Please make sure to update your software
*now* to include a native `systemd` unit file instead of a legacy
System V script to retain compatibility with future `systemd` releases.

The complete removal of support for cgroup v1 ('legacy' and 'hybrid'
hierarchies) is scheduled for v258.
:::

Note: Resolute comes with 259.

:::{versionchanged} 24.10
Ubuntu now ships upstream `systemd`'s `tmp.mount` by default. In effect this means that `/tmp` is now a `tmpfs` by default.
:::

#### Netplan

The Netplan network manager has been updated from version X to Y

:::{versionadded} 24.10
The new [version 1.1 of Netplan](https://github.com/canonical/netplan/releases/tag/1.1) introduces a custom `systemd-networkd-wait-online` logic, waiting for link-local addresses and one routable interface, as described in the https://discourse.ubuntu.com/t/spec-definition-of-an-online-system/27838. Besides improvements to the `embedded-switch-mode` setting for SR-IOV devices, the introduction of parser flag to skip broken configurations and fixes for ProtonVPN and Microsoft Azure Linux.
:::

:::{versionadded} 25.04
Adding support for **wpa-psk-sha256** WiFis and allowing to configure **routing-policy** on the NetworkManager backend (LP: [#2086544](https://launchpad.net/bugs/2086544)). Additionally, the version shipped in Ubuntu enables [new functionality](https://github.com/systemd/systemd/pull/34640) in **systemd-networkd-wait-online** to wait for DNS servers to be configured and reachable, before [considering an interface to be online](https://discourse.ubuntu.com/t/spec-definition-of-an-online-system/27838).
:::

:::{versionadded} 25.10
Adds support non-standard OVS setups, e.g. inside snap environments.
:::

#### AppArmor

::::{versionadded} 25.04
As part of a profile writing effort to improve overall system security, the AppArmor package now includes many new profiles for applications. This improved sandboxing can help mitigate the impact of any exploit in the confined applications.

:::{dropdown} Report bugs
These profiles may cause breakage for unanticipated uses of those applications, and we encourage users to file a bug on [Launchpad](https://bugs.launchpad.net/ubuntu/+source/apparmor/+filebug) for AppArmor-induced breakage in common use cases. When AppArmor denies an action, it usually generates a log entry describing the denial, which will help us investigate the bug, but which can also be used to add additional rules for customization or to work around the denials. AppArmor log entries can be read in the auditd logs, if auditd is installed, or in the syslog otherwise. [This page](https://gitlab.com/apparmor/apparmor/-/wikis/denial_quick_guide) describes how the information contained in the denial log can be used to update a local override.
:::
::::

#### `sudo-rs`

:::{versionadded} 25.10
The `sudo-rs` tool is now the default `sudo` provider.

The `sudo` tool (the original `sudo` maintained by Todd C. Miller) has been renamed to `sudo.ws`. Additionally, the `sudo-ldap` package has been removed: please switch to using LDAP authentication via PAM.

See [Ubuntu Server Docs](https://documentation.ubuntu.com/server/how-to/security/user-management/#sudo-rs) for configuring your default `sudo` provider and for the differences between `sudo-rs` and `sudo.ws`.
:::

#### `rust-coreutils`

:::{versionadded} 25.10
The core utilities of the operating system are now provided by the [`rust-coreutils`](https://launchpad.net/ubuntu/+source/rust-coreutils) package. Among other things, this brings significant performance improvements, such as in the `base64` tool.

Since `rust-coreutils` are not necessarily fully compatible yet, we continue to provide the classic GNU utilities as well. You can switch back and forth between them.
:::
