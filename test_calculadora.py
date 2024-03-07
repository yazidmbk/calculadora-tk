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


def test_set_values_in_input(app):
    app._set_values_in_input(5)
    assert app._entrada.get() == "5"

def test_set_operator_in_input(app):
    app._set_operator_in_input("+")
    assert app._entrada.get() == "+"

def test_set_dot_in_input(app):
    app._set_dot_in_input(".")
    assert app._entrada.get() == "0."

def test_set_open_parent(app):
    app._set_open_parent()
    assert app._entrada.get() == "("

def test_set_close_parent(app):
    app._set_close_parent()
    assert app._entrada.get() == ")"

def test_clear_input(app):
    app._set_values_in_input(5)
    app._clear_input()
    assert app._entrada.get() == "0"

def test_del_last_value_in_input(app):
    app._set_values_in_input(123)
    app._del_last_value_in_input()
    assert app._entrada.get() == "12"

def test_get_data_in_input(app):
    app._set_values_in_input(2)
    app._set_operator_in_input("+")
    app._set_values_in_input(3)
    app._get_data_in_input()
    assert app._entrada.get() == "5"

def test_change_theme_to(app):
    app._change_theme_to("Dark")
    assert app.settings['current_theme'] == "Dark"


