import sys
import gdsfactory as gf

from components.UDNF_10mm_die import UDNF_10mm_die

from components.PhC_2D_hex_lattice import PhC_2D_hex_lattice
from components.PhC_wvg_hex_lattice import PhC_wvg_hex_lattice
from components.L3_cavity import L3_cavity
from components.parabolic_taper import parabolic_taper
from components.strip_waveguide import strip_waveguide

from components.p_electrode import p_electrode
from components.n_electrode import n_electrode
from components.hex_lattice import HexLattice

# from gdsfactory.components __init__.py
cells = gf.get_cells(sys.modules[__name__])