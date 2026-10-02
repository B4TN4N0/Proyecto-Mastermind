import random

def select_parents(population_with_fitness):
    # Extraer los valores de fitness
    fitness_values = [score for _, score in population_with_fitness]
    total_fitness = sum(fitness_values)

    # Probabilidades de selección proporcional al fitness
    selection_probs = [f / total_fitness for f in fitness_values]

    # Selección ponderada con repeticiones
    selected_parents = random.choices(population_with_fitness, weights=selection_probs, k=len(population_with_fitness))

    return selected_parents
