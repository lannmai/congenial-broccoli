import gdsfactory as gf
from layer_map import LayerMapUDNF

LAYER = LayerMapUDNF()

@gf.cell
def UDNF_10mm_laser_markers() -> gf.Component:
    return 

@gf.cell
def UDNF_10mm_PAM_arrays() ->gf.Component:
    return

@gf.cell
def UDNF_10mm_EBL_squares_20um() -> gf.Component:
    return

@gf.cell
def UDNF_10mm_EBL_markers() -> gf.Component:
    return

@gf.cell
def UDNF_10mm_die(sample_id: str,
                  EBL_markers: bool = True,
                  laser_markers: bool = True) -> gf.Component:
    
    component = gf.Component()
    component.add_ref(gf.components.die(size=(10000.0, 10000.0),
                                        street_width = 0,
                                        street_length = 0,
                                        die_name = sample_id,
                                        text_size = 100.0,
                                        text_location = 'N',
                                        layer = LAYER.FLOORPLAN))
    
    if EBL_markers == True:
        component.add_ref(UDNF_10mm_EBL_markers)
    if laser_markers == True:
        component.add_ref(UDNF_10mm_laser_markers)

    return component

@gf.cell
def label() -> gf.Component:
    return