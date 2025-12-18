import pytest
import sys
sys.path.append("..")
from src.Mesure_fitnes_for_individuals import mesure_individual_fitness
# ========================================================================== #
# ==================== TESTS GENERALES MASTERMIND ========================== #
# ========================================================================== #


# ============== TESTS DE GENERACION DE MEDICIÓN DE APTITUD ================ #

# ESTE TEST COMPROBARÁ QUE LA MEDICIÓN DE APTITUD DEVUELVE UN VALOR ENTRE 1 Y 8
@pytest.mark.fitness
def test_mesure_individual_fitness_range():
    individual = ['Red', 'Blue', 'Green', 'Yellow']
    solution = ['Red', 'Green', 'Blue', 'Yellow']
    fitness = mesure_individual_fitness(individual, solution)
    assert 1 <= fitness <= 8, "La aptitud debe estar entre 1 y 8"
# ESTE TEST COMPROBARÁ QUE LA MEDICIÓN DE APTITUD DEVUELVE 8 PARA UNA COINCIDENCIA PERFECTA
@pytest.mark.fitness
def test_mesure_individual_fitness_perfect_match():
    individual = ['Red', 'Blue', 'Green', 'Yellow']
    solution = ['Red', 'Blue', 'Green', 'Yellow']
    fitness = mesure_individual_fitness(individual, solution)
    assert fitness == 8, "La aptitud debe ser 8 para una coincidencia perfecta"
# ESTE TEST COMPROBARÁ QUE LA MEDICIÓN DE APTITUD DEVUELVE 1 PARA NINGUNA COINCIDENCIA
@pytest.mark.fitness
def test_mesure_individual_fitness_no_match():
    individual = ['Red', 'Red', 'Red', 'Red']
    solution = ['Blue', 'Blue', 'Blue', 'Blue']
    fitness = mesure_individual_fitness(individual, solution)
    assert fitness == 1, "La aptitud debe ser 1 para ninguna coincidencia"
# ESTE TEST COMPROBARÁ QUE LA MEDICIÓN DE APTITUD DEVUELVE 4 PARA DOS COINCIDENCIAS DE COLOR Y POSICIÓN
@pytest.mark.fitness
def test_mesure_individual_fitness_two_black_pegs():
    individual = ['Red', 'Blue', 'Green', 'Yellow']
    solution = ['Red', 'Blue', 'Purple', 'Orange']
    fitness = mesure_individual_fitness(individual, solution)
    assert fitness == 4, "La aptitud debe ser 4 para dos coincidencias de color y posición"
# ESTE TEST COMPROBARÁ QUE LA MEDICIÓN DE APTITUD DEVUELVE 2 PARA CUATRO COINCIDENCIAS DE COLOR
@pytest.mark.fitness
def test_mesure_individual_fitness_four_white_pegs():
    individual = ['Red', 'Blue', 'Green', 'Yellow']
    solution = ['Blue', 'Red', 'Yellow', 'Green']
    fitness = mesure_individual_fitness(individual, solution)
    assert fitness == 4, "La aptitud debe ser 4 para cuatro coincidencias de color"
# ESTE TEST COMPROBARÁ QUE LA MEDICIÓN DE APTITUD DEVUELVE 6 PARA TRES COINCIDENCIAS DE COLOR Y POSICIÓN Y UNA COINCIDENCIA DE COLOR
@pytest.mark.fitness
def test_mesure_individual_fitness_three_black_one_white_pegs():
    individual = ['Red', 'Blue', 'Green', 'Yellow']
    solution = ['Red', 'Blue', 'Green', 'Purple']
    fitness = mesure_individual_fitness(individual, solution)
    assert fitness == 6, "La aptitud debe ser 6 para tres coincidencias de color y posición y una coincidencia de color"
# ESTE TEST COMPROBARÁ QUE LA MEDICIÓN DE APTITUD DEVUELVE 5 PARA DOS COINCIDENCIAS DE COLOR Y POSICIÓN Y DOS COINCIDENCIAS DE COLOR
@pytest.mark.fitness
def test_mesure_individual_fitness_two_black_two_white_pegs():
    individual = ['Red', 'Blue', 'Green', 'Yellow']
    solution = ['Red', 'Blue', 'Yellow', 'Green']
    fitness = mesure_individual_fitness(individual, solution)
    assert fitness == 6, "La aptitud debe ser 6 para dos coincidencias de color y posición y dos coincidencias de color"

#========================================================================== #
# ========================= FIN DE LOS TESTS ============================== #
# ========================================================================== #
