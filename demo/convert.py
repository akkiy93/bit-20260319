"""
Markdown テスト仕様書 → Excel 変換スクリプト
使用方法: uv run python3 convert.py
"""

import re
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import (
    PatternFill, Font, Alignment, Border, Side
)
from openpyxl.utils import get_column_letter

# ── 色設定 ──────────────────────────────────────────
COLOR_TITLE_BG    = "1F4E79"  # タイトル背景（濃紺）
COLOR_TITLE_FG    = "FFFFFF"  # タイトル文字（白）
COLOR_H2_BG       = "2E75B6"  # ## セクション背景（青）
COLOR_H2_FG       = "FFFFFF"
COLOR_H3_BG       = "BDD7EE"  # ### サブセクション背景（薄青）
COLOR_H3_FG       = "1F4E79"
COLOR_HEADER_BG   = "4472C4"  # テーブルヘッダー背景（青）
COLOR_HEADER_FG   = "FFFFFF"
COLOR_ROW_ODD     = "FFFFFF"  # 奇数行
COLOR_ROW_EVEN    = "DEEAF1"  # 偶数行（薄い青）
COLOR_BORDER      = "B8CCE4"

# ── スタイル生成 ─────────────────────────────────────
def make_fill(hex_color):
    return PatternFill("solid", fgColor=hex_color)

def make_border():
    side = Side(style="thin", color=COLOR_BORDER)
    return Border(left=side, right=side, top=side, bottom=side)

def apply_title(cell, text):
    cell.value = text
    cell.fill = make_fill(COLOR_TITLE_BG)
    cell.font = Font(bold=True, size=14, color=COLOR_TITLE_FG)
    cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

def apply_h2(cell, text):
    cell.value = text
    cell.fill = make_fill(COLOR_H2_BG)
    cell.font = Font(bold=True, size=12, color=COLOR_H2_FG)
    cell.alignment = Alignment(horizontal="left", vertical="center")

def apply_h3(cell, text):
    cell.value = text
    cell.fill = make_fill(COLOR_H3_BG)
    cell.font = Font(bold=True, size=11, color=COLOR_H3_FG)
    cell.alignment = Alignment(horizontal="left", vertical="center")

def apply_table_header(cell, text):
    cell.value = text
    cell.fill = make_fill(COLOR_HEADER_BG)
    cell.font = Font(bold=True, color=COLOR_HEADER_FG)
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = make_border()

def apply_table_cell(cell, text, row_index):
    cell.value = text
    color = COLOR_ROW_EVEN if row_index % 2 == 0 else COLOR_ROW_ODD
    cell.fill = make_fill(color)
    cell.font = Font(size=10)
    cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
    cell.border = make_border()

# ── Markdown パース ──────────────────────────────────
def parse_table(lines):
    """Markdown テーブルを [[cell, ...], ...] に変換"""
    rows = []
    for line in lines:
        line = line.strip()
        if not line.startswith("|"):
            break
        if re.match(r"^\|[-| :]+\|$", line):
            continue  # 区切り行をスキップ
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)
    return rows

def parse_markdown(md_text):
    """
    Markdownを構造化データに変換する。
    戻り値: [{"type": "title"|"h2"|"h3"|"table", "content": ...}, ...]
    """
    blocks = []
    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("# ") and not stripped.startswith("## "):
            blocks.append({"type": "title", "content": stripped[2:].strip()})
            i += 1

        elif stripped.startswith("## "):
            blocks.append({"type": "h2", "content": stripped[3:].strip()})
            i += 1

        elif stripped.startswith("### "):
            blocks.append({"type": "h3", "content": stripped[4:].strip()})
            i += 1

        elif stripped.startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            rows = parse_table(table_lines)
            if rows:
                blocks.append({"type": "table", "content": rows})

        else:
            i += 1

    return blocks

# ── Excel 書き込み ────────────────────────────────────
def write_excel(blocks, output_path):
    wb = Workbook()
    ws = wb.active
    ws.title = "テスト仕様書"

    # 列幅追跡（最大文字数）
    col_widths = {}
    current_row = 1

    def merge_and_write(apply_func, text, height=24):
        nonlocal current_row
        ws.row_dimensions[current_row].height = height
        cell = ws.cell(row=current_row, column=1, value=text)
        apply_func(cell, text)
        # A〜L列を結合（最大12列想定）
        ws.merge_cells(
            start_row=current_row, start_column=1,
            end_row=current_row, end_column=12
        )
        current_row += 1

    for block in blocks:
        btype = block["type"]

        if btype == "title":
            merge_and_write(apply_title, block["content"], height=32)
            current_row += 1  # タイトル後に空行

        elif btype == "h2":
            current_row += 1  # セクション前に空行
            merge_and_write(apply_h2, block["content"], height=22)

        elif btype == "h3":
            merge_and_write(apply_h3, block["content"], height=20)

        elif btype == "table":
            rows = block["content"]
            if not rows:
                continue

            header = rows[0]
            data_rows = rows[1:]

            # ヘッダー行
            ws.row_dimensions[current_row].height = 22
            for col_idx, cell_text in enumerate(header, start=1):
                cell = ws.cell(row=current_row, column=col_idx)
                apply_table_header(cell, cell_text)
                # 列幅更新
                col_letter = get_column_letter(col_idx)
                col_widths[col_letter] = max(
                    col_widths.get(col_letter, 0), len(cell_text) + 4
                )
            current_row += 1

            # データ行
            for row_i, row in enumerate(data_rows):
                ws.row_dimensions[current_row].height = 40
                for col_idx, cell_text in enumerate(row, start=1):
                    cell = ws.cell(row=current_row, column=col_idx)
                    apply_table_cell(cell, cell_text, row_i)
                    col_letter = get_column_letter(col_idx)
                    col_widths[col_letter] = max(
                        col_widths.get(col_letter, 0),
                        min(len(cell_text), 50)  # 最大50文字分
                    )
                current_row += 1

        current_row += 0  # 必要なら行間調整

    # ── 列幅の適用（日本語考慮で係数1.8） ──
    for col_letter, width in col_widths.items():
        ws.column_dimensions[col_letter].width = max(width * 1.8, 10)

    # ウィンドウ枠の固定（ヘッダー行を見やすく）
    # ※テーブルが複数あるため固定なし

    # シートの左上に戻る
    ws.freeze_panes = None

    wb.save(output_path)
    print(f"✅ 変換完了: {output_path}")
    print(f"   行数: {current_row - 1} 行")
    print(f"   列数: {len(col_widths)} 列")


# ── メイン ───────────────────────────────────────────
if __name__ == "__main__":
    input_path = Path(__file__).parent / "test_spec.md"
    output_path = Path(__file__).parent / "test_spec.xlsx"

    if not input_path.exists():
        print(f"❌ ファイルが見つかりません: {input_path}")
        exit(1)

    md_text = input_path.read_text(encoding="utf-8")
    blocks = parse_markdown(md_text)
    write_excel(blocks, output_path)
