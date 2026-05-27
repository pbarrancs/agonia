import re
import pathlib

csv_path = pathlib.Path(
    r"c:\Users\pablo\OneDrive\Documentos\Docs\agonia\new-astro-site\src\data\productos.csv")
src_img = pathlib.Path(
    r"c:\Users\pablo\OneDrive\Documentos\Docs\agonia\Documentos\playeras\playeras_images\web\Con fondo_inventario")

text = csv_path.read_text(encoding="utf-8")

replacements = [
    # image path: lisa_ → solido_
    ("playeras/lisa_",           "playeras/solido_"),
    # typo fix
    ("deslavada_girs_1.png",     "deslavada_gris_1.png"),
    # product names
    ("Playera Lisa - Diseño",    "Playera Sólida - Diseño"),
    # model codes  (comma-bounded so we don't accidentally hit longer strings)
    (",lisa_1,",                 ",solido_1,"),
    (",lisa_2,",                 ",solido_2,"),
]

for old, new in replacements:
    count = text.count(old)
    text = text.replace(old, new)
    print(f"  {old!r:45s} → {new!r}  ({count} replacements)")

csv_path.write_text(text, encoding="utf-8")
print(f"\nCSV written: {csv_path}")

# Verify: list all unique imagen values
lines = text.strip().split("\n")
headers = lines[0].split(",")
img_idx = headers.index("imagen")
images = sorted({l.split(",")[img_idx] for l in lines[1:]})
print("\nUnique imagen values in CSV:")
for img in images:
    # check if the file actually exists (strip leading slash for path check)
    fname = img.split("/")[-1]
    # playeras folder
    dest = pathlib.Path(
        r"c:\Users\pablo\OneDrive\Documentos\Docs\agonia\new-astro-site\public\assets\images\playeras") / fname
    exists = "✓" if dest.exists() else "✗ MISSING"
    print(f"  {exists}  {img}")
