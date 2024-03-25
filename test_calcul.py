import unittest
import pytest
from tkinter import Tk
from app.calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.calculadora = Calculadora(self.root, lang="pt")

    def test_calcul(self):
        # Teste une opération simple
        self.calculadora._set_values_in_input(5)
        self.calculadora._set_operator_in_input('+')
        self.calculadora._set_values_in_input(3)
        self.calculadora._get_data_in_input()
        self.assertEqual(self.calculadora._entrada.get(), "8")

    def test_calcule(self):  # Teste une opération plus complexe avec des parenthèses
        self.calculadora._clear_input()
        self.calculadora._set_values_in_input(2)
        self.calculadora._set_operator_in_input('*')
        self.calculadora._set_open_parent()
        self.calculadora._set_values_in_input(3)
        self.calculadora._set_operator_in_input('+')
        self.calculadora._set_values_in_input(4)
        self.calculadora._set_close_parent()
        self.calculadora._get_data_in_input()
        self.assertEqual(self.calculadora._entrada.get(), "10")

    def tearDown(self):
        self.root.destroy()


if __name__ == "__main__":
    unittest.main()
