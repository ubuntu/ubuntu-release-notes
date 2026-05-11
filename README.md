# Ubuntu release notes

This repository stores the sources for the Ubuntu release notes.

The content is written in the MyST dialect of Markdown, built using Sphinx and published on Read the Docs.

## Read the release notes

To browse the release notes for current and upcoming Ubuntu releases, go to <https://documentation.ubuntu.com/release-notes/>.

## Contribute

To add or edit a release note, see [How to contribute to Ubuntu release notes](https://documentation.ubuntu.com/release-notes/contribute/).

## Build the documentation

To build the documentation locally, use Sphinx:

```bash
cd docs
```

```bash
make run
```

### Translating the documentation

To translate the documentation, you first need to update the translation template files to match the latest source documents.

Run the following command:

```bash
cd docs
make update-po DOCS_LANG=ja
```

This will generate or update `.po` files under the `locale/<lang>/` directory (for example, `locale/ja/LC_MESSAGES/`).

If new `.po` files are created, make sure to add them to Git:

```bash
git add locale/
git commit -m "Add new translation files"
```

After that, edit the `.po` files to add or update translations.
