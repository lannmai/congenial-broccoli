import gdsfactory as gf
from layer_map import LAYER

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

    return component

if __name__ == "__main__":
    c = UDNF_10mm_die(sample_id="die_1")
    c.show()