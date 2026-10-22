#!/usr/bin/env python3
"""Télécharge l'export GPX de boites-a-livres.fr et régénère data/boites.json.

Format de sortie : [[lat, lon, id, adresse], ...]
Données issues d'OpenStreetMap (ODbL).
"""
import json, re, urllib.request, xml.etree.ElementTree as ET
from pathlib import Path

URL = "https://www.boites-a-livres.fr/dumps/boites.gpx"
OUT = Path(__file__).parent / "data" / "boites.json"
NS = {"g": "http://www.topografix.com/GPX/1/1"}

req = urllib.request.Request(URL, headers={"User-Agent": "boites-a-livres-app"})
root = ET.fromstring(urllib.request.urlopen(req, timeout=60).read())
out = []
for w in root.findall("g:wpt", NS):
    m = re.search(r"(\d+)", w.findtext("g:name", "", NS))
    out.append([round(float(w.get("lat")), 6), round(float(w.get("lon")), 6),
                int(m.group(1)) if m else 0, w.findtext("g:desc", "", NS).strip()])
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"{len(out)} boîtes écrites dans {OUT}")
