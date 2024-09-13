import gdsfactory as gf
from layer_map import LAYER

@gf.cell
def strip_waveguide(length: float,
                    width: float) -> gf.Component:

    component = gf.Component()
    component.add_ref(gf.components.rectangle(size=(length, width),
                                              layer=LAYER.SHALLOW_DRY_ETCH,
                                              centered=False))
    component.add_port(name="o1",
                       center=(0, width/2),
                       width=width,
                       port_type="optical",
                       orientation=180,
                       layer=LAYER.SHALLOW_DRY_ETCH)
    component.add_port(name="o2",
                       center=(length, width/2),
                       width=width,
                       port_type="optical",
                       orientation=0,
                       layer=LAYER.SHALLOW_DRY_ETCH)
    
    return component