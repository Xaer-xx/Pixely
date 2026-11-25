from pathlib import Path

from PIL import Image

PRIEČINOK = Path(__file__).resolve().parent
PRIPONY = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp", ".tif", ".tiff"}
PRAH = 128 
def najdi_fotky():
    return sorted(
        p for p in PRIEČINOK.iterdir()
        if p.is_file() and p.suffix.lower() in PRIPONY
    )

def spocitaj_pixely(cesta):
    with Image.open(cesta) as obrazok:
        sedy = obrazok.convert("L")
        histogram = sedy.histogram()
    tmave = sum(histogram[:PRAH])
    svetle = sum(histogram[PRAH:])
    return tmave, svetle

def main():
    fotky = najdi_fotky()
    if not fotky:
        print(f"V priečinku {PRIEČINOK} som nenašiel žiadnu fotku.")
        print("Vlož sem fotky (jpg, png, bmp, gif, webp, tiff) a spusti program znova.")
        return

    for fotka in fotky:
        print(f"Fotka: {fotka.name}")
        try:
            tmave, svetle = spocitaj_pixely(fotka)
        except OSError as chyba:
            print(f"  Nepodarilo sa otvoriť fotku: {chyba}\n")
            continue
        spolu = tmave + svetle

        print(f"  Spolu pixelov: {spolu}")
        print(f"  Tmavé pixely:  {tmave} ({tmave / spolu * 100:.2f} %)")
        print(f"  Svetlé pixely: {svetle} ({svetle / spolu * 100:.2f} %)\n")


if __name__ == "__main__":
    main()
