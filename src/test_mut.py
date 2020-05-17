from mutable import *
import hypothesis.strategies as st
from hypothesis import given
import unittest

class TestMutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(DA_mut().size, 0)
        self.assertEqual(DA_mut([1, 2, 3]).size, 3)
    
    def test_change_capacity(self):
        lst=DA_mut()
        lst.change_capacity(120)
        self.assertEqual(lst._capacity, 120)

    def test_to_list(self):
        self.assertEqual(DA_mut().to_list(), [])
        self.assertEqual(DA_mut([1, 2, 3]).to_list(), [1, 2, 3])

    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            lst = DA_mut()
            lst.from_list(e)
            self.assertEqual(lst.to_list(), e)

    def test_add_to_head(self):
        lst = DA_mut()
        self.assertEqual(lst.to_list(), [])
        lst.add_to_head('a')
        self.assertEqual(lst.to_list(), ['a'])
        lst.add_to_head('b')
        self.assertEqual(lst.to_list(), ['b', 'a'])

    def test_add_to_tail(self):
        lst = DA_mut()
        self.assertEqual(lst.to_list(), [])
        lst.add_to_tail('a')
        self.assertEqual(lst.to_list(), ['a'])
        lst.add_to_tail('b')
        self.assertEqual(lst.to_list(), ['a', 'b'])

    def test_map(self):
        lst = DA_mut()
        lst.map(str)
        self.assertEqual(lst.to_list(), [])
        lst = DA_mut()
        lst.from_list([1, 2, 3])
        lst.map(str)
        self.assertEqual(lst.to_list(), ["1", "2", "3"])

    def test_reduce(self):
        # sum of empty list
        lst = DA_mut()
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 0)
        # sum of list
        lst = DA_mut()
        lst.from_list([1, 2, 3])
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 6)
        # size
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            lst = DA_mut()
            lst.from_list(e)
            self.assertEqual(lst.reduce(lambda state, _: state + 1, 0), lst.size)

    def test_find(self):
        lst = DA_mut()
        self.assertEqual(lst.find(1), False)
        lst = DA_mut([1, 2, 3])
        self.assertEqual(lst.find(1), True)

    def test_filter(self):
        lst = DA_mut()
        self.assertEqual(lst.filter(1), [])
        lst = DA_mut([1, 2, 3])
        self.assertEqual(lst.filter(1), [2, 3])

    def test_mconcat(self):
        lst=DA_mut()
        lst1 = [1, 2, 3]
        lst2 = [1, 2, 3]
        lst.mconcat(lst1,lst2)
        self.assertEqual(lst.to_list(), [1, 2, 3, 1, 2, 3])

    def test_remove(self):
        lst = DA_mut([1, 2, 3])
        lst.remove(1)

        self.assertEqual(lst.to_list(), [1,3])

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        lst = DA_mut()
        lst.from_list(a)
        b = lst.to_list()
        self.assertEqual(a, b)

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        lst2 = DA_mut()
        lst2.from_list(a)
        self.assertEqual(lst2.size, len(a))

    @given(st.lists(st.integers()))
    def test_monoid_identity(self,li):
        lst = DA_mut()
        lst.from_list(li)
        self.assertEqual(lst.mconcat(lst.mempty(), lst.to_list()),li)
        self.assertEqual(lst.mconcat(lst.to_list(), lst.mempty()),li)

    @given(a=st.lists(st.integers()),b=st.lists(st.integers()),c=st.lists(st.integers()))
    def test_monoid_associativity(self,a,b,c):
        lst=DA_mut()
        lst1 = DA_mut(a)
        lst2 = DA_mut(b)
        lst3= DA_mut(c)
        self.assertEqual(lst.mconcat(lst.mconcat(lst1.to_list(), lst2.to_list()),lst3),lst.mconcat(lst1,lst.mconcat(lst2.to_list(), lst3.to_list())))

    def test_iter(self):
        x = [1, 2, 3]
        lst = DA_mut()
        lst.from_list(x)
        tmp = []
        for e in lst:
            tmp.append(e)
        self.assertEqual(x, tmp)
        self.assertEqual(lst.to_list(), tmp)
        i = iter(DA_mut())
        self.assertRaises(StopIteration, lambda: next(i))


if __name__ == '__main__':
    unittest.main()
