#!/usr/bin/env python3
"""Statischer Server fuer den PDF-Werkzeugkasten (nur fuers Hosting auf Railway).

Zwei Unterschiede zum blossen `python3 -m http.server`:

1. `/status` antwortet mit einem winzigen "ok" statt mit der 4-MB-Datei.
   sellgrad.ch fragt diesen Punkt an, bevor es den Werkzeugkasten oeffnet.
2. Die Antworten tragen `Access-Control-Allow-Origin: *`. Nur dadurch kann
   die Website den Status ueberhaupt lesen — laeuft der Dienst nicht mehr,
   fehlt dieser Kopf und die Abfrage schlaegt fehl. Genau daran erkennt die
   Website, dass hier nichts mehr da ist.

Am Werkzeugkasten selbst (index.html) aendert das nichts.
"""

import http.server
import os
import socketserver

VERZEICHNIS = "/srv"
PORT = int(os.environ.get("PORT", "8080"))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=VERZEICHNIS, **kw)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

    def _status(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", "2")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        return b"ok"

    def do_GET(self):
        if self.path.split("?")[0] == "/status":
            self.wfile.write(self._status())
            return
        super().do_GET()

    def do_HEAD(self):
        if self.path.split("?")[0] == "/status":
            self._status()
            return
        super().do_HEAD()


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    with Server(("", PORT), Handler) as httpd:
        print(f"PDF-Werkzeugkasten laeuft auf Port {PORT}", flush=True)
        httpd.serve_forever()
