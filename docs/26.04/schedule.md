(resolute-raccoon-schedule)=
# Ubuntu Resolute Raccoon Release Schedule

<!-- migrated from https://discourse.ubuntu.com/t/resolute-raccoon-release-schedule/47198 -->

:::{timeline}
:reversed:

- start: 2026-02-19
  name: "[Feature Freeze](https://ubuntu.com/project/docs/release-team/freezes/#feature-freeze), Debian Import Freeze"
- start: 2026-03-26
  name: Beta (mandatory)
- start: 2026-04-23
  name: "[Final Release](https://ubuntu.com/project/docs/release-team/release-cycle/#final-release)"

---
**{{dtrange}}**

{{e.name}}
:::

| Week | Date (Thursday) | 26.04 events |
|----|----|----|
| **October 2025** |  |  |
| 1 | October 16 | Toolchain Uploaded |
| 2 | October 23 |  |
| 3 | October 30 |  |
| **November 2025** |  |  |
| 4 | November 06 |  |
| 5 | November 13 |  |
| 6 | November 20 |  |
| 7 | November 27 | Resolute Snapshot 1 |
| **December 2025** |  |  |
| 8 | December 04 |  |
| 9 | December 11 | Resolute Snapshot 2 |
| 10 | December 18 |  |
| 11 | December 25 |  |
| **January 2026** |  |  |
| 12 | January 01 |  |
| 13 | January 08 |  |
| 14 | January 15 |  |
| 15 | January 22 |  |
| 16 | January 29 | Resolute Snapshot 3 |
| **February 2026** |  |  |
| 17 | February 05 |  |
| 18 | February 12 |  |
| 19 | February 19 | [Feature Freeze](https://ubuntu.com/project/docs/release-team/freezes/#feature-freeze), Debian Import Freeze |
| 20 | February 26 | Resolute Snapshot 4 |
| **March 2026** |  |  |
| 21 | March 05 |  |
| 22 | March 12 | [User Interface Freeze](https://ubuntu.com/project/docs/release-team/freezes/#user-interface-freeze) |
| 23 | March 19 | [Documentation String Freeze](https://ubuntu.com/project/docs/release-team/freezes/#documentation-string-freeze), [Kernel Feature Freeze](https://ubuntu.com/project/docs/release-team/freezes/#kernel-feature-freeze) |
| 24 | March 23 (Monday) | [Beta Freeze](https://ubuntu.com/project/docs/release-team/freezes/#beta-freeze), [Hardware Enablement Freeze](https://ubuntu.com/project/docs/release-team/freezes/#hardware-enablement-freeze), ISO Testing Week (mandatory) |
| ⠀ | March 26 | Beta (mandatory) |
| **April 2026** |  |  |
| 25 | April 02 |  |
| 26 | April 09 | [Kernel Freeze](https://ubuntu.com/project/docs/release-team/freezes/#kernel-freeze), [Non Language Pack Translation Deadline](https://ubuntu.com/project/docs/release-team/freezes/#non-language-pack-translation-deadline) |
| 27 | April 16 | [Final Freeze](https://ubuntu.com/project/docs/release-team/freezes/#final-freeze), [Release Candidate](https://ubuntu.com/project/docs/release-team/freezes/#release-candidate), [Language Pack Translation Deadline](https://ubuntu.com/project/docs/release-team/freezes/#language-pack-translation-deadline) |
| 28 | April 23 | [Final Release](https://ubuntu.com/project/docs/release-team/release-cycle/#final-release) |
|... | ||
| **August 2026**| ||
| 46 | August 27 | [26.04.1 Point Release ](https://ubuntu.com/project/docs/release-team/ubuntu-releases/#point-releases) |

## Planned and potentially disruptive archive-wide activities

If you’re planning a change that might have a disruptive effect on the archive - e.g. transitions or switches of important defaults (such as compiler versions) - list it here.

|Week | Date (Thursday) | Planned activity|
|--- | --- | ---|
|**October 2025** |  | |
|1 | October 16 | Python 3.14 as a supported version|
|2 | October 23 | enable autosync from Debian|
|3 | October 30 | Golang 1.25 transition|
|**November 2025** |  | |
|4 | November 06 | |
|5 | November 13 | |
|6 | November 20 | |
|7 | November 27 | |
|**December 2025** |  | |
|8 | December 04 | |
|9 | December 11 | |
|10 | December 18 | binutils 2.46|
|11 | December 25 | |
|**January 2026** |  | |
|12 | January 01 | GNOME 50 alpha|
|13 | January 08 | Python 3.14 as the default version|
|14 | January 15 | |
|15 | January 22 | PHP 8.5|
|16 | January 29 | GNOME 50 beta|
|**February 2026** |  | |
|17 | February 05 | |
|18 | February 12 | GCC 16 as optional, Rust 1.93 transition (tentative), Java 25 default (tentative)|
|19 | February 19 | |
|20 | February 26 | |
|**March 2026** |  | |
|21 | March 05 | |
|22 | March 12 | |
|23 | March 19 | |
|24 | March 26 | |
|**April 2026** |  | |
|25 | April 02 | |
|26 | April 09 | |
|27 | April 16 | |
|28 | April 23 | |

## Ubuntu Resolute Raccoon Release Task Signup Sheet

This signup sheet is to be used for planning release milestone tasks.

The Alpha and Beta 1 milestones have been replaced with [Testing Weeks](https://lists.ubuntu.com/archives/ubuntu-release/2018-April/004434.html), which are organized ad hoc at this point.

| Milestone | Date | Image (Nusakan) Engineering | Checklist Tracking | Announcement Email |
|----|----|----|----|----|
| Feature Freeze | | n/a | n/a | @utkarsh |
| UI Freeze | | n/a | n/a | @utkarsh |
| Doc String Freeze | | n/a | n/a | @utkarsh |
| 26.04 Beta | | | | |
| 26.04 Release | April 23 2026 | @utkarsh | @utkarsh | @utkarsh |

When the archive is frozen, all members of the release team are expected to participate in bug fix reviews.

After [Feature Freeze](https://ubuntu.com/project/docs/release-team/freezes/#feature-freeze), all members of the release team are expected to participate in Feature Freeze Exception reviews in their particular area of expertise.

After [Final Beta](https://ubuntu.com/project/docs/release-team/release-cycle/#finalization), all members of the release team are expected to participate in Bug fix reviews in their particular area of expertise.
