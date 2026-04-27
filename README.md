# brewfile

Personal Homebrew Bundle and homebrew-file setup for bootstrapping a Mac.

The canonical local path is:

```sh
~/.config/brewfile/Brewfile
```

That matches homebrew-file's documented default location when `XDG_CONFIG_HOME` is not set.

## Fresh Mac Bootstrap

Install Apple's command-line tools if needed:

```sh
xcode-select --install
```

Clone this repo into the expected location:

```sh
mkdir -p ~/.config
git clone git@github.com:dgitman/brewfile.git ~/.config/brewfile
```

Run the bootstrap helper:

```sh
~/.config/brewfile/install_apps_via_homebrew.py
```

Or, if `~/bin` is already on `PATH`:

```sh
mac-bootstrap
```

Sign into the Mac App Store before installing `mas` apps.

## Daily Use

With `brew-wrap` enabled in `~/.zshrc`, normal Homebrew changes update the Brewfile automatically:

```sh
brew install jq
brew uninstall jq
```

After a wrapped update, `_post_brewfile_update` commits and pushes the Brewfile change.

## Manual Update

Regenerate the Brewfile from the current machine and push it:

```sh
brewfile-update
```

## Cleanup Preview

Preview packages installed locally but not listed in the Brewfile:

```sh
brewfile-cleanup-preview
```

To actually remove those packages, run Homebrew's cleanup command with `--force` only after reviewing the preview.
