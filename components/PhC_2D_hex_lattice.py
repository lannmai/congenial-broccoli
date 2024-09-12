import gdsfactory as gf
import math
from layer_map import LAYER

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
    
    for i in range(n_rows):
        for j in range(n_holes):
            if i%2 == 0:
                component.add_ref(component=hole).dmove((j*a, 
                                                         i*a*math.sqrt(3)/2))
            if i%2 == 1 and j <= n_holes-2:
                component.add_ref(component=hole).dmove(((2*j+1)*(a/2), 
                                                         i*a*math.sqrt(3)/2))

    return component

if __name__ == "__main__":
    component = PhC_2D_hex_lattice()
    component.show()