"""_summary_
"""
import inspect
import models
from models.engine.storage import Storage
import pycodestyle
import unittest


class TestStorage(unittest.TestCase):
    """_summary_
    """
    @classmethod
    def setUpClass(self):
        """_summary_
        """
        self.all_funcs = inspect.getmembers(
            Storage, inspect.isfunction)

    def test_pep(self):
        """_summary_
        """
        for path in ['models/engine/storage.py',
                     'tests/test_models/test_engine/test_storage.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """test module docstring
        """
        for module in [models.engine.storage]:
            with self.subTest(module=module):
                doc = module.__doc__
                self.assertIsNot(
                    doc, None,
                    "storage needs a docstring")
                self.assertTrue(
                    len(doc) >= 1,
                    "storage needs a docstring")

    def test_class_docstring(self):
        """test class docstring
        """
        for path in [Storage, TestStorage]:
            with self.subTest(cls=path):
                doc = path.__doc__
                self.assertIsNot(
                    doc, None,
                    "storage needs a docstring")
                self.assertTrue(
                    len(doc) >= 1,
                    "storage needs a docstring")

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
