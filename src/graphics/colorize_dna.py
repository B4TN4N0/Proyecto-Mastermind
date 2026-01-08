import sys
sys.path.append("..")
sys.path.append("..")
from src.algorithm_parameters import COLORS_ANSI

def colorize_dna(dna_list):
    """Convierte una lista de nombres de colores en bloques visuales."""
    return [COLORS_ANSI.get(color, "[?]") for color in dna_list]
