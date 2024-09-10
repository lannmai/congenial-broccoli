import gdsfactory as gf
import math
from layer_map import LAYER

@gf.cell
def PhC_2D_hex_lattice(r: float = 0.5,
                       a: float = 1.0,
                       angle_resolution: float = 1.0,
                       n_cols: int = 10,
                       n_rows: int = 5) -> gf.Component:
    
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

if __name__ == "__main__":
    c = PhC_2D_hex_lattice()
    c.show()