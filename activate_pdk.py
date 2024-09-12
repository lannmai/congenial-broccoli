import gdsfactory as gf
from gdsfactory.get_factories import get_cells
from layer_map import LAYER
import components

__version__ = "0.0.1"

__all__ = [
    "LAYER",
    "cells",
    "pdk",
    "__version__",
]

cells = get_cells(modules=components, verbose=True)

pdk = gf.Pdk(name="udnf35photonic",
             layers=LAYER,
             cells=cells)

pdk.activate()
