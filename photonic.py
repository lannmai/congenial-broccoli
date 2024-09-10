import gdsfactory as gf
import math
from layer_map import LAYER

@gf.cell
def PhC_2D_hex_lattice(r: float,
                       a: float,
                       angle_resolution: float,
                       n_cols: int,
                       n_rows: int) -> gf.Component:
    
    component = gf.Component()
    hole = gf.components.circle(radius=r,
                                angle_resolution=angle_resolution,
                                layer=LAYER.SHALLOW_DRY_ETCH)
    hole_arr = gf.components.array(component=hole, 
                                   spacing=(a, 0),
                                   columns=n_cols,
                                   rows=1,
                                   add_ports=False)
    for i in range(n_rows):
        if i%2 == 0:
            component.add_ref(hole_arr).dmove((0, i*a*math.sqrt(3)/2))
        if i%2 == 1:
            component.add_ref(hole_arr).dmove((a/2, i*a*math.sqrt(3)/2))

    return component

@gf.cell
def inverse_design_coupler_wvg() -> gf.Component:
    return

@gf.cell
def grating_coupler() -> gf.Component:
    return

@gf.cell
def PhC_wvg() -> gf.Component:
    return   