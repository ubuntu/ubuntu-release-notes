import datetime
import os
import textwrap
import yaml

# Configuration for the Sphinx documentation builder.
# All configuration specific to your project should be done in this file.
#
# If you're new to Sphinx and don't want any advanced or custom features,
# just go through the items marked 'TODO'.
#
# A complete list of built-in Sphinx configuration values:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# The Sphinx Stack uses the Canonical Sphinx theme to keep all documentation consistent
# and on brand:
# https://github.com/canonical/canonical-sphinx

#######################
# Project information #
#######################

# Project name

project = "Ubuntu release notes"

# Author name; used in the default copyright statement in the page footer
author = "Canonical Ltd."

# The year in the copyright statement
copyright = f"{datetime.date.today().year}"

# Sidebar documentation title
# To disable the title, set it to an empty string.
html_title = project

# Documentation website URL
ogp_site_url = "https://documentation.ubuntu.com/release-notes/"

# Preview name of the documentation website
ogp_site_name = project

# Preview image URL
ogp_image = "https://assets.ubuntu.com/v1/cc828679-docs_illustration.svg"

# Product favicon; shown in bookmarks, browser tabs, etc.
# TODO: To customise the favicon, uncomment and update the next line.
# html_favicon = "_dev/_static/favicon.png"

# Dictionary of values to pass into the Sphinx context for all pages:
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_context
html_context = {
    # Product page URL; can be different from product docs URL
    "product_page": "ubuntu.com",
    # Product tag image; the orange part of your logo, shown in the page header
    # 'product_tag': '_static/tag.png',
    # Your Discourse instance URL
    # NOTE: If set, adding ':discourse: 123' to an .rst file
    #       will add a link to Discourse topic 123 at the bottom of the page.
    "discourse": "https://discourse.ubuntu.com",
    # Your Mattermost channel URL
    # "mattermost": "https://chat.canonical.com/canonical/channels/documentation",
    "mattermost": "",
    # Your Matrix channel URL
    "matrix": "https://matrix.to/#/#release:ubuntu.com",
    # Your documentation GitHub repository URL. If set, links for viewing the
    # documentation source files and creating GitHub issues are added at the bottom of
    # each page.
    "github_url": "https://github.com/ubuntu/ubuntu-release-notes",
    # Docs branch in the repo; used in links for viewing the source files
    "repo_default_branch": "main",
    # Docs location in the repo; used in links for viewing the source files
    "repo_folder": "/docs/",
    # TODO: To enable or disable the Previous / Next buttons at the bottom of pages
    # Valid options: none, prev, next, both
    # "sequential_nav": "both",
    # TODO: To enable listing contributors on individual pages, set to True
    "display_contributors": True,
    # Required for feedback button
    "github_issues": "enabled",
    # Passes the top-level 'author' value to the theme
    "author": author,
    # Documentation license information
    "license": {
        # The documentation content is licensed under CC-BY-SA 3.0
        "name": "CC-BY-SA-3.0",
        "url": "https://github.com/ubuntu/ubuntu-release-notes/blob/main/LICENSE",
    },
    # Links for the "Ubuntu docs" dropdown in the site header
    #  - comment out "your" docs set, duh! ;-)
    "ubuntu_docs": [
        # {"title": "Ubuntu release notes", "url": "https://documentation.ubuntu.com/release-notes/"},
        {"title": "Ubuntu Desktop", "url": "https://documentation.ubuntu.com/desktop/"},
        {"title": "Ubuntu Server", "url": "https://ubuntu.com/server/docs/"},
        {
            "title": "Ubuntu on WSL",
            "url": "https://documentation.ubuntu.com/wsl/latest/",
        },
        {
            "title": "Ubuntu for developers",
            "url": "https://documentation.ubuntu.com/ubuntu-for-developers/",
        },
        {"title": "Ubuntu project", "url": "https://documentation.ubuntu.com/project/"},
        {"title": "Ubuntu Pro", "url": "https://documentation.ubuntu.com/pro/"},
    ],
}

html_extra_path = []

