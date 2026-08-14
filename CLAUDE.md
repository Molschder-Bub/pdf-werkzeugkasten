# Projekt-Anweisungen

## Projektstruktur

- `index.html` = das gesamte Tool (sellgrad PDF-Werkzeugkasten). **Eine einzige,
  eigenständige Datei**: alle Bibliotheken, die sellgrad-Logos (Marke in der
  Sidebar, Lockup im Footer) und das Favicon sind als Base64/Data-URI **direkt
  eingebettet**. Es gibt **keine
  externen Verweise** – die Datei läuft komplett offline und ist die Datei zum
  Versenden (z. B. per Teams).
- `sellgrad-lockup-light@486.png` = Lockup mit dunkler Tinte (für helle
  Flächen, z. B. Footer).
- `sellgrad-lockup-dark@486.png` = Lockup mit heller Tinte (für dunkle
  Flächen; daraus stammen Marke in der Sidebar-Kachel und Favicon).
- `Dockerfile` / `.dockerignore` = nur fürs Hosting auf Railway; liefert
  ausschliesslich `index.html` statisch aus (ändert das Tool selbst nicht).

**Wichtig:** Beim Bearbeiten von `index.html` darf **kein** externer Verweis
(`http(s)://`, externe Datei) eingefügt werden. Neue Assets immer als Data-URI
einbetten, damit die Datei eine einzige, offline-fähige Datei bleibt.

## Branding-Schutz (CI)

- `.github/check-branding.py` prüft, ob Favicon, Sidebar-Marke, Footer-Lockup
  und die Copyright-Zeile in `index.html` vorhanden und sichtbar sind.
- Die GitHub Action `.github/workflows/branding.yml` führt das bei **jedem**
  Push und Pull Request aus — ein Stand ohne sellgrad-Marke wird rot.
- Vor dem Push lokal prüfen: `python3 .github/check-branding.py`.

## Git-Workflow (automatisch)

Nach **jeder** Änderung an Dateien in diesem Projekt automatisch und **ohne
Rückfrage**:

1. `git add -A`
2. `git commit` mit einer sinnvollen, beschreibenden Commit-Nachricht (auf Deutsch)
3. `git push` nach `origin` (Branch `main`)

## Versionsnummer (automatisch erhöhen)

Bei **jeder neuen Version** (= Commit mit einer funktionalen/sichtbaren Änderung)
die Versionsnummer **hochzählen**:

- Sie steht im Footer von `index.html` als „Copyright sellgrad, JS, Vers. X.Y".
- Schema: Minor-Stelle um **+0.1** (1.0 → 1.1 → … → 1.9 → 2.0).
- Reine Doku-/Hilfsänderungen (z. B. nur `CLAUDE.md`) brauchen keine Erhöhung.

## sellgrad-Branding

- Farben: Blau `#1b34d6`, Hellblau `#7d97ff`, Tinte `#101114`,
  Papier `#e9e7e2`.
- Blau = Hauptakzent (Buttons, aktive Elemente), Tinte = Dunkelton,
  Hellblau = Akzent/Fokus. Zentral als CSS-Variablen in `:root`
  (`--primary`, `--accent`, `--dark` …).

## Repo / Identität

- Remote: `origin` → https://github.com/Molschder-Bub/pdf-werkzeugkasten (öffentlich)
- Commit-Identität (nur dieses Repo): `Jens Sellgrad <Molschder-Bub@users.noreply.github.com>`
- `.claude/` und `.build/` bleiben per `.gitignore` ausgeschlossen.

## Hosting (Railway)

- Projekt `pdf-werkzeugkasten` in der Workspace „Molschder's Projects",
  Service `pdf-werkzeugkasten`.
- Öffentliche URL: https://pdf-werkzeugkasten-production.up.railway.app
- Neu ausrollen nach einer Änderung an `index.html`:
  `railway up --ci -y -s pdf-werkzeugkasten`
