import gdsfactory as gf
from layer_map import LAYER

@gf.cell
def deep_etch_pit(size: tuple) -> gf.Component: 

    component = gf.Component()
    component.add_ref(gf.components.rectangle(size=size, 
                                              layer=LAYER.DEEP_ETCH,
                                              centered=True,
                                              port_type="electrical",
                                              port_orientations=None,
                                              round_corners_east_west=False,
                                              round_corners_north_south=False))
    
    return component

@gf.cell
def shallow_etch_pit(size: tuple) -> gf.Component:

    component = gf.Component()
    component.add_ref(gf.components.rectangle(size=size, 
                                              layer=LAYER.SHALLOW_ETCH,
                                              centered=True,
                                              port_type="electrical",
                                              port_orientations=None,
                                              round_corners_east_west=False,
                                              round_corners_north_south=False))
    
    return component

@gf.cell
def p_electrode(size: tuple) -> gf.Component:

    component = gf.Component()
    component.add_ref(gf.components.rectangle(size=size, 
                                              layer=LAYER.P_ELECTRODE,
                                              centered=True,
                                              port_type="electrical",
                                              port_orientations=None,
                                              round_corners_east_west=False,
                                              round_corners_north_south=False))
    
    return component

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