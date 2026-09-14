---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/LucidLynx/ReleaseNotes -->

(ubuntu-10-04-lts-release-notes)=
# Ubuntu 10.04 LTS release notes

These release notes document known issues with Ubuntu 10.04 LTS and its variants.  **For the known open issues with the latest version, please see the [Change Log](https://wiki.ubuntu.com/LucidLynx/ReleaseNotes/ChangeSummary/10.04.4).**


(10-04-lts-system-requirements)=
## System Requirements

The minimum memory requirement for Ubuntu 10.04 LTS is 256 MB of memory. Note that some of your system's memory may be unavailable due to being used by the graphics card. If your computer has only the minimum amount of memory, the installation process will take longer than normal, but will complete successfully, and the system will perform adequately once installed.

Systems with less memory may be able to select "Install Ubuntu" from the boot menu to run just the installer, rather than the whole desktop, or may be able to use the alternate install CD.


(release-notes-for-ubuntu-10-04-for-arm)=
## Release notes for Ubuntu 10.04 for ARM

A separate page has been made available with release notes for the developer-oriented Ubuntu 10.04 armel port.  Please see [wiki.ubuntu.com/ARM/LucidReleaseNotes](https://wiki.ubuntu.com/ARM/LucidReleaseNotes) for information about issues affecting installation on ARM.


(10-04-lts-installation)=
## Installation


(10-04-lts-performance-regressions-with-ext4-under-certain-workloads)=
### Performance regressions with ext4 under certain workloads

The default file system for installations of Ubuntu 10.04 LTS is `ext4`, the latest version in the popular series of Linux extended file systems.  `ext4` includes a number of performance tuning changes relative to previous versions such as `ext3`, the file system used by default up to Ubuntu 9.04.  These generally produce improvements, but some particular workloads are known to be significantly slower when using `ext4` than when using `ext3`.  If you have performance-sensitive applications, we recommend that you run benchmarks using multiple file systems in your environment and select the most appropriate.

In particular, the `dpkg` package manager is known to run significantly slower on `ext4`, causing installations using the server or alternate install CD to take on the order of twice as long as before.  `ext4` does not guarantee atomic renames of new files over existing files in the event of a power failure shortly after the rename, and so `dpkg` needs to force the contents of the new file out to disk before renaming it in order to avoid leaving corrupt zero-length files after power failures.  This operation involves waiting for the disk significantly more than it strictly needs to, and so degrades performance.  If fast package management operations are most important to you, then you should use `ext3` instead.  (Bug:570805)

The simplest way to select a different file system such as `ext3` at installation time is to add the `partman/default_filesystem=ext3` boot parameter when starting the installer.  If you are deploying Ubuntu automatically using Kickstart or preseeding, then you can set a different file system in the partitioning recipe instead.


(10-04-lts-recommended-packages-installed-by-default)=
### Recommended packages installed by default

In accordance with the Debian Policy Manual (which says "The 'Recommends' field should list packages that would be found together with this one in all but unusual installations"), the package management system now installs packages listed in the Recommends: field of other installed packages as well as Depends: by default. If you want to avoid this for specific packages, use `apt-get --no-install-recommends`; if you want to make this permanent, set `APT::Install-Recommends "false";` in `/etc/apt/apt.conf`. Be aware that this may result in missing features in some programs.

(This change was made in Ubuntu 8.10.)


(10-04-lts-hibernation-may-be-unavailable-with-automatic-partitioning)=
### Hibernation may be unavailable with automatic partitioning

The default partitioning recipe in the installer will in some cases allocate a swap partition that is smaller than the physical memory in the system.  This will prevent the use of hibernation (suspend-to-disk) because the system image will not fit in the swap partition.  If you intend to use hibernation with your system, you should ensure that the swap partition's size is at least as large as the system's physical RAM. (Bug:345126)


(10-04-lts-i-o-error-after-cd-is-ejected-at-end-of-install)=
### I/O error after CD is ejected at end of install

In some cases, ejecting the CD at the end of installation will leave errors on the screen such as:

```none
end_request: I/O error, dev sr0, sector 437628
```

these error messages indicate that the system is still trying to access some files on the CD, and are harmless except that they obscure the message asking the user to press Enter to reboot.  You can safely remove the CD from the tray and press Enter at this point to reboot to your new Ubuntu system. (Bug:539027)


(10-04-lts-boot-options-hidden-by-default-on-desktop-and-netbook-cds)=
### Boot options hidden by default on Desktop and Netbook CDs

The Ubuntu 10.04 LTS Desktop and Netbook CDs feature a new boot interface that is noninteractive by default.  To configure advanced boot options, press any key at the first boot screen.


(10-04-lts-dmraid-active-by-default-on-desktop-cd)=
### Dmraid active by default on Desktop CD

Dmraid "fake raid" devices are supported out-of-the-box on the Ubuntu 10.04 LTS Desktop CD, and are detected and activated by dmraid on boot. Ubiquity will offer to install on the RAID array, and not on the RAID members.

The automatic activation of dmraid can be disabled with the "nodmraid" boot option, available by pressing F6 in the CD boot menu. This can be useful for setups which have fakeraid metadata present on the disks, but where dmraid activation would be undesired or cause problems.


(10-04-lts-partition-alignment-changes-may-break-some-systems)=
### Partition alignment changes may break some systems

By default, Ubuntu 10.04 LTS aligns partitions on disk to 1 MiB (1048576 bytes) boundaries.  This ensures maximum performance on many modern disks, particularly solid state drives but also new "Advanced Format" disks with physical sectors larger than the traditional 512 bytes.  Very few systems nowadays need the old alignment, used in the days of MS-DOS when it was useful for partitions to start at the beginning of a cylinder.

In some rare cases, optimal alignment may cause problems.  Some BIOS implementations (those on Asus P5P800-MX and Asus P5GZ-MX motherboards) have been reported to hang after installation.  It may be difficult to install Microsoft Windows XP and older after installing Ubuntu, although more recent versions of Windows should be compatible with optimal alignment and indeed may produce it themselves.  If you find that you need to use the old cylinder alignment instead, then add the `partman/alignment=cylinder` boot parameter when starting the installer. (Bug:551965)


(10-04-lts-desktop-installer-sometimes-crashes-on-startup)=
### Desktop installer sometimes crashes on startup

On some machines, the CD boot fails with the message "The installer encountered an unrecoverable error.  A desktop session will now be run so that you may investigate the problem or try installing again."  If you encounter this error, restart your computer with the CD inserted, press any key at the splash screen (when you see the keyboard icon at the bottom of the screen), and select "Try Ubuntu without installing".  Once the desktop appears, use the "Install Ubuntu 10.04" icon to begin installing Ubuntu.  (Bug:567899)


(10-04-lts-upgrading)=
## Upgrading

Users of Ubuntu 9.10 and Ubuntu 8.04 LTS can upgrade to Ubuntu 10.04 by a convenient automated process. Users of other Ubuntu releases need to upgrade first to either Ubuntu 8.04 LTS or Ubuntu 9.10, and then to 10.04. Complete instructions may be found at [www.ubuntu.com/getubuntu/upgrading](http://www.ubuntu.com/getubuntu/upgrading).


(10-04-lts-grub-menu-lst-install-the-maintainers-version-vs-keep-the-local-version)=
### GRUB menu.lst: install the maintainer's version vs. keep the local version

If you have previously modified the `menu.lst` bootloader configuration for GRUB, either by hand or with a tool such as `kgrubeditor`, you may be asked on upgrade whether you wish to keep your local version of the menu.lst or install the package maintainer's version.  This question is asked because such changes cannot be merged automatically with 100% reliability, and care is taken to not overwrite the user's manually edited bootloader configuration without warning.

However, if you choose to "keep the local version currently installed," your system will not be set up to boot from any newly-installed kernels.  **Manual action is required on your part to ensure that your system is running the current, security-supported kernel after upgrade.**  If you have local changes to your bootloader config that you want to keep, it is recommended that you follow these steps:

* Choose "keep the local version currently installed" at the prompt.

* Open `/boot/grub/menu.lst` with a text editor (e.g., `sudo gedit /boot/grub/menu.lst`).

* Apply any changes you've made to the kernel boot options to the commented variables (e.g., `groot`, `kopt`, `defoptions`) above.

* Move any manually-added boot options for other operating systems so that they are above the line

```none
### BEGIN AUTOMAGIC KERNELS LIST

```

or below the line

```none
### END DEBIAN AUTOMAGIC KERNELS LIST

```

* Save the file, and run `sudo update-grub` from the commandline.
* Choose "install the package maintainer's version".

For example, if you added an option `i915.modeset=0` to the "kernel" line:

```none
kernel          /vmlinuz-2.6.31-14-generic root=UUID=0e7... ro quiet splash i915.modeset=0
```

then add this option to `kopt`:

```none
# kopt=root=UUID=0e7... ro i915.modeset=0

```

An updated version of the `grub` package will include information about this problem in the help screen for the `menu.lst` prompt. (Bug:470490)


(10-04-lts-setting-wireless-regulatory-domain-via-module-option-no-longer-supported)=
### Setting wireless regulatory domain via module option no longer supported

Ubuntu 10.04 LTS enables the CRDA wireless regulatory framework for controlling which wireless channels are usable and visible in a particular location. If you previously had to use the module option similar to that below in `/etc/modprobe.d/options.conf` to allow access to certain channels in your locality then you may find that wireless will not function at all:

options cfg80211 ieee80211_regdom=EU

You should remove this kernel module option on upgrade from releases earlier than Ubuntu 9.04 and use the `iw reg` command instead.

(This change was made in Ubuntu 9.04.)


(10-04-lts-bonded-network-interfaces-must-use-hotplug-style-configuration)=
### Bonded network interfaces must use hotplug-style configuration

The migration of network handling to upstart means that all network devices are now handled in a hotplug manner.  As a result, bonded interfaces are only brought up reliably on boot when the bonded interface is created as part of the configuration of the physical interface; otherwise, the system may attempt to bring up the bonded interface before the underlying physical interfaces are available, and fail.  For an example of how to configure a bonding interface for hotplug, please see `/usr/share/doc/ifenslave-2.6/examples/two_hotplug_ethernet` in the `ifenslave-2.6` package.

(This change was made in Ubuntu 9.10.)


(10-04-lts-kubuntu-may-keep-unneeded-guidance-power-package)=
### Kubuntu may keep unneeded guidance power package

The kubuntu upgrade may leave the no longer needed packages "kde-guidance-powermanager" or "guidance-power-manager" installed. Those can be removed.


(10-04-lts-kubuntus-akonadi-may-need-restarting)=
### Kubuntu's Akonadi may need restarting

Akonadi startup is sometimes faulty preventing access to the address book and other resources.  To work around this, close and restart Kontact. (Bug:564263)


(10-04-lts-ctrl-alt-backspace-disabled-by-default-in-xorg-configured-via-xkb)=
### Ctrl-Alt-Backspace disabled by default in Xorg, configured via XKB

Since Ubuntu 9.04, the Ctrl-Alt-Backspace key combination to force a restart of X is now disabled by default, to eliminate the problem of accidentally triggering the key combination.  In addition, the Ctrl-Alt-Backspace option is now configured as an X keymap (XKB) option, replacing the X server "DontZap" option and allowing per-user configuration of this setting.

As a result, enabling or disabling the Ctrl+Alt+Backspace shortcut can now be done easily from the desktop.


(10-04-lts-enabling-ctrl-alt-backspace-for-ubuntu)=
#### Enabling Ctrl-Alt-Backspace for Ubuntu

* Select "System"->"Preferences"->"Keyboard"

* Select the "Layouts" tab and click on the "Layout Options" button.

* Select "Key sequence to kill the X server" and enable "Control + Alt + Backspace".


(10-04-lts-enabling-ctrl-alt-backspace-for-kubuntu)=
#### Enabling Ctrl-Alt-Backspace for Kubuntu

* Click on the Application launcher and select "System Settings"

* Click on "Regional & Language".

* Select "Keyboard Layout".

* Click on "Enable keyboard layouts" (in the Layout tab).

* Select the "Advanced" tab. Then select "Key sequence to kill the X server" and enable "Control + Alt + Backspace".

For further information, see: [wiki.ubuntu.com/X/Config/DontZap](https://wiki.ubuntu.com/X/Config/DontZap)


(10-04-lts-change-in-notifications-of-available-updates)=
### Change in notifications of available updates

Ubuntu 10.04 LTS launches `update-manager` directly to handle package updates, instead of displaying a notification icon in the GNOME panel.  Users are notified of security updates on a daily basis, but for updates that are not security-related, users will only be prompted once a week.

Users who wish to continue receiving update notifications in the previous manner can restore the earlier behavior using the following command:

```none
gconftool -s --type bool /apps/update-notifier/auto_launch false
```

(This change was made in Ubuntu 9.04.)


(10-04-lts-gdm-does-not-support-xdmcp)=
### GDM does not support XDMCP

The version of `gdm` included in Ubuntu 10.04 LTS does not support the XDMCP protocol for remote graphical logins.  Users who require XDMCP support will need to install another display manager, such as `wdm` or `xdm`, for this functionality. (Bug:408417)


(10-04-lts-mysql-upgrade)=
### MySQL upgrade

In Ubuntu 10.04 LTS, MySQL 5.1 is the only version of MySQL available. Performing an upgrade via update-manager will correctly handle the transition from MySQL 5.0 to MySQL 5.1.


(10-04-lts-mysql-cluster-setup)=
#### MySQL Cluster setup

If MySQL has been set up to use the MySQL Cluster engine (NDB engine), upgrading to MySQL 5.1 will **not** work since the mysql-dfsg-5.1 packages don't support MySQL Cluster. Instead the **mysql-cluster-server** package should be installed.


(10-04-lts-etc-event-d-no-longer-used)=
### /etc/event.d no longer used

The version of `upstart` included in Ubuntu 10.04 LTS no longer uses the configuration files in the `/etc/event.d` directory, looking to `/etc/init` instead.  No automatic migration of changes to `/etc/event.d` is possible.  If you have modified any settings in this directory, you will need to reapply them to `/etc/init` in the new configuration format by hand. (Bug:402759)

(This change was made in Ubuntu 9.10.)


(10-04-lts-syslog-upgrade)=
### Syslog upgrade

The `sysklogd` package has been replaced with `rsyslog`.  Configurations in `/etc/syslog.conf` will be automatically migrated to `/etc/rsyslog.d/50-default`.  If you modified the log rotation settings in `/etc/cron.daily/sysklogd` or `/etc/cron.weekly/sysklogd`, you will need to change the new configurations in `/etc/logrotate.d/rsyslog`.  Also note that the prior rotation configurations used `.0` as the first rotated file extension, and now with logrotate it will be `.1`.

(This change was made in Ubuntu 9.10.)


(10-04-lts-openoffice-org-registry-may-be-corrupted-on-upgrade-from-version-3-1-1-14)=
### OpenOffice.org registry may be corrupted on upgrade from version 3.1.1-14

Users who had installed pre-release versions of Ubuntu 9.10 may have corrupted OpenOffice.org service or component registry files on their system as a result of a bug in version 1:3.1.1-14 of the OpenOffice.org packages.  If you experience segfaults in either `unopkg` or OpenOffice.org after upgrade, you may need to remove and regenerate the registry files in `/var/lib/openoffice/basis3.2/program/` and `/var/spool/openoffice/uno_packages/cache`. (Bug:546797)


(10-04-lts-lpia-architecture-discontinued)=
### LPIA architecture discontinued

The `lpia` architecture present in previous releases has been discontinued as of Ubuntu 10.04 LTS.  The hardware is still supported, but systems that were installed as `lpia` will need to be backed up and reinstalled from scratch using either the `i386` or `amd64` architectures.  See [bug 523295](https://bugs.launchpad.net/bugs/523295), which includes an unsupported method for migration from `lpia` to `i386`.


(10-04-lts-dovecot-cmusieve-plugin-renamed-to-sieve)=
### Dovecot cmusieve plugin renamed to sieve

The "cmusieve" plugin used in dovecot has been renamed to "sieve".  Users who have the following set in their dovecot configuration:

```none
	mail_plugins = cmusieve
```

should change this to:

```none
	mail_plugins = sieve
```


(10-04-lts-other-known-issues)=
## Other known issues


(10-04-lts-security-issue-when-upgrading-from-lucid-alpha-2)=
### Security Issue when upgrading from Lucid Alpha 2

If you installed Lucid prior to Alpha 3, you may have `libmysqlclient16` 7.0.9-1 installed.  This package was present in the Ubuntu archive by mistake and was retracted, but because it has a later version number than the real `libmysqlclient16` package, the real package will not be installed automatically on upgrade.  To ensure that you have the official package installed on your Lucid system and will receive security support for it throughout Ubuntu 10.04 LTS, it is important that you run `sudo apt-get install libmysqlclient16/lucid` and follow the instructions. (Bug:522225)


(10-04-lts-switching-to-ext4-requires-manually-updating-grub)=
### Switching to ext4 requires manually updating grub

If you choose to upgrade your `/` or `/boot` filesystem in place from ext2 or ext3 to ext4 (as documented on the [ext4 wiki](http://ext4.wiki.kernel.org/index.php/Ext4_Howto#Converting_an_ext3_filesystem_to_ext4)), then you _must_ also use the `grub-install` command after upgrading to Ubuntu 10.04 LTS to reinstall your boot loader. If you do not do this, then the version of GRUB installed in your boot sector will not be able to read the kernel from the ext4 filesystem and your system will fail to boot.


(10-04-lts-upstart-jobs-cannot-be-run-in-a-chroot)=
### Upstart jobs cannot be run in a chroot

Upstart jobs cannot be started in a chroot because upstart acts as a service supervisor, and processes within the chroot are unable to communicate with the upstart running outside of the chroot (Bug:430224).  This will cause some packages that have been converted to use upstart jobs instead of init scripts to fail to upgrade within a chroot.  Users are advised to configure their chroots with /sbin/initctl pointing to /bin/true, with the following commands run within the chroot:

```none
dpkg-divert --local --rename --add /sbin/initctl
ln -s /bin/true /sbin/initctl
```


(10-04-lts-use-of-degraded-raid-1-array-may-cause-data-loss-in-exceptional-cases)=
### Use of degraded RAID 1 array may cause data loss in exceptional cases

If each member of a RAID 1 array is separately brought up in degraded mode across subsequent runs of the array with no reassembly in between, there is a risk that the disks will be reported as in sync when they are not, resulting in data loss due to inconsistencies between the data that has been written to each member. This is an unlikely occurrence during normal operations, but admins of systems using RAID 1 arrays should take care during maintenance to avoid this situation. (Bug:557429)


(10-04-lts-encrypted-partitions-must-be-listed-in-etc-fstab)=
### Encrypted partitions must be listed in /etc/fstab

Users who have configured any encrypted partitions in `/etc/crypttab` to start at boot time (i.e., not using the `noauto` option) should make sure that the filesystems on these volumes are listed in `/etc/fstab`.  Otherwise, the passphrase prompt is not guaranteed to be displayed at boot time.


(10-04-lts-lvm-filesystems-should-be-listed-in-etc-fstab-by-name)=
### LVM filesystems should be listed in /etc/fstab by name

In general, filesystems are listed in `/etc/fstab` by UUID rather than by device name, to ensure that the filesystem can always be found reliably.  If you are mounting a filesystem located on LVM, however, it is recommended that you list them in `/etc/fstab` by device name, not by UUID, because UUIDs are not unique if LVM snapshots are used, which can result in wrong filesystems being mounted at boot. (Bug:563902)


(10-04-lts-boot-failures-with-lvm-on-ia64-powerpc-sparc)=
### Boot failures with LVM on ia64, powerpc, sparc

The linux kernel packages for the ia64, powerpc, and sparc architectures builds device-mapper support as a module, where the packages for the other architectures have the driver built in, which leads to boot failures on ia64/powerpc/sparc when using LVM.  To work around this, users must run these commands manually from the initramfs:

```none
modprobe dm_mod
lvm vgchange -a y
```

This issue will be addressed in a post-release kernel update. (Bug:560717)


(10-04-lts-avahi-will-always-start-even-if-a-local-domain-is-present)=
### Avahi will always start even if a .local domain is present

The `avahi-daemon` package, which implements the mDNS "zeroconf" standard, formerly included a check to avoid running when a conflicting `.local` DNS domain is present, as it was reported that some ISPs advertise such a `.local` domain on their networks, leaving Ubuntu hosts unable to see names advertised on the local network (Bug:327362).  In Ubuntu 9.10, `avahi-daemon` is started regardless.

It is possible that this may cause other problems.  If your network is configured this way, you can disable mDNS using the following command:

```none
sudo stop avahi-daemon
sudo sed -e '/^start/,+1s/^/#/' /etc/init/avahi-daemon.conf
```


(10-04-lts-working-around-bugs-in-the-new-kernel-video-architecture)=
### Working around bugs in the new kernel video architecture

Ubuntu 10.04 LTS enables the new kernel-mode-setting (KMS) technology by default on most common video chipsets.  While this is a major step forward for the graphics architecture in Ubuntu, in some rare cases KMS will prevent your video output from working correctly, or from working at all.  If you need to disable KMS, you can do so by booting with the `nomodeset` option.  You can also save this setting so that it's applied at every boot by adding it to your grub config (for GRUB 2: edit `/etc/default/grub` and add `nomodeset` to `GRUB_CMDLINE_LINUX`, then run `sudo update-grub`; for GRUB 1: edit `/boot/grub/menu.lst` and add `nomodeset` to the line beginning with `# kopt=`, then run `sudo update-grub`).  (Bug:533784, Bug:541501)


(10-04-lts-evince-pdf-viewer-does-not-work-for-nonstandard-home-directories)=
### Evince PDF viewer does not work for nonstandard home directories

Evince, the GNOME document viewer, now ships with an enforcing AppArmor profile. This greatly increases security by protecting users against flaws in the historically problematic PDF and image libraries. Users who use a non-standard location for their home directory will need to adjust the home tunable in /etc/apparmor.d/tunables/home. See [wiki.ubuntu.com/DebuggingApparmor#Adjusting%20Tunables](https://wiki.ubuntu.com/DebuggingApparmor#Adjusting%20Tunables) for details.


(10-04-lts-no-delay-for-boot-menu-with-grub-2)=
### No delay for boot menu with GRUB 2

When using the GRUB 2 bootloader included in Ubuntu 10.04 LTS, the first boot option will by default be loaded automatically without pausing for user input.  To interrupt the boot, users can hold down the Shift key to bring up the boot menu, allowing them to select a different boot option or to configure kernel arguments. (https://help.ubuntu.com/community/Grub2#GRUB%20vs%20GRUB%202)


(10-04-lts-changes-in-boot-time-output-on-ubuntu-server)=
### Changes in boot-time output on Ubuntu Server

With the introduction of plymouth, boot-time messages from startup scripts are no longer displayed above the login prompt on tty1.  Instead, they are all output to tty7 and on Ubuntu Server, can be viewed after boot by pressing Alt+F7.  On all systems the boot output can also be found in `/var/log/boot.log`.

On new installs of Ubuntu 10.04 LTS Server, no boot splash screen is shown by default.  While this provides server administrators with more immediate feedback about their system while booting, it also prevents prompts from reaching the user in the event of filesystem mounting failures.  Users can add the `splash` option to `/etc/default/grub` if they prefer to always see the splash screen. Hotkeys for interacting with `mountall` will still work without the splash screen, but are not discoverable: `C` to cancel a running fsck; `M` to request a maintenance shell; `S` to skip an unavailable mount; and `F` to try to fix errors found by a fsck. (Bug:563916)


(10-04-lts-nss-resolution-breaks-with-ldap-over-ssl-in-ubuntu-server)=
### NSS resolution breaks with LDAP over SSL in Ubuntu Server

Upgrading systems configured to use LDAP via SSL as the first service in the NSS stack (in /etc/nsswitch.conf) leads to broken NSS resolution afterwards such that `setuid` applications like `sudo` would stop working.  To work around this, switch to the libnss-ldapd package instead of libnss-ldap before the upgrade, or use nscd. (Bug:423252)


(10-04-lts-openldap-may-fail-to-start-on-upgrade)=
### OpenLDAP may fail to start on upgrade

When upgrading some systems from Karmic or pre-release versions of Lucid, OpenLDAP may fail to start by logging messages similar to "ordered_value_sort failed on attr olcAccess#012". To workaround the problem remove the line "olcAccess: to _ by dn.exact=cn=localroot,cn=config manage by _ break" from /etc/ldap/slapd.d/cn=config/olcDatabase={-1}frontend.ldif and /etc/ldap/slapd./cn=config/olcDatabase={0}config.ldif. An update fixing this automatically should be available soon after release. (Bug:571057)


(10-04-lts-sun-java-moved-to-the-partner-repository)=
### Sun Java moved to the Partner repository

For Ubuntu 10.04 LTS, the `sun-java6` packages have been dropped from the Multiverse section of the Ubuntu archive. It is recommended that you use `openjdk-6` instead.

If you can not switch from the proprietary Sun JDK/JRE to OpenJDK, you can install `sun-java6` packages from the Canonical Partner Repository. You can configure your system to use this repository via command-line:

```none
     sudo add-apt-repository "deb http://archive.canonical.com/ lucid partner"
     sudo apt-get update
     sudo apt-get install sun-java6-jre sun-java6-plugin
     sudo update-alternatives --config java
```

For Ubuntu 10.10, the `sun-java6` packages have been dropped from the Multiverse section of the Ubuntu archive. It is recommended that you use `openjdk-6` instead.

If you can not switch from the proprietary Sun JDK/JRE to OpenJDK, you can install `sun-java6` packages from the Canonical Partner Repository. You can configure your system to use this repository via command-line:

```none
     sudo add-apt-repository "deb http://archive.canonical.com/ maverick partner"
     sudo apt-get update
     sudo apt-get install sun-java6-jre sun-java6-plugin
     sudo update-alternatives --config java
```


(10-04-lts-window-corruption-with-older-ati-graphics-cards)=
### Window corruption with older ATI graphics cards

With older ATI graphics cards with 32MB or less of video RAM some corruption of direct rendered windows, for example OSD notifier windows, might appear. This may be worked around by disabling 'RenderAccel' in the Xorg configuration.  (Bug:426582)

To do this first exit to the console using the following command:

```none
sudo service gdm stop
```

Then create an Xorg configuration file with the command below:

```none
sudo Xorg -configure
```

Then add the 'RenderAccel' option to `/etc/X11/xorg.conf`:

```none
Section "Device"
        ...
        Driver "radeon"
        Option "RenderAccel" "off"
EndSection
```

And restart X/GDM.

```none
sudo service gdm start
```


(10-04-lts-incompatibility-with-nvidia-upstream-driver-installer)=
### Incompatibility with nVidia upstream driver installer

Ubuntu 10.04 LTS includes improved integration for nVidia binary driver packages.  Unfortunately, this comes at the expense of compatibility with the installer provided upstream on the nVidia website.  Users who wish to use the nVidia binary video drivers with 10.04 LTS should install them using the Ubuntu packages, as made available under `System -> Administration -> Hardware Drivers`.


(10-04-lts-intel-8xx-x-freezes-crashes)=
### Intel 8xx X freezes/crashes

The -intel driver fails with X freezes or crashes on certain i8xx hardware. The issue is known upstream but solutions are still under development. For now, to work around the issue, boot with the -vesa video driver. See [wiki.ubuntu.com/X/Bugs/Lucidi8xxFreezes](http://wiki.ubuntu.com/X/Bugs/Lucidi8xxFreezes) for further details.


(10-04-lts-abiword-freezes-when-accessing-help-documentation)=
### AbiWord freezes when accessing help documentation

A bug in the AbiWord package in Xubuntu 10.04 causes the application to hang whenever accessing the help interface, either from the menu or by pressing F1.  Users of Xubuntu should upgrade to version 2.8.2-2ubuntu1.1 of AbiWord in the `lucid-updates` repository to get the fix for this issue. (Bug:519541)


(10-04-lts-bootstrapping-on-old-kernels)=
### Bootstrapping on old kernels

Ubuntu 10.04 LTS cannot currently be bootstrapped (using `debootstrap`) on a system running a kernel prior to 2.6.22, due to a bug in tar and the inability of `debootstrap` to use the fix in `lucid-updates`. (Bug:539814)
