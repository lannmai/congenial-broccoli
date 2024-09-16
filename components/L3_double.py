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
    if n_rows%2 == 0:
        raise Exception("Number of rows must be odd.")

    component = gf.Component()
    hole = gf.components.circle(radius=r, 
                                angle_resolution=angle_resolution, 
                                layer=LAYER.SHALLOW_DRY_ETCH)
    
    for i in range(n_rows):
        if i == (n_rows-1)/2+1: # create first L3 cavity
            for j in range(n_holes):
                if int(n_holes/2) <= j <= int(n_holes/2) + 2:
                    continue
                component.add_ref(component=hole).dmove((j*a, 
                                                         i*a*math.sqrt(3)/2))
        elif i == (n_rows-1)/2-1: # create second L3 cavity
            for j in range(n_holes):
                if int(n_holes/2)-3 <= j <= int(n_holes/2)-1:
                    continue
                component.add_ref(component=hole).dmove((j*a, 
                                                         i*a*math.sqrt(3)/2))
        else: # create PhC around 2xL3 cavities
            for j in range(n_holes):
                if i%2 == 0:
                    component.add_ref(component=hole).dmove((j*a, 
                                                             i*a*math.sqrt(3)/2))
                if i%2 == 1 and j < n_holes-1:
                    component.add_ref(component=hole).dmove(((2*j+1)*(a/2), 
                                                              i*a*math.sqrt(3)/2))
    
    return component