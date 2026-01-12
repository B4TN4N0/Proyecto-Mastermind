import sys
sys.path.append("..")
sys.path.append("..")
from src.algorithm_parameters import COLORS_ANSI

def colorize_color(color_name, placeholder="[ ]"):
    """Convierte un nombre de color en su representación visual."""
    return COLORS_ANSI.get(color_name, "[ ]")

def colorize_dna(dna_list):
    """Convierte una lista de nombres de colores en bloques visuales."""
    return [colorize_color(color_name, dna_list) for color_name in dna_list]
