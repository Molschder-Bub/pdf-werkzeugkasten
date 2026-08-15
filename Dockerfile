# Statisches Hosting des PDF-Werkzeugkastens (Railway).
# Es wird ausschliesslich die eigenstaendige index.html ausgeliefert.
FROM python:3.12-alpine

WORKDIR /srv
COPY index.html /srv/index.html
COPY serve.py /srv/serve.py

ENV PORT=8080
EXPOSE 8080

CMD ["python3", "/srv/serve.py"]
