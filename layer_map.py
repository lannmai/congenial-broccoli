from gdsfactory.typings import Layer
from gdsfactory.technology.layer_map import LayerMap, LayerViews

class LayerMapUDNF(LayerMap):

    FLOORPLAN = (100, 0) 
    CORNERS = (101, 0)
    PAM_ARRAYS = (105, 0) 
    SQUARES_20UM = (106, 0)
    PAM_LABELS= (107, 0)
    LASER_CROSSES = (108, 0)

    P_ELECTRODE = (60, 0)
    N_ELECTRODE = (61, 0)
    WET_ETCH_PIT = (70, 0)
    
    TEXT: Layer = (199, 0)
    
    ID_COUPLER_BIG = (0, 0)
    ID_COUPLER_SMALL = (1, 0)
    WG = (2, 0)
    GRATING_COUPLER = (10, 0)
    SHALLOW_DRY_ETCH = (11, 0)
    DEEP_DRY_ETCH = (99, 0)

    FDTD = (30, 1)
    CNST = (255, 255)

LAYER = LayerMapUDNF