---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/KarmicKoala/ReleaseNotes -->

(ubuntu-9-10-release-notes)=
# Ubuntu 9.10 release notes

These release notes document known issues with Ubuntu 9.10 and its variants.


(9-10-system-requirements)=
## System Requirements

The minimum memory requirement for Ubuntu 9.10 is 256 MB of memory. Note that some of your system's memory may be unavailable due to being used by the graphics card. If your computer has only the minimum amount of memory, the installation process will take longer than normal, but will complete successfully, and the system will perform adequately once installed.

Systems with less memory may be able to select "Install Ubuntu" from the boot menu to run just the installer, rather than the whole desktop, or may be able to use the alternate install CD.


(release-notes-for-ubuntu-9-10-for-arm)=
## Release notes for Ubuntu 9.10 for ARM

A separate page has been made available with release notes for the developer-oriented Ubuntu 9.10 armel port.  Please see [wiki.ubuntu.com/ARM/KarmicReleaseNotes](https://wiki.ubuntu.com/ARM/KarmicReleaseNotes) for information about issues impacting installation on ARM.


(9-10-installation)=
## Installation


(9-10-recommended-packages-installed-by-default)=
### Recommended packages installed by default

In accordance with the Debian Policy Manual (which says "The 'Recommends' field should list packages that would be found together with this one in all but unusual installations"), the package management system now installs packages listed in the Recommends: field of other installed packages as well as Depends: by default. If you want to avoid this for specific packages, use `apt-get --no-install-recommends`; if you want to make this permanent, set `APT::Install-Recommends "false";` in `/etc/apt/apt.conf`. Be aware that this may result in missing features in some programs.

(This change was made in Ubuntu 8.10.)


(9-10-hibernation-may-be-unavailable-with-automatic-partitioning)=
### Hibernation may be unavailable with automatic partitioning

The default partitioning recipe in the installer will in some cases allocate a swap partition that is smaller than the physical memory in the system.  This will prevent the use of hibernation (suspend-to-disk) because the system image will not fit in the swap partition.  If you intend to use hibernation with your system, you should ensure that the swap partition's size is at least as large as the system's physical RAM. (Bug:345126)


(9-10-package-list-must-be-manually-refreshed-before-installing-drivers)=
### Package list must be manually refreshed before installing drivers

The "Hardware Drivers" tool (Jockey) requires up to date package lists before it detects and advertises necessary driver packages. Immediately after a new installation, these package lists will not be present. Before running Jockey for the first time, update the package lists using `System->Administration->Software->Update Manager` (on Ubuntu) or "KPackageKit" (on Kubuntu). (Bug:462704)


(other-os-options-not-shown-in-boot-menu-when-installing-with-ubuntu-9-10-rc)=
### Other OS options not shown in boot menu when installing with Ubuntu 9.10 RC

After installation from the Ubuntu 9.10 Release Candidate, other installed operating systems are not correctly displayed in the boot menu.  To correct this, users should run `sudo update-grub` from the commandline after rebooting to their installed Ubuntu system.  This problem does not occur for installations from the final Ubuntu 9.10 release. (Bug:456776)


(9-10-automatic-boot-from-a-degraded-raid-array-not-configured-upon-installation)=
### Automatic boot from a degraded RAID array not configured upon installation

The installer option to support "boot from a degraded array" does not properly configure the installed system.  To correct this after installation, run `dpkg-reconfigure mdadm` after installation and select the option again. (Bug:462258)


(9-10-oem-prepare-for-shipping-icon-not-shown-in-kubuntu-netbook-edition)=
### OEM "prepare for shipping" icon not shown in Kubuntu Netbook Edition

When using the OEM installation option on Kubuntu Netbook Edition, no "prepare for shipping" icon is placed on the desktop.  Users who are doing OEM installations with Kubuntu Netbook Edition can access this feature under by choosing `System->Prepare for shipping ...` from the main bar. (Bug:386099)


(9-10-unr-install-confirmation-dialog-may-be-hidden)=
### UNR install confirmation dialog may be hidden

In some cases, the confirmation dialog at the end of a successful Ubuntu Netbook Remix installation will be hidden.  To reach the popup window prompting for reboot, you may click on it in the list of windows in the top panel or press Alt-Tab until you switch to it. (Bug:462178)


(9-10-wubi-using-persistent-storage-on-a-usb-disk)=
### Wubi using persistent storage on a USB disk

Users who wish to run Wubi from a USB disk that has persistent storage enabled will need to run it with the `--force-wubi` option from the Windows command line. (Bug:461566)


(9-10-no-installer-shortcut-in-ubuntu-moblin-remix-developer-preview)=
### No installer shortcut in Ubuntu Moblin Remix developer preview

The installer is not available as a shortcut on the welcome screen in the Ubuntu Moblin Remix developer preview.  To start the installation from a live session, open "Install Ubuntu" under Applications > Settings. (Bug:439656)


(9-10-installations-with-separate-boot-partition)=
### Installations with separate /boot partition

If there is a previously existing Ubuntu (or other Linux) installation and the
new one gets installed side by side (with e. g. using the "auto-resize"
option), the previous installation will not start from the boot menu. This is
due to wrong settings in the generated `/boot/grub/grub.cfg`.  A fix for this
issue will be provided in a post-release update immediately after the Ubuntu
9.10 release. (Bug:462961)


(9-10-dmraid-active-by-default-on-desktop-cd)=
### Dmraid active by default on Desktop CD

Dmraid "fake raid" devices are supported out-of-the-box on the Ubuntu 9.10 Desktop CD, and are detected and activated by dmraid on boot. Ubiquity will offer to install on the RAID array, and not on the RAID members.

The automatic activation of dmraid can be disabled with the "nodmraid" boot option, available by pressing F6 in the CD boot menu. This can be useful for setups which have fakeraid metadata present on the disks, but where dmraid activation would be undesired or cause problems.


(9-10-upgrading)=
## Upgrading

Users of Ubuntu 9.04 can upgrade to Ubuntu 9.10 by a convenient automated process. Users of older Ubuntu releases need to upgrade to Ubuntu 9.04 first, and then to 9.10. Complete instructions may be found at [www.ubuntu.com/getubuntu/upgrading](http://www.ubuntu.com/getubuntu/upgrading).

Kubuntu users can upgrade directly from Kubuntu 8.04 to Kubuntu 9.10.  Users upgrading in this way are advised to also read the [release notes for Ubuntu 8.10](http://www.ubuntu.com/getubuntu/releasenotes/810) and [for Ubuntu 9.04](http://www.ubuntu.com/getubuntu/releasenotes/904), as the issues described there will in most cases also apply.


(9-10-grub-menu-lst-install-the-maintainers-version-vs-keep-the-local-version)=
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


(9-10-setting-wireless-regulatory-domain-via-module-option-no-longer-supported)=
### Setting wireless regulatory domain via module option no longer supported

Ubuntu 9.10 enables the CRDA wireless regulatory framework for controlling which wireless channels are usable and visible in a particular location. If you previously had to use the module option similar to that below in /etc/modprobe.d/options.conf to allow access to certain channels in your locality then you may find that wireless will not function at all:

options cfg80211 ieee80211_regdom=EU

You should remove this kernel module option on upgrade to Ubuntu 9.10 and use the `iw reg` command instead.

(This change was made in Ubuntu 9.04.)


(9-10-bonded-network-interfaces-must-use-hotplug-style-configuration)=
### Bonded network interfaces must use hotplug-style configuration

The migration of network handling to upstart means that all network devices are now handled in a hotplug manner.  As a result, bonded interfaces are only brought up reliably on boot when the bonded interface is created as part of the configuration of the physical interface; otherwise, the system may attempt to bring up the bonded interface before the underlying physical interfaces are available, and fail.  For an example of how to configure a bonding interface for hotplug, please see `/usr/share/doc/ifenslave-2.6/examples/two_hotplug_ethernet` in the `ifenslave-2.6` package.


(9-10-upgrade-from-beta-must-be-triggered-manually)=
### Upgrade from beta must be triggered manually

A bug in the apt package included in the Ubuntu 9.10 Beta prevents automatic notification of available package updates.  Users who have installed or upgraded to Ubuntu 9.10 prior to the Release Candidate should ensure that updates are being made available by running `update-manager` manually, clicking `Check`, and installing the presented updates. (Bug:449535)


(9-10-x-server-crashes-when-using-a-wacom-tablet)=
### X server crashes when using a wacom tablet

The wacom driver in Ubuntu 9.10 supports automatic configuration, but it conflicts with manual device entries for wacom tablets in `/etc/X11/xorg.conf`, causing the X server to crash either on startup or shutdown. Please comment out or remove the entries from `xorg.conf` to get rid of the crashes. (Bug:358643)


(9-10-ubuntu-netbook-remix-missing-shutdown-applet-after-upgrade)=
### Ubuntu Netbook Remix missing shutdown applet after upgrade

After upgrading Ubuntu Netbook Remix, the shutdown applet may be absent from the top panel.  As a workaround, move the current applets to make some available space on the panel, then right-click in the freed space to add the "Indicator Applet Session" applet manually.  See Bug:461115 for detailed instructions.


(9-10-kubuntu-may-keep-unneeded-guidance-power-package)=
### Kubuntu may keep unneeded guidance power package

The kubuntu upgrade may leave the no longer needed packages "kde-guidance-powermanager" or "guidance-power-manager" installed. Those can be removed.


(9-10-ctrl-alt-backspace-disabled-by-default-in-xorg-configured-via-xkb)=
### Ctrl-Alt-Backspace disabled by default in Xorg, configured via XKB

Since Ubuntu 9.04, the Ctrl-Alt-Backspace key combination to force a restart of X is now disabled by default, to eliminate the problem of accidentally triggering the key combination.  In addition, the Ctrl-Alt-Backspace option is now configured as an X keymap (XKB) option, replacing the X server "DontZap" option and allowing per-user configuration of this setting.

As a result, enabling or disabling the Ctrl+Alt+Backspace shortcut can now be done easily from the desktop.


(9-10-enabling-ctrl-alt-backspace-for-ubuntu)=
#### Enabling Ctrl-Alt-Backspace for Ubuntu

* Select "System"->"Preferences"->"Keyboard"

* Select the "Layouts" tab and click on the "Layout Options" button.

* Select "Key sequence to kill the X server" and enable "Control + Alt + Backspace".


(9-10-enabling-ctrl-alt-backspace-for-kubuntu)=
#### Enabling Ctrl-Alt-Backspace for Kubuntu

* Click on the Application launcher and select "System Settings"

* Click on "Regional & Language".

* Select "Keyboard Layout".

* Click on "Enable keyboard layouts" (in the Layout tab).

* Select the "Advanced" tab. Then select "Key sequence to kill the X server" and enable "Control + Alt + Backspace".

For further information, see: [wiki.ubuntu.com/X/Config/DontZap](https://wiki.ubuntu.com/X/Config/DontZap)


(9-10-change-in-notifications-of-available-updates)=
### Change in notifications of available updates

Ubuntu 9.10 launches `update-manager` directly to handle package updates, instead of displaying a notification icon in the GNOME panel.  Users are notified of security updates on a daily basis, but for updates that are not security-related, users will only be prompted once a week.

Users who wish to continue receiving update notifications in the previous manner can restore the earlier behavior using the following command:

```none
gconftool -s --type bool /apps/update-notifier/auto_launch false
```

(This change was made in Ubuntu 9.04.)


(9-10-mysql-upgrade)=
### MySQL upgrade

In Ubuntu 9.10 MySQL 5.1 has been promoted as the default MySQL server. MySQL 5.0 is still available from the universe repository though. Performing an upgrade via update-manager will correctly handle the transition from MySQL 5.0 to MySQL 5.1. However using a dist-upgrade will not: mysql-server-5.0 will be upgraded instead of being replaced by mysql-server-5.1. If MySQL 5.0 needs to be kept the **mysql-server** and **mysql-client** packages should be removed before the upgrade is started.


(9-10-mysql-cluster-setup)=
#### MySQL Cluster setup

If MySQL has been setup to use the MySQL Cluster engine (NDB engine) upgrade to MySQL 5.1 will **not** work since the mysql-dfsg-5.1 packages don't support MySQL Cluster. Instead **mysql-server** and **mysql-client** should be removed before upgrade and mysql-server-5.0 should be kept. update-manager will automatically take care of this situation. Note that MySQL 5.0 is in universe and thus won't have have the same maintenance coverage as MySQL 5.1 (which is in main).


(9-10-etc-event-d-no-longer-used)=
### /etc/event.d no longer used

The version of `upstart` included in Ubuntu 9.10 no longer uses the configuration files in the `/etc/event.d` directory, looking to `/etc/init` instead.  No automatic migration of changes to `/etc/event.d` is possible.  If you have modified any settings in this directory, you will need to reapply them to `/etc/init` in the new configuration format by hand. (Bug:402759)


(9-10-syslog-upgrade)=
### Syslog upgrade

The `sysklogd` package has been replaced with `rsyslog`.  Configurations in `/etc/syslog.conf` will be automatically converted to `/etc/rsyslog.d/50-default`.  If you modified the log rotation settings in `/etc/cron.daily/sysklogd` or `/etc/cron.weekly/sysklogd`, you will need to change the new configurations in `/etc/logrotate.d/rsyslog`.  Also note that the prior rotation configurations used `.0` as the first rotated file extension, and now via logrotate it will be `.1`.


(9-10-eucalyptus-1-5-snapshots-not-preserved-on-upgrade-to-1-6)=
### Eucalyptus 1.5 snapshots not preserved on upgrade to 1.6

If a system running Ubuntu Enterprise Cloud on Ubuntu 9.04 is upgraded to Ubuntu 9.10, any existing snapshots will be unavailable after upgrade. Users affected by this issue may wish to defer their upgrade until a complete migration guide from Ubuntu 9.04 to Ubuntu 9.10 is made available at [help.ubuntu.com/community/UEC](http://help.ubuntu.com/community/UEC) at a later time. (Bug:429781)


(9-10-other-known-issues)=
## Other known issues


(9-10-switching-to-ext4-requires-manually-updating-grub)=
### Switching to ext4 requires manually updating grub

If you choose to upgrade your `/` or `/boot` filesystem in place from ext2 or ext3 to ext4 (as documented on the [ext4 wiki](http://ext4.wiki.kernel.org/index.php/Ext4_Howto#Converting_an_ext3_filesystem_to_ext4)), then you _must_ also use the `grub-install` command after upgrading to Ubuntu 9.04 to reinstall your boot loader. If you do not do this, then the version of GRUB installed in your boot sector will not be able to read the kernel from the ext4 filesystem and your system will fail to boot.


(9-10-ubuntu-one-client-requires-post-install-upgrade)=
### Ubuntu One client requires post-install upgrade

A serious bug in the Ubuntu One client software included in Ubuntu 9.10 that could potentially result in loss of data has led to disabling file syncing access for this client version on the Ubuntu One servers as a precaution.  Users who see a "Capabilities Mismatch" error when trying to use Ubuntu One should install the post-release upgrade of the client that will be made available immediately after release, fixing the original bug and restoring file syncing access to the Ubuntu One servers.   Files are still available via the web interface at [one.ubuntu.com](http://one.ubuntu.com).

Contact syncing and tomboy syncing services are not affected by this issue.


(9-10-upstart-jobs-cannot-be-run-in-a-chroot)=
### Upstart jobs cannot be run in a chroot

Upstart jobs cannot be started in a chroot because upstart acts as a service supervisor, and processes within the chroot are unable to communicate with the upstart running outside of the chroot (Bug:430224).  This will cause some packages that have been converted to use upstart jobs instead of init scripts to fail to upgrade within a chroot.  Users are advised to configure their chroots with /sbin/initctl pointing to /bin/true, with the following commands run within the chroot:

```none
dpkg-divert --local --rename --add /sbin/initctl
ln -s /bin/true /sbin/initctl
```


(9-10-login-screen-presented-before-optional-filesystems-are-mounted)=
### Login screen presented before optional filesystems are mounted

With the new `upstart`-based boot process in Ubuntu 9.10, the X server will be started, and the login screen launched, as soon as the core filesystems are available.  This means that optional filesystems, mounted at locations not required for the system to boot, may not be mounted yet at login time, and may even fail to mount in the case of a filesystem check error.

Users who prefer the previous behavior of waiting for all filesystems to be mounted before launching the login screen can add the `bootwait` option to these filesystems in `/etc/fstab`. (Bug:439604)


(9-10-optional-encrypted-partitions-must-be-marked-bootwait-in-etc-fstab)=
### Optional encrypted partitions must be marked bootwait in /etc/fstab

In addition to the above, users who have configured any encrypted partitions in `/etc/crypttab` to start at boot time (i.e., not using the `noauto` option) should make sure that the filesystems on these volumes are listed in `/etc/fstab` if they are not mounted at a standard system mountpoint.  Failure to do this on a desktop system will lead to problems from the X server and `cryptsetup` trying to control the console at the same time.  At best, this will prevent the user from seeing the passphrase prompt; at worst it will also cause the X server to spin and consume 100% CPU. (Bug:430496)


(9-10-avahi-will-always-start-even-if-a-local-domain-is-present)=
### Avahi will always start even if a .local domain is present

The `avahi-daemon` package, which implements the mDNS "zeroconf" standard, formerly included a check to avoid running when a conflicting `.local` DNS domain is present, as it was reported that some ISPs advertise such a `.local` domain on their networks, leaving Ubuntu hosts unable to see names advertised on the local network (Bug:327362).  In Ubuntu 9.10, `avahi-daemon` is started regardless.

It is possible that this may cause other problems.  If your network is configured this way, you can disable mDNS using the following command:

```none
sudo stop avahi-daemon
sudo sed -e '/^start/,+1s/^/#/' /etc/init/avahi-daemon.conf
```


(9-10-disabling-ralink-rt2860-wifi-on-eeepc-with-fn-f2-hotkey-causes-a-kernel-crash)=
### Disabling Ralink rt2860 wifi on EeePC with Fn+F2 hotkey causes a kernel crash

Using the Fn+F2 hotkey to disable the wireless antenna on an EeePC that uses a Ralink rt2860 chip (EeePC 900 and 1000 series) results in a kernel panic that will hang the system.  A fix for this issue is expected to be provided in a post-release update immediately after the Ubuntu 9.10 release. (Bug:404626)


(9-10-bison-webcam-in-msi-wind-netbook-causes-usb-errors-if-not-disabled)=
### bison webcam in MSI Wind netbook causes USB errors if not disabled

An error in the `uvcvideo` driver used for the bison webcam in certain MSI Wind and related netbooks causes USB support to fail, resulting in an inability to use USB devices or suspend/resume the netbook.  As a workaround, users can disable the camera before boot using the Fn+F6 hotkey. (Bug:435352)


(9-10-no-xv-support-for-intel-82852-855gm-video-chips-with-kms)=
### No Xv support for Intel 82852/855GM video chips with KMS

When using the default kernel-mode-setting (KMS) option in Ubuntu 9.10, users with Intel 82852/855GM cards will find that they are unable to use the Xv extension for playing videos.  This may show up as high CPU usage or stuttering during video playback, or a failure to play videos at all with some applications.  As a workaround, users can add the option `nomodeset` to the kernel boot options in the grub config (for GRUB 2: edit `/etc/default/grub` and add `nomodeset` to `GRUB_CMDLINE_LINUX`, then run `sudo update-grub`; for GRUB 1: edit `/boot/grub/menu.lst` and add `nomodeset` to the line beginning with `# kopt=`, then run `sudo update-grub`), to disable the use of KMS. (Bug:395932)


(9-10-brightness-flickering-on-msi-wind-netbooks-with-kms)=
### Brightness flickering on MSI Wind netbooks with KMS

A bug in the kernel-mode-setting (KMS) brightness handling on certain MSI Wind netbooks, including the U90, U100, and U120, results in a bad flickering effect whenever the brightness is changed on the desktop, as the brightness is repeatedly raised and then lowered.  Users affected by this issue can use the same workaround as described in the previous note to disable KMS. (Bug:415023)


(9-10-kubuntu-gui-package-manager-does-not-warn-about-installing-from-unsigned-package-repositories)=
### Kubuntu GUI package manager does not warn about installing from unsigned package repositories

The `kpackagekit` package manager used in Kubuntu 9.10 does not notify users if the packages they are installing come from repositories that are not secured with PGP.  Users who have unsigned package repositories in their `/etc/apt/sources.list` configuration and wish to be informed of any packages installed from these sources should use the `apt-get` commandline tool as a workaround. (Bug:256245)


(9-10-amarok-will-not-offer-to-download-additional-codecs-when-running-kubuntu-from-the-live-cd)=
### Amarok will not offer to download additional codecs when running Kubuntu from the live CD

When started from the live session, Amarok will not offer to download additional media codecs when needed, so, for example, it will be unable to play MP3 files. This will work normally after the system is installed to the hard disk. (Bug:362538)


(9-10-evince-pdf-viewer-does-not-work-for-nonstandard-home-directories)=
### Evince PDF viewer does not work for nonstandard home directories

Evince, the GNOME document viewer, now ships with an enforcing AppArmor profile. This greatly increases security by protecting users against flaws in the historically problematic PDF and image libraries. Users who use a non-standard location for their home directory will need to adjust the home tunable in /etc/apparmor.d/tunables/home. See [wiki.ubuntu.com/DebuggingApparmor#Adjusting%20Tunables](https://wiki.ubuntu.com/DebuggingApparmor#Adjusting%20Tunables) for details.


(9-10-uec-may-refuse-to-serve-the-first-requests-received-after-startup)=
### UEC may refuse to serve the first requests received after startup

On startup a UEC system may not process requests correctly, for instance returning "403 Forbidden" errors in response to some client requests. This is caused by a database deadlock condition which is automatically cleared after some retries.  To workaround this issue you can restart eucalyptus on the cluster controller by running "sudo restart eucalyptus" after boot. (Bug:444352)


(9-10-uec-node-controller-installation-failure-in-an-existing-uec)=
### UEC Node Controller installation failure in an existing UEC

Extending an existing Ubuntu Enterprise Cloud may fail during node controller installation started using the "Install Ubuntu Enterprise Cloud" option on the server CD. The node installation reports that the preseed file cannot be downloaded from the Cluster Controller, because the wrong IP address is used to connect to the Cluster Controller.

As a workaround for this issue, users can install a standard Ubuntu 9.10 server and then install the `eucalyptus-nc` package after reboot. Additionally, the system's primary ethernet interface will need to be configured as a bridge and the public ssh key of the Cloud Controller's eucalyptus user will need to be manually copied into the `authorized_keys` file of the Node Controller's eucalyptus user. More detailed instructions can be found in Step 3 of the UEC Package Install tutorial at [help.ubuntu.com/community/UEC/PackageInstall](https://help.ubuntu.com/community/UEC/PackageInstall). (Bug:458904)


(9-10-confirmation-emails-for-new-uec-users-not-sent)=
### Confirmation emails for new UEC users not sent

When a new user is created in the UEC admin interface, an email is sent to the user to confirm the registration.  A bug in the smtp configuration of UEC prevents the Cloud Controller from accepting and forwarding the confirmation email to the end user.  As a workaround, edit the postfix configuration file `/etc/postfix/main.cf` on the Cloud Controller to comment out the `mynetworks` option and add a `mynetworks_style` option set to `host` instead:

```none
  #mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
  mynetworks_style = host
```

Then reload postfix with `sudo service postfix reload`. (Bug:459101)


(9-10-uec-user-data-not-usable-by-guest-instances)=
### UEC user-data not usable by guest instances

When user data is passed to an instance started with `euca-run-instances` (using either the `-d`, `--user-data` option or the `-f`, `--user-data-file` option), the data returned at `http://169.254.169.254/latest/user-data` will be base64-encoded.  `ec2-init` is unable make use of this user data because it must be decoded before use.  A fix for this issue is expected to be provided in a post-release update immediately after the Ubuntu 9.10 release. (Bug:461156)


(9-10-ubuntu-8-04-lts-crashes-as-a-kvm-guest-when-using-virtio-networking)=
### Ubuntu 8.04 LTS crashes as a KVM guest when using virtio networking

Ubuntu 8.04 LTS using virtio networking as a KVM guest may crash when running on an Ubuntu 9.10 host.  As a workaround, such guests should use either e1000 or rtl839 as the networking model. A fix for the bug is currently in progress and will be included in an update to the qemu-kvm package in Karmic. (Bug:458521)


(windows-7-domain-member-fails-to-authenticate-to-ubuntu-9-10-samba-domain-controller)=
### Windows 7 domain member fails to authenticate to Ubuntu 9.10 Samba domain controller

After upgrading a Samba domain controller to Ubuntu 9.10, Windows 7 domain members will not be able to authenticate to it even if their registry settings were modified as outlined in [wiki.samba.org/index.php/Windows7](http://wiki.samba.org/index.php/Windows7) prior to joining the Samba domain.  A fix for this issue will be provided in a post-release update immediately after the Ubuntu 9.10 release. (Bug:462626)


(9-10-samba-nmbd-daemon-not-started-during-boot)=
### Samba nmbd daemon not started during boot

On an Ubuntu 9.10 system with Samba installed, the `nmbd` daemon may fail to start on boot.  To workaround this problem, restart the samba service once the system has finished booting by running `sudo service samba restart`. A fix for this issue will be provided in a post-release update. (Bug:462169)


(sparc-not-supported-by-ubuntu-9-10)=
### Sparc not supported by Ubuntu 9.10

The upstart init system in Ubuntu 9.10 fails to work on the sparc architecture due to an undiagnosed SIGBUS error.  Users of Ubuntu on sparc are advised to remain on Ubuntu 9.04 instead of upgrading to 9.10.  Assistance in resolving this architecture-specific bug for Ubuntu 10.04 is welcome. (Bug:436758)


(9-10-window-corruption-with-older-ati-graphics-cards)=
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

