
from src.algorithm_parameters import *
from src.generate_first_population import first_population
from src.User_Imput_secret_code import get_secret_code_from_user
from src.Mesure_fitnes_for_individuals import mesure_population_fitness
from src.select_parents import select_parents

def main():
    population = first_population()
    solution = get_secret_code_from_user()
    population_with_fitness = mesure_population_fitness(population, solution)
    parents = select_parents(population_with_fitness)

if __name__ == "__main__":
    main()
