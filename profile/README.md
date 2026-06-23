# Etabli Suite

A coordinated suite of privacy-respecting mobile apps for **research,
knowledge-work, and self-hosted-cloud workflows**. No analytics, no third-party
SDKs, no accounts. Everything is Apache-2.0.

Built by [R. Heller](mailto:raban.heller@outlook.com).

---

## The apps

### Flagship runtimes
What nobody else ships: real scientific runtimes, running offline, on your phone.

| App | What it does | Platforms |
|-----|--------------|-----------|
| **[Atelier](https://github.com/etabli-dev/atelier)** | Offline R + Python IDE | iOS · Android · Desktop |
| **[Vitrine](https://github.com/etabli-dev/vitrine)** | Offline Shiny app runner | iOS · Android · Desktop |

### Self-hosted clients
Thin, minimal clients that talk only to **your own** server — never to ours.

| App | Backend | Platforms |
|-----|---------|-----------|
| **[Doc](https://github.com/etabli-dev/doc)** | Paperless-ngx | iOS · Android |
| **[Table](https://github.com/etabli-dev/table)** | SeaTable | iOS · Android |
| **[Projet](https://github.com/etabli-dev/projet)** | OpenProject | iOS · Android |
| **[Nuage](https://github.com/etabli-dev/nuage)** | Nextcloud client — files, contacts, calendar, link checks | iOS · Android |

### Offline tools
Small, focused, fully offline.

| App | What it does | Platforms |
|-----|--------------|-----------|
| **[Focus](https://github.com/etabli-dev/focus)** | Pomodoro session tracker | iOS · Android |
| **[Plume](https://github.com/etabli-dev/plume)** | LaTeX command reference | iOS · Android |


> _Statistical power analysis (formerly a standalone app) is now delivered as a Shiny app runnable in **Vitrine** — no separate install needed._

## Where to get them

- **iOS:** App Store
- **Android:** Google Play, and F-Droid
  - Doc, Table, Projet, Nuage, Focus, Plume → **main F-Droid repository**
  - Atelier, Vitrine → **[Etabli F-Droid repo](#)** (they bundle scientific
    runtimes that the main repo's build server can't compile from source)

## Shared design & principles

- **Coder Design System** — one accent (`#28A745`), light / dark / system, identical across iOS, Android and Flutter.
- **Privacy-first** — zero analytics, zero third-party SDKs, credentials only in the platform secure store.
- **Offline-first** — runtimes run on-device; clients touch only your self-hosted backend.

## Support

If these are useful to you: [☕ Buy Me a Coffee](https://buymeacoffee.com/rabanheller) · [💚 Liberapay](https://liberapay.com/rabanheller/)

## License

Every repository is licensed under the **Apache License 2.0**.
