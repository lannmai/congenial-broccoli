import gdsfactory as gf
import math
from layer_map import LAYER
from components.PhC_wvg_hex_lattice import PhC_wvg_hex_lattice

@gf.cell
def L3_double(r: float = 0.2,
               a: float = 1.0,
               angle_resolution: float = 1.0,
               n_rows: int = 7,
               n_holes: int = 11) -> gf.Component:
    
    if n_holes < 10:
        raise Exception("Number of holes per row must be at least 10.")

    component = gf.Component()
    w3_wvg = PhC_wvg_hex_lattice(r=r,
                                  a=a,
                                  angle_resolution=angle_resolution,
                                  n_rows=n_rows,
                                  n_holes=n_holes,
                                  width=None,
                                  wvg_type=3)
    component.add_ref(component=w3_wvg)
    hole = gf.components.circle(radius=r, 
                                angle_resolution=angle_resolution, 
                                layer=LAYER.SHALLOW_DRY_ETCH)
    component.add_ref(component=hole, 
                      columns=n_holes, 
                      spacing=(a, 0)).dmove((0, w3_wvg.dy))
    
    for i in range(n_holes-1):
        if int(n_holes/2) <= i <= int(n_holes/2) + 2:
            continue
        component.add_ref(component=hole).dmove((w3_wvg.dxmin + r + (2*i+1)*(a/2), 
                                                 w3_wvg.dy + a*math.sqrt(3)/2))
    for j in range(n_holes-1):
        if int(n_holes/2) - 3 <= j <= int(n_holes/2) - 1:
            continue
        component.add_ref(component=hole).dmove((w3_wvg.dxmin + r + (2*j+1)*(a/2), 
                                                 w3_wvg.dy - a*math.sqrt(3)/2))

    return component