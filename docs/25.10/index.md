---
tocdepth: 3
---

(ubuntu-25.10-release-notes)=
# Ubuntu 25.10 release notes

These release notes for **Ubuntu 25.10** (Questing Quokka) provide an overview of the release and document the known issues with Ubuntu and its flavors.

:::{toctree}
:maxdepth: 1
:hidden:

Release schedule <schedule>
:::

## Support lifespan

Ubuntu 25.10 will be supported for 9 months until July 2026. If you need long term support, we recommend you use [Ubuntu 24.04.3 LTS](https://ubuntu.com/download) which is supported until at least 2029.

## Upgrades

Upgrades to 25.10 are expected to be enabled on or before Nov 3.

Current blockers:

* [LP#2125535](https://bugs.launchpad.net/ubuntu/+source/rust-coreutils/+bug/2125535)
* [LP#2127970](https://bugs.launchpad.net/ubuntu/+source/rust-coreutils/+bug/2127970)

(25-10-new-features-in-25-10)=
## New features in 25.10

### Updated Packages

### Linux kernel 6.17🐧
This release delivers the newest 6.17 Linux kernel. Due to the final upstream release occurring after Kernel Freeze, the kernels shipped with the release images will be based on `6.17-rc7`. Updates for all Questing Quokka kernels are scheduled for release in the subsequent week to incorporate the final upstream 6.17 release.

Highlights for this release:
* The `linux-modules-extra-*` packages have been deprecated ([LP#2042831](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2042831)). All the kernel modules are now shipped by the `linux-modules-<version>-<flavor>` packages.
* `linux-generic` for arm64 will provide via `stubble` broader compatibility for arm64 desktop platforms that utilize UEFI for booting ([LP#2121352](https://bugs.launchpad.net/ubuntu/+source/linux-signed/+bug/2121352)).
* The foundation for Intel TDX Host Support was merged upstream on Linux 6.16 with additional improvements included in 6.17. The Ubuntu 6.17 kernel will ship with early support for kexec/kdump for TDX-enabled hosts ([LP#2121873](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2121873)).
* From 25.10, the Ubuntu RISC-V kernel (`linux-riscv`) will only support hardware that implements the RVA23S64 ISA profile. Systems that don't satisfy this requirement will not be able to run 25.10. The RISC-V kernel in 24.04 will continue to support boards with RVA20 processor cores.
* Other features can be found in the [Linux 6.17 upstream](https://kernelnewbies.org/Linux_6.17) changelog.

### systemd v257.9
The init system was updated to systemd v257.9. See the [upstream changelog ](https://github.com/systemd/systemd/releases/tag/v257) for more information about individual features.

### sudo-rs and sudo

sudo-rs is the **default sudo provider** on Ubuntu from 25.10 onwards. 0.2.8 release includes support for older Linux kernels < 5.9, sudoedit, support for NOEXEC and AppArmor profile switching. The Ubuntu release also includes various bug fixes picked from the main upstream branch.

sudo (original sudo maintained by Todd C. Miller) has been upgraded to the latest version 1.9.17p2. The binary files are now renamed with the `.ws` suffix. Additionally, sudo-ldap package has been removed, please switch to using LDAP authentication via PAM.

Please see [Ubuntu Server Docs](https://documentation.ubuntu.com/server/how-to/security/user-management/#sudo-rs) for configuring default sudo provider and differences between sudo-rs and sudo.ws.

### rust-coreutils and gnu-coreutils
The core utilities of the operating system are now provided by the **[rust-coreutils ](https://launchpad.net/ubuntu/+source/rust-coreutils) package**. We just updated to the latest version of it: 0.2.2, which features incredible performance improvements to base64 amongst other things.

As rust-coreutils are not necessarily fully compatible yet, we are providing the old utilities by the side, so you can switch back and forth between them. We are also keeping a list of these diversions [here](https://git.launchpad.net/ubuntu/+source/coreutils-from/tree/debian/coreutils-from-uutils.links).

### Netplan v1.1.2ubuntu3 🌐
Adds support non-standard OVS setups, e.g. inside snap environments.

### Toolchain Upgrades 🛠️
* GCC 🐄 GCC is updated to 15.2, binutils to 2.45, and glibc to 2.42
* Python 🐍 is updated to 3.13.7 while 3.14 is now available
* LLVM 🐉 defaults to version 20 while 21 is now available
* Rust 🦀 toolchain defaults to version 1.85 while 1.88 is now available
* Golang 🐀 is updated to 1.24
* OpenJDK ☕ defaults to 21 (LTS), while version 25 (LTS) and an early access snapshot of version 26 are now available
* .NET 10 🦄 now available
* Zig ⚡ is available for the first time in Ubuntu, defaults to version 0.14.1.
* And Ubuntu Toolchains has a new [homepage](https://ubuntu.com/toolchains)

#### OpenJDK

OpenJDK 21 is still the default. OpenJDK 25 (LTS) is now available. An early access snapshot of OpenJDK 26 is also included. Support for OpenJDK LTS versions 17, 11 and 8 is being maintained. OpenJDK with CRaC version 25 is also made available, while versions 17 and 21 continue to be supported. 

The [devpack-for-spring snap](https://snapcraft.io/devpack-for-spring) now supports development environment setup, by automating the installation and configuration of development tools (OpenJDK, container runtime, IDEs etc.) selected by the user. The [Maven and Gradle plugins for Rockcraft](https://github.com/rockcrafters/java-rockcraft-plugins) have been extended to support native images compiled by GraalVM. 

GraalVM Community Edition v25 is available through the graalvm-jdk [snap](https://snapcraft.io/graalvm-jdk), while GraalVM CE v21 continues to be supported. The snap is now available on arm64 too. 

#### .NET
.NET versions 8 and 9 continue to be supported.

The .NET 10 RC1 SDK and runtimes are now included. Following its general availability in November, the final release will be provided as a subsequent package update.

Alternatively, .NET 10 is available on the `latest/beta` channel of the official .NET snap. It will be promoted to the `latest/stable` channel upon final release in November.

Support for the PowerShell snap has been expanded to include the `arm64`, `s390x`, and `ppc64el` architectures, broadening its availability across platforms.

### Default configuration changes ⚙️

### Ubuntu Desktop

#### Installer

New [TPM-Backed disk encryption](https://canonical-ubuntu-desktop-documentation.readthedocs-hosted.com/en/latest/explanation/hardware-backed-disk-encryption/) features include:

* Passphrase support and management
* Regeneration of the recovery key 
* Better integration with firmware updates

When you enable *Install third-party software for graphics and Wi-Fi hardware and additional media formats* during installation, screen recording will be hardware accelerated for supported hardware.

The installer has also seen plenty of accessibility fixes.

#### Updates

When system updates are available, the Software Updater window no longer pops up unprompted, stealing the keyboard focus. Instead, a notification shows up with options to open the Software Updater or to install all updates directly.

An icon in the system tray reminds you that updates are available even after dismissing the notification. It also provides a quick way to apply all the updates or inspect them in the Software Updater.

#### Enterprise

[authd](https://github.com/ubuntu/authd): Ubuntu’s cloud authentication solution:
* Supports device registration with EntraID
* authctl is a new command line tool to manage authd
* Many improvements and important bug fixes such as UID/GID handling 

#### Wayland

* The Ubuntu Desktop session now runs only on the Wayland back end. The [Ubuntu on X\.org session is no longer available](https://discourse.ubuntu.com/t/ubuntu-25-10-drops-support-for-gnome-on-xorg/62538) because GNOME Shell can no longer run as an X\.org session.

* Suspend-resume support is now enabled in the proprietary Nvidia driver so as to prevent corruption and freezes when waking an Nvidia desktop.

#### GNOME 👣

* GNOME Shell and related components have been updated to [GNOME 49](https://release.gnome.org/49/).
* You can now set an application to start automatically after login in Settings -> Apps.
* Fractional scaling factors are now optimized so as to minimize blur.
* The default monospace font size has been reduced to match the default user interface font size. The monospace font is used in terminals and similar applications.

#### New default applications

* The **Image Viewer** app is now provided by [Loupe](https://apps.gnome.org/Loupe/) instead of Eye of GNOME (EOG). Loupe is written in Rust and powered by the [Glycin](https://gitlab.gnome.org/GNOME/glycin) library.
* The **Terminal** app is now provided by [Ptyxis](https://gitlab.gnome.org/chergert/ptyxis/-/blob/main/README.md?ref_type=heads) instead of GNOME Terminal.

#### Security Center

- You can now manage your recovery key for the TPM-backed Full Disk Encryption. For details, see [Encrypt your disk with TPM](https://canonical-ubuntu-desktop-documentation.readthedocs-hosted.com/en/latest/how-to/encrypt-your-disk-with-tpm/).

#### Ubuntu Insights

[Ubuntu Insights](https://github.com/ubuntu/ubuntu-insights) is being developed as a replacement for [Ubuntu Report](https://github.com/ubuntu/ubuntu-report) and gives you more control over the non-personally identifying system metrics that you choose to share with Canonical. The metrics collection is opt-in.

In this release, Ubuntu Insights introduces periodic metric collection and replaces Ubuntu Report integration in GNOME Initial Setup.

Note: Any consent that you previously granted to Ubuntu Report will not be carried over to Ubuntu Insights.

#### Dracut

Ubuntu Desktop 25.10 now uses Dracut as its default initial ramdisk infrastructure, replacing `initramfs-tools`. Dracut uses `systemd` in the initial ramdisk and supports new features like Bluetooth and NVM Express over Fabrics (NVMe-oF). Ubuntu Server installations and Ubuntu Desktop for Raspberry Pi continue to use `initramfs-tools` while we port the [remaining hooks](https://bugs.launchpad.net/ubuntu/+source/dracut/+bug/2125790). The original `initramfs-tools` remains supported and you can switch between the two implementations if required. For details about the switch, see https://discourse.ubuntu.com/t/spec-switch-to-dracut/54776.

#### Updated Applications
* [Firefox](https://mozilla.org/firefox/releases/) 143 🔥🦊
* [LibreOffice 25.8](https://wiki.documentfoundation.org/ReleaseNotes/25.8) 📚
* [OpenVINO™ Toolkit 2025.2.0](https://github.com/openvinotoolkit/openvino/releases/tag/2025.2.0) 🤖 includes [openvino.genai](https://github.com/openvinotoolkit/openvino.genai) for the first time. 
Also related to that:
  * [Audacity 3.7.1](https://support.audacityteam.org/additional-resources/changelog/audacity-3.7) 🎧 comes with OpenVINO™ AI plugins for music separation, noise suppression, music generation and continuation, transcription, and super resolution, and can be run on Intel CPU, GPU, and NPU.
  * [GIMP 3.0.4](https://www.gimp.org/news/2025/05/18/gimp-3-0-4-released/) 🖼️ which supports the usage of the [snap](https://snapcraft.io/openvino-ai-plugins-gimp) to add AI functionality to GIMP for stable diffusion, super resolution, and semantic segmentation via [OpenVINO™ AI plugins for GIMP 3.1.2](https://github.com/intel/openvino-ai-plugins-gimp/releases/tag/3.1.2).

#### Updated Subsystems
* [BlueZ 5.83](https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/ChangeLog?id=5.83) 💙
* [Pipewire 1.4.7](https://gitlab.freedesktop.org/pipewire/pipewire/-/raw/1.4.7/NEWS) 🔊

#### Support for new Intel® integrated and discrete GPUS

This release brings full support for Intel® Core™ Ultra Xe3 integrated Intel® Arc™ graphics, and Intel® Arc™ Pro B50 and B60 “Battlemage” discrete GPUs. Further Intel® Graphics related features are now available by changes in various components:

* Via the [Linux Kernel](https://launchpad.net/ubuntu/+source/linux) v6.17:
  * Initial support for Intel's next-gen client platform codenamed Panther Lake
  * Enhanced IOMMU and PCIe subsystem for improved GPU virtualization and passthrough.
  * Improved multi-GPU configuration support for Intel hardware.
* Via [Mesa](https://launchpad.net/ubuntu/+source/mesa) 25.2.3:
  * VK_KHR_shader_bfloat16 enabled in Intel ANV Vulkan driver for Battlemage and Panther Lake** (GFX125+).
  * Completed OpenCL 2.0 coarse grain buffer SVM support in Iris driver.
  * Improved color fast-clear handling and multi-engine surface usage for Intel Vulkan (ANV) driver.
* Via [intel-media-driver](https://launchpad.net/ubuntu/+source/intel-media-driver) 25.3.0:
  * Panther Lake Upstream decoding and VP9 encoding support
* Via [intel-compute-runtime](https://launchpad.net/ubuntu/+source/intel-compute-runtime) 25.31:
  * Enabling a Level Zero device unified shared memory (USM) pool as a performance change.
  * A performance-minded change for Xe2 graphics to ensure Level Zero events are always allocated in the local device memory.
* Via [level-zero](https://launchpad.net/ubuntu/+source/level-zero) 1.24
  * Update Level Zero Loader and Headers to support v1.13.1 of L0 Spec
* Via [level-zero-raytracing](https://launchpad.net/ubuntu/+source/level-zero-gpu-raytracing) 1.1.0:
  * Ray Tracing Acceleration Structure (RTAS) Extensions

### Ubuntu Foundations

* https://discourse.ubuntu.com/t/ubuntu-25-10-foundations-edition-what-s-coming-and-what-s-next/68147#p-177120-foundations-toolchains

#### Cryptography

##### Libraries

OpenSSL has been updated to [3.5.3 ](https://github.com/openssl/openssl/blob/master/NEWS.md#openssl-35) (It includes security patches from 3.5.4). The most notable updates are:
* Support for server side QUIC (RFC 9000).
* Support for PQC algorithms (ML-KEM, ML-DSA and SLH-DSA).
* The default TLS supported groups list has been changed to include and prefer Hybrid PQC KEM groups.

#### Package Management: APT 3.1

APT has been updated to 3.1.6, the latest release, including many new features:

* The new solver is now the default. For more insight, see the post "[How we delivered the new APT solver in 25.10](https://discourse.ubuntu.com/t/how-we-delivered-the-new-apt-solver-in-25-10/68920)"
* The `apt why` and `apt why-not` commands have been added that tell you why the solver installed or could not install a package.
* Repositories can now be configured with `Include` and `Exclude` directives. In the `Include` case, only these packages are included; in the `Exclude` case, these packages are excluded from the repository. This allows you to restrict a repository to specific packages.
* The `apt history-list` and `apt history-info` commands are included as an early preview easter egg. Enjoy!

### Ubuntu Server

#### ubuntu-server Meta and Seed

Starting in 25.10, the default Ubuntu server image and `ubuntu-server` metapackage have been updated. Read more at the [public spec on Discourse.](https://discourse.ubuntu.com/t/ubuntu-server-seed-changes-for-25-10/61552)

* `screen` has been removed from the ubuntu-server seed, and moved to a supported seed. `screen` remains in `main`. Users will still see `screen` installed in most cases, as it is now listed as a [dependency of `ubuntu-release-upgrader`](https://bugs.launchpad.net/ubuntu/+source/ubuntu-release-upgrader/+bug/2116874)
* `wget` has been removed from the ubuntu-server seed, and moved to a supported seed. `wget` remains in `main`. Users utilizing `wget` have a number of options.
  * for simple cases (downloading a file from the internet), `wcurl` is available as part of the still included `curl`.  This can be a drop-in replacement for simple calls such as `wget $URL` to `wcurl $URL`. `wcurl` exposes all of `curl`'s options, so adding retries is easy.
  * For more specialized cases, ensuring `wget` is installed prior to running is required.
* `byobu` has been removed from the ubuntu-server seed and meta-package and demoted to `universe`. `byobu` is still available in Ubuntu.
* `cloud-guest-utils` has been removed from the ubuntu-server seed and meta-package. It is expected to still be installed via `cloud-init-base` which is a dependency of `cloud-init`.
* `dirmngr` has been removed from the ubuntu-server seed and metapackage. it is expected to still be installed as it is a dependency of many packages (`gnupg`, `gpg`, `vanilla-gnome-desktop` and other desktop flavors).

#### Apache 2

Apache 2 has been upgraded to version 2.4.64. This new release includes several bug and security fixes. It also includes the following changes to specific modules:

* core: Report invalid Options= argument when parsing AllowOverride directives.
* mod_systemd added systemd socket activation support.
* Mod_http2 was updated to version 2.0.32, which includes a new directive `H2MaxHeaderBlockLen` to set the limit on response header sizes.
* Mod_proxy now reuses ProxyRemote connections when possible.

For more details, see the [upstream release notes](https://www.apachelounge.com/Changelog-2.4.html).

#### Bacula

This is a newly supported package in our “main” repo (was “universe” before).

It was updated from 13.0.4 to 15.0.3 (there was no v14).

* You must upgrade the director and storage daemons at the same time.
* Old file daemons are still compatible.
* Storage volume format was updated from `BB02` to `BB03`, old volumes are still supported.
* The catalog database schema needs migration, which is automatically applied if you have installed `dbconfig-common`.

For more details, see the upstream [v15](http://gitlab.bacula.org/bacula-community-edition/bacula-community/-/releases/Beta-15.0.1) and [v15.0.3](https://gitlab.bacula.org/bacula-community-edition/bacula-community/-/blob/Release-15.0.3/bacula/ChangeLog) changelog.

#### Chrony
Chrony was upgraded to version v4.7 and comes pre-installed as the new default *time-daemon* in Ubuntu 25.10, replacing **systemd-timesyncd**. It ships with a configuration set to use Ubuntu **Network Time Security (NTS)** servers by default. In order to migrate upgraded systems to **chrony** you can execute `apt-mark auto systemd-timesyncd && apt install chrony`.

See upstream [release notes for v4.7](https://chrony-project.org/news.html#_jun_11_2025_chrony_4_7_released).

The two primary changes related to NTS are:

* NTS/KE ("Key Exchange") uses a separate port (4460/tcp) to negotiate security parameters,   which are then used via the normal NTP port (123/udp).

* A new CA is installed in `/etc/chrony/nts-bootstrap-ubuntu.crt` that is used specifically for the Ubuntu NTS bootstrap server, needed for when the clock is too far off. This is added to certificate set ID "1", and defined via `/etc/chrony/conf.d/ubuntu-nts.conf`.

If your network does not allow access to the Ubuntu NTS servers or the required ports, and the new configuration is in place, **chrony** will not be able to adjust this system's clock. To revert to NTP, edit the configuration file in `/etc/chrony/sources.d/ubuntu-ntp-pools.sources` and revert to using the listed NTP servers in favor of the NTS ones.

#### cloud-init v. 25.3

Notable features beyond 25.1.2 in Plucky:

* Add RaspberryPi OS support
* CentOS support for ca_certs writing
* Azure: better reporting of platform VM ID errors
* CloudStack: add ephemeral network support for early boot config
* EC2: Support metadata retrieval over multiple NICs when crawling the datasource
* GCE: add template rendering support for processing instance data
* Hetzner: report private networks in cloud-init metadata
* Oracle: detect ipv6 only for private ULA addresses
* VMware: support to apply network configuration updates per-boot and hotplug events
* WSL: support for Landscape installation request id provisioning
* Add a generalized datasource clean operation for `sudo cloud-init clean`
* Security fix: hotplug socket file is now only root-writable CVE-2024-11584
* NetworkManager bug fix for reloading multiple connections
* ENI rendering filter out dns entries from written config

Breaking changes:

* Security fix CVE-2024-6174: cloud-init will be disabled on non-x86 platforms which do not declare a known datasource in early boot through DMI data, kernel boot params, filesystem configuration or environment files. Such environments may experience inability to SSH into launched VMs. [This may require action for non-x86 image creators or OpenStack admins](https://cloudinit.readthedocs.io/en/latest/reference/breaking_changes.html#id2).

#### Container runtimes

Containerd was updated to the recent 2.1.3 and runC to 1.3.0, docker.io was updated to 28.2
But even more importantly along these updates it established a pattern to either keep the regular updates to the latest version or to opt for slower more stable updates throughout the time the release is active. For more please read [Ubuntu Server Gazette - Issue 8 - Containers: Steady paths for agile stacks ](https://discourse.ubuntu.com/t/ubuntu-server-gazette-issue-8-containers-steady-paths-for-agile-stacks/68680)

#### Django

Django has been updated to the latest LTS release 5.2 from 4.2, which includes many new features and bug fixes. All Django middleware provided in Ubuntu has also been updated to be compatible with the new version. See the [5.0 release notes ](https://docs.djangoproject.com/en/5.2/releases/5.0/) for features and updates added with the major version change and the [5.2 release notes ](https://docs.djangoproject.com/en/5.2/releases/5.2/) for the changes made leading up to the LTS release.

#### Dovecot
Upgrading from Dovecot 2.3.x to 2.4 requires several important config file changes. These are explained in detail in the link below. This includes renamed configuration parameters as well as a major change to the syntax. While converting an existing config is possible, it will need careful review to ensure your site customizations are carried through properly.

Additionally, Dovecot 2.4 brings new features including support for the ARGON2 password scheme, SCRAM-SHA-1 and SCRAM-SHA-256 SASL mechanisms, and the X25519 and X448 cryptographic curves for some plugins. A number of features are being removed, changed, or deprecated; for the full list please see:

* https://doc.dovecot.org/main/installation/upgrade/2.3-to-2.4.html

Notably, support for building for 32-bit architectures has ended, so dovecot will no longer be natively installable on i386 and armhf platforms.

#### EDK2

* Added firmware for Intel ® TDX guests with secure boot capability ([LP#2125123](https://bugs.launchpad.net/ubuntu/+source/edk2/+bug/2125123))

#### frr
FRRouting is a free and open source Internet routing protocol suite for Linux and Unix platforms. It implements BGP, OSPF, RIP, IS-IS, PIM, LDP, BFD, Babel, PBR, OpenFabric and VRRP, with alpha support for EIGRP and NHRP.

The FRRouting package was updated to version 10.4.1. Series 10.4.x introduced many new features and bugfixes: please see https://github.com/FRRouting/frr/releases/tag/frr-10.4.0 for details.

#### HAProxy

Updated from 3.0.8 to the recent release 3.0.10 which includes

* https://www.mail-archive.com/haproxy@formilux.org/msg45741.html

* https://www.mail-archive.com/haproxy@formilux.org/msg45804.html

Furthermore, it now uses jemalloc for memory allocation which is [faster and less memory hungry than the default allocator](https://github.com/haproxy/haproxy/issues/1782#issuecomment-1183128613).

#### iPXE

- [iPXE](https://ipxe.org/) was updated to [upstream version from June 2025](https://github.com/ipxe/ipxe/compare/fbbdc3926...b3ebf8b24ae40a6f9f9f78491702d508f843e56).
- For physically booting to iPXE (e.g. via grub), make sure to install the `grub-ipxe` package and to adjust you GRUB scripts/config to use `ipxe.efi` (UEFI) or `ipxe.lkrn` (x86 BIOS).
- UEFI network boot roms for qemu (from `ipxe-qemu`) are network drivers only (for PXE or HTTP boot) without the iPXE stack.
  To boot x86-64 qemu VMs with UEFI and network boot using iPXE scripts, make sure to chainload `ipxe.efi` (from `ipxe` package) (see https://ipxe.org/howto/chainloading).

#### libvirt

The [libvirt ](https://libvirt.org) package was upgraded to version 11.6.0. Here are the important changes since Ubuntu Plucky:

* qemu: ppc64 POWER11 processor support
* Allow control over QEMU TLS priority strings
* qemu: Add support for NVMe disks
* qemu: add support for AMD IOMMU device
* qemu: Add support for Intel ® TDX guests
* Adds TDX as a new type of `<launchSecurity/>`.
* All helper programs are now detected from $PATH during runtime - allowing you to modify its behavior more easily
* qemu: Added guest load averages to the output of virDomainGetGuestInfo
* qemu: Add support for multiple iothreads for virtio-scsi controller
* qemu: integrate support for VM shutdown on host shutdown - a new opt-in way to shut down guests on host shutdown
* qemu: Add support for parallel save/restore
* qemu: Support for Block Disk Along with Throttle Filters
* nodedev: Support ccwgroup based qeth devices
* Introduce virtio-mem `<memory/>` model for s390 guests

For more details, please see [the upstream changelog ](https://libvirt.org/news.html#v11-4-0-2025-06-02).
Additionally in Ubuntu, the **default URI choice** behavior was modified slightly: In the past Ubuntu enforced the `qemu:///system` URI by overriding `LIBVIRT_DEFAULT_URI` in `/etc/profile.d/libvirt-uri.sh`. Starting with Ubuntu 25.10, we're dropping that `profile.d` script in favour of a fallback mechanism, which still **preserves the default behavior** as `qemu:///system` for privileged and non-privileged users, but allows to override that default choice by setting `LIBVIRT_DEFAULT_URI` manually or changing the `uri_default` parameter in `/etc/libvirt/libvirt.conf` or `~/.config/libvirt/libvirt.conf` (for non-privileged users) respectively.

#### MySQL

MySQL 8.4 now builds directly against tcmalloc for additional memory efficiency. For more information, see the most recent edition of the [Ubuntu Server Gazette](https://discourse.ubuntu.com/t/ubuntu-server-gazette-issue-7-mysql-memory-allocation/66197).

#### Nginx

Nginx was updated from 1.26.3 that we had in plucky to the latest stable version 1.28 which, among many other fixes and improvements, brings:

* Performance and stability improvements in HTTP/3 and QUIC

* Feature: SSL certificates, secret keys, and CRLs are now cached on start or during reconfiguration.

For more details see the [upstream release notes](https://nginx.org/en/CHANGES-1.28)

#### OpenLDAP

Updated from 2.6.9 to 2.6.10, which contains various bugfixes. See the [2.6 series upstream release notes](https://git.openldap.org/openldap/openldap/-/blob/OPENLDAP_REL_ENG_2_6/CHANGES)

#### OpenSSH

Updated to the new major 10.0 upstream release, which among other things now uses a hybrid post-quantum algorithm by default for key agreement. It also adds support for glob patterns in “Authorized{Keys,Principals}File” and `Match version/sessiontype/command` stanzas inside `ssh[d]_config`, e.g. "Match version OpenSSH_10.*". And adds support for FIDO tokens that return no attestation data.

Breaking changes

* Removes support for the weak DSA signature algorithm.
* Announces itself as "SSH-2.0-OpenSSH_10.0". Do not match on “OpenSSH_1*”.

For more please see the [full release notes](https://www.openssh.com/txt/release-10.0)

#### PHP

Upgrade to the 8.4.11 upstream version. The upgrade mostly improves stability and security, fixing crashes and leaks. It brings fixes for a few CVEs (CVE-2025-1735, CVE-2025-6491, CVE-2025-1220).

For more read the [upstream changelog](https://www.php.net/ChangeLog-8.php#8.4.11) since the former version in Plucky that was 8.4.5

#### PostgreSQL

PostgreSQL stayed on version 17, but received the stable updates (which we also backport regularly) and now is on 17.6.

A dump/restore is not required for those running 17.X.

If you have self-referential foreign key constraints on partitioned tables, it may be necessary to recreate those constraints to ensure that they are being enforced correctly.

If you have any BRIN numeric_minmax_multi_ops indexes, it is advisable to reindex them after updating.

For more details check the upstream release notes for [17.5](https://www.postgresql.org/docs/release/17.5/) and [17.6](https://www.postgresql.org/docs/release/17.6/).

#### QEMU

The [QEMU](https://qemu.org/) package was updated to version 10.1.0. Here are the changes since Ubuntu 25.04.

* Arm is able to emulate Secure EL2 physical and virtual timers as well as architectural features  `FEAT_AFP, FEAT_RPRES, FEAT_XS` and even more by 10.1
* Arm's virt board can configuring a larger PCIe MMIO regions via `highmem-mmio-size`
* RISC-V got various improvements like
  * support for Smdbltrp, Ssdbltrp and Smrnmi extensions
  * Add 'sha' support
  * Support of the [RVA23 Profile](https://riscv.org/ecosystem-news/2025/04/risc-v-rva23-a-major-milestone/)
* s390x added support for generation 17 mainframe CPUs and virtio-mem
* s390x Control program identification data can now be retrieved via QOM
* x86 emulation got a performance boost handling string instructions
* x86 furthermore got more recent CPU types like ClearwaterForest
* `virtio-scsi` has gained true multiqueue support
* Support for Intel ® TDX included
* Support for starting a TDX or SEV-SNP virtual machine from an IGVM file.
* Support for VFIO on TDX and SNP virtual machines and many more vfio improvements.
* 32 bit hosts never could never provide the atomicity requirements of 64-bit guests. From 10.0, QEMU has disabled configuration of 64-bit guests on 32-bit hosts.

It is important to note that very old machine types have been deprecated for a while and now finally have been removed upstream and in Ubuntu.
* x86 dropped every type <= 2.5 which translates to anything <=xenial. That implies that you can migrate your older guests e.g. from trusty up to 24.04 LTS (Noble Numbat) or 25.04 (Plucky Puffin). The former giving another 4 + 5  +5 (basic, pro, legacy) years of support. But then after way more than a decade, guests would need to be [bumped to a newer machine type which is generally recommended regularly](https://documentation.ubuntu.com/server/explanation/virtualisation/upgrading-the-machine-type-of-your-vm/).
* On s390x the cleanup was a bit more aggressive - with <=4.1 and thereby <=eoan gone. This is a slightly shorter timeline, but still all the 5+5+5 years of support of an Ubuntu LTS plus the 4 years between focal and noble and thereby quite a long time until you need to consider updating your guest to a newer machine type.
* On ppc64 no Ubuntu related machine type was dropped yet, on arm we didn't yet need to introduce them.

For more details, please see related upstream changelogs and the general log on removed features:
* [10.0 Changelog](https://wiki.qemu.org/ChangeLog/10.0)
* [Removed Features](https://qemu-project.gitlab.io/qemu/about/removed-features.html)

#### Samba

Samba has been updated to the new upstream 4.22 version.

New features:
- SMB3 Directory Leases
- Netlogon Ping over LDAP and LDAPS
- Experimental Himmelblaud Authentication in Samba
- AD DC schema upgrade and provision performance improvements

Removed features:
- `nmbd proxy logon`
- `cldap port`
- `fruit:posix_rename`

Please refer to the upstream release notes for details: https://www.samba.org/samba/history/samba-4.22.0.html


#### Strongswan
Strongswan was upgraded to v6.0.1, following upstream in **dropping the NTRU post-quantum encryption algorithm**. See upstream changelogs for the full listing of changes:
* https://github.com/strongswan/strongswan/releases/tag/5.9.14
* https://github.com/strongswan/strongswan/releases/tag/6.0.0
* https://github.com/strongswan/strongswan/releases/tag/6.0.1

#### Intel® QuickAssist Technology (Intel® QAT)

Intel® QAT components have been updated to their most recent versions. Those are:

* qatlib : 25.08.0
For more information, visit the project’s[ repo](https://github.com/intel/qatlib?tab=readme-ov-file#features).
* qatengine : updated to 2.0.0
For more information, visit the project’s[ repo](https://github.com/intel/QAT_Engine/blob/master/docs/features.md).
* qatzip : updated to 1.3.1
For more information, visit the project’s[ repo](https://github.com/intel/QATzip?tab=readme-ov-file#features).

#### sos (sosreport)

`sos` was updated to version 4.10.0. Key updates below

* The temporary directory has now been changed from `/tmp` to `/var/tmp`. This follows changed in systemd-tmpfiles and the cleaning of `/var/tmp`, this aligns with other distros.
* `sos clean` now cleans the sos concurrently, improving the speed of cleaning.
*  Many new additional plugins include `authd`, `charmed_mysql`, `helm`, `opensearch`, `pulseaudio` and `valkey`
* Many other plugins have also been updated.

Upstream release notes can be viewed on the [sos project GitHub](https://github.com/sosreport/sos/releases/tag/4.10.0)

#### Subiquity

Please see the [25.10 Release Notes](https://github.com/canonical/subiquity/releases/tag/25.10) post on GitHub.

#### Valkey

Valkey was updated to version 8.1, starting with 8.1.1. This includes additional significant performance and efficiency improvements, without any backwards-incompatible changes to commands and responses. For more information on the new version, see the [Valkey 8.1 blog post ](https://valkey.io/blog/valkey-8-1-0-ga/). Release notes are available on the [Valkey project GitHub ](https://github.com/valkey-io/valkey/releases/tag/8.1.1).

Additionally, now that Redis has been updated to 8.0, **Valkey no longer acts as a drop-in replacement**. Therefore, the valkey-redis-compat package has been removed. If you are planning to swap from Redis to Valkey, **make sure to do so prior to upgrading**.

### OpenStack

OpenStack has been updated to the [2025.2 (Flamingo) ](https://releases.openstack.org/flamingo/) release. This includes packages for Aodh, Barbican, Ceilometer, Cinder, Designate, Glance, Heat, Horizon, Ironic, Keystone, Magnum, Manila, Masakari, Mistral, Neutron, Nova, Octavia, Swift, Vitrage, Watcher and Zaqar.

This release is also provided for Ubuntu 24.04 LTS via the Ubuntu Cloud Archive.

The Flamingo release significantly strengthens OpenStack's security posture with new confidential computing features in Nova (SEV-ES support, one-time passthrough devices), credential rotation capabilities in Magnum, and bring-your-own encryption keys in Manila. The Eventlet Removal is still underway, already being removed across multiple core services including Ironic, Barbican, Heat, modernizing OpenStack's asynchronous operations foundation for long-term sustainability.

#### Ceph

#### Open vSwitch (OVS) and Open Virtual Network (OVN)
OVS was updated to 3.6.0 and OVN was updated 25.09.0. Please refer to the upstream NEWS files  for more information about individual features:
* [OVS 3.6.0](https://github.com/openvswitch/ovs/blob/v3.6.0/NEWS)
* [OVN 25.09.0](https://github.com/ovn-org/ovn/blob/v25.09.0/NEWS)

### Platforms

#### GRUB2

We’ve started shipping a pre-release beta of GRUB 2.14 as the bootloader. Everything should work smoothly, but if you notice anything strange, please file a bug report and let us know!

#### Public Cloud / Cloud images

##### Microsoft Azure

Ubuntu images on Microsoft Azure now include azure-vm-utils package, which provides consistent disk naming across SCSI and NVMe devices, improved handling for accelerated networking (MANA and Mellanox), and removes the need for custom udev or Netplan configurations.

###### How to report any issues resulting from these changes

#### Raspberry Pi 🍓

* A new layout of the boot partition is introduced to enhance the reliability of the boot process ([LP: #2116266](https://launchpad.net/bugs/2116266)). This will automatically "test" new boot assets written to the boot partition before committing them as the current "known good" set. See the [call for testing](https://discourse.ubuntu.com/t/call-for-testing-a-b-boot-on-raspberry-pi/64173) for more information, or [the blog post](https://waldorf.waveform.org.uk/2025/pull-yourself-up-by-your-bootstraps.html) covering the feature for the full details (including advice on how to opt-out of this feature, where required)

* Please note that, due to the new boot process, the boot firmware on your Pi *must* be up to date. On the Pi 3, 3+, and Zero 2W, the boot firmware is in the image itself, and so is guaranteed to be up to date. On the Pi 5, all boot firmware since release are compatible. However, on the Pi 4 your boot firmware must be dated no earlier than 2022-11-25. To check this, run `sudo rpi-eeprom-update`. If your firmware is dated earlier than this, using Ubuntu 24.04 LTS (Noble Numbat) or later, run `sudo rpi-eeprom-update -a` and reboot.

* The Ubuntu desktop images for Raspberry Pi are now based upon the "desktop-minimal" seed rather than "desktop" ([LP: #2103808](https://launchpad.net/bugs/2103808)). This greatly reduces the default set of applications installed on the images (saving approximately 777MB of space on the uncompressed image, and thus on user's systems). The list of applications removed from the image is:

  - deja-dup (backup service)
  - file-roller (archive handler)
  - gnome-calendar
  - gnome-snapshot (camera application)
  - libreoffice-*
  - remmina (remote desktop client)
  - rhythmbox (music player)
  - shotwell (photo catalogue)
  - simple-scan (flat-bed scanner application)
  - thunderbird (email client)
  - totem (video player)
  - transmission-gtk (bittorrent client)

* The applications mentioned above will *not* be automatically removed for upgraders as the `ubuntu-desktop` meta-package remains manually installed in this circumstance. If you wish to remove these applications (in bulk), you may do so with: `sudo apt purge ubuntu-desktop --autoremove`. If you wish to keep specific applications, simply "install" them with apt first (which will mark them as "manually installed", excluding them from automatic removal).

* The creation of the swap-file on the desktop images is now handled by [cloud-init](https://cloudinit.readthedocs.io/en/latest/) ([LP: #2116275](https://launchpad.net/bugs/2116275)). You may customize the size of the swapfile by editing user-data on the boot partition prior to first boot

#### IBM Z and LinuxONE (s390x)

* With every new Ubuntu release, the s390-tools package got upgraded to it's latest available release v2.38 ([LP: #2115416](https://launchpad.net/bugs/2115416)), that now includes support to provide Topology-Map information to user-space ([LP: #2098361](https://launchpad.net/bugs/#2098361)), support to convert LUKS2 volume from AES keys to retrievable PAES keys ([LP: #2117450](https://launchpad.net/bugs/#2117450)) as well as Control Program Identification (CPI) hardening for SEL (Security Enhanced Linux) guests ([LP: #2118866](https://launchpad.net/bugs/#2118866)).

* Further support and enhancements were done in the virtualization stack with the implementation of virsh hypervisor-cpu-models in libvirt ([LP: #2027925](https://launchpad.net/bugs/#2027925), performance enhanced refresh PCI translation in qemu ([LP: #2049699](https://launchpad.net/bugs/#2049699)) and kernel ([LP: #2049700](https://launchpad.net/bugs/#2049700)), the implementation of Control Program Identification (CPI) in qemu ([LP: #2118769](https://launchpad.net/bugs/#2118769)) and the new reporting of vfio-ap configuration changes with CHSC Store Event Information in KVM, kernel ([LP: #2118771](https://launchpad.net/bugs/#2118771)) and qemu ([LP: #2119160](https://launchpad.net/bugs/#2119160)).

* Significant effort was spent to enable Ubuntu for the latest IBM Z (z17) and LinuxONE (LinuxONE 5) hardware generations, with support in glibc ([LP: #2117398](https://launchpad.net/bugs/#2117398)), and the tool-chain, namely:
  * gcc ([LP: #2117410](https://launchpad.net/bugs/#2117410))
  * llvm ([LP: #2117411](https://launchpad.net/bugs/#2117411)) and
  * valgrind ([LP: #2116735](https://launchpad.net/bugs/#2116735) and [LP: #2119288](https://launchpad.net/bugs/#2119288))

* Another big area of enhancements is cryptography:
  * with the upgrade to opencryptoki v3.25 ([LP: #2116720](https://launchpad.net/bugs/#2116720)) there is now also
  * support for ep11 token based import and export of secure key objects ([LP: #2117436](https://launchpad.net/bugs/#2117436))
  * the new tools p11kmip that allows to import/export PKCS #11 keys from to a KMIP server ([LP: #2117449](https://launchpad.net/bugs/#2117449))
  * and basic support for AES-GCM in CCA tokens ([LP: #2117451](https://launchpad.net/bugs/#2117451))
In addition several cryptography packages were updated, like:
  * openssl-ibmca to v2.5.0 ([LP: #2116709](https://launchpad.net/bugs/#2116709))
  * openssl-pkcs11-sign-provider to v1.0.2 ([LP: #2116721](https://launchpad.net/bugs/#2116721))
  * libzpc to v1.4.0 ([LP: #2116711](https://launchpad.net/bugs/#2116711))
  * libica4 to v4.4.1 ([LP: #2116716](https://launchpad.net/bugs/#2116716)) and 
  * cryptsetup to v2.8.0 ([LP: #2116736](https://launchpad.net/bugs/#2116736))
* The kernel also comes with new PHMAC support for MSA 11 HMAC ([LP: #2096891](https://launchpad.net/bugs/#2096891)).

* Finally further tools were updated, like the
  * smc-tools to v1.8.5, used for shared memory communication cards ([LP: #2119285](https://launchpad.net/bugs/#2119285))
  * libzdnn to v1.1.2, for neuronal network usage with IBM Z hardware support ([LP: #2116713](https://launchpad.net/bugs/#2116713)) and the
  * qclib to v2.5.1, that allows to query s390x hardware data ([LP: #2116708](https://launchpad.net/bugs/#2116708))

#### IBM POWER (ppc64el)

#### RISC-V

Ubuntu 25.10 targets the RVA23S64 ISA profile. Systems that don't satisfy this requirement cannot run Ubuntu 25.10. RVA20 hardware will continue to be supported by Ubuntu 24.04 LTS.

If you’d like to try it out in a VM, please refer to this guide https://canonical-ubuntu-boards.readthedocs-hosted.com/en/latest/how-to/qemu-riscv/

(25-10-known-issues)=
## Known Issues

As is to be expected with any release, there are some significant known bugs that users may encounter with this release of Ubuntu. The ones we know about at this point (and some of the workarounds) are documented here, so you don't need to spend time reporting these bugs again:

### General

* Offline installs ticking the box for Nvidia drivers result in Nouveau drivers being installed instead - to work around, install online or update drivers after install.  ([LP: #2127099](https://bugs.launchpad.net/ubuntu/+source/nvidia-graphics-drivers-580/+bug/2127099))
* There is a bug ([LP: #2104316](https://bugs.launchpad.net/ubuntu-power-systems/+bug/2104297)) in the *beta* images that prevents netboot installs in some scenarios.
* It has been reported that cloud-init may fails to upgrade properly in the Oracular to Pluck upgrade path, see [LP: #2104316](https://bugs.launchpad.net/ubuntu-power-systems/+bug/2104297).
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

    6. Finally, make the change take effect:

        ```
        sudo update-grub
        ```
* flatpak is failing to install applications due to missing or incorrect AppArmor rules in the profile for fusermount3. Please see https://bugs.launchpad.net/ubuntu-release-notes/+bug/2122161 for details.

### Linux kernel

* There is an AppArmor issue where confined profiles may unexpectedly seem to apply to another process and restrict things like "`<tool> > output.log`" from working inside questing LXD containers. See https://bugs.launchpad.net/ubuntu-release-notes/+bug/2121552 for more details.

### Ubuntu Desktop

* Screen reader support is present with the new desktop installer, but is incomplete ([LP: #2061015](https://launchpad.net/bugs/2061015), [LP: #2061018](https://launchpad.net/bugs/2061018), [LP: #2036962](https://launchpad.net/bugs/2036962), [LP: #2061021](https://launchpad.net/bugs/2061021))

* You will perhaps experience crashes trying to use the snap-store on Qualcomm Snapdragon X Elite hardware ([LP: #2127161](https://bugs.launchpad.net/ubuntu/+source/mesa/+bug/2127161))

* OEM installs are not supported yet ([LP: #2048473](https://launchpad.net/bugs/2048473))

* GTK4 apps (including the desktop wallpaper) do not display correctly with VirtualBox or VMWare with 3D Acceleration ([LP: #2061118](https://launchpad.net/bugs/2061118)).

* **Incompatibility between TPM-backed Full Disk Encryption and Absolute:** TPM-backed Full Disk Encryption (FDE) has been introduced to enhance data security. However, it's important to note that this feature is incompatible with Absolute (formerly Computrace) security software. If Absolute is enabled on your system, the machine will not boot post-installation when TPM-backed FDE is also enabled. Therefore, disabling Absolute from the BIOS is recommended to avoid booting issues.
* **Hardware-Specific Kernel Module Requirements for TPM-backed Full Disk Encryption:** TPM-backed Full Disk Encryption (FDE) requires a specific kernel snap which may not include certain kernel modules necessary for some hardware functionalities. A notable example is the `vmd` module required for NVMe RAID configurations. In scenarios where such specific kernel modules are indispensable, the hardware feature may need to be disabled in the BIOS (such as RAID) to ensure the continued availability of the affected hardware post-installation. If disabling in the BIOS is not an option, the related hardware will not be available post-installation with TPM-backed FDE enabled.
* [FDE specific bug reports](https://bugs.launchpad.net/bugs/+bugs?field.searchtext=&orderby=-importance&field.status%3Alist=NEW&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.tag=fde&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search).

* Installing `ubuntu-fonts-classic` results in a non-Ubuntu font being displayed ([LP#2083683](https://bugs.launchpad.net/bugs/2083683)). To resolve this, install `gnome-tweaks` and set ‘Interface Text’ to ‘Ubuntu’.

* Wayland desktop performance using the Nvidia driver is still suboptimal. Work is underway to resolve this in 26.04 ([LP#2081140](https://bugs.launchpad.net/bugs/2081140)).

* There is no simple way to customize the login screen ([upstream issue](https://gitlab.gnome.org/GNOME/gnome-control-center/-/issues/2185)). As a workaround, you can copy your personal monitor settings to the login screen with:
  ```
  sudo cp ~/.config/monitors.xml /var/lib/gdm3/seat0/config/
  ```
  and (at your own risk) you can copy all your other personal settings to the login screen with:
  ```
  sudo cp ~/.config/dconf/user /var/lib/gdm3/seat0/config/dconf/
  ```

### Ubuntu Server

#### rabbitmq-server

Certain version hops may be unsupported due to feature flags, raising questions about how Ubuntu will maintain this package moving forward. We are currently exploring the use of snaps as a potential solution to enable smoother upgrades. For more information please read [LP: #2074309](https://launchpad.net/bugs/2074309).

#### Openstack

Currently, Nova Compute is non-functional because of a python3.13 incompatibility ([LP:#2103413](https://bugs.launchpad.net/ubuntu/+source/nova/+bug/2103413)).
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

* Installing to a remote NVMe drive using NVMe over TCP firmware support can result in an unbootable system. A workaround exists using an autoinstall directive. Alternatively, the configuration on the target system can be manually fixed post installation before rebooting to the target system. More information at [LP: #2127072](https://bugs.launchpad.net/bugs/2127072).

#### Raspberry Pi

* The new gnome-initial-setup has issues preventing it from working properly:
  - Time zone input dropdown can "wobble" ([LP: #2084611](https://launchpad.net/bugs/2084611))
  - The hostname change is mandatory ([LP: #2093132](https://launchpad.net/bugs/2093132))

* During boot on the server image, if your `cloud-init` configuration (in `user-data` on the boot partition) relies upon networking (importing SSH keys, installing packages, etc.) you *must* ensure that at least one network interface is required (`optional: false`) in `network-config` on the boot partition. This is due to netplan changes to the wait-online service (~~[LP: #2060311](https://launchpad.net/bugs/2060311)~~)

* The seeded totem video player will not prompt users to install missing codecs when attempting to play a video requiring them ([LP: #2060730](https://launchpad.net/bugs/2060730))

* With the removal of the `crda` package in 22.04, the method of setting the wifi regulatory domain (editing `/etc/default/crda`) no longer operates. On server images, use the `regulatory-domain` option in the Netplan configuration. On desktop images, append `cfg80211.ieee80211_regdom=GB` (substituting `GB` for the relevant country code) to the kernel command line in the `cmdline.txt` file on the boot partition  ([LP: #1951586](https://launchpad.net/bugs/1951586)).

* The power LED on the Raspberry Pi 2B, 3B, 3A+, 3B+, and Zero 2W currently goes off and stays off once the Ubuntu kernel starts booting ([LP: #2060942](https://launchpad.net/bugs/2060942))

* Colours appear incorrectly in the Ubuntu App Centre ([LP: #2076919](https://launchpad.net/bugs/2076919))

* On server images, re-authentication to WiFi APs when regulatory domain is set result in `dmesg` spam to the console ([LP: #2063365](https://launchpad.net/bugs/2063365))

* On the Pi Zero 2W, the release image contains a bug in the Bluetooth components of the firmware package. This is due to be fixed in an SRU ([LP: #2127041](https://launchpad.net/bugs/2127041))

#### Google Compute Platform

##### Google cloud's ssh-in-browser is broken in 25.10

[ssh-in-browser](https://cloud.google.com/compute/docs/ssh-in-browser) (i.e. the SSH button in the console GUI) does not work in Questing 25.10. This is because the capability relies on older `ssh` algorithms (`diffie-hellman-group-exchange-sha256` and `diffie-hellman-group14-sha1`) which have now been deprecated in 25.10 ([LP: #2127982](https://bugs.launchpad.net/cloud-images/+bug/2127982)).

#### Microsoft Azure

* When inspecting system logs with journalctl, users may encounter a denied log entry relating to systemd-detect-virt. There is no known impact on functionality (LP:#[2124958](https://bugs.launchpad.net/ubuntu/+source/apparmor/+bug/2124958)).


#### AWS

Nothing yet.

#### s390X

* During upgrade from Ubuntu Server 25.04 (Plucky Puffin) to Ubuntu 25.10 (Questing Quokka) one may notice the following error with kdump-tools:

    ```text
    Errors were encountered while processing:
    kdump-tools
    ```

    This is likely due to a race condition.

    One may proceed and complete the upgrade, but at the end of the process the system needs to be manually rebooted. The bug is tracked here: [LP: #2126934](https://launchpad.net/bugs/2126934)

(25-10-official-flavors)=
## Official flavors

Find the release notes for the official flavors at the following links:

* [Edubuntu Release Notes](https://discourse.ubuntu.com/t/edubuntu-25-10-released/)
* [Kubuntu Release Notes](https://wiki.ubuntu.com/QuestingQuokka/ReleaseNotes/Kubuntu)
* [Lubuntu Release Notes](https://lubuntu.me/lubuntu-25-10-questing-quokka-released/)
* [Ubuntu Budgie Release Notes](https://ubuntubudgie.org/2025/10/ubuntu-budgie-25-10-release-notes/)
* [Ubuntu MATE Release Notes](https://ubuntu-mate.org/blog/ubuntu-mate-p-p-release-notes/)
* [Ubuntu Studio Release Notes](https://discourse.ubuntu.com/t/ubuntu-studio-25-10-release-notes/)
* [Ubuntu Unity Release Notes](https://ubuntuunity.org/posts/ubuntu-unity-2504-released/)
* [Xubuntu Release Notes](https://wiki.xubuntu.org/releases/25.10/release-notes)
* [Ubuntu Kylin Release Notes](https://ubuntukylin.com/news/ubuntukylin2510-en.html)
* [Ubuntu Cinnamon Release Notes](https://ubuntucinnamon.org/?p=1406)

(25-10-more-information)=
## More information

Refer to {ref}`release-policy-and-schedule` and {ref}`project-and-community`.
