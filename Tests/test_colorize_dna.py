import pytest
import sys
sys.path.append("..")
from src.graphics.colorize import colorize_dna, colorize_color

@pytest.mark.colorize_dna
def test_colorize_color_red():
    """Verifica que un color rojo se convierta correctamente."""
    color_name = "Red"
    colored_output = colorize_color(color_name, "[ ]")

    assert colored_output == "\033[41m  \033[0m"  # ANSI para rojo

@pytest.mark.colorize_dna
def test_colorize_color_blue():
    """Verifica que un color azul se convierta correctamente."""
    color_name = "Blue"
    colored_output = colorize_color(color_name, "[ ]")

    assert colored_output == "\033[44m  \033[0m"  # ANSI para azul

@pytest.mark.colorize_dna
def test_colorize_dna_chain():
    """Verifica que una lista de colores se convierta correctamente."""
    dna_list = ["Red", "Green", "Blue", "Yellow"]
    colored_dna = colorize_dna(dna_list)

    expected_output = [
        "\033[41m  \033[0m",  # Red
        "\033[42m  \033[0m",  # Green
        "\033[44m  \033[0m",  # Blue
        "\033[43m  \033[0m"   # Yellow
    ]

    assert colored_dna == expected_output
