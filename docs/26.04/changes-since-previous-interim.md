(ubuntu-26.04-lts-changes-since-25.10)=
# Ubuntu 26.04 LTS changes since 25.10

If you're upgrading to Ubuntu 26.04 LTS from the previous interim release, Ubuntu 25.10 (Questing Quokka), the following changes apply to you.

## New features and improvements

### Desktop features

:::{rubric} GNOME 50
:::

The GNOME desktop environment has been updated to version 50.

### Server features

:::{rubric} cloud-init v. 25.1.1
:::

...

:::{rubric} Kerberos
:::

Kerberos has been configured to observe the `/etc/krb5.conf.d/` directory by default. This introduces support for third-party packages that need to add Kerberos configuration.

* If you have existing configuration snippets in `/etc/krb5.conf.d/`, but do not include them, they will now be included in the `krb5.conf` file.
* If you already include `/etc/krb5.conf.d/` in your `krb5.conf` file, either active or commented out, no changes will be made.
* If your existing `krb5.conf` file is a symbolic link, no changes will be made.

MIT Kerberos and Heimdal are both supported, but use different orderings for the include directive. MIT Kerberos uses alphanumerical order, while Heimdal uses the unpredictable order of the readdir() system call ([LP: #2140967](https://bugs.launchpad.net/ubuntu/+source/heimdal/+bug/2140967)).

### Development features

:::{rubric} Toolchain Upgrades 🛠️
:::

* glibc 2.42 now ships non-utf8 encodings as `libc-gconv-modules-extra`.
* LLVM 21 is the default LLVM toolchain.
* Rust 1.93.1 is the default Rust toolchain.

:::{rubric} OpenJDK
:::

OpenJDK 25 is the default Java toolchain.

:::{rubric} .NET
:::

...

### Enterprise features

### Cloud features

### Security features

### Hardware support features

### Common features

:::{rubric} Linux kernel 7.0 🐧
:::

* `cgroupfs` is now mounted with `nsdelegate,memory_recursiveprot,memory_hugetlb_accounting`

:::{rubric} systemd v257.4
:::

...

:::{rubric} Netplan v1.1.2 🌐
:::

...

:::{rubric} fwupd
:::

Systems running TPM/FDE will now prompt for the recovery key before firmware updates that may require the recovery key upon reboot.

:::{rubric} sudo-rs
:::

Password feedback is now enabled by default in order to improve the user experience of `sudo`.
If the previous behavior is preferred, password feedback can be disabled using the following steps:

1. Edit sudoers using `sudo visudo` in the terminal
2. Add the option `Defaults !pwfeedback` to the configuration file

:::{rubric} Package Management: APT 3.0
:::

...

## Backwards-incompatible changes

### Desktop changes

### Server changes

:::{rubric} SSSD
:::

Now running under user `sssd` (instead of `root`)!

* Please make sure that sssd can still access secrets or integrations from its new user

Updated to version 2.12.

* The implicit files provider and domain was removed: https://sssd.io/docs/files-provider-deprecation.html

Other changes of importance are listed upstream:

* https://sssd.io/release-notes/sssd-2.11.0.html
* https://sssd.io/release-notes/sssd-2.12.0.html

### Development changes

### Enterprise changes

### Cloud changes

### Security changes

### Hardware support changes

### Common changes


## Deprecated features

### Desktop deprecations

### Server deprecations

### Development deprecations

### Enterprise deprecations

### Cloud deprecations

### Security deprecations

### Hardware support deprecations

### Common deprecations


## Bug fixes

### Desktop fixes

### Server fixes

### Development fixes

### Enterprise fixes

### Cloud fixes

### Security fixes

:::{rubric} Apache2
:::

Apache 2 has been upgraded to upstream version 2.4.65. This new release includes a security fix:

* [CVE-2025-54090](https://www.cve.org/CVERecord?id=CVE-2025-54090): Apache HTTP Server: ‘RewriteCond expr’ always evaluates to true in 2.4.64

For more details, see the [upstream release notes](https://www.apachelounge.com/Changelog-2.4.html) and the list of [security fixes](https://httpd.apache.org/security/vulnerabilities_24.html).

The Debian changes for the new version have also disabled TLS 1.0 and 1.1, following RFC 8996. These should be already disabled by default in OpenSSL, and now Apache2 follows the same. See [the fixed bug](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=943415).

### Hardware support fixes

### Common fixes


## Known issues

As is to be expected with any release, there are some significant known bugs that users may encounter with this release of Ubuntu. The ones we know about at this point (and some of the workarounds) are documented here, so you don’t need to spend time reporting these bugs again:

### Desktop issues

:::{rubric} Localization
:::

The Live Session of the new Ubuntu Desktop installer is not localized. It is still possible to perform a non-English installation using the new installer, but internet access at install time is required to download the language packs. ([LP: #2013329](https://bugs.launchpad.net/ubuntu-release-notes/+bug/2013329))

:::{rubric} Screen reader support
:::

Screen reader support is present with the new desktop installer, but is incomplete ([LP: #2061015](https://launchpad.net/bugs/2061015), [LP: #2061018](https://launchpad.net/bugs/2061018), [LP: #2036962](https://launchpad.net/bugs/2036962), [LP: #2061021](https://launchpad.net/bugs/2061021))

:::{rubric} OEM installs
:::

OEM installs are not supported yet. ([LP: #2048473](https://launchpad.net/bugs/2048473))

:::{rubric} Virtualized GTK 4 apps
:::

GTK 4 apps (including the desktop wallpaper) do not display correctly with VirtualBox or VMWare with 3D Acceleration ([LP: #2061118](https://launchpad.net/bugs/2061118)).

:::{rubric} Incompatibility between TPM-backed Full Disk Encryption and Absolute
:::

TPM-backed Full Disk Encryption (FDE) has been introduced to enhance data security. However, it’s important to note that this feature is incompatible with Absolute (formerly Computrace) security software. If Absolute is enabled on your system, the machine will not boot post-installation when TPM-backed FDE is also enabled. Therefore, disabling Absolute from the BIOS is recommended to avoid booting issues.

:::{rubric} Hardware-Specific Kernel Module Requirements for TPM-backed Full Disk Encryption
:::

TPM-backed Full Disk Encryption (FDE) requires a specific kernel snap which may not include certain kernel modules necessary for some hardware functionalities. A notable example is the `vmd` module required for NVMe RAID configurations. In scenarios where such specific kernel modules are indispensable, the hardware feature may need to be disabled in the BIOS (such as RAID) to ensure the continued availability of the affected hardware post-installation. If disabling in the BIOS is not an option, the related hardware will not be available post-installation with TPM-backed FDE enabled.

:::{rubric} Full-disk encryption
:::

See [FDE specific bug reports](https://bugs.launchpad.net/bugs/+bugs?field.searchtext=&orderby=-importance&field.status%3Alist=NEW&field.status%3Alist=CONFIRMED&field.status%3Alist=TRIAGED&field.status%3Alist=INPROGRESS&field.status%3Alist=FIXCOMMITTED&field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&assignee_option=any&field.assignee=&field.bug_reporter=&field.bug_commenter=&field.subscriber=&field.tag=fde&field.tags_combinator=ANY&field.status_upstream-empty-marker=1&field.has_cve.used=&field.omit_dupes.used=&field.omit_dupes=on&field.affects_me.used=&field.has_patch.used=&field.has_branches.used=&field.has_branches=on&field.has_no_branches.used=&field.has_no_branches=on&field.has_blueprints.used=&field.has_blueprints=on&field.has_no_blueprints.used=&field.has_no_blueprints=on&search=Search).

:::{rubric} Resuming from suspend on Nvidia
:::

Resuming from suspend on Nvidia desktops (where Nvidia is the primary GPU so generally not laptops)  will exhibit visual corruption and freezes using the default Wayland session  ([LP#1876632](https://bugs.launchpad.net/bugs/1876632)). If you need suspend/resume support then the simplest solution is to select ‘Ubuntu on Xorg’ at the login screen.

:::{rubric} Classic fonts
:::

Installing `ubuntu-fonts-classic` results in a non-Ubuntu font being displayed ([LP#2083683](https://bugs.launchpad.net/bugs/2083683)). To resolve this, install `gnome-tweaks` and set ‘Interface Text’ to ‘Ubuntu’.

### Server issues

:::{rubric} rabbitmq-server
:::

Certain version hops may be unsupported due to feature flags, raising questions about how Ubuntu will maintain this package moving forward. We are currently exploring the use of snaps as a potential solution to enable smoother upgrades. For more information please read <https://bugs.launchpad.net/bugs/2074309>.

:::{rubric} Bacula
:::

Moved from our `main` repository to `universe`. All relevant Ubuntu changes are upstream now, so we directly sync this from Debian.

:::{rubric} Openstack
:::

Currently, Nova Compute is non-functional because of a python3.13 incompatiblity ([LP:#2103413](https://bugs.launchpad.net/ubuntu/+source/nova/+bug/2103413)).
The Openstack team and Upstream work on it and it will be resolved via an SRU later.

The Ubuntu Cloud Archive is not affected by this bug.

:::{rubric} Installer
:::

On systems booting via U-Boot, U-Boot should be updated to the current Plucky version before installation as subiquity does not run flash-kernel and grub-update during the installation. So for first boot the device-tree from U-Boot will be used.

* In some situations, it is acceptable to proceed with an offline installation when the mirror is inaccessible. In this scenario, it is advised to use:

    ```yaml
    apt:
      fallback: offline-install
    ```

* Network interfaces left unconfigured at install time are assumed to be configured via dhcp4. If this doesn’t happen (for example, because the interface is physically not connected) the boot process will block and wait for a few minutes ([LP: #2063331](https://bugs.launchpad.net/subiquity/+bug/2063331)). This can be fixed by removing the extra interfaces from `/etc/netplan/50-cloud-init.conf` or by marking them as `optional: true`. Cloud-init is disabled on systems installed from ISO images, so settings will persist.

:::{rubric} samba apparmor profile
:::

Due to [bug LP: #2063079](https://bugs.launchpad.net/ubuntu/+source/samba/+bug/2063079), the samba `smbd.service` unit file is no longer calling out to the helper script to dynamically create apparmor profile snippets according to the existing shares.

By default, the `smbd` service from samba is not confined. To be affected by this bug, users have to:

* install the optional `apparmor-profiles` package
* switch the `smbd` profile confinement from `complain` to `enforce`

Therefore, only users who have taken those steps and upgrade to Noble, will be affected by this bug. An SRU to fix it will be done shortly after release.

:::{rubric} Docker
:::

There is an AppArmor related bug where containers cannot be promptly stopped due to the recently added AppArmor profile for `runc`. The containers are always killed with `SIGKILL` due to the denials when trying to receive a signal. More details about this bug can be found [here](https://bugs.launchpad.net/ubuntu/+source/docker.io/+bug/2063099), and a workaround is described [here](https://bugs.launchpad.net/ubuntu/+source/docker.io/+bug/2063099/comments/4).

### Development issues

### Enterprise issues

### Cloud issues

:::{rubric} Microsoft Azure
:::

The current version of walinuxagent relies on python3-legacycrypt for password changing functionality but it cannot be made a dependency due to a component mismatch ([LP: #2106484](https://launchpad.net/bugs/2106484)).

### Security issues

### Hardware support issues

:::{rubric} Hardware requiring `nomodeset`
:::

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

:::{rubric} PPC64EL
:::

PMDK sees some hardware-specific failures in its test suite, which may make the software partially or fully inoperable on the ppc64el architecture. ([LP: #2061913](https://bugs.launchpad.net/ubuntu/+source/pmdk/+bug/2061913/))

:::{rubric} Raspberry Pi
:::

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

:::{rubric} TPM/FDE
:::

TPM/FDE installs seem to fail to boot after the installation is complete ([LP: #2104316](https://bugs.launchpad.net/snap-pc/+bug/2104316)). This is an issue with the *beta* image, and it is projected to be fixed by the plucky release.

:::{rubric} Netboot installs
:::

There is a bug ([LP: #2104316](https://bugs.launchpad.net/ubuntu-power-systems/+bug/2104297)) in the *beta* images that prevents netboot installs in some scenarios.

:::{rubric} cloud-init upgrade
:::

It has been reported that cloud-init may fail to upgrade properly in the Oracular to Pluck upgrade path, see [LP: #2104316](https://bugs.launchpad.net/ubuntu-power-systems/+bug/2104297).

:::{rubric} ZFS with cryptoswap
:::

ZFS with Encryption on Ubuntu 24.10 will [fail to activate the cryptoswap partition](https://bugs.launchpad.net/ubuntu/+source/subiquity/+bug/2084089).  This affects both new installs and upgrades.  We expect to address this post-release with an archive update.

:::{rubric} I/O scheduler
:::

A bug prevents the I/O scheduler from being reset to “none” ([LP: #2083845](https://bugs.launchpad.net/bugs/2083845)): the fix is already in Linux v6.11.2, and will be part of the first SRU kernel.

:::{rubric} FAN networking
:::

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