# Allow opt-in build of the OpenAPI "Hello" example so docs stay clean by default.
# if os.getenv("OPENAPI", ""):
#     tags.add("openapi")
#     html_extra_path.append("how-to/assets/openapi.yaml")

# TODO: To enable the edit button on pages, uncomment and change the link to a
# public repository on GitHub or Launchpad. Any of the following link domains
# are accepted:
# - https://github.com/example-org/example"
# - https://launchpad.net/example
# - https://git.launchpad.net/example
#
html_theme_options = {
    "source_edit_link": "https://github.com/ubuntu/ubuntu-release-notes",
}

# Project slug
# TODO: If your documentation is hosted on https://documentation.ubuntu.com/,
#       uncomment and set to the RTD slug.
slug = "release-notes"

#######################
# Sitemap configuration: https://sphinx-sitemap.readthedocs.io/
#######################

# Use RTD canonical URL to ensure duplicate pages have a specific canonical URL
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "/")

# sphinx-sitemap uses html_baseurl to generate the full URL for each page:
sitemap_url_scheme = "{link}"

# Include `lastmod` dates in the sitemap:
sitemap_show_lastmod = True

# Pages excluded from the sitemap:
sitemap_excludes = [
    "404/",
    "genindex/",
    "search/",
]

################################
# Template and asset locations #
################################

html_static_path = ["_static"]
templates_path = ["_templates"]

#############
# Redirects #
#############

# Add redirects to the 'redirects.txt' file
# https://sphinxext-rediraffe.readthedocs.io/en/latest/

# To set up redirects in the Read the Docs project dashboard:
# https://docs.readthedocs.io/en/stable/guides/redirects.html

rediraffe_redirects = "redirects.txt"

# Strips '/index.html' from destination URLs when building with 'dirhtml'
rediraffe_dir_only = True


############################
# sphinx-llm configuration #
############################

# This description is included in llms.txt to provide some initial context for your
# product docs.
llms_txt_description = textwrap.dedent(
    """\
    This is the documentation for the Ubuntu release notes, which describe the changes
    in current and upcoming Ubuntu releases.
    """
)

# Suppress warnings for nodes that sphinx-llm does not know how to handle
# (for example, nodes produced by the sphinx-timeline extension).
llms_txt_suppress_unknown_node_warnings = True

# The base URL for references built by sphinx-markdown-builder.
if os.environ.get("READTHEDOCS"):
    markdown_http_base = html_baseurl

###########################
# Link checker exceptions #
###########################

