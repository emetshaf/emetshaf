"""test console module
"""
import console
from console import EMETSHAFCommand
import inspect
import pycodestyle
import unittest


class TestConsoleDocs(unittest.TestCase):
    """TestConsoleDocs class
    """
    @classmethod
    def setUpClass(cls):
        """_summary_
        """
        cls.all_funcs = inspect.getmembers(EMETSHAFCommand,
                                           inspect.isfunction)

    def test_pep(self):
        """test code style
        """
        for path in ['console.py', 'tests/test_console.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """test module docstring
        """
        for path in [console]:
            with self.subTest(module=path):
                doc = path.__doc__
                self.assertIsNot(doc, None, "console needs a docstring")
                self.assertTrue(len(doc) >= 1, "console needs a docstring")

    def test_class_docstring(self):
        """test class docstring
        """
        for path in [EMETSHAFCommand, TestConsoleDocs]:
            with self.subTest(cls=path):
                doc = path.__doc__
                self.assertIsNot(doc, None, "console needs a docstring")
                self.assertTrue(len(doc) >= 1, "console needs a docstring")

    def test_func_docstrings(self):
        for clss in []:
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
