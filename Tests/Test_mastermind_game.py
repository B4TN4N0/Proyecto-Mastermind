import pytest





# ========================================================================== #
# ==================== TESTS GENERALES MASTERMIND ========================== #
# ========================================================================== #


# ================ TESTS DE GENERACION DE POBLACION INICIAL ================ #

# ESTE TEST COMPROBARÁ QUE LA POBLACIÓN INICIAL TIENE EL TAMAÑO CORRECTO

@pytest.mark.people

def test_tamaño_poblacion_inicial(first_population): 
    assert len(first_population)== 100


# ------------------------------------------------------------------ #

# ESTE TEST COMPROBARÁ QUE CADA INDIVIDUO DE LA POBLACIÓN INICIAL TIENE EL TAMAÑO CORRECTO

@pytest.mark.people
def test_tamaño_genoma_poblacion_inicial(first_population):
    for individual in first_population:
        assert len(individual) == 4

# ------------------------------------------------------------------ #

# Este test comprueba que los colores en la población inicial son válidos

@pytest.mark.people
def test_colores_validos_poblacion_inicial(first_population,color_genes):
    for gen in first_population:
        for value in gen:
            assert value in color_genes

# ------------------------------------------------------------------ #

# =========================================================================== #