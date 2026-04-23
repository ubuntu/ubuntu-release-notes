---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/JauntyJackalope/ReleaseNotes -->

(ubuntu-9-04-release-notes)=
# Ubuntu 9.04 release notes

These release notes document known issues with Ubuntu 9.04 and its variants.


(9-04-system-requirements)=
## System Requirements

The minimum memory requirement for Ubuntu 9.04 is 256 MB of memory. Note that some of your system's memory may be unavailable due to being used by the graphics card. If your computer has only the minimum amount of memory, the installation process will take longer than normal, but will complete successfully, and the system will perform adequately once installed.

Systems with less memory may be able to select "Install Ubuntu" from the boot menu to run just the installer, rather than the whole desktop, or may be able to use the alternate install CD.


(9-04-installation)=
## Installation


(9-04-recommended-packages-installed-by-default)=
### Recommended packages installed by default

In accordance with the Debian Policy Manual (which says "The 'Recommends' field should list packages that would be found together with this one in all but unusual installations"), the package management system now installs packages listed in the Recommends: field of other installed packages as well as Depends: by default. If you want to avoid this for specific packages, use `apt-get --no-install-recommends`; if you want to make this permanent, set `APT::Install-Recommends "false";` in `/etc/apt/apt.conf`. Be aware that this may result in missing features in some programs.

(This change was made in Ubuntu 8.10.)


(9-04-wrong-display-when-installing-to-largest-continuous-free-space-on-disk)=
### Wrong display when installing to largest continuous free space on disk

When both the "Install them side by side" and the "Use the largest continuous free space" options are present, the "Use the largest continuous free space" option will display the wrong information in the partition bar that shows what the disk will look like after installation. However, selecting this option will correctly install Ubuntu into the largest empty partition. (Bug:364181)


(9-04-hibernation-may-be-unavailable-with-automatic-partitioning)=
### Hibernation may be unavailable with automatic partitioning

The default partitioning recipe in the installer will in some cases allocate a swap partition that is smaller than the physical memory in the system.  This will prevent the use of hibernation (suspend-to-disk) because the system image will not fit in the swap partition.  If you intend to use hibernation with your system, you should ensure that the swap partition's size is at least as large as the system's physical RAM.


(9-04-suggests-removing-boot-medium-after-installing-on-arm-based-babbage-boards)=
### Suggests removing boot medium after installing on ARM-based Babbage boards

On the ARM-based Babbage board, the installation medium (an SD card) is reused as the boot medium after installation. When restarting the system at the end of installation, you will be prompted to remove the installation medium. This message is incorrect, and you should leave the SD card in place in order to be able to start the installed system. (Bug:364273)


(9-04-upgrading)=
## Upgrading

