import unittest

from scopeton import scope, scopeTools
from scopeton.objects import Bean
from scopeton.qualifier_tree import QualifierTree
from scopeton.scopeTools import getBean_qualifier, callMethodByName, ScopetonException


class ScopeTest(unittest.TestCase):

    def test_register(self):
        tree = QualifierTree()
        tree.register("aaa", 1)
        tree.register("bbb", 2)
        tree.register(["zzz", "bbb", "ccc"], 3)
        res = tree.find_by_qualifier_name("aaa")
        self.assertEqual(1, res)
        self.assertEqual(3, tree.find_by_qualifier_name("zzz"))
        self.assertEqual(3, tree.find_by_qualifier_name("ccc"))

    def test_register_multiple(self):
        tree = QualifierTree()
        tree.register(["aaa", "bbb", "ccc"], 1)
        tree.register(["aaa", "bbb", "ddd"], 2)
        self.assertEqual(1, tree.find_by_qualifier_name("ccc"))
        self.assertEqual(2, tree.find_by_qualifier_name("ddd"))

    def test_error(self):
        tree = QualifierTree()
        tree.register(["aaa", "bbb", "ddd"], 1)
        tree.register(["aaa", "bbb", "ddd"], 2)
        try:
            self.assertEqual(2, tree.find_by_qualifier_name("ddd"))
            ok = False
        except ScopetonException:
            ok = True

        self.assertTrue(ok)

    def test_get_object(self):
        tree = QualifierTree()
        tree.register(["aaa", "bbb", "ddd"], 1)
        tree.register(["aaa", "bbb", "ddd"], 2)
        res = sorted(tree.get_all_objects())
        self.assertEqual([1, 2], res)



if __name__ == "__main__":
    unittest.main()