import sys
sys.path.append("..")  
from src.algorithm_parameters import COLOR_GENES, GENOME_LENGTH

# ==================== UI ==================== #

def display_color_menu():
    print("------Bienvenido al juego Mastermind.------")
    print("menu de colores disponibles:")
    for id_gen, gen in enumerate(COLOR_GENES):
        print(f"{id_gen + 1}. {gen}")
    print("-------------------------------------------")


def get_secret_code_from_user():
    display_color_menu()
    while True:
        try:
            user_input = input(
                f"Por favor ingrese su codigo secreto de {GENOME_LENGTH} digitos "
                f"(ejemplo: 1 2 3 4). Se permiten colores repetidos: "
            )
            user_choices = [int(gen) for gen in user_input.split()]
        except ValueError:
            print("Entrada no valida. Asegurate de ingresar numeros separados por espacios.")
            continue

        if len(user_choices) != GENOME_LENGTH:
            print(f"Error: Debes ingresar exactamente {GENOME_LENGTH} numeros.")
            continue

        if any(gen < 1 or gen > len(COLOR_GENES) for gen in user_choices):
            print(f"Error: Los numeros deben estar entre 1 y {len(COLOR_GENES)}.")
            continue

        return [COLOR_GENES[gen - 1] for gen in user_choices]


# ==================== ENTRY POINT ==================== #

def main():
    codigo_secreto = get_secret_code_from_user()
    print(f"Tu codigo secreto es: {codigo_secreto}")


if __name__ == "__main__":
    main()

