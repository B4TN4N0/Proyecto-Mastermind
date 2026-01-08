import random
from src.algorithm_parameters import *
from src.generate_first_population import first_population
from src.User_Imput_secret_code import get_secret_code_from_user
from src.Mesure_fitnes_for_individuals import mesure_population_fitness
from src.select_parents import select_parents

# Importamos la función de reproducción que definiste antes
# Asegúrate de que esté en un archivo llamado src/reproduce.py o similar
from src.Reproduce_offspring import reproduce_offspring

def main():
    # 1. Configuración inicial
    population = first_population() # Tamaño N
    solution = get_secret_code_from_user()

    found = False
    generation = 0
    max_generations = 14 # Límite de seguridad

    # Evaluamos la primera población
    population_with_fitness = mesure_population_fitness(population, solution)

    while not found and generation < max_generations:
        # --- PROGRESO ---
        # Buscamos al mejor individuo actual
        best_individual = max(population_with_fitness, key=lambda x: x[1])

        # Formateamos el ADN del mejor individuo con colores
        visual_dna = colorize_dna(best_individual[0])

        print(f"Generación {generation:02d} | FMejor Fitness: {best_individual[1]} | ADN: {visual_dna}")

        # Si el fitness es el máximo
        if best_individual[0] == solution:
            print(f"\n✨ ¡Solución encontrada en la generación {generation}! ✨")
            print(f"Resultado final: {visual_dna}")
            found = True
            break

        # --- EVOLUCIÓN ---

        # 2. Cruce: Generamos hijos
        offspring_dna = reproduce_offspring(population_with_fitness)

        # 3. Evaluación: Medimos el fitness de los hijos
        offspring_with_fitness = mesure_population_fitness(offspring_dna, solution)

        # 4. Competencia: Mezclamos padres e hijos
        total_pool = population_with_fitness + offspring_with_fitness

        # 5. Supervivencia
        population_with_fitness = select_parents(total_pool)

        generation += 1

    if not found:
        print("\nSe alcanzó el límite de generaciones sin encontrar la solución exacta.")

if __name__ == "__main__":
    main()
