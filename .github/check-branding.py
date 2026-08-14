#!/usr/bin/env python3
"""Prueft, ob die sellgrad-Marke in index.html vollstaendig vorhanden ist.

Wird von der GitHub Action `.github/workflows/branding.yml` bei jedem Push
und jedem Pull Request ausgefuehrt und schlaegt fehl, sobald Favicon,
Sidebar-Marke, Footer-Lockup oder die Copyright-Zeile fehlen, leer sind
oder per CSS unsichtbar gemacht wurden.

Laesst sich auch lokal aufrufen:  python3 .github/check-branding.py
"""

import re
import sys
from pathlib import Path

HTML = Path(__file__).resolve().parent.parent / "index.html"

DATA_URI = r'data:image/(?:png|x-icon|vnd\.microsoft\.icon);base64,([A-Za-z0-9+/=]+)'

fehler = []
ok = []


def pruefe(name, bedingung, hinweis):
    (ok if bedingung else fehler).append(name if bedingung else f"{name} — {hinweis}")


def tags(html, tagname):
    return re.findall(rf"<{tagname}\b[^>]*>", html, re.I)


def main():
    if not HTML.exists():
        print(f"FEHLER: {HTML} nicht gefunden.")
        return 1
    html = HTML.read_text(encoding="utf-8")

    # 1 · Favicon: eingebettetes Icon im <head>
    favicon = [t for t in tags(html, "link") if 'rel="icon"' in t.lower()]
    treffer = re.search(DATA_URI, favicon[0]) if favicon else None
    pruefe("Favicon (eingebettetes Icon)",
           bool(treffer) and len(treffer.group(1)) > 800,
           "kein oder zu kleines Data-URI im <link rel=\"icon\">")

    # 2 · Marke in der Sidebar-Kachel
    kachel = re.search(r'class="brand-logo-icon"\s*>(.*?)</div>', html, re.S)
    treffer = re.search(DATA_URI, kachel.group(1)) if kachel else None
    pruefe("Sidebar-Marke (.brand-logo-icon)",
           bool(treffer) and len(treffer.group(1)) > 800,
           "kein eingebettetes Logo in der Marken-Kachel")

    # 3 · Lockup im Footer
    lockup = [t for t in tags(html, "img") if "footer-logo" in t]
    treffer = re.search(DATA_URI, lockup[0]) if lockup else None
    pruefe("Footer-Lockup (img.footer-logo)",
           bool(treffer) and len(treffer.group(1)) > 4000,
           "kein oder zu kleines Data-URI im Footer-Logo")

    # 4 · Footer-Lockup darf nicht per CSS versteckt werden
    regel = re.search(r"\.footer-logo\s*\{([^}]*)\}", html)
    inhalt = (regel.group(1) if regel else "").replace(" ", "").lower()
    pruefe("Footer-Lockup sichtbar",
           bool(regel) and "display:none" not in inhalt
           and "visibility:hidden" not in inhalt and "opacity:0;" not in inhalt,
           "CSS-Regel .footer-logo fehlt oder blendet das Logo aus")

    # 5 · Copyright-Zeile mit Versionsnummer
    pruefe("Copyright-Zeile",
           bool(re.search(r"Copyright sellgrad, JS, Vers\. \d+\.\d+", html)),
           "Zeile \"Copyright sellgrad, JS, Vers. X.Y\" fehlt")

    for zeile in ok:
        print(f"  OK      {zeile}")
    for zeile in fehler:
        print(f"  FEHLER  {zeile}")

    if fehler:
        print("\nDie sellgrad-Marke ist unvollstaendig — dieser Stand darf nicht "
              "ins Repository. Bitte Logo, Favicon und Copyright-Zeile in "
              "index.html wiederherstellen.")
        return 1

    print("\nsellgrad-Marke vollstaendig.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
