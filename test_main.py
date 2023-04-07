import unittest

from main import check_list_elements_recursive

class TestCheckListElementsRecursive(unittest.TestCase):

    def test_same_lists(self):
        L1 = [1, 2, 3]
        L2 = [1, 2, 3]
        self.assertTrue(check_list_elements_recursive(L1, L2))

    def test_extra_elements_in_L2(self):
        L1 = [1, 2, 3]
        L2 = [1, 2, 3, 4, 5]
        self.assertTrue(check_list_elements_recursive(L1, L2))

    def test_missing_elements_in_L2(self):
        L1 = [1, 2, 3]
        L2 = [1, 2, 4, 5]
        self.assertFalse(check_list_elements_recursive(L1, L2))

    def test_empty_lists(self):
        L1 = []
        L2 = []
        self.assertTrue(check_list_elements_recursive(L1, L2))

    def test_empty_L1(self):
        L1 = []
        L2 = [1, 2, 3]
        self.assertTrue(check_list_elements_recursive(L1, L2))

    def test_empty_L2(self):
        L1 = [1, 2, 3]
        L2 = []
        self.assertFalse(check_list_elements_recursive(L1, L2))
