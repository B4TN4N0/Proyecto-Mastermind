# mesure fitness for individuals in the population

# ==================== CONSTANTES ==================== #

BLACK_PEG_VALUE = 2
WHITE_PEG_VALUE = 1
REVISED_GEN = None


# ==================== FITNESS INDIVIDUAL ==================== #

def mesure_black_and_white_pegs(individual, solution):
    solution_temp = list(solution)
    individual_temp = list(individual)

    # Pegs negros (color y posición)
    black_pegs = 0
    for i in range(len(solution_temp)):
        if solution_temp[i] == individual_temp[i]:
            black_pegs += 1
            solution_temp[i] = REVISED_GEN
            individual_temp[i] = REVISED_GEN

    # Pegs blancos (color correcto, posición incorrecta)
    white_pegs = 0
    for color in individual_temp:
        if color != REVISED_GEN:
            try:
                match_index = solution_temp.index(color)
                white_pegs += 1
                solution_temp[match_index] = REVISED_GEN
            except ValueError:
                pass

    return black_pegs, white_pegs

def mesure_individual_fitness(individual, solution):

    black_pegs, white_pegs = mesure_black_and_white_pegs(individual, solution)

    # Valor mínimo si no hay aciertos
    no_pegs = 1 if black_pegs == 0 and white_pegs == 0 else 0

    individual_fitness = black_pegs * BLACK_PEG_VALUE + white_pegs * WHITE_PEG_VALUE + no_pegs
    return individual_fitness

# ==================== FITNESS POBLACIÓN ==================== #

def mesure_population_fitness(population, solution):
    return [
        (individual, mesure_individual_fitness(individual, solution))
        for individual in population
    ]
