# How to contribute to Ubuntu release notes

Ubuntu release notes have recently moved from Discourse to this location. Read more: [New Ubuntu release notes](https://discourse.ubuntu.com/t/new-ubuntu-release-notes/78722).

## Add a new release note

Anyone can add or modify release notes using the GitHub interface. The process is open for community members and Canonical employees.

### Simplified: file an issue

The easiest way to submit a release note is to [fill out an issue form](https://github.com/ubuntu/ubuntu-release-notes/issues/new?template=add-a-release-note.yml).

There, provide all the requested information about the change in Ubuntu.

After you file the issue, the repository maintainers will review the information and publish the release note based on it.

### More complex: open a pull request

If you want more control over the process, you can propose changes directly through a pull request:

1. [Fork](https://github.com/ubuntu/ubuntu-release-notes/fork) the release notes repository.

1. Make changes in your fork.

    Every Ubuntu release is represented as a directory under `docs/`, named after the Ubuntu version: for example, `docs/26.04/` stores Ubuntu 26.04 LTS (Resolute Raccoon) release notes.

    When writing your release note, keep in mind the documentation standards described in {ref}`contribute-review-release-notes`.

1. [Create a pull request](https://github.com/ubuntu/ubuntu-release-notes/pulls) to propose your changes.

1. Let the repository maintainers review and merge your changes.

(contribute-review-release-notes)=
## Review the release notes

Before each Ubuntu release, every team working on a certain part of Ubuntu should review their release notes.

Maintainers should monitor the [issues](https://github.com/ubuntu/ubuntu-release-notes/issues) and [pull requests](https://github.com/ubuntu/ubuntu-release-notes/pulls) in the release notes repository, review them and merge them.

Label every issue and pull request with the version number of the Ubuntu release where the release note applies, such as `26.04`. Add the `New release note` label if this introduces a new release note.

### Information correctness

**Engineers** are mainly responsible for this review.

- Review the changes since the previous interim release, such as {ref}`here <ubuntu-26.04-lts-changes-since-25.10>` for Ubuntu 26.04 LTS.

    In this document, cover what you've been working on for the past 6 months. Make sure that the information related to your team there is correct and complete. Go into detail: this part of the release notes should be exhaustive.

- Decide which of the 6-month changes you want to highlight as major changes. These will be gathered later as the basis of the next (or currently prepared) LTS release notes. Interim release notes contain a highlights section at the start.

- If this is an LTS release, review the summary since the previous LTS release, such as {ref}`here <ubuntu-26.04-lts-summary>` for Ubuntu 26.04 LTS.

    These are the highlights of the major changes in the past two years. Primarily, include significant new features and breaking changes to alert upgrading users.

    This part of the release notes should be less detailed. You can link to older interim release notes for additional details. If you want to repeat the same release note in an interim and LTS section, you can rely on [content reuse](https://documentation.ubuntu.com/sphinx-stack/latest/reference/myst-syntax/#reuse).

### Writing style and content placement

**Technical Authors** are mainly responsible for this review.

- Check that the writing is fine. Adjust headings to summarize every release note.

- Check the markup. Focus on code elements such as package names, tool names, function names and similar: format them as code literals. Code elements without any markup show up as spelling issues.

- In case of LTS, clarify the timeline of the change: Is this a change since the previous interim release or since the previous LTS release? Based on that, move the release note to the appropriate section.

- Check that the placement of each release note is correct. Separate the news into the following categories:

    New features or improvements
    : Strictly improvements in functionality, performance, reliability, support level and similar.
    
    Backwards-incompatible changes, including removed features
    : Something that worked in an earlier Ubuntu release no longer works. The user needs to actively change their configuration: rewrite a configuration file, switch to another application etc.
    
    Deprecated features
    : Features that are planned to be removed in a later Ubuntu release. They still work as expected in the current release. We're giving Ubuntu users a heads-up.
    
    Bug fixes
    : Bugs that were present in an earlier Ubuntu release are fixed in this release. Also include updates to new upstream releases that only contain bug fixes.
    
    Known issues
    : Something doesn't work as expected in this Ubuntu release and the team is working on a fix. In each case, try to provide a workaround for users.
    
    :::{note}
    In the LTS summary, these change types aren't separated the same way as in interim release notes. This is an experiment for now and we'll revisit the organization with upcoming releases.
    :::
