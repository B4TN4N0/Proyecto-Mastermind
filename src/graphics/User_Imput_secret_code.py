import sys
sys.path.append("..")
sys.path.append("..")
from src.algorithm_parameters import COLOR_GENES, GENOME_LENGTH, COLORS_ANSI
from src.graphics.colorize_dna import colorize_color
def display_color_menu():
    print("\n" + "="*43)
    print("      BIENVENIDO AL JUEGO MASTERMIND")
    print("="*43)
    print("Menú de colores disponibles:")
    for id_gen, gen in enumerate(COLOR_GENES):
        # Mostramos el número, el cuadro de color y el nombre
        color_box = colorize_color(gen, "[ ]")
        print(f"{id_gen + 1}. {color_box} {gen}")
    print("-" * 43)

def get_secret_code_from_user():
    display_color_menu()
    while True:
        try:
            user_input = input(
                f"Ingresa tu código de {GENOME_LENGTH} dígitos (ej. 1 2 3 4): "
            )
            user_choices = [int(gen) for gen in user_input.split()]
        except ValueError:
            print("❌ Entrada no válida. Usa solo números.")
            continue

        if len(user_choices) != GENOME_LENGTH:
            print(f"❌ Error: Debes ingresar exactamente {GENOME_LENGTH} números.")
            continue

        if any(gen < 1 or gen > len(COLOR_GENES) for gen in user_choices):
            print(f"❌ Error: Números fuera de rango (1-{len(COLOR_GENES)}).")
            continue

        return [COLOR_GENES[gen - 1] for gen in user_choices]