Users of Ubuntu 8.10 can upgrade to Ubuntu 9.04 by a convenient automated process. Users of older Ubuntu releases need to upgrade to Ubuntu 8.10 first, and then to 9.04. Complete instructions may be found at [www.ubuntu.com/getubuntu/upgrading](http://www.ubuntu.com/getubuntu/upgrading).

Kubuntu users can upgrade directly from Kubuntu 8.04 to Kubuntu 9.04.  Users upgrading in this way are advised to also read the [release notes for Ubuntu 8.10](http://www.ubuntu.com/getubuntu/releasenotes/810), as the issues described there will also apply.


(9-04-boot-failures-on-systems-with-intel-d945-motherboards)=
### Boot failures on systems with Intel D945 motherboards

Users have reported slower than normal detection of SATA hard drives on systems with Intel D945 motherboards in Ubuntu 9.04.  This may cause the system to drop to a busybox initramfs shell on boot with a "Gave up waiting for root device." error. Wait a minute or two and then exit the initramfs shell by typing 'exit'. Booting should proceed normally. If it doesn't, wait a bit longer and try again. Once the system boots, edit `/boot/grub/menu.lst` and add `rootdelay=90` to the kernel stanza for your current kernel. (Bug:290153)


(9-04-upgrades-from-beta-may-use-label-in-etc-fstab)=
### Upgrades from beta may use LABEL= in /etc/fstab

Systems installed using Jaunty Alpha 5, Jaunty Alpha 6, or the Ubuntu 9.04 beta may use `LABEL=` syntax in `/etc/fstab` to identify file systems. This may cause unexpected behaviour later if another disk (such as a USB drive) is added later containing file systems with clashing labels. Unless you are sure that this is what you intend, we recommend that you switch to using universally unique identifiers (UUIDs) instead.

For example, if a file system is identified as `LABEL=home` in `/etc/fstab`, you can find the UUID as follows:

```none
blkid -o value -s UUID -l -t LABEL=home
```

You can then replace `LABEL=home` with `UUID=output`, where `output` is the output of blkid.

Systems installed using the release candidate or final release of Ubuntu 9.04 do not have this problem.


(python-importerror-with-systems-upgraded-before-ubuntu-9-04-release-candidate)=
### python ImportError with systems upgraded before Ubuntu 9.04 release candidate

A bug in the python packages present in jaunty prior to the Ubuntu 9.04 release candidate caused python modules to fail to be registered for use with the current python version, python 2.6.  This problem appears as an import error, e.g:

```none
ImportError: No module named foo
```

even though the package providing the module foo is installed.

To correct this, run the command:

```none
sudo dpkg-reconfigure python-foo
```

for each `python-foo` package providing an affected module.


(9-04-upgrades-from-alphas-may-need-re-encryption-of-encrypted-home-directories)=
### Upgrades from alphas may need re-encryption of encrypted home directories

Users who were running eCryptfs on the Jaunty Alpha milestones are advised to re-encrypt any encrypted files. An upstream 2.6.28 kernel bug caused random kernel memory to be written to eCryptfs encrypted file headers. The fix has been applied and deployed to Ubuntu users in the Ubuntu 9.04 release candidate. After upgrading to Ubuntu 9.04, eCryptfs users should re-encrypt each encrypted file using /usr/bin/ecryptfs-rewrite-file. For more information, please see [ecryptfs-rewrite-file(1)](http://manpages.ubuntu.com/manpages/jaunty/en/man1/ecryptfs-rewrite-file.1.html). (Bug:345544)


(9-04-upgrades-from-8-10-users-with-encrypted-private-directories)=
### Upgrades from 8.10 Users with Encrypted Private Directories

Users of 8.10 with Encrypted Private Directories should **not** use the LiveCD to do the upgrade.  These users **will experience** Bug:361627.  These users should use [update-manager to perform a network upgrade](http://www.ubuntu.com/getubuntu/upgrading).


(9-04-upgrades-from-ubuntu-8-10-may-have-lilo-installed)=
### Upgrades from Ubuntu 8.10 may have lilo installed

Ubuntu 8.10 systems installed from the desktop CD mistakenly had the `lilo` package installed as well as `grub`, although `grub` was used for booting. If you use the recommended Update Manager upgrade method, then the `lilo` package will be removed if it does not appear to be used. If you upgrade using some other method and are sure that you only use the GRUB boot loader, then we recommend that you remove the `lilo` package manually. [Bug 314004](https://bugs.launchpad.net/bugs/314004)


(9-04-setting-wireless-regulatory-domain-via-module-option-no-longer-supported)=
### Setting wireless regulatory domain via module option no longer supported

Ubuntu 9.04 enables the CRDA wireless regulatory framework for controlling which wireless channels are usable and visible in a particular location. If you previously had to use the module option similar to that below in /etc/modprobe.d/options to allow access to certain channels in your locality then you may find that wireless will not function at all:

options cfg80211 ieee80211_regdom=EU

You should remove this kernel module option on upgrade to Ubuntu 9.04 and use the `iw reg` command instead.


(9-04-network-management-applet-must-be-re-added-on-kubuntu-upgrade)=
### Network management applet must be re-added on Kubuntu upgrade

When upgrading from Kubuntu 8.10, the new Network Management applet will need to be added to the panel manually.  (Bug:349066)

<!-- Image: plasma-1.png --> <!-- Image: plasma-2.png --> <!-- Image: plasma-3.png -->
Click the Plasma icon in the bottom right.  Click Add Widget. Double click on Network Management.


(9-04-x-server-crashes-when-using-a-wacom-tablet)=
### X server crashes when using a wacom tablet

The wacom driver in Ubuntu 9.04 supports automatic configuration, but it conflicts with manual device entries for wacom tablets in `/etc/X11/xorg.conf`, causing the X server to crash either on startup or shutdown. Please comment out or remove the entries from `xorg.conf` to get rid of the crashes. (Bug:358643)


(9-04-kubuntu-network-management-applet-does-not-connect-to-wpa2-networks)=
### Kubuntu Network Management applet does not connect to WPA2 networks

The Network Management applet in Kubuntu is unable to connect to WPA 2 networks and some VPN setups.  You can use knetworkmanager (available on the DVD) or network-manager-gnome as a workaround. (Bug:339313)


(9-04-kubuntu-may-keep-unneeded-guidance-power-package)=
### Kubuntu may keep unneeded guidance power package

The kubuntu upgrade may leave the no longer needed packages "kde-guidance-powermanager" or
"guidance-power-manager" installed. Those can be removed.


(9-04-ctrl-alt-backspace-disabled-by-default-in-xorg)=
### Ctrl-Alt-Backspace disabled by default in Xorg

The Ctrl-Alt-Backspace key combination to force a restart of X is now disabled by default, to eliminate the problem of accidentally triggering the key combination. Users who do want this function can enable it in their xorg.conf, or by running the command `dontzap --disable`.


(9-04-change-in-notifications-of-available-updates)=
### Change in notifications of available updates

Ubuntu 9.04 introduces a change to the handling of package updates, launching `update-manager` directly instead of displaying a notification icon in the GNOME panel.  Users will still be notified of security updates on a daily basis, but for updates that are not security-related, users will only be prompted once a week.

Users who wish to continue receiving update notifications in the previous manner can restore the earlier behavior using the following command:

```none
gconftool -s --type bool /apps/update-notifier/auto_launch false
```


(9-04-iscsi-upgrades-fail-to-generate-initramfs)=
### iSCSI upgrades fail to generate initramfs

Upgrades of systems using iSCSI will fail to generate the initramfs. As a workaround, edit `/usr/share/initramfs-tools/hooks/iscsi` and change this line:

```none
copy_exec /usr/sbin/iscsistart /sbin
```

to this:

```none
copy_exec /sbin/iscsistart /sbin
```

This will be fixed in a post-release update (Bug:364616).


(9-04-other-known-issues)=
## Other known issues


(9-04-performance-regressions-on-intel-graphics-cards)=
### Performance regressions on Intel graphics cards

Users of Intel video chipsets have reported performance regressions in Ubuntu 8.10 compared with previous releases (Bug:252094).  Many of the issues have been resolved in Ubuntu 9.04, but some remain.

* Some users have found improved performance by using the "greedy" migration heuristic.  This can be done by running "sudo gedit /etc/X11/xorg.conf", and adding `Option "MigrationHeuristic" "greedy"` to the `Device` section of your `xorg.conf`.

* Alternatively, a new experimental acceleration architecture option, "DRI2/UXA", is available for Intel graphics users which our [testing](https://wiki.ubuntu.com/X/UxaTesting) has found provides significant performance improvements in some cases, but has also shown risk of severe stability problems.  You can opt-in to enable this by running "sudo gedit /etc/X11/xorg.conf", and adding `Option "AccelMethod" "UXA"` to the `Device` section of your `xorg.conf`.  Users wishing to maximize stability should stay with the standard default acceleration method, "EXA".


```{warning}
In some cases this will lead to the graphical environment not starting at all or becoming entirely unusable. In that case, start into rescue mode or press Ctrl+Alt+F2 and log into the text console, and use `sudo nano /etc/X11/xorg.conf` to revert the UXA option.
```

* If none of the above helps, some users reported success with [using an older driver version](https://wiki.ubuntu.com/ReinhardTartler/X/RevertingIntelDriverTo2.4).


(9-04-display-freezes-with-intel-graphics-cards)=
### Display freezes with Intel graphics cards

Users of various Intel video chipsets reported freezes under various conditions (e. g. a few minutes after suspend on the i945, see Bug:339091). In many cases, switching off desktop effects in System → Preferences → Appearance was reported to help.

If it still happens without desktop effects, you can add `Option "DRI" "off"` to the `Device` section of `/etc/X11/xorg.conf`, as described above. This will disable 3D acceleration and desktop effects, but makes suspend work reliably again and also avoid many types of crashes.

These freezes happen particularly often on the i965 chips (Bug:359392). For that reason, desktop effects were disabled by default on this chipset in the final release. They will be re-enabled in a 9.04 Update once the problem has been fixed.


(9-04-lock-ups-when-deleting-files-from-ext4-filesystems)=
### Lock-ups when deleting files from ext4 filesystems

In some cases, deleting files from an ext4 filesystem is reported to cause soft lock-ups in the kernel (Bug:330824).  Investigation of this problem is ongoing, and it is expected that a fix for this problem will be made available as a post-release update.  To avoid this problem, users may wish to install using the default ext3 filesystem and convert their filesystem to ext4 (as documented on the [ext4 wiki](http://ext4.wiki.kernel.org/index.php/Ext4_Howto#Converting_an_ext3_filesystem_to_ext4)) once a fix is available.


(9-04-switching-to-ext4-requires-manually-updating-grub)=
### Switching to ext4 requires manually updating grub

If you choose to upgrade your `/` or `/boot` filesystem in place from ext2 or ext3 to ext4 (as documented on the [ext4 wiki](http://ext4.wiki.kernel.org/index.php/Ext4_Howto#Converting_an_ext3_filesystem_to_ext4)), then you _must_ also use the `grub-install` command after upgrading to Ubuntu 9.04 to reinstall your boot loader. If you do not do this, then the version of GRUB installed in your boot sector will not be able to read the kernel from the ext4 filesystem and your system will fail to boot.


(9-04-possible-data-loss-problems-resizing-ext4)=
### Possible data-loss problems resizing ext4

The resize2fs tool may cause data loss when growing or shrinking ext4 filesystems off-line. See [this mail from the upstream maintainer](http://article.gmane.org/gmane.comp.file-systems.ext4/12763) for more details. Unfortunately we became aware of this too late to fix it in Ubuntu 9.04. If you wish to resize an ext4 filesystem using the tools in Ubuntu 9.04, you may be able to work around these problems by first disabling the `flex_bg` and `uninit_bg` features (do not attempt this on a mounted filesystem!):

```none
tune2fs -O ^flex_bg,^uninit_bg /dev/DEVICE_NAME
e2fsck /dev/DEVICE_NAME
```

However, we still strongly recommend taking significantly more care with backups than usual before attempting to resize an ext4 filesystem.


(9-04-pulseaudio-inadvertently-enabled-in-kubuntu-when-installing-from-dvd-or-upgrading-with-apt-get)=
### Pulseaudio inadvertently enabled in Kubuntu when installing from DVD or upgrading with apt-get

When installing Kubuntu 9.04 from the DVD images, or upgrading to Kubuntu 9.04 from a previous release using `apt-get dist-upgrade`, the `pulseaudio` package will be installed in error.  This package is not intended to be installed as part of the Kubuntu desktop.  Users can remove this package with the command:

```none
sudo apt-get purge pulseaudio
```


(9-04-apparmor-profiles-incompatible-with-ecryptfs)=
### Apparmor profiles incompatible with ecryptfs

When using encrypted directories together with apparmor in enforcing mode, apparmor will deny access to certain files unexpectedly because the Linux kernel sees the process as accessing the file via both the unencrypted and encrypted paths (Bug:359338).  As a workaround, users can modify their apparmor profiles under `/etc/apparmor.d/` to grant permissions to

```none
@{HOME}/.Private/**
```

.


(9-04-avahi-will-not-start-if-a-local-domain-is-present)=
### Avahi will not start if a .local domain is present

The `avahi-daemon` package, which implements the mDNS "zeroconf" standard, includes a check to avoid running when a conflicting `.local` DNS domain is present.  It is reported that some ISPs advertise such a `.local` domain on their networks, which will leave Ubuntu 9.04 hosts unable to see names advertised on the local network (Bug:327362).

To force the use of mDNS on a network configured this way, users can run the commands:

```none
sudo sed -i -e'/AVAHI_DAEMON_DETECT_LOCAL/s/1/0/' /etc/default/avahi-daemon
sudo service avahi-daemon start
```


(9-04-wubi-reuses-a-pre-existing-ubuntu-directory-and-removes-it-on-uninstallation)=
### Wubi reuses a pre-existing "ubuntu" directory and removes it on uninstallation

If there is a pre-existing directory called "ubuntu" in the target drive, it will be reused during the Windows installation and the full directory will be removed when uninstalling (Bug:364166). This will result in the loss of any files which were originally in that directory. It is recommended to rename any directory called "ubuntu" before proceeding with a Wubi installation.


(9-04-occasional-hangs-possible-on-arm-architecture)=
### Occasional hangs possible on ARM architecture

The ARM port currently does not support the ppoll() & pselect() system syscalls, which will sometimes cause a failure to mount the root filesystem on boot. This is a race condition, and retrying the boot will usually clear the problem. The work to add the syscalls is currently underway and will be delivered as an update to the Ubuntu 9.04 kernel some time after release.


(9-04-problems-displaying-text-in-mythbuntu-with-radeon-driver)=
### Problems displaying text in Mythbuntu with Radeon driver

The mythtv frontend in mythbuntu fails to render fonts correctly when using the radeon driver and DRI is enabled (Bug:341898).  This issue is expected to be resolved in a post-release update soon after release.  In the meantime, users can work around this problem by disabling DRI in their X configuration.


(9-04-tracker-index-corruption)=
### Tracker index corruption

In some cases it can happen that the index of the "tracker" desktop search engine becomes invalid. A dialog will be shown, offering you to "Reindex all contents". This button does not work, and the tracker service might start to use large amounts of CPU and disk resources. As a workaround, please press Alt+F2 and run `tracker-processes -r`. This will be fixed in a post-release update soon (Bug:361205).

Notes: If you met "Could not open location:file:///home/USERNAME/tracker-processes" messages, please exec `sudo apt-get install tracker-utils`.


(9-04-fujitsu-celsius-h270-notebook-and-nvidia-graphics-driver)=
### Fujitsu Celsius H270 notebook and NVIDIA graphics driver

The NVIDIA graphics driver that is currently in Ubuntu 9.04 has an interaction problem that results in corruption of the internal flatpanel's EDID on the Fujitsu Technology Solutions Celsius H270 notebook, which will persist across reboots. It is not recommended to install Ubuntu 9.04 on this model notebook at this time (Bug:364965).


(9-04-missing-gnome-panels-in-ubuntu-netbook-remix-after-using-the-desktop-switcher-application)=
### Missing GNOME panels in Ubuntu Netbook Remix after using the desktop-switcher application

When using the Switch Desktop Mode option to swap from netbook to classic, the GNOME desktop settings are not retained after a logout.  Upon logging back in, users receive just the desktop background image, without the GNOME panels on the top & bottom of screen.  This problem  will be fixed in a post-release update soon (Bug:349519).


(9-04-real-time-clock-driver-not-loaded-on-arm-nslu2)=
### Real-time clock driver not loaded on ARM NSLU2

On ARM NSLU2 systems, the driver for the real-time clock is not loaded correctly on startup (Bug:353196). You can work around this after installation by running the following commands:

```none
sudo apex-env setenv cmdline 'console=ttyS0,115200 noirqdebug'
sudo rm /etc/modprobe.d/local.conf
sudo update-initramfs -u
```


(9-04-amarok-will-not-offer-to-download-additional-codecs-when-running-kubuntu-from-the-live-cd)=
### Amarok will not offer to download additional codecs when running Kubuntu from the live CD

When started from the live session, Amarok will not offer to download additional media codecs when needed, so, for example, it will be unable to play MP3 files. This will work normally after the system is installed to the hard disk. (Bug:362538)
