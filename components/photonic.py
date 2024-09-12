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
                component.add_ref(hole).dmove((j*a, i*a*math.sqrt(3)/2))
            if i%2 == 1 and j <= n_holes-2:
                component.add_ref(hole).dmove(((2*j+1)*(a/2), i*a*math.sqrt(3)/2))

    return component

@gf.cell
def PhC_wvg_hex_lattice(r: float,
                        a: float,
                        angle_resolution: float,
                        n_rows: int,
                        n_holes: int,
                        width: float | None,
                        wvg_type: int | None) -> gf.Component:
    
    if width == None and wvg_type == None:
        raise Exception("Specify waveguide width or type (1 for W1 or 3 for W3)")
    
    component = gf.Component()
    phc = PhC_2D_hex_lattice(r=r, a=a, angle_resolution=angle_resolution, 
                             n_rows=n_rows, n_holes=n_holes)
    top_half = component.add_ref(phc)

    if wvg_type == 1: 
        component.add_ref(phc).dmirror_y(top_half.dy-(a*math.sqrt(3)- 2*r + top_half.dysize)/2)
    elif wvg_type == 3:
        component.add_ref(phc).dmirror_y(top_half.dy - (a*2*math.sqrt(3) - 2*r + top_half.dysize)/2)
    else:
        component.add_ref(phc).dmirror_y(top_half.dy - (width + top_half.dysize)/2)

    return component

@gf.cell
def L3_cavity(r: float,
              a: float,
              angle_resolution: float,
              n_rows: int,
              n_holes: int) -> gf.Component:
    
    """
    L3 cavity is created by adding holes to a W1 PhC waveguides. 
    W1 waveguide composes of 2 PhC hex lattices mirroring about the x-axis.

    n_rows: number of rows of top (or bottom) hex lattice of W1 waveguide. 
    n_holes: number of holes per row. To maintain mirror symmetry about the y-axis, n_holes alternates between n_holes and n_holes-1
    """

    if n_holes < 6:
        raise Exception("Number of holes per row must be at least 6")
    if n_holes%2 == 1:
        raise Exception("Number of holes per row must be even")
    
    component = gf.Component()
    phc_wvg = PhC_wvg_hex_lattice(r=r, 
                                  a=a, 
                                  angle_resolution=angle_resolution, 
                                  n_rows=n_rows,
                                  n_holes=n_holes, 
                                  width=None, 
                                  wvg_type=1)
    component.add_ref(phc_wvg)
    hole = gf.components.circle(radius=r, 
                                angle_resolution=angle_resolution, 
                                layer=LAYER.SHALLOW_DRY_ETCH)
    # max holes = n - 1 for short, inset row
    # leave 3 holes -> n - 4 holes left. Due to mirror sym, we need (n-4)/2 adding steps
    for i in range(int((n_holes-4)/2)):
        component.add_ref(hole).dmove((phc_wvg.dxmax - r - (2*i+1)*(a/2), phc_wvg.dy))
        component.add_ref(hole).dmove((phc_wvg.dxmin + r + (2*i+1)*(a/2), phc_wvg.dy))

    return component 

if __name__ == "__main__":
    component = PhC_2D_hex_lattice()
    component.show()