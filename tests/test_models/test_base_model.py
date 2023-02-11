import inspect
import models
from models.base_model import BaseModel
import pycodestyle
import unittest


class BaseModelTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def testpep8(self):
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        doc = models.base_model.__doc__
        self.assertIsNot(doc, None, "base_model.py needs a docstring")
        self.assertTrue(len(doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__, None,
                    "{:s} method needs a docstring".format(
                        func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(
                        func[0])
                )
