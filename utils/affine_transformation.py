from pathlib import Path
from affine import Affine

def read_pgwx(pgwx_path: Path) -> Affine:
    values = [float(value) for value in pgwx_path.read_text().split()]

    if len(values) != 6:
        raise ValueError(
            f"{pgwx_path.name} contains {len(values)} values; expected 6."
        )

    # World-file order
    A, D, B, E, C, F = values

    # World files reference the centre of the upper-left pixel.
    # Rasterio uses the outer upper-left corner.
    return Affine(
        A,
        B,
        C - (A + B) / 2,
        D,
        E,
        F - (D + E) / 2,
    )