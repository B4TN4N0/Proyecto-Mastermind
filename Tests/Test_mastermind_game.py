import pytest





# ========================================================================== #
# ==================== TESTS PRINCIPALES CON MASTERMIND ==================== #
# ========================================================================== #




# ESTE TEST COMPROBARÁ QUE LA POBLACIÓN INICIAL TIENE EL TAMAÑO CORRECTO

@pytest.mark.people

def test_tamaño_poblacion_inicial(first_population): 
    assert len(first_population)== 100


# ------------------------------------------------------------------ #

# ESTE TEST COMPROBARÁ QUE CADA INDIVIDUO DE LA POBLACIÓN INICIAL TIENE EL TAMAÑO CORRECTO

@pytest.mark.people
def test_tamaño_poblacion_inicial(first_population):
    for individual in first_population:
        assert len(individual) == 4

# ------------------------------------------------------------------ #

