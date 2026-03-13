---
tocdepth: 3
---

(ubuntu-25.04-release-notes)=
# Ubuntu 25.04 release notes

These release notes for **Ubuntu 25.04** (Plucky Puffin) provide an overview of the release and document the known issues with Ubuntu and its flavors.

:::{toctree}
:maxdepth: 1
:hidden:

Release schedule <schedule>
:::

## Dedication

Subscribers to the `ubuntu-{devel-}announce` mailing list and long term participants in the Ubuntu community will have come across Steve Langasek's work. Steve, known in the community as vorlon, was a long-term member of the Release team (along with being a member of Archive Admin, Techboard, SRU team, and so on) and a colleague to many of us at Canonical. As a member of the Release team, Steve was responsible for devising many of the processes, policies, and tools which we use today, and teaching his fellow members the ropes. [Steve passed away on 1st January 2025](https://discourse.ubuntu.com/t/remembering-and-thanking-steve-langasek/52665) after being unwell for quite some time. The Ubuntu Release Team dedicates 25.04 “Plucky Puffin” to our colleague and friend, Steve Langasek. He is missed and will live in our hearts forever. Thank you for everything, Steve.

## Upgrades

We've identified two issues in the `ubuntu-release-upgrader` affecting upgrades to Ubuntu 25.04 "Plucky Puffin":

