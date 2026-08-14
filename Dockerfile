# Statisches Hosting des PDF-Werkzeugkastens (Railway).
# Es wird ausschliesslich die eigenstaendige index.html ausgeliefert.
FROM python:3.12-alpine

WORKDIR /srv
COPY index.html /srv/index.html

ENV PORT=8080
EXPOSE 8080

CMD ["sh", "-c", "python3 -m http.server ${PORT} --directory /srv"]
