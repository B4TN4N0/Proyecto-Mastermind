from src.algorithm_parameters import COLOR_GENES, GENOME_LENGTH, POPULATION_SIZE
import random
def first_population():
    first_population = []
    for _ in range(POPULATION_SIZE):
        gen_combination = random.choices(COLOR_GENES, k=GENOME_LENGTH)
        first_population.append(gen_combination)
    return first_population
