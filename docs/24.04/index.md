---
tocdepth: 3
---

(ubuntu-24.04-lts-release-notes)=
# Ubuntu 24.04 LTS release notes

These release notes for **Ubuntu 24.04 LTS** (Noble Numbat) provide an overview of the release and document the known issues with Ubuntu and its flavors.

For details of the changes applied since 24.04, refer to the following changelogs:

:::{toctree}
:maxdepth: 1

24.04.4 <4>
24.04.3 <3>
24.04.2 <2>
24.04.1 <1>
:::

For the release schedule of Ubuntu 24.04 LTS and its point releases, refer to:

:::{toctree}
:maxdepth: 1

Release schedule <schedule>
:::

## Support lifespan

Ubuntu 24.04 LTS will be security maintained for 5 years until 31 May 2029. Users can choose to extend this to 10 years with [Ubuntu Pro](https://ubuntu.com/pro) or 12 years with the [Legacy add-on](https://ubuntu.com/blog/canonical-expands-long-term-support-to-12-years-starting-with-ubuntu-14-04-lts). 

## Upgrades

Users of Ubuntu 23.10 have been offered an automatic upgrade to 24.04 since shortly after the release. Users of 22.04 LTS will also start being offered the automatic upgrade now that 24.04.1 LTS has been released.


## Changes since 22.04 LTS

If you’re upgrading from Ubuntu 22.04 LTS to 24.04 LTS, you get all the changes that happened in the six months since Ubuntu 23.10, as well as the changes in all the interim releases between 22.04 LTS and 24.04 LTS.

For details, see the complete interim release notes: [22.10](https://discourse.ubuntu.com/t/kinetic-kudu-release-notes/27976), [23.04](https://discourse.ubuntu.com/t/lunar-lobster-release-notes/31910) and [23.10](https://discourse.ubuntu.com/t/mantic-minotaur-release-notes/35534). Finally, review the following changes since Ubuntu 23.10.


(24-04-new-features-in-24-04-lts)=
## New features in 24.04 LTS

### Year 2038 support for the armhf architecture

Ubuntu 24.04 LTS solves the [Year 2038 problem](https://en.wikipedia.org/wiki/Year_2038_problem) that existed on armhf. More than a thousand packages have been updated to handle time using a 64-bit value rather than a 32-bit one, making it possible to handle times up to 292 billion years in the future.

### Updated Packages

### Linux kernel 🐧

Ubuntu 24.04 LTS includes the new 6.8 Linux kernel that brings many new features.

Detailed changes are reported in the [Noble Kernel Release Notes](https://discourse.ubuntu.com/t/introducing-kernel-6-8-for-the-24-04-noble-numbat-release) post.

### systemd v255.4

The init system was updated to systemd v255.4. See the [upstream changelog](https://github.com/systemd/systemd/releases/tag/v255) for more information about individual features.

### Netplan v1.0 🌐 

The network stack was updated to [Netplan version 1.0](https://github.com/canonical/netplan/releases/tag/1.0). Supporting simultaneous WPA2 & WPA3, Mellanox VF-LAG for high-performance SR-IOV networking and VXLAN improvements. It also provides a [stable libnetplan1 API](https://netplan.readthedocs.io/en/stable/apidoc/) and a new `netplan status --diff` sub-command to find differences between configuration and system state. For more information please see the [Introducing Netplan v1.0](https://ubuntu.com/blog/introducing-netplan-v1) blog post.

### Toolchain Upgrades 🛠️

* GCC 🐄 is updated to the 14, binutils to 2.42, and glibc to 2.39.
* Python 🐍 now defaults to version 3.12
* OpenJDK ☕ now defaults to LTS version 21
* LLVM 🐉 now defaults to version 18
* Rust 🦀 toolchain defaults to version 1.75
* Golang 🐀 is updated to 1.22
* .NET 8 is now default

#### OpenJDK

OpenJDK LTS 21 is the default in Ubuntu 24.04 LTS while maintaining support for versions 17, 11, and 8. OpenJDK 17 and 21 are also TCK certified, which means they adhere to Java standards and ensure interoperability with other Java platforms. A special FIPS-compliant OpenJDK 11 package is also available for Ubuntu Pro users.

#### .NET

With the introduction of .NET 8, Ubuntu is taking a significant step forward in supporting the .NET community. .NET 8 will be fully supported on Ubuntu 24.04 LTS and 22.04 LTS for the entire lifecycle of both releases. This enables developers to upgrade their applications to newer .NET versions before upgrading their Ubuntu release. Starting with 24.04 LTS the .NET support has also been extended to the IBM System Z platform.

.NET 6 and .NET 7 packages with limited support are available via a [PPA](https://launchpad.net/~dotnet/+archive/ubuntu/backports).

#### Apport

Apport added integration with systemd-coredump to handle crashes. Developers on Ubuntu can co-install systemd-coredump now and use coredumpctl to analyze crash data. Apport will continue to collect crash information and submit it to the Ubuntu Error Tracker and Launchpad.

### Security Improvements 🔒

#### Unprivileged user namespace restrictions

In combination with the `apparmor` package, the Ubuntu kernel now restricts the use of unprivileged user namespaces. This affects all programs on the system that are unprivileged and unconfined. A default AppArmor profile is provided that allows the use of user namespaces for unprivileged and unconfined applications but will deny the subsequent use of any capabilities within the user namespace. A common use-case for unprivileged user namespaces is applications that construct their own sandboxes or work with styles of container workloads. As such, AppArmor profiles that allow the use of unprivileged user namespaces are also provided for common applications and frameworks that come from the Ubuntu archive, as well as popular third party applications like Google Chrome, Discord and others. This is a subsequent step towards trying to mitigate the larger attack surface presented by unprivileged user namespaces (the first being the introduction of this feature in Ubuntu 23.10 where it was not enabled by default).

Whilst significant effort has been expended to try and identify all applications that may require such profiles, it is expected that there may be cases where additional profiles are required.

In this case, there are several options if you run into problems:

  * Confine your applications with an AppArmor profile. Because this can be potentially onerous, a new `unconfined` profile mode/flag has been added to AppArmor. This designates the profile to essentially act like the unconfined mode for AppArmor where an application is not restricted, and it allows additional permissions to be added, such as the `userns,` permission. Such profile for, e.g. [Google Chrome](https://www.google.com/chrome/?platform=linux), would look like the following, and it would be located within the `/etc/apparmor.d/chrome` file:
    ```
    abi <abi/4.0>,

    include <tunables/global>

    /opt/google/chrome/chrome flags=(unconfined) {
      userns,

      # Site-specific additions and overrides. See local/README for details.
      include if exists <local/chrome>
    }
    ```
    Alternatively, a complete AppArmor profile for the application can be created (see the [AppArmor](https://ubuntu.com/server/docs/security-apparmor) documentation).

  * Launch your application in a way that doesn't use unprivileged user namespaces, e.g. `google-chrome-stable --no-sandbox`. However, since this disables the use of an internal security feature within the application, this is not recommended. Instead, use the `unconfined` profile mode described above instead.

  * Disable this restriction on the entire system for one boot by executing `echo 0 | sudo tee /proc/sys/kernel/apparmor_restrict_unprivileged_userns`. This setting is lost on reboot. This similar to the previous behaviour, but it does not mitigate against kernel exploits that abuse the unprivileged user namespaces feature.

  * Disable this restriction using a persistent setting by adding a new file (`/etc/sysctl.d/60-apparmor-namespace.conf`) with the following contents:
    ```
    kernel.apparmor_restrict_unprivileged_userns=0
    ```
    Reboot. This is similar to the previous behaviour, but it does not mitigate against kernel exploits that abuse the unprivileged user namespaces feature.

#### TLS 1.0, 1.1 and DTLS 1.0 are forcefully disabled

- for software using openssl this was the case since 20.04
- for software using gnutls, this is now enforced (with openconnect being a notable exception)

#### More consistent application of openssl and gnutls system configurations

Some libraries do not raise errors when their configuration is not accessible; this could happen when AppArmor does not allow access to the configuration files. Due to how widespread openssl and gnutls are, the AppArmor rules now grant access to their configuration files by default. Their system-wide configuration will therefore be followed better.

#### Deprecation and disablement of 1024-bit RSA APT repository signing keys

APT in 24.04 requires repositories to be signed with the RSA keys no smaller than 2048 bits, Ed25519, or Ed448. As work to resign old Launchpad PPAs with a stronger keys is still ongoing for some weeks, this is initially only a warning.

Once Launchpad PPAs have been resigned, you will need to manually migrate any affected PPAs to new signing keys by removing and re-adding them to quiesce the warning. 

The final APT 2.8.0 release that converts the warning to an error should be published as a stable release update some time after the resigning is complete.

#### pptpd removed

- [`pptpd` and `bcrelay` have been removed](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/2041751)

#### OpenSSH with reduced dependencies

As per the XZ-utils backdoor, `openssh` in Ubuntu does not depend anymore on libsystemd, reducing the number of dependencies and making it less prone to future security issues.

#### Package security-hardening improvements

Packages are now built with security-hardening features which stop many undiscovered security vulnerabilities, rendering them unexploitable.

The [gcc compiler](https://wiki.ubuntu.com/ToolChain/CompilerFlags) and dpkg now defaults to `-D_FORTIFY_SOURCE=3` instead of `-D_FORTIFY_SOURCE=2` which greatly increases buffer overflow detection and mitigation.

dpkg now defaults to use `-mbranch-protection=standard` which mitigates code reuse attacks on arm64.

### Performance ⚡

#### Performance Engineering tools
A set of performance engineering tools is installed by default on relevant Ubuntu systems. Additionally, a performance-tools metapackage has been created to assist in debugging performance and reliability issues. See [specification](https://discourse.ubuntu.com/t/spec-include-performance-tooling-in-ubuntu/43134) for more details.

### Default configuration changes ⚙️

As always there are many changes to defaults, mostly by newer versions of
packages. But a few are worth spelling out if your former automation,
configuration and tuning relied on those settings being one or the other way.

#### Apt priority of the proposed pocket

The proposed pocket is used as a staging area for software updates. These
updates land in the proposed pocket before they are released to the wider
public userbase.

But in the past, if someone enabled the proposed pocket for testing they often
got into trouble by getting their system flooded with everything that is in the
proposed pocket.
If just one of the packages in there was weirdly broken you'd have been broken
by that as well - and it might have been unrelated to what you really care about
and made your regular testing consume more effort and thereby less attractive.

By changing the default priority, users are less likely to install potentially
unstable updates unintentionally. Therefore the default apt priority of the
proposed pocket was reduced from 500 to 100. This change already happened in
Ubuntu Lunar, but Noble is the first Ubuntu LTS to pick it up and therefore
there is much more time of consumption from the proposed pocket in front of it.

With the change, users can now selectively install packages from the proposed
pocket. This allows for more conscious selection and testing of updates.
You can always see the new versions of the packages e.g. via `apt-cache policy`
but they will no more auto-install.
To install a package from proposed you'd now need to select from which pocket
you want to install like `apt install <package>/<release>-proposed`

The above helps a lot for the conscious testing of changes. But on the other
hand having automation and people testing (almost) all new package versions
regularly can provide great signal. Especially in canary setup with their very
own workload it can prevent breaking these specific setup unintentionally as
it might be different from what is tested elsewhere.

Therefore in those situations if you want to go back to the old behavior of
just getting everything from proposed all the time, you'd need to bump the apt
pin priority back up to 500 so the versions from the proposed pocket compete on
the same level with the rest of the Ubuntu Archive. To do that you could put
the following in a file like `/etc/apt/preferences.d/bump-proposed-prio`:

```
# Consider proposed all the time, set default priority 500
Package: *
Pin: release a=noble-proposed
Pin-Priority: 500
```

#### deb822 sources management

The sources configuration for Ubuntu has moved from `/etc/apt/sources.list` to `/etc/apt/sources.list.d/ubuntu.sources` in the more featureful deb822 format, aligning with PPAs that already migrated to deb822 last year. See [the specification](https://discourse.ubuntu.com/t/spec-apt-deb822-sources-by-default/29333/19) for more details.

#### Services restart on unattended-upgrade

The `needrestart` package has been modified to systematically restart services
if affected by a library upgrade, including in non-interactive scenarios such
as `unattended-upgrade`. The reason for this change is that
`unattended-upgrade` defaults to security updates only, and failing to
restarting services means that those running daemons will still be exposed to
the security issues fixed by the update.

It is possible to exclude specific services from automatic restart by adding
them to the `override_rc` section of `/etc/needrestart/needrestart.conf`.

See [this Discourse post](https://discourse.ubuntu.com/t/needrestart-changes-in-ubuntu-24-04-service-restarts/44671/1) for more details.

#### irqbalance no more installed and enabled by default

The `irqbalance` service is designed to distribute hardware interrupts across
processors on a multiprocessor system to increase performance. This is
particularly useful in server configurations where multiple devices will be
competing for the CPU’s attention. And in doing so it has served Ubuntu well
being default enabled since 14 years based on [a discussion](https://lists.ubuntu.com/archives/ubuntu-devel/2010-January/029939.html) and related to
the [kernel actively delegating this to userspace](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=8b8e8c1bf7275eca859fe551dfa484134eaf013b).

But evolution of the wider ecosystem has outpaced irqbalance in most situations.
`Irqbalance` can still be useful, but unless the admin configures it, the policy
it provides is not a discernible improvement over the in-kernel default policy.

At the same time a few cases have been reported where `irqbalance` causes issues,
[hence discussions have been ongoing for quite a while](https://bugs.launchpad.net/ubuntu/+source/ubuntu-meta/+bug/1833322). It does usually not make
as much sense for virtual guests, it might conflict with manual tuning and other
power consumption or latency targets. Furthermore the kernel and in particular many device
drivers evolved since then and often do an equal or better job now.

This change is just not installing it by default, `irqbalance` will stay available and
anyone that benefits or even just want to experiment with it can use it as
before.

Some specific scenarios, like particular cloud images, already had `irqbalance`
disabled by default before. In a similar fashion some have been (and more might
be) identified which will keep it enabled by default as there has been evidence
that on this platform it is more helpful.

### tzdata package split

The tzdata package was split into tzdata, tzdata-icu, and tzdata-legacy. The tzdata package ships only timezones that follow the current rules of geographical region (continent or ocean) and city name. All legacy timezone symlinks (old or merged timezones mentioned in the upstream backward file) were moved to tzdata-legacy. This includes the US/* timezones.

Please install tzdata-legacy in case you need the legacy timezones or to restore the previous behavior. This might be needed in case the system provides timezone-aware data over the network (e. g. SQL databases).

### Ubuntu Desktop

#### Installer and Upgrades

* We've taken the first steps towards a more general "provisioning" approach that encompasses a "device bootstrap" stage followed by a "first boot initialization" and a "desktop welcome" step.
  * This means the ubuntu-desktop-installer is now part of the larger ubuntu-desktop-provision project and has been renamed to ubuntu-desktop-bootstrap.
  * It comes with an improved UI design that is customizable via a central configuration file. Default image assets automatically follow the customized accent color, or can be swapped out entirely according to the needs of flavors or OEM providers.

* In order to enable advanced users to benefit from subiuity's/cloud-init's autoinstall capabilities, we've added a dedicated page that allows side-loading an autoinstall.yaml from a network URL during the installation.

* We are reintroducing support for **ZFS guided installations**, enhancing the flexibility and choices available for your storage management needs. This is a new implementation in the Subiquity-based installers, and is without encryption by default. The encrypted ZFS guided option will be developed in a future release.

* Starting with Ubuntu 23.10, **TPM-backed full-disk encryption** (FDE) is introduced as an experimental feature, building on years of experience with Ubuntu Core. On supported platforms, you no longer need to enter passphrases at boot manually. Instead, the TPM securely manages the decryption key, providing enhanced security against physical attacks. This new feature streamlines the user experience and offers additional layers of security, especially in enterprise environments. However, the traditional passphrase-backed FDE is still available for those who prefer it. We invite users to experiment with this new feature, although caution is advised as it's still experimental. More details in the [TPM-backed Full Disk Encryption is coming to Ubuntu](https://ubuntu.com/blog/tpm-backed-full-disk-encryption-is-coming-to-ubuntu) blog post. Do not hesitate to [report bugs in Launchpad against the ubuntu-desktop-provision project](https://bugs.launchpad.net/ubuntu-desktop-provision/+filebug).

  Known limitations:

  * Requires TPM 2.0.
  * Only a limited set of hardware is supported.
  * No external kernel-modules support. For example, no support of NVIDIA graphics cards.
  * Firmware updates and upgrades to future releases of Ubuntu are not currently supported.

  Common issues:
  The 2 most common bugs experienced by users when testing the experimental TPM backed FDE option are:

  * The installation fails to complete and logs contain an error message that references an operation not being able to complete successfully because of "DA lockout mode". In this case, the TPM must be cleared using one of two mechanisms. Note that this will result in the loss of all keys previously protected by this TPM, such as Windows BitLocker keys.

      * Reboot into the firmware settings UI and select the option to clear the TPM. The experience of this will differ between vendors.
    * Request that the firmware clear the TPM on the next reboot from userspace by running "echo 5 | sudo tee /sys/class/tpm/tpm0/ppi/request > /dev/null" and then rebooting the device.

  * The installation completes, but the user is prompted for a recovery key on the first boot. Many modern laptops contain a piece of endpoint management software called Absolute that is built into the firmware and runs before the operating system loads. This currently causes us to mis-predict PCR values. The existing workaround is to disable Absolute, which can be done using one of two mechanisms.
    *  On Dell devices, Absolute can be disabled from userspace by running "echo DisableAbsolute | sudo tee /sys/devices/virtual/firmware-attributes/dell-wmi-sysman/attributes/Absolute/current_value > /dev/null" and then rebooting.
    * On other devices, it may be possible to disable Absolute from the firmware UI. The experience of this will differ between vendors.

  Future updates to the installer will provide additional tools to provide richer error messaging and support for these use-cases.

* The configuration file, `/etc/netplan/01-network-manager-all.yaml` (which specifies Network Manager as the Netplan renderer), has been moved to `/lib/netplan/00-network-manager-all.yaml` to reflect that it should not be edited. Also, it is now owned by the `ubuntu-settings` package. For upgraders, the move is be performed automatically and the old file removed if it was unchanged. If it was changed, the move still takes place, but a copy of the old file is left in `/etc/netplan/01-network-manager-all.yaml.dpkg-backup` ([LP: #2020110](https://bugs.launchpad.net/ubuntu/+source/ubuntu-settings/+bug/2020110)).

* **NetworkManager now uses Netplan** as its default settings-storage backend. On upgrade, all connection profiles from `/etc/NetworkManager/system-connections/` are transparently migrated to `/etc/netplan/90-NM-*.yaml` and become ephemeral, Netplan-rendered connection profiles in `/run/NetworkManager/system-connections/`. Backups of the original profiles are automatically created in `/var/lib/NetworkManager/backups/` (read more at [NetworkManager YAML settings backend](https://netplan.readthedocs.io/en/stable/netplan-everywhere) and [LP: #1985994](https://bugs.launchpad.net/netplan/+bug/1985994)).

* **ADSys Active Directory Certificates auto-enrollment:** Windows Server offers a solution for auto-enrolling certificates using Group Policies. This interacts with Certificate Enrollment Services by Microsoft and works seamlessly with Windows clients.

  ADSys introduces AD certificates auto-enrollment to streamline connecting to corporate Wi-Fi and VPN networks. Automated enrollment eliminates the need for manual interactions with the certificate authority, such as pre-creating certificates. This simplifies IT administration and minimises security risks associated with managing sensitive data.

* The **installer** is now able to update itself and will prompt the user to update in the very early stages of the installation if a newer version is available.

* **Power Profiles Manager** [has been improved and optimized](https://gitlab.freedesktop.org/upower/power-profiles-daemon/-/releases/#0.21) to support better newer hardware features (especially AMD), can now support multiple optimization drivers and is now battery-aware to automatically increase the optimization levels when running on battery only.

* **fprintd** has been updated and [**libfprint** supports now many other fingerprint drivers and devices](https://gitlab.freedesktop.org/libfprint/libfprint/-/releases#v1.94.7).

#### New Store

* There is a brand new **Ubuntu App Center** that replaces the previous Snap Store. The application has been written from scratch using the Flutter toolkit.
  * New since 23.10, a Games page has been added to the Ubuntu App Center

* There is also a new standalone **Firmware Updater** application available for both amd64 and arm64. This provides the possibility to update firmware without needing to have a full app store running continuously in the background.

#### GNOME 👣

* GNOME has been updated to include new features and fixes from the latest GNOME release, [GNOME 46](https://release.gnome.org/46/)

#### Default app changes

* The default Ubuntu Desktop installation is now **minimal**. There is still an “extended selection” option for those who prefer to have applications like LibreOffice and Thunderbird installed for the first boot.

* In the extended install, the webcam app is now provided by GNOME Snapshot instead of Cheese

* Games are no longer installed by default

#### Updated Ubuntu font

A more modern slimmer version of the Ubuntu font family is now shipped as standard. Anyone wishing to return to the older Ubuntu font used in 22.04 can do so by installing the `fonts-ubuntu-classic` package.

#### Updated Applications

* [Firefox](https://mozilla.org/firefox/releases/) 124 🔥🦊
  * Firefox is a native [Wayland application](https://discourse.ubuntu.com/t/firefox-snap-with-wayland-enabled-by-default-in-ubuntu-23-10-mantic-minotaur/38660) for this Ubuntu release
* [LibreOffice 24.2](https://wiki.documentfoundation.org/ReleaseNotes/24.2) 📚
* [Thunderbird 115 "Supernova"](https://blog.thunderbird.net/2023/07/our-fastest-most-beautiful-release-ever-thunderbird-XY-supernova-is-here/) 🌩️🐦
  * Thunderbird is now provided as a Snap package only

#### Updated Subsystems

* [BlueZ 5.72](https://git.kernel.org/pub/scm/bluetooth/bluez.git/tree/ChangeLog?id=5.72)
* [Cairo 1.18](https://cairographics.org/news/cairo-1.18.0/)
* [NetworkManager 1.46](https://gitlab.freedesktop.org/NetworkManager/NetworkManager/-/blob/nm-1-46/NEWS)
* [Pipewire 1.0.4](https://gitlab.freedesktop.org/pipewire/pipewire/-/blob/1.0.4/NEWS)
* [Poppler 24.02](https://gitlab.freedesktop.org/poppler/poppler/-/blob/poppler-24.02.0/NEWS)
* [xdg-desktop-portal 1.18](https://github.com/flatpak/xdg-desktop-portal/blob/1.18.2/NEWS)

### Ubuntu WSL

#### Cloud-init support

`cloud-init`  is the *industry standard* multi-distribution method for cross-platform cloud instance initialisation. It is supported across all major public cloud providers, provisioning systems for private cloud infrastructure, and bare-metal installations.

With `cloud-init` on WSL you can now automatically and reproducibly configure your WSL instances on first boot. Make the first steps with [this tutorial](https://canonical-ubuntu-wsl.readthedocs-hosted.com/en/latest/tutorials/cloud-init/).

#### New documentation

The documentation specific to [Ubuntu on WSL is available on Read the Docs](https://canonical-ubuntu-wsl.readthedocs-hosted.com/en/latest/). This evolving project is regularly updated with new content about Ubuntu's specifics on WSL.

#### Enhancements 

* **Reduced footprint**
Experience faster download and installation times with 24.04, with a 200MB reduction in image size.

* **systemd by default everywhere**
`systemd` is now enabled by default even when the instance is launched directly from a terminal with the `wsl.exe` command or from an imported root files system.

### Ubuntu Server

#### Apache2

The Apache2 package has been updated to version 2.4.58.  Here are the
major changes since Ubuntu Jammy:

* mod_http2 has a partial rewrite of how connections and streams are handled. APR pollset and pipes do the monitoring instead of stuttered timed waits. Resource handling for misbehaving clients is improved. It also gains new directives `H2ProxyRequests`, `H2MaxDataFrameLen`, `H2WebSockets` and `H2EarlyHint`.
* Add an auto status to mod_md using a format similar to mod_proxy_balancer, and supports managing certificates via the tailscale secure networking service.
* mod_md fixes certificate renewal issues in certain situations, and gains a new directive `MDCertificateAuthority` for failover of renewals, along with configurational directives `MDRetryDelay` and `MDRetryFailover` to control its behavior.
* mod_md also gains new directives MDMatchNames and MDChallengeDns01Version to give more configurational control over MDomains and challenges.
* Support for managing mod_md configurations via local tailscale daemon
* Support pcre2 (10.x) library in place of the now end-of-life pcre (8.x) for regular expression evaluation.
* mod_proxy gains various backend refinements and fixes, including detecting AJP/CPING support correctly now.
* MPM event fix issues during restart and idle maintenance.
* Add the BCTLS and BNE RewriteRule flags to mod_rewrite and fixes   security issues and several bugs.

More information on the changes in Apache2 2.4.53 through 2.4.58, now included in Ubuntu can be found at: https://www.apachelounge.com/changelog-2.4.html


#### Clamav

The clamav anti-virus toolkit saw a 1.0.0 release between Ubuntu 22.04 LTS and now.  Some of the major changes since Ubuntu Jammy include:
* Support for decrypting read-only OLE2-based XLS files that are encrypted with the default password.
* Overhauled the implementation of the all-match feature. The newer code
* Added a new callback, cl_engine_set_clcb_file_inspection(), for inspecting file content during a scan at each layer of archive extraction.
* Added a new API function unpacking CVD signature archives, cl_cvdunpack().

The full list of changes for the ClamAV 1.0.0 LTS release can be found at https://blog.clamav.net/2022/11/clamav-100-lts-released.html.  For details on subsequent bugfix releases in the 1.0 branch, including 1.0.5, see Clamav's blog at https://blog.clamav.net/.


#### Chrony

Chrony is updated to 4.5, which adds support for systemd socket activation, multiple refclocks on one PHC, corrections from PTP transparent clocks, AES-GCM-SIV in GnuTLS, and AES-GCM-SIV with Nettle >= 3.9 to shorten NTScookies to avoid some length-specific blocking of NTP.  DSCP is set for IPv6 packets.  New options include maxpoll for the hwtimestamp directive to improve PHC tracking with low packet rates, maxdelayquant for adding long-term quantile-based filtering to the server/pool/peer directive, and a local option to the refclock directive to stabilise system clock with more stable free-running clock (e.g. TCXO, OCXO).  A new hwtstimeout directive has been added to configure timeout for late timestamps, and a selectopts command to modify source-specific selection options.

More information about the 4.5 and other releases can be found at Chrony's news page, at https://chrony-project.org/news.html.

#### cloud-init v.24.1.3
Notable features:
- Windows Subsystem for Linux(WSL) datasource support
- azure: improved handling and retires of DHCP during pre-provisioning stage (PPS)
- ec2: support for multi-NIC/IP instances
- oracle: add resilience to early network issues
- network: dhcpcd support as primary DHCP client (successor to isc-dhclient)
- APT deb822 support for default sources
- cloud-init status improved recoverable_error(warning) visibility

Breaking changes:
- cloud-init status exist 2 on warnings and exits 1 on error.
- SSH dropped support for DSA host keys
- boot optimization: removed systemd ordering dependency on snapd.seeded
- stopped adding network v2 DNS to global DNS
- mandate use of a single datasource when specified in datasource_list

Features since Ubuntu Jammy: (details in [cloud-init's Github releases page](https://github.com/canonical/cloud-init/releases/))

- Clouds: added NWCS and Akamai(Linode)
- Config Modules: added ansible and wireguard modules, sodoers doas and opendoas support
- Ephemeral network IPv4/IPv6 dual-stack support setup, support ucdhcp client
- Netplan schema validation and config passthrough
- NetworkManager and networkd renderer support
- jinja template support of /etc/cloud/cloud.cfg.d
- cloud-init schema: validation of user-data, vendor-data and network-config
- cloud-init clean: /etc/machine-id support for golden images

#### Containerd

The containerd package was updated to version 1.7.12. It contains a bunch of bug fixes, adding support to newer Golang version, updating dependencies and so on. The two features below are new in this version since the last Ubuntu release:

- Add blockfile snapshotter.
- Add remote/proxy differ.

Some features were marked as deprecated, please try to not use them anymore. Deprecation warnings:

- Emit deprecation warning for `containerd.io/restart.logpath` label usage.
- Emit deprecation warning for AUFS snapshotter.
- Emit deprecation warning for v1 runtime.
- Emit deprecation warning for deprecated CRI configs.
- Emit deprecation warning for CRI v1alpha1 usage.
- Emit deprecation warning for CRIU config in CRI.

For more information, please see [the upstream changelog](https://github.com/containerd/containerd/releases).

#### Django

Django was updated to version 4.2.11, providing the latest LTS bug and security fixes. For more information see the upstream changelogs for [4.2.5](https://docs.djangoproject.com/en/4.2/releases/4.2.5/)-[4.2.11](https://docs.djangoproject.com/en/4.2/releases/4.2.11/).

#### Docker

The docker.io package was updated to version 24.0.7. It contains many bug fixes and dependencies update. Some highlights are the fix of data corruption with zstd output and many improvements to the containerd storage backend. For more information, please see [the upstream changelog](https://docs.docker.com/engine/release-notes/24.0/).

:::{note}
There is a AppArmor related bug where containers cannot be promptly stopped due to the recently added AppArmor profile for `runc`. The containers are always killed with `SIGKILL` due to the denials when trying to receive a signal. More details about this bug can be found [here](https://bugs.launchpad.net/ubuntu/+source/docker.io/+bug/2063099), and a workaround is described [here](https://bugs.launchpad.net/ubuntu/+source/docker.io/+bug/2063099/comments/4).
:::

#### Dovecot
Dovecot received several micro-point updates from 2.3.16 in Ubuntu Jammy, to 2.3.21 in this new LTS.

There is also a new dsync_features=no-header-hashes setting, which enables an optimization that assumes identical IMAP UIDs contain the same mail contents. This is useful on IMAP servers that don’t cache the Date/Message-ID headers.

* [New events](https://doc.dovecot.org/admin_manual/list_of_events/) are added.
* New Lua HTTP client settings and a new doveadm replicator status command.
* fts: [Don't index inline base64 encoded content](https://doc.dovecot.org/configuration_manual/fts/tokenization) in FTS indexes using the generic tokenizer. This reduces the FTS index sizes by removing input that is very unlikely to be searched for. Only applies when using libfts.
* stats: If metric has fields specified, all these fields are [exported as counters](https://doc.dovecot.org/configuration_manual/stats/openmetrics/.) to prometheus exposition.
* lua: [HTTP client has more settings](https://doc.dovecot.org/admin_manual/lua/#dovecot.http.client) now.  
* Added [mail_user_session_finished event](https://doc.dovecot.org/admin_manual/list_of_events/), which is emitted when the mail user session is finished (e.g. imap, pop3, lmtp). It also includes fields with some process statistics information.
* auth: Add [a cache hit indicator](https://doc.dovecot.org/admin_manual/list_of_events/) to auth passdb/userdb finished events.
* lib-lua: Add [a Lua interface](https://doc.dovecot.org/admin_manual/lua/) to Dovecot's HTTP client library.
* [Events now have a "reason_code" field](https://doc.dovecot.org/admin_manual/event_reasons/), which can provide a list of reasons why the event is happening.
* fts: Added [fts_header_excludes and fts_header_includes settings](https://doc.dovecot.org/settings/plugin/fts-plugin#plugin-fts-setting-fts-header-excludes) to specify which headers to index.

For more detailed information on the changes since Ubuntu Jammy, see Dovecot's release announcements for [2.3.17](https://dovecot.org/pipermail/dovecot-news/2021-October/000465.html), [2.3.18](https://dovecot.org/pipermail/dovecot-news/2021-December/000468.html), [2.3.19](https://dovecot.org/list/dovecot-news/2022-May/000473.html), [2.3.20](https://dovecot.org/pipermail/dovecot-news/2022-December/000479.html), and [2.3.21](https://dovecot.org/mailman3/archives/list/dovecot-news@dovecot.org/thread/KYDR7WWPEQOBZA3IA4NL5XDSLODZLG6N/).


#### Exim4

The exim4 mail transport agent was updated to version 4.97.  This brings numerous fixes to syntax parsing including ${run...}, ${if} and ${filter } constructions.  Query-style lookups are now checked for quoting; for now issues are just logged but will be treated as errors in a future release. An expansion operator for wrapping long header lines has been added.

Other notable changes include:

* Queue runners for several queues can now be started from one daemon.
* A new ACL condition: seen. Records/tests a timestamp against a key.
* Events on a failing SMTP AUTH, for both client and server operations, and for failing TLS connects to the daemon.
* Variable $sender_helo_verified with the result of an ACL "verify = helo".
* The smtp transport option "max_rcpt" is now expanded before use.
* The expansion-test facility (exim -be) can set variables.
* The "allow_insecure_tainted_data" main config option and the "taint" log_selector have been removed.  These were deprecated in the 4.95 release.

Please note that the default configuration (/etc/default/exim4) generated for fresh installations differs from past practices, and a number of settings (QFLAGS, QUEUEINTERVAL, COMMONOPTIONS, QUEUERUNNEROPTIONS and SMTPLISTENEROPTIONS) have been replaced.  As well, the `update-exim4defaults` script is no longer used for setting run parameters for the Exim daemon; users are encouraged to edit /etc/default/exim4 directly to customize.  Also, the internal (but exposed in logs, Received: headers and Message-ID: headers) identifier used for messages is longer than in the previous release.

For more information on the changes introduced in Exim4 4.96 and 4.97, please see the [Exim4 project's ChangeLog](https://github.com/Exim/exim/blob/master/doc/doc-txt/ChangeLog).

#### GlusterFS

The GlusterFS clustering filesystem package was updated to version [11.1](https://lists.gluster.org/pipermail/gluster-devel/2023-February/058414.html). Following this update, some changes were made to the packaging layout of GlusterFS and dependent packages:

 * GlusterFS upstream no longer supports 32 bit architectures (see [LP: #2052734](https://bugs.launchpad.net/ubuntu/+source/glusterfs/+bug/2052734)). Therefore, there are no armhf packages for GlusterFS in Ubuntu Noble. As a further consequence, other packages that linked or relied on GlusterFS also no longer have that support on the armhf architecture.
* GlusterFS has been demoted to Universe ([LP: #2045063](https://bugs.launchpad.net/ubuntu/+source/glusterfs/+bug/2045063)).
* Since there cannot be packages in Main depending on Universe, packages in main that had a dependency on GlusterFS were modified to ship that dependency also in Universe.

The following packages were changed:

* qemu: The binary `qemu-block-extra` package had a dependency on GlusterFS due to the gluster storage module it shipped. That module is now being shipped in the new `qemu-block-supplemental` binary package.

* samba: The binary `samba-vfs-modules` package had a dependency on GlusterFS due to a VFS module. All GlusterFS VFS modules were moved to the new `samba-vfs-modules-extra` package.

Note that since GlusterFS is no longer available for 32 bit architectures (see [LP: #2052734](https://bugs.launchpad.net/ubuntu/+source/glusterfs/+bug/2052734)), the two new packages mentioned above do not exist on armhf.

##### Upgrade considerations for qemu and samba
If you have a deployment of qemu or samba that used the glusterfs storage or VFS modules, then there are considerations to be made. In other words, if you:
* had `qemu-block-extra` installed, and were using the `block-gluster.so` module
* had `samba-vfs-modules` installed and were using either `glusterfs.so` or `glusterfs_fuse.so` VFS modules

Then the release upgrade to Ubuntu Noble will replace those packages with the new versions that DO NOT have the glusterfs modules. In such cases, you will have to install the new packages manually after the release upgrade is completed:
* `sudo apt install qemu-block-supplemental`, or
* `sudo apt install samba-vfs-modules-extra`

Considerations were made ([ubuntu-devel mailing list thread](https://lists.ubuntu.com/archives/ubuntu-devel/2024-January/042872.html)) to perhaps include this logic in the Ubuntu release upgrade tool, but it was decided to not increase the complexity of the upgrader at this time. If you have a different scenario where this will have a big impact on your deployments, then please comment on the [LP: #2045063](https://bugs.launchpad.net/ubuntu/+source/glusterfs/+bug/2045063) bug.


#### HAProxy

The [HAProxy](https://www.haproxy.org) package was updated to version 2.8.5. This new version includes several improvements and bug fixes. For more information, please see [the upstream changelog](https://www.haproxy.org/download/2.8/src/CHANGELOG).

#### Kea

The [Kea](https://www.isc.org/kea/) package was updated to version 2.4.1. This is now the supported DHCP server in Ubuntu, replacing ISC DHCP, which has been discontinued by ISC.

`keama` a new binary package to aid migrating ISC DHCP configuration files to Kea was also made available in noble.

Here are some of the major changes in Kea since Ubuntu Jammy.

* Native TLS support.
* PostgreSQL configuration backend.
* Support password-files to store HTTP API credentials.
* Multi-threading is now enabled by default.
* Affinity for released leases. Kea now keeps leases for a configurable period after they are released. This is useful for devices that send RELEASE when rebooting so they have more chances of obtaining the same lease when the reboot process is complete.

For more details, please see the upstream release notes for [version 2.4](https://downloads.isc.org/isc/kea/2.4.0/Kea-2.4.0-ReleaseNotes.txt) and for [version 2.2](https://downloads.isc.org/isc/kea/2.2.0/Kea-2.2.0-ReleaseNotes.txt)

#### libvirt

The [libvirt](https://libvirt.org) package was updated to version 10.0.0.  Here are the changes since Ubuntu Jammy.

* Support mode option for `dirtyrate` calculation.
* Improve domain save/restore throughput
* Introduce manual disk snapshot mode to coordinate outside libvirt.
* Introduce memory allocation threads (handy for guests with large amounts of memory).
* Introduce support for `virtio-iommu`.
* PPC64 Power10 processor support.
* Introduce absolute clock offset.
* Add support for post-copy migration recovery.
* qemu: Add support for zero-copy migration
* qemu: Add support for specifying vCPU physical address size in bits
* qemu: Add flags to keep or remove TPM state for virDomainUndefineFlags
* QEMU: Core Scheduling support (not enabled by default).
* External snapshot deletion.
* External backend for swtpm.
* Passing file descriptors instead of opening files for `<disk>`.
* Allow multiple nodes for preferred policy.
* Report Hyper-V Enlightenments in `domcapabilities`.
* Support for SGX EPC (enclave page cache).
* Support migration of vTPM state of QEMU VMs on shared storage.
* Introduce support for `igb` network interface model.
* Support compression for parallel migration.
* AppArmor: All profiles and abstractions now support local overrides
* Add Sapphire Rapids CPU model.
* Support removable attribute for SCSI disk.
* qemu: Change default machine type for ARM and RISC-V to 'virt'
* QEMU: Enable `postcopy-preempt` migration capability.
* QEMU: Add support for mapping iothreads to virtqueues of `virtio-blk` devices.
* QEMU: Allow automatic resize of block-device-backed disk to full size of the device.
* QEMU: Automatic selection/binding of VFIO variant drivers.
* qemu: Add support for vDPA block devices
* QEMU: Add runtime configuration option for nbdkit.
* QEMU: Add ID mapping support for `virtiofsd`.
* QEMU: Improve migration XML use when persisting VM on destination.
* QEMU: Simplify non-shared storage migration to raw block devices.
* QEMU: Allow `virtiofsd` to run unprivileged.
* The RBD/Ceph storage driver (`libvirt-daemon-driver-storage-rbd`) is now available only on 64-bit architectures.

For more details, please see [the upstream changelog](https://www.libvirt.org/news.html).

#### LXD

Keeping with the theme of further streamlining Ubuntu, starting with this release, LXD snap won’t be pre-installed in the Ubuntu server by default. Instead, we will be applying the same logic as with the ubuntu-minimal images, where we use a small script (`lxd-installer`) to install LXD on first use.

LXD 5.21.0 LTS has been released with a number of useful features and a few other operational changes. For more information, please read [the full release announcement](https://discourse.ubuntu.com/t/lxd-5-21-0-lts-has-been-released/42476/1).

#### Monitoring Plugins

Four micro-version release updates to monitor-plugins brings it to
version 2.3.5 in this Ubuntu LTS release, providing a number of fixes
and enhancements.  A few items of note:

* check_dhcp: Add dhcp rogue detection
* check_icmp: Add support to Jitter, MOS and Score
* check_smtp: Add support for SMTP over TLS
* check_smtp: Add support for SNI
* check_http: Implement chunked encoding decoding
* check_curl: detect ipv6
* check_by_ssh: Let ssh decide if a host is valid, enables usage of
  ssh .config file
* check_curl: Add an option to check_curl to verify the peer
  certificate & host using the system CA's
* check_fping: Implements 'host-alive' mode
* check_http: Support http redirect
* check_ping: understand ping6
* check_smtp: add -L flag to support LMTP (LHLO instead of
  HELO/EHLO).
* check_snmp: Added option for null zero length string exit codes

For more detail, see the release announcements for [2.3.2](https://www.monitoring-plugins.org/news/release-2-3-2.html), [2.3.3](https://www.monitoring-plugins.org/news/release-2-3-3.html), [2.3.4](https://www.monitoring-plugins.org/news/release-2-3-4.html), and [2.3.5](https://www.monitoring-plugins.org/news/release-2-3-5.html).


#### Net SNMP

The [Net SNMP](http://www.net-snmp.org/) package was updated to version 5.9.4.

In addition to a few security and stability fixes, support is now included for recognizing Docker's overlay filesystem such as when running `snmpwalk` against a Docker container.

For more details, please see [the upstream changelog](https://github.com/net-snmp/net-snmp/blob/v5.9.4/CHANGES).

#### Nginx

The Nginx web server has been updated to version 1.24 in Ubuntu 24.04 LTS, marking a major jump from version 1.18 in the previous LTS.  This brings OpenSSL 3.0 compatibility, support for the PCRE2 library, protocol TLSv1.3 enabled by default, Application-Layer Protocol Negotiation (ALPN) support for the stream module, Online Certificate Status Protocol (OCSP) validation of client SSL certificates, and improved HTTP/2 support among other things.

For a complete listing of changes, please see the release notices for Nginx [1.20](https://nginx.org/en/CHANGES-1.20), [1.22](https://nginx.org/en/CHANGES-1.22), and [1.24](https://nginx.org/en/CHANGES-1.24).


#### OpenLDAP

The [OpenLDAP ](https://openldap.org) package was updated to version 2.6.7, which brings several bug fixes. For more details, please see [the upstream changelog ](https://www.openldap.org/software/release/changes.html).

#### OpenVmTools

open-vm-tools moves to 12.3.5 in Ubuntu 24.04 LTS.  Intermediate versions resolved a few critical problems, vulnerabilities, and Coverity issues. In addition, it brings support for managing Salt Minion, and for gathering and publishing lists of containers running inside Linux guests.  A tools.conf configuration setting is also available to temporarily direct Linux quiesced snapshots to restore pre open-vm-tools 12.2.0 behavior of ignoring file systems already frozen.

The announcements for 12.3.5 and other releases since 11.3.5 can be found on the [open-vm-tools Github releases page](https://github.com/vmware/open-vm-tools/releases).

#### PAM

`pam_lastlog.so` has [been removed](https://bugs.launchpad.net/ubuntu/+source/shadow/+bug/2060676) because it was not Year 2038 compliant.

#### Percona Xtrabackup

Percona Xtrabackup has been added as a new package, working alongside MySQL 8.0.x. It is a tool for creating and restoring backups of MySQL databases while maintaining availability. For more information see Percona Xtrabackup's [upstream documentation](https://docs.percona.com/percona-xtrabackup/8.0/).

#### PHP

The [PHP](https://php.net) package was updated to version 8.3.6. Here are the major changes since Ubuntu Jammy.

* Upon updates, PHP will re-start apache2 to ensure any bugs in your PHP powered web server gets addressed as soon as an upgrade is performed.
* Read only classes
* Disjunctive Normal Form (DNF) types to allow the combination of union and intersection types
* `null`, `false`, and `true` are now allowed as stand-alone types
* A new "random" extension was introduced. It provides an object-oriented API for random for random number generation.
* Constants can now be declared in traits. They can then be accessed by classes which use the trait.
* Creation of dynamic properties are now deprecated to avoid mistakes and typos.
* Typed class constants
* Class constants can now be fetched dynamically
* A new `#[\Override]` attribute was introduced. It ensures that a method of the same name exists in the parent class or implemented interface.
* Deep-cloning of readonly properties is now allowed.
* A now `json_validate()` function was introduced to check if a string is syntactically valid JSON.
* The command line linter now supports parsing multiple files at once.

Moreover, an apache2 change now ensures that the apache2 service will restart after the PHP package is upgraded. This is a change in the package behavior. Before, needrestart would inform the user of the need to restart the service, but the service would not restart automatically. Please see [LP: #2038912](https://bugs.launchpad.net/ubuntu/+source/apache2/+bug/2038912) for additional context on this change.

For more details, please see the [upstream changelog](https://www.php.net/ChangeLog-8.php#PHP_8_3)

#### PostgreSQL

The [PostgreSQL](https://www.postgresql.org) package was updated to version 16.2. The new version includes several performance improvements. Here are some of the major changes included since Ubuntu Jammy.

* The SQL standard `MERGE` command is now available. it lets you write conditional SQL statements including `INSERT`, `DELETE`, and `UPDATE` actions in a single statement.
* New regular expressions related functions.
* New `jsonlog` format to output logs using a defined JSON structure.
* Users can now perform logical replication from standby instance
* More syntax from `SQL/JSON` was added, such as `JSON_ARRAY()`, `JSON_ARRAYAGG()`, and `IS JSON`.
* Users can now express thousands using `_` as a separator (e.g., `5_100_042`)
* Added support for non-decimal integer literals, such as `0x1234A`, `0o777`, and `0b0101011`
* Several security-oriented client connection parameters were added, including `require_auth` to specify accepted authentication parameters, and `sslrootcert="system"` to use the trusted certificate authority (CA) store provided by the client's operating system.

For details on the above changes or to get a complete list of changes introduced in PostgreSQL 16, please refer to the [upstream release notes](https://www.postgresql.org/docs/16/release-16.html).

#### QEMU

The [QEMU](https://qemu.org) package was updated to version 8.2.1.  Here are the changes since Ubuntu Jammy.

* User-mode emulation (`linux-user`, `bsd-user`) will enforce guest alignment constraints and raise
`SIGBUS` to the guest program as appropriate.
* The `qemu-nbd` program has gained a new `--tls-hostname` parameter to allow TLS validation against a different hostname, such as when setting up TLS through a TCP tunnel, and now supports TLS over UNIX sockets.
 * ARM
   * Emulation of ARM Cortex-A76, Cortex-A35, Cortex-A710, Neoverse-N1, Neoverse-N2 CPUs.
   * The virt board now supports emulation of the GICv4.0.
   * Several new PCPU architecture features are now emulated as well.
   * KVM VMs on a host which supports MTE (the Memory Tagging Extension) can now use MTE in the guest
 * RISC-V
   * Add support for privileged spec version 1.12.0.
   * Add support for the `Zbkb`, `Zbkc`, `Zbkx`, `Zknd`/`Zkne`, `Zknh`, `Zksed`/`Zksh` and `Zkr` extensions.
   * Add support for `Zmmul` extension.
   * Add TPM support to the virt board.
   * virt machine device tree improvements.
   * Support for various further RISC-V extensions, among them the hypervisor extension is no more marked experimental and now enabled by default.
    * Add RISC-V vector cryptographic instruction set support.
    * Update RISC-V vector crypto to ratified v1.0.0.
 * s390x
   * Emulate the s390x Vector-Enhancements Facility 2 with TCG.
   * The `s390-ccw` bios has been fixed to also boot from drives with non-512 sector sizes that have a different geometry than the typical DASD drives.
   * Fix emulation of `LZRF`, `VISTR`, `SACF` instructions.
   * Enhanced zPCI interpretation support for KVM guests.
   * Implement Message-Security-Assist Extension 5 (random number generation via `PRNO` instruction).
    * Support s390x CPU topology (books and drawers, `STSI` 15.1.x instruction, `PTF` instruction) with KVM.
 * More
   * Support for zero-copy-send on Linux, which reduces CPU usage on the source host. Note that locked memory is needed to support this.
   * Added support for Intel AMX.
   * TCG performance improvements in full-system emulation.
   * TCG support for `AVX`, `AVX2`, `F16C`, `FMA3` and `VAES` instructions.
* Support for the Sapphire Rapids and Granite Rapids CPU models.
* System emulation on 32-bit x86 hosts has been deprecated. The QEMU project no longer considers 32-bit x86 host support for system emulation to be an effective use of its limited resources, and thus intends to discontinue. User mode emulation continues to be supported on 32-bit hosts.
* Support for `igb` device emulation.
* Support virtual machines with up to 1024 vCPUs (for more details, see [here](https://ubuntu.com/server/docs/create-qemu-vms-with-up-to-1024-vcpus))
* Due to the GlusterFS demotion (see [LP: #2045063](https://bugs.launchpad.net/ubuntu/+source/glusterfs/+bug/2045063)), the GlusterFS block storage module was moved out of the `qemu-block-extra` package and into the new `qemu-block-supplemental` package. Please see the GlusterFS section of these Release Notes for upgrade considerations if you are using qemu with the GlusterFS block storage module.
* Since GlusterFS is no longer available for 32 bit architectures (see [LP: #2052734](https://bugs.launchpad.net/ubuntu/+source/glusterfs/+bug/2052734)), the `block-gluster` storage module (now shipped in `qemu-block-supplemental`) is no longer available in armhf.

For more details, please see related upstream changelogs:
- [8.2](https://wiki.qemu.org/ChangeLog/8.2)
- [8.1](https://wiki.qemu.org/ChangeLog/8.1)
- [8.0](https://wiki.qemu.org/ChangeLog/8.0) [Mantic]
- [7.2](https://wiki.qemu.org/ChangeLog/7.2)
- [7.1](https://wiki.qemu.org/ChangeLog/7.1)
- [7.0](https://wiki.qemu.org/ChangeLog/7.0)
- [6.2](https://wiki.qemu.org/ChangeLog/6.2) [Jammy]


#### Ruby 3.2

The default ruby interpreter was updated to version 3.2.3. There are many new features and bug fixes, some highlights are:

- YJIT is now production ready (JIT compiler for Ruby).
- Immutable objects with `Data.define` (new `Data` class).
- WebAssembly support.
- `bundle gem` now supports `--ext=rust` to allow building gems with rust extensions.

There are some constants and methods that were already deprecated and now they are removed, when migrating to this ruby version be careful with the following:

- `Fixnum` and `Bignum`
- `Random::DEFAULT`
- `Struct::Group`
- `Struct::Passwd`
- `Dir.exists?`
- `File.exists?`
- `Kernel#=~`
- `Kernel#taint`, `Kernel#untaint`, `Kernel#tainted?`
- `Kernel#trust`, `Kernel#untrust`, `Kernel#untrusted?`

All the above was removed from Ruby 3.2 and cannot be used anymore. For more information, please see [the upstream release announcement](https://www.ruby-lang.org/en/news/2022/12/25/ruby-3-2-0-released/).

#### `runc`

The runc package was updated to version 1.1.12. It contains bug fixes specially related to the cgroup v2 support, and most importantly, it adds support for riscv64. For more information, please see [the upstream changelog](https://github.com/opencontainers/runc/releases).

For users/developers willing to customize the runc package, the source package is now split into `runc` (library package) and `runc-app` (application package). This was done to follow what was done in containerd and docker.io, and therefore, ease the future maintenance, including backports to stable releases.

#### Samba
The Samba package has been updated to the 4.19.x series. Here are the upstream release notes for 4.19.0: https://www.samba.org/samba/history/samba-4.19.0.html

Due to the GlusterFS demotion (see [LP: #2045063](https://bugs.launchpad.net/ubuntu/+source/glusterfs/+bug/2045063) and the GlusterFS section of these release notes), the samba packaging had to be changed a bit to accommodate this change.

The GlusterFS VFS modules which were previously shipped in the binary `samba-vfs-modules` package, are now shipped in the new binary package called `samba-vfs-modules-extra`. Specifically, these modules (and their respective manual pages) were moved to `samba-vfs-modules-extra`:
* `glusterfs.so`
* `glusterfs_fuse.so`

The `fuse` module does not depend on the gluster libraries, but was moved together with `glusterfs.so` for consistency.

If you are upgrading from an Ubuntu release that used either of those two VFS modules, you should install `samba-vfs-modules-extra` after the upgrade:

    sudo apt install samba-vfs-modules-extra

If you are doing a fresh install of Ubuntu Noble, and want to use the glusterfs VFS modules with samba, you should also install `samba-vfs-modules-extra`.

#### Spamassassin

Apache SpamAssassin 4.0.0 contains numerous tweaks and bug fixes over the past releases. In particular, it includes major changes that significantly improve the handling of text in international language.

As with any major release, there are countless functional patches and improvements to upgrade to 4.0.0. Apache SpamAssassin 4.0.0 includes several years of fixes that significantly improve classification and performance.

New plugins include ExtractText, DMARC, and DecodeShortURLs. The HashCash module, which had been deprecated previously, is now fully removed.  Mail::SPF::Query use is deprecated, along with settings do_not_use_mail_spf, do_not_use_mail_spf_query.  Mail::SPF is now the only supported module used by the SPF plugin.

Other notable changes include:

* Bayes plugin has been improved to skip common words aka noise words written in languages other than English
* You can now use Captured Tags to use tags "captured" in one rule inside other rules
* sa-update has been improved with three new options: forcemirror, score-multiplier, and score-limit.
* DKIM plugin can now detect ARC signatures
* The normalize_charset option is now enabled by default.
* SPF lookups are not done asynchronously
* The default sa-update ruleset doesn't make ASN lookups or header additions anymore.

The [SpamAssassin 4.0.0 release announcement](https://svn.apache.org/repos/asf/spamassassin/trunk/build/announcements/4.0.0.txt) provides more details about these changes.

#### Squid

The [Squid](http://www.squid-cache.org) package was updated to version 6.6. Here are some of the major changes since Ubuntu Jammy.

* Squid is now more tolerant on `tls-cert=` misconfiguration. It will try to sort the CA chain and send certificates in the required order.
* Squid now logs communication details for TLS connections it accepts or establishes.
* A new `to_linklocal` ACL was introduced as pre-defined to match requests from 169.254.0.0/16 and fe80::/10.
* The `X-Cache` and the `X-Cache-Lookup` HTTP headers were replaced with the new `Cache-Status` HTTP header, as per RFC 9211. Tools and systems relying on the `X-` headers should be upgraded to use the new header.
* The Gopher protocol support was removed.

For more details, please see [the upstream release notes](http://www.squid-cache.org/Versions/v6/squid-6.6-RELEASENOTES.html).

#### SSSD

The [SSSD](https://sssd.io) package was updated to version 2.9.4.  Here are the changes since Ubuntu Jammy.

* All SSSD client libraries (`nss`, `pam`, etc.) won’t serialize requests anymore by default, i.e. requests from multiple threads can be executed in parallel. The old behavior (serialization) can still be enabled by setting the environment variable `SSS_LOCKFREE` to `NO`.
* Added a new krb5 plugin `idp` and a new binary `oidc_child` which performs **OAuth2** authentication against FreeIPA. This, however, cannot be tested yet because this feature is still under development on the FreeIPA server side.
* `sss_simpleifp` library is deprecated and might be removed in further releases.
* “Files provider” (i.e. `id_provider = files`) is deprecated and might be removed in further releases. Consider using “Proxy provider” with `proxy_lib_name = files` instead.
* Add support for `ldapi://` URLs to allow connections to local LDAP servers.
* The `proxy` provider is now able to handle certificate mapping and matching rules and users handled by the proxy provider can be configured for local Smartcard authentication. Besides the mapping rule local Smartcard authentication should be enabled with the `local_auth_policy` option in the backend and with `pam_cert_auth` in the PAM responder.

### Intel® QuickAssist Technology (Intel® QAT)

Intel® QAT is a built-in accelerator on 4th Gen and newer Intel® Xeon® Scalable Processors that offloads critical data compression and decompression, encryption and decryption, and public key data encryption tasks from the CPU cores and accelerates those operations to help improve performance and save valuable compute resources.

The components enabled on Ubuntu 24.04 LTS are:
* qatlib 24.02.0
This package provides user space libraries that allow access to Intel® QAT devices and expose the Intel® QAT APIs and sample codes.
For more information, visit the project’s [repo](https://github.com/intel/qatlib?tab=readme-ov-file#features).
* qatengine 1.5.0
This package provides the Intel® QAT OpenSSL Engine Plug-in as a shared library that sits between OpenSSL and the QAT library. The engine can be configured to use Intel optimized libraries (ipp-crypto and intel-ipsec-mb) and/or offload those operations to the QAT device.
For more information, visit the project’s [repo](https://github.com/intel/QAT_Engine/blob/master/docs/features.md).
* qatzip 1.2.0
This package provides a user space library offering accelerated compression and decompression services by offloading the work to the Intel QAT device, which uses the deflate* and lz4* algorithms.
For more information, visit the project’s [repo](https://github.com/intel/QATzip?tab=readme-ov-file#features).
* ipp-crypto 2021.10.0
Intel® Integrated Performance Primitives Cryptography (Intel® IPP Cryptography) is a secure, fast and lightweight library of building blocks for cryptography, highly-optimized for various Intel® CPUs.
For more information, visit the project’s [repo](https://github.com/intel/ipp-crypto).
* intel-ipsec-mb 1.5-1
Intel® Multi-Buffer Crypto for IPsec Library provides software crypto acceleration that primarily focuses on symmetric cryptography applications.
For more information, visit the project’s [repo](https://github.com/intel/intel-ipsec-mb).

#### Subiquity

A new version of the Subiquity server installer has been released. Please read the full [release notes for 24.04.1](https://github.com/canonical/subiquity/releases/tag/24.04.1) on GitHub.

#### OpenSSH

Since Ubuntu 22.10, `openssh-server` is configured to use systemd socket activation by default. In Ubuntu 24.04 LTS, the implementation changed so that settings from `/etc/ssh/sshd_config` (and snippets from `/etc/ssh/sshd_config.d/`) are read by a systemd generator to configure the `ssh.socket` unit accordingly.  See the [original discourse post](https://discourse.ubuntu.com/t/sshd-now-uses-socket-based-activation-ubuntu-22-10-and-later/30189/1) for more details. 

#### Ubuntu HA/Clustering

##### Pacemaker

The [Pacemaker](https://clusterlabs.org/pacemaker/) package was updated to version 2.1.6. There are several fixes, API changes and new features introduced since jammy. For more details, please see [the upstream changelog](https://github.com/ClusterLabs/pacemaker/releases).

##### Resource Agents

The [Resource Agents](https://github.com/ClusterLabs/resource-agents) package was updated to version 4.13.0.

A noteworthy change is the upstream improvements on PostgreSQL support. The pgsql agent was moved to the resource-agents-base package and is now part of our curated set of resource agents.

Moreover, the transitional resource-agents package was removed. You should now install resource agents through the resource-agents-base package or through the resource-agents-extra package. The agents available in each of these packages are listed in the package descriptions.

For further information, please refer to [the upstream changelog](https://github.com/ClusterLabs/resource-agents/blob/main/ChangeLog).

#### OpenStack

OpenStack has been updated to the [2024.1 (Caracal) release](https://releases.openstack.org/caracal/).  This includes packages for Aodh, Barbican, Ceilometer, Designate, Glance, Heat, Horizon, Ironic, Keystone, Magnum, Manila, Masakari, Mistral, Neutron, Nova, Octavia, Swift, Watcher and Zaqar.

Murano, Senlin, Sahara, Freezer and Solum where all [declared inactive](https://governance.openstack.org/tc/reference/emerging-technology-and-inactive-projects.html#current-inactive-projects) as of the 2024.1 cycle and have been removed from Ubuntu.

This release is also provided for Ubuntu 22.04 LTS via the Ubuntu Cloud Archive.

#### Ceph

[Ceph](http://ceph.com) has been updated to a snapshot in preparation for the 19.2.0 (Squid) release which will be provided via a [stable release update](https://bugs.launchpad.net/ubuntu/+source/ceph/+bug/2065515).

This release is also provided for Ubuntu 22.04 LTS via the Ubuntu Cloud Archive.

#### Open vSwitch (OVS) and Open Virtual Network (OVN)

[Open vSwitch](https://www.openvswitch.org/) has been updated to the 3.3.0 release.

[Open Virtual Network](https://www.ovn.org/) has been updated to the 24.03 release.

These releases are also provided for Ubuntu 22.04 LTS via the Ubuntu Cloud Archive.

### Platforms

#### Public Cloud / Cloud images

##### All

* [23.10 cloud images unexpected UDP listening...” : Bugs : cloud-images](https://bugs.launchpad.net/cloud-images/+bug/2038894)
* Cloud-init no longer blocks by default when preseeding snaps
  * See the [cloud-init docs](https://cloudinit.readthedocs.io/en/latest/reference/breaking_changes.html#removed-ubuntu-s-ordering-dependency-on-snapd-seeded) for details on how to fix user scripts that rely on snaps
* Cloud images no longer preseed any snaps by default
  * With the changes to [LXD detailed above](https://discourse.ubuntu.com/t/noble-numbat-release-notes/39890#lxd-45), LXD snap is no longer seeded/installed in the non minimal public cloud images. As a result, snaps will no longer be seeded/installed in non minimal images.
    * The decision remove LXD snap seeding was made @ https://bugs.launchpad.net/ubuntu/+source/ubuntu-meta/+bug/2051346 and the decision to stop seeding any snaps was made @ https://bugs.launchpad.net/ubuntu/+source/ubuntu-meta/+bug/2051572
  * The exceptions are AWS and GCE, which have cloud specific snaps preseeded.
* Upgrading from previous releases
  * Upgrading to Ubuntu 24.04 LTS using do-release-upgrade will result in one of more interactive prompts. One for grub-pc, which will request you choose the boot device, and if chrony is installed you will also be prompted to choose “on disk config” or “packaged config”. These are expected and do not impact the ability to upgrade.
* The footprint of minimal images has been reduced
  * [Introduced in the 23.10 cycle](https://discourse.ubuntu.com/t/mantic-minotaur-release-notes/35534#minimal-downloadqcow2-cloud-images-42), minimal cloud images now are smaller than the Ubuntu 22.04 LTS minimal images. The package count has dropped from 426 to 288 (difference: 138) resulting in a much smaller image size. For example, download qcow2 images have reduced from 337.19MiB to 226.75MiB (diff: 110.44MiB).
  * This was achieved, in part, by reducing the packages installed to only those we feel are required for a functional Ubuntu cloud instance and by removing the installation of ‘Recommends’ packages.

##### Vagrant

Starting in Ubuntu 24.04 LTS, Ubuntu no longer produces Vagrant images. Documentation regarding creating an Ubuntu Base Image from scratch is provided at https://documentation.ubuntu.com/public-images/en/latest/public-images-how-to/build-vagrant-with-bartender/.

##### Public Images (cloud-images.ubuntu.com) images

* Release notes/image diff
  * Since 19th April 2024 we have introduced `.image_changelog.json` files to accompany published images @ https://cloud-images.ubuntu.com/. This is a JSON document listing all the package additions, removals and changes as well as noting the changelog entries for the package changes. It also highlights any CVEs addressed in those package updates. The tool used to generate these diffs is `ubuntu-cloud-image-changelog` available @ [github.com/canonical/ubuntu-cloud-image-changelog](http://github.com/canonical/ubuntu-cloud-image-changelog)
  * Diffs are generated between the image being published and the previous daily image, and also between the image being published and the previous release image.
  * These image diffs have been backported to previous published Ubuntu release too.

* There are potential issues with OVA images and some versions of Cloud Director related to the attached serial port. In some cases, this may lead to a failure to deploy the OVA image. In the event of a failure, editing the OVF directly in your deployment and removing the serial port stanza should allow successful deployment. VMware has an associated [KB article](https://kb.vmware.com/s/article/2128084) regarding these failures. Cloud Director versions around version 10.4.2.22463311 are potentially effected. This is currently under investigation: [LP:2062552](https://bugs.launchpad.net/cloud-images/+bug/2062552).

##### AWS EC2

* Noble instances now launch using [IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) by default for the instance metadata service.
* Auto configuration of [multi-NIC](https://documentation.ubuntu.com/aws/en/latest/aws-how-to/instances/automatically-setup-multiple-nics/) instances is now supported with source-routing via cloud-init.
* The `awscli` debian package got removed from the archive. The [aws-cli](https://snapcraft.io/aws-cli) snap should be used instead. That snap is maintained by AWS itself.

##### Microsoft Azure

* Canonical is introducing  a new way of publishing on Azure with Ubuntu 24.04 LTS. All Ubuntu Images for 24.04 LTS will be available under the same offer: ubuntu-24_04-lts. Derivative images, such as the minimized version of Ubuntu server or Ubuntu Pro are available as plans under this main offer.
* We have identified an issue with AppArmor profiles on Confidential VM images available under the `cvm` plan of the offer `ubuntu-24_04-lts`. For example, the `rsyslog` service will fail to start on VMs launched from this plan. This is being investigated and a new image with a fix will be published shortly.

* Users with multic-NIC setup on their instances may experience delays in DNS resolution due to mis-configuration of systemd-resolved. We are currently implementing a solution on cloud-init (https://github.com/canonical/cloud-init/pull/5180). Before the solution lands in cloud-init, users can remedy the misconfiguration by creating the file `/etc/netplan/91-secondary-nics-azure.yaml` with the content:

```
network:
    version: 2
    ethernets:
        ephemeral:
            dhcp4: true
            dhcp4-overrides:
                use-dns: false
            match:
                driver: hv_netvsc
                name: '!eth0'
            optional: true
        hotpluggedeth0:
            dhcp4: true
            match:
                driver: hv_netvsc
                name: 'eth0'
```

Users should then reboot the instance for the netplan configuration to take effect.

##### Google

* GCE: Setting a hostname via cloud-init user-data requires the addition of the create_hostname_file key; see [here](https://documentation.ubuntu.com/gcp/en/latest/google-how-to/gce/set-hostname-using-cloudinit/) for more details.
* Boot speed improvements: the I/O scheduler has been changed to `none` (from `noop`) to improve i/o performance for the most common disk types ([LP: #2045708](https://bugs.launchpad.net/ubuntu/+source/gce-compute-image-packages/+bug/2045708))
* A regression has been discovered with the GCP suspend feature with the linux-gcp 6.8 kernel that is being investigated in [LP: #2063315](https://bugs.launchpad.net/ubuntu/+source/linux-gcp/+bug/2063315)
* Ubuntu 24.04 LTS has introduced a change in the behaviour of the needrestart package - see notes @ [Services restart on unattended-upgrade](https://discourse.ubuntu.com/t/noble-numbat-release-notes/39890#services-restart-on-unattended-upgrade-26) for more information. This results in any google-guest-agent startup scripts being run again on package upgrade or re-install. This is being investigated but it will only be triggered when the google-guest-agent package is re-installed. It can be worked around by setting `NEEDRESTART_SUSPEND=1` prior to any re-install as per the [`needrestart` man pages](https://manpages.ubuntu.com/manpages/noble/man1/needrestart.1.html#environment) or by appending to the `needrestart` configuration `echo "\$nrconf{override_rc}{qr(^google-(shutdown|startup)-scripts\.service$)} = 0;" >> /etc/needrestart/conf.d/google-guest-agent.conf` which will disable this behaviour for any future `google-guest-agent` upgrade or reinstall. New GCE images will be built and published shortly after release to disable this behaviour for the google-guest-agent by default.

##### Oracle

* The uncomplicated Firewall package ufw is no longer installed in Oracle Cloud Ubuntu 24.04 LTS+ images. Upgrading from an earlier version of Ubuntu to 24.04 will uninstall ufw. The ufw tool conflicts with system configuration through iptables-persistent and netfilter-persistent as documented by Oracle [here](https://docs.oracle.com/en-us/iaas/Content/Compute/References/bestpracticescompute.htm#Essentia), illustrated further on this [blog](https://blogs.oracle.com/developers/post/enabling-network-traffic-to-ubuntu-images-in-oracle-cloud-infrastructure), and listed as a known [issue](https://docs.oracle.com/en-us/iaas/Content/Compute/known-issues.htm#ufw). If ufw is optionally installed on Ubuntu 24.04 LTS+, it will uninstall iptables-persistent and netfilter-persistent, disabling default functionality needed to support iSCSI boot and block devices.

###### How to report any issues resulting from these changes

If you notice any unexpected changes or bugs in the minimal images, create a new bug in [cloud-images](https://bugs.launchpad.net/cloud-images).

#### Raspberry Pi 🍓

##### Pi 5 LTS

24.04 (noble) will be the first LTS release supporting the Raspberry Pi 5 with both arm64 server and desktop images.

##### Browser Acceleration

The Firefox browser now supports 3D acceleration after mesa 23.2 was backported to 22.04 (jammy) which permitted the necessary content snaps to be regenerated. The classic [aquarium sample](https://webglsamples.org/aquarium/aquarium.html) can be used to test the performance of the new graphics stack, which can achieve a smooth 40+fps full-screen on a Pi 5 at a resolution of 1080p.

##### Power monitoring

On the Pi 5, the [pemmican](https://pemmican.readthedocs.io/) package will now provide monitoring of the power supply.

On server images, the MOTD on login will indicate if the power supply failed to negotiate the 5A expected for unlimited operation, or if brownout was the cause of the last reset. Kernel messages will warn of undervolt or overcurrent situations.

On desktop images, a desktop notification will be displayed for these issues, with options for further information or suppression of future warnings of this type.

##### No 32-bit (armhf) images

From 24.04 (noble), we will no longer be producing 32-bit (armhf) images for the Raspberry Pi. The only images produced will be 64-bit (arm64). For the avoidance of doubt, this does *not* mean that armhf is no longer supported as an architecture on Raspberry Pi; it will remain supported as a foreign architecture in noble (see below).

To add armhf as a foreign architecture to an arm64 image, use the following commands:

```
sudo dpkg --add-architecture armhf
sudo apt update
```

Thereafter, to install an armhf package:

```
sudo apt install SOME-PACKAGE:armhf
```

Please note, there will be no armhf kernels (primarily because the Pi 5 does not support 32-bit kernels), and users who are currently on armhf images *will not* be able to upgrade directly to noble.

##### Simpler Bluetooth on server

There is no longer a need to install the `pi-bluetooth` package in order to enable Bluetooth functionality on server images. Simply install the regular `bluez` package and Bluetooth will be configured by the kernel.

#### arm64

The new arm64+largemem ISO includes a kernel with 64k page size. A larger page size can increase throughput, but comes at the cost of increased memory use, making this option more suitable for servers with plenty of memory. Typical use cases for this ISO include: machine learning, databases with many large entries, high performance computing.

#### IBM Z and LinuxONE

* The key 's390-tools' package was step-by-step upgraded to latest v2.31.0 ([LP: #2049612](https://launchpad.net/bugs/2049612)), which incl. lots of updates, new tools and features, especially a secure guest tool to bind and associate APQNs crypto domains ([LP: #2003672](https://launchpad.net/bugs/2003672)).
* Like on all other architectures, COMPAT_32BIT_TIME was also disabled on s390x ([LP: #2038583](https://launchpad.net/bugs/2038583)), and with that 31/32bit legacy support is removed ([LP: #2051683](https://launchpad.net/bugs/2051683)).
* With the upgrade to GDB 15, support for IBM z16 was introduced ([LP: #1982336](https://launchpad.net/bugs/1982336)).
* The Glasgow Haskell Compiler was upgraded to version 9.4.7 that is new enough to enable the LLVM backend to allow performance improvements ([LP: #1913302](https://launchpad.net/bugs/1913302)).
* IBM Z specific improvements also landed in the KVM virtualization stack with the introduction of virtual CPU topology ([LP: #1983223](https://launchpad.net/bugs/1983223)) and enhancement of the dynamic CPU topology for KVM guests ([LP: #2049703](https://launchpad.net/bugs/2049703)), as well as the implementation for nested guest shadow event counters ([LP: #2027926](https://launchpad.net/bugs/2027926)). For more details see the qemu and libvirt sections above.
* Another big area of s390x improvements is cryptography, with the upgrade to opencryptoki v2.23 ([LP: #2050023](https://launchpad.net/bugs/2050023)), there is now support in PKCS #11 3.0 for AES_XTS ([LP: #2025924](https://launchpad.net/bugs/2025924)) and EP11 token support for FIPS 2021-session bound EP11 keys ([LP: #2050014](https://launchpad.net/bugs/2050014)).
* Furthermore libica was updated to v4.3.0 ([LP: #2050024](https://launchpad.net/bugs/2050024)), the openssl-ibmca package to v2.4.1 and the openssl-pkcs11-sign-provider package was made available in v1.0.1 ([LP: 2003668)](https://launchpad.net/bugs/003668),) including fork support ([LP: #2050015](https://launchpad.net/bugs/2050015)).
* And finally several s390x-specific libraries were bumped to their latest version, like qclib to 2.4.1 ([LP: #2050028](https://launchpad.net/bugs/2050028)) and libzpc to v1.2.0 ([LP: #2050031](https://launchpad.net/bugs/2050031)).

#### IBM POWER (ppc64el)

KVM running in IBM PowerVM LPARs:
Ubuntu Server 24.04 has now the required technology enablement and support for running KVM in a PowerVM LPAR.
This technology enables expanded open-source based innovations and solutions for Ubuntu Server on the IBM Power platform.
Below are the firmware and hardware requirements:
* Firmware: FW1060.10
* Hardware: IBM Power10

Note: KVM virtualization continues to be supported on POWER9 bare-metal / OPAL based systems.

#### RISC-V

Ubuntu 24.04 LTS is the first LTS release for the StarFive VisionFive 2 board.
For an overview of Canonical supported boards see https://ubuntu.com/download/risc-v/canonical-built.

The RISC-V Ubuntu userland is compatible with all RVA20 hardware.

(24-04-known-issues)=
## Known Issues

As is to be expected with any release, there are some significant known bugs that users may encounter with this release of Ubuntu. The ones we know about at this point (and some of the workarounds) are documented here, so you don't need to spend time reporting these bugs again:

### General

* In 24.04.2 HDMI output for Nezha D1 and LicheeRV is broken due to a missing kernel module.


#### sysstat enablement state mismatches intent

In 24.04, we shipped sysstat by default as part of a wider performance engineering effort. The idea is that relevant performance engineering tooling is already present and available when a user finds themselves needing to solve a performance engineering problem.

In some cases the sysstat services are not actually enabled. This will be fixed in a future update. When the update arrives, sysstat will become enabled in situations where it wasn't enabled before, to realign with our intended defaults. If you do not wish sysstat services to ever run, you may remove the sysstat package in advance.

See [LP: #2073285](https://launchpad.net/bugs/2073285) and [LP: #2073284](https://launchpad.net/bugs/2073284) for details.

### Linux kernel

In 24.04.4:
* for 6.17.0-14.14 (HWE kernel)
  - Kernel crash when connecting multiple displays that are daisy-chained via USB-C ([LP: #2141225](https://launchpad.net/bugs/2141225)). Still under investigation.
  - Intel MIPI (IPU6/7) cameras are not detected ([LP: #2140761](https://launchpad.net/bugs/2140761)). Fix is known and scheduled to be included in the next kernel update.
  - Some Intel Wifi chips are missing their firmware file ([LP: #2140975](https://bugs.launchpad.net/ubuntu/+source/linux-firmware/+bug/2140975)). If you need to install online using Wifi and one of those chips, make sure to grab the previous point-release image (24.04.3).
* for 6.8.0-100.100
  - Suspend failures when mt7925* wireless driver is loaded ([LP: #2141198](https://launchpad.net/bugs/2141198)). Still under investigation.

### Ubuntu Desktop

* Screen reader support is present with the new desktop installer, but is incomplete ([LP: #2061015](https://launchpad.net/bugs/2061015), [LP: #2061018](https://launchpad.net/bugs/2061018), [LP: #2036962](https://launchpad.net/bugs/2036962), [LP: #2061021](https://launchpad.net/bugs/2061021))

* OEM installs are not supported yet ([LP: #2048473](https://launchpad.net/bugs/2048473))

* Application icons don't use the correct High Contrast theme when High Contrast is enabled [(LP: #2013107](https://launchpad.net/bugs/2013107))

* GTK4 apps (including the desktop wallpaper) do not display correctly with VirtualBox or VMWare with 3D Acceleration ([LP: #2061118](https://launchpad.net/bugs/2061118)).

* Fullscreen graphics performance in Xorg sessions (i.e. with the Nvidia driver) has temporarily regressed ([LP: #2052913](https://bugs.launchpad.net/bugs/2052913)).

* Netbooting the new desktop installer causes the installer to crash on startup. The issue will be resolved for the 24.04.1  release (or sooner) and at that time the fix will become available via a manual `snap refresh` in the live environment on the 24.04 ISOs ([LP: #2062988](https://launchpad.net/bugs/2062988)).

* **Incompatibility between TPM-backed Full Disk Encryption and Absolute:** TPM-backed Full Disk Encryption (FDE) has been introduced to enhance data security. However, it's important to note that this feature is incompatible with Absolute (formerly Computrace) security software. If Absolute is enabled on your system, the machine will not boot post-installation when TPM-backed FDE is also enabled. Therefore, disabling Absolute from the BIOS is recommended to avoid booting issues.
* **Hardware-Specific Kernel Module Requirements for TPM-backed Full Disk Encryption:** TPM-backed Full Disk Encryption (FDE) requires a specific kernel snap which may not include certain kernel modules necessary for some hardware functionalities. A notable example is the `vmd` module required for NVMe RAID configurations. In scenarios where such specific kernel modules are indispensable, the hardware feature may need to be disabled in the BIOS (such as RAID) to ensure the continued availability of the affected hardware post-installation. If disabling in the BIOS is not an option, the related hardware will not be available post-installation with TPM-backed FDE enabled.
* [FDE specific bug reports](https://bugs.launchpad.net/bugs/+bugs?field.searchtext=&orderby=-importance&field.status%3Alist=NEW&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.tag=fde&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search).

### Ubuntu Server

#### freeradius
The [freeradius](https://launchpad.net/ubuntu/+source/freeradius) package will be accidentally removed by the release upgrade tool on upgrades from Ubuntu 22.04 LTS to Ubuntu 24.04 LTS. The removal is reported in the upgrade summary before any action is taken, but might be missed.
This is being tracked in [LP: #2114224](https://bugs.launchpad.net/ubuntu/+source/freeradius/+bug/2114224).

#### Installer

* In some situations, it is acceptable to proceed with an offline installation when the mirror is inaccessible. In this scenario, it is advised to use:

```
apt:
  fallback: offline-install
```

#### samba apparmor profile
Due to [bug LP: #2063079](https://bugs.launchpad.net/ubuntu/+source/samba/+bug/2063079), the samba `smbd.service` unit file is no longer calling out to the helper script to dynamically create apparmor profile snippets according to the existing shares.

By default, the `smbd` service from samba is not confined. To be affected by this bug, users have to:
- install the optional `apparmor-profiles` package
- switch the `smbd` profile confinement from `complain` to `enforce`

Therefore, only users who have taken those steps and upgrade to Noble, will be affected by this bug. An SRU to fix it will be done shortly after release.

#### rrdtool on armhf
`rrdtool` is a very popular package used by monitoring and graphing tools such as [cacti](https://www.cacti.net/), [munin](https://munin-monitoring.org/), [mrtg](https://oss.oetiker.ch/mrtg/), and others.

Due to the Ubuntu 24.04 LTS `time_t` change from 32bits to 64bits in the armhf architecture, to fix the [Year 2038 problem](https://discourse.ubuntu.com/t/ubuntu-24-04-lts-noble-numbat-release-notes/39890#year-2038-support-for-the-armhf-architecture) mentioned elsewhere in these Release Notes, the `rrd` databases produced by `rrdtool` in armhf in Ubuntu releases before Noble are not binary compatible with `rrdtool` in Ubuntu 24.04 LTS and later.

If such `rrd` files are attempted to be read by `rrdtool` from Ubuntu 24.04 LTS or later, it will fail with an error that can be similar to this:

```
ERROR: 'database-file.rrd' is too small (should be 1032 bytes)
```

This essentially prevents the database from being opened, read, or written to.

To correctly upgrade such systems, each `rrd` database needs to be dumped into xml using the tool from the system before the upgrade, and restored into `rrd` from that xml on the upgraded system. This is a manual process and there is no automated tooling for this available at the moment.

To dump a `rrd` file into xml:

```
rrdtool dump file.rrd > file.xml
```

To later restore it on the new upgraded system:

```
rrdtool restore file.xml file.rrd
```

For more details, please see the [rrddump](https://manpages.ubuntu.com/manpages/noble/man1/rrddump.1.html) and [rrdrestore](https://manpages.ubuntu.com/manpages/noble/man1/rrdrestore.1.html) manpages.

#### Raspberry Pi

* On Pi 3A+, 3B+, 4B, and 5, when the wifi reconnects to an AP advertising a regulatory domain, various kernel errors are reported which may interrupt the console output (particularly on server). While annoying, this doesn't actually affect wifi connectivity, but may slow down re-authentication ([LP: #2063365](https://launchpad.net/bugs/2063365))

* The startup sound does not play before the initial setup process, hence users cannot currently rely on hearing this sound to determine if the system has booted ([LP: #2060693](https://launchpad.net/bugs/2060693))

* The seeded totem video player will not prompt users to install missing codecs when attempting to play a video requiring them ([LP: #2060730](https://launchpad.net/bugs/2060730))

* With some monitors connected to a Raspberry Pi, it is possible that a monitor powers off after a period of inactivity but then powers back on and shows a black screen. Investigation into the types of monitors affected is ongoing in [LP: #1998716](https://bugs.launchpad.net/ubuntu/+source/mutter/+bug/1998716).

* With the removal of the `crda` package in 22.04, the method of setting the wifi regulatory domain (editing `/etc/default/crda`) no longer operates. On server images, use the `regulatory-domain` option in the Netplan configuration. On desktop images, append `cfg80211.ieee80211_regdom=GB` (substituting `GB` for the relevant country code) to the kernel command line in the `cmdline.txt` file on the boot partition  ([LP: #1951586](https://launchpad.net/bugs/1951586)).

* The power LED on the Raspberry Pi 2B, 3B, 3A+, 3B+, and Zero 2W currently goes off and stays off once the Ubuntu kernel starts booting ([LP: #2060942](https://launchpad.net/bugs/2060942))

* libcamera support is currently broken; this will be a priority for next cycle and fixes will be SRU'd to noble as and when they become available ([LP: #2038669](https://bugs.launchpad.net/ubuntu/+source/libcamera/+bug/2038669))

* Red and blue colours in the Ubuntu software store are reversed ([LP: #2076919](https://launchpad.net/bugs/2076919))

#### RISC--V

* SD-card support is missing on the Milk-V Mars CM Lite.
* PCIe on StarFive JH7110 based boards only supports NVMe.

#### Google Compute Platform 

* Ubuntu 24.04 LTS has introduced a change in the behaviour of the needrestart package - see notes @ [Services restart on unattended-upgrade](https://discourse.ubuntu.com/t/noble-numbat-release-notes/39890#services-restart-on-unattended-upgrade-26) for more information. This results in any google-guest-agent startup scripts being run again on package upgrade or re-install. This is being investigated but it will only be triggered when the google-guest-agent package is re-installed. It can be worked around by setting `NEEDRESTART_SUSPEND=1` prior to any re-install as per the [`needrestart` man pages](https://manpages.ubuntu.com/manpages/noble/man1/needrestart.1.html#environment) or by appending to the `needrestart` configuration `echo "\$nrconf{override_rc}{qr(^google-(shutdown|startup)-scripts\.service$)} = 0;" >> /etc/needrestart/conf.d/google-guest-agent.conf` which will disable this behaviour for any future `google-guest-agent` upgrade or reinstall.
New GCE images will be built and published shortly after release to disable this behaviour for the google-guest-agent by default.

#### Microsoft Azure

* We have identified an issue with AppArmor profiles on Confidential VM images available under the `cvm` plan of the offer `ubuntu-24_04-lts`. For example, the `rsyslog` service will fail to start on VMs launched from this plan. This is being investigated and a new image with a fix will be published shortly.

(24-04-official-flavors)=
## Official flavors

Find the release notes for the official flavors at the following links:

* [Edubuntu Release Notes](https://discourse.ubuntu.com/t/edubuntu-24-04-lts-released/44455/)
* [Kubuntu Release Notes](https://wiki.ubuntu.com/NobleNumbat/ReleaseNotes/Kubuntu)
* [Lubuntu Release Notes](https://lubuntu.me/noble-released/)
* [Ubuntu Budgie Release Notes](https://ubuntubudgie.org/2024/04/ubuntu-budgie-24-04-release-notes/)
* [Ubuntu MATE Release Notes](https://ubuntu-mate.org/blog/ubuntu-mate-noble-numbat-release-notes/)
* [Ubuntu Studio Release Notes](https://ubuntustudio.org/ubuntu-studio-24-04-LTS-release-notes/)
* [Ubuntu Unity Release Notes](https://ubuntuunity.org/posts/ubuntu-unity-2404-released/)
* [Xubuntu Release Notes](https://wiki.xubuntu.org/releases/24.04/release-notes)
* [Ubuntu Kylin Release Notes](https://ubuntukylin.com/news/ubuntukylin2404-en.html)
* [Ubuntu Cinnamon Release Notes](https://ubuntucinnamon.org/?p=1310)

(24-04-more-information)=
## More information

Refer to {ref}`release-policy-and-schedule` and {ref}`project-and-community`.
