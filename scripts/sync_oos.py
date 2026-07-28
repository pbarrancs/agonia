"""
sync_oos.py — Normalize the inventory workbook and sync availability to productos.csv.
The workbook is now the source of truth: missing values are replaced with zeros,
Stock is derived as Unidades - Vendidas, and the catalog uses that stock value.
"""
from pathlib import Path

from inventory_utils import DEFAULT_CSV_PATH, DEFAULT_XLSX_PATH, map_inventory_to_catalog, normalize_inventory_workbook, update_catalog_availability

xlsx_path = Path(DEFAULT_XLSX_PATH)
prod_path = Path(DEFAULT_CSV_PATH)

# ─── Normalize workbook and derive stock ────────────────────────────────────
workbook, sheet, rows = normalize_inventory_workbook(xlsx_path)

# flag negative stock rows in the workbook for review
neg_count = 0
for entry in rows:
    if entry['stock'] < 0:
        neg_count += 1

print(
    f'Workbook normalized: {len(rows)} rows, {neg_count} negative-stock rows flagged')

# ─── Update productos.csv based on derived stock ─────────────────────────────
inventory = map_inventory_to_catalog(xlsx_path)
prod_rows, changed = update_catalog_availability(prod_path, inventory)

now_oos = [(m, c, t) for m, c, t, _, new in changed if new == 'false']
now_avail = [(m, c, t) for m, c, t, _, new in changed if new == 'true']

print(
    f'productos.csv updated: {len(now_oos)} newly OOS, {len(now_avail)} newly available')

if now_oos:
    print('\nNow OOS:')
    for m, c, t in sorted(now_oos):
        print(f'  {m:16} | {c:8} | {t}')

if now_avail:
    print('\nNow available (were OOS):')
    for m, c, t in sorted(now_avail):
        print(f'  {m:16} | {c:8} | {t}')

# Summary: total OOS in catalog after update
total_oos = sum(1 for pr in prod_rows if pr['disponible'] == 'false')
total = len(prod_rows)
print(
    f'\nTotal catalog rows: {total} | OOS: {total_oos} | Available: {total - total_oos}')
