import sys

def remove_indent(s: str):
    assert "\t" not in s, "we don't support tabs"
    MAX_INDENT = 40
    i = 0
    while i < len(s) and s[i] == " " and i < MAX_INDENT:
        i += 1
    return i, s[i:]

def chunk(s: str, n: int):
    return (s[i:i+n] for i in range(0, max(1, len(s)), n))

COLS = 80
def fmt_line(line: str):
    indent, line = remove_indent(line.rstrip("\n"))
    width = COLS - indent
    indent = " " * indent
    return ((indent + ch).ljust(COLS) for ch in chunk(line, width))

BLACK, WHITE = "10"
BLANK_LINE = BLACK * COLS
PADDING = 10 * BLACK

def make_bitmap(lines: list[str]):
    ROWS = 200
    lines = [l for line in lines for l in fmt_line(line)]
    pages: list[str] = list(chunk(lines, ROWS))
    img_height = max(map(len, pages))
    img_width = max(0, len(pages) * (COLS + len(PADDING)) - len(PADDING))
    img: list[str] = []
    for row in range(img_height):
        img_row = []
        for page in pages:
            if img_row: img_row.append(PADDING)
            if row < len(page):
                img_row.extend(BLACK if c == " " else WHITE for c in page[row])
            else:
                img_row.append(BLANK_LINE)
        img_row = "".join(img_row)
        assert len(img_row) == img_width
        img.append(img_row)
    return "P1\n{} {}\n{}".format(img_width, img_height, "\n".join(img))

def main():
    print(make_bitmap(list(sys.stdin)))

if __name__ == "__main__":
    main()
