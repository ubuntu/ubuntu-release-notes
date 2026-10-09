---
tocdepth: 3
---

<!-- SOURCE: https://wiki.ubuntu.com/GutsyReleaseNotes -->
<!-- redirected to GutsyGibbon/ReleaseNotes -->

(ubuntu-7-10-release-notes)=
# Ubuntu 7.10 release notes

These release notes document known issues with version 7.10 of Ubuntu, Kubuntu, Edubuntu, Xubuntu, and Gobuntu.

## System Requirements

The minimum memory requirement for Ubuntu 7.10 is 384MB of memory for desktop CDs, and 256MB for other installation methods. (Note that some of your system's memory may be unavailable due to being used for the graphics card.)

With only the minimum amount of memory available, the installation process will take longer than normal, but will complete successfully, and the system will perform adequately once installed. Low-memory systems may be able to use the desktop CD to install by adding the `only-ubiquity` boot option to run just the installer rather than the whole desktop.

## Installation

### AACRAID in Dell PowerEdge 2650

* The "server" kernel flavor does not work on Dell PowerEdge 2650 servers due to an error initializing the `aacraid` driver.  As a workaround, users can run the "generic" kernel flavor instead. [Bug #149071](https://launchpad.net/bugs/149071)

### Mail server and sudo

* If the `mail-server` task is selected during installation and "No configuration" is selected in response to the question "General type of mail configuration:", then the initial user will be set up without sudo access. To repair this, boot in recovery mode and run:

  ```none
  addgroup --system admin
  adduser USERNAME admin
  echo '%admin ALL=(ALL) ALL' >>/etc/sudoers
  ```

  where `USERNAME` is the name of the initial user created during installation. Selecting any other answer to the "General type of mail configuration:" question will avoid this problem. [Bug #158952](https://launchpad.net/bugs/158952)

### GPT disks

* Partitioning of disks with [GPT](http://en.wikipedia.org/wiki/GUID_Partition_Table) disk labels, which are used on very large disks (over 2 terabytes), will not work correctly due to a conflict with changes needed to support Intel-based Apple Mac systems. If you repartition a disk with existing data (e.g. during installation), this may cause data loss unless you know how to restore the protective MBR by hand. [Bug #107326](https://launchpad.net/bugs/107326)

## Upgrading

Users of Ubuntu 7.04 can upgrade to Ubuntu 7.10 by a convenient automated process. <!-- Complete instructions may be found at http://www.ubuntu.com/getubuntu/upgrading.-->

### /etc/papersize not present

* If you installed a pre-release of Ubuntu 7.10 from the Desktop CD prior to the Beta release, the file `/etc/papersize` will not exist, which may cause printing problems.  This can be fixed by creating the file with the default paper size you want to use; this is usually "a4" or "letter" depending on your location, for example:

  ```none
  echo letter | sudo tee /etc/papersize >/dev/null
  ```

### Route metrics

* `ifupdown` now sets the default route metric to 100 for interfaces with no metric option set in `/etc/network/interfaces`. This change makes no difference for most users, but may affect a few users with complex networking requirements. If you rely on the previous default route metric of 0 (zero), edit `/etc/network/interfaces` and set the metric option explicitly for your interface, for example:

    ```none
    iface eth0 inet static
            address 192.168.0.2
            network 192.168.0.0
            broadcast 192.168.0.255
            netmask 255.255.255.0
            gateway 192.168.0.1
            metric 0
    ```

### Network Manager

* In Ubuntu 7.10, `network-manager` only manages interfaces that are marked for roaming. Thus, all interfaces that were previously managed by `network-manager` will be set to roaming mode during upgrade. Technically, this takes any interface stanzas using the `dhcp` method with no options and that are marked `auto`, and removes them from `/etc/network/interfaces`. If you rely on your interfaces being started by `ifupdown` when the system starts up, you need to re-enable them in `/etc/network/interfaces` manually, or disable roaming in **System** -> **Administration** -> **Network**.

### NFS mount support

* To mount NFS filesystems, you must now install the `nfs-common` package.

### Commercial/partner repository

* The "commercial" repository on `archive.canonical.com` has been renamed to "partner". If you upgrade directly from an earlier release to Ubuntu 7.10 using the documented upgrade procedure, then this will be handled automatically. However, if you upgraded via the beta and/or manually, you will need to edit `/etc/apt/sources.list` by hand.  The correct syntax is:

    ```none
    deb http://archive.canonical.com/ gutsy partner
    ```

### UltraSPARC disk label changes

* Users upgrading to Ubuntu 7.10 on UltraSPARC should manually re-run `fdisk` on all disks. `fdisk` will warn if the disk label needs to be updated; follow its instructions. New installations of Ubuntu 7.10 will automatically use the new disk label format.

### PlayStation 3 changes

* The kernel flavor for PlayStation 3 systems has changed from `powerpc64-smp` to `cell`. Users upgrading their PlayStation 3 from Ubuntu 7.04 to 7.10 should run this before or after the upgrade:

    ```none
    $ sudo apt-get remove linux-image-powerpc64-smp linux-powerpc64-smp linux-restricted-modules-powerpc64-smp
    $ sudo apt-get install linux-cell
    ```
* In addition, the block device names have changed from the normal `/dev/sdX` naming to `/dev/ps3dX` (e.g. `/dev/sda1` will now be known as `/dev/ps3da1`). Standard installs should not be affected by this, since they use UUID naming. However, if you changed `/etc/fstab` to refer to hardcoded device names, you will need to adjust these for the new kernel.

* Check if `/etc/kboot.conf` uses the `/dev/sdX` naming and change it to the UUID naming or the `/dev/ps3dX` naming.

### GnuPG agent integration missing on upgrade from Ubuntu 7.04

* If you are upgrading from Ubuntu 7.04, the file `~/.gnupg/gpg.conf` may have failed to be created by default in your home directory due to a bug in the `gnupg` package.  In that case, GPG agent integration will not be enabled by default.  If you have not created your own `gpg.conf`, you can correct this issue by running `cp /usr/share/gnupg/options.skel ~/.gnupg/gpg.conf`. If you do have a `gpg.conf` and are affected by this issue, correct it by running `echo use-agent >> ~/.gnupg/gpg.conf`. [Bug #76983](https://launchpad.net/bugs/76983)

## Other known bugs

### Blank screen with some ATI hardware

* People with ATI display adapters may get a blank screen when loading X due to the driver being unable to initialize certain hardware. Upstream is working on it, and hopefully we'll be able to release an update for 7.10 soon after the release. In the meantime, add '`Option "LVDSBiosNativeMode" "false"`' to the driver section of `xorg.conf`. [Bug #132716](https://bugs.launchpad.net/bugs/132716)

### Dual-head (multi-screen) setups

* The ATI driver has dropped MergedFB / Xinerama support in favour of XRandR 1.2 support, and old multi-head xorg.conf setups will break. To set up dual-head see the guides at https://www.intel.com/content/www/us/en/homepage.html or http://wiki.debian.org/XStrikeForce/HowToRandR12
* As XRandR and Xinerama are incompatible, you cannot mix some graphics cards using `xrandr`-enabled drivers with others that are still limited to using Xinerama.  In this case, you will need to revert to pre-`xrandr` versions of the respective drivers: for Intel cards, use the old "i810" driver instead of "intel", for ATI cards, use the old [6.6 version](https://launchpad.net/ubuntu/+source/xserver-xorg-video-ati/1:6.6.3-2ubuntu6).
* With `xrandr`, it is now possible to use Compiz in a multi-screen setup, however it is dependent on available video card memory.  The workaround for this issue is to switch to a lower virtual resolution.

### Compiz and session management

* Users who enable desktop effects will find that they are unable to use the "Remember currently running applications" feature.  The workaround for this issue is to disable the use of the Compiz compositing window manager by turning off desktop effects in the **System** -> **Preferences** -> **Appearance** menu.

### Suspend to RAM with `fglrx`

* Attempting to suspend to RAM using the proprietary `fglrx` ATI video driver from the restricted component will hard-lock the system due to changes in the kernel's memory allocator (which will be the default in Linux 2.6.23) that have not been followed by ATI in a timely fashion; this is the vendor's responsibility and is beyond our control due to the proprietary nature of the driver.  Workarounds include using Ubuntu 7.04, avoiding suspending to RAM, or using the free ATI driver. [Bug #121653](https://launchpad.net/bugs/121653)

### Printing with AppArmor

Ubuntu 7.10 introduces an additional security layer called AppArmor, whose support for CUPS printing is not yet complete.  This will result in printing failures in certain corner cases described below.  The workaround in each of these cases is to disable the AppArmor CUPS profile by running `sudo aa-complain cupsd`.  AppArmor support may be re-enabled by running `sudo aa-enforce cupsd`.

* Printing to bluetooth printers does not work with AppArmor enabled. [Bug #147800](https://launchpad.net/bugs/147800)
* Many third-party printer drivers (especially from printer manufacturers) do not work. [Bug #152537](https://launchpad.net/bugs/152537)
* The HP DeskJet 710C/712C/720C/722C/820C/1000C (driver "pnm2ppa") do not work. [Bug #155530](https://launchpad.net/bugs/155530)

### Fax on HP multi-function devices does not work

* Due to a bug in HP's driver software, faxing on all of HP multi-function devices does not work. No workaround is currently available, but HP has been informed of the issue. [Bug #153152](https://launchpad.net/bugs/153152)

### No printer admin rights for added users

* Users must be in the printing administration group, "`lpadmin`", to be able to configure printer settings. The first system user created during installation is added to this group, but users added or modified with the `user-admin` tool at **System** -> **Administration** -> **Users and Groups** will not be added to this group. As a workaround, you can grant "`lpadmin`" privileges to users by running the command `sudo adduser <user> lpadmin` in a terminal window. [Bug #152107](https://launchpad.net/bugs/152107)

### User management tool may lose user privileges

* It is reported that the `users-admin` user management tool (**System** -> **Administration** -> **Users and Groups**) will in some cases remove the group memberships of all users when adding a new user, which means that all existing users lose their administrator privileges, possibly leaving the system with no administrator access at all.  The nature of this issue has not yet been established, and therefore no fix is presently known for this issue.  If you experience this problem, you can recover by booting in recovery mode and using command-line tools to restore group memberships: for example, `adduser joe admin` will give the user `joe` administrator privileges. [Bug #26338](https://launchpad.net/bugs/26338)

### Kopete crashes when connecting to MSN

* Kubuntu's instant messenger application Kopete crashes when connecting with an account using MSN.  A fix should be available from gutsy-updates soon.  [Bug #153500](https://bugs.launchpad.net/ubuntu/+source/kdenetwork/+bug/153500)

### CPU fan no longer runs on Dell Latitude L400

* On a Dell Latitude L400, the CPU fan no longer runs and the CPU overheats under stress. Add `acpi=off` to the grub boot command for a workaround. [Bug #127772](https://bugs.launchpad.net/ubuntu/+source/linux-source-2.6.22/+bug/127772)

### Boot splash screen does not display

* With some monitors the resolution is wrongly detected when installed from a desktop CD and the boot splash screen is not displayed.  You can fix the resolution by editing `/etc/usplash.conf`.  [Bug #150930](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/150930)
