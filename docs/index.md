# Ubuntu release notes

Release notes for Ubuntu, summarizing new features, bug fixes and backwards-incompatible changes in each version.

Release notes contain specific upgrade instructions for that particular release. See also the general guidance on how to prepare for, and perform, an upgrade: [Ubuntu Desktop](https://documentation.ubuntu.com/desktop/en/latest/how-to/upgrade-ubuntu-desktop/) or [Ubuntu Server](https://ubuntu.com/server/docs/how-to/software/upgrade-your-release/).

## 26.04 LTS

* {ref}`ubuntu-26.04-lts-release-notes`
* {ref}`resolute-raccoon-schedule`
* [Ubuntu 26.04 LTS roadmap](https://discourse.ubuntu.com/t/ubuntu-26-04-lts-the-roadmap/72740)

## 25.10

* [Questing Quokka release notes](https://discourse.ubuntu.com/t/questing-quokka-release-notes/59220)

## 24.04 LTS

* [24.04.2](https://discourse.ubuntu.com/t/noble-numbat-point-release-changes/47565/3)  
* [24.04.1](https://discourse.ubuntu.com/t/noble-numbat-point-release-changes/47565#h-24041-1)  
* [Ubuntu 24.04 LTS (Noble Numbat) release notes](https://discourse.ubuntu.com/t/ubuntu-24-04-lts-noble-numbat-release-notes/39890)
* {ref}`noble-numbat-schedule`

(release-policy-and-schedule)=
## Release policy and schedule

Our release cadence nunc elit magna, pulvinar sed egestas ut, porta sed leo. Nam in urna ultricies, lacinia nisl non, dictum risus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam turpis mauris, pulvinar a enim eget, dignissim feugiat libero. Aenean volutpat sit amet justo sit amet eleifend.

### Long-term support (LTS)

LTS releases eleifend augue eros, vel viverra arcu accumsan malesuada. Cras consectetur, orci a porttitor pellentesque, est leo fringilla sapien, eu sagittis urna magna nec ipsum. Quisque iaculis tincidunt felis, a placerat quam. Curabitur non leo ac neque consectetur viverra. Duis mattis consectetur convallis.

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


:::{toctree}
:hidden:
:maxdepth: 2
:caption: Supported releases

26.04 LTS (Resolute Raccoon) <26.04/index>
24.04 LTS (Noble Numbat) <24.04/index>
:::

:::{toctree}
:hidden:
:maxdepth: 2
:caption: Currently in development

26.10 (S* S*) <26.10/schedule>
:::

:::{toctree}
:hidden:
:maxdepth: 2
:caption: Other releases

Upcoming releases <upcoming>
Older releases <archive>
:::
