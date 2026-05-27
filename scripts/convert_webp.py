#!/usr/bin/env python3
"""
scripts/convert_webp.py
Image optimisation for agonia catalog.

For every PNG in new-astro-site/public/assets/images/playeras/:
  1. Copy original to playeras_original/  (backup — not deleted until confirmed)
  2. Resize to 800×483, save as WebP Q80  → replaces the PNG in playeras/
  3. Resize to 1200×724, save as WebP Q85 → playeras_preview/<stem>_preview.webp

Then updates the imagen column in productos.csv (.png → .webp).
"""
import re
import shutil
from pathlib import Path

from PIL import Image

BASE = Path(__file__).resolve().parent.parent / \
    "new-astro-site" / "public" / "assets" / "images"
SRC = BASE / "playeras"
BACKUP = BASE / "playeras_original"
PREVIEW = BASE / "playeras_preview"
CSV = Path(__file__).resolve().parent.parent / \
    "new-astro-site" / "src" / "data" / "productos.csv"

THUMB_SIZE = (800, 483)
PREVIEW_SIZE = (1200, 724)


def main() -> None:
    BACKUP.mkdir(exist_ok=True)
    PREVIEW.mkdir(exist_ok=True)

    pngs = sorted(SRC.glob("*.png"))
    if not pngs:
        print("No PNG files found — nothing to do.")
        return

    print(f"Processing {len(pngs)} PNG files…\n")
    print(
        f"  {'File':<32}  {'Before':>8}  {'Thumb':>7}  {'Preview':>8}  {'Saved':>6}")
    print(f"  {'─'*32}  {'─'*8}  {'─'*7}  {'─'*8}  {'─'*6}")

    rows = []
    for src_path in pngs:
        stem = src_path.stem
        orig_kb = src_path.stat().st_size / 1024

        # ── Backup ──────────────────────────────────────────────────────────
        shutil.copy2(src_path, BACKUP / src_path.name)

        # ── Open ─────────────────────────────────────────────────────────────
        with Image.open(src_path) as img:
            rgb = img.convert("RGB")

            # Thumbnail 800×483, Q80
            thumb_path = SRC / f"{stem}.webp"
            rgb.resize(THUMB_SIZE, Image.LANCZOS).save(
                thumb_path, "WEBP", quality=80, method=6
            )
            thumb_kb = thumb_path.stat().st_size / 1024

            # Preview 1200×724, Q85
            prev_path = PREVIEW / f"{stem}_preview.webp"
            rgb.resize(PREVIEW_SIZE, Image.LANCZOS).save(
                prev_path, "WEBP", quality=85, method=6
            )
            prev_kb = prev_path.stat().st_size / 1024

        # ── Remove original PNG ───────────────────────────────────────────────
        src_path.unlink()

        pct = (1 - thumb_kb / orig_kb) * 100
        rows.append((stem, orig_kb, thumb_kb, prev_kb, pct))
        print(
            f"  {stem:<32}  {orig_kb:>7.0f}K  {thumb_kb:>6.0f}K  {prev_kb:>7.0f}K  {pct:>5.0f}%")

    # ── Update productos.csv ───────────────────────────────────────────────────
    text = CSV.read_text(encoding="utf-8")
    updated = re.sub(
        r"(/assets/images/playeras/[^,\r\n]+)\.png",
        r"\1.webp",
        text,
    )
    CSV.write_text(updated, encoding="utf-8")
    print(f"\n  ✔  productos.csv — imagen column updated (.png → .webp)")

    # ── Summary ────────────────────────────────────────────────────────────────
    total_orig = sum(r[1] for r in rows)
    total_thumb = sum(r[2] for r in rows)
    total_prev = sum(r[3] for r in rows)
    print(f"\n  {'─'*55}")
    print(f"  Files processed  : {len(rows)}")
    print(
        f"  Before (total)   : {total_orig:>8,.0f} KB  ({total_orig/1024:.1f} MB)")
    print(
        f"  Thumbnails total : {total_thumb:>8,.0f} KB  ({total_thumb/1024:.1f} MB)")
    print(
        f"  Previews total   : {total_prev:>8,.0f} KB  ({total_prev/1024:.1f} MB)")
    print(f"  Thumbnail saving : {(1 - total_thumb/total_orig)*100:.0f}%")
    print(f"\n  Originals backed up → playeras_original/")
    print(f"  Previews created  → playeras_preview/")


if __name__ == "__main__":
    main()
