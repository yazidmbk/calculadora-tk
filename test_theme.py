import pytest
import sys

from app.calculador import Calculador
from app.calculadora import Calculadora
from tkinter import Tk


class Calculadora:
    def __init__(self, master, lang="pt"):
        self.master = master
        self.calc = Calculador()
        self.lang = Calculadora.LANG[lang]
        self.settings = self._load_settings()

        # Définissez un thème par défaut au cas où aucun thème ne serait trouvé
        self.default_theme = {
            'master_bg': 'default_background_color',
            'text_color': 'default_text_color'
        }

        # Définissez le chemin d'accès à Tcl, nécessaire pour Tkinter
        sys.path.append('C:/Users/bachelor/AppData/Local/Programs/Python/Python311/tcl/tcl8.6')

        # Autres initialisations...

    # Modifiez la méthode _get_theme pour gérer les thèmes inexistants
    def _get_theme(self, theme_name):
        # Supposez que self.available_themes contient les thèmes disponibles
        return self.available_themes.get(theme_name, self.default_theme)
@pytest.fixture
def app():
    root = Tk()
    calc_app = Calculadora(root, lang="en")
    return calc_app

def test_change_theme_to_valid_theme(app):
    app._change_theme_to('Dark')
    # Suppose que le thème Dark définit la couleur de fond à 'darkgrey' et la couleur de texte à 'white'
    assert app.main_color == 'darkgrey', "La couleur principale doit être 'darkgrey' pour le thème Dark"
    assert app.text_color == 'white', "La couleur du texte doit être 'white' pour le thème Dark"

def test_change_theme_to_invalid_theme(app):
    original_main_color = app.main_color
    original_text_color = app.text_color
    app._change_theme_to('Invalid Theme')
    # Vérifiez qu'aucune erreur n'est survenue et que le thème reste le même
    assert app.main_color == original_main_color, "La couleur principale doit rester inchangée avec un thème invalide"
    assert app.text_color == original_text_color, "La couleur du texte doit rester inchangée avec un thème invalide"

def test_default_theme(app):
    app._change_theme_to('Default')
    # Suppose que le thème par défaut a certaines valeurs que vous pouvez tester
    expected_main_color = 'default_main_color'  # Remplacer par la vraie valeur
    expected_text_color = 'default_text_color'  # Remplacer par la vraie valeur
    assert app.main_color == expected_main_color, f"La couleur principale doit être '{expected_main_color}' pour le thème par défaut"
    assert app.text_color == expected_text_color, f"La couleur du texte doit être '{expected_text_color}' pour le thème par défaut"

def test_theme_colors(app):
    app._change_theme_to('Light')  # Suppose que 'Light' est un thème valide
    # Suppose que le thème Light définit la couleur de fond à 'white' et la couleur de texte à 'black'
    assert app.main_color == 'white', "La couleur principale doit être 'white' pour le thème Light"
    assert app.text_color == 'black', "La couleur du texte doit être 'black' pour le thème Light"