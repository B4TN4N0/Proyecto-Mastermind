# Parámetros del Mastermind
COLOR_GENES = ['Red', 'Green', 'Blue', 'Purple', 'Yellow', 'White', 'Pink', 'Orange']
GENOME_LENGTH = 4

# Códigos para colorear el fondo (más parecido a una ficha de Mastermind)
COLORS_ANSI = {
    'Red': '\033[41m  \033[0m',
    'Green': '\033[42m  \033[0m',
    'Blue': '\033[44m  \033[0m',
    'Purple': '\033[45m  \033[0m',
    'Yellow': '\033[43m  \033[0m',
    'White': '\033[47m  \033[0m',
    'Pink': '\033[105m  \033[0m',
    'Orange': '\033[48;5;208m  \033[0m',
}

def colorize_dna(dna_list):
    """Convierte una lista de nombres de colores en bloques visuales."""
    return " ".join([COLORS_ANSI.get(color, "[?]") for color in dna_list])

# Parámetros del Algoritmo Genético
POPULATION_SIZE = 100
MUTATION_RATE = 0.05
