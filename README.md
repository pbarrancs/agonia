# agonia — Website

Brand presence website for **agonia**, an independent climbing apparel collective based in Mexico. The site communicates the brand's identity, values, and mission to the climbing and outdoor community.

> No e-commerce. Display-only catalog. Static site deployed to Firebase Hosting.

## Latest Updates (2026-05-27)

- Catalog card product names are mapped in UI to brand display names (for example: `Fall T Sólida`, `Cadenas Deslavada`, `Top Back Logo`) without editing `productos.csv`.
- Catalog section headers now show only display collection names (`Fall T`, `Cadenas`, `Back Logo`, `Lágrima`) without `Diseño X` prefixes.
- Home page section title changed from `Videos` to `Clips`.
- Home keeps a single CTA (`Ver catálogo`) and no secondary `Nosotros` card in the hero box.
- Entry-point behavior reverted: root `/` now loads the home page directly (no Firebase redirect to `/catalogo`), while `/catalogo` remains accessible via route and nav.
- Nosotros page includes updated manifesto content plus a bottom dog illustration loaded from:
  `/assets/images/Ilustraciones/Perrito_03/P3_PNG_/P3_BlancoNegro_png/Perrito3_blanco_FondoOscuro.png`.

---

## Tech Stack

| Tool                 | Version         | Role                                                        |
| -------------------- | --------------- | ----------------------------------------------------------- |
| **Astro**            | ^4.16.0         | Static site framework                                       |
| **CSS**              | Plain CSS       | Styling — no Tailwind, no PostCSS                           |
| **Google Fonts**     | CDN             | New Rocker (titles), Nova Cut (subtitles), Syne Mono (body) |
| **Font Awesome 5**   | Bundled locally | Icons (in `public/assets/webfonts/`)                        |
| **Vanilla JS**       | Inline scripts  | Catalog interactivity                                       |
| **Firebase Hosting** | `agonia-255fe`  | Deployment and CDN                                          |

---

## Prerequisites

- **Node.js** v18+ and **npm**
- **Firebase CLI** — required only to deploy:
  ```bash
  npm install -g firebase-tools
  ```

---

## Local Development

```bash
# 1. Clone the repo
git clone https://github.com/pbarrancs/agonia.git
cd agonia/new-astro-site

# 2. Install dependencies
npm install

# 3. Start dev server
npm run dev
```

Then visit `http://localhost:4321`.

---

## Build

```bash
cd new-astro-site
npm run build
```

Output goes to `new-astro-site/dist/`.

---

## Deploy to Firebase

```bash
# From the repo root (not new-astro-site/)
firebase login
firebase deploy
```

Firebase reads `firebase.json`, which points to `new-astro-site/dist/`.

**Live URL:** `https://agonia-255fe.web.app`

---

## Project Structure

```
agonia/
├── firebase.json                  # Firebase Hosting config — serves new-astro-site/dist/
├── .firebaserc                    # Firebase project alias (agonia-255fe)
├── .gitignore
├── new-astro-site/                # Astro project — the live site
│   ├── package.json
│   ├── astro.config.mjs           # output: 'static'
│   ├── dist/                      # Build output (gitignored)
│   ├── public/assets/             # Static assets served as-is
│   │   ├── a_icono.ico
│   │   ├── css/                   # fontawesome-all.min.css
│   │   ├── images/                # bg.jpg, Logos/, Ilustraciones/, etc.
│   │   │   ├── playeras/          # 29 product photos (WebP, 800×483) + placeholder.svg
│   │   │   ├── playeras_original/ # original PNG backups (pre-conversion)
│   │   │   └── playeras_preview/  # 29 preview photos (WebP, 1200×724)
│   │   └── webfonts/              # Font Awesome font files
│   └── src/
│       ├── data/productos.csv     # 144-row product source of truth
│       ├── layouts/Layout.astro   # Base HTML shell
│       ├── components/
│       │   ├── Nav.astro
│       │   ├── Footer.astro
│       │   └── ProductCard.astro
│       ├── pages/
│       │   ├── index.astro
│       │   ├── nosotros.astro
│       │   ├── catalogo.astro
│       │   └── aviso-de-privacidad.astro
│       └── styles/
│           ├── global.css
│           └── catalog.css
├── scripts/
│   ├── process_ventas.py          # Sales data → ventas.csv + inventory update
│   ├── sync_oos.py                # Inventory → productos.csv disponible field
│   └── convert_webp.py            # Converts product PNGs → WebP thumbnails + previews
└── public/                        # Old static site — backup only (remove after 2026-06-02)
```

---

## Configuration

No environment variables. Firebase configuration is handled by two files:

- **`firebase.json`** — declares `new-astro-site/dist/` as the hosting root.
- **`.firebaserc`** — maps the `default` alias to the `agonia-255fe` Firebase project.

---

## Links

| Resource  | URL                                  |
| --------- | ------------------------------------ |
| Website   | https://agonia-255fe.web.app         |
| Instagram | https://www.instagram.com/___agonia/ |
| YouTube   | https://www.youtube.com/@agon_ia     |
