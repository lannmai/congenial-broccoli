import gdsfactory as gf
from gdsfactory.get_factories import get_cells
from layer_map import LAYER
import electrical, photonic, markers

__version__ = "0.0.1"

__all__ = [
    "LAYER",
    "cells",
    "PDK",
    "__version__",
]

cells = get_cells([electrical, photonic, markers])

PDK = gf.Pdk(name="UDNF",
             layers=LAYER,
             cells=cells)

if __name__ == "__main__":
    pass