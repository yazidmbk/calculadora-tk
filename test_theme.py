import pytest
from tkinter import Tk
from app.calculadora import Calculadora

@pytest.fixture
def app():
    root = Tk()
    calc_app = Calculadora(root, lang="en")
    return calc_app

def test_theme_default(app):
    assert app.theme is not None  # Assurez-vous que self.theme est correctement initialisé
    assert app.theme['master_bg'] == '#212121'
    assert app.theme['frame_bg'] == '#212121'
    assert app.theme['BTN_NUMERICO']['bg'] == '#424242'
    assert app.theme['BTN_OPERADOR']['bg'] == '#616161'
    assert app.theme['BTN_DEFAULT']['bg'] == '#757575'
    assert app.theme['BTN_CLEAR']['bg'] == '#9E9E9E'
    assert app.theme['INPUT']['bg'] == '#BDBDBD'

def test_change_theme(app):
    assert app.theme is not None  # Assurez-vous que self.theme est correctement initialisé
    app._change_theme_to("Light")
    assert app.theme['master_bg'] == '#FAFAFA'
    assert app.theme['frame_bg'] == '#FAFAFA'
    assert app.theme['BTN_NUMERICO']['bg'] == '#FFFFFF'
    assert app.theme['BTN_OPERADOR']['bg'] == '#E0E0E0'
    assert app.theme['BTN_DEFAULT']['bg'] == '#BDBDBD'
    assert app.theme['BTN_CLEAR']['bg'] == '#9E9E9E'
    assert app.theme['INPUT']['bg'] == '#FFFFFF'