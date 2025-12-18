import pytest





# ========================================================================== #
# ==================== TESTS GENERALES MASTERMIND ========================== #
# ========================================================================== #


# ================ TESTS DE INTRODUCCIÓN DE CODIGO SECRETO ================ #

# EN ESTE TEST COMPROBAMOS QUE EL CÓDIGO SECRETO INTRODUCIDO POR EL USUARIO TIENE EL TAMAÑO CORRECTO
@pytest.mark.user_input
def test_tamaño_codigo_secreto (user_secret_code):
    assert len(user_secret_code) == 4, (
        f"ERROR: El código secreto {user_secret_code} no tiene el tamaño correcto de 4 genes."
    )

# ------------------------------------------------------------------ #

# ESTE TEST COMPROBARÁ QUE LOS COLORES INTRODUCIDOS POR EL USUARIO SON VÁLIDOS
@pytest.mark.user_input
def test_colores_validos_codigo_secreto (secret_code,color_genes):
    for value in secret_code:
        assert value in color_genes(), (
            f"ERROR: El color {value} no es válido. Los colores permitidos son: {color_genes()}"
        )

# ------------------------------------------------------------------ #

# ESTE TEST COMPROBARÁ QUE LOS NÚMEROS INTRODUCIDOS POR EL USUARIO ESTÁN DENTRO DEL RANGO VÁLIDO
@pytest.mark.user_input
def test_rango_numeros_dentro_de_menu (user_input_numbers, color_genes):
    for number in user_input_numbers:
        assert 1 <= number <= len (color_genes()), (
            f"ERROR: El número {number} está fuera del rango válido. Debe estar entre 1 y {len(color_genes())}."
        )

# ------------------------------------------------------------------ #
