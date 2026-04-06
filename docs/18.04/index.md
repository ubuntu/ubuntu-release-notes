---
tocdepth: 3
---

(ubuntu-18-04-lts-release-notes)=
# Ubuntu 18.04 LTS "Bionic Beaver" Release Notes

<!-- Source: https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes -->

## When adding features to this page, please add credits for the relevant upstream developers where appropriate.
||<tablestyle="float:right; width:40%; background:#F1F1ED; margin: 0 0 1em 1em;" style="padding:0.5em;">'''Table of Contents'''<<BR>> <<TableOfContents(3)>>||

'''WARNING: Release reached End of Life'''

'''This release is no longer supported, please see [[Releases]]'''

'''WARNING: Release reached End of Life'''

= Introduction =

These release notes for '''Ubuntu 18.04.6 LTS''' (Bionic Beaver) provide an overview of the release and document the known issues with Ubuntu 18.04 LTS and its flavors.  For details of the changes applied since 18.04, please see the [[BionicBeaver/ReleaseNotes/ChangeSummary/18.04.5|18.04.5 change summary]].  The release notes for [[BionicBeaver/ReleaseNotes/18.04|18.04]], [[BionicBeaver/ReleaseNotes/18.04.1|18.04.1]], [[BionicBeaver/ReleaseNotes/18.04.2|18.04.2]], [[BionicBeaver/ReleaseNotes/18.04.3|18.04.3]] and [[BionicBeaver/ReleaseNotes/18.04.4|18.04.4]] are available as well.

=== Support lifespan ===
The 'main' archive of Ubuntu 18.04 LTS will be supported for 5 years until [[Releases|April 2023]]. Ubuntu 18.04 LTS will be supported for 5 years for Ubuntu Desktop, Ubuntu Server, and Ubuntu Core. Ubuntu Studio 18.04 will be supported for 9 months. All other flavors will be supported for 3 years. 

=== Official flavor release notes ===
Find the links to release notes for official flavors [[#Official_flavours|here]].

<<BR>>
= Get Ubuntu 18.04.6 LTS =
== Download Ubuntu 18.04.6 LTS ==

Images can be downloaded from a location near you.

You can download ISOs and flashable images from:
http://releases.ubuntu.com/18.04.6/ (Ubuntu Desktop and Server) <<BR>>
http://cdimage.ubuntu.com/ubuntu/releases/18.04.6/release/ (Less Popular Ubuntu Images) <<BR>>
http://cloud-images.ubuntu.com/daily/server/bionic/current/ (Ubuntu Cloud Images) <<BR>>
http://cdimage.ubuntu.com/netboot/18.04.5/ (Ubuntu Netboot) <<BR>>
http://cdimage.ubuntu.com/kubuntu/releases/18.04.5/release/ (Kubuntu) <<BR>>
http://cdimage.ubuntu.com/lubuntu/releases/18.04.5/release/ (Lubuntu and Lubuntu Alternate) <<BR>>
http://cdimage.ubuntu.com/ubuntu-budgie/releases/18.04.5/release/ (Ubuntu Budgie) <<BR>>
http://cdimage.ubuntu.com/ubuntukylin/releases/18.04.5/release/ (Ubuntu Kylin) <<BR>>
https://ubuntu-mate.org/download/ (Ubuntu MATE) <<BR>>
http://cdimage.ubuntu.com/xubuntu/releases/18.04.5/release/ (Xubuntu)


== Upgrading from Ubuntu 16.04 LTS or 17.10 ==

To upgrade on a desktop system:
 * Open the "Software & Updates" Setting in System Settings.
 * Select the 3rd Tab called "Updates".
 * Set the "Notify me of a new Ubuntu version" drop down menu to "For long-term support versions" if you are using 16.04 LTS; set it to "For any new version" if you are using 17.10.
 * Press Alt+F2 and type ` update-manager -c  ` into the command box.
 * Update Manager should open up and tell you that Ubuntu 18.04 LTS is now available.
 * If not you can run ` /usr/lib/ubuntu-release-upgrader/check-new-release-gtk`
 * Click Upgrade and follow the on-screen instructions.

To upgrade on a server system:
 * Install  ` update-manager-core ` if it is not already installed.
 * Make sure the {{{Prompt}}} line in /etc/update-manager/release-upgrades is set to 'normal' if you want non-LTS upgrades, or 'lts' if you only want LTS upgrades.
 * Launch the upgrade tool with the command ` sudo do-release-upgrade `
 * Follow the on-screen instructions.
Note that the server upgrade will use GNU screen and automatically re-attach in case of dropped connection problems.

There are no offline upgrade options for Ubuntu Desktop and Ubuntu Server. Please ensure you have network connectivity to one of the official mirrors or to a locally accessible mirror and follow the instructions above.

<<BR>>
= New features in 18.04 =

 * For other changes since 16.04 LTS, see the [[ArtfulAardvark/ReleaseNotes|17.10 Release Notes]],[[ZestyZapus/ReleaseNotes|17.04 Release Notes]] and [[YakketyYak/ReleaseNotes|16.10 Release Notes]].

== 32-bit PowerPC Support Dropped ==

  * The '''powerpc''' port is not included in the 18.04 release. See [[https://lists.ubuntu.com/archives/ubuntu-devel-announce/2016-December/001199.html|announcement]] for details.
  * '''ppc64el''' support support continues as previously.

== Updated Packages ==

Ubuntu 18.04.4 ships with a v5.3 based Linux kernel updated from the v5.0 based kernel in 18.04.3.  This enables the latest hardware and peripherals available from IBM, Intel, and others. The 18.04 kernel delivers new features inherited from upstream, including:

 * New support for a number of new Intel and AMD graphics chipsets
 * New default networking queue management algorithms to improve networking on slow and congested links
 * Preliminary support for WiFi 6 (802.11ax)
 * BTRFS swap file support
 * New block I/O latency controller
 * Numerous security related improvements

We also see notable Ubuntu specific achievements with:

 * Further AppArmor and security module improvements
 * shiftfs filesystem providing LXD performance improvements

As well as the usual myriad of bug fixes for supported platforms.

=== OpenJDK ===

As of 18.04.4, OpenJDK 11 is the default in 18.04.

OpenJDK 8 has moved to universe and will remain available there for the life of 18.04, to provide migration time for packages, custom applications, or scripts that can't be build with OpenJDK 11. OpenJDK 8 will be updated in 18.04 until Ubuntu 16.04 LTS reaches EOL in April 2021.

=== OpenSSL ===

The default OpenSSL has been upgraded from 1.1.0 to 1.1.1 LTS series bringing improved performance and ability to use TLSv1.3 in select packages. Co-installable 1.0.2n series OpenSSL remains to be available as well.

== Security Improvements ==

In Ubuntu 18.04 LTS, gcc is now set to default to compile applications as position independent executables (PIE) as well as with immediate binding, to make more effective use of Address Space Layout Randomization (ASLR). All packages in main have been rebuilt to take advantage of this, with a few exceptions. 

Mitigations are in place to protect against Spectre and Meltdown. See the [[https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/SpectreAndMeltdown|Spectre and Meltdown KnowledgeBase article]] for more details about the remediation and [[https://wiki.ubuntu.com/SecurityTeam/KnowledgeBase/SpectreAndMeltdown/MitigationControls|configuration options]].

'''`bolt`''' and '''`thunderbolt-tools`''' have been promoted to main to provide security controls for Thunderbolt devices.

=== Default CIFS/SMB protocol version change in CIFS mounts ===
Since 17.10, the default SMB protocol used when mounting remote CIFS filesystems via `mount.cifs` (from the `cifs-utils` package) changed to 2.1 or higher, depending on what is negotiated with the server. If no version is specified when mounting such a remote share, the following will be logged:
{{{
No dialect specified on mount. Default has changed to a more secure dialect, SMB2.1 or later (e.g. SMB3),
from CIFS (SMB1). To use the less secure SMB1 dialect to access old servers which do not support SMB3
(or SMB2.1) specify vers=1.0 on mount.
}}}

Should you encounter compatibility issues, like [[https://bugs.launchpad.net/ubuntu/+source/sssd/+bug/1764778|#1764778]] or [[https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1572132|#1572132]], please specify `vers=1.0` when mounting the share and please file a bug if that fixes the problem for you.

=== Improved UEFI Secure Boot handling for the use of third-party modules ===

Ubuntu now allows you to generate a signing key when needed, as you install third-party (DKMS) modules. On install of a DKMS package, you will be prompted to enter a password that is used to enroll a signing key (an X509 certificate) that will then be used to sign the new kernel modules. The prompts will allow you to enter the same password twice, and describe the steps needed to enroll the new key at the next reboot. For more information, see https://wiki.ubuntu.com/UEFI/SecureBoot/DKMS.


== Network configuration ==

=== New since 18.04.2 ===

'''[[https://netplan.io/|netplan.io]]''' has grown support for IPv6 Privacy Extensions, DHCP overrides, improved error reporting, support for WPA Enterprise wifi and 802.1x authentication, as well as support for IP tunnels.

'''[[https://netplan.io/|netplan.io]]''' now will bring up network devices even if no IP address is specified for them, as long as they are configured in a file in /etc/netplan. This allows configuring "anonymous" bridges and integration with other networked services.

=== New since 17.10 ===
Teaming support with libteam is available in NetworkManager.

=== New since 16.04 LTS ===

The default DNS resolver is systemd-resolved. 

'''`ifupdown`''' has been deprecated in favor of '''[[https://netplan.io/|netplan.io]]''' and is no longer present on new installs. The installer will generate a configuration file for netplan.io in the ''/etc/netplan'' directory.  This netplan.io configuration in turn renders backend-specific configuration via either systemd-networkd or NetworkManager.  Desktop users will see their system fully managed via NetworkManager as it has been the case in previous releases.  Server users will now see their network devices managed via systemd-networkd. This only applies to new installations.

Given that `ifupdown` is no longer installed by default, the commands: `ifup` and `ifdown` are also unavailable. Please use the `ip` command to achieve similar functionality, specifically `ip link set $device up` and `ip link set $device down`.

The '''`networkctl`''' command is now available for users to see a summary of network devices. `networkctl status` will display the current global state of IP addresses on the system. `networkctl status $device` displays details specific to a network device.

The `ifupdown` package remains available and supported in Ubuntu main for users that find netplan does not currently meet their networking needs.

For more information about netplan.io, please refer to the manual page using the `man 5 netplan` command or visit https://netplan.io/.

Scripts in `/etc/network/ifup.d` and `/etc/network/ifdown.d` no longer work in this new configuration. For the systemd-networkd backend, similar scripts can be added into subdirectories of `/usr/lib/networkd-dispatcher` (`dormant.d`, `no-carrier.d`, `off.d`, `routable.d`), if `networkd-dispatcher` is installed. Later on, custom scripts can be placed in `/etc/networkd-dispatcher` and potentially also override the ones in `/usr/lib`.

== Other base system changes since 16.04 LTS ==

 * The '''`gpg`''' binary is provided by [[https://debian-administration.org/users/dkg/weblog/116|gnupg2]]
 * For new installs, a '''swap file''' will be used by default instead of a swap partition.
 * '''Python 2''' is no longer installed by default. Python 3 has been updated to 3.6. This is the last LTS release to include Python 2 in main.
 * The installer no longer offers the encrypted home option using ecryptfs-utils. It is recommended to use full-disk encryption instead for this release. (Bug:1756840)
 * OpenSSH now refuses to use RSA keys smaller than 1024 bits. `ssh-keygen -l -f /path/to/key.pub` can report the length of a key.

== Ubuntu Desktop ==

=== Updates and fixes in 18.04.2 ===
 * Fixed a bug which prevented the login screen from appearing on early generation Intel GPUs (Core2 and Atom etc) (Bug:1727356)
 * Fixed memory leak in Nautilus (Bug:1798426)
 * Fixed OSK bug preventing uppercase letters being entered (Bug:1730211)
 * Fixed bug where two instances of an application were launched if you touched on the dock (Bug:1745888)
 * Updated Firefox to version 65
 * Updated !LibreOffice to 6.0.7
 * Updated Thunderbird to 60.4.0
 * Fixed a bug which caused the dock to show on the lock screen (Bug:1769383)
 * Fixed a bug with Livepatch notifications startup ordering causing missing notifications (Bug:1809505)
 * Made some performance improvements to GNOME Shell (Bug:1803271, Bug:1743976)

=== New since 17.10 ===
 * X is the default display server. '''Wayland''' is provided as a Technical Preview and is expected to be the default display server in 20.04 LTS. To try it out, just choose ''Ubuntu on Wayland'' from the cog on the log in screen.  X.org logs may now be found at ~/.local/share/xorg
 * The installer offers a '''minimal install''' option for a basic desktop environment with a web browser and core system utilities. Many official 18.04 desktop flavors are using this new feature too!
 * Apps provided by GNOME have been updated to '''3.28'''. For more details about GNOME 3.28, see their [[https://help.gnome.org/misc/release-notes/3.28/|Release Notes]].
 * '''!LibreOffice''' has been updated to [[https://wiki.documentfoundation.org/ReleaseNotes/6.0|6.0]].
 * Emoji now show in '''color''' in most apps. Keyboard shortcuts for the emoji input chooser are Ctrl+. or Ctrl+;
 * '''Calendar''' now supports weather forecasts.
 * Some utilities have been switched to the '''snap''' format for new installs (Calculator, Characters, Logs, and System Monitor). Snap apps provide better isolation which allows them to be upgraded to new stable releases during the LTS lifecycle.
 * The '''Characters''' app replaces the older Character Map by default.
 * The Ubuntu Software app allows easy switching between different '''channels''' for Snap apps.
 * The '''To Do''' app has been added to the default normal install.
 * '''spice-vdagent''' is pre-installed for better performance for Spice clients such as the GNOME Boxes app.
 * The right-click method for touchpads without physical buttons has changed to a '''two-finger click''' instead of clicking in the bottom right of the touchpad. You can use the GNOME Tweaks app (not installed by default) to change this setting.
 * Although libinput is the default driver for mice and touchpads, it is now possible to use the '''synaptics'''  driver with the Settings app. Support for the synaptics driver will be dropped in a future Ubuntu release.
 * Computers will '''automatically suspend''' after 20 minutes of inactivity while on battery power.
 * GNOME Shell now supports '''Thunderbolt 3'''.

=== Other highlights since 16.04 LTS ===

 * '''32-bit''' installer images are no longer provided for Ubuntu Desktop.
 * The Ubuntu Desktop now uses '''GNOME''' instead of Unity.
 * '''GDM''' has replaced LightDM as the default display manager. The login screen now uses virtual terminal 1 instead of virtual terminal 7.
 * Window control buttons are back on the '''right'''.
 * '''Driverless printing support''' is now available.
 * GNOME's built-in '''screen keyboard''' is used instead of Onboard.
 * '''Calendar''' has a Week View and supports recurring events.
 * These apps have received major user interface redesigns: Disk Usage Analyzer, Files (nautilus), Remmina, Settings, and Ubuntu Software.
 * System Log has been replaced by '''Logs''', an app to view logs from the systemd journal.
 * Many GNOME apps now have a '''Keyboard Shortcuts''' popup available in the app menu.
 * '''gconf''' is no longer installed by default since it has long been superseded by gsettings. Note that statistics and preferences for the Aisleriot card games will be reset when upgrading from 16.04 LTS or 16.10. gconf will be removed from the Ubuntu package archives in a future Ubuntu release.
 * The '''Ubuntu GNOME''' flavor has been discontinued. If you are using Ubuntu GNOME, you will be upgraded to Ubuntu. Choose the ''Ubuntu'' session from the cog on the login screen if you would like the default Ubuntu experience.
 * Install '''gnome-session''' then restart your computer and choose ''GNOME'' (or ''GNOME on Wayland'') from the cog on the login screen if you would like to try a more upstream version of GNOME. If you'd like to also install more core apps, install the '''vanilla-gnome-desktop''' metapackage.

== Ubuntu Server ==

=== Updates and fixes in 18.04.2 ===

 * Only "main" component enabled after install (Bug:1783129)
 * /etc/default/grub.d/50-curtin-settings.cfg overwrites GRUB_CMDLINE_LINUX_DEFAULT (Bug:1527664)
 * Install failed on disk previously used for ZFS (Bug:1782744)

=== New since 17.10 ===

=== Server installer ===

The next generation [[https://github.com/CanonicalLtd/subiquity|Subiquity]] server installer, brings the comfortable live session and speedy install of Ubuntu Desktop to server users at last.

N.B., If you require multipath you will want to continue to use the alternate installer which can be downloaded from http://cdimage.ubuntu.com/releases/18.04/release/

A new feature in the server installer in 18.04.3 is that it automatically checks for a new version of the installer snap on startup and offers to update to a new version if it is available.

Also new in 18.04.3 is support for encrypted LVM volume groups and reusing existing partitions, as well as LVM, RAID, vlans, and bonds which were added in 18.04.1.

There are some known limitations in the reuse of existing partitions:

 * [[https://bugs.launchpad.net/subiquity/+bug/1837214|Reusing a partition that was part of an LVM volume group or RAID can fail]]. This can be worked around by switching to another tty and destroying the RAID or VG by hand, then restarting. If there is no other data on the same drive that you want to keep, reformatting the drive entirely also works.
 * [[https://bugs.launchpad.net/subiquity/+bug/1837217|The installer cannot add or remove individual partitions]]. You can format (or not) and mount existing partition, but not add a partition to free space or remove a single partition from a drive.

We hope to fix both of these limitations via snap updates well before the next point release.

=== netplan.io ===

'''`ifupdown`''' has been deprecated in favor of '''[[https://netplan.io/|netplan.io]]''' and is no longer present on new installs. Backend configuration on Ubuntu Server by default is provided by '''[[http://manpages.ubuntu.com/manpages/bionic/man8/systemd-networkd.service.8.html|systemd-networkd]]'''.

Please see the [[#Network_configuration|Network configuration]] section of these release notes.

=== LXD 3.0 ===

'''LXD''' is the system container manager that ships with all Ubuntu servers.

Ubuntu 18.04 includes the all new LXD 3.0 release, some of the highlights include:

   * Clustering of LXD servers (one big virtual LXD)
   * Support for NVIDIA runtime passthrough
   * Remote transfer of custom storage volumes
   * Extended /dev/lxd API inside the containers
   * Support for port redirection
   * Numerous improvements to the command line tools

To learn more about LXD 3.0, read the [[https://discuss.linuxcontainers.org/t/lxd-3-0-0-has-been-released/1491|release announcement]].

A new external tool called '''`lxd-p2c`''' is also available to turn existing systems into LXD containers.

=== QEMU 2.11.1 ===

'''QEMU''' has been updated to the 2.11.1 release.

See the [[http://wiki.qemu.org/ChangeLog/2.11|Changelog]] for major changes since Artful.

Among many other changes, fixes around [[https://meltdownattack.com/|Meltdown/Spectre]] are included. Since fully utilizing these mitigations needs more than just an upgrade, it is recommended to read details at the [[https://www.qemu.org/2018/02/14/qemu-2-11-1-and-spectre-update/|qemu.org blog post]].

QEMU in Ubuntu 18.04 now has rdma support enabled as over the past year much unification in the [[https://github.com/linux-rdma/rdma-core|rdma-core]] project has occured.  

Migrations from former versions are supported just as usual.  When upgrading it is always recommended to [[https://wiki.ubuntu.com/QemuKVMMigration#Upgrade_machine_type|upgrade the machine types]] allowing guests to fully benefit from all the improvements and fixes of the most recent version.

=== libvirt 4.0 ===

'''`libvirt`''' has been updated to version 4.0. See the upstream [[https://libvirt.org/news.html|Changelogs]] for details since version 3.6 that was in [[https://wiki.ubuntu.com/ArtfulAardvark/ReleaseNotes|Artful]].

The packaging now builds libvirt storage drivers as pluggable libraries.  This slims down the installation requirements but some drivers of less general interest will now be found in [[https://help.ubuntu.com/community/Repositories/Ubuntu|universe]]. (ex: gluster, sheepdog, zfs). On the other hand that means that a few formerly integrated features like rbd or zfs now might require you to install the package after upgrade e.g. in this case libvirt-daemon-driver-storage-zfs.


=== DPDK 17.11.x ===

Ubuntu includes 17.11.x the latest stable release branch of '''DPDK'''.

See the [[http://dpdk.org/doc/guides/rel_notes/release_17_11.html|Release Notes]] for details.

By the new [[https://wiki.ubuntu.com/StableReleaseUpdates/DPDK|Stable Release exception for DPDK]] future stable updates to 17.11.x will be made available to Ubuntu 18.04

=== Open vSwitch 2.9 ===

'''Open vSwitch''' has been updated to 2.9.

Please read the [[http://openvswitch.org/releases/NEWS-2.9.0|release notes]] for more detail.

=== Chrony ===

In Ubuntu 18.04 '''[[https://chrony.tuxfamily.org/|chrony]]''' will replace '''`ntpd`''' as the recommended server for the NTP protocol.  See the [[https://chrony.tuxfamily.org/news.html|upstream changelog]] for an overview of recent changes as well as the [[https://chrony.tuxfamily.org/faq.html|FAQ]] which will help for smooth conversions from NTP.

The [[https://chrony.tuxfamily.org/comparison.html|comparison]] among ntp servers by the chrony maintainers may interest some users looking to see a high level reason why this change was made.  It does lack the rather new and not yet completely ready [[https://www.ntpsec.org/|ntpsec]], but otherwise is a fair analysis.

For simple time sync needs the base system already comes with [[https://www.freedesktop.org/software/systemd/man/timedatectl.html|systemd-timesyncd]]. Chrony is only needed to act as a time server or if you want the advertised more accurate and efficient syncing.

Going along with this change, `ntpd` has been demoted from [[https://help.ubuntu.com/community/Repositories/Ubuntu|main to universe]]. `ntpd` will continue to work but will only receive best-effort security maintenance.  When upgrading to Ubuntu 18.04 it is highly recommended to migrate to '''`chrony`''' if you had set up `ntpd` before.


=== cloud-init ===
The version was updated to [[https://launchpad.net/cloud-init/trunk/18.2|18.2]]. Notable new features include:

 * VMware: support for 64-bit platforms and identifying OVF datasource provided
 * GCE: Improvements and changes to ssh key behavior for default user.
 * Azure pre-provisioning speed improvements
 * NoCloudKVM and EC2 tests now run in continuous integration.
 * New cloud support: IBMCloud and HetznerCloud now have official datasources and OpenTelekom is now recognized by cloud-id
 * OpenNebula: Improve network configuration support.
 * New cloud-init command-line tools available: status, analyze and clean
 * New ubuntu cloud-config modules for managing snaps and ubuntu-advantage services

=== curtin ===

The version was updated to [[https://launchpad.net/curtin/trunk/18.1|18.1]]. Notable features include:

 * Add experimental zpool and zfs filesystem support, including ZFS on root.
 * Add support for installing remote sources that are a filesystem image.  ([[https://bugs.launchpad.net/bugs/1746348|1746348]])
 * Add pollinate user-agent configuration support.
 * Improved device teardown of dirty devices to support re-deployment ([[https://bugs.launchpad.net/bugs/1750519|1750519]]) ([[https://bugs.launchpad.net/bugs/1743643|1743643]])  ([[https://bugs.launchpad.net/bugs/1713537|1713537]]) ([[https://bugs.launchpad.net/bugs/1722322|1722322]]) ([[https://bugs.launchpad.net/bugs/1708052|1708052]]) ([[https://bugs.launchpad.net/bugs/1718699|1718699]])
 * Default config now automatically tars curtin logs upon error using new `curtin collect-logs` command.
 * storage: accept filesystem mount options ([[https://bugs.launchpad.net/bugs/1709284|1709284]])
 * Extensive integration test coverage and improvements.

=== MAAS ===

The version was updated to [[https://launchpad.net/maas/2.4|2.4b2]]. Notable features include:

 * Add audit logging
 * Add KVM pod support to create tags, select the storage pool, and compose machines with multiple storage pools.
 * Add UI for DNS management
 * Add the commissioning template framework for HBA management.
 * Add the commissioning template framework for Firmware Upgrades.
 * Improve UI performance by performance.
 * Improve MAAS' backend performance and
 * Improve the UI for the Settings.
 * Add experimental support to configure zfs as the root filesystem.
 * Switch to use Chrony instead of ntp.

For more information, please visit the [[https://maas.io|MAAS website]] or review the [[https://docs.maas.io/devel/en/release-notes|2.4 Release Notes]].

=== SSSD ===
SSSD was updated to version 1.16.x and its secrets service is now enabled. Previously it was disabled because it required the http-parser library which lived in Universe, but a successful MIR brought it to main so SSSD could link with it.

The defaults for autofs related configuration settings changed in SSSD 1.14.0 (see https://pagure.io/SSSD/sssd/issue/2858). If you are upgrading from SSSD 1.13 in Xenial, you might have to explicitly specify all `ldap_autofs_*` settings in your `sssd.conf` to match your data in LDAP.

These are the defaults, based on the setting of `ldap_schema`:
|| '''sssd.conf setting''' || '''xenial default''' || '''bionic default''' ||
|| ldap_autofs_map_object_class || automountMap || nisMap (rfc2307, autofs_provider=ad), otherwise automountMap ||
|| ldap_autofs_map_name || ou (rfc2307), automountMapName (rfc2307bis, ipa, ad) || nisMapName (rfc2307, autofs_provider=ad), otherwise automountMapName ||
|| ldap_autofs_entry_object_class || automount || nisObject (rfc2307, autofs_provider=ad), otherwise automount ||
|| ldap_autofs_entry_key || cn (rfc2307), automountKey (rfc2307bis, ipa, ad) || cn (rfc2307, autofs_provider=ad), otherwise automountKey ||
|| ldap_autofs_entry_value || automountInformation || nisMapEntry (rfc2307, autofs_provider=ad), otherwise automountInformation ||

 See [[https://bugs.launchpad.net/ubuntu/+source/sssd/+bug/1767886/comments/3|bug #1767886]] for details.

=== Samba ===
The vfs module `aio_linux` was removed from the `samba-vfs-modules` package (see [[https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=881239|Debian bug #881239]]), and it's nowadays also [[https://git.samba.org/?p=samba.git;a=commitdiff;h=6381044c0270a647c20935d|no longer present in upstream Samba code]]. The upstream [[https://bugzilla.samba.org/show_bug.cgi?id=13128|Samba bug #13128]] has more details.

If you had a configuration that included this module in a share, something like this:
{{{
[someshare]
    ...
    vfs objects = aio_linux
}}}
Then when this share is accessed, the server will notice it can't find the `aio_linux` module and fail. You should remove the `aio_linux` from the list of vfs objects that are being loaded.

Note that `testparm(1)` won't catch this type of error (see [[https://bugs.launchpad.net/samba/+bug/1778860|bug #1778860]]).

=== Nginx ===

[[http://nginx.org/|nginx]] was updated to version 1.14.0. New features include [[http://nginx.org/en/docs/http/ngx_http_mirror_module.html|the mirror module]], [[http://nginx.org/en/docs/http/ngx_http_v2_module.html#http2_push|HTTP/2 push]], and the [[http://nginx.org/en/docs/http/ngx_http_grpc_module.html|gRPC proxy module]].  

=== PHP ===
PHP was updated to version 7.2.x. For upstream guidance on migrating from PHP 7.1 (Artful's version) to 7.2: http://php.net/manual/en/migration72.php. Also of relevance might be the 7.0 to 7.1 migration documentation: http://php.net/manual/en/migration71.php.

=== Apache ===
Apache was updated to version 2.4.29. Additionally, HTTP/2 support is now enabled in 18.04.

=== landscape-client ===
landscape-client has been ported to Python 3 and is now available to install on the default image.

=== ubuntu-advantage-tools ===
 * New dynamic MOTD support for Canonical Livepatch. This indicates, at a glance, the status of livepatches when logging in on a console.
 * New ```enable-fips-updates``` command to enable a special FIPS repository with non-certified updates for FIPS enabled systems.

=== s390x-specific enhancements (since 17.10) ===
 * improvements for IBM z14,z14 ZR1,LinuxONE Rockhopper II and LinuxONE Emporer II (Bug:1725260) (Bug:1736100)
 * s390-tools major version upgrade to v2.3.0 (Bug:1735447)
 * cryptsetup rebase and enhancements in support of dm-crypt (Bug:1724592)
 * protected key support for dm-crypt (Bug:1741904)
 * TLB enhancements (Bug:1732426) (Bug:1732452)
 * TOD-Clock Epoch Extension Support (Bug:1732437) (Bug:1732691)
 * DASD multi-queue (Bug:1732446) support and block layer discard support (Bug:1732440)
 * Improved memory handling (Bug:1734120)
 * support for new crypto hardware CEX6S (Bug:1735437)
 * AP bus kernel API for KVM (Bug:1732449)
 * CPACF enhancements and acceleration for AES GCM (Bug:1735438) (Bug:1743750)
 * HiperSocket connections enhacements (Bug:1735695)
 * parted update for fdasd/vtoc (Bug:1737144)
 * openssl-ibmca rebase (Bug:1747626)
 * opencryptoki rebase for EP11 and ECC enhancement (Bug:1751272)
 * lock optimization enhancement (Bug:1747877)
 * libica upgrade for z14, several bug fixes (Bug:1737159) and to use PRNO-TRNG to seed SHA512-DRBG (Bug:1754617)
 * auto detect layer2 setting in qeth driver (Bug:1747639)
 * Kernel support for STHYI/LPAR (Bug:1736093)
 * rebase libpfm4 for z13/z13s CPU-MF hardware counters (Bug:1741905)

=== OpenStack Queens ===

Ubuntu 18.04 includes the latest !OpenStack release, Queens, including the following components:

 * !OpenStack Identity - Keystone
 * !OpenStack Imaging - Glance
 * !OpenStack Block Storage - Cinder
 * !OpenStack Compute - Nova
 * !OpenStack Networking - Neutron
 * !OpenStack Telemetry - Ceilometer, Aodh, Gnocchi, and Panko
 * !OpenStack Orchestration - Heat
 * !OpenStack Dashboard - Horizon
 * !OpenStack Object Storage - Swift
 * !OpenStack Database as a Service - Trove
 * !OpenStack DNS - Designate
 * !OpenStack Bare-metal - Ironic
 * !OpenStack Filesystem - Manila
 * !OpenStack Key Manager - Barbican

Please refer to the [[http://releases.openstack.org/queens/|OpenStack Queens release notes]] for full details of this release of !OpenStack.

!OpenStack Queens is also provided via the [[OpenStack/CloudArchive|Ubuntu Cloud Archive]] for !OpenStack Queens for Ubuntu 16.04 LTS users.

'''WARNING''': Upgrading an !OpenStack deployment is a non-trivial process and care should be taken to plan and test upgrade procedures which will be specific to each !OpenStack deployment.

Make sure you read the [[https://docs.openstack.org/charm-guide/latest/1802.html|OpenStack Charm Release Notes]] for more information about how to deploy Ubuntu !OpenStack using Juju.

=== ARM64 performance considerations ===
Ubuntu supports 4k page size, 64K page size has benefits to certain applications and benchmarks. Please follow this link for [[https://wiki.ubuntu.com/ARM64/performance|ARM64 performance considerations]] that may yield similar results with 4k page size.

= Known issues =

As is to be expected, with any release, there are some significant known bugs that users may run into with this release of Ubuntu 18.04.  The ones we know about at this point (and some of the workarounds), are documented here so you don't need to spend time reporting these bugs again:

== Kernel ==

  * The default I/O scheduler has changed.  SCSI multi-queue is now enabled for appropriate devices.  This changes the set of available I/O schedulers for that device to be only those schedulers which are multi-queue aware; currently only mq-deadline and none.  Testing has shown this to be advantageous in the common case.  This does however mean that manually selected schedulers may not be available leaving a unexpected scheduler enabled.  This affects both the kernel command line elevator= option and any udev rules for specific devices.

== Desktop ==

  * The computer suspends after 20 minutes of inactivity on battery power even if a user is logged in remotely. ([[https://gitlab.gnome.org/GNOME/gnome-control-center/issues/22|GNOME:gnome-control-center#22]])

  * Bluetooth audio devices cannot be used in the Greeter.  This will cause issues for people using the accessibility features such as screenreaders at the login screen.  Once logged in everything should work as expected.

  * Some admin utilities will not work with GNOME on Wayland since the apps have not been adapted to use PolicyKit to only use admin privileges for the specific functions needed. Also, some screenshot and screencast apps and all remote desktop server apps do not currently work on GNOME on Wayland. As a workaround, you can use the default Ubuntu session.

  * Exiting the live session may get stuck with a "A start job is running for " error. You may need to forcefully power off the computer if you see this. (Bug:1706939)

  * The Dock and Appindicator system extensions appear to be Off in tools like GNOME Tweaks. (They are on but cannot be disabled because they are system extensions for the Ubuntu session.) (Bug:1718850)

  * Tracker is not installed by default. When installed, you must log out and log back in for the tracker service to start (Bug:1697769)

  * Systems may fail to boot when connected over DisplayPort to an external screen, on NVidia graphics hardware such as the GTX970 chipset. (Bug:1723619)

  * When an external monitor is connected to a laptop, the login screen is only displayed on the internal one and in some case is not visible (Bug:1723025)

  * The warning dialog when a user force a UEFI installation does not respond to input event and the installation is then blocked at this stage (Bug:1724482) Avoid yourself some troubles and do not force a UEFI installation without a UEFI partition, grub-installer will fail anyway.

  * Doing an "Entire disk" installation over an existing LVM installation will fail because the installer selects the wrong boot device (Bug:1724417) Use custom partitioning instead and manually select the right boot device in the combo box.

  * The Files app [[https://didrocks.fr/2018/01/23/welcome-to-the-ubuntu-bionic-age-nautilus-a-lts-and-desktop-icons/|remains]] at 3.26.

  * Upgrading via the installer (Ubiquity) is deemed not safe due to bugs in apt-clone and so is no longer supported. (Bug:1756862) UIFE - remove ubiquity upgrade option.

  * Setting a ulimit may cause segfaults in certain applications, especially those using webkit2gtk. Disabling the ulimit should restore normal functionality.  More information in this Debian news entry: https://salsa.debian.org/webkit-team/webkit/blob/wk2/unstable/debian/NEWS


  * The installer can crash, especially noticeable on HiDPI screens where scaling has been applied (Bug:1751252).  The workaround is to boot into the live session, change Settings > Devices > Displays > Scale = 100%, click Apply and proceed with installation by clicking "Install Ubuntu 18.04 LTS".

  * The installer may not use the EFI partition you expect it to use (Bug:1396379). If you've experienced this, this bug comment has advice to repair the situation: https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1396379/comments/8

== Server ==

 * LVM Entire Disk option does not use entire disk (Bug:1785321)

 * Partitioning step allows to configure LVM across multiple devices without requiring to setup a separate /boot partition. This may lead to failure to install the bootloader at the end of the installation, and failures to boot the resultant installations. (Bug:1680101)

 * LVM configuration cannot be removed when volume groups with the same name are found during installation. Partitioner does not support installation when multiple conflicting/identical volume groups have been detected. For example reinstalling Ubuntu with LVM across multiple disk drives that had individual LVM installations of Ubuntu. As a workaround, please format disk drives prior to installation, or from the built in shell provided in the installer. (Bug:1679184)

 * cio_ignore blacklist is no longer active after installation, because not all install-time parameters, like cio_ignore (s390x), are propagated to the installed system. Workaround is to edit /etc/zipl.conf to apply these and re-run sudo zipl to update the IPL. (Bug:1571561)

 * Importing ssh keys from GitHub or Launchpad during the installation with the new `subiquity` server installer currently won't work. ([[https://pad.lv/1766980|#1766980]])


##== Graphics and Display ==

##== Networking ==

##== Kernel ==

== Raspberry Pi ==

 * As of 18.04.5, the Raspberry Pi 4 8GB version is now fully supported.

 * As of 18.04.4, the Raspberry Pi 4B is supported. For users upgrading to the release, please ensure all packages including the kernel are up to date on a prior supported model (e.g. 3B, 3B+) before attempting to boot the card on a 4B. If you encounter problems, verify (by booting on the older model) that you are running kernel version 5.3 or above (with {{{uname -r}}}), and that no updates are pending.

 * The WiFi firmware present for the BCM4345/6 chipset (found on the Raspberry Pi 3A+, 3B+, and 4B) in the 18.04.4 release is out of date and results in unreliable operation when used with 5Ghz [[https://en.wikipedia.org/wiki/IEEE_802.11ac|802.11ac]] WiFi. Note that most 5Ghz WiFi routers at present are [[https://en.wikipedia.org/wiki/IEEE_802.11n-2009|802.11n]] or a combination of 802.11n and 802.11ac, so the expected impact is low. However, the firmware package is in the process of being updated to fix this and will be updated in 18.04 as a priority after the release of 18.04.4. (Bug:1862760)

 * For Ubuntu Core 18 on the Raspberry Pi, the {{{vc4-fkms-v3d}}} overlay is included in the default boot configuration. This is known to cause issues on the Raspberry Pi 3A+ on which the overlay allocates half the available memory, leaving insufficient memory for the system to operate correctly (Bug:1848247). The recommended workaround is to comment out the {{{dtoverlay}}} line in {{{config.txt}}} on the {{{system-boot}}} partition (the first partition on the card), like so:

 {{{
 #dtoverlay=vc4-fkms-v3d
 }}}

 * The [[https://pinout.xyz/pinout/fan_shim#|Pimoroni Fan Shim]] for the Raspberry Pi 4 re-uses the serial console pins, pins 8 and 10 (GPIO14 and GPIO15 respectively), on the GPIO header to control its RGB LED. This results in "noise" on the serial line which stops u-boot during startup (as it thinks a key has been pressed). Adding the following line to {{{config.txt}}} on the {{{system-boot}}} partition (the first partition on the card) disables the serial console permitting the boot sequence to complete:

 {{{
 enable_uart=0
 }}}

<<BR>>
= Official flavours =

The release notes for the official flavors can be found at the following links:

 * Kubuntu [[https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes/Kubuntu]]
 * Lubuntu [[https://lubuntu.me/bionic-released/]]
 * Ubuntu Budgie [[https://ubuntubudgie.org/blog/2019/02/15/18-04-2-lts-ubuntu-budgie-released]]
 * Ubuntu Kylin [[https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes/UbuntuKylin]]
 * Ubuntu MATE [[https://ubuntu-mate.org/blog/ubuntu-mate-bionic-final-release/]]
 * Ubuntu Studio [[https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes/UbuntuStudio]]
 * Xubuntu [[http://wiki.xubuntu.org/releases/18.04/release-notes]]

<<BR>>
= More information =

=== Reporting bugs ===

Your comments, bug reports, patches and suggestions will help fix bugs and improve the quality of future releases. Please [[http://help.ubuntu.com/community/ReportingBugs|report bugs using the tools provided]].

If you want to help out with bugs, the [[http://wiki.ubuntu.com/BugSquad|Bug Squad]] is always looking for help.

=== Participate in Ubuntu ===

## These images were able to be made available to you thanks to the help of our [[https://wiki.ubuntu.com/SaucySalamander/TechnicalOverview/Beta1/Testers|QA Community]].

If you would like to help shape Ubuntu, take a look at the list of ways you can participate at

 https://community.ubuntu.com/contribute

=== More about Ubuntu ===

You can find out more about Ubuntu on the [[https://www.ubuntu.com|Ubuntu website]] and [[https://wiki.ubuntu.com|Ubuntu wiki]].

To sign up for future Ubuntu development announcements, please subscribe to Ubuntu's development announcement list at:

 https://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce
