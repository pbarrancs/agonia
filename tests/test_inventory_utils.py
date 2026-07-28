import tempfile
from pathlib import Path

import openpyxl

from scripts.inventory_utils import normalize_inventory_workbook


def test_normalize_inventory_fills_missing_values_and_computes_stock():
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Inventario'
    sheet.append(['Tipo', 'Color', 'Diseño', 'Talla', 'Unidades', 'Vendidas'])
    sheet.append(['Solido', 'Blanco', 1, 'S', 2, None])
    sheet.append(['Solido', 'Negro', 2, 'M', None, 1])
    sheet.append(['Deslavada', 'Gris', 3, 'L', 4, 5])

    temp_dir = Path(tempfile.mkdtemp())
    xlsx_path = temp_dir / 'inventario_test.xlsx'
    workbook.save(xlsx_path)

    _, _, rows = normalize_inventory_workbook(xlsx_path)

    assert rows[0]['unidades'] == 2
    assert rows[0]['vendidas'] == 0
    assert rows[0]['stock'] == 2

    assert rows[1]['unidades'] == 0
    assert rows[1]['vendidas'] == 1
    assert rows[1]['stock'] == -1

    assert rows[2]['stock'] == -1
