(jammy-jellyfish-schedule)=
# Ubuntu Jammy Jellyfish Release Schedule

Week | Date (Thursday) | 22.04 events
--- | --- | ---
**October 2021** |
1 | October 21 | Toolchain Uploaded
2 | October 28 | 
**November 2021** |
3 | November 04 | 
4 | November 11 | 
5 | November 18 | 
6 | November 25 | 
**December 2021** |
7 | December 02 | 
8 | December 09 | 
9 | December 16 | 
10 | December 23 | Ubuntu Testing Week (optional)
11 | December 30 | 
**January 2022** |
12 | January 06 | 
13 | January 13 | 
14 | January 20 | 
15 | January 27 | 
**February 2022** |
16 | February 03 | Chinese New Year week
17 | February 10 |
18 | February 17 | 
19 | February 24 | [Feature Freeze](https://ubuntu.com/project/docs/release-team/freezes/#feature-freeze), Debian Import Freeze,  20.04.4 Point Release
**March 2022** |
20 | March 03 | Ubuntu Testing Week (optional)
21 | March 10 | 
22 | March 17 | [User Interface Freeze](https://ubuntu.com/project/docs/release-team/freezes/#user-interface-freeze)
23 | March 24 | [Documentation String Freeze](https://ubuntu.com/project/docs/release-team/freezes/#documentation-string-freeze), [Kernel Feature Freeze](https://ubuntu.com/project/docs/release-team/freezes/#kernel-feature-freeze)
24 | March 28 (Monday) | Beta Freeze, [Hardware Enablement Freeze](https://ubuntu.com/project/docs/release-team/freezes/#hardware-enablement-freeze)
⠀ | March 31 | Beta (mandatory)
**April 2022** |
25 | April 07 | [Kernel Freeze](https://ubuntu.com/project/docs/release-team/freezes/#kernel-freeze), [Non Language Pack Translation Deadline](https://ubuntu.com/project/docs/release-team/freezes/#non-language-pack-translation-deadline)
26 | April 14 | [Final Freeze](https://ubuntu.com/project/docs/release-team/freezes/#final-freeze), [Release Candidate](https://ubuntu.com/project/docs/release-team/freezes/#release-candidate), [Language Pack Translation Deadline](https://ubuntu.com/project/docs/release-team/freezes/#language-pack-translation-deadline)
27 | April 21 | [Final Release](https://ubuntu.com/project/docs/release-team/release-cycle/#final-release)
... | ...
**August 2022** |
42 | August 04 | [22.04.1 Point Release ](https://ubuntu.com/project/docs/release-team/ubuntu-releases/#point-releases)
43 | August 11 | 
44 | August 18 | 
45 | August 21 | 
... | ...
**February 2023** |
68 | February 02 | 
69 | February 09 | 
70 | February 16 | 
71 | February 23 | [22.04.2 Point Release ](https://ubuntu.com/project/docs/release-team/ubuntu-releases/#point-releases)
... | ...
**August 2023** |
94 | August 03 |
95 | August 10 | [22.04.3 Point Release ](https://ubuntu.com/project/docs/release-team/ubuntu-releases/#point-releases)
96 | August 17 |
97 | August 24 |
98 | August 31 |
... | ...
**February 2024** |
120 | February 1 |
121 | February 8 |
122 | February 15 |
123 | February 22 | [22.04.4 Point Release ](https://ubuntu.com/project/docs/release-team/ubuntu-releases/#point-releases)
... | ...
**August 2024** |
147 | August 01 | 
148 | August 08 | 
149 | August 15 | 
150 | August 22 | 
151 | August 29 |  
**September 2024** |
152 | September 05 | 
153 | September 12 | [22.04.5 Point Release ](https://ubuntu.com/project/docs/release-team/ubuntu-releases/#point-releases)


## Planned and potentially disruptive archive-wide activities

If you're planning a change that might have a disruptive effect on the archive - e.g. transitions or switches of important defaults (such as compiler versions) - list it here.

Week | Date (Thursday) | Planned activity
--- | --- | ---
**October 2021** |
1 | October 21 | 
2 | October 28 | php8.1
**November 2021** |
3 | November 04 | OpenSSL3
4 | November 11 | 
5 | November 18 | Ruby 3.0
6 | November 25 | 
**December 2021** |
7 | December 02 | systemd v249
8 | December 09 |  DPDK 21.11
9 | December 16 | binutils 2.38
10 | December 23 | 
11 | December 30 | 
**January 2022** |
12 | January 06 |
13 | January 13 | Python 3.10
14 | January 20 | ~~OpenLDAP 2.6 (tentative; depends on upstream release schedule)~~ -- Cancelled, see [this comment](https://bugs.launchpad.net/ubuntu/+source/openldap/+bug/1946883/comments/5)
15 | January 27 | 
**February 2022** |
16 | February 03 | Glibc 2.35
17 | February 10 | 
18 | February 17 | [GNOME 42 Beta](https://wiki.gnome.org/FortyTwo), Golang 1.18
19 | February 24 | 
**March 2022** |
20 | March 03 | 
21 | March 10 | 
22 | March 17 | LLVM 14
23 | March 24 | [GNOME 42.0](https://wiki.gnome.org/FortyTwo)
24 | March 31 | Openstack Yoga
**April 2022** |
25 | April 07 | 
26 | April 14 | 
27 | April 21 | 

## Ubuntu Jammy Jellyfish Release Task Signup Sheet

This signup sheet is to be used for planning release milestone tasks.

The Alpha and Beta 1 milestones have been replaced with [Testing Weeks](https://lists.ubuntu.com/archives/ubuntu-release/2018-April/004434.html), which are organized ad hoc at this point.

| Milestone         |     Date        | Image (Nusakan) Engineering | Checklist Tracking | Announcement Email |
| ----------------- | --------------- | --------------------------- | ------------------ | ------------------ |
| Feature Freeze    |                 | n/a                         | n/a                |                    |
| UI Freeze         |                 | n/a                         | n/a                |                    |
| Doc String Freeze |                 | n/a                         | n/a                |                    |
| 22.04 Beta        |  March 31 2022  |  @sil2100  |                    |    @sil2100    |
| Final Freeze      |   April 14 2022  |                             |                    |                    |
| 22.04 Release     | April 21 2022 |                             |                    |                    |

When the archive is frozen, all members of the release team are expected to participate in bug fix reviews.

After [Feature Freeze](https://ubuntu.com/project/docs/release-team/freezes/#feature-freeze), all members of the release team are expected to participate in Feature Freeze Exception reviews in their particular area of expertise.

After [Final Beta](https://ubuntu.com/project/docs/release-team/release-cycle/#finalization), all members of the release team are expected to participate in Bug fix reviews in their particular area of expertise.
