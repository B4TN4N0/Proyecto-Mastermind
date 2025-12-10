import pytest





# ========================================================================== #
# ==================== TESTS GENERALES MASTERMIND ========================== #
# ========================================================================== #


# ================ TESTS DE GENERACION DE POBLACION INICIAL ================ #

# ESTE TEST COMPROBARÁ QUE LA POBLACIÓN INICIAL TIENE EL TAMAÑO CORRECTO

@pytest.mark.population

def test_tamaño_poblacion_inicial(first_population): 
    assert len(first_population)== 100


# ------------------------------------------------------------------ #

# ESTE TEST COMPROBARÁ QUE CADA INDIVIDUO DE LA POBLACIÓN INICIAL TIENE EL TAMAÑO CORRECTO

@pytest.mark.population
def test_tamaño_genoma_poblacion_inicial(first_population):
    for individual in first_population:
        assert len(individual) == 4 (
            f"ERROR: El individuo {individual} no tiene el tamaño correcto de 4 genes."
        )

# ------------------------------------------------------------------ #

# Este test comprueba que los colores en la población inicial son válidos #

@pytest.mark.population
def test_colores_validos_poblacion_inicial(first_population,color_genes):
    for gen in first_population:
        for value in gen:
            assert value in color_genes (
             f"ERROR: El color {value} no es válido. Los colores permitidos son: {color_genes()}" 
             )
            


# ------------------------------------------------------------------ #

# Este test comprueba que si puedan existir convinaciones con los  colores permitidos repetidos en el mismo individuo 
# ejemplo [RED , GREEN , RED , BLUE]#

@pytest.mark.population
def test_colores_repetidos_dentro_individuo(first_population):
    TAMAÑO_POBLACION = len(first_population)
    repeticiones_encontradas = 0
    for individuo in first_population:
        colores_unicos = set(individuo)
        
        if len(colores_unicos) < len(individuo):
            repeticiones_encontradas += 1
 
    UMBRAL_MINIMO_REPETICIONES = max(1, int(TAMAÑO_POBLACION * 0.05)) # Al menos un 5% de la población debe tener colores repetidos
    
    assert repeticiones_encontradas >= UMBRAL_MINIMO_REPETICIONES, (
        f"ERROR: De {TAMAÑO_POBLACION} códigos generados, solo {repeticiones_encontradas} contenían colores repetidos. " 
        f"Se esperaba un mínimo de {UMBRAL_MINIMO_REPETICIONES}. La función 'first_population' puede haber sido cambiada "
        f"accidentalmente a un método sin reemplazo (como random.sample)."
    )


# =========================================================================== #