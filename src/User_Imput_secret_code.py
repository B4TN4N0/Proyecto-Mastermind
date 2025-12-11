import sys
sys.path.append("..")  
from src.algorithm_parameters import COLOR_GENES, GENOME_LENGTH
    
# Instrucciones para el usuario #

def display_color_menu():
    print("------Bienvenido al juego Mastermind.------")
    print ("menu de colores disponibles:")
    for id_gen, gen in enumerate(COLOR_GENES):
        print(f"{id_gen + 1}. {gen}")
    print("-------------------------------------------")


  # Solicitar al usuario que ingrese el código secreto# 
def get_secret_code_from_user():
    display_color_menu()
    while True:
        try:
            user_input = input(
                f"porfavor ingrese su codigo secreto de {GENOME_LENGTH} digitos (ejemplo: 1 2 3 4): se permiten colores repetidos: ")
            user_choices = [int(gen)for gen in user_input.split()]
# Validar la entrada del usuario #
        except ValueError:
            print ("entrada no valida. Asegurate de ingresar numeros separados por espacios.")
            continue
# Verificar que la longitud del código sea correcta #
        if len (user_choices) != GENOME_LENGTH:
            print (f"Error: Debes ingresar exactamente {GENOME_LENGTH} números.")
            continue
# Verificar que los números estén dentro del rango válido #
        if any (gen < 1 or gen > len(COLOR_GENES) for gen in user_choices):
            print (f"Error: Los números introducidos deben estar entre 1 y {len(COLOR_GENES)}.")
            continue
# Convertir los números a colores #
        secret_code = [COLOR_GENES[gen-1] for gen in user_choices]
        return secret_code

codigo_secreto = get_secret_code_from_user()
print(f"Tu código secreto es: {codigo_secreto}")

