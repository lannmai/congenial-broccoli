from gdsfactory.typings import Layer
from gdsfactory.technology.layer_map import LayerMap, LayerViews

class LayerMapUDNF(LayerMap):
    """ 
    Inspired by “Silicon Photonics Design: From Devices to Systems Lukas Chrostowski, Michael Hochberg” and 
    University of Delaware Nanofabrication Facility's markers template.

    PAM_ARRAYS: EBL pre-alignment marker arrays.
    GAAS_P: p-doped GaAs.
    GAAS_N: n-doped GaAs.
    GAAS_I: instrinsic GaAs.
    ALGAAS: AlGaAs sacrificial layer.
    ID_COUPLER: inverse design coupler-waveguide.
    GRAT_CPL: grating coupler.
    MEEP: FDTD simulation in Meep.
    """
    
    FLOORPLAN: Layer = (100, 0) 
    CORNERS: Layer = (101, 0)
    PAM_ARRAYS: Layer = (105, 0) 
    SQUARES_20UM: Layer = (106, 0)
    PAM_LABELS: Layer = (107, 0)
    LASER_CROSSES: Layer = (108, 0)
    
    GAAS_P: Layer = (0, 3)
    GAAS_N: Layer = (1, 3)
    GAAS_I: Layer = (2, 3)
    ALGAAS: Layer = (13, 3)

    P_ELECTRODE: Layer = (60, 0)
    N_ELECTRODE: Layer = (61, 0)
    
    TEXT: Layer = (199, 0)
    
    ID_COUPLER_BIG: Layer = (0, 0)
    ID_COUPLER_SMALL = (1, 0)
    GRAT_CPL: Layer = (10, 0)
    UNDERCUT: Layer = (5, 0)
    SHALLOW_ETCH: Layer = (51, 0)
    DEEP_ETCH: Layer = (52, 0)

    FDTD_DOMAIN: Layer = (30, 1)
    