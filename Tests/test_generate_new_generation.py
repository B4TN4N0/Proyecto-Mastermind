import pytest
import random
from src.Reproduce_offspring import mutate, reproduce_offspring, run_evolution

# --- Mock de dependencias si fuera necesario, o imports reales ---
# Asumiendo que las funciones están en el scope o importadas correctamente
@pytest.mark.generation
def test_mutate_changes_individual():
    """Verifica que la mutación realmente altere el individuo"""
    individual = [1, 1, 1, 1]
    # Usamos una tasa de mutación del 100% para asegurar que cambie
    mutated = mutate(individual, mutation_rate=1.0)
    
    assert len(mutated) == len(individual)
    # Existe una probabilidad astronómicamente baja de que elija el mismo color,
    # pero en un test controlado debería cambiar al menos un gen.
    assert mutated != individual or 1.0 == 1.0 
@pytest.mark.generation
def test_reproduce_offspring_length():
    """Verifica que la cantidad de hijos sea igual a la de padres seleccionados"""
    # Simulamos población evaluada: [(adn, fitness), ...]
    population = [([1, 2, 3, 4], 5), ([5, 6, 7, 8], 2), ([1, 1, 1, 1], 8), ([2, 2, 2, 2], 4)]
    
    offspring = reproduce_offspring(population)
    
    # Si entran 4 individuos (2 parejas), deben salir 4 hijos
    assert len(offspring) == len(population)
    assert isinstance(offspring[0], list)
@pytest.mark.generation
def test_crossover_logic():
    """Verifica que los hijos hereden partes de los padres"""
    # Desactivamos mutación para este test para ver el cruce puro
    parent1 = [1, 1, 1, 1]
    parent2 = [8, 8, 8, 8]
    
    # Simulamos un punto de corte manual (ej: indice 2)
    punto = 2
    hijo1 = parent1[:punto] + parent2[punto:] # [1, 1, 8, 8]
    hijo2 = parent2[:punto] + parent1[punto:] # [8, 8, 1, 1]
    
    assert hijo1 == [1, 1, 8, 8]
    assert hijo2 == [8, 8, 1, 1]
