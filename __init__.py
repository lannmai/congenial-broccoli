import gdsfactory as gf
from gdsfactory.get_factories import get_cells
import components.n_electrode
import components.p_electrode
from layer_map import LAYER
import components

__version__ = "0.0.1"

__all__ = [
    "LAYER",
    "cells",
    "PDK",
    "__version__",
]

cells = get_cells([components.PhC_2D_hex_lattice, 
                   components.n_electrode,
                   components.p_electrode])

PDK = gf.Pdk(name="udnf35photonic",
             layers=LAYER,
             cells=cells)

if __name__ == "__main__":
    pass