 
from src.algorithm_parameters import *
from src.generate_first_population import first_population
from src.User_Imput_secret_code import get_secret_code_from_user
from src.Mesure_fitnes_for_individuals import mesure_population_fitness

def main():
    population = first_population()
    solution = get_secret_code_from_user()
    fitness = mesure_population_fitness(population, solution)

if __name__ == "__main__":
    main()
