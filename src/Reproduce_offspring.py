import random
from src.select_parents import select_parents
from src.Mesure_fitnes_for_individuals import mesure_population_fitness
from src.algorithm_parameters import COLOR_GENES,MUTATION_RATE

# Definimos los colores disponibles para la mutación
COLORES_MASTERMIND = [COLOR_GENES]

def mutate(individual, mutation_rate=MUTATION_RATE):
 
    mutated_ind = list(individual)
    for i in range(len(mutated_ind)):
        if random.random() < mutation_rate:
            # Seleccionamos un color aleatorio de los 8 disponibles
            mutated_ind[i] = random.choice(COLORES_MASTERMIND)
    return mutated_ind

def reproduce_offspring(population_with_fitness):
    # Selección por ruleta para decidir quiénes son padres
    selected_parents = select_parents(population_with_fitness)
    
    offspring = []
    for i in range(0, len(selected_parents), 2):
        if i + 1 < len(selected_parents):
            parent1 = selected_parents[i][0]
            parent2 = selected_parents[i+1][0]
            
            punto = random.randint(1, len(parent1) - 1)
            
            # Cruce
            hijo1 = parent1[:punto] + parent2[punto:]
            hijo2 = parent2[:punto] + parent1[punto:]
            
            # Mutación inmediata de los hijos
            offspring.append(mutate(hijo1))
            offspring.append(mutate(hijo2))
            
    return offspring

def run_evolution(initial_population, solution, max_generations=200):
    # Evaluación inicial
    current_pop_with_fitness = mesure_population_fitness(initial_population, solution)
    
    for gen in range(max_generations):
        # Localizamos al mejor para informar y verificar victoria
        mejor_individuo = max(current_pop_with_fitness, key=lambda x: x[1])
        
        # El fitness máximo depende de tu constante BLACK_PEG_VALUE (ej: 4 aciertos * 2 pts = 8)
        print(f"Gen {gen} | Mejor: {mejor_individuo[0]} | Fitness: {mejor_individuo[1]}")

        if mejor_individuo[0] == solution:
            print(f"--- ¡SOLUCIÓN ENCONTRADA EN GEN {gen}! ---")
            break

        # Evolución: Cruce -> Mutación -> Evaluación -> Selección de sobrevivientes
        offspring_dna = reproduce_offspring(current_pop_with_fitness)
        offspring_with_fitness = mesure_population_fitness(offspring_dna, solution)
        
        # Unimos padres e hijos y pasamos la ruleta para mantener el tamaño original
        pool_total = current_pop_with_fitness + offspring_with_fitness
        current_pop_with_fitness = select_parents(pool_total)

    return current_pop_with_fitness