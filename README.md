# Boîtes à livres — la plus proche

Petite app web (un seul `index.html`, sans build) qui localise la boîte à livres la plus proche et lance l'itinéraire dans Google Maps, Plans (Apple) ou Waze.

## Fichiers

- `index.html` : l'app (carte Leaflet + fond vectoriel OpenFreeMap (clair / sombre), regroupement des marqueurs, recherche d'adresse via la Base Adresse Nationale)
- `data/boites.json` : 19 080 boîtes `[lat, lon, id, adresse]`, issues de l'export GPX de boites-a-livres.fr (données OpenStreetMap, licence ODbL)
- `update_data.py` : retélécharge l'export et régénère `data/boites.json`
- `manifest.webmanifest`, `icon.svg` : pour « Ajouter à l'écran d'accueil »

## Lancer en local

```bash
python3 -m http.server 8765
```

Puis ouvrir http://localhost:8765.

## Utiliser sur le téléphone

La géolocalisation du navigateur exige HTTPS. Le plus simple : déposer le dossier sur un hébergement statique gratuit (GitHub Pages, Netlify Drop, Cloudflare Pages), ouvrir l'URL sur le téléphone, puis « Ajouter à l'écran d'accueil ».

## Mettre à jour les données

```bash
python3 update_data.py
```
