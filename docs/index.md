# Ubuntu release notes

Release notes for Ubuntu, summarizing new features, bug fixes and backwards-incompatible changes in each version.

Release notes contain specific upgrade instructions for that particular release. See also the general guidance on how to prepare for, and perform, an upgrade: [Ubuntu Desktop](https://documentation.ubuntu.com/desktop/en/latest/how-to/upgrade-ubuntu-desktop/) or [Ubuntu Server](https://ubuntu.com/server/docs/how-to/software/upgrade-your-release/).

:::{toctree}
:hidden:
:maxdepth: 2
:caption: Supported LTS releases

26.04 LTS (Resolute Raccoon) <26.04/index>
24.04 LTS (Noble Numbat) <24.04/index>
22.04 LTS (Jammy Jellyfish) <22.04/index>
:::

:::{toctree}
:hidden:
:maxdepth: 2
:caption: Supported interim releases

25.10 (Questing Quokka) <25.10/index>
:::

:::{toctree}
:hidden:
:maxdepth: 2
:caption: Currently in development

26.10 (Stonking Stingray) <26.10/index>
:::

:::{toctree}
:hidden:
:maxdepth: 2
:caption: Other releases

Future releases <future>
Older releases <archive>
:::

:::{toctree}
:hidden:
:maxdepth: 2

Contribute to release notes <contribute>
:::

## LTS releases

### 26.04 LTS (Resolute Raccoon)

* {ref}`ubuntu-26.04-lts-release-notes`
* {ref}`resolute-raccoon-schedule`

### 24.04 LTS (Noble Numbat)

* {ref}`changes-in-ubuntu-24.04.4`
* {ref}`changes-in-ubuntu-24.04.3`
* {ref}`changes-in-ubuntu-24.04.2`
* {ref}`changes-in-ubuntu-24.04.1`
* {ref}`ubuntu-24.04-lts-release-notes`
* {ref}`noble-numbat-schedule`

### 22.04 LTS (Jammy Jellyfish)

* {ref}`changes-in-ubuntu-22.04.5`
* {ref}`changes-in-ubuntu-22.04.4`
* {ref}`changes-in-ubuntu-22.04.3`
* {ref}`changes-in-ubuntu-22.04.2`
* {ref}`changes-in-ubuntu-22.04.1`
* {ref}`ubuntu-22.04-lts-release-notes`
* {ref}`jammy-jellyfish-schedule`

## Interim releases

### 25.10 (Questing Quokka)

* {ref}`ubuntu-25.10-release-notes`

(release-policy-and-schedule)=
## Release policy and schedule

Ubuntu releases a new version every six months. Releases of Ubuntu get a development codename (‘Resolute Raccoon’) and are versioned by the year and month of delivery – for example, Ubuntu 26.04 was released in April 2026.

Each version includes the latest features, updates, and security patches during its supported lifecycle.

For details, see [Ubuntu release cycle](https://ubuntu.com/about/release-cycle).

### Interim releases

Ubuntu’s interim releases are designed for users and teams who move fast and need access to the latest kernels, languages, and toolchains. They provide cutting-edge features and hardware support every six months, but with only 9 months of updates. For long-term stability, production environments should use the LTS version, while interim releases suit those prioritizing speed and rapid feature testing.

### Long-term support (LTS)

LTS are released every two years and receive 5 years of standard security maintenance.

LTS releases are the go-to choice for users who value stability and extended support. These versions are security maintained for 5 years with CVE patches for packages in the Main repository. They are recommended for production environments, enterprises, and long-term projects.

### Security vulnerability policy on release day

What happens if there is a high- or critical-priority Common Vulnerability and Exposure (CVE) during release day?

Server, Desktop and Cloud plan to release in lockstep on release day, but there are some exceptions.

In the unlikely event that a critical- or high-priority CVE is announced on release day, the release team have agreed on the following plan of action:

* For critical priority CVEs, the release of Server, Desktop and Cloud will be blocked until new images can be built addressing the CVE.

* For high-priority CVEs, the decision to block release will be made on a per-product (Server, Desktop and Cloud) basis and will depend on the nature of the CVE, which might result in images not being released on the same day.

This was discussed in the [`ubuntu–release` mailing list March/April 2023](https://lists.ubuntu.com/archives/ubuntu-release/2023-April/005610.html).

The mailing list thread also confirmed there is no technical or policy reason why a package cannot be pushed to the Updates or Security pocket to address high or critical-priority CVEs prior to the release.


(project-and-community)=
## Project and community

Ubuntu is an open source project that warmly welcomes community projects, contributions, suggestions, fixes and constructive feedback.

You can find out more about Ubuntu on the [Ubuntu website](https://ubuntu.com/).

### Report bugs

Your comments, bug reports, patches and suggestions help fix bugs and improve the quality of future releases. Please [report bugs using the tools provided](http://help.ubuntu.com/community/ReportingBugs). If you want to help with bugs, the [Bug Squad](http://wiki.ubuntu.com/BugSquad) is always looking for help.

### Get involved

* [Sign up for future Ubuntu development announcements](https://lists.ubuntu.com/mailman/listinfo/ubuntu-devel-announce)
* [Get support](https://ubuntu.com/support/community-support)
* [Join our Discourse forum](https://discourse.ubuntu.com)
* [Join our online chat on Matrix](https://matrix.to/#/#release:ubuntu.com)
* If you'd like to help shape Ubuntu, look at the list of ways you can participate at community.ubuntu.com/contribute.

### Governance and policies

* [Code of conduct](https://ubuntu.com/community/code-of-conduct)
