import pytest
import sys
from app.calculadora import Calculadora
from tkinter import Tk


@pytest.fixture
def app():
    root = Tk()
    calc_app = Calculadora(root, lang="en")
    return calc_app

def test_initialization(app):
    assert isinstance(app, Calculadora)

def test_change_language_to_pt(app):
    app._pt()
    assert app.lang == Calculadora.LANG["pt"]
    assert app._entrada.get() == "0"

def test_change_language_to_fr(app):
    app._fr()
    assert app.lang == Calculadora.LANG["fr"]
    assert app._entrada.get() == "0"

def test_change_language_to_en(app):
    app._en()
    assert app.lang == Calculadora.LANG["en"]
    assert app._entrada.get() == "0"