---
tocdepth: 3
---

(ubuntu-11-04-release-notes)=
# Ubuntu 11.04 "Natty Narwhal" Release Notes

<!-- Source: https://wiki.ubuntu.com/NattyNarwhal/ReleaseNotes -->

||<tablestyle="float:right; width:40%; background:#F1F1ED; margin: 0 0 1em 1em;" style="padding:0.5em;"><<BR>> <<TableOfContents>>||

These release notes for Ubuntu 11.04 (Natty Narwhal) provide an overview of the release, and document the known issues with Ubuntu 11.04 and its variants.

= Release Overview =

For PC users, Ubuntu 11.04 supports laptops, desktops and netbooks
with a unified look and feel based on a new desktop shell called "Unity".
This version supersedes Ubuntu Netbook Edition for all PC netbooks.

Developer reference images are provided for select Texas Instruments (TI) ARM
platforms, specifically the "PandaBoard" and "BeagleBoard" developer systems.

Ubuntu Server 11.04 has made it easier to provision servers, and reduce
power consumption.   Ubuntu Server 11.04 for UEC and EC2 has a new kernel and
improved initialization and configuration options.

The Ubuntu 11.04 family of Kubuntu, Xubuntu, Edubuntu, Mythbuntu, and Ubuntu Studio have had numerous updates as well.


== Ubuntu Changes ==

=== New Features ===

Unity is now the default Ubuntu desktop session. The Unity launcher has
many [[http://unity.ubuntu.com/about/|new features]], including drag and drop re-ordering of launcher
icons, full keyboard navigation support, launcher activation through
keyboard shortcuts, right-click context menu quick-list and switching
between running applications.

The Ubuntu One control panel now allows selective syncing, and the
launcher icon now displays sync progress.  File syncing speed has been
improved as well.

The Ubuntu Software Center now allows users to  "rate & review"
installed applications, share reviews via integration with social
networking services added into Gwibber,  and has other usability
improvements.

GNOME programs now use a
[[https://launchpad.net/ayatana-scrollbar|new scrollbar]] which takes less
screen space.

=== Updated Applications ===

Ubuntu 11.04 comes with the latest Firefox 4.0 as the standard web browser.

Libre``Office 3.3.2 has replaced Open``Office.org in 11.04 as the default office
suite.

Banshee 2.0 has replaced Rhythmbox is the standard music player, and has now
been integrated into the sound menu.


=== Improved Underlying Infrastructure ===

11.04 has a kernel based on mainline branch stable kernel 2.6.38.2.  Some of the highlights include upstream acceptance of AppArmor, support for Intel IPS (Intelligent Power Sharing), removal of the Big Kernel Lock, file system improvements to Btrfs, Ext4, and XFS, and of course the usual driver updates and support for new hardware.

X.org 1.10.1 and Mesa 7.10.2 are the new versions included with 11.04.  The X server includes a prototype of the multitouch input extension (XInput 2.1). The Qt toolkit also includes pre-release support for multitouch.

The GNU toolchain has transitioned to be based off of gcc 4.5 for i386, amd64, ARM omap3/omap4 and PowerPC architectures.

All main packages have now been built and are installable with Python 2.7.

dpkg 1.16.0-pre brings us up-to-date with staged changes for the
upcoming Debian 1.16.0 dpkg release, as well as pulling in the current
version of the in-progress multiarch work.

Upstart has been updated to 0.9.7-1. There are a lot of new features:
it is now "chroot-aware", there is support for basic job/event
visualization, there are two new initctl commands (`show-config`,
`check-config`), a socket bridge is now provided, the latest D-Bus version
now allows D-Bus services to be activated via Upstart, a manual job
configuration stanza, and override file support is now available.
More details can be found in the [[http://wiki.ubuntu.com/NattyNarwhal/TechnicalOverviewUpstart |Upstart Technical overview]].

== Ubuntu on ARM ==

=== Netbook Images ===

The preinstalled Ubuntu Netbook images for ARM come with the brand new unity-2d desktop by default which incorporates the improved usability and user interface design of unity into low end 2D graphics hardware.

=== *New* Headless Images ===

As a response to long standing community requests, an Ubuntu Headless image is now available for omap3 and omap4 hardware. This image is fully set up to be run and configured using the serial port and contains a minimal command line install.

A detailed list of features and known issues on ARM images can be found [[http://wiki.ubuntu.com/ARM/NattyReleaseNotes|here]].

== Ubuntu Server ==

=== New Features ===

cobbler and mcollective have been included, which will make provisioning servers easier.

Power``Nap 2.0 uses a new method to reduce power consumption and can now
monitor user activity (Console, Mouse, Keyboard), system activity (load,
processors, process IO), and network activity (wake-on-lan, udp ports
tcp ports)

Default dhcpd server updated from dhcp3 to isc-dhcp (version 4).

Eucalyptus is now the latest stable point release (2.0.2) with security
and efficiency fixes.

Open``Stack (nova) in Universe is a technology preview, with a recent
snapshot of 2011.2 (Cactus) release.

=== Cloud images ===

Ubuntu Server is available for for UEC and EC2.

cloud-init has been updated to 0.60. This version includes support for
resizing of the root file system at first boot, adds minimal OVF
transport (iso) support and allow setting of hostname when first
booting. Rightscale support has been added to cloud-config and
cloud-init.

Cloud images now have support for being run as an LXC guest.

Some of the supporting technologies that have been packaged and included
are, Cassandra 0.7.0, ZeroMQ, Membase, and Xtra``Backup.

Images are verified to run against Open``Stack (nova) cloud.


== Kubuntu ==

Kubuntu 11.04 sports the latest KDE software including KDE Platform and Plasma 4.6.2.

Kubuntu now provides a working Samba file sharing module that lets you add and manage shares from the folder's Properties dialogs.

The new Language Selector module allows you to add, remove, and manage system languages directly from System Settings.

An updated system-config-printer-kde brings a number of bug fixes to Kubuntu's printer management tool.

Please see  http://www.kubuntu.org/news/11.04-release for details.


== Xubuntu ==

Xubuntu wallpaper has been updated for this release. The wallpaper is
designed to integrate well with the new graybird theme.

The installation slide show has been updated for Natty Narwhal, and
really displays the best of Xubuntu.

The Elementary Xubuntu icon theme has been updated.

Xubuntu is using the Droid font by default, since it is a lightweight,
good visibility font.

The newly released Xfce 4.8 is included. The menus in Xfce 4.8 are now
editable with any menu editor that meets the freedesktop.org standards.
The suggested editor is alacarte.

== Edubuntu ==
You can test Edubuntu 11.04 directly from your web browser by going at
http://www.edubuntu.org/weblive (regular Ubuntu 11.04 is also available).

!WebLive is also directly integrated in the Ubuntu Software Center
letting you test the most popular apps without installing them on your
machine. Just click the "Test drive" button.

The installer now has an additional step allowing users to fine-tune which
applications should be installed on the final system.

Edubuntu now ships with Arkose, which provides application sandboxing
for downloaded apps.

New software packages in Edubuntu include Pencil, Geogebra, Calibre,
LibreCAD, Freemind and Stellarium.

Theming improvements include a new wallpaper, a LDM theme when installing LTSP
from the Edubuntu installer. The text-mode boot mode now displays "Edubuntu"
instead of "Ubuntu". Our ongoing menu refinements include new icons
where they were missing, and more consistent case use in menu entries.

Edubuntu 11.04 ships with the classical Gnome desktop by default but
Unity is available as an option in the installer.

For more details on what has changed in Edubuntu 11.04, please refer to
http://www.edubuntu.org/news/11.04-release .

== Ubuntu Studio ==

The task selections during installation have been updated. The audio
tasks have been parsed into two groups: generation and recording.

Currently, Ubuntu Studio is shipping the -generic kernel. We are working
with the Ubuntu Kernel Team to get a -low latency kernel into the
archives.  An interim -lowlatency kernel is available in Allesio
Bogani's PPA.

network-manager has replaced gnome-network-admin.

The packages shipped in Ubuntu Studio are now more focused to support
identified tasks and their derived work flows.

Ubuntu Studio does not currently use Unity. As the user logs in it will
default to Gnome Classic Desktop (i.e. Gnome2).


== Mythbuntu ==

The Mythbuntu-bare (Backup and Restore for the database and
configuration files) Mythbuntu Control Center plugin now has the
ability to schedule backups on a daily, weekly, or monthly basis.

Android and iOS devices can now be used as remote controls.

MythTV 0.24 is now integrated into the builds.



= Installation =

== Overview ==

Preparing your computer for Ubuntu is now much simpler, with a wider range of disk setup options.  Each of these are detailed at length to provide you with a clear understanding of the actions that will take place with your selection.

You can now reinstall or upgrade an existing copy of Ubuntu with the Desktop CD installer, provided that your computer is connected to the Internet.


== Download Release ==

11.04 images can be downloaded from a location near you:

 http://www.ubuntu.com/download (Ubuntu and Ubuntu Server) <<BR>>

In addition, they can be found at the following links:

 http://releases.ubuntu.com/11.04/ (Ubuntu, Ubuntu Server) <<BR>>
 http://cdimage.ubuntu.com/releases/11.04/release/ (Ubuntu Netbook ARM, Ubuntu Headless ARM, Ubuntu DVD, 64-Bit for Mac, source) <<BR>>
 http://uec-images.ubuntu.com/releases/11.04/ (Ubuntu Server for UEC and EC2) <<BR>>
 http://cdimage.ubuntu.com/netboot/11.04/ (Ubuntu Netboot) <<BR>>
 http://releases.ubuntu.com/kubuntu/11.04/ (Kubuntu) <<BR>>
 http://cdimage.ubuntu.com/kubuntu/releases/11.04/release/ (Kubuntu DVD, 64-Bit for Mac, preinstalled ARM images) <<BR>>
 http://cdimage.ubuntu.com/xubuntu/releases/11.04/release/ (Xubuntu) <<BR>>
 http://cdimage.ubuntu.com/edubuntu/releases/11.04/release/ (Edubuntu) <<BR>>
 http://cdimage.ubuntu.com/ubuntustudio/releases/11.04/release/ (Ubuntu Studio) <<BR>>
 http://cdimage.ubuntu.com/mythbuntu/releases/11.04/release/ (Mythbuntu) <<BR>>



== System Requirements ==

The minimum memory requirement for Ubuntu 11.04 is 384 MB of memory for Ubuntu Desktop.  Note that some of your system's memory may be unavailable due to being used by the graphics card. If your computer has only the minimum amount of memory, the installation process will take longer than normal; however, it will complete successfully, and the system will perform adequately once installed.

The minimum memory requirement for Ubuntu Server 11.04 is 128 MB of memory.

Systems with less memory may be able to select "Install Ubuntu" from the boot menu to run just the installer, rather than the whole desktop, or may be able to use the alternate install CD.

= Upgrading =


== From Ubuntu 10.10 ==

To upgrade from Ubuntu 10.10 on a desktop system, press Alt+F2, type in "update-manager" (without the quotes), and press Enter. Update Manager will open up and display the message, "New distribution release '11.04' is available." Click Upgrade and follow the on-screen instructions.

To upgrade from Ubuntu 10.10 on a server system, install the package update-manager-core if it is not already installed. Then execute the command sudo do-release-upgrade, and follow the on-screen instructions. Note that the server upgrade is now more robust, and thus will utilize GNU screen and automatically re-attach in case unexpected problems arise, e.g. dropped connection problems.

The same instructions apply to all other editions of Ubuntu (such as Kubuntu, Xubuntu, etc.)

For further information,  please see the instructions in :

  https://help.ubuntu.com/community/NattyUpgrades

== From Other Ubuntu Releases ==

Users of other Ubuntu releases need to upgrade first to 10.10,  and then to 11.04.

For further information on upgrading to 10.10,  please see the instructions in:

  https://help.ubuntu.com/community/MaverickUpgrades


= Known Issues =

== Boot, installation and post-install ==

 * There is a problem creating a bootable 10.04.2 or earlier USB image from Ubuntu 10.10 or 11.04 system.  Booting from the USB can be made to work, but using the workaround of typing "help" and pressing Return. (Bug:645818)
 * The swap partition appears become unusable during some installations (UUID not set).   This issue is under investigation. (Bug:709363)
 * The return_to_partitioning function executes and returns as normal, but seemingly fails to properly clean up after partman-commit and initialize partman. (Bug:740903)
 * During boot, on the cryptsetup passphrase prompt, every character typed causes a repeat of the prompt. (Bug:566818)
 * When making the keyboard layout selection from Ubiquity, cannot get the right selection. (Bug:656777)
 * After selecting "Continue testing" rather than "restart now" there is no GUI option to do the restart. (Bug:657086)
 * There are some cosmetic effects that need cleaning up on the installation slideshow (Bug:529201, Bug:628159) and some translations are missing (Bug:644736, Bug:758739).
 * Some systems installed with the root filesystem on an iSCSI disk fail to boot, although this is not reproducible in all cases. (Bug:728088)
 * The system occasionally fails to reboot after completing the installation and clicking 'Reboot Now'. (Bug:712654)
 * When installing the amd64+mac version, please do not use LVM.  Also avoid using multiple linux instances at this time. (Bug:745960)
 * Keyboard preseeding that worked in previous versions of Ubuntu no longer works.  Instead of `console-setup/layoutcode`, `console-setup/variantcode`, `console-setup/modelcode`, and `console-setup/optionscode`, you need to preseed `keyboard-configuration/layoutcode`, `keyboard-configuration/variantcode`, `keyboard-configuration/modelcode`, and `keyboard-configuration/optionscode` respectively. (Bug:747854)
 * Selecting "Configure encrypted volumes" in the alternate/server installer initialises encrypted volumes from scratch, and will destroy any encrypted data that was previously present.  There is no way to reuse an existing encrypted volume at installation time at the moment, although we do consider this a bug that will be fixed in a future release. (Bug:420080)
 * Some users booting machines from the network using PXE, and using the `LOCALBOOT` facility in Syslinux to hand off to a local hard disk, found that there was no argument that would successfully cause a local boot.  Syslinux provides a `chain.c32` COM32 image which is less reliant on PXE BIOS implementation details. (Bug:625383)
 * Even if no Internet access is available during installation, the desktop CD installer offers checkboxes to install third-party software and software updates.  These options may not work properly without Internet access. (Bug:651932)
 * The manual mount point entry box in the desktop installer's partitioner does not accept keyboard input.  The drop-down still works, so various standard mount points may be selected, and copying and pasting within the entry box also works.  This was noticed too late to be corrected for 11.04.  In the meantime, you can mount partitions manually later, use copy-and-paste, or use the alternate install CD. (Bug:769043)


=== btrfs ===

The btrfs filesystem is considered experimental in this release.  It can generally be installed and used, but with a number of problems.  You should only use it if you are comfortable with dealing with problems and helping us resolve them.

 * As the [[http://btrfs.wiki.kernel.org/|btrfs wiki]] notes: "Note that Btrfs does not yet have a fsck tool that can fix errors. While Btrfs is stable on a stable machine, it is currently possible to corrupt a filesystem irrecoverably if your machine crashes or loses power on disks that don't handle flush requests correctly. This will be fixed when the fsck tool is ready."
 * Crash trying to install over btrfs partition in live installer. (Bug:759503)
 * GRUB cannot detect a btrfs installation within an encrypted disk, and fails to set up the correct kernel parameters. (Bug:757631)
 * Other installations of Ubuntu on btrfs will not be detected or added to the boot menu. (Bug:764893)
 * If btrfs is used for `/boot`, then the gap between the start of the disk and the first partition must be more than the traditional 63 sectors.  A good modern default is 1 MiB. (Bug:774217)

== Upgrades from Ubuntu 10.10 ==

 * In some cases (particularly if different kernel parameters from the default are in use), upgrades from Ubuntu 10.10 may prompt to resolve conflicts in the `/etc/default/grub` configuration file even when it has not been manually changed.  Performing a three-way merge should normally be sufficient if presented with this prompt, although you should check afterwards to ensure that `/etc/default/grub` still looks correct. (Bug:759545)

 * If you have manually installed a PAE kernel (for example to make use of >4GB of RAM) ''and'' you have also installed the proprietary NVidia drivers, you will have to manually install the package "{{{linux-headers-generic-pae}}}" after the upgrade has completed but before rebooting. Failure to do so will result in a system that hangs at boot. If you do forget to install this package before rebooting, select the "recovery" option from the boot menu to allow you to install this package using "{{{apt-get install linux-headers-generic-pae}}}". See bug Bug:772226.

== Downgrades to Ubuntu 11.04 ==

  * If you insert a bootable disk with Ubuntu 11.04 in a system running 11.10 and proceed through the installation process you will be presented with an option to "Upgrade from 11.10 to 11.04".  This option should not have appeared in the installer and it is not a recommended nor supported way to switch from a newer release of Ubuntu to an older one.  Additionally, doing this for a system that was running 11.10 will result a non-working system. (Bug:891711)

== Graphics and display ==

 * The -nouveau video driver has had an ABI change but lacked a version number increment.  Following Debian we're versioning it as 'libdrm-nouveau1a'.  Be aware this can cause difficulties in upgrading/downgrading from PPAs that include libdrm packages.
 * The NVidia-graphics-driver on 8600 GTS cards needs "NoPowerConnectorCheck" option to work. (Bug:522588)
 * Video error "[drm:radeon_ttm_backend_bind] *ERROR* failed to bind 1772 pages" during installation (Bug:557261 and Bug:656486)
 * On certain systems, a bad interaction between Unity, the GL driver and the kernel may cause the system to hang. (Bug:740126)
 * On certain systems, the display may be corrupted after switching resolutions or connecting to an external display under Unity (Bug:753971)
 * Under certain conditions, on systems equipped with nvidia GPUs, focused or maximized windows may be blank. (Bug:763680)
 * Certain applications like Chromium, Xchat or Opera may expose rendering artifacts. (Bug:753369)

== Desktop ==

 * Nautilus keeps opening when ubuntu one plugin is installed. (Bug:674876)
 * When starting the live session on a system without 3D support, the GNOME panel is not displayed. As a workaround, you can press Alt+F2 and run `gnome-panel --replace`. On installed systems you should pick the "Ubuntu Classic (No effects)" session in the login manager. (Bug:711378)
 * When switching between windows, Orca does not speak the title of the focused window. (Bug:724093)
 * In the classic session gnome-panel sometimes fails to load applets. (Bug:716714)
 * On ARM images, the Unity 2D version crashes on various occasions. (Bug:739386)
 * Unity may not behave correctly if DRI settings are present in ~/.drirc (Bug:745996)
 * Unity does not yet fully support focus-follows-mouse/sloppy-focus/point-to-click. Enabling this feature may cause unexpected behavior (Bug:674138)
 * The search feature in Unity does not support ibus input (Bug:66377) or dead keys (Bug:746761); search results in CJK locales are not supported either (Bug:745243) - Those limitations will be addressed in an upcoming update ([[https://launchpad.net/unity/+milestone/3.8.14|3.8.14]]) and will be proposed as SRUs
 * Libreoffice has no minimize/maximize/close buttons. (Bug:728927) - An SRU should fix this issue shortly
 * 3rd party lenses may not start correctly at startup. (Bug:758839) - A workaround is to restart Unity with unity --replace, while a fix is proposed in an SRU
 * In some cases, the SUPER+1..9 shortcuts don't work. (Bug:768076) - As a workaround, start a terminal with CTRL+ALT+T to fix the problem
 * The Dash window may incorrectly appear under a fullscreen window. (Bug:763680)
 * Sometimes, the icons of applications authorized to use the legacy systray protocol may appear under the panel. (Bug:753369)
 * The "stracciatella GNOME session" uses the new small scrollbars instead of the standard GNOME ones. (Bug:766660)
 * The new [[https://wiki.ubuntu.com/Ayatana/ScrollBars|Ayatana Scrollbars]] are now enabled by default. Certain applications however are blacklisted, see https://wiki.ubuntu.com/Ayatana/ScrollBars#Blacklist

In general, the recommended HW configuration for running Unity is available at: https://wiki.ubuntu.com/DesktopExperienceTeam/UnityHardwareRequirements

== Trackpads, touchscreens, mice, and keyboards ==

 * The -synaptics driver has received a new acceleration mechanism.  Trackpad users may notice a significant decrease (or increase) in acceleration as a result.  We are investigating configuration options for this new behavior.
 * The -evdev driver no longer provides middle mouse button emulation.  2-button mice that need this functionality are quite rare these days.  The emulation mode causes a laggy pointer in cases where emulation is not needed, so this change improves responsiveness for all users.  If you have a 2-button mouse that needs this, please see the directions for [[https://wiki.ubuntu.com/X/Quirks#2-button%20Mice|creating a 2-button mouse quirk]]. (Bug:710762)
 * Trackpads now have kinetic scrolling. If you flick to perform a scroll, then press a keyboard key while kinetic scroll events are generated, unexpected application behavior may result. (Bug:728643)
 * The -evtouch driver is not available anymore due to a lack of upstream support. Users are encouraged to switch to the default -evdev driver. Please [[https://bugs.launchpad.net/ubuntu/+source/xserver-xorg-input-evdev/+filebug|file a bug report against the -evdev driver]] for any broken or missing functionality.

== Linux kernel ==

 * Toshiba NB305 hangs for 5 minutes after suspend. Workaround: specify "nohz=off highres=off" as kernel parameters at boot. (Bug:508516)
 * ThinkPad BIOS/EC models may have outdated firmware. (Bug:745363)
 * On certain hardware, enabling power saving for the SATA link can cause disk errors and data corruption. (Bug:539467)
 * On amd64/Mac the main physical screen (iMac display) is detected by the OS radeon driver as output eDP-0, name 'Color LCD', and it is connected but not lit. (Bug:542660)
 * X will flicker, and will dmesg: "[drm:drm_edid_block_valid] *ERROR* EDID checksum is invalid".  Intermittently the screen may go dark after one of these flickers.  This can be worked around by 'sudo get-edid'. (Bug:712075)
 * On 32 bit t1.micro server, instance hangs when installing Sun java. (Bug:634487)
 * Screenful of errors like "[drm:radeon_ttm_backend_bind] *ERROR* failed to bind 1772 pages" may be seen during a liveCD restart. (Bug:656486)
 * Samsung N150 hangs indefinitely after suspend. Workaround: specify "intel_idle.max_cstate=3" as kernel parameter at boot. (Bug:640100)
 * 10-30% increase in power consumption. (Bug:760131)


== Ubuntu Software Center ==

 * When deauthorize my computer is used, the packages are removed but the sources.list entries are not disabled. (Bug:723911)

== Ubuntu Server  ==

 * user prompted to update unmodified grub configuration during Ubuntu server upgrade.  (Bug:759545)
 * Cryptsetup passphrase prompt during boot: every character typed repeats the prompt. (Bug:566818)
 * If you have set up Apache with an encrypted SSL key, the system will now prompt for the passphrase on the console during boot.  This is different from the behaviour of previous versions which would simply fail to start apache. (Bug:582963)
 * Power``Nap does not take recover action in Power``Save mode after powernap-now. (Bug:768598)

== Ubuntu Server for UEC and EC2 ==

 * Installing Java in a 32 bit t1.micro instance will hang, as a work around you may install Java in a t1.small instance and then resize the instance (see [[https://bugs.launchpad.net/ubuntu-release-notes/+bug/634487/comments/13|comment #13]] for details).  (Bug:634487)
 * User prompted for sudo changes on upgrade in ec2/uec image. (Bug:768625)

== Ubuntu ARM ==

 * Due to a bug in the OMAP4 video driver it can happen that the display loses its sync which results in a black screen. To overcome this state switching tty's (ctrl+alt+F1 and switching back to X with ctrl+alt+F7) helps to get your screen back (Bug:746133)
 * On the OMAP4 pandaboard the sound initialization does not work properly due to a race condition between udev  rules and upstart jobs. Calling "alsaucm set _verb Hi``Fi" and "sudo alsactl store" in a terminal will work around this. An updated alsa-utils package that fixes this issue automatically is being prepared (Bug:746023)
 * OMAP3 CPUs dont run at full speed by default. While we set the required mpurate commandline parameter on our images, the values for the different OMAP3 CPUs are not always correct, to work around this you can edit the cmdline in /boot/boot.script and call "sudo flash-kernel", the change will take effect on next reboot (Bug:771537)
 * Libreoffice database packages are currently not installable on ARM systems due to missing architecture support in the package metadata, fixed packages are being prepared in the natty-updates repository (Bug:770627)
 * The GCC compiler defaults changed shortly before release for the ARM architecture dropping an option that might cause troubles with some binaries. Packages that are locally rebuilt will build without the shrink-wrap option set. Binaries in the archive that have not been tested prior to release might expose issues due to this option (Bug:736081)
 * On ARM platforms update-initramfs -c does not update the bootloader. (Bug:701698)

== Kubuntu ==

 * During a Wubi install of Kubuntu the second stage of install after the reboot does not show the progress of the install. The install completes regardless and will reboot into Kubuntu. (Bug:758614)
 * When restarting Kubuntu Live CD, in a language other than English, errors may be seen on screen before desktop starts. (Bug:656486)
 * Existing Kubuntu is listed twice in grub boot page after auto-resize install. (Bug:759459)
 * After a new user is created in Kubuntu systemsettings, they will be prompted to change their password when they log in for the first time.  There is an issue that prevents the new password from being entered.  In order to avoid this problem, the X server needs to be restarted before the new user logs in.  After logout, click on the red logout button on the KDM screen and then click on "Restart X Server". Once the KDM login screen returns, the new user should be able to log in normally. (Bug:641712)
 * The kernel may panic when trying to  install over btrfs partition in live installer. (Bug:759503)
 * kded4 defunct after suspend (Bug:515138)

== Xubuntu ==

 * There is a bug in the "session-menu" plugin in Xfce4. To reboot or shutdown from Virtual``Box, you must logout, then reboot or shutdown from GDM. (Bug:711571)
 * When updating Xubuntu 10.10 to 11.04
   * In Xubuntu, update-manager fails to allow upgrade from 10.10, the command {{{sudo do-release-upgrade}}} is a workaround (Bug:756763)
   * The network-manager icon is missing from indicator area after upgrading to Xubuntu 11.04 (Bug:759608)

== Edubuntu ==
 * There is no Edubuntu AMD64+mac image for Edubuntu. Users of Apple hardware should use the 32bit version of Edubuntu.
 * A bug in the installer makes the space requirement for Edubuntu to be 14.1GB instead of 6-7GB. (Bug:771401)
 * When using Edubuntu 11.04 with LTSP, Unity is always the default session even if it wasn't selected at install time. (Bug:770323)
 * The custom Edubuntu installer steps (Unity/LTSP selection and package selection) aren't translated. (Bug:771268)
 * The default Edubuntu LTSP environment (including LTSP live) isn't using the system's locale by default. This can be worked around post-installation by setting the "LANGUAGE" parameter to the wanted locale in /var/lib/tftpboot/ltsp/i386/lts.conf (Bug:771270)

== Ubuntu Studio ==

 * No issues to report.

== Mythbuntu ==

 * No issues to report.

== Other ==

If you would like to help shape Ubuntu, take a look at the list of ways
you can participate at:  http://www.ubuntu.com/community/participate .

Your comments, bug reports, patches and suggestions really help us to
improve this and future releases of Ubuntu.   Instructions can be
found at: https://help.ubuntu.com/community/ReportingBugs .
