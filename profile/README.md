<p align="center"><img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/etabli-suite.svg" alt="Établi" width="112"></p>
<h1 align="center">Établi Suite</h1>
<p align="center">Tools for research, local knowledge work, games and self-hosted services.<br>By R. Heller.</p>

Établi is under active development. Each repository documents its implemented features, first-use commands and verification limits. Existing GitHub prereleases are development snapshots; new source changes are not automatically included in those downloads. Store publication and device acceptance are separate release steps.

## Projects

| Project | Current purpose | Implementation and distribution |
|---|---|---|
| [Atelier](https://github.com/etabli-dev/etabli-atelier) | Local R/WebR and Python/Pyodide workspace with bundled scientific packages and plots. | Flutter; Android development APKs. iOS/desktop runners need platform checks. |
| [Vitrine](https://github.com/etabli-dev/etabli-vitrine) | Import and run R Shiny source or shinylive bundles, including offline examples. | Flutter; Android development APKs. iOS/desktop runners need platform checks. |
| [Courrier](https://github.com/etabli-dev/etabli-courrier) | Local mail, calendar, contacts, tasks, reminders, notes and feeds; incoming IMAP and Nextcloud synchronization. | Flutter; production and demo paths are distinct. Provider/device validation remains necessary. |
| [Recueil](https://github.com/etabli-dev/etabli-recueil) | Local research-library ingestion, storage, verification and reading workflows. | TypeScript CLI, server and web application; see its setup and integration gates. |
| [Doc](https://github.com/etabli-dev/etabli-doc) | Browse/search Paperless-ngx documents; iOS also downloads previews. | Native Android and iOS clients; own HTTPS server and token required. |
| [Table](https://github.com/etabli-dev/etabli-table) | Browse tables and rows in a configured SeaTable base. | Native Android and iOS clients; viewing UI with bounded result windows. |
| [Projet](https://github.com/etabli-dev/etabli-projet) | Browse OpenProject projects/work packages; iOS includes subject editing. | Native Android and iOS clients; own HTTPS server and token required. |
| [Nuage](https://github.com/etabli-dev/etabli-nuage) | Check URLs from CSV files and retain/export results; optional WebDAV CSV/log exchange. | Native Android and iOS. General file management, contacts and calendar are future work. |
| [Focus](https://github.com/etabli-dev/etabli-focus) | Category-based focus timers, weekly targets and local session statistics. | Native Android and iOS; notification and upgrade behavior needs device acceptance. |
| [Plume](https://github.com/etabli-dev/etabli-plume) | Search, copy and favourite bundled LaTeX commands and snippets. | Native Android and iOS; local dictionary and preferences. |
| [BranchXO](https://github.com/etabli-dev/etabli-branchxo) | Tic-tac-toe with replay, alternate branches, AI and probability views. | React Native/Expo; Android and browser checks, iOS source. |
| [Lattttice](https://github.com/etabli-dev/etabli-lattttice) | Four-dimensional tic-tac-toe on a 4×4×4×4 board. | React Native/Expo; Android and browser checks, iOS source. |

## Privacy and offline use

The suite has no shared hosted account or analytics service. Server clients require credentials for the services you configure. Their secure-storage implementation, cached data, backup behavior and network scope are documented per repository.

Games and bundled examples can operate locally. Imported scripts, Shiny applications and checked web pages can request external resources; they are not a sandbox for untrusted code. Courrier retains local data and refreshes configured services explicitly. Recueil's optional integrations require their own services. Offline capability differs by workflow.

## Development and releases

Android development downloads, where available, are on each repository's Releases page. They are not store-approved production releases. App Store, Google Play and F-Droid publication are not established by this profile. Follow each project's README for the current source build and its audit/refinement record for observed checks and remaining gates.

The apps share the Coder visual vocabulary: a green accent, restrained borders and monospaced code/value displays. Platform behavior and accessibility should be evaluated in each app; a shared design does not imply identical functionality.

## Documentation and support

Start with a project's README; it links to its guides, source, tests and release records. Historical screenshots and documentation sites can describe earlier builds.

[Support development on Liberapay](https://liberapay.com/rabanheller/).

## Licensing

Consult each repository's LICENSE and NOTICE. Application code and bundled runtimes can have different licenses; Atelier and Vitrine document their WebR/GPL and other runtime components in THIRD_PARTY.md. © 2026 R. Heller.
