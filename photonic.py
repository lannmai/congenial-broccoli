import gdsfactory as gf
import math
from layer_map import LayerMapUDNF

LAYER = LayerMapUDNF()

@gf.cell
def PhC_2D_hex_lattice(r: float,
                       a: float,
                       angle_resolution: float,
                       n_holes: int,
                       n_rows: int,
                       w: float) -> gf.Component:
    
    '''
    Adopted from Tidy3D's script
    Creates a PhC waveguide structure based on the parameters:
    r = photonic crystal radius,
    a = lattice constant,
    angle_resolution = circle's angle resolution,
    n_holes = the number of PhC holes in each row,
    n_rows = number of PhC rows in each mirror,
    w = photonic crystal waveguide width.
    '''
    component = gf.Component()
    hole = gf.components.circle(radius=r,
                                angle_resolution=angle_resolution,
                                layer=LAYER.SHALLOW_ETCH)

    for i in range(n_rows):
        if i % 2 == 0:
            shift = a / 2
            N = n_holes
        else:
            shift = 0
            N = n_holes + 1
        for j in range(N):
            # Add a hole at a position based on the i, j values. 
            component.add_ref(hole).dmovex((j - (n_holes) / 2) * a + shift, 
                                           (w / 2 + r) + i * math.sqrt(3) * a / 2)
    
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

@gf.cell
def ring_single_bus(gap: float, 
                    r: float, 
                    width: float,
                    angle: float,
                    bus_length) -> gf.Component:
    
    component = gf.Component()
    component.add_ref(gf.components.ring(radius=r, 
                                         width=width,
                                         angle_resolution=1.0,
                                         layer=LAYER.WG,
                                         angle=angle))
    component.add_ref(gf.components.straight(length=bus_length))
    

    
