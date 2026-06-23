<p align="center">
  <img src="profile/icons/etabli-suite.svg" alt="Etabli" width="112">
</p>

<h1 align="center">Etabli Suite</h1>

<p align="center">
  Datenschutzorientierte, offline-fähige Mobil- und Desktop-Apps für
  Forschung, Wissensarbeit und selbstgehostete Workflows.<br>
  Apache-2.0 · von R. Heller.
</p>

---

## Flagship-Laufzeiten

Echte wissenschaftliche Laufzeiten — R und Python — auf dem Gerät.
Keine Cloud, keine Telemetrie, keine Konten.

|  | App | Zweck | Plattformen | Repo |
|--|-----|-------|-------------|------|
| <img src="profile/icons/icon-atelier.svg" width="28" alt=""> | **Atelier** | Offline-IDE für R (WebR) und Python (Pyodide) mit gemeinsamem virtuellem Dateisystem; `numpy`, `pandas`, `scipy`, `matplotlib`, `scikit-learn` vorgebündelt. | iOS · Android · macOS · Linux · Windows | [`etabli-dev/etabli-atelier`](https://github.com/etabli-dev/etabli-atelier) |
| <img src="profile/icons/icon-vitrine.svg" width="28" alt=""> | **Vitrine** | Offline-Runner für Shiny-Apps (shinylive + WebR). Statistische Power-Analyse wird als Shiny-App in Vitrine ausgeliefert, nicht mehr als eigenständige App. | iOS · Android · macOS · Linux · Windows | [`etabli-dev/etabli-vitrine`](https://github.com/etabli-dev/etabli-vitrine) |

## Self-hosted-Clients

Schlanke, minimale Clients, die ausschließlich mit der eigenen Instanz sprechen — nie mit Servern Dritter.

|  | App | Backend | Plattformen | Repo |
|--|-----|---------|-------------|------|
| <img src="profile/icons/icon-doc.svg" width="28" alt=""> | **Doc** | Paperless-ngx | iOS · Android | [`etabli-dev/etabli-doc`](https://github.com/etabli-dev/etabli-doc) |
| <img src="profile/icons/icon-table.svg" width="28" alt=""> | **Table** | SeaTable | iOS · Android | [`etabli-dev/etabli-table`](https://github.com/etabli-dev/etabli-table) |
| <img src="profile/icons/icon-projet.svg" width="28" alt=""> | **Projet** | OpenProject | iOS · Android | [`etabli-dev/etabli-projet`](https://github.com/etabli-dev/etabli-projet) |
| <img src="profile/icons/icon-nuage.svg" width="28" alt=""> | **Nuage** *(in Entwicklung)* | Nextcloud — Dateien und Link-Prüfer round-trippen heute; Kontakte (CardDAV) und Kalender (CalDAV) folgen. | iOS · Android | [`etabli-dev/etabli-nuage`](https://github.com/etabli-dev/etabli-nuage) |

## Offline-Werkzeuge

Klein, fokussiert, vollständig offline.

|  | App | Zweck | Plattformen | Repo |
|--|-----|-------|-------------|------|
| <img src="profile/icons/icon-focus.svg" width="28" alt=""> | **Focus** | Pomodoro-Tracker für Fokus-Sessions, mit Kategorien und Verlauf. | iOS · Android | [`etabli-dev/etabli-focus`](https://github.com/etabli-dev/etabli-focus) |
| <img src="profile/icons/icon-plume.svg" width="28" alt=""> | **Plume** | Referenz und Snippet-Picker für Typesetting-Befehle: Befehle, griechische Buchstaben, Mathe-Operatoren, Formatierung, Umgebungen, Bibliographie. | iOS · Android | [`etabli-dev/etabli-plume`](https://github.com/etabli-dev/etabli-plume) |

> Plume ist die bewusste Umbenennung des früheren *EtabliTeX*. Nicht mit
> TeX oder dem LaTeX Project affiliiert.

---

## Querschnitt

### Coder Design System
Ein einzelner Akzent (`#28A745`), Hell / Dunkel / System, **JetBrains Mono**
für Code und Werte, Hairline-Trennlinien statt Schattenebenen. Identisch
über iOS, Android und Flutter — zentrale Tokens unter
[`design/coder-design-system.json`](https://github.com/etabli-dev/etabli-atelier/blob/main/design/coder-design-system.json)
im jeweiligen App-Repo.

### Datenschutz
Keine Analytics. Keine Dritt-SDKs. Keine Konten. Anmeldedaten leben — wo
nötig — ausschließlich im Plattform-Schlüsselspeicher (iOS Keychain ·
Android EncryptedSharedPreferences).

### Offline-first
Wissenschaftliche Laufzeiten laufen auf dem Gerät. Self-hosted-Clients
sprechen nur mit der vom Nutzer angegebenen Instanz. Keine impliziten
Netzwerkanfragen.

---

## Bezug

| Kanal | Apps |
|------|------|
| **App Store** (iOS) · **Google Play** (Android) | alle Apps |
| **F-Droid — Haupt-Repository** | Doc, Table, Projet, Nuage, Focus, Plume |
| **F-Droid — eigenes Repository** | Atelier, Vitrine *(bündeln vorgefertigte WebAssembly-Laufzeiten — WebR, Pyodide, shinylive — die der Build-Server des Haupt-Repos nicht aus Quelltext kompilieren kann; Details in `FDROID_NOTES.md` im jeweiligen App-Repo)* |

## Vignetten

Begleitende Quarto-Sites mit Tutorials, Datenmodellen und Beispielen:

- <https://etabli-dev.github.io/etabli-atelier/>
- <https://etabli-dev.github.io/etabli-vitrine/>
- <https://etabli-dev.github.io/etabli-doc/>
- <https://etabli-dev.github.io/etabli-table/>
- <https://etabli-dev.github.io/etabli-projet/>
- <https://etabli-dev.github.io/etabli-nuage/>
- <https://etabli-dev.github.io/etabli-focus/>
- <https://etabli-dev.github.io/etabli-plume/>

## Unterstützen

- [**Liberapay** (`rabanheller`)](https://liberapay.com/rabanheller/) — wiederkehrende Unterstützung über das FOSS-Surface.
- *Buy Me a Coffee* ist der In-App-Link in den jeweiligen Stores (App Store, Google Play).

---

## Lizenz

Apache-2.0 · © 2026 Raban Heller.
