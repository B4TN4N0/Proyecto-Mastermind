import pytest
import sys
sys.path.append("..")

from src.generate_first_population import first_population
# ========================================================================== #
# ==================== TESTS GENERALES MASTERMIND ========================== #
# ========================================================================== #


# ================ TESTS DE GENERACION DE POBLACION INICIAL ================ #

# ESTE TEST COMPROBARÁ QUE LA POBLACIÓN INICIAL TIENE EL TAMAÑO CORRECTO
@pytest.mark.population
def test_first_population_size():                   
    population = first_population()
    assert len(population) == 100, "La población inicial debe tener 100 individuos"
# ESTE TEST COMPROBARÁ QUE CADA INDIVIDUO EN LA POBLACIÓN INICIAL TIENE LA LONGITUD DE GENOMA CORRECTA
@pytest.mark.population
def test_first_population_individual_length():             
    population = first_population()
    for individual in population:
        assert len(individual) == 4, "Cada individuo debe tener una longitud de genoma de 4"
# ESTE TEST COMPROBARÁ QUE LA POBLACIÓN INICIAL ES DIFERENTE EN CADA EJECUCIÓN
@pytest.mark.population
def test_first_population_randomness():             
    population1 = first_population()
    population2 = first_population()
    assert population1 != population2, "La población inicial debe ser diferente en cada ejecución"
# ESTE TEST COMPROBARÁ QUE LA POBLACIÓN INICIAL SE GENERA EN UN TIEMPO RAZONABLE
import time
@pytest.mark.population
def test_first_population_performance():             
    start_time = time.time()
    first_population()
    end_time = time.time()
    elapsed_time = end_time - start_time
    assert elapsed_time < 1, "La generación de la población inicial debe ser rápida (menos de 1 segundo)"
# ESTE TEST COMPROBARÁ QUE TODOS LOS COLORES EN CADA INDIVIDUO SON VÁLIDOS
from src.algorithm_parameters import COLOR_GENES
@pytest.mark.population
def test_first_population_valid_colors():             
    population = first_population()
    for individual in population:
        for color in individual:
            assert color in COLOR_GENES, f"El color {color} no es válido en el individuo {individual}"
            
#========================================================================== #
# ========================= FIN DE LOS TESTS ============================== #
# ========================================================================== #
