from pathlib import Path
from affine import Affine

def read_world_file(world_file_path: Path | str) -> Affine:
    """
    Read a world file as an Affine transform for file extensions: .pgw, .pgwx, .jgw, .jgwx, .tfw, .tfwx, .wld.
    """

    path = Path(world_file_path)

    values = [float(value) for value in path.read_text().split()]

    # Raise a Value Error if the file doe not contain six values:
    if len(values) != 6:
        raise ValueError(
            f"{path.name} contains {len(values)} values; 6 expected."
        )

    # World-file order:
        # A: pixel width (x-scale), 
        # D: row rotation (y-skew),
        # B: column rotation (x-skew),
        # E: pixel height (y-scale),
        # C: upper-left pixel-center X,
        # F: upper-left pixel-center Y
    A, D, B, E, C, F = values

    # World files reference the center of the upper-left pixel.
    # Rasterio/Affine transforms uses the outer upper-left corner.
    return Affine(
        A,
        B,
        C - (A + B) / 2,
        D,
        E,
        F - (D + E) / 2,
    )