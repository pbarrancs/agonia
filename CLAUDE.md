# CLAUDE.md — agonia website

## What this project is

Brand presence website for **agonia**, an independent climbing apparel collective
based in Mexico. The site communicates the brand's identity, mission, and values
to the climbing and outdoor community. There is no e-commerce or purchasing flow —
the catalog is display-only.

---

## Brand context

- **Category:** Independent climbing apparel (streetwear inspired by climbing culture)
- **Location:** Mexico
- **Audience:** Climbing and outdoor community in Mexico and Latin America
- **Tone:** Independent, aesthetic, community-driven
- **Social:** Instagram [@\_\_\_agonia](https://www.instagram.com/___agonia/) · YouTube [@agon_ia](https://www.youtube.com/@agon_ia)
- **Catalog rule:** Display only — no shopping cart, no checkout, no purchasing flow

---

## Current stack (as found in the project)

| Tool             | Version/Source                                    | Role                                            |
| ---------------- | ------------------------------------------------- | ----------------------------------------------- |
| HTML5            | —                                                 | Single-page static markup (`public/index.html`) |
| CSS              | Strata by HTML5UP (CCA 3.0) + custom brand styles | Layout, typography, brand colors                |
| Sass (SCSS)      | Source in `public/assets/sass/`                   | Sass source for the compiled `main.css`         |
| Google Fonts     | `New Rocker`, `Nova Cut`, `Syne Mono`             | Brand typography (loaded via CDN)               |
| Font Awesome 5   | Bundled locally in `public/assets/webfonts/`      | Social and UI icons                             |
| jQuery           | `public/assets/js/jquery.min.js`                  | DOM utilities (Strata dependency)               |
| jQuery Poptrox   | `public/assets/js/jquery.poptrox.min.js`          | Lightbox gallery (Strata dependency)            |
| Firebase Hosting | Project: `agonia-255fe`                           | Static site deployment and CDN                  |

No `package.json` exists at the project root. No Node.js build step currently.

---

## Brand design tokens (from main.css)

```css
/* Font classes */
.font-titulo {
  font-family: "New Rocker", system-ui;
  color: #e8431e;
}
.font-subtitulo {
  font-family: "Nova Cut", system-ui;
  color: #f4ec62;
}
.font-cuerpo {
  font-family: "Syne Mono", monospace;
  color: #fcfcfc;
}
```

---

## Current project structure

```
agonia/                                  ← repo root
├── firebase.json                        ← Firebase Hosting config; serves from public/
├── .firebaserc                          ← Firebase project alias: agonia-255fe
├── .gitignore                           ← ignores .firebase/, node_modules/, Videos/, *.mp4
├── README.md                            ← project documentation
├── CLAUDE.md                            ← this file
├── public/                              ← current live site (deployed to Firebase)
│   ├── index.html                       ← single-page site; sections: Somos, Misión, Visión,
│   │                                       No negociables, Cómo le hacemos
│   ├── a_icono.ico                      ← browser favicon
│   ├── assets/
│   │   ├── css/
│   │   │   ├── main.css                 ← compiled stylesheet (do not edit directly)
│   │   │   ├── fontawesome-all.min.css  ← Font Awesome CSS
│   │   │   └── images/overlay.png       ← CSS asset used by Strata
│   │   ├── sass/
│   │   │   ├── main.scss                ← Sass entry point
│   │   │   └── libs/                   ← Sass partials: _vars, _functions, _mixins,
│   │   │                                   _vendor, _breakpoints, _html-grid
│   │   ├── js/
│   │   │   ├── main.js                  ← parallax + touch handling (Strata)
│   │   │   ├── jquery.min.js
│   │   │   ├── jquery.poptrox.min.js    ← lightbox
│   │   │   ├── browser.min.js
│   │   │   ├── breakpoints.min.js
│   │   │   └── util.js
│   │   └── webfonts/                   ← 15 Font Awesome font files (.eot/.svg/.ttf/.woff/.woff2)
│   └── images/
│       ├── bg.jpg                       ← page background image
│       ├── avatar.jpg                   ← header avatar
│       ├── avatar_2.jpg
│       ├── nico_razo.gif
│       ├── nico_razo.mp4
│       ├── Fondos/                      ← 7 background color variants (amarillo, beige, blanco,
│       │                                   gria, narajna, rojo, verde) — note: 2 typos in filenames
│       ├── Logos/
│       │   ├── Logo_A_lagrima/A_PNG_/   ← 8 color variants (LogoA_*.png)
│       │   ├── Logo_figura/PNG_/        ← 8 color variants (logo_figura_*.png)
│       │   └── Logo_horizontal/PNG_/   ← 8 color variants; logo_blanco.png used in header
│       │                                   note: lgoo_naranja.png has a typo in filename
│       ├── Ilustraciones/
│       │   ├── Perrito_01/ … Perrito_08/ ← each has BlancoNegro/ (2 files) + Colores/ (11 files)
│       │   └── Personaje_A/             ← same structure as Perritos
│       ├── fulls/                       ← gallery images 01.jpg–06.jpg
│       └── thumbs/                      ← gallery thumbnails 01.jpg–06.jpg
├── scripts/
│   ├── convert_mod.py                   ← video conversion script (not web-related)
│   └── convert_mts.py                   ← video conversion script (not web-related)
└── Documentos/                          ← brand docs, drafts, inventory — not web-related
```

---

## Firebase deployment

- **Config file:** `firebase.json` — currently serves from `public/`
- **Project alias:** `.firebaserc` → `agonia-255fe`
- **Deploy command:** `firebase deploy` (from repo root, after `firebase login`)
- **Live URL:** `https://agonia-255fe.web.app`

---

## Migration plan — Phase checklist

- [ ] **Phase 1 — Setup:** Create `new-astro-site/` folder with `package.json` and
      `astro.config.mjs` (output: static). Do not modify any existing files.
- [ ] **Phase 2 — Content migration:** Build Layout, Nav, Footer components and styles.
      Migrate all existing HTML content into Astro pages (nosotros.astro, index.astro).
- [ ] **Phase 3 — New features:** Implement catalog page (CSV-driven), brand values page,
      privacy notice page, active nav tab logic, footer Aviso de Privacidad link.
- [ ] **Phase 4 — Assets:** Copy all images and Font Awesome files into
      `new-astro-site/public/assets/`. Update all src paths in components.
- [x] **Phase 5 — Swap** ✅ **(completed 2026-05-26):**
      Updated `firebase.json` to point to `new-astro-site/dist/`. Deployed to Firebase.
      Live at https://agonia-255fe.web.app. `public/index.html` retained as backup
      (do not delete before 2026-06-02).
      Verified `.firebaserc` still references `agonia-255fe`.

---

## Development rules

### Files that must not be modified

- `public/index.html` — do not touch unless explicitly instructed
- `.firebaserc` — never modify
- `firebase.json` — do not modify until Phase 5, and only after explicit confirmation
- `public/assets/` — do not modify; treat as read-only source for asset copying

### Technical constraints

- **Framework:** Astro only — no React, no Vue, no Svelte
- **CSS:** Plain CSS only — no Tailwind, no CSS-in-JS, no PostCSS plugins
- **No e-commerce:** No shopping cart, no checkout, no payment integration
- **Image references:** All images in the Astro project must be served from `/assets/`
  (i.e., inside `new-astro-site/public/assets/`)
- **Content:** Do not invent text — read only from actual files and data sources
  (index.html for existing copy, productos.csv for catalog data)
- **CSV parsing:** Use `fs.readFileSync` + manual split in Astro frontmatter at build
  time — no external CSV parsing npm packages

### Naming conventions observed in the project

- Image filenames use mixed case and underscores (e.g., `Perrito01_FondoClaro.png`)
- Known typos in existing filenames — copy as-is, do not rename:
  - `Perrito4_blanco_FondoOscuropng.png` (double extension)
  - `lgoo_naranja.png` (missing letter)
  - `gria_01.png` and `narajna_01.png` (spelling errors in Fondos)
