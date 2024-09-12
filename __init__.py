import gdsfactory as gf
from layer_map import LAYER
from components import cells

def get_pdk() -> gf.Pdk:
    return gf.Pdk(name="udnf35photonicPDK",
                  layers=LAYER,
                  cells=cells)