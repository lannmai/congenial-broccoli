import gdsfactory as gf
from layer_map import LAYER 

@gf.cell
def parabolic_taper(length: float,
                    width1: float,
                    width2: float) -> gf.Component:
    
    component = gf.Component()

    component.add_ref(gf.components.taper_parabolic(length=length,
                                                    width1=width1,
                                                    width2=width2,
                                                    npoints=200,
                                                    layer=LAYER.SHALLOW_DRY_ETCH))
    component.add_port(name="o1",
                       center=(0, 0),
                       width=width1,
                       port_type="optical",
                       orientation=180,
                       layer=LAYER.SHALLOW_DRY_ETCH)
    component.add_port(name="o2",
                       center=(length, 0),
                       width=width2,
                       port_type="optical",
                       orientation=0,
                       layer=LAYER.SHALLOW_DRY_ETCH)
    
    return component