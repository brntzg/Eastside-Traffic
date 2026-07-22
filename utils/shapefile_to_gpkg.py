from pathlib import Path
import geopandas as gpd


def shapefile_to_gpkg(
    input_dir: Path | str,
    output_dir: Path | str,
) -> None:
    """
    Create one GeoPackage for each immediate subfolder in input_dir.

    All shapefiles within a subfolder are written as separate layers.
    """
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)

    if not input_dir.is_dir():
        raise NotADirectoryError(
            f"Source shapefile directory does not exist: {input_dir.resolve()}"
        )

    output_dir.mkdir(parents=True, exist_ok=True)

    source_folders = sorted(
        folder for folder in input_dir.iterdir() if folder.is_dir()
    )

    if not source_folders:
        raise FileNotFoundError(
            f"No source folders were found under: {input_dir.resolve()}"
        )

    failures: list[str] = []

    for source_folder in source_folders:
        shapefiles = sorted(source_folder.rglob("*.shp"))

        # Silently skip folders that contain no shapefiles.
        if not shapefiles:
            continue

        output_gpkg = output_dir / f"{source_folder.name}.gpkg"

        # Start with a fresh GeoPackage for this folder.
        if output_gpkg.exists():
            output_gpkg.unlink()

        used_layer_names: set[str] = set()
        layers_written = 0

        for shapefile in shapefiles:
            layer_name = shapefile.stem
            original_name = layer_name
            counter = 2

            # Prevent collisions between identically named shapefiles.
            while layer_name.lower() in used_layer_names:
                layer_name = f"{original_name}_{counter}"
                counter += 1

            used_layer_names.add(layer_name.lower())

            try:
                gdf = gpd.read_file(shapefile)

                gdf.to_file(
                    output_gpkg,
                    layer=layer_name,
                    driver="GPKG",
                    mode="w" if layers_written == 0 else "a",
                    index=False,
                )

                layers_written += 1

            except Exception as error:
                failures.append(
                    f"{shapefile}: {type(error).__name__}: {error}"
                )

        # Remove an empty or partially created file when no layers succeeded.
        if layers_written == 0 and output_gpkg.exists():
            output_gpkg.unlink()

    # Produce output only when processing failures occurred.
    if failures:
        failure_details = "\n".join(f" - {failure}" for failure in failures)
        raise RuntimeError(
            f"Some shapefiles could not be converted:\n{failure_details}"
        )


if __name__ == "__main__":
    shapefile_to_gpkg(
        input_dir=Path(r"Data\SourceShapefiles"),
        output_dir=Path(r"Data\Geopackages"),
    )