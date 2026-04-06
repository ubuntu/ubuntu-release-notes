---
tocdepth: 3
---

(ubuntu-10-10-release-notes)=
# Ubuntu 10.10 "Maverick Meerkat" Release Notes

<!-- Source: https://wiki.ubuntu.com/MaverickMeerkat/ReleaseNotes -->

||<tablestyle="float:right; width:40%; background:#F1F1ED; margin: 0 0 1em 1em;" style="padding:0.5em;"><<BR>> <<TableOfContents>>||

These release notes for Ubuntu 10.10 (Maverick Meerkat) provide an overview of the release, and document the known issues with Ubuntu 10.10 and its variants.  



= Release Overview =

== Ubuntu Software Center ==

Ubuntu Software Center now shows "Featured" and "What's New" sections, a History of package installations and removals, and makes it easier to find add-ons for applications. It also offers Fluendo DVD Player for purchase, with more software to come soon.

== Ubuntu Font ==

The [[http://font.ubuntu.com/|Ubuntu Font Family]] is a brand-new typeface that is used for the user interface menus, widgets and titles in Ubuntu and Kubuntu.  It covers Latin, Cyrillic and Greek in Ubuntu 10.10 with choices of Regular, Bold, Italic and Bold Italic styles and weights.  The fonts also feature support for the new [[http://en.wikipedia.org/wiki/Indian_rupee_sign|Indian Rupee Sign]] making Ubuntu 10.10 the first operating system to ship with out-of-the-box support for the world's newest currency symbol: ready for use by [[http://www.kdedevelopers.org/node/4331|one billion Indians]].

Designed with screen readability and [[http://www.markshuttleworth.com/archives/537|aesthetic beauty in mind]], the font was first seen in the new Ubuntu 10.04 logo design.  It will continue to be expanded with Arabic, Hebrew, and Monospace support in future Ubuntu releases under the guidance of the [[http://www.daltonmaag.com|Dalton Maag]] type foundry and the [[http://design.canonical.com|Canonical design team]].

== Installer ==

The Ubiquity Installer has been redesigned to be easier to use as well as to install drivers and download updates during installation.

== Ubuntu Desktop Edition ==

The [[http://www.gnome.org|GNOME]] base platform has been updated to the current [[http://library.gnome.org/misc/release-notes/2.32/|2.32 version]], including the new [[http://live.gnome.org/dconf|dconf and gsettings]] API. 

[[http://projects.gnome.org/evolution/|Evolution]] was updated to the 2.30 version, which operates much faster compared to the version in Ubuntu 10.04 LTS.

[[http://yorba.org/shotwell/|Shotwell]] has replaced [[http://f-spot.org/|F-Spot]] as the default photo manager.

[[http://gwibber.com/|Gwibber]] has been updated to support the recent change in Twitter's authentication system, as well as changing the back end storage to improve performance.

The [[https://launchpad.net/indicator-sound|sound menu]] has been enhanced to include music player controls.

Ubuntu One has improved desktop integration with new sign-up and sign-in processes, Nautilus enhancements for managing folder sync preferences, faster file sync speed, and the ability to share links to music within the Ubuntu One Music Store.

== Ubuntu Netbook Edition ==

The new [[http://www.markshuttleworth.com/archives/383|Unity interface]] is now the default in Ubuntu Netbook Edition. It includes places for launching applications and browsing files, semantic search through the usage of zeitgeist, optimizing vertical space with a global menu bar and maximizing application by default. 

A launcher is also available for keeping and dealing with mostly used applications. All favorites from UNE lucid or gnome panel items and desktop shortcuts are automatically shown in the launcher when you first run Unity.

The time is shown in the panel using a new module, `indicator-datetime`, which does not yet have a graphical setting for showing the date. A graphical setting would be provided in Ubuntu 11.04.

The standard photo management application has been switched to [[http://yorba.org/shotwell/|Shotwell]] and UNE comes will all goodness of the Desktop Edition too. Evolution is now performing a special mode more suited for netbook screen size.

A list of required hardware is [[https://wiki.ubuntu.com/DesktopExperienceTeam/UnityHardwareRequirements|available here]].


== Ubuntu Server Edition ==

We have added a major new version of Eucalyptus (version 2.0) that provides numerous bug fixes, more stability, and better user management.

Ubuntu cloud images can now easily be run outside of an EC2 or UEC instance environment.  This will allow you to quickly and easily test function in cloud-init or other features of the image without needing to start a new instance.  There is more information available on the Ubuntu [[https://help.ubuntu.com/community/UEC/Images|wiki]]. 

Canonical has also launched the ''Ubuntu Server on Cloud 10'' program. Anyone will be able to try out Ubuntu 10.10 Server Edition on Amazon EC2 for free for one hour. Visitors to the download pages will now be able to choose to experience the ease and speed of public cloud computing and Ubuntu.  For a direct link to the trial, please go to http://10.cloud.ubuntu.com


== Kubuntu ==

Kubuntu 10.10 comes with the latest [[http://www.kde.org|KDE]] Software.  KDE Platform, Workspaces and Applications were [[http://www.kde.org/announcements/announce-4.5.1.php|updated to 4.5.1]].

For 10.10, Kubuntu has merged the Desktop and Netbook images into one image featuring both the Plasma Desktop and Plasma Netbook workspaces.  The appropriate workspace for your machine will be launched at login, you can also change the workspace in System Settings.

Plasma Netbook now sports the Global Menu by default.

The defaults web browser is now Rekonq, a KDE browser based on Qt Webkit. 

The new KDE bluetooth application collection Bluedevil is now installed by default.

Pulseaudio is the default sound server to match other Ubuntu variants.

KPackageKit updates bring a faster backend and an updated UI with an application based view.  It also has new features such as a backup/restore tool for the list of installed packages.

Kubuntu's installer, Ubiquity, now offers install of restricted packages during the OS install.  Install starts after partitioning making it a quicker experience.

Qapt-batch now replaces install-package as the update/batch-installer utility  

[[http://qt.nokia.com/products/|Qt]] was updated to the current [[http://labs.qt.nokia.com/2010/09/21/qt-4-7-0-now-available/|4.7]] release and Qt Webkit to 2.0.

Kubuntu Mobile Tech Preview is a new variant with a workspace suitable for smart phones.

For more information see the Kubuntu [[http://www.kubuntu.org/news/10.10-release|release page]]


== Xubuntu ==

[[http://www.xfce.org/|Xfce4]] was updated to the current [[http://www.xfce.org/documentation/changelogs/4.6.2?PHPSESSID=01a9340c291d5153df6ecade0e0ce0ad|4.6.2 release]]. This fixes many of the bugs and updates the programs used in Xubuntu.

New default applications: Parole (Xfce4 Media Player) replaced Totem Movie Player, Xfburn (Xfce4 CD/DVD burning tool) replaced Brassero, and xfce4-taskmanager (Xfce4 process manager) replaced Gnome-Task-Manager. See the [[Xubuntu/MaverickMeerkat/|Xubuntu release notes]].


== Edubuntu ==

Edubuntu features an easier than ever installation for LTSP and netbook users. It also now ships with Gnome Nanny, a tool for restricting computer access to users at certain times that also provides basic content filtering.

Ubuntu Netbook Remix is now replaced with the Unity interface. LTSP has been updated to 5.2.4 and the Edubuntu menueditor has been updated to fix issues in the previous release.

Edubuntu also includes now additional wallpapers and language support has now been expanded to 143 languages.

During this release cycle Edubuntu also got a brand new website and now has presence on the most popular social networking sites.



== Ubuntu Studio ==

Ubuntu Studio has had several applications updated and includes the changes from Ubuntu.  There is now better integration between Pulse Audio and JACK - starting JACK does not automatically suspend Pulse Audio anymore. JACK and Pulse Audio can be used side by side if they are using different audio interfaces, if they are trying to use the same audio interface JACK will take precedent.   In addition,  the network connections can now be configured with gnome-network-admin.


== Mythbuntu ==

In this release,  Mythbuntu has updated to [[http://www.mythtv.org/|MythTV 0.23.1]].   There is also a new backup and restore tool. 


== Linux kernel 2.6.35 ==

RC includes the 2.6.35-22.33 kernel which is based on the 2.6.35.4 Upstream stable [[http://kernel.org|kernel]].

This kernel includes additional input subsystem patches for improved multitouch capability, improved support for Intel Sandybridge which includes support for 82579 LOM's, Apparmor bug fixes, reverts some KMS disablement patches, and general security updates ([[http://people.canonical.com/~ubuntu-security/cve/2010/CVE-2010-3081.html|CVE-2010-3081]],[[http://people.canonical.com/~ubuntu-security/cve/2010/CVE-2010-3301.html|CVE-2010-3301]]).  With 10.10 we have also dropped support for i586 and lower processors, as well as i686 processors without cmov support.

This kernel also includes new [[https://wiki.ubuntu.com/SecurityTeam/Roadmap/KernelHardening|security enhancements]]. Of major note is the change to the default behavior of [[https://wiki.ubuntu.com/SecurityTeam/Roadmap/KernelHardening#ptrace|PTRACE]] which is used by gdb, strace, ltrace, etc. The behavior for 10.10 is that only child processes can be PTRACEd, due to the default value of "1" in `/proc/sys/kernel/ptrace_scope`. This value may be inappropriate for some development systems and servers with only admin accounts. If using "sudo" for PTRACE is not desired, please change this value to "0", though read `/etc/sysctl.d/10-ptrace.conf` for more details.

There will be a kernel update made available shortly after the release. 
<<BR>>
<<BR>>
<<BR>>
= Installation =

== Overview ==

The graphical installer has been streamlined and given a substantial visual redesign.  It now only asks the minimum of questions (language and partitioning) before it starts to copy files from the CD, and asks the remaining questions while transferring files to disk.

The new [[https://btrfs.wiki.kernel.org/index.php/Main_Page|btrfs]] file system may now be used during installation via manual partitioning, as long as `/boot` is on some other file system.


== Download Release ==

The following link will direct you to a download location near you:

 http://www.ubuntu.com/testing/download (Ubuntu Desktop, Server, and Netbook) <<BR>>

Additional ISOs and torrents are also available at:
 http://uec-images.ubuntu.com/releases/10.10/ (Ubuntu Server for UEC and EC2) <<BR>>
 http://releases.ubuntu.com/kubuntu/10.10/ (Kubuntu) <<BR>>
 http://cdimage.ubuntu.com/xubuntu/releases/10.10/ (Xubuntu) <<BR>>
 http://cdimage.ubuntu.com/edubuntu/releases/10.10/ (Edubuntu DVD) <<BR>>
 http://cdimage.ubuntu.com/ubuntustudio/releases/10.10/ (Ubuntu Studio) <<BR>>
 http://cdimage.ubuntu.com/ubuntu-netbook/ports/releases/10.10/ (Ubuntu ARM) <<BR>>
 http://cdimage.ubuntu.com/mythbuntu/releases/10.10/ (Mythbuntu) <<BR>>
 http://cdimage.ubuntu.com/kubuntu-mobile/releases/10.10/ (Kubuntu Mobile Preview) <<BR>>
 http://cdimage.ubuntu.com/kubuntu-mobile/ports/releases/10.10/ (Kubuntu Mobile Preview ARM) <<BR>>


== System Requirements ==

The minimum memory requirement for Ubuntu 10.10 is 256 MB of memory. Note that some of your system's memory may be unavailable due to being used by the graphics card. If your computer has only the minimum amount of memory, the installation process will take longer than normal; however, it will complete successfully, and the system will perform adequately once installed.

Systems with less memory may be able to select "Install Ubuntu" from the boot menu to run just the installer, rather than the whole desktop, or may be able to use the alternate install CD.
<<BR>>
<<BR>>
<<BR>>
= Upgrading =

Complete instructions are available [[http://www.ubuntu.com/getubuntu/upgrading|online]].

== From Ubuntu 10.04 LTS  ==

To upgrade from Ubuntu 10.04 LTS on a desktop system, press Alt+F2 and type in "update-manager" (without the quotes) into the command box. Update Manager should open up and tell you: New distribution release '10.10' is available. Click Upgrade and follow the on-screen instructions.

To upgrade from Ubuntu 10.04 LTS on a server system: install the {{{update-manager-core}}} package if it is not already installed; edit {{{/etc/update-manager/release-upgrades}}} and set {{{Prompt=normal}}}; launch the upgrade tool with the command {{{sudo do-release-upgrade}}}; and follow the on-screen instructions.  

== From Kubuntu 10.04 LTS ==

To upgrade from Kubuntu 10.04 LTS, please follow the [[https://help.ubuntu.com/community/MaverickUpgrades/Kubuntu|upgrade instructions]].

== From Other Ubuntu Releases ==

Users of other Ubuntu releases need to upgrade first to 10.04LTS, and then to 10.10. 



= Known Issues =


== Boot, installation, upgrade and post-install ==

 *  '''In dual boot installs, side-by-side partitioning can be overridden by the user, resulting in data loss.''' After selecting the "Install alongside other operating systems" option, clicking on either the "Use entire partition" of "Use entire disc" buttons will override the side-by-side partitioning and result in a loss of data. (Bug:655950)

 * '''In dual boot installs, after using Windows applications that use the [[http://en.wikipedia.org/wiki/Flexnet|FlexNet Publisher]], as a license manager, such software will overwrite GRUB, effectively breaking the boot process.''' This has been fixed for applications including Adobe Photoshop (CS4), Dell Datasafe backup, Autocad 2009,Adobe Flash Builder 4,UtraISO. If you have this problem with a new application, see the bug report to add its signature to prevent future problems (Bug:441941) 

 * '''The Wubi Windows installer was reported to be unable to open Windows' boot configuration data store in some (but not all) cases.'''  Investigation of the problems are ongoing (Bug:613288)

 * '''You cannot upgrade if wubi is installed to a partition other than Windows.''' (Bug:610898,Bug:653134)

 * '''Lenovo S10-3 systems don't boot.''' Temporary workaround: add "intel_idle.max_cstate=0" as a kernel paremeter at boot (Bug:634702). A fix already exists that will be available only at release time (Bug:647071).

 * '''Macbooks with EFI will not be able to boot the 64bit (amd64) version of Ubuntu 10.10 live cd.''' The i386 CDs will work. (Bug:633983)

 * '''When the XHCI module is loaded for USB 3.0 operation the system cannot suspend.''' Manually unloading XHCI will allow suspend to complete normally.  To avoid future suspend problems, the workaround is to add {{{SUSPEND_MODULES="xhci-hcd"}}} to {{{/etc/pm/config.d/unload_module}}} then the system can suspend normally. (Bug:522998)


 *'''Hibernation may be unavailable with automatic partitioning.''' The default partitioning recipe in the installer will in some cases allocate a swap partition that is smaller than the physical memory in the system.  This will prevent the use of hibernation (suspend-to-disk) because the system image will not fit in the swap partition.  If you intend to use hibernation with your system, you should ensure that the swap partition's size is at least as large as the system's physical RAM. (Bug:345126)

 * '''I/O error after CD is ejected at end of install.'''  In some cases, ejecting the CD at the end of installation will leave errors on the screen such as:

{{{
end_request: I/O error, dev sr0, sector 437628
}}}

these error messages indicate that the system is still trying to access some files on the CD, and are harmless except that they obscure the message asking the user to press Enter to reboot.  You can safely remove the CD from the tray and press Enter at this point to reboot to your new Ubuntu system. (Bug:539027)

 * '''Upstart jobs cannot be run in a chroot.''' Upstart jobs cannot be started in a chroot because upstart acts as a service supervisor, and processes within the chroot are unable to communicate with the upstart running outside of the chroot (Bug:430224).  This will cause some packages that have been converted to use upstart jobs instead of init scripts to fail to upgrade within a chroot.  Users are advised to configure their chroots with /sbin/initctl pointing to /bin/true, with the following commands run within the chroot:

{{{
dpkg-divert --local --rename --add /sbin/initctl
ln -s /bin/true /sbin/initctl
}}}

 * '''The version of upstart included since Ubuntu 9.10 no longer uses the configuration files in the /etc/event.d directory, looking to /etc/init instead.''' No automatic migration of changes to /etc/event.d is possible. If you have modified any settings in this directory, you will need to reapply them to /etc/init in the new configuration format by hand. (Bug:402759)

== File Systems and Disk Device Setup ==

 * '''Performance regressions with ext4 under certain workloads.'''  The default file system for installations of Ubuntu 10.10 is `ext4`, the latest version in the popular series of Linux extended file systems.  `ext4` includes a number of performance tuning changes relative to previous versions such as `ext3`, the file system used by default up to Ubuntu 9.04.  These generally produce improvements, but some particular workloads are known to be significantly slower when using `ext4` than when using `ext3`.  If you have performance-sensitive applications, we recommend that you run benchmarks using multiple file systems in your environment and select the most appropriate.

 * '''Use of degraded RAID 1 array may cause data loss in exceptional cases.'''  If each member of a RAID 1 array is separately brought up in degraded mode across subsequent runs of the array with no reassembly in between, there is a risk that the disks will be reported as in sync when they are not, resulting in data loss due to inconsistencies between the data that has been written to each member. This is an unlikely occurrence during normal operations, but admins of systems using RAID 1 arrays should take care during maintenance to avoid this situation. (Bug:557429)

 * '''Cryptsetup is not by default compatible with the version in 10.04LTS.'''  An encrypted disk set up under 10.04LTS will fail to properly mount under maverick. This is because, as documented in the {{{/usr/share/doc/cryptsetup/NEWS.Debian.gz}}}, defaults have changed. So to mount a disk which was created in 10.04LTS with cryptsetup, in 10.10 you must specify the cipher as such: {{{cryptsetup -c aes-cbc-plain create h /dev/sdb1}}}  (Bug:622762)

== Graphics and Display ==

 * '''Connected DisplayPort monitors may prevent booting when using the nouveau video driver.''' (Bug:655795)

 * '''External monitor connected via DisplayPort is not recognized when using the nouveau driver.''' (Bug:655800)

 * '''Image distortion (vsync) on some AMD ATI cards with the proprietary drivers'''. (Bug:303697)

 * '''The new Xorg 1.9 available in Maverick is not compatible with nVidia based chipsets that use the (nvidia-96) and (nvidia-173) drivers.''' (Bug:626974)
 
 * '''The logo will not display during boot when using the Nvidia proprietary driver.''' (Bug:653274)

 * '''The wrong display port is chosen during install of Apple iMacs (Core i5).''' If you plug a second screen on the mini display port, you can install ubuntu normally using this 2nd screen. (Bug:542660)

 * '''Non-mirrored dual-screen setups may provide incorrect display on secondary monitor.''' (Bug:619663)

== Networking & WiFi ==

 * '''802.11n support for the iwlagn driver has been temporarily disabled.''' Intel is actively working to get this properly fixed up in the firmware. This workaround should be reverted once updated firmware is available. (Bug:630748)

 * '''"Additional drivers" proposes b43, but the installation fails with "Not supported low-power chip"'''. This affects some Dell Mini 9 models and potentially any system with BCM4312 adapters.(Bug:655111)

 * '''Ubuntu 10.10 does not  support the XDMCP protocol for remote graphical logins.''' Users who require XDMCP support will need to install another display manager, such  as wdm or xdm, for this functionality (Bug:408417).

 * '''New drivers preventing "sleep" problem for RTL8111/8168B gigabit network adapter (usually onboard) are missing.''' (Bug:573259)

 * '''Laptops using Intel Corporation PRO/Wireless 3945ABG experience reduced wifi speeds of the order of 1Mb/s.'''  To see if your laptop uses this card, type the following: "lspci -v | grep 3945ABG". (Bug:621265)

 * '''Avahi will always start even if a .local domain is present.'''  The {{{avahi-daemon}}} package, which implements the mDNS "zeroconf" standard, formerly included a check to avoid running when a conflicting {{{.local}}} DNS domain is present, as it was reported that some ISPs advertise such a {{{.local}}} domain on their networks, leaving Ubuntu hosts unable to see names advertised on the local network (Bug:327362).  In Ubuntu 9.10, {{{avahi-daemon}}} is started regardless.  It is possible that this may cause other problems.  If your network is configured this way, you can disable mDNS using the following command:

{{{
sudo stop avahi-daemon
sudo sed -e '/^start/,+1s/^/#/' /etc/init/avahi-daemon.conf
}}}

== Input devices ==

 *'''Some fingerprint readers normally supported by fprint are not fully supported yet.''' Installing fprint from the latest PPA may work (Bug:640083, Bug:657017, Bug:657031). See [[https://bugs.edge.launchpad.net/ubuntu/+source/libfprint|the current bug list for libfprint0]] to see if your device is affected and possible workarounds.
 

== Common Desktop Applications ==

 *'''When running on battery, clicking on the battery icon permanently says "Battery life (estimating...)".''' This affects some HP, Compaq, Dell and System76 systems (Bug:629258).

 *'''Resizing windows with the Ambiance theme by grabbing window borders is difficult.''' This can be mitigated by switching to the Dust or Clear Looks theme (Bug:160311).

 *'''Several panel applets may be displayed twice or overlap.''' (Bug:439448).

 *'''It is not possible to create Ubuntu 10.04 USB disks from the Startup Disk Creator in Ubuntu 10.10 due to a backwards incompatibility in the syslinux program.'''

 *'''Adobe Air is not available for 64-bit.'''

 *'''GDM does not support XDMCP.''' The version of {{{gdm}}} included in Ubuntu 10.10 does not support the XDMCP protocol for remote graphical logins.  Users who require XDMCP support will need to install another display manager, such as {{{wdm}}} or {{{xdm}}}, for this functionality. (Bug:408417)

 *'''When uploading a file to a website, the file browse window doesn't show a preview when an image is selected.''' This only happens on some websites, when Flash is installed. It appears such websites replace the Nautilus "Browse" dialog with a Flash version (Bug:613886).

 *'''The Gwibber micro-blogging client no longer permits synching of account details across computers.'''  The client was switched to SQLite for back end  storage and to make it faster, but means that syncing of account details across computers is no longer supported.

 *'''The Cheese webcam application has video recording related performance regressions.''' (Bug:610600)

 *'''The Nautilus file manager application will sometimes create a non-existent device after the mount and umount of a device.''' (Bug:548546)

== Ubuntu Server Edition ==

 * '''As a security improvement, libvirt in Maverick runs kvm with limited rights.''' This disables the possibility of displaying a local SDL window (Bug:615077). Users are advised to use the VNC support instead.

 * '''If you configure apache to use a password-protected SSL key, you cannot specify the key passphrase at boot-time.''' To work around this, Apache needs to be started manually after boot (Bug:582963)

 * '''libdbi 0.8.3 has a known ABI incompatibility with earlier versions of libdbi that have been distributed with past versions of Ubuntu and Debian.''' As such, any third-party software linked against libdbi.so.0 may give unexpected results if they utilize the 'dbi_error_flag' enum. Recompiling these applications will resolve this issue. (Bug:625882)

 * '''Previous libvirt versions would probe a qemu disk to determine its format and did not require that the format be declared in the XML.''' This is considered a security problem in most deployments and newer versions of libvirt will default to the 'raw' format when the format is not specified in the XML. As a result, non-raw disks without a specified disk format will no longer be available in existing virtual machines. The libvirt-migrate-qemu-disks tool is provided to aid in transitioning virtual machine definitions to the new required format. In essence, it will check all domains for affected virtual machines, probe the affected disks and update the domain definition accordingly. This command will be run automatically on upgrade. For new virtual machines using non-raw images, the disk format must be specified in the domain XML provided to libvirt, otherwise the disk will not be available to the virtual machine. See {{{man 1 libvirt-migrate-qemu-disks}}} for details. Users who require the old behavior can adjust the 'allow_disk_format_probing' option in /etc/libvirt/qemu.conf.

  * '''NSS resolution breaks with LDAP over SSL'''  Upgrading systems configured to use LDAP via SSL as the first service in the NSS stack (in /etc/nsswitch.conf) leads to broken NSS resolution afterwards such that `setuid` applications like `sudo` would stop working.  To work around this, switch to the libnss-ldapd package instead of libnss-ldap before the upgrade, or use nscd. (Bug:423252)

== Ubuntu Netbook Edition ==

 *'''UNE needs graphical driver acceleration to be able to run.'''  Otherwise, you should be warned about missing them and will be logout and proposed to run standard ubuntu desktop session.

 *'''The targeted netbooks were intel GPU graphic mainly and was heavily tested on nvidia as well.'''  You may encounter visual glitches, and Unity may not work altogether on some ATI cards.

 *'''Newly installed UNE 10.10 does not have a guest session.''' (Bug:657371)

 *'''Certain applications such as Firefox and Shotwell do not use the global menu.  Certain applications such as Glade may not be functioning properly with the global menu.'''

== ARM ==

 *A separate page has been made available with release notes for the developer-oriented Ubuntu 10.10 armel port.  Please see [[https://wiki.ubuntu.com/ARM/MaverickReleaseNotes]] for information about issues affecting installation on specific ARM boards.

 *'''Users upgrading beagle (armel omap) from lucid (10.04 LTS) to maverick (10.10) can run out of free space if USB drive is 4G or less.'''

 *'''After installing the system on the Dove architecture, you may see many a text screen with errors that say "end_request: I/O error".''' However, this has not seemed to cause any installs to fail. Pressing 'enter' on this screen will reboot the system, but a message should have been displayed here warning you to remove the install media first. (Bug:539027)

 *'''Cannot suspend Ubuntu ARM images for Panda Boards(OMAP4).''' Due to current hardware limitations it is not possible to use suspend on the Ubuntu ARM images for the Panda Boards(OMAP4) even though the suspend option is shown in the logout menu.  (Bug:628029)

 *'''Sound is not working on the Dove A0 boards, OMAP3 Beagleboards, and OMAP4 Panda boards.''' (Bug:644028, Bug:651302, Bug:637947)

 *'''On Dove X0 based hardware, if you have speakers or headphones plugged into the headphone jack on the board, you will need to make some adjustments to hear audio.''' Under sound preferences, click the "Output" tab and select "Analog Headphones" for the connector. (Bug:551249)

== Kubuntu ==

 *'''In many cases desktop effects are not active by default or on login in Kubuntu even for systems with video systems that support the current default effects well.''' These can be manually enabled in SystemSettings -> Desktop Effects, but in order to continue to have effects enabled on login, it is necessary to disable hardware checks in the advanced tab of desktop effect settings. Before bypassing these check, do verify that your system is working correctly with effects enabled. (Bug:628930)

 *'''On some Kubuntu systems, the display server crashes on logout instead of returning to the KDE Display Manger (KDM) login display.''' For systems with this problem, the problem can be avoided by changing the method KDM uses to interact with the display server. Edit /etc/kde4/kdm/kdmrc and uncomment the line "#TerminateServer=true" by changing it to "TerminateServer=true" and restart KDM (reboot the system or sudo restart kdm). (Bug:651294)

 *'''The Global Menu may not show gtk applications' menus.''' You will need to install the package ''appmenu-gtk''.

 * '''Updates not downloaded during install when selected and internet is available during install''' the can be downloaded after install through the normal update method (Bug: 634664)

 * '''Ubiquity not removed after OEM install''' This makes the favourites in Plasma Netbook show the installer after the user setup (Bug: 651086)

 * '''KDevelop crashes''' Fix will be released soon, or use the new Beta packages [[http://www.kubuntu.org/news/kdevelop-41-rc-and-koffice-23-beta-1-packaged|the new Beta packages]] or update to [[http://www.kubuntu.org/news/kde-sc-4.5.2|KDE Platform 4.5.2]] (Bug: 656195)

 * '''Dist Upgrade tool does not allow viewing conffile changes''' this causes a Qt plugin to get loaded which can crash the upgrade tool if Qt has already been upgraded.  You can view the changes manually on the command line with ''diff -u <filename> <filename>.dpkg-new''  (Bug: 656876)

 * '''New user can't log in''' After a new user is created in Kubuntu systemsettings, they will be prompted to change their password when they log in for the first time. There is an issue in 10.10 that prevents the new password from being entered.  In order to avoid this problem, the X server needs to be restarted before the new user logs in.  After logout, click on the red logout button on the KDM screen and then click on "Restart X Server". Once the KDM login screen returns, the new user should be able to log in normally. (Bug: 641712)

== Mythbuntu ==

 *'''On KMS hardware, the background might not be stable during installation.'''

 *'''No way to currently configure the backend until after installation.'''

== Edubuntu ==

 *'''During an upgrade, Edubuntu will prompt the user whether they would like to use GDM or KDM. GDM should be be chosen to maintain current configuration.''' (Bug 650615)


== Ubuntu One ==
 *'''In certain specific circumstances, the Nautilus file manager may crash while trying to search folders sync'd by the Ubuntu One sync daemon.''' (Bug:617656)

== Others ==

'''For a listing of more known issues, please refer to the Maverick Meerkat [[https://bugs.launchpad.net/ubuntu/maverick/+bugs|bug tracker]] in Launchpad.'''
