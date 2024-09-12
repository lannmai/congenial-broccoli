import gdsfactory as gf
from layer_map import LAYER

@gf.cell
def p_electrode(size: tuple[float, float] = (5.0, 5.0)) -> gf.Component:

    component = gf.Component()
    component.add_ref(gf.components.rectangle(size=size, 
                                              layer=LAYER.P_ELECTRODE,
                                              centered=True,
                                              port_type="electrical",
                                              port_orientations=None))
    
    return component

if __name__ == "__main__":
    component = p_electrode()
    component.show()