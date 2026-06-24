<p align="center">
  <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/etabli-suite.svg" alt="Établi" width="112">
</p>

<h1 align="center">Établi Suite</h1>

<p align="center">
  Privacy-first, offline-capable mobile and desktop apps for research, knowledge
  work and self-hosted workflows — plus a pair of abstract strategy games.<br>
  Apache-2.0 · by R. Heller.
</p>

<p align="center">
  <strong>Status: in active development.</strong> There are no App Store, Google
  Play or F-Droid releases yet. Right now every app is distributed <strong>only as
  an Android development build (signed APK) on GitHub Releases</strong> — currently
  <strong>v0.1.0 prereleases</strong>. iOS and desktop builds are planned.
</p>

> **How to install:** open an app's **v0.1.0** release linked below, download the
> `*-0.1.0.apk` asset, and install it on Android (enable "install unknown apps").
> These are debug-signed development builds — expect rough edges.

---

## Flagship runtimes

Real scientific runtimes — R and Python — on the device. No cloud, no telemetry,
no accounts.

|  | App | What it does | Platforms (target) | Android dev build |
|--|-----|--------------|--------------------|-------------------|
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-atelier.svg" width="28" alt=""> | **Atelier** | Offline IDE for R (WebR) and Python (Pyodide) with a shared virtual filesystem; `numpy`, `pandas`, `scipy`, `matplotlib`, `scikit-learn` pre-bundled. | iOS · Android · macOS · Linux · Windows | [v0.1.0 APK](https://github.com/etabli-dev/etabli-atelier/releases/tag/v0.1.0) |
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-vitrine.svg" width="28" alt=""> | **Vitrine** | Run Shiny apps offline (shinylive + WebR) — import a bundle and it stages and runs locally. | iOS · Android · macOS · Linux · Windows | [v0.1.0 APK](https://github.com/etabli-dev/etabli-vitrine/releases/tag/v0.1.0) |

## Strategy games

Abstract strategy made tactile — tic-tac-toe pushed past its limits. Fully
offline, with live analysis and an AI opponent.

|  | App | Idea | Platforms (target) | Android dev build |
|--|-----|------|--------------------|-------------------|
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-lattttice.svg" width="28" alt=""> | **lattttice** | Four-dimensional tic-tac-toe on a 4×4×4×4 board (256 cells, four in a row). Four ways to see one position — grid of grids, slices, a 3D Schlegel projection, and a strength heat-map — plus win probability. | Android | [v0.1.0 APK](https://github.com/etabli-dev/etabli-lattttice/releases/tag/v0.1.0) |
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-branchxo.svg" width="28" alt=""> | **branchxo** | Multiverse tic-tac-toe: a 3×3 game where you scrub the move timeline, **fork alternate universes**, and track win probability across every branch. | Android | [v0.1.0 APK](https://github.com/etabli-dev/etabli-branchxo/releases/tag/v0.1.0) |

## Self-hosted clients

Lean, minimal clients that talk only to your own instance — never to a third
party. *(Data screens need your own backend; set the server + credentials in
Settings.)*

|  | App | Backend | Platforms (target) | Android dev build |
|--|-----|---------|--------------------|-------------------|
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-doc.svg" width="28" alt=""> | **Doc** | Paperless-ngx | iOS · Android | [v0.1.0 APK](https://github.com/etabli-dev/etabli-doc/releases/tag/v0.1.0) |
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-table.svg" width="28" alt=""> | **Table** | SeaTable | iOS · Android | [v0.1.0 APK](https://github.com/etabli-dev/etabli-table/releases/tag/v0.1.0) |
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-projet.svg" width="28" alt=""> | **Projet** | OpenProject | iOS · Android | [v0.1.0 APK](https://github.com/etabli-dev/etabli-projet/releases/tag/v0.1.0) |
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-nuage.svg" width="28" alt=""> | **Nuage** *(in development)* | Nextcloud — files and the link checker round-trip today; Contacts (CardDAV) and Calendar (CalDAV) to follow. | iOS · Android | [v0.1.0 APK](https://github.com/etabli-dev/etabli-nuage/releases/tag/v0.1.0) |

## Offline tools

Small, focused, fully offline.

|  | App | What it does | Platforms (target) | Android dev build |
|--|-----|--------------|--------------------|-------------------|
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-focus.svg" width="28" alt=""> | **Focus** | Pomodoro / focus-session tracker with per-weekday targets, categories and stats. | iOS · Android | [v0.1.0 APK](https://github.com/etabli-dev/etabli-focus/releases/tag/v0.1.0) |
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-plume.svg" width="28" alt=""> | **Plume** | Reference and snippet-picker for typesetting commands: commands, Greek letters, math operators, formatting, environments, bibliography. | iOS · Android | [v0.1.0 APK](https://github.com/etabli-dev/etabli-plume/releases/tag/v0.1.0) |

> Plume is the deliberate rename of the former *EtabliTeX*. Not affiliated with
> TeX or the LaTeX Project.

---

## Cross-cutting

### Coder design system
A single accent (`#28A745`), light / dark / system, **JetBrains Mono** for code
and values, hairline dividers instead of shadow layers. Identical across iOS,
Android and Flutter — central tokens in
[`design/coder-design-system.json`](https://github.com/etabli-dev/etabli-atelier/blob/main/design/coder-design-system.json)
in each app repo.

### Privacy
No analytics. No third-party SDKs. No accounts. Credentials, where needed, live
only in the platform secure store (iOS Keychain · Android EncryptedSharedPreferences).

### Offline-first
Scientific runtimes and games run on the device. Self-hosted clients talk only to
the instance you point them at. No implicit network requests.

---

## Availability

The suite is **in active development**. App Store, Google Play and F-Droid
releases are **planned but not yet available**.

| Channel | Status |
|---------|--------|
| **Android (APK)** | **Available now** — `v0.1.0` development builds on each repo's **GitHub Releases** (links above). |
| **App Store** (iOS) | planned — not yet available |
| **Google Play** | planned — not yet available |
| **F-Droid** | planned — not yet available |

All current builds are **debug-signed development prereleases** at version
**0.1.0**.

## Vignettes

Companion Quarto sites with tutorials, screenshots and examples:

- <https://etabli-dev.github.io/etabli-atelier/>
- <https://etabli-dev.github.io/etabli-vitrine/>
- <https://etabli-dev.github.io/etabli-doc/>
- <https://etabli-dev.github.io/etabli-table/>
- <https://etabli-dev.github.io/etabli-projet/>
- <https://etabli-dev.github.io/etabli-nuage/>
- <https://etabli-dev.github.io/etabli-focus/>
- <https://etabli-dev.github.io/etabli-plume/>
- <https://etabli-dev.github.io/etabli-lattttice/> *(game)*
- <https://etabli-dev.github.io/etabli-branchxo/> *(game)*

## Support

- [**Liberapay** (`rabanheller`)](https://liberapay.com/rabanheller/) — recurring support via the FOSS surface.
- *Buy Me a Coffee* is planned as the in-app link once store builds ship.

---

## License

Apache-2.0 · © 2026 R. Heller.
