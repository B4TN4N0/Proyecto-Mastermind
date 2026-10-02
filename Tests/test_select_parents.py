import pytest
import sys
sys.path.append("..")
from src.select_parents import select_parents
# ========================================================================== #
# ==================== TESTS GENERALES MASTERMIND ========================== #
# ========================================================================== #

# ====================== TESTS DE SELECCIÓN DE PADRES ====================== #

# ESTE TEST COMPROBARÁ QUE LA FUNCIÓN DEVUELVE CUATRO PADRES
@pytest.mark.parentselection
def test_select_parents_count():
    population = [
        (['Red', 'Blue', 'Green', 'Yellow'], 5),
        (['Blue', 'Green', 'Yellow', 'Red'], 3),
        (['Green', 'Yellow', 'Red', 'Blue'], 8),
        (['Yellow', 'Red', 'Blue', 'Green'], 2)
    ]
    parents = select_parents(population)
    assert len(parents) == 4, "La función debe devolver cuatro padres"
# ESTE TEST COMPROBARÁ QUE LOS PADRES DEVUELTOS PERTENECEN A LA POBLACIÓN ORIGINAL
@pytest.mark.parentselection
def test_select_parents_in_population():
    population = [
        (['Red', 'Blue', 'Green', 'Yellow'], 5),
        (['Blue', 'Green', 'Yellow', 'Red'], 3),
        (['Green', 'Yellow', 'Red', 'Blue'], 8),
        (['Yellow', 'Red', 'Blue', 'Green'], 2)
    ]
    parents = select_parents(population)
    for parent in parents:
        assert parent in population, "Los padres deben pertenecer a la población"
# ESTE TEST COMPROBARÁ QUE LA MAYORIA DE LOS PADRES TIENE UNA APTITUD ALTA
@pytest.mark.parentselection
def test_select_parents_high_fitness():
    population = [
        (['Red', 'Blue', 'Green', 'Yellow'], 5),
        (['Blue', 'Green', 'Yellow', 'Red'], 3),
        (['Green', 'Yellow', 'Red', 'Blue'], 8),
        (['Yellow', 'Red', 'Blue', 'Green'], 2)
    ]
    parents = select_parents(population)
    fitness_values = [fitness for _, fitness in parents]
    average_fitness = sum(fitness_values) / len(fitness_values)
    assert average_fitness >= 4, "La mayoría de los padres debe tener una aptitud alta"
# ESTE TEST COMPROBARÁ QUE LA FUNCIÓN MANEJA UNA POBLACIÓN CON APTITUDES IGUALES
@pytest.mark.parentselection
def test_select_parents_equal_fitness():
    population = [
        (['Red', 'Blue', 'Green', 'Yellow'], 5),
        (['Blue', 'Green', 'Yellow', 'Red'], 5),
        (['Green', 'Yellow', 'Red', 'Blue'], 5),
        (['Yellow', 'Red', 'Blue', 'Green'], 5)
    ]
    parents = select_parents(population)
    fitness_values = [fitness for _, fitness in parents]
    average_fitness = sum(fitness_values) / len(fitness_values)
    assert average_fitness == 5, "Todos los padres deben tener la misma aptitud"
#========================================================================== #
# ========================= FIN DE LOS TESTS ============================== #
