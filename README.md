# PDF Werkzeugkasten

Ein vollständiger, browserbasierter PDF-Werkzeugkasten – keine Installation, kein Server, kein Tracking. Alle Dateien werden ausschließlich lokal im Browser verarbeitet.

🔗 **Live:** https://molschder-bub.github.io/pdf-werkzeugkasten/

---

## Funktionen

### Organisieren
- **Zusammenführen** – Mehrere PDFs per Drag & Drop sortieren und zu einem Dokument verbinden
- **Teilen** – PDF seitenweise oder nach Bereichen aufteilen (ZIP-Download)
- **Extrahieren** – Einzelne Seiten oder Bereiche als neues PDF speichern
- **Neu anordnen** – Seiten per Drag & Drop in neue Reihenfolge bringen
- **Seiten löschen** – Unerwünschte Seiten entfernen

### Bearbeiten
- **Drehen** – Seiten um 90°, 180° oder 270° drehen
- **Seitenzahlen** – Automatische Seitennummerierung einfügen
- **Wasserzeichen** – Text- oder Bildwasserzeichen hinzufügen
- **Signatur** – Mit der Maus unterschreiben oder ein Signaturbild platzieren
- **Kommentare** – Textstellen markieren und Kommentare einbetten

### Konvertieren
- **Bild → PDF** – JPG/PNG-Bilder in ein PDF umwandeln
- **PDF → Bilder** – Jede Seite als PNG exportieren (ZIP-Download)
- **Bild komprimieren** – JPG/PNG/WebP mit einstellbarer Qualität komprimieren

### Sicherheit
- **Schützen** – PDF mit AES-256 verschlüsseln und Berechtigungen einschränken

---

## Installation & lokale Nutzung

Der PDF Werkzeugkasten ist eine einzelne HTML-Datei ohne Build-System oder Abhängigkeiten. Es gibt zwei Möglichkeiten, ihn zu nutzen:

### Option 1 – Direkt im Browser öffnen

1. Repository herunterladen oder klonen:
   ```bash
   git clone https://github.com/Molschder-Bub/pdf-werkzeugkasten.git
   ```
   > 💡 Hinweis: Dies ist die Repository-Adresse zum Herunterladen des Codes.
   > Die fertige Website ist direkt unter **https://molschder-bub.github.io/pdf-werkzeugkasten/** erreichbar – kein Download nötig.

2. Die Datei `index.html` direkt im Browser öffnen (Doppelklick oder Drag & Drop in den Browser)

> ⚠️ Manche Browser blockieren lokale Dateizugriffe. Falls Funktionen nicht laden, Option 2 verwenden.

---

### Option 2 – Lokaler Webserver (empfohlen)

**Mit Python (vorinstalliert auf macOS/Linux):**
```bash
cd pdf-werkzeugkasten
python3 -m http.server 8080
```
Dann im Browser öffnen: [http://localhost:8080](http://localhost:8080)

**Mit Node.js:**
```bash
npx serve .
```

**Mit VS Code:**
Die Erweiterung [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) installieren → Rechtsklick auf `index.html` → *Open with Live Server*

---

### Selbst hosten (GitHub Pages)

1. Repository forken
2. In den Repository-Einstellungen unter **Settings → Pages** den Branch `main` auswählen
3. Die App ist dann unter `https://<dein-username>.github.io/pdf-werkzeugkasten/` erreichbar

---

## Technologie

- Reines HTML/CSS/JavaScript – keine Abhängigkeiten, kein Build-System
- [PDF-lib](https://pdf-lib.js.org/) – PDF-Erstellung und -Bearbeitung
- [PDF.js](https://mozilla.github.io/pdf.js/) – PDF-Rendering im Browser

---

## Datenschutz

Alle Dateien werden **nur lokal im Browser** verarbeitet. Es werden keine Daten an einen Server übertragen.

---

© 2026 Molschder · Version 1.0
