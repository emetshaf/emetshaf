"""_summary_
"""
import inspect
import models
from models.base_model import BaseModel
import pycodestyle
import unittest


class TestBaseModelDocs(unittest.TestCase):
    """_summary_
    """
    @classmethod
    def setUpClass(self):
        """_summary_
        """
        self.all_funcs = inspect.getmembers(
            BaseModel, inspect.isfunction)

    def test_pep(self):
        """_summary_
        """
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """test module docstring
        """
        for module in [models.base_model]:
            with self.subTest(module=module):
                doc = module.__doc__
                self.assertIsNot(doc, None, "base_model needs a docstring")
                self.assertTrue(len(doc) >= 1, "base_model needs a docstring")

    def test_class_docstring(self):
        """test class docstring
        """
        for path in [BaseModel, TestBaseModelDocs]:
            with self.subTest(cls=path):
                doc = path.__doc__
                self.assertIsNot(doc, None, "base_model needs a docstring")
                self.assertTrue(len(doc) >= 1, "base_model needs a docstring")

    def test_func_docstrings(self):
        """_summary_
        """
        for clss in [self.all_funcs]:
            for func in clss:
                with self.subTest(function=func):
                    self.assertIsNot(
                        func[1].__doc__, None,
                        "{:s} method needs a docstring".format(func[0])
                    )
                    self.assertTrue(
                        len(func[1].__doc__) > 1,
                        "{:s} method needs a docstring".format(func[0])
                    )
