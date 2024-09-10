import gdsfactory as gf
from layer_map import LAYER

@gf.cell
def n_electrode(size) -> gf.Component:
    
    component = gf.Component()
    component.add_ref(gf.components.rectangle(size=size, 
                                              layer=LAYER.N_ELECTRODE,
                                              centered=True,
                                              port_type="electrical",
                                              port_orientations=None,
                                              round_corners_east_west=False,
                                              round_corners_north_south=False))

    return component