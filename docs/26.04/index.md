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

:::{rubric} Performance improvements for Windows games
:::
:::{versionadded} 25.04
:::

A new NTSYNC driver that emulates WinNT sync primitives is available, delivering better performance potential for Windows games running on Wine and Proton (Steam Play).


### Server

### Development

* GCC 🐄 has been updated from version 14 to 15.2, `binutils` from 2.42 to 2.45, and `glibc` from 2.39 to 2.42.
* Python 🐍 has been updated from version 3.12 to 3.13.9, while 3.14 is also available.
* LLVM 🐉 has been updated from version 18 to 21.
* Rust 🦀 toolchain has been updated from version 1.75 to 1.88.
* Golang 🐀 has been updated from version 1.22 to 1.25.
* Zig ⚡ is now available in Ubuntu. It defaults to version 0.14.1.
* Ubuntu Toolchains has a new [homepage](https://ubuntu.com/toolchains).

:::{rubric} OpenJDK 21 and TCK certification
:::
:::{versionadded} 24.10
:::

OpenJDK defaults to 21 (LTS), while version 25 (LTS) and an early access snapshot of version 26 are now available.

OpenJDK 21 and OpenJDK 17 packages are now TCK (Technology Compatibility Kit) certified on AMD64, ARM64, s390x, ppc64el and armhf. The Java TCK is the most comprehensive test suite that covers all aspects of Java SE specification including language features, libraries and APIs. This guarantees interoperability and conformance to standard.

:::{rubric} Spring® snaps
:::
:::{versionadded} 25.04
:::

We are excited to announce the [devpack-for-spring](https://snapcraft.io/devpack-for-spring) snap and a set of Spring® [content snaps](https://snapcraft.io/devpack-for-spring-manifest) that will serve as development tools for Spring® projects.

Developers can now quickly build Ubuntu ROCK images for their Java applications using the [Gradle and Maven plugins for Rockcraft](https://github.com/rockcrafters/java-rockcraft-plugins).

:::{rubric} GraalVM snap
:::
:::{versionadded} 25.04
:::

GraalVM Community Edition for JDK versions 21, 24 and 25 is now available as a [snap](https://snapcraft.io/graalvm-jdk). Java developers now have a choice to build and deploy their applications with standard OpenJDK, with OpenJDK-CRaC or as a GraalVM native image.


:::{rubric} .NET 10
:::

.NET has been updated from version 8 to 10.

We have also expanded .NET support to the IBM Power platform, further broadening the platform’s reach.

:::{rubric} .NET snap
:::
:::{versionadded} 24.10
:::

We are excited to introduce the new and improved [.NET Snap](https://snapcraft.io/dotnet), allowing developers to seamlessly install any supported version of .NET on any Ubuntu system.

:::{rubric} PowerShell snap on more architectures
:::
:::{versionadded} 25.10
:::

Support for the PowerShell snap has been expanded to include the `arm64`, `s390x`, and `ppc64el` architectures, broadening its availability across platforms.


### Cloud

### Security

:::{rubric} New AppArmor sandboxing profiles
:::
:::{versionadded} 25.04
:::

As part of a profile writing effort to improve overall system security, the AppArmor package now includes many new profiles for applications. This improved sandboxing can help mitigate the impact of any exploit in the confined applications.

:::{dropdown} Report bugs
These profiles may cause breakage for unanticipated uses of those applications, and we encourage users to file a bug on [Launchpad](https://bugs.launchpad.net/ubuntu/+source/apparmor/+filebug) for AppArmor-induced breakage in common use cases. When AppArmor denies an action, it usually generates a log entry describing the denial, which will help us investigate the bug, but which can also be used to add additional rules for customization or to work around the denials. AppArmor log entries can be read in the auditd logs, if auditd is installed, or in the syslog otherwise. [This page](https://gitlab.com/apparmor/apparmor/-/wikis/denial_quick_guide) describes how the information contained in the denial log can be used to update a local override.
:::


### Hardware support

:::{rubric} ARM desktop platforms
:::
:::{versionadded} 25.10
:::

The `linux-generic` kernel for ARM64 provides broader compatibility for ARM64 desktop platforms that utilize UEFI for booting ([LP#2121352](https://bugs.launchpad.net/ubuntu/+source/linux-signed/+bug/2121352)).


:::{rubric} New RISC requirements
:::
:::{versionchanged} 25.10
:::

The Ubuntu RISC-V kernel (`linux-riscv`) only supports hardware that implements the RVA23S64 ISA profile. You can't run Ubuntu 26.04 LTS on systems that don't satisfy this requirement. The RISC-V kernel in Ubuntu 24.04 LTS continues to support boards with RVA20 processor cores.


### Common changes

:::{rubric} `sudo-rs`
:::
:::{versionadded} 25.10
:::

The `sudo-rs` tool is now the default `sudo` provider.

The `sudo` tool (the original `sudo` maintained by Todd C. Miller) has been renamed to `sudo.ws`. Additionally, the `sudo-ldap` package has been removed: please switch to using LDAP authentication via PAM.
    
See [Ubuntu Server Docs](https://documentation.ubuntu.com/server/how-to/security/user-management/#sudo-rs) for configuring your default `sudo` provider and for the differences between `sudo-rs` and `sudo.ws`.
    

:::{rubric} `rust-coreutils`
:::
:::{versionadded} 25.10
:::

The core utilities of the operating system are now provided by the [`rust-coreutils`](https://launchpad.net/ubuntu/+source/rust-coreutils) package. Among other things, this brings significant performance improvements, such as in the `base64` tool.

Since `rust-coreutils` are not necessarily fully compatible yet, we continue to provide the classic GNU utilities as well. You can switch back and forth between them.
    

:::{rubric} Linux kernel 7.0
:::

The Linux kernel has been updated from version 6.8 to 7.0.

* Crash dumps are now [enabled by default](https://documentation.ubuntu.com/server/how-to/software/kernel-crash-dump/#kdump-enabled-by-default) for desktop and server installations.

    :::{versionadded} 24.10
    :::

* Kernel developers can now make use of a [new scheduling system](https://canonical.com/blog/crafting-new-linux-schedulers-with-sched-ext-rust-and-ubuntu), `sched_ext`, which provides a mechanism to implement scheduling policies as eBPF programs. This enables developers to defer scheduling decisions to standard user-space programs and implement fully functional hot-swappable Linux schedulers, using any language, tool, library, or resource accessible in user-space.

    :::{versionadded} 25.04
    :::

* After the generic kernel gained the ability to [tune responsiveness at boot time](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2051342), the `linux-lowlatency` binary package has been retired in favor of a combination of `linux-generic` and a new user-space `lowlatency-kernel` package, responsible of tuning the GRUB command line.

    :::{versionadded} 25.04
    :::

:::{rubric} `systemd` 259
:::

The `systemd` service manager has been updated from version 255 to 259.

* Support for System V service scripts has been removed. Use native `systemd` unit files instead of legacy System V scripts.

    :::{versionremoved} 26.04
    :::

* Support for `cgroup` version 1 ('legacy' and 'hybrid' hierarchies) has been removed.

    :::{versionremoved} 26.04
    :::

* Ubuntu now comes with the upstream `tmp.mount` unit by default. As a result, the `/tmp` directory is now a `tmpfs` file system by default.

    :::{versionchanged} 24.10
    :::

:::{rubric} Netplan 1.2
:::

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
