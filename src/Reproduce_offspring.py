import random

def reproduce_offspring(selected_parents):
    offspring_population = []
    
    # Recorremos la lista de dos en dos (paso de 2)
    for i in range(0, len(selected_parents), 2):
        # Aseguramos que haya un par disponible
        if i + 1 < len(selected_parents):
            parent1 = selected_parents[i]
            parent2 = selected_parents[i+1]
            
            # Punto de cruce (Single Point Crossover)
            cut_point = random.randint(1, len(parent1) - 1)
            
            # Creación de los dos hijos
            offspring1 = parent1[:cut_point] + parent2[cut_point:]
            offspring2 = parent2[:cut_point] + parent1[cut_point:]
            
            # Los añadimos a la nueva lista
            offspring_population.append(offspring1)
            offspring_population.append(offspring2)
            
    return offspring_population
# crear una nueva generación de individuos donde estan los hijos generados a partir de los padres seleccionados + los padres seleccionados
def create_new_generation(selected_parents, offspring_population):
    # Combinar padres e hijos
    new_generation = selected_parents + offspring_population
    return new_generation