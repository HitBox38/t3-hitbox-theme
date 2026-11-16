# Hitbox

A game-editor theme for [T3 Code](https://t3.codes): charcoal panels, cyan accents, a drifting grid, and animated collision-box outlines. Focus the composer to lock onto its target box. Hover a thread or button to see the dashed outline march, then press to flash a red hitbox.

Includes dark and light palettes, matching terminal colors, and reduced-motion support. The dashed outlines use tiny embedded SVGs; the theme needs no external images, fonts, or services.

## Install

```sh
curl -fsSL https://raw.githubusercontent.com/HitBox38/t3-hitbox-theme/main/hitbox.json -o hitbox.json
t3 theme set hitbox.json
```

T3 applies Hitbox to connected desktop and web clients. The theme defaults to dark and includes a light variant; choose your appearance in Settings → Appearance.

To switch back, pick another theme in the theme picker or run:

```sh
t3 theme set t3-chat
```

### Let your agent install it

Paste this into a T3 Code thread:

> Install the Hitbox theme from https://github.com/HitBox38/t3-hitbox-theme. Follow the "Instructions for agents" section of its README.

### Instructions for agents

1. Download `https://raw.githubusercontent.com/HitBox38/t3-hitbox-theme/main/hitbox.json`.
2. If the `t3` command is available, run `t3 theme set <path to hitbox.json>`.
3. Otherwise, read the theme guide with `t3_theme_read`, then call `t3_theme_set` with `themeId: "hitbox"` and the downloaded JSON object as `theme`.
4. Install the file as provided. It contains both appearances and the complete animations.

## Requirements

- A recent T3 Code build with custom themes, such as the November 2026 Nightly.
- Desktop or web. T3's mobile app does not use custom themes.

## Interactions

- The conversation's cyan grid drifts diagonally and gently changes brightness.
- Hover threads and buttons for marching dashed collision boxes; press for a red hitbox flash.
- Selecting a thread draws a frame inward until it locks into corner reticles.
- Focusing the composer snaps in an animated dashed target box.
- The send button powers up like an arcade key when text is ready, then depresses when pressed.
- The theme reduces decorative motion when the system requests reduced motion.

Some effects follow T3's UI selectors. Future layout changes may require CSS updates.

## Change the theme yourself

- `palette.json` contains the theme metadata and both color palettes.
- `theme.css` contains the commented styles, embedded SVGs, and animations.
- `build.py` combines them into the installable `hitbox.json` and checks T3's 20,000-character CSS limit.

After editing the sources, rebuild and install:

```sh
python3 build.py
python3 build.py --check
t3 theme set hitbox.json
```

Python 3 is only needed to rebuild. Installing the published JSON requires no build tools or dependencies.

## License

[MIT](LICENSE)
