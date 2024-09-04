from gdsfactory.typings import Layer
from gdsfactory.technology.layer_map import LayerMap, LayerViews

class LayerMapUDNF(LayerMap):

    FLOORPLAN: Layer = (100, 0) 
    CORNERS: Layer = (101, 0)
    PAM_ARRAYS: Layer = (105, 0) 
    SQUARES_20UM: Layer = (106, 0)
    PAM_LABELS: Layer = (107, 0)
    LASER_CROSSES: Layer = (108, 0)

    P_ELECTRODE: Layer = (60, 0)
    N_ELECTRODE: Layer = (61, 0)
    
    TEXT: Layer = (199, 0)
    
    ID_COUPLER_BIG: Layer = (0, 0)
    ID_COUPLER_SMALL: Layer = (1, 0)
    WG: Layer = (2, 0)
    GRATING_COUPLER: Layer = (10, 0)
    SHALLOW_ETCH: Layer = (11, 0)
    DEEP_ETCH: Layer = (99, 0)

    FDTD: Layer = (30, 1)
    CNST: Layer = (255, 255)

LAYER = LayerMapUDNF