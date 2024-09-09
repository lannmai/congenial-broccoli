import gdsfactory as gf
import math
from layer_map import LAYER
import cnst

CNST_JAR_PATH = 'CNSTNanolithographyToolboxV2016.10.01.jar'
JAVA_FX_SDK_PATH = '~/javafx-sdk-22.0-2.2/lib'

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
                                layer=LAYER.SHALLOW_DRY_ETCH)

    for i in range(n_rows):
        if i % 2 == 0:
            shift = a / 2
            N = n_holes
        else:
            shift = 0
            N = n_holes + 1
        for j in range(N):
            # Add a hole at a position based on the i, j values. 
            (component.add_ref(hole)).dmovex((j - (n_holes) / 2) * a + shift, 
                                              (w / 2 + r) + i * math.sqrt(3) * a / 2)
    
    return component

@gf.cell
def inverse_design_coupler_wvg() -> gf.Component:
    return

@gf.cell
def grating_coupler() -> gf.Component:
    return

@gf.cell
def W1_PhC_wvg() -> gf.Component:
    cnstpath = 'cnst_scripts/W1_PhC_wvg.cnst'
    component = cnst.cnst_to_gf(cnstpath, CNST_JAR_PATH, JAVA_FX_SDK_PATH, 'W1_PhC_wvg.gds')
    
    component.flatten()

    component.add_port(name='o1', 
                       center=(component.dxmin, (component.dymax+component.dymin)/2),
                       orientation=180,
                       port_type='optical',
                       layer = LAYER.SHALLOW_DRY_ETCH,
                       width=0.38)
    
    component.add_port(name='o2', 
                       center=(component.dxmax, (component.dymax+component.dymin)/2),
                       orientation=0,
                       port_type='optical',
                       layer = LAYER.SHALLOW_DRY_ETCH,
                       width=0.38)
    
    return component

@gf.cell
def ring_single_bus(gap: float, 
                    r: float, 
                    width: float,
                    angle: float,
                    bus_length) -> gf.Component:
    
    component = gf.Component()
    
if __name__ == "__main__":
    print("photonic.py has been invoked")