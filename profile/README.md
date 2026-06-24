<p align="center">
  <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/etabli-suite.svg" alt="Établi" width="112">
</p>

<h1 align="center">Établi Suite</h1>

<p align="center">
  Datenschutzorientierte, offline-fähige Mobil- und Desktop-Apps für
  Forschung, Wissensarbeit, selbstgehostete Workflows — und ein Paar
  abstrakter Strategiespiele.<br>
  Apache-2.0 · von R. Heller.
</p>

<p align="center">
  <strong>Status: in aktiver Entwicklung.</strong> Es gibt noch keine
  Veröffentlichung im App Store, bei Google Play oder F-Droid. Aktuell werden
  ausschließlich <strong>Entwicklungs-Builds als signierte APK über GitHub
  Releases</strong> verteilt (Android).
</p>

---

## Flagship-Laufzeiten

Echte wissenschaftliche Laufzeiten — R und Python — auf dem Gerät.
Keine Cloud, keine Telemetrie, keine Konten.

|  | App | Zweck | Plattformen | Repo |
|--|-----|-------|-------------|------|
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-atelier.svg" width="28" alt=""> | **Atelier** | Offline-IDE für R (WebR) und Python (Pyodide) mit gemeinsamem virtuellem Dateisystem; `numpy`, `pandas`, `scipy`, `matplotlib`, `scikit-learn` vorgebündelt. | iOS · Android · macOS · Linux · Windows | [`etabli-atelier`](https://github.com/etabli-dev/etabli-atelier) |
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-vitrine.svg" width="28" alt=""> | **Vitrine** | Offline-Runner für Shiny-Apps (shinylive + WebR). Statistische Power-Analyse wird als Shiny-App in Vitrine ausgeliefert, nicht mehr als eigenständige App. | iOS · Android · macOS · Linux · Windows | [`etabli-vitrine`](https://github.com/etabli-dev/etabli-vitrine) |

## Strategiespiele

Abstrakte Strategie zum Anfassen — Tic-Tac-Toe, über seine Grenzen hinaus
gedacht. Vollständig offline, mit Live-Analyse und KI-Gegner. Bereits als
**v0.1.0**-Entwicklungs-APK verfügbar.

|  | App | Idee | Plattformen | Repo | Release |
|--|-----|------|-------------|------|---------|
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-lattttice.svg" width="28" alt=""> | **lattttice** | Vierdimensionales Tic-Tac-Toe auf einem 4×4×4×4-Brett (256 Felder, vier in einer Reihe). Vier Sichten auf dieselbe Stellung — Raster der Raster, Schnitte, 3D-Schlegel-Projektion, Stärke-Heatmap — plus Gewinnwahrscheinlichkeit. | Android | [`etabli-lattttice`](https://github.com/etabli-dev/etabli-lattttice) | [v0.1.0 (APK)](https://github.com/etabli-dev/etabli-lattttice/releases/tag/v0.1.0) |
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-branchxo.svg" width="28" alt=""> | **branchxo** | Multiversum-Tic-Tac-Toe: ein 3×3-Spiel, in dem man die Zug-Timeline zurückspult, **alternative Universen abzweigt** und Gewinnwahrscheinlichkeiten über alle Verzweigungen hinweg verfolgt. | Android | [`etabli-branchxo`](https://github.com/etabli-dev/etabli-branchxo) | [v0.1.0 (APK)](https://github.com/etabli-dev/etabli-branchxo/releases/tag/v0.1.0) |

## Self-hosted-Clients

Schlanke, minimale Clients, die ausschließlich mit der eigenen Instanz sprechen — nie mit Servern Dritter.

|  | App | Backend | Plattformen | Repo |
|--|-----|---------|-------------|------|
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-doc.svg" width="28" alt=""> | **Doc** | Paperless-ngx | iOS · Android | [`etabli-doc`](https://github.com/etabli-dev/etabli-doc) |
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-table.svg" width="28" alt=""> | **Table** | SeaTable | iOS · Android | [`etabli-table`](https://github.com/etabli-dev/etabli-table) |
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-projet.svg" width="28" alt=""> | **Projet** | OpenProject | iOS · Android | [`etabli-projet`](https://github.com/etabli-dev/etabli-projet) |
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-nuage.svg" width="28" alt=""> | **Nuage** *(in Entwicklung)* | Nextcloud — Dateien und Link-Prüfer round-trippen heute; Kontakte (CardDAV) und Kalender (CalDAV) folgen. | iOS · Android | [`etabli-nuage`](https://github.com/etabli-dev/etabli-nuage) |

## Offline-Werkzeuge

Klein, fokussiert, vollständig offline.

|  | App | Zweck | Plattformen | Repo |
|--|-----|-------|-------------|------|
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-focus.svg" width="28" alt=""> | **Focus** | Pomodoro-Tracker für Fokus-Sessions, mit Kategorien und Verlauf. | iOS · Android | [`etabli-focus`](https://github.com/etabli-dev/etabli-focus) |
| <img src="https://raw.githubusercontent.com/etabli-dev/.github/main/profile/icons/icon-plume.svg" width="28" alt=""> | **Plume** | Referenz und Snippet-Picker für Typesetting-Befehle: Befehle, griechische Buchstaben, Mathe-Operatoren, Formatierung, Umgebungen, Bibliographie. | iOS · Android | [`etabli-plume`](https://github.com/etabli-dev/etabli-plume) |

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
Wissenschaftliche Laufzeiten und Spiele laufen auf dem Gerät. Self-hosted-Clients
sprechen nur mit der vom Nutzer angegebenen Instanz. Keine impliziten
Netzwerkanfragen.

---

## Bezug

Die Suite befindet sich **in aktiver Entwicklung**. Veröffentlichungen im
App Store, bei Google Play und F-Droid sind **geplant, aber noch nicht
verfügbar**.

| Kanal | Status |
|------|--------|
| **Android (APK)** | Entwicklungs-Builds über **GitHub Releases** des jeweiligen App-Repos (Spiele bereits als `v0.1.0`). |
| **App Store** (iOS) | geplant — noch nicht verfügbar |
| **Google Play** | geplant — noch nicht verfügbar |
| **F-Droid** | geplant — noch nicht verfügbar |

## Vignetten

Begleitende Quarto-Sites mit Tutorials, Screenshots und Beispielen:

- <https://etabli-dev.github.io/etabli-atelier/>
- <https://etabli-dev.github.io/etabli-vitrine/>
- <https://etabli-dev.github.io/etabli-doc/>
- <https://etabli-dev.github.io/etabli-table/>
- <https://etabli-dev.github.io/etabli-projet/>
- <https://etabli-dev.github.io/etabli-nuage/>
- <https://etabli-dev.github.io/etabli-focus/>
- <https://etabli-dev.github.io/etabli-plume/>
- <https://etabli-dev.github.io/etabli-lattttice/> *(Spiel)*
- <https://etabli-dev.github.io/etabli-branchxo/> *(Spiel)*

## Unterstützen

- [**Liberapay** (`rabanheller`)](https://liberapay.com/rabanheller/) — wiederkehrende Unterstützung über das FOSS-Surface.
- *Buy Me a Coffee* ist als In-App-Link vorgesehen, sobald die Store-Builds erscheinen.

---

## Lizenz

Apache-2.0 · © 2026 R. Heller.
