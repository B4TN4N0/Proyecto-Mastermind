import random
from src.select_parents import select_parents
from src.Mesure_fitnes_for_individuals import mesure_population_fitness

# ... (Aquí iría tu función reproduce_offspring ya definida)

def run_evolution(initial_population, solution, max_generations=100):
    """
    Ejecuta el bucle de generaciones.
    """
    # 1. Evaluación inicial de la población
    current_pop_with_fitness = mesure_population_fitness(initial_population, solution)
    
    for gen in range(max_generations):
        # Mostramos el mejor fitness de la generación actual para seguimiento
        best_individual = max(current_pop_with_fitness, key=lambda x: x[1])
        print(f"Generación {gen}: Mejor fitness = {best_individual[1]}")

        # Si encontramos la solución perfecta, detenemos el bucle
        # (Ajusta el valor 10 según el puntaje máximo de tu fitness)
        if best_individual[1] >= 10: 
            print("¡Solución encontrada!")
            break

        # --- EL BUCLE DE GENERACIÓN ---
        
        # 2. Generamos los hijos (ADN)
        offspring_dna = reproduce_offspring(current_pop_with_fitness)
        
        # 3. Evaluamos a los hijos
        offspring_with_fitness = mesure_population_fitness(offspring_dna, solution)
        
        # 4. Creamos el pool total (Padres + Hijos)
        total_pool = current_pop_with_fitness + offspring_with_fitness
        
        # 5. PASO POR SELECT_PARENTS (Ruleta de supervivencia)
        # Esto genera la población que entrará en la SIGUIENTE iteración del bucle
        current_pop_with_fitness = select_parents(total_pool)

    return current_pop_with_fitness