import pytest
import Test_mastermind as casos_test
import src.generate_first_population

@pytest.mark.population
def test_tamaño_poblacion_inicial(first_population):
    casos_test.test_tamaño_poblacion_inicial(first_population)
    casos_test.test_tamaño_genoma_poblacion_inicial(first_population)
    casos_test.test_colores_validos_poblacion_inicial(first_population)
    casos_test.test_colores_repetidos_dentro_individuo(first_population)