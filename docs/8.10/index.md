---
tocdepth: 3
---

(ubuntu-8-10-release-notes)=
# Ubuntu 8.10 "Intrepid Ibex" Release Notes

<!-- Source: https://wiki.ubuntu.com/IntrepidReleaseNotes -->

||<tablestyle="float:right; width:40%; background:#F1F1ED; margin: 0 0 1em 1em;" style="padding:0.5em;"><<BR>> <<TableOfContents>>||

These release notes document known issues with Ubuntu 8.10 and its variants.

= System Requirements =

The minimum memory requirement for Ubuntu 8.10 is 256 MiB of memory. (Note that some of your system's memory may be unavailable due to being used by the graphics card.)

With only the minimum amount of memory available, the installation process will take longer than normal, but will complete successfully, and the system will perform adequately once installed. Low-memory systems may be able to use the desktop CD to install by selecting "Install Ubuntu" from the boot menu to run just the installer, rather than the whole desktop started by selecting "Try Ubuntu without any change to your computer".

= Installation =

== Hard disks potentially not shown when installing in Live CD mode ==

If a user browses a hard disk in Live CD mode before choosing to install, Ubiquity will not allow installation onto this disk because disks cannot be partitioned if they have busy (mounted) partitions.  To use a mounted disk for installation, first unmount the drive before attempting to install.   

== "Free software only" option installs restricted software ==

The "Free software only" option, available by pressing F6 twice on the first screen of the desktop CD/DVD, will install the restricted package {{{linux-restricted-modules-2.6.27-7-generic}}} in error.  This can be worked around by removing the {{{linux-restricted-modules-2.6.27-7-generic package}}} after the installation completes.

Note that the "Free software only" option does not install any other restricted software.

For more information, please see [[https://bugs.launchpad.net/ubuntu-release-notes/+bug/290925|Bug 290925]]

== Slow start to "Select and install software" step in text-mode installer ==

The "Select and install software" step in the text-mode install CD may appear to hang at a low single-digit percentage. This is particularly the case for netboot installations, where there will be no progress bar updates at all while downloading packages. This is due to a fault in the interaction between the installer and `apt-get`, which was diagnosed too late to fix for Ubuntu 8.10: [[https://launchpad.net/bugs/290234|bug 290234]].

You can find out whether the installer is making progress by pressing Alt-F4 to switch to the logging console; Alt-F1 switches back to the main installer. (If you are installing in QEMU or KVM, be careful to press Ctrl+Alt or click in the window to have the emulator grab focus before pressing Alt-F4, as otherwise this will close the emulator!)

== oem-config fails to handle some languages properly ==

The OEM end-user configuration tool mishandles selection of languages that do not use the ASCII or ISO-8859-1 character sets, and the end user will end up with no localisation set after selecting such languages ([[https://launchpad.net/bugs/290580|bug 290580]]). The list of ''known-good'' languages is as follows: Basque, Catalan, Danish, Dutch, English, Finnish, French, Galician, German, Indonesian, Italian, Northern Sami, Norwegian Bokmål, Norwegian Nynorsk, Portuguese, Portuguese (Brazil), Spanish, Swedish, Tagalog.

For the meantime, OEMs affected by this problem may apply this [[http://bazaar.launchpad.net/~ubuntu-core-dev/oem-config/trunk/revision/555|patch]] (the `scripts/tzsetup` part) to the file `/usr/lib/oem-config/timezone/tzsetup` before running "Prepare for shipping to end user". We expect to release an update for this in due course, which will be installable via the normal packaging system at that same stage.

== MID image requires a network for successful installation ==

When trying to install the Ubuntu MID (Mobile Internet Device) image without a network, the installer displays a pop-up dialog in a loop near the end of the installation while scanning the archive. The only way to break this loop is to connect to a network ([[https://launchpad.net/bugs/288320|bug 288320]]).

== Recommended packages installed by default ==

In accordance with the Debian Policy Manual (which says "The 'Recommends' field should list packages that would be found together with this one in all but unusual installations"), the package management system now installs packages listed in the Recommends: field of other installed packages as well as Depends: by default. If you want to avoid this for specific packages, use `apt-get --no-install-recommends`; if you want to make this permanent, set `APT::Install-Recommends "false";` in `/etc/apt/apt.conf`. Be aware that this may result in missing features in some programs.

== Password limitation with ecryptfs ==

Users of the alternate/server installation who choose a password containing a "%" or a "-" will end up with an encrypted ~/Private directory that will not mount on reboot and subsequent logins. To fix this, affected users will need to do the following in the newly installed system:
 1. Update ecryptfs-utils to at least version 53-1ubuntu12 (as soon as it becomes available as a package update)
 2. Run: {{{$ ecryptfs-setup-private --force}}}

For more information on the bug and solution approach see [[https://launchpad.net/bugs/290445|bug #290445]].

== PlayStation 3 installation issues ==

There are some non-fatal issues with installation from the alternate install CD on Play``Station 3 systems. See the [[http://psubuntu.com/wiki/IntrepidReleaseNotes|PS3 release notes]] for more details.

= Upgrading =

Users of Ubuntu 8.04 LTS can upgrade to Ubuntu 8.10 by a convenient automated process. Users of older Ubuntu releases need to upgrade to Ubuntu 8.04 LTS first, and then to 8.10. Complete instructions may be found at http://www.ubuntu.com/getubuntu/upgrading.

== nVidia "legacy" video support ==

The 71 and 96 series of proprietary nVidia drivers, as provided by the {{{nvidia-glx-legacy}}} and {{{nvidia-glx}}} packages in Ubuntu 8.04 LTS, are not compatible with the X.Org included in Ubuntu 8.10.  Users with the nVidia TNT, TNT2, TNT Ultra, Ge``Force, Ge``Force2, Ge``Force3, and Ge``Force4 chipsets are affected and will be transitioned on upgrade to the free {{{nv}}} driver instead.  This driver does not support 3D acceleration.

Users of other nVidia chipsets that are supported by the 173 or 177 driver series will be transitioned to the {{{nvidia-glx-173}}} or {{{nvidia-glx-177}}} package instead.  However, unlike drivers 96 and 71, drivers 173 and 177 are only compatible with CPUs that support [[http://en.wikipedia.org/wiki/Streaming_SIMD_Extensions|SSE]] (e.g. Intel Pentium III, AMD Athlon XP or higher).  Systems with older CPUs will also be transitioned to the {{{nv}}} driver on upgrade.

== ATI "fglrx" video support ==

The ATI video driver in 8.10 drops support for video cards with r300 based chips (the Radeon 9500 - X600 Series of cards). If you have such a card, please use "Hardware Drivers" at System/Administration to disable it before the upgrade.
Please see [[https://bugs.launchpad.net/ubuntu/+source/fglrx-installer/+bug/284408|bug 284408]] for more information

== X.Org Input Devices ==

The X.Org configuration file ({{{/etc/X11/xorg.conf}}}) still has Input``Device entries for the mouse and keyboard, but they are ignored now because input-hotplug is used. The keyboard settings now come from {{{/etc/default/console-setup}}}; to change them please use `sudo dpkg-reconfigure console-setup`. After that, HAL and X need to be restarted (e.g., by rebooting your system).

== X.Org evdev xmodmap incompatibility ==

The X keycodes generated with the new {{{evdev}}} input driver in X.Org 1.5 are not compatible with those generated in Ubuntu 8.04 LTS and before.  If you have configured keybindings for your user with a {{{~/.Xmodmap}}} file, you will need to convert or disable it by hand on upgrade.

== UbuntuStudio real-time kernel support ==

The real-time kernel variant included in Ubuntu 8.10 does not include SMP support.  Users of Ubuntu``Studio 8.04 who need real-time kernel support for dual-core, dual-processor, or more complex SMP configurations are advised not to upgrade to Ubuntu``Studio 8.10 at this time.

== Toshiba laptop hotkey support ==

The {{{tlsup}}} kernel driver included in Linux 2.6.27 for support for Toshiba laptops is not compatible with the X.Org 1.5 event model, as a result of which hotkeys on these laptops are not usable with Ubuntu 8.10.  This will be addressed in a post-release kernel update to reintroduce the {{{toshiba_acpi}}} driver.

== Boot failures on systems with Intel D945 motherboards ==

Users have reported slower than normal detection of SATA hard drives on systems with Intel D945 motherboards in Ubuntu 8.10.  This may cause the system to drop to a busybox initramfs shell on boot with a "Gave up waiting for root device." error. Wait a minute or two and then exit the initramfs shell by typing 'exit'. Booting should proceed normally. If it doesn't, wait a bit longer and try again. Once the system boots, edit {{{/boot/grub/menu.lst}}} and add {{{rootdelay=90}}} to the kernel stanza for your current kernel. ([[https://launchpad.net/bugs/290153|Bug 290153]]).

== Kubuntu KDE4 remix ==

In some cases an upgrade from Kubuntu 8.04 KDE 4 Remix to Kubuntu 8.10 will not update all applications. This will happen if the package {{{kubuntu-desktop}}} was removed. We strongly advise to ensure {{{kubuntu-desktop}}}, and if KDE 4 is installed also {{{kubuntu-kde4-desktop}}}, is installed before upgrading. If using the release upgrader, this will be handled automatically.

=== Cannot login after upgrade from Kubuntu 8.04 KDE 4 Remix ===

After an upgrade from Kubuntu 8.04 KDE 4 Remix, logging in will return directly to the login screen again.  The {{{x-session-manager}}} alternative link is not correctly updated.  Select "KDE" from the Session Menu before logging in and fix it with {{{update-alternatives --set x-session-manager /usr/bin/startkde}}}.  ([[https://launchpad.net/bugs/287488|Bug 287488]])

== Support for ssl/blowfish-v0.2, version 2:0:1 not in encfs ==

Compatibility for this old algorithm was dropped in the 1.4.x version of {{{encfs}}} included in Ubuntu 8.10. Before upgrading, users of this algorithm will have to manually migrate their encfs volumes to a new one created with the new version. Alternatively, you may stay at an old version of encfs to be able to read the volumes. 

== PlayStation 3 upgrade issues ==

The graphical boot splash must be turned off when upgrading Play``Station 3 systems from Ubuntu 8.04 ([[https://launchpad.net/bugs/285218|bug 285218]]). See the [[http://psubuntu.com/wiki/IntrepidReleaseNotes|PS3 release notes]] for more details.

= Other known issues =

== System lock-ups with Intel 4965 wireless ==

The version of the {{{iwlagn}}} wireless driver for Intel 4965 wireless chipsets included in Linux kernel version 2.6.27 causes kernel panics when used with 802.11n or 802.11g networks.  Users affected by this issue can install the {{{linux-backports-modules-intrepid}}} package, to install a newer version of this driver that corrects the bug.  (Because the known fix requires a new version of the driver, it is not expected to be possible to include this fix in the main kernel package.)

== Cannot reactivate Intel 3945/4965 wireless if booting with killswitch enabled ==

On laptops with Intel 3945 or Intel 4965 wireless chipsets and a killswitch for the wireless antenna, starting the system with the killswitch enabled (i.e., with wireless disabled) will prevent re-enabling the wireless by toggling the killswitch.  As a workaround, users should boot the system with the killswitch disabled.  For more information see [[https://bugs.launchpad.net/bugs/193970|bug 193970]].  A future kernel update is expected to address this issue.

== Atheros ath5k wireless driver not enabled by default ==

The version of the {{{ath5k}}} driver for Atheros wireless devices included in Linux 2.6.27 interferes with the use of the {{{madwifi}}} driver for some wireless devices and as a result has been disabled by default.  Many Atheros chipsets will work correctly with the {{{madwifi}}} driver, but some newer chipsets may not, and the {{{madwifi}}} driver may not work with WPA authentication.  If you have an Atheros device that does not work with {{{madwifi}}}, you will want to install the {{{linux-backports-modules-intrepid-generic}}} package, which includes an updated version of the {{{ath5k}}} driver.  While not installed by default, this {{{linux-backports-modules-intrepid-generic}}} package is included on the Ubuntu 8.10 CD and DVD images for ease of installation.

== Limited support for Wacom tablet hotplugging ==

X.Org 1.5 includes support for autodetection of input devices, but for Wacom tablets this is currently limited to detecting the stylus only.  Users of tablet devices who wish to use other input features will need to statically configure their input devices in {{{/etc/X11/xorg.conf}}}.

A complete discussion of this issue can be found in [[https://bugs.launchpad.net/bugs/282203|bug 282203]].

== iSCSI boot order ==

File systems hosted on iSCSI targets may not be mounted automatically at boot time, even if they have an entry in `/etc/fstab`, if a bridged or bonded Ethernet interface is required to reach the iSCSI target. As a work-around, you would have to restart the open-iscsi service and manually mount the file system in question after system boot, once the required network interface have been brought up. Systems equipped with a plain Ethernet interface are not affected.

See [[https://launchpad.net/bugs/227848|bug 227848]].

== Cannot mount more than one iSCSI target ==

Mounting multiple iSCSI targets at the same time is currently not supported. Systems configured to use more than one iSCSI targets should not be upgraded to Ubuntu 8.10.

For more information on the bug and solution approach see [[https://launchpad.net/bugs/289470|bug 289470]].

== Wireless doesn't work after suspend with ath_pci driver ==

Wireless devices that use the {{{ath_pci}}} kernel driver, such as the Atheros AR5212 wireless card, will be unable to connect to the network after using suspend and resume.  To work around this issue, users can create a file {{{/etc/pm/config.d/madwifi}}} containing the single line:
{{{
   SUSPEND_MODULES=ath_pci
}}}

This will cause the module to be unloaded before suspend and reloaded on resume.

== Systems installed from pre-release daily images may be missing some files ==

A bug present in pre-release daily desktop images caused some files related to language support to be missing from installed systems.  Uninstalling and reinstalling the language support packages should correct this issue.

This issue does not affect users who installed using the Ubuntu 8.10 Beta or Release Candidate.

== Kubuntu Bluetooth support ==

Bluetooth is not supported in Kubuntu 8.10 because KDE does not yet support the bluez 4.x stack required for compatibility with the kernel used in 8.10.  
A fix for this is being evaluated as a post-release update. ([[https://launchpad.net/bugs/280997|Bug 280997]])

== KNetworkManager cannot manage connections with static IPs ==

KNetwork``Manager in Kubuntu 8.10 sometimes fails with network connections that require static IP address configuration ([[https://launchpad.net/bugs/280762|bug 280762]]).  Connections which use DHCP for IP address configuration are not affected by this problem.

== Using usb-creator with 8.04.1 (Hardy) images ==

Persistence support in 8.04.1 images is broken. Creating a USB disk with usb-creator and an 8.04.1 image results in a busybox prompt if the persistence option is checked.

== Only US wireless channels enabled by default on Intel 3945 ==

The {{{iwl3945}}} wireless driver defaults to the US regulatory domain for wireless, so wireless networks on channels forbidden by US regulations but permitted by European or Japanese regulations will not work out of the box. This affects IEEE 802.11b/g channels 12 (Europe and Japan), 13 (Europe and Japan), and 14 (Japan only), as well as all 802.11a channels. (Some other wireless drivers may be affected; this is the only one we are sure of so far.)

To work around this, add the following line to the `/etc/modprobe.d/options.conf` file if you use this driver and need to use European wireless channels: {{{
options cfg80211 ieee80211_regdom=EU
}}}

Alternatively, add the following line if you use this driver and need to use Japanese wireless channels: {{{
options cfg80211 ieee80211_regdom=JP
}}}

== Cyrus SASL database created with incorrect permissions ==

Cyrus SASL creates the database for its sasldb2 plugin with incorrect permissions. As a result, other users of this database, such as cyrus-imap, will not be able to access it and will fail. This does not affect upgrades of existing databases from a previous release. The workaround is to manually change the group of /etc/sasldb2 to sasl: {{{
$ sudo chgrp sasl /etc/sasldb2
}}}

See [[https://launchpad.net/bugs/288478|bug 288478]] for details.

== Access to Java Runtime Environment ==

To use Java programs, you need to install the `openjdk-6-jre` package whch contains the Java Runtime Environment. If you want to develop Java programs, then install the `openjdk-6-jdk` package. To work with Java applets in the Firefox browser and compatible browsers on x86 architectures, you need to install the `icedtea6-plugin` package by hand.

The JRE and the Java applet plugin are installed by default in the live session on the Ubuntu DVD, but are not currently installed elsewhere due to space constraints. However, a [[https://launchpad.net/bugs/290400|missing feature]] in the installer means that these packages will not be installed when installing using the graphical installer on the DVD, so you will need to install them afterwards.

== CD eject problems ==

After ejecting a CD tray containing a disc, the tray will be immediately retracted, making it difficult to remove the disc ([[https://launchpad.net/bugs/283316|bug 283316]]). This can be worked around by pressing the eject button again before the disc is fully mounted, after which it will stay open. We expect to fix this in a post-release update.

== Session save/restore does not work, and applications cannot auto-save on logout ==

The "Automatically remember running applications when logging out" option found in Session Preferences does not work at all in this release ([[https://launchpad.net/bugs/249373|bug 249373]]).

Many applications are capable of automatically saving, or offering to save, any open documents when you log out.  The GNOME session manager in this release does not notify them when you log out, giving no opportunity to save their state.  As a result, logging out of the session while modified documents are open may cause data loss.

== Hangs with desktop effects on Intel 830MG and 845G video cards ==

There is a bug in the Intel video driver for the older intel 830 and 845 integrated video cards that are used on laptops like the IBM R30. Desktop effects with compiz will not work on those chips and will freeze the system. For new installations, please install using the safe graphics mode (press F4 in the startup screen) on these systems and disable desktop effects via {{{System -> Preferences -> Appearance}}}, clicking on "Visual effects" and choosing "None".

== PlayStation 3 issues ==

There are a variety of other known issues affecting Play``Station 3 systems, documented in more detail in the [[http://psubuntu.com/wiki/IntrepidReleaseNotes|PS3 release notes]]. They include:

 * To get back to the Sony Play``Station 3 XMB operating system from the boot prompt, users need to type `game` and press the Return key ([[https://launchpad.net/bugs/277839|bug 277839]]). If this is for some reason not possible, carrying out a hard-reset (see PS3 instruction manual) will return to the XMB on next run.
 * Users may occasionally see an intermittent shutdown hang with a message like "IRQ 50: nobody cared". The problem has been reported upstream. Press and hold the PS3 power button until you hear 2 beeps will force power off. The system will boot normally on next run ([[https://launchpad.net/bugs/220370|bug 220370]]).
 * Network``Manager does not list available wireless networks, although it is possible to connect to a wireless network with a known SSID using the "connect to hidden wireless network" option ([[https://launchpad.net/bugs/289977|bug 289977]]); and it cannot connect to WPA/WPA2 wireless networks, although WEP works ([[https://launchpad.net/bugs/289982|bug 289982]]).
