import gdsfactory as gf
import math
from layer_map import LAYER
from components.hex_lattice import HexLattice

@gf.cell
def PhC_2D_hex_lattice(r: float = 0.2,
                       a: float = 1.0,
                       angle_resolution: float = 1.0,
                       n_rows: int = 11,
                       n_holes: int = 5) -> gf.Component:
    
    component = gf.Component()
    hole = gf.components.circle(radius=r,
                                angle_resolution=angle_resolution,
                                layer=LAYER.SHALLOW_DRY_ETCH)
    hex_lattice = HexLattice(a=a, elem=hole)
    component.add_ref(hex_lattice.generate(n_rows=n_rows,
                                           n_holes=n_holes))

    return component

if __name__ == "__main__":
    component = PhC_2D_hex_lattice()
    component.show()