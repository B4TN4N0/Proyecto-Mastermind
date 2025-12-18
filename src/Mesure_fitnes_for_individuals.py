#mesure fitness for individuals in the population
import sys
sys.path.append("..")
from src.generate_first_population import first_population
from src.User_Imput_secret_code import secret_code_list

population = first_population()
solution = secret_code_list
# definimos valores para los pegs
BLACK_PEG_VALUE = 2 
WHITE_PEG_VALUE = 1 
REVISED_GEN = None
# funcion para medir la aptitud de un individuo
def mesure_individual_fitness(individual, solution):
    
    solution_temp = list(solution)
    individual_temp = list(individual) 
# contamos los pegs negros  cuando coinciden en posicion y  color
    black_pegs = 0
    for i in range(len(solution_temp)):
        if solution_temp[i] == individual_temp[i]:
            black_pegs += 1

            solution_temp[i] = REVISED_GEN
            individual_temp[i] = REVISED_GEN
# contamos los pegs blancos cuando coinciden en color pero no en posicion
    white_pegs = 0
    for individual_color in individual_temp:
        if individual_color != REVISED_GEN:
            try:
                match_index = solution_temp.index(individual_color)
                white_pegs += 1

                solution_temp[match_index] = REVISED_GEN


            except ValueError:
                pass
# asignamos un valor mínimo para cuando que cuando no haya aciertos se puedan reproducir
    no_pegs = 0
    if black_pegs == 0 and white_pegs == 0:
        no_pegs = 1

    fitness_value = black_pegs * BLACK_PEG_VALUE + white_pegs * WHITE_PEG_VALUE + no_pegs
    
    return fitness_value
# funcion para medir la aptitud de toda la poblacion
def mesure_population_fitness(population, solution):
    population_fitness = []
    
    for individual in population:
        score = mesure_individual_fitness(solution, individual)

        population_fitness.append((individual, score))
 
    return population_fitness
print (mesure_population_fitness(population, solution))