# A regex list of URLs that are ignored by 'make linkcheck'
linkcheck_ignore = [
    "http://127.0.0.1:8000",
    "https://github.com/canonical/ACME/*",
    # The link checker tries to treat the part after # as an anchor and fails.
    "https://matrix.to/*",
    # Rate-limited domains that cause delays
    r"http://www\.gnu\.org/software/.*",
    r"https://github\.com/.*/blob/.*",
    # Ubuntu wiki (rate-limited)
    r"https://wiki\.ubuntu\.com/.*",
    # Ubuntu wiki over HTTP (connect timeouts)
    r"http://wiki\.ubuntu\.com.*",
    # Rate-blocked or bot-challenged (418 / 5xx responses)
    r"https?://ceph\.com.*",
    r"https://dev\.mysql\.com/.*",
    r"https://blogs\.oracle\.com/.*",
    r"https://gitlab\.gnome\.org/.*",
    r"https://discourse\.lubuntu\.me/.*",
    # Mythbuntu: page is live but blocks bots with 403
    r"http://www\.mythbuntu\.org/.*",
    r"https://downloads\.apache\.org/.*",
    r"https://www\.freedesktop\.org/.*",
    r"https://gstreamer\.freedesktop\.org/.*",
    r"https://linux-nfs\.org/wiki/.*",
    # Flaky host (intermittent connection aborts from CI)
    r"https://www\.xfce\.org/.*",
    # Launchpad: bugs/commits may be private or deleted
    r"https://bugs\.launchpad\.net/.*",
    r"https://git\.launchpad\.net/.*",
    r"https://launchpad\.net/bugs/.*",
    # Ubuntu manpages site: pages for newer/unreleased series may 404
    r"https://manpages\.ubuntu\.com/.*",
    # Ubuntu ESM endpoint (times out from CI)
    r"http://esm\.ubuntu\.com.*",
    # Old / dead external pages
    r"https://release\.gnome\.org/.*",
    r"https://lubuntu\.me/.*",
    # Filenames in text incorrectly parsed as URLs by the link checker
    r"http://[^\s/]+\.(py|sh|mk|in)$",
    # Servers being migrated right now - ignore for now
    r"https://ubuntukylin\.com/.*",
    # Dead links in existing content (historical; not worth updating)
    r"https://github\.com/docker-snap/.*",
    r"https://github\.com/ipxe/.*",
    r"https://blog\.thunderbird\.net/.*",
    # Unreleased / forthcoming Discourse posts
    r"https://discourse\.ubuntu\.com/t/edubuntu-.*",
    r"https://discourse\.ubuntu\.com/t/ubuntu-studio-.*",
    # Various, probably rate-limited
    r"https://thekelleys\.org\.uk/gitweb/.*",
    r"https://git\.openldap\.org/.*",
    r"https://github\.com/canonical/.*",
    r"https://github\.com/snapcore/.*",
    r"https://github\.com/systemd/.*",
    r"https://ubuntustudio\.org/ubuntu-studio-.*-release-notes/",
    r"https://www.monitoring-plugins\.org/news/.*",
    r"https://kernelnewbies\.org/.*",
    r"https://cairographics\.org/news/.*",
    r"https?://dark-net\.net/.*",
    # 22.10 release notes: dead (404) and (403) external links
    # 20.04 release notes: bot-challenged links (kept live)
    r"https?://help\.ubuntu\.com/.*",
    r"https://en\.wikipedia\.org/.*",
    r"http://connectivity-check\.ubuntu\.com/",
    r"https?://www\.bluez\.org/.*",
    # Old apt repository host unreachable from CI (historical release notes)
    r"http://archive\.canonical\.com/.*",
    # 22.10 release notes: dead (404) and bot-challenged (403) external links
    r"https://bind9\.readthedocs\.io/en/v9_18_7/manpages\.html.*",
    r"https://docs\.docker\.com/release-notes/.*",
    r"https://www\.raspberrypi\.com/.*",
    r"https://docs\.kernel\.org/admin-guide/gpio/sysfs\.html",
    r"https://kubuntu\.org/news/.*",
    r"https://ubuntuunity\.org/blog/.*",
    # 10.10 release notes: bot-challenged / TLS-broken external links
    r"https?://www\.kdedevelopers\.org/.*",
    r"https?://help\.ubuntu\.com/community/UEC/Images",
    r"https?://help\.ubuntu\.com/community/MaverickUpgrades/Kubuntu",
    r"http://www\.mythtv\.org/.*",
    # 9.10 release notes: bot-challenged (403 / timeout) external links
    r"https?://help\.ubuntu\.com/community/UEC.*",
    r"http://one\.ubuntu\.com.*",
    r"http://wiki\.samba\.org/index\.php/Windows7.*",
    r"https://www\.samba\.org.*",
    # 8.10 release notes: bot-challenged (403) external link
    r"http://psubuntu\.com/.*",
    # 8.04 release notes: archive.canonical.com times out from CI
    r"https?://archive\.canonical\.com/.*",
    # 11.10 release notes: bot-challenged (timeout / 418) external links
    r"https?://www\.compiz\.org.*",
    r"http://www\.freedesktop\.org/.*",
    r"https?://paste\.ubuntu\.com/.*",
    # Debian wiki serves a bot challenge page without the expected anchors
    r"https?://wiki\.debian\.org/.*",
    # KDE Bugzilla rejects CI runners (403 / unreachable); live for humans
    r"https://bugs\.kde\.org/.*",
]

# A regex list of URLs where anchors are ignored by 'make linkcheck'
linkcheck_anchors_ignore_for_url = [
    r"https://github\.com/.*",
    # Discourse anchor IDs change when posts are edited
    r"https://discourse\.ubuntu\.com/.*",
    # GitLab release tag anchors are not standard HTML ids
    r"https://gitlab\.freedesktop\.org/.*",
    # Ubuntu documentation anchors may drift between doc versions
    r"https://documentation\.ubuntu\.com/.*",
    # Launchpad bug list anchors use non-standard fragment format
    r"https://launchpad\.net/.*",
    # External project changelogs with non-stable anchor IDs
    r"https://chrony-project\.org/.*",
    # Dovecot docs restructure anchors between versions
    r"https://doc\.dovecot\.org/.*",
    # Raspberry Pi docs restructure anchors
    r"https://www\.raspberrypi\.com/.*",
]

# How long the link checker will wait for a response for each request
linkcheck_timeout = 15

# Give linkcheck multiple tries on failure
linkcheck_retries = 2

# Number of parallel workers for linkcheck (default is 5)
# Higher values work well for network I/O-bound tasks
linkcheck_workers = 20

########################
# Configuration extras #
########################

# Custom MyST syntax extensions; see
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
# NOTE: By default, the following MyST extensions are enabled:
#   - substitution
#   - deflist
#   - linkify
myst_enable_extensions = {
    "colon_fence",
}

# Custom Sphinx extensions; see
# https://www.sphinx-doc.org/en/master/usage/extensions/index.html
extensions = [
    "canonical_sphinx",
    "notfound.extension",
    "sphinx_design",
    "sphinx_rerediraffe",
    "sphinx_reredirects",
    "sphinx_tabs.tabs",
    "sphinxcontrib.jquery",
    "sphinxext.opengraph",
    "sphinx_config_options",
    "sphinx_contributor_listing",
    "sphinx_filtered_toctree",
    "sphinx_llm.txt",
    "sphinx_related_links",
    "sphinx_roles",
    "sphinx_terminal",
    "sphinx_ubuntu_images",
    "sphinx_youtube_links",
    "sphinxcontrib.cairosvgconverter",
    "sphinx_last_updated_by_git",
    "sphinx.ext.intersphinx",
    "sphinx_sitemap",
    "sphinx_timeline",
]

# Excludes files or directories from processing
exclude_patterns = [
    "reuse/*-template.md",
    ".venv*",
]

# Adds custom CSS files, located remotely or in 'html_static_path'.
html_css_files = ["custom.css"]

# Adds custom JavaScript files, located remotely or in 'html_static_path'.
# html_js_files = [
#     "https://assets.ubuntu.com/v1/287a5e8f-bundle.js",
# ]

# Appends extra markup to the end of every document written in reST
rst_epilog = """
.. include:: /reuse/links.txt
.. include:: /reuse/substitutions.txt
"""

# Feedback button at the top; enabled by default
# TODO: Disable the button if your project is unsuitable for public feedback.
# disable_feedback_button = True

# Your manpage URL
# NOTE: If set, adding ':manpage:' to an .rst file
#       adds a link to the corresponding man section at the bottom of the page.
manpages_url = (
    "https://manpages.ubuntu.com/manpages/resolute/en/"
    + "man{section}/{page}.{section}.html"
)

# Specifies a reST snippet to be prepended to each .rst file
# This defines a :center: role that centers table cell content.
# This defines a :h2: role that styles content for use with PDF generation.
rst_prolog = """
.. role:: center
   :class: align-center
.. role:: h2
    :class: hclass2
.. role:: woke-ignore
    :class: woke-ignore
.. role:: vale-ignore
    :class: vale-ignore
"""

# Workaround for https://github.com/canonical/canonical-sphinx/issues/34
if "discourse_prefix" not in html_context and "discourse" in html_context:
    html_context["discourse_prefix"] = html_context["discourse"] + "/t/"

# Workaround for substitutions.yaml
if os.path.exists("./reuse/substitutions.yaml"):
    with open("./reuse/substitutions.yaml", "r") as fd:
        myst_substitutions = yaml.safe_load(fd.read())

# Add configuration for intersphinx mapping
intersphinx_mapping = {
    "sphinxcontrib-mermaid": (
        "https://sphinxcontrib-mermaid-demo.readthedocs.io/en/latest",
        None,
    )
}