* [Handling of Qt dependencies](https://bugs.launchpad.net/ubuntu/+source/ubuntu-release-upgrader/+bug/2095535)
* [Removal of foreign packages from disabled sources](https://bugs.launchpad.net/ubuntu/+source/ubuntu-release-upgrader/+bug/2107657)

As a result, upgrades to Ubuntu 25.04 have been temporarily suspended while these issues are being addressed.

The necessary updates are already in the pipeline, and we expect to re-enable upgrades very soon.
Thank you for your patience.

## Support lifespan

Ubuntu 25.04 will be supported for 9 months until January 2026. If you need long term support, we recommend you use [Ubuntu 24.04.2 LTS](https://ubuntu.com/download) which is supported until at least 2029.

## Upgrades

* Upgrades to to Ubuntu 25.04 will refresh seeded snaps to the appropriate snap channels, regardless of what was being tracked before. Snaps that are newly-seeded will be installed during the upgrade. In particular, the following snaps will be installed or refreshed on upgrade: 

  Early upgrades may wish to perform these updates manually.

(25-04-new-features-in-25-04)=
## New features in 25.04

### Updated Packages

### Linux kernel 6.14🐧

This release delivers the latest Linux kernel, following Canonical’s new policy. Kernel developers can now make use of a [new scheduling system](https://canonical.com/blog/crafting-new-linux-schedulers-with-sched-ext-rust-and-ubuntu), "sched_ext", which provides a mechanism to implement scheduling policies as eBPF programs. This enables developers to defer scheduling decisions to standard user-space programs and implement fully functional hot-swappable Linux schedulers, using any language, tool, library, or resource accessible in user-space.

A new NTSYNC driver that emulates WinNT sync primitives is also available, delivering better performance potential for Windows games running on Wine and Proton (Steam Play).

The "bpftools" and linux-perf tools have been decoupled from the kernel version, making dependency management easier for developers working with containers. These tools are now shipped in their own packages.

Other features can be found in the [Linux 6.14 upstream](https://kernelnewbies.org/Linux_6.14) changelog.

After the generic kernel grew the ability to [tune responsiveness at boot time](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2051342), the linux-lowlatency binary package has been retired in favour of a combination of linux-generic and a new userspace `lowlatency-kernel` package, responsible of tuning the grub cmdline.

### systemd v257.4

The init system was updated to systemd v257.4. See the [upstream changelog ](https://github.com/systemd/systemd/releases/tag/v257) for more information about individual features. To highlight a few things:

* In Ubuntu, systemd is no longer built with utmp support. Among other things, this means that systemd's default `/usr/lib/tmpfiles.d/systemd.conf` no longer creates `/run/utmp`.
There is currently this known bug ([LP: #2103489](https://launchpad.net/bugs/2103489)) in Ubuntu 25.04, that prevents 'who' from properly working and requires a coreutils rebuild.

* The complete removal of support for cgroup v1 ('legacy' and 'hybrid'
hierarchies) is scheduled for v258.

* Support for System V service scripts is deprecated and will be
removed in v258. Please make sure to update your software
*now* to include a native systemd unit file instead of a legacy
System V script to retain compatibility with future systemd releases.

### Netplan v1.1.2 🌐
Adding support for **wpa-psk-sha256** WiFis and allowing to configure **routing-policy** on the NetworkManager backend (LP: [#2086544](https://launchpad.net/bugs/2086544)). Additionally, the version shipped in Ubuntu enables [new functionality](https://github.com/systemd/systemd/pull/34640) in **systemd-networkd-wait-online** to wait for DNS servers to be configured and reachable, before [considering an interface to be online](https://discourse.ubuntu.com/t/spec-definition-of-an-online-system/27838).

### Toolchain Upgrades 🛠️

* GCC 🐄 a snapshot of the upcoming GCC 15, binutils updated to 2.44, and glibc to 2.41.
* Python 🐍 is updated to 3.13.3
* LLVM 🐉 now defaults to version 20
* Rust 🦀 toolchain defaults to version 1.84
* Golang 🐀 is updated to 1.24
* OpenJDK ☕ versions 24 GA and 25 early access snapshot are now available

#### OpenJDK

OpenJDK 21 is still the default. OpenJDK 24 is included as an optional OpenJDK. An early access snapshot of OpenJDK 25 is also included. Support for OpenJDK LTS versions 17, 11 and 8 is being maintained. OpenJDK with CRaC versions 17 and 21 also continue to be supported.

We are excited to announce the [devpack-for-spring](https://snapcraft.io/devpack-for-spring) snap and a set of Spring® [content snaps](https://snapcraft.io/devpack-for-spring-manifest) that will serve as development tools for Spring® projects. Developers can now quickly build Ubuntu ROCK images for their Java applications using the [Gradle and Maven plugins for Rockcraft](https://github.com/rockcrafters/java-rockcraft-plugins).

Additionally, GraalVM Community Edition for JDK versions 21, 24 and 25ea is now available as a [snap](https://snapcraft.io/graalvm-jdk). Java developers now have a choice to build and deploy their applications with standard OpenJDK, with OpenJDK-CRaC or as a GraalVM native image.

#### .NET

.NET versions 8 and 9 continue to be supported. 

The [dotnet](https://snapcraft.io/dotnet) snap is updated to include .NET version 9. The [powershell-preview](https://snapcraft.io/powershell-preview) snap has been updated to build from source.

### Default configuration changes ⚙️

### AppArmor profiles

#### AppArmor profile writing effort

As part of a profile writing effort to improve overall system security, the AppArmor package now includes many new profiles for applications. This improved sandboxing can help mitigate the impact of any exploit in the confined applications. However, these profiles may cause breakage for unanticipated uses of those applications, and we encourage users to file a bug on [Launchpad](https://bugs.launchpad.net/ubuntu/+source/apparmor/+filebug) for AppArmor-induced breakage in common use cases. When AppArmor denies an action, it usually generates a log entry describing the denial, which will help us investigate the bug, but which can also be used to add additional rules for customization or to work around the denials. AppArmor log entries can be read in the auditd logs, if auditd is installed, or in the syslog otherwise. [This page](https://gitlab.com/apparmor/apparmor/-/wikis/denial_quick_guide) describes how the information contained in the denial log can be used to update a local override.

#### AppArmor profile for bwrap

AppArmor now comes with a bwrap profile (bwrap-userns-restrict) that allows it to create user namespaces and set up sandboxing, before transitioning to a tighter profile that denies capabilities for the processes running inside the bwrap sandbox. The addition of this profile should unblock more use cases for bwrap while allowing a reduction in the kernel attack surface opened up by unprivileged user namespaces. However, this profile still restricts unprivileged userns creation and capability usage even when bwrap (and its sandboxed application) are run as a privileged user, so such use cases may not be fully supported yet.

#### AppArmor profile removals

As part of [hardening improvements around AppArmor user namespace mediation](https://discourse.ubuntu.com/t/understanding-apparmor-user-namespace-restriction/58007), profiles for busybox and nautilus that directly allowed them access to user namespaces have been removed. As a result, the busybox unshare function can no longer be used to create unprivileged user namespaces. Nautilus' use of user namespaces should still work due to the new bwrap-users-restrict profile, but regressions are possible if there are bugs in the bwrap profile.

### tzdata

Previously, the tzdata package in Ubuntu used the `/etc/timezone` file to configure the system's timezone. This method is not supported by systemd and certain desktop environments, which instead only change the `/etc/localtime` symlink to point to a file in `/usr/share/zoneinfo`.

For this reason, starting with version 2024b-5, the tzdata package no longer automatically creates the `/etc/timezone` file, but still updates it if it exists. In the next Ubuntu 25.10 release, the `/etc/timezone` file will be automatically removed and support for it in the maintainer scripts will be completely dropped.

### Ubuntu Desktop

#### New ARM64 Desktop Image
* There is now also an official generic arm64 desktop ISO targeting VMs, ACPI + EFI platforms and Snapdragon based WoA devices.
* Initial hardware enablement work for the Snapdragon X Elite platform is included in the desktop ISO

#### Installer and Upgrades

* Added the option to replace an existing Ubuntu installation
* Improved dual boot UX (with a focus on BitLocker protected Windows systems):
  * Added the option to install Ubuntu alongside existing BitLocker partitions if enough unallocated  space (or a sufficiently large and resizable partition) is available
  * Made encrypted installations and other 'advanced options' available for dual boot scenarios

#### Enterprise

- [authd](https://github.com/ubuntu/authd): Ubuntu's cloud authentication solution:
  - Many fixes and improvements to the EntraID provider
  - New Google provider
  - New [authd documentation](https://documentation.ubuntu.com/authd/en/stable/)

- New [ADSys Release](https://github.com/ubuntu/adsys): the Active Directory Group Policy client for Ubuntu, supports the latest Polkit and comes with improvements and bug fixes to certificates enrolment.

#### GNOME 👣

- GNOME has been updated to include new features and fixes from the latest GNOME release, [GNOME 48](https://release.gnome.org/48/)
- GNOME 48 now includes the [triple buffering](https://discourse.ubuntu.com/t/triple-buffering-a-debrief/56314) feature from Ubuntu

#### Default app changes

- The **Document Viewer** app for viewing PDFs is now provided by Papers instead of Evince. Papers started with the Evince codebase but it has been updated to use GTK4 and partially rewritten in Rust.
- **`xdg-terminal-exec`** is installed by default making it easier to switch a user's default terminal for the Ctrl+Alt+T keyboard shortcut and for opening terminal apps ([LP: #2107326](https://launchpad.net/bugs/2107326))
- **Geolocation** services are now backed by [BeaconDB](https://beacondb.net/) after Mozilla Location Services was retired last year
- The **JPEG XL** format is now supported without needing to install any additional packages

#### Updated Applications

* [Firefox](https://mozilla.org/firefox/releases/) 137 🔥🦊
* [LibreOffice 25.2](https://wiki.documentfoundation.org/ReleaseNotes/25.2) 📚
* [Thunderbird 128 "Supernova"](https://blog.thunderbird.net/2023/07/our-fastest-most-beautiful-release-ever-thunderbird-XY-supernova-is-here/) 🌩️🐦
* [GNU Image Manipulation Program 3.0](https://www.gimp.org/news/2025/03/16/gimp-3-0-released/) 🖼️ is available for install
* The `fish` shell has always been known for its smart and user-friendly interface, making command-line interactions more intuitive and efficient. With the release of version 4, `fish` has undergone a significant transformation, rewritten entirely in Rust.

    This change brings a on one side the values of the ecosystem like enhanced performance and improved stability, while on the other side is not compromising on the feature set. The upstream community had a great [blog about the rust port](https://fishshell.com/blog/rustport/), which we recommend reading if you are curious.

    As shells go, this is about your taste and preferences: if you have not been trying [fish](https://fishshell.com/) before, consider to try it out now and experience its features for yourself.

#### Updated Subsystems

* [BlueZ 5.79](https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/ChangeLog?id=5.79) 💙
* [Cairo 1.18.4](https://cairographics.org/news/cairo-1.18.4/) 🐫
* [NetworkManager 1.52](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/blob/nm-1-52/NEWS) 🖧
* [Pipewire 1.2.7](https://gitlab.freedesktop.org/pipewire/pipewire/-/blob/1.2.7/NEWS) 🔊
* [Poppler 25.03](https://gitlab.freedesktop.org/poppler/poppler/-/blob/poppler-25.03.0/NEWS) 📝
* [xdg-desktop-portal 1.20](https://github.com/flatpak/xdg-desktop-portal/blob/1.20.0/NEWS.md) ⛩️
* [Nvidia 570](https://www.nvidia.com/en-us/drivers/details/242273/) 👁️
* The `libva` library is now available in the *Main* repository component. The library implements VA-API (Video Acceleration API) for hardware video decoding and encoding. Applications can now use VA-API out of box. Notably, you can record your screen at the original screen rate. Without VA-API, your screen recording has a reduced frame rate because it's limited by the CPU. To use VA-API, enable third-party drivers during Ubuntu installation. You can also install the library after installation:

    ```bash
    sudo apt install va-driver-all
    ```

#### Gaming
##### NVIDIA Dynamic Boost
This release enabled NVIDIA Dynamic Boost by default on supported laptops with NVIDIA GPUs.

NVIDIA Dynamic Boost is a feature of the NVIDIA drivers that dynamically shifts power between CPU and GPU depending on the workload on the system. While gaming, this allows extracting more performance by granting more power to the GPU.

Dynamic Boost will be active only when the laptop is powered by AC and there is enough load on the GPU. It will not be engaged when the system is running on battery.

For more details refer to [NVIDIA's documentation](https://download.nvidia.com/XFree86/Linux-x86_64/570.133.07/README/dynamicboost.html).

#### Support for new Intel® integrated and discrete GPUS 
This release brings full support for Intel® Core™ Ultra Xe2 integrated Intel® Arc™ graphics, and Intel® Arc™ B580 and B570 “Battlemage” discrete GPUs. 
Moreover, the following features are also included:
 * Improved GPU and CPU ray tracing rendering performance in applications with Intel Embree support, such as Blender (v4.2+). Ray tracing hardware acceleration on the GPU improves frame rendering by 20-30%, due to a 2-4x speed-up for the ray tracing component. 
 * Full hardware accelerated video encoding of AVC, JPEG, HEVC, and AV1 on “Battlemage” devices.
 * Introduction of the new CCS optimization in Intel® Compute Runtime.
 * Enable debugging support for Intel Xe GPUs. 
 * oneAPI Level Zero Ray Tracing improves AI/ML workload speeds via Embree on SYCL

### Ubuntu Foundations

#### Cryptography

##### Libraries
OpenSSL has been updated to [3.4.1](https://github.com/openssl/openssl/blob/openssl-3.4.0/NEWS.md) and GnuTLS has been updated to [3.8.9](https://gitlab.com/gnutls/gnutls/-/blob/master/NEWS). In addition, patches from their git stable branches have been added in order to include as many fixes as possible starting with release day.


#### Package Management: APT 3.0

APT has been updated to 3.0. 

The new dependency solver is now automatically used if the classic solver cannot find a solution to either find a solution or add more context to the failure, and in other cases to [evaluate its performance](https://discourse.ubuntu.com/t/evaluating-the-new-apt-solver-in-25-04/55618).

APT has switched from GnuTLS and gcrypt to the OpenSSL library for TLS connections and file hashing, which should improve compatibility and reduces the footprint of minimal installations.

An automatic pager has been added to `apt(8)` for commands such as show and list, similar to `git log` and `journalctl`.

The `apt-key` command has been removed. Signature verification now makes direct use of `gpgv`. Some packages and system administration scripts may need adjustment for managing keys directly, advice can be found in the `apt-secure(8)` manual page.

### Ubuntu Server

#### Apache2

* mod_md: update to version 2.4.31
  * Improved behavior waiting for ACME server to verify domains.
  * Fix certificate retrieval on ACME renewal to not require a 'Location:' header returned by the ACME CA. This was the way it was done in ACME before it became an IETF standard. Let's Encrypt still supports this, but other CAs do not.
  * When the server starts, it looks for new, staged certificates to activate. If the staged set of files in `md/staging/<domain>` is messed up, this could prevent further renewals to happen. Now, when the staging set is present, but could not be activated due to an error, purge the whole directory.
  * Restore compatibility with OpenSSL < 1.1.
* Add the ldap-search option to mod_authnz_ldap, allowing authorization to be based on arbitrary expressions that do not include the username.
* mod_ssl: Restore support for loading PKCS#11 keys via ENGINE without "SSLCryptoDevice" configured.
* http: Remove support for Request-Range header sent by Navigator 2-3 and MSIE 3.
* mod_rewrite: Don't require [UNC] flag to preserve a leading // added by applying the perdir prefix to the substitution.
* mod_proxy: Avoid AH01059 parsing error for SetHandler "unix:" URLs in `<Location>` (incomplete fix in 2.4.62).
* mod_tls: removed the experimental module. It now is available standalone from https://github.com/icing/mod_tls. The rustls provided API is not stable and does not align with the httpd release cycle.
* mod_rewrite: Better question mark tracking to avoid UnsafeAllow3F.
* mod_http2: Return connection monitoring to the event MPM when blocking on client updates.

#### Clamav

ClamAV was updated from 1.3 in Ubuntu 24.10, to version 1.4.2 in 25.04.
This brings a number of fixes, along with the following noteworthy
changes from the Clamav 1.4.0 feature release:

* Added support for extracting ALZ archives. The new ClamAV file type for ALZ archives is CL_TYPE_ALZ. Added a DCONF (Dynamic CONFiguration) option to enable or disable ALZ archive support, via ClamAV .cfg "signatures".
* Added support for extracting LHA/LZH archives. The new ClamAV file type for LHA/LZH archives is CL_TYPE_LHA_LZH. Added a DCONF option to enable or disable LHA/LZH archive support.
* Added the ability to disable image fuzzy hashing, if needed. For context, image fuzzy hashing is a detection mechanism useful for identifying malware by matching images included with the malware or phishing email/document.
* Added a DCONF option to enable or disable image fuzzy hashing support.
* Fixed an unaligned pointer dereference issue on select architectures.

For complete details of all changes leading up to 1.4.2, please see the upstream release notes at:  https://blog.clamav.net/


#### Chrony

Starting with version [4.5-3ubuntu4]( https://launchpad.net/ubuntu/+source/chrony/4.5-3ubuntu4), chrony will ship with a default configuration set to use Ubuntu NTS servers by default.

The two main changes are:

1. NTS/KE uses a separate port (4460/tcp) to negotiate security parameters, which are then used via the normal NTP port (123/udp). This is a new deployment, running on different IP addresses than the service without NTS.

2. A new CA is installed in `/etc/chrony/nts-bootstrap-ubuntu.crt` that is used specifically for the Ubuntu NTS bootstrap server, needed for when the clock is too far off. This is added to certificate set ID "1", and defined via `/etc/chrony/conf.d/ubuntu-nts.conf`. There is also a staging CA shipped with the package, but it's not referred to anywhere and is just there as a convenience for testing the staging servers.

If your network does not allow access to the Ubuntu NTS servers and the required ports, and the new configuration is in place, chrony will not be able to adjust this system's clock. To revert to NTP, just edit the configuration file in `/etc/chrony/sources.d/ubuntu-ntp-pools.sources` and revert to using the listed NTP servers in favor of the NTS ones. Or revert to your previous copy of that configuration file.

For other changes introduced in version 4.6.1, please refer to the [upstream release notes](https://chrony-project.org/news.html#_8_oct_2024_chrony_4_6_1_released).

#### cloud-init v. 25.1.1

Notable features beyond v. 24.3 present in Oracular:
* oracle: [add true single stack ipv6 support](https://github.com/canonical/cloud-init/pull/5785)
* networkd: [Support RequiredForOnline option](https://github.com/canonical/cloud-init/pull/5852)
* smartos: [Add addrconf IPv6 support](https://github.com/canonical/cloud-init/pull/5831)
* networkd: Conditionally remove networkd online dependency on Ubuntu (#5772)-
* security: [Ensure random passwords contain multiple character types](https://github.com/canonical/cloud-init/pull/5815)
* Enable new datasource for CloudCIX platform
* vmware:
  * Move DS VMware to be in front of DS OVF ([#5912](https://github.com/canonical/cloud-init/pull/5912))
  * Convert imc network config to v2 ([#5937](https://github.com/canonical/cloud-init/pull/5937))
* Identify Samsung Cloud Platform as OpenStack ([#5924](https://github.com/canonical/cloud-init/pull/5924))
* aliyun: support crawl metadata at once ([#5942](https://github.com/canonical/cloud-init/pull/5942)) [jinkangkang]

For the full list of changes, please see the upstream [release notes](https://github.com/canonical/cloud-init/releases)

Breaking changes:
* To avoid installing unnecessary debian package dependencies on all images, cloud-init debian package now creates separate binaries:
  * `cloud-init-base`: installs all debian package `Depends:` common to all cloud platforms
  *  separate `cloud-init-<cloudname>` metapackage defining cloud-specific package dependencies for platforms such as CloudSigma, SmartOs.

Seeding the `cloud-init` metapackage in Plucky and later will continue to install all package dependencies previously provided by the `cloud-init` package on Noble and Oracular.



#### Containerd

The containerd (src:containerd-app) package was updated to version 2.0.2. Version 2 includes the stabilization of new features added in the last 1.x release as well as the removal of features which were deprecated in 1.x, meaning you should expect breaking changes here.

For further details on such changes, please refer to [the upstream release notes](https://github.com/containerd/containerd/blob/main/docs/containerd-2.0.md).

<!--
#### Dcmstack
 Only minor changes from Oracular to Plucky.  And we're in sync.
-->

#### runc

runc (src:runc-app) was updated to upstream version 1.2.5. This new version includes several fixes and changes including

* When using cgroups v2, allow to set or update memory limit to "unlimited" and swap limit to a specific value. 
* Mount options on bind-mounts that clear a mount flag are now always applied. Previously, if a user requested a bind-mount with only clearing options (such as `rw,exec,dev`) the options would be ignored and the original bind-mount options would be set.
* Container configurations using bind-mounts with superblock mount flags (i.e. filesystem-specific mount flags, referred to as "data" in `mount(2)`, as opposed to VFS generic mount flags like `MS_NODEV`) will now return an error.
* Fix CVE-2024-45310, a low-severity attack that allowed maliciously configured containers to create empty files and directories on the host.
* `runc features` is no longer experimental.
* `runc` option `--criu` is now ignored (with a warning), and the option will be removed entirely in a future release.
* `runc kill` option `-a` is now deprecated. Previously, it had to be specified to kill a container (with SIGKILL) which does not have its own private PID namespace (so that runc would send SIGKILL to all processes). Now, this is done automatically.
* runc now supports id-mapped mounts for bind-mounts (with no restrictions on the mapping used for each mount).
* runc will now use `cgroup.kill` if available to kill all processes in a container (such as when doing `runc kill`).

For a complete list of changes and more details on the ones above, refer to the [upstream changelog](https://github.com/opencontainers/runc/blob/main/CHANGELOG.md).

#### Docker

The docker.io (src:docker.io-app) package was updated to version 27.5.1. Some highlights of this version include:

* `docker image ls` now supports `--tree` flag that shows a multiplatform-aware image list.
* The `Aliases` field returned by `docker inspect` contains the container short ID once the container is started. This behavior was removed. Now, the `Aliases` field only contains the aliases set through the `docker container create` and `docker run` flag `--network-alias`. A new field `DNSNames` containing the container name (if one was specified), the hostname, the network aliases, as well as the container short ID, has been introduced in v25.0 and should be used instead of the `Aliases` field.
* Add `--platform` flag to `docker image push` and improve the default behavior when not all platforms of the multi-platform image are available locally.
* Several improvements to IPv6 network configuration.
* `ip6tables` is no longer experimental. You may remove the `experimental` configuration option and continue to use IPv6, if it is not required by any other features.
* `ip6tables` is now enabled for Linux bridge networks by default.

Watch out for deprecation or removal of features in this [upstream page](https://github.com/docker/cli/blob/v27.5.1/docs/deprecated.md)

**docker-buildx:** docker-buildx was updated to version 0.20.1. This version introduces new features such as

* New `--call` option allows setting evaluation method for a build, replacing the previous experimental `--print` flag.
* Build command now ensures that multi-node builds use the same build reference for each node.
* Several improvements for the `bake` command.
* New `buildx history` command has been added that allows working with build records of completed and running builds.

**docker-compose-v2:** docker-compose-v2 was updated to version 2.33.0. This version introduces several fixes and new features such as

* A new `--environment` flag to `config` command to output the resolved environment variables used for interpolation.
* A new `--prune` option to the docker-compose `watch` command to ensure that dangling images are pruned automatically when rebuilding.
* Support to bake was added.

<!-- #### Exim4
 Only minor changes from Oracular to Plucky
 -->


#### HAProxy
The HAProxy package was upgraded to version 3.0.7. This new version introduces performance improvements for Lua scripts and stick tables, support for virtual ACL and map files, limiting glitchy HTTP/2 connections, and persistent stats after a reload.
**Breaking changes** include detection of accidental multiple commands sent to the Runtime API, rejecting the `enabled` keyword for dynamic servers, stricter parsing of non-standard URIs and renaming of `tune.ssl.ocsp-update` to `tune.ocsp-update`. You can learn more about it at [https://www.haproxy.com/blog/announcing-haproxy-3-0](https://www.haproxy.com/blog/announcing-haproxy-3-0). A complete list of changes is avalilable at [https://www.haproxy.org/download/3.0/src/CHANGELOG](https://www.haproxy.org/download/3.0/src/CHANGELOG).

#### freeradius 

freeradius 3.2.7+dfsg-1ubuntu1 drops `radlast`. This is due to `radlast` calling `last`, which is no longer available in Ubuntu. These use `wtmp` 32 bit files, which are not 2038 compliant. Upstream source has dropped `radlast` and other tools in [an upstream commit](https://github.com/FreeRADIUS/freeradius-server/commit/b0f4123c84a0aeaa6fc393fd5e6fdaa0e0a86eaf). These were originally made optional, and later removed entirely. Information in [lp: 2096611](https://bugs.launchpad.net/ubuntu/+source/freeradius/+bug/2096611)

#### libvirt

The [libvirt ](https://libvirt.org) package was upgraded to version 10.10.0. Here are the changes since Ubuntu Oracular:

* network: make networks with `<forward mode='open'/>` more useful.
   It is now permissable to have a `<forward mode='open'>` network that has no IP address assigned to the host's port of the bridge. This is the only way to create a libvirt network where guests are unreachable from the host (and vice versa) and also 0 firewall rules are added on the host.

   It is now also possible for a `<forward mode='open'/>` network to use the `zone` attribute of `<bridge>` to set the firewalld zone of the bridge interface (normally it would not be set, as is done with other forward modes).

* qemu: zero block detection for non-shared-storage migration

    Users can now request that all-zero blocks are not transferred when migrating non-shared disk data without actually enabling zero detection on the disk itself. This allows sparsifying images during migration where the source has no access to the allocation state of blocks at the cost of CPU overhead.

    This feature is available via the `--migrate-disks-detect-zeroes` option for `virsh migrate` or `VIR_MIGRATE_PARAM_MIGRATE_DISKS_DETECT_ZEROES` migration parameter. See the documentation for caveats.

* qemu: internal snapshot improvements

   The qemu internal snapshot handling code was updated to use modern commands which avoid the problems the old ones had, preventing use of internal snapshots on VMs with UEFI NVRAM. Internal snapshots of VMs using UEFI are now possible provided that the NVRAM is in `qcow2` format.

* qemu: add multi boot device support on s390x

   For classical mainframe guests (i.e. LPAR or z/VM installations), you always have to explicitly specify the disk where you want to boot from (or "IPL" from, in s390x-speak -- IPL means "Initial Program Load").

   In the past QEMU only used the first device in the boot order to IPL from. With the new multi boot device support on s390x that is available with QEMU version 9.2 and newer, this limitation is lifted. If the IPL fails for the first device with the lowest boot index, the device with the second lowest boot index will be tried and so on until IPL is successful or there are no remaining boot devices to try.

   Limitation: The s390x BIOS will try to IPL up to 8 total devices, any number of which may be disks or network devices.

* qemu: Add support for versioned CPU models

  Updates to QEMU CPU models with `-vN` suffix can now be used in libvirt just like any other CPU model.

* qemu: Automatically add IOMMU when needed

   When domain of `qemu` or `kvm` type have more than 255 vCPUs, IOMMU with EIM mode is required. Starting with this release libvirt automatically adds one (or turns on the EIM mode if there's IOMMU without it).

* In 10.5 (thereby oracular) already support for `SEV-SNP` was introduced as another type of `<launchSecurity/>`. Its support is reported in both domain capabilities and virt-host-validate. Now also the qemu version in the release is ready to provide that.

* The Debian (and consequently the Ubuntu) libvirt package has been significantly redesigned. To quote its NEWS file:

   > All the various drivers and storage backends come in their own separate binary packages now, which makes it possible to install exactly as many or as few as desired.
   >
   > The system-wide configuration for the libvirtd daemon is no longer shipped separately from the daemon itself, as was the case until now. The `libvirt-daemon-system` package still exists, but it's now simply a convenient way to install the "typical" libvirt deployment consisting of all the components needed to run a QEMU-based hypervisor.

For more details, please see [the upstream changelog ](https://www.libvirt.org/news.html#v10-10-0-2024-12-02).

#### Monitoring Plugins

Monitoring-plugins is upgraded to the 2.4.0 release in Plucky Penguin. While primarily a bugfix release, this includes a few minor enhancements:

* Add new test function for percentage expressions
* check_ups: output ups.realpower if supported
* check_curl: add haproxy protocol option
* check_disk: increase alert precision
* check_ircd: IPv6 support
* check_nwstat: adds percentage used space
* check_swap: Possibility to run check_swap without thresholds
* check_ups: additional alarm conditions

For the full list of changes, please see the upstream [release notes](https://github.com/monitoring-plugins/monitoring-plugins/releases)


#### Nginx

The upgrade from Oracular's 1.26.0 to Plucky's 1.26.3 brings a handful of bug fixes, along with security fixes (already backported to the Oracular version).  There are no feature changes this release.

#### OpenLDAP

The 2.6.9 release is a bugfix-only release with improvements to libldap, slapd, and slapo subcomponents.  For the full list of changes please see the [release notes](https://www.openldap.org/software/release/changes.html).

#### Openssh

OpenSSH was updated to version 9.9. Here are some highlights since 9.7, last shipped in Ubuntu 24.10:

- new `PerSourcePenalties` option that will penalise client addresses that for some reason do not complete authentication. New in version 9.8.
- support for a new hybrid post-quantum key exchange algorithm, called "mlkem768x25519-sha256". Described in https://datatracker.ietf.org/doc/html/draft-kampanakis-curdle-ssh-pq-ke-03, it's available by default. New in version 9.8.
- new match option `invalid-user`, which can be used when the target username is not valid
- prevent private keys from being included in core dump files for most of their lifespans. New in version 9.8.
- and more
For a detailed list of the changes since 9.7, please consult the upstream release notes at https://www.openssh.com/releasenotes.html.

In terms of Ubuntu and Debian packaging, here are the most important changes:
- New `sshd.service` alias to `ssh.service`. Both names can now be used in `systemctl` commands.
- New binary packages called `openssh-client-gssapi` and `openssh-server-gssapi` . This is in preparation for a future split of the GSSAPI authentication mechanism into separate packages in the near future. For now, they just pull in their non-gssapi counterparts, if installed. See https://lists.debian.org/debian-devel/2024/04/msg00044.html for the detailed plan.
- Host DSA keys are no longer generated.

#### Valkey

Valkey was updated to version 8, starting with 8.0.2. This includes significant performance and reliability improvements, without any backwards-incompatible changes to commands and responses. For more information on the new version, see the [Valkey 8 blog post](https://valkey.io/blog/valkey-8-0-0-rc1/). Release notes are available on the [Valkey project GitHub](https://github.com/valkey-io/valkey/releases/tag/8.0.2).


#### MySQL

MySQL was updated from 8.0 to 8.4 LTS, starting with 8.4.4. This is MySQL's first official long term support release, including various internal improvements, new features, and some important configuration changes.

Upstream release notes are now available in the [Mysql 8.4 documentation library](https://dev.mysql.com/doc/relnotes/mysql/8.4/en/). For more information about the transition from MySQL 8.0 to 8.4, see the [MySQL 8.4 overview](https://dev.mysql.com/doc/refman/8.4/en/mysql-nutshell.html).

Due to upstream policy, support for 32-bit MySQL Server has been removed. However, Ubuntu will continue to provide a MySQL client and client library for 8.4.


#### MySQL Shell

MySQL Shell was updated from 8.0.38 to 8.4.4 to coencide with MySQL 8.4. It adds support for MySQL 8.4 servers, and provides additional improvements for interacting with MySQL 8.0 servers. For a list of features, see the [MySQL Shell 8.4 documentation](https://dev.mysql.com/doc/mysql-shell/8.4/en/). Release notes for MySQL Shell 8.4 can be found [here](https://dev.mysql.com/doc/relnotes/mysql-shell/8.4/en/).


#### Percona Xtrabackup

Percona-Xtrabackup was updated from the 8.0 track to 8.4 with 8.4.0-1, also to coencide with the release of MySQL 8.4. This version provides changes to match MySQL 8.4, along with support for the `keyring_vault` component. For more information see the [upstream release notes](https://docs.percona.com/percona-xtrabackup/8.4/release-notes/8.4.0-1.html).


#### PHP

PHP was updated to version 8.4. This is a major update of the languages including new features such as property hooks, asymmetric visibility, an updated DOM API, and more.

For more details see the [upstream release notes](https://www.php.net/releases/8.4/en.php).

#### PostgreSQL

PostgreSQL was updated to version 17, which contains several new features and enhancements, including

* A new memory management system for `VACUUM`, which reduces memory consumption and can improve overall vacuuming performance;
* New SQL/JSON capabilities, including constructors, identity functions, and the `JSON_TABLE()` function, which converts JSON data into a table representation;
* Various query performance improvements and Logical replication enhancements; and
* A new client-side connection option, `sslnegotiation=direct`], that performs a direct TLS handshake to avoid a round-trip negotiation.

For more details, see the [upstream release notes](https://www.postgresql.org/docs/17/release-17.html).

#### QEMU

The [QEMU ](https://qemu.org/) package was updated to version 9.2.0. Here are the changes since Ubuntu Oracular.

* The `scsi` property of `virtio-blk` devices has been removed. SCSI command passthrough had never been present on `virtio-blk` 1.0 devices, and is now removed from legacy devices as well. Use `virtio-scsi` instead.
* The `block migration` options to the migrate commands (`blk` and `inc` for QMP, `-b`/`-i` for the human monitor) have been removed; guest management software such as libvirt is able to perform block migration more efficiently using block jobs and NBD devices.
* The `compress` migration capability has been removed; `multifd` migration is able to do compression and can be used instead.
* The `proxy` backend for 9pfs, and the `virtfs-proxy-helper` program, have been removed. Use the `local` backend driver or `virtio-fs` instead.

* x86
  * Support for AMD SEV-SNP using the "-object sev-snp-guest" command line option in QEMU 9.1 followed by fixups for related virtio handling in QEMU 9.2.
  * As usual new named CPU models and detection of their related CPU features, this time new variants of Icelake-Server, Cascadelake-Server, GraniteRapids, and SapphireRapids

* ARM
  *   New CPU architectural features emulated:
        `FEAT_NMI`
        `FEAT_CSV2_3`
        `FEAT_ETS2`
        `FEAT_Spec_FPACC`
        `FEAT_WFxT`
        `FEAT_Debugv8p8`
        `FEAT_EBF16`
        `FEAT_CMOW`
  * The `max` CPU and any new CPU types will default to a 1GHz generic timer frequency rather than the old 62.5MHz (this is architecturally required from ARMv8.6 onwards).
  * KVM-based VMs can now support MTE (if the host CPU has MTE support).
  * 

* RISC-V
    * Support RISC-V privilege 1.13 spec.
    * Implement SBI debug console (`DBCN`) calls for KVM.
    * Add support for `Zve32x` extension.
    * Add support for `Zve64x` extension.
    * Add `th.sxstatus` CSR emulation.
    * Remove experimental prefix from `B` extension.
    * Support the `zimop`, `zcmop`, `zama16b` and `zabha` extensions.
    * Add decode support for `Zawrs` extension.
    * Add `smcntrpmf` extension support.
    * Support 64-bit addresses for `initrd`.
    * QEMU support for KVM Guest Debug on RISC-V.
    * Add `fcsr` register to QEMU log as a part of F extension.
    * Add `Svvptc` extension support.
    * Support for control flow integrity extensions.
    * Support for the IOMMU with the virt machine.

* s390x
  * New architectural features emulated:
    `FMAF`
    `IMA`
    `VIS3`
    `VIS4`
  * No new cpu types with these features are added, yet, but one may enable them manually with `-cpu <type>,+<feature>`.
  * The `s390-ccw` guest firmware now supports booting from other devices in case the previous ones fail.

For more details, please see related upstream changelogs:

* [9.1](https://wiki.qemu.org/ChangeLog/9.1)
* [9.2](https://wiki.qemu.org/ChangeLog/9.2)


#### Samba

Samba was updated to series 4.21.x. Here are some of the highlights:

- LDAP TLS/SASL channel binding support
- Group Managed Service Accounts
- Samba can now claim Functional Level 2012R2 support
- Some Samba public libraries made private by default
- Samba AD will rotate expired passwords on smartcard-required accounts
- Automatic keytab update after machine password change
- and more

For a more detailed explanation, please refer to the upstream release notes at https://www.samba.org/samba/history/samba-4.21.0.html

##### samba on i386

Samba version 4.21.x added a dependency to the `python3-samba` package: `python3-cryptography`. Unfortunately, `python3-cryptography` was last built for i386 for Ubuntu Bionic 18.04, and is no longer available for that architecture, making this new dependency unsatisfiable.

For Ubuntu Plucky, it was decided to not build `python3-samba` for i386. Please see [LP: #2099895](https://bugs.launchpad.net/ubuntu/+source/samba/+bug/2099895) for details. The main consequence is that the `samba-tool` script (part of that package) is no longer available for i386.

##### Upgrading an AD/DC from previous Ubuntu releases

If you have deployed a Samba Active Directory Domain Controller WITHOUT having installed the `samba-ad-dc` package, you should install it before doing a release upgrade to Ubuntu Plucky Puffin 25.04. If `samba-ad-dc` is not installed prior to the release upgrade, the Active Directory Domain Controller functionality will not work on the upgraded system due to many missing components.

See [LP: #2101838](https://bugs.launchpad.net/ubuntu/+source/samba/+bug/2101838) for more information.


#### Squid

Squid 6.13 is a stable release consisting mainly of bugfixes and cleanups.  One functional change of note is that `ext_time_quota_acl` no longer supports the -l option.  For the complete list of changes, see the [v6.13 change list](https://github.com/squid-cache/squid/releases).

#### SSSD

SSSD has been updated to 2.10.1 and these are the highlights:

  - unprivileged service user: there is initial support for running sssd with less privileges, but in Debian/Ubuntu the main daemons still run under root. Filesystem capabilities had to be added to many binary helpers, though:
    - `sssd_pam`: *cap_dac_read_search*
    - `selinux_child`: *cap_setuid*, *cap_setgid*
    - `ldap_child`: *cap_dac_read_search*
    - `krb5_child`: *cap_dac_read_search*, *cap_setuid*, *cap_setgid*
  This should all be transparent.
  - The `sssctl cache-upgrade` command was removed. SSSD will do automatic cache upgrades at startup if needed.
  - Default `ldap_id_use_start_tls` value changed from `false` to `true`.
  - Obsolete `config_file_version` option was removed.
  - Option `reconnection_retries` was removed.

For more details and other changes, please refer to the upstream release notes at https://sssd.io/release-notes/sssd-2.10.0.html.

#### Intel® QuickAssist Technology (Intel® QAT)

Intel® QAT components have been updated to their most recent versions. Those are:
 * qatlib : 24.09.0
   For more information, visit the project’s [repo](https://github.com/intel/qatlib?tab=readme-ov-file#features).
 * qatengine : 1.8.1
   For more information, visit the project’s [repo](https://github.com/intel/QAT_Engine/blob/master/docs/features.md).
 * qatzip : 1.2.1
   For more information, visit the project’s [repo](https://github.com/intel/QATzip?tab=readme-ov-file#features).
 * ipp-crypto : 1:1.0.0
   For more information, visit the project’s [repo](https://github.com/intel/ipp-crypto).

#### Subiquity

Please see the [25.04 Release Notes](https://github.com/canonical/subiquity/releases/tag/25.04) post on GitHub.

#### thin-provisioning-tools

The thin-provisioning tools package was updated to version 1.1.0, which was fully re-written in rust from scratch.

See the [upstream changelog](https://github.com/jthornber/thin-provisioning-tools/blob/v1.1.0/CHANGES) for more details.

#### Ubuntu HA/Clustering


##### fence-agents

fence-agents was updated to version 4.16.0, which introduces bug fixes and a new fence-agents-nutanix-ahv which adds support for Nutanix AHV Cluster.

##### resource-agents

fence-agents was updated to version 4.16.0, which introduces bug fixes and improvements, including support for the asure aznfs filesystem.

#### sos (sosreport)

The `sosreport` package was renamed to `sos` with the upgrade to 4.9.0 from 4.8.0.

* The rename follows upstream name change in 2020 and the removal of `sosreport` and `sos-collector` commands.
* The `sosreport` package will remain as a transitional package that will carry the `sosreport` and `sos-collector` command for a few revisions of Ubuntu.
* `sos upload` is a new sub command, that allows you to upload a collected `sos` or a file to a vendor primarily Canonical or RedHat See [man pages](https://manpages.ubuntu.com/manpages/plucky/en/man1/sos-upload.1.html) for more details.
* Further details on the changes between 4.8.0 and 4.9.0 can be viewed [upstream release notes](https://github.com/sosreport/sos/releases)

### Ubuntu WSL

* WSL images publication has moved to [cdimage.ubuntu.com](https://cdimage.ubuntu.com/ubuntu-wsl/) (previously on cloud-images.ubuntu.com)

### OpenStack

OpenStack has been updated to the [2025.1 (Epoxy)](https://releases.openstack.org/epoxy/) release. This includes packages for Aodh, Barbican, Ceilometer, Cinder, Designate, Glance, Heat, Horizon, Ironic, Keystone, Magnum, Manila, Masakari, Mistral, Neutron, Nova, Octavia, Swift, Vitrage, Watcher and Zaqar.

This release is also provided for Ubuntu 24.04 LTS via the Ubuntu Cloud Archive.

#### Ceph

#### Open vSwitch (OVS) and Open Virtual Network (OVN)

OVS was updated to version 3.5.0, and OVN to 25.03.0.

Common to both projects are changes in SSL/TLS support:
* Protocols can be specified as ranges, e.g `TLSv1.2+` or `TLSv1.2-TLSv1.3`.

* Explicit support for configuring `TLSv1.3` protocol and accompanying ciphersuites. TLSv1.3 was supported in earlier versions only when protocols option was not set.

* Support for TLSv1 and TLSv1.1 is deprecated and will be removed in the next release.

OVS:
* DPDK 24.11.1 support.

* New tool called `ovs-flowviz` capable of visualizing OpenFlow and datapath flow dumps.

* Prefix tracking is enabled by default for both IPv4 and IPv6, allowing to significantly reduce amount of datapath flows generated from mixed IPv4+IPv6 flow tables.

* Userspace datapath TSO now includes support for VXLAN, Geneve and GRE tunneled packets.

* TC offload now supports matching on tunnel flags as well as setting the Don't Fragment (DF) flag in `encap` action.

* Various improvements in `ovs-ctl` for handling IPSec configuration.

OVN:
* Dynamic routing support allows the `ovn-controller` to exchange routing information with a routing protocol daemon.  The `dynamic-routing-redistribute` option controls what routes are redistributed including `lb` and `nat` options which can be used for resource location.  When used together with the routing protocol redirect feature, a routing protocol daemon can speak using a Logical Router Port (LRP) IP implemented in the OVS datapath, facilitating accelerated networking.

* Support was added for routing IPv4 packets over IPv6 networks as well as the ability to create LRPs without specifying an IPv4 address.  When used together with the new dynamic routing features and a suitable routing protocol daemon, this can be used to configure BGP unnumbered peering.

* New Logical Switch Port (LSP) type `switch` to directly connect two logical switches, which can be used to construct multi-stage clos topology for logical switches.

* New Transit Router concept for use with OVN Interconnect which may improve traffic flow between AZs for some configurations.

* New ACL option `persist-established` that allows for established connections to bypass ACL matching.

* Logical router policies can now be arranged in chains, using the new `jump`, `chain` and `jump_chain` actions.

* Support for STT tunnels is deprecated and will be removed in the next release.


#### GRUB2

The cd-boot-images-* packages are no longer used in the build process of plucky ISOs and were removed from the archive. Instead the ISO build processes uses the shim, grub2 and u-boot packages directly, streamlining the build process and reducing maintenance burden.

Also there was about [27 CVE fixes](https://git.launchpad.net/~ubuntu-core-dev/grub/+git/ubuntu/commit/?id=0ac81e083f719a990a0f905e0b80238eda00b2fc) in grub2 release for Plucky!

### Platforms

#### Public Cloud / Cloud images

* `UseDomains=true` is set in `/etc/systemd/networkd.conf.d/50-cloudimg-settings.conf` to restore the pre-Oracular behavior of adding search domains from DHCP responses to `/etc/resolv.conf`. The new default behavior introduced in Oracular broke some common use cases and it is too strict for cloud environments where there's usually no risk of a malicious DHCP server on the network ([LP: #2106729](https://bugs.launchpad.net/cloud-images/+bug/2106729)).

##### How to report any issues resulting from these changes

If you notice any unexpected changes or bugs in the minimal images, create a new bug in [cloud-images](https://bugs.launchpad.net/cloud-images).

#### Raspberry Pi 🍓

* Camera support is now included with libcamera 0.4 and libpisp ([LP: #2038669](https://launchpad.net/bugs/2038669))

* The desktop now uses [gnome-initial-setup](https://launchpad.net/ubuntu/+source/gnome-initial-setup) as the first time setup guide. This runs directly under Wayland, and is much quicker than the legacy ubiquity installer. Please see the known issues section below before reporting bugs against gnome-initial-setup as it is possible you are running into something being worked on

* The above change also means cloud-init is now useable on the Raspberry Pi desktop images; this can be used to automate initial user creation, package installation, customization, etc.

* The legacy libraspberry-bin utilities have been replaced with [raspi-utils](https://launchpad.net/ubuntu/+source/raspi-utils)

* nbd-client is now seeded in the Raspberry Pi images, making it simple to network boot your Pi with these images

#### arm64

* In addition to arm64 server ISO there is now also an official generic arm64 desktop ISO targeting VMs, ACPI + EFI platforms and Snapdragon based WoA devices.
* Initial hardware enablement work for the Snapdragon X Elite platform is included in the desktop ISO

#### IBM Z and LinuxONE (s390x) ![image|32x32](upload://dZM0RRlelqCcZc6RhqJGMW8DMZr.png) 

The key package, 's390-tools', was step-by-step upgraded to latest version v2.37.0 ([LP: #2096789](https://launchpad.net/bugs/2096789), via [LP: #2091549](https://launchpad.net/bugs/2091549)), that covers the removal of scsi_logging_level, since it's now in sg3_utils ([LP: #2098500](https://launchpad.net/bugs/2098500)), the new pvimg and with that the rewritten genprotimg tool in Rust ([LP: #2098046](https://launchpad.net/bugs/2098046)), with it's new info command ([LP: #2098047](https://launchpad.net/bugs/2098047)), to display of encrypted & unencrypted Secure Execution (SE) image information, validations in genprotimg, if an SE image can run on particular host ([LP: #2097576](https://launchpad.net/bugs/2097576)), supporting unencrypted SE images by exposing the resp. SE header flag ([LP: #2098045](https://launchpad.net/bugs/2098045)), supporting extended attestation for SE ([LP: #2097535](https://launchpad.net/bugs/2097535)) and support for retrievable secrets in SE guests ([LP: #2097533](https://launchpad.net/bugs/2097533) and kernel [LP: #2097534](https://launchpad.net/bugs/2097534)).

Further enhancements based on the new 6.14 kernel are support for kprobes without stop machine ([LP: #2100329](https://launchpad.net/bugs/2100329)), providing topology-map information to userspace ([LP: #2098392](https://launchpad.net/bugs/2098392)), PCHID per port toleration ([LP: #2095480](https://launchpad.net/bugs/2095480)) and the new option to display available host key hashes for SE, aka Query Host-key hash UVC ([LP: #2101108](https://launchpad.net/bugs/2101108)).

Improvements in the area of zPCI came on top, with enhanced RAS and Call Home support ([LP: #2095413](https://launchpad.net/bugs/2095413)), the new option of optics monitoring for PF in access mode (s390-tools: [LP: #2095429](https://launchpad.net/bugs/2095429), kernel: [LP: #2095427](https://launchpad.net/bugs/2095427)), the promiscuous mode exploitation for new VFs ([LP: #2096791](https://launchpad.net/bugs/2096791)) and base work in the kernel for CPU-MF counters in support for new IBM Z hardware ([LP: #2101111](https://launchpad.net/bugs/2101111)).

So support of new hardware is another significant area of work - starting with new IBM Z hardware base support in the kernel ([LP: #2100303](https://launchpad.net/bugs/2100303)) PAI/NNPA was updated for new IBM Z hardware ([LP: #2100302](https://launchpad.net/bugs/2100302)) and a new CPU model for new IBM Z hardware (kernel: [LP: #2097523](https://launchpad.net/bugs/2097523) and qemu: [LP: #2097521](https://launchpad.net/bugs/2097521)).
Also user space components were enabled for new IBM Z hardware, like for gdb v16.2 ([LP: #2095361](https://launchpad.net/bugs/2095361)), valgrind v3.24 ([LP: #2095363](https://launchpad.net/bugs/2095363)), binutils v2.44 ([LP: #2095372](https://launchpad.net/bugs/2095372)), libzdnn v1.1.1 for exploiting new AI hardware ([LP: #2095373](https://launchpad.net/bugs/2095373)) - and the smc-tool update to latest v1.8.4 ([LP: #2095005](https://launchpad.net/bugs/2095005)).

Several dedicated new features were added, like:
- the cpacfinfo tool to provide CPACF (on-chip crypto co-processor) information (kernel: [LP: #2096894](https://launchpad.net/bugs/2096894), s390-tools: [LP: #2096896](https://launchpad.net/bugs/2096896))
- the zpwr tool, for LPAR level power consumption reporting (kernel: [LP: #2098391](https://launchpad.net/bugs/2098391), s390-tools: [LP: #2098358](https://launchpad.net/bugs/2098358))
- the chpstat tool, for additional channel measurements (kernel: [LP: #2095483](https://launchpad.net/bugs/2095483), s390-tools [LP: #2095485](https://launchpad.net/bugs/2095485))
- full boot order support in KVM (qemu: [LP: #2049698](https://launchpad.net/bugs/2049698), libvirt: [LP: #2051239](https://launchpad.net/bugs/2051239))
- enablement of virtio-mem support (kernel: [LP: #2097883](https://launchpad.net/bugs/2097883), qemu: [LP: #2097884](https://launchpad.net/bugs/2097884) and libvirt: [LP: #2097886](https://launchpad.net/bugs/2097886)) and
- enablement of dynamic updates of vfio-ap mediated (crypto) devices for management applications (kernel: [LP: #2097489](https://launchpad.net/bugs/2097489), s390-tools: [LP: #2097488](https://launchpad.net/bugs/2097488), libvirt: [LP: #2097487](https://launchpad.net/bugs/2097487) and mdevctl: [LP: #2097486](https://launchpad.net/bugs/2097486))

While mentioning cryptography, there are many more enhancements in this area, like in kernel crypto support:
- for MSA 10 XTS ([LP: #2096809](https://launchpad.net/bugs/2096809))
- for MSA 11 HMAC ([LP: #2096812](https://launchpad.net/bugs/2096812))
- for for MSA 12 (SHA3) ([LP: #2100946](https://launchpad.net/bugs/2100946))
- for PAES support for MSA 10 XTS ([LP: #2100935](https://launchpad.net/bugs/2100935))
but also:
- of MSA 10 and MSA 11 in cpacfstats ([LP: #2096890](https://launchpad.net/bugs/2096890))
- for zkey key for dm-crypt with XTS keys ([LP: #2096892](https://launchpad.net/bugs/2096892))
- for pkey, protected XTS and HMAC keys ([LP: #2100936](https://launchpad.net/bugs/2100936)) and support
- for SE retrieved protected keys ([LP: #2097543](https://launchpad.net/bugs/2097543))

This partially also requires updates in openSSL:
- for MSA 10 XTS support ([LP: #2096810](https://launchpad.net/bugs/2096810))
- for MSA 11 HMAC support ([LP: #2096811](https://launchpad.net/bugs/2096811)) and support
- for MSA 12 (SHA3) ([LP: #2096949](https://launchpad.net/bugs/2096949))

In addition openCryptoki was upgraded to the latest v3.24 ([LP: #2095337](https://launchpad.net/bugs/2095337)), that includes support for:
- CCA token SHA3 ([LP: #2096950](https://launchpad.net/bugs/2096950))
- CCA token RSA OAEP v2.1 ([LP: #2096951](https://launchpad.net/bugs/2096951))
- CCA token cipher keys ([LP: #2097111](https://launchpad.net/bugs/2097111))
- CCA token of Dilithium ([LP: #2096897](https://launchpad.net/bugs/2096897)) and support of
- CKM_RSA_AES_KEY_WRAP for cca, ica and soft tokens ([LP: #2097110](https://launchpad.net/bugs/2097110))

Finally further cryptography-related packages were updated, like:
- p11-kit v0.25.5, to update IBM specific mechanisms (up to IBM z16) ([LP: #2098092](https://launchpad.net/bugs/2098092))
- libica, to latest v4.4.0 ([LP: #2095409](https://launchpad.net/bugs/2095409))
- libzpc v1.3.0, to support protected key derived from SE retrievable secrets ([LP: #2097545](https://launchpad.net/bugs/2097545))

#### IBM POWER (ppc64el)

* The powerpc-utils package was upgraded to the latest available version  1.3.13 ([LP: #2096946](https://launchpad.net/bugs/2096946)).

* The new package 'secvarctl' was added ([LP: #2064345](https://launchpad.net/bugs/2064345)), that allows to handle secureboot artifacts and key management on ppc64el.

#### RISC-V

* Provide a single pre-installed image for all JH7110 boards.
* Support Pine64 Star64


(25-04-known-issues)=
## Known Issues

As is to be expected with any release, there are some significant known bugs that users may encounter with this release of Ubuntu. The ones we know about at this point (and some of the workarounds) are documented here, so you don't need to spend time reporting these bugs again:

### General

* There is a bug ([LP: #2104316](https://bugs.launchpad.net/ubuntu-power-systems/+bug/2104297)) in the *beta* images that prevents netboot installs in some scenarios.
* It has been reported that cloud-init may fails to upgrade properly in the Oracular to Plucky upgrade path, see [LP: #2104316](https://bugs.launchpad.net/ubuntu-power-systems/+bug/2104297).
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
* ZFS may cause kernel freezes during the 25.10 upgrades, rendering the upgrade unable to complete, due to a bug in the interaction between newer ZFS userspace utilities with older kernel modules. ([LP: #2110891](https://bugs.launchpad.net/ubuntu/+source/ubuntu-release-upgrader/+bug/2110891))


### Ubuntu Desktop

* Screen reader support is present with the new desktop installer, but is incomplete ([LP: #2061015](https://launchpad.net/bugs/2061015), [LP: #2061018](https://launchpad.net/bugs/2061018), [LP: #2036962](https://launchpad.net/bugs/2036962), [LP: #2061021](https://launchpad.net/bugs/2061021))

* OEM installs are not supported yet ([LP: #2048473](https://launchpad.net/bugs/2048473))

* GTK4 apps (including the desktop wallpaper) do not display correctly with VirtualBox or VMWare with 3D Acceleration ([LP: #2061118](https://launchpad.net/bugs/2061118)).

* **Incompatibility between TPM-backed Full Disk Encryption and Absolute:** TPM-backed Full Disk Encryption (FDE) has been introduced to enhance data security. However, it's important to note that this feature is incompatible with Absolute (formerly Computrace) security software. If Absolute is enabled on your system, the machine will not boot post-installation when TPM-backed FDE is also enabled. Therefore, disabling Absolute from the BIOS is recommended to avoid booting issues.
* **Hardware-Specific Kernel Module Requirements for TPM-backed Full Disk Encryption:** TPM-backed Full Disk Encryption (FDE) requires a specific kernel snap which may not include certain kernel modules necessary for some hardware functionalities. A notable example is the `vmd` module required for NVMe RAID configurations. In scenarios where such specific kernel modules are indispensable, the hardware feature may need to be disabled in the BIOS (such as RAID) to ensure the continued availability of the affected hardware post-installation. If disabling in the BIOS is not an option, the related hardware will not be available post-installation with TPM-backed FDE enabled.
* [FDE specific bug reports](https://bugs.launchpad.net/bugs/+bugs?field.searchtext=&orderby=-importance&field.status%3Alist=NEW&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.tag=fde&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search).

* Resuming from suspend on Nvidia desktops (where Nvidia is the primary GPU so generally not laptops)  will exhibit visual corruption and freezes using the default Wayland session  ([LP#1876632](https://bugs.launchpad.net/bugs/1876632)). If you need suspend/resume support then the simplest solution is to select 'Ubuntu on Xorg' at the login screen.

* Installing `ubuntu-fonts-classic` results in a non-Ubuntu font being displayed ([LP#2083683](https://bugs.launchpad.net/bugs/2083683)). To resolve this, install `gnome-tweaks` and set ‘Interface Text’ to ‘Ubuntu’.

### Ubuntu Server

#### rabbitmq-server

Certain version hops may be unsupported due to feature flags, raising questions about how Ubuntu will maintain this package moving forward. We are currently exploring the use of snaps as a potential solution to enable smoother upgrades. For more information please read https://bugs.launchpad.net/bugs/2074309.

#### libvirt

Libvirt provides the default network on install, in a nested installation it modified the configuration to not conflict with the one already provided by the first level host. There is an [issue](https://bugs.launchpad.net/ubuntu-release-notes/+bug/2107448) where the file it needs to modify is not yet present when it needs to modify it. That will be fixed via an SRU, but until then it can be worked around by installing `libvirt-daemon-config-network` before installing the other libvirt components that are needed in that nested environment.

#### Openstack

Currently, Nova Compute is non-functional because of a python3.13 incompatiblity ([LP:#2103413](https://bugs.launchpad.net/ubuntu/+source/nova/+bug/2103413)).
The Openstack team and Upstream work on it and it will be resolved via an SRU later.

The Ubuntu Cloud Archive is not affected by this bug.

#### Installer

On systems booting via U-Boot, U-Boot should be updated to the current Plucky version before installation as subiquity does not run flash-kernel and grub-update during the installation. So for first boot the device-tree from U-Boot will be used.

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

#### s390x

* Plucky provides better apparmor isolation for the tools in util-linux which is great, but it was found that on s390x this might break usage of lsblk. Fixes will soon be provided via bug [2107402](https://bugs.launchpad.net/ubuntu/+source/apparmor/+bug/2107402) and bug [2107455](https://bugs.launchpad.net/ubuntu/+source/apparmor/+bug/2107455). Until then the effect will be that lsblk on s390x will show no devices or in s390x based containers segfault. Until the SRU is available that can be mitigated by disabling the related apparmor profile via `aa-disable lsblk`.

#### ppc64el

* Ubuntu Server for IBM Power installation using SAN disks ([LP: #2107523](https://bugs.launchpad.net/bugs/2107523/), [LP: #2080474](https://bugs.launchpad.net/bugs/2080474/)) will fail in case disks have existing configurations. A potential workaround is to wipe (wipefs) the disks first (using the installer shell) and then restart the installation with a clean disk.
* PMDK sees some hardware-specific failures in its test suite, which may make the software partially or fully inoperable on the ppc64el architecture. ([LP: #2061913](https://bugs.launchpad.net/ubuntu/+source/pmdk/+bug/2061913/))
* For interfaces attached via 'virsh attach-interface' to be reflected and visible in a ppc64el KVM guest running inside a PowerVM LPAR a reboot is required (regardless if option '--live' got used or not) ([LP: #2111231](https://bugs.launchpad.net/bugs/2111231)).

#### Raspberry Pi

* The new gnome-initial-setup has some teething issues:
  - Time zone input dropdown can "wobble" ([LP: #2084611](https://launchpad.net/bugs/2084611))
  - The localization of the application fails ([LP: #2104148](https://launchpad.net/bugs/2104148))
  - The hostname change is mandatory ([LP: #2093132](https://launchpad.net/bugs/2093132))

* During boot on the server image, if your `cloud-init` configuration (in `user-data` on the boot partition) relies upon networking (importing SSH keys, installing packages, etc.) you *must* ensure that at least one network interface is required (`optional: false`) in `network-config` on the boot partition. This is due to netplan changes to the wait-online service (~~[LP: #2060311](https://launchpad.net/bugs/2060311)~~)

* The seeded totem video player will not prompt users to install missing codecs when attempting to play a video requiring them ([LP: #2060730](https://launchpad.net/bugs/2060730))

* With the removal of the `crda` package in 22.04, the method of setting the wifi regulatory domain (editing `/etc/default/crda`) no longer operates. On server images, use the `regulatory-domain` option in the Netplan configuration. On desktop images, append `cfg80211.ieee80211_regdom=GB` (substituting `GB` for the relevant country code) to the kernel command line in the `cmdline.txt` file on the boot partition  ([LP: #1951586](https://launchpad.net/bugs/1951586)).

* The power LED on the Raspberry Pi 2B, 3B, 3A+, 3B+, and Zero 2W currently goes off and stays off once the Ubuntu kernel starts booting ([LP: #2060942](https://launchpad.net/bugs/2060942))

* Colours appear incorrectly in the Ubuntu App Centre ([LP: #2076919](https://launchpad.net/bugs/2076919))

* On server images, re-authentication to WiFi APs when regulatory domain is set result in dmesg spam to the console ([LP: #2063365](https://launchpad.net/bugs/2063365))

* The default audio output on the Raspberry Pi 4 is "Analogue Output - Built-in Audio" instead of "HDMI/Displayport", so you might be confused after the first boot when you hear no sound even after moving the volume slider. You can change the audio output to HDMI in the settings, which persists in subsequent boots. ([LP: #1993347](https://bugs.launchpad.net/ubuntu/+source/pipewire/+bug/1993347))

#### Google Compute Platform 

Nothing yet.

#### Microsoft Azure

* The current version of walinuxagent relies on python3-legacycrypt for password changing functionality but it cannot be made a dependency due to a component mismatch ([LP: #2106484](https://launchpad.net/bugs/2106484)).

#### s390X

Nothing yet.

(25-04-official-flavors)=
## Official flavors

Find the release notes for the official flavors at the following links:

* [Edubuntu Release Notes](https://discourse.ubuntu.com/t/edubuntu-25-04-released)
* [Kubuntu Release Notes](https://wiki.ubuntu.com/PluckyPuffin/ReleaseNotes/Kubuntu)
* [Lubuntu Release Notes](https://lubuntu.me/plucky-released/)
* [Ubuntu Budgie Release Notes](https://ubuntubudgie.org/2025/04/ubuntu-budgie-25-04-release-notes/)
* [Ubuntu MATE Release Notes](https://ubuntu-mate.org/blog/ubuntu-mate-p-p-release-notes/)
* [Ubuntu Studio Release Notes](https://discourse.ubuntu.com/t/ubuntu-studio-25-04-release-notes/)
* [Ubuntu Unity Release Notes](https://ubuntuunity.org/posts/ubuntu-unity-2504-released/)
* [Xubuntu Release Notes](https://wiki.xubuntu.org/releases/25.04/release-notes)
* [Ubuntu Kylin Release Notes](https://ubuntukylin.com/news/ubuntukylin2504-en.html)
* [Ubuntu Cinnamon Release Notes](https://ubuntucinnamon.org/?p=1348)


(25-04-more-information)=
## More information

Refer to {ref}`release-policy-and-schedule` and {ref}`project-and-community`.
