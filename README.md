# agonia — Website

Brand presence website for **agonia**, an independent climbing apparel collective based in Mexico. The site communicates the brand's identity, values, and mission to the climbing and outdoor community.

> No e-commerce. No framework. Just a fast, static page deployed to Firebase Hosting.

---

## Tech Stack

| Tool                  | Role                                                                              |
| --------------------- | --------------------------------------------------------------------------------- |
| **HTML5**             | Single-page markup (`index.html`)                                                 |
| **CSS / Sass (SCSS)** | Styling. Source lives in `assets/sass/`; compiled output is `assets/css/main.css` |
| **Google Fonts**      | Brand typography — New Rocker (titles), Nova Cut (subtitles), Syne Mono (body)    |
| **Font Awesome 5**    | Social icons (bundled locally in `assets/webfonts/`)                              |
| **jQuery + Poptrox**  | DOM utilities and lightbox, inherited from the HTML5UP Strata base template       |
| **Firebase Hosting**  | Static site deployment and CDN                                                    |

The site is built on the [Strata](https://html5up.net/strata) template by HTML5UP, licensed under [CCA 3.0](https://html5up.net/license).

---

## Prerequisites

- **Firebase CLI** — required only to deploy:
  ```bash
  npm install -g firebase-tools
  ```
- A **Sass compiler** — required only if you edit `.scss` files:
  ```bash
  npm install -g sass
  ```
- No other build tools, bundlers, or runtimes are needed.

---

## Local Development

The site is a static HTML file. No build step is required to preview it.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/pbarrancs/agonia.git
   cd agonia
   ```

2. **Open the site:**
   Open `public/index.html` directly in a browser, or use any static file server:

   ```bash
   npx serve public
   ```

   Then visit `http://localhost:3000`.

3. **Edit styles (optional):**
   If you modify any `.scss` file under `public/assets/sass/`, recompile to `main.css`:

   ```bash
   sass public/assets/sass/main.scss public/assets/css/main.css
   ```

   For watch mode:

   ```bash
   sass --watch public/assets/sass/main.scss:public/assets/css/main.css
   ```

---

## Deploy to Firebase

The site deploys to **Firebase Hosting** under project `agonia-255fe`.

1. **Log in to Firebase:**

   ```bash
   firebase login
   ```

2. **Deploy:**

   ```bash
   firebase deploy
   ```

   Firebase will upload everything inside `public/` (excluding dotfiles and `node_modules`).

3. **Live URL:**
   `https://agonia-255fe.web.app`

The hosting configuration is in `firebase.json`. The project alias is defined in `.firebaserc`.

---

## Project Structure (web files only)

```
agonia/
├── firebase.json          # Firebase Hosting config — serves from public/
├── .firebaserc            # Firebase project alias (agonia-255fe)
├── .gitignore
└── public/                # Everything deployed to Firebase
    ├── index.html         # Main (and only) page
    ├── a_icono.ico        # Browser favicon
    ├── assets/
    │   ├── css/
    │   │   ├── main.css               # Compiled stylesheet (do not edit directly)
    │   │   └── fontawesome-all.min.css
    │   ├── sass/
    │   │   ├── main.scss              # Sass entry point — edit this for styles
    │   │   └── libs/                  # Sass partials (vars, mixins, breakpoints…)
    │   ├── js/
    │   │   ├── main.js                # Site JS (parallax, touch handling)
    │   │   ├── jquery.min.js
    │   │   ├── jquery.poptrox.min.js  # Lightbox
    │   │   ├── browser.min.js
    │   │   ├── breakpoints.min.js
    │   │   └── util.js
    │   └── webfonts/                  # Font Awesome font files
    └── images/
        ├── Logos/                     # Brand logo variants
        ├── Ilustraciones/             # Character illustrations (Perrito 01–08, Personaje A)
        ├── Fondos/                    # Background images
        └── bg.jpg                     # Page background
```

---

## Configuration

There are no environment variables. Firebase project configuration is entirely handled by two files:

- **`firebase.json`** — declares `public/` as the hosting root and sets ignore rules.
- **`.firebaserc`** — maps the `default` alias to the `agonia-255fe` Firebase project.

To deploy to a different Firebase project, update `.firebaserc` or run:

```bash
firebase use <your-project-id>
```

---

## Links

| **Resource** | **URL**                              |
| ------------ | ------------------------------------ |
| Website      | https://agonia-255fe.web.app         |
| Instagram    | https://www.instagram.com/___agonia/ |
| YouTube      | https://www.youtube.com/@agon_ia     |
