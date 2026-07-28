import sys
from pathlib import Path

from inventory_utils import DEFAULT_CSV_PATH, DEFAULT_XLSX_PATH, normalize_inventory_workbook, update_catalog_availability

xlsx_path = Path(DEFAULT_XLSX_PATH)
prod_path = Path(DEFAULT_CSV_PATH)

print('This workflow now uses inventario_agonia.xlsx as the only source of truth.')
print('Edit the workbook directly when a sale happens; no ventas.csv processing is required.')

# Normalize the workbook and refresh the catalog availability from it.
normalize_inventory_workbook(xlsx_path)
prod_rows, changed_oos = update_catalog_availability(prod_path)

print(
    f'Workbook normalized and catalog refreshed. {len(changed_oos)} availability changes detected.')

if changed_oos:
    print('Availability changes:')
    for modelo, color, talla, old, new in changed_oos:
        print(f'  {modelo:16} | {color:8} | {talla:4} -> {new} (was {old})')

sys.exit(0)
