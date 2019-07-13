import unittest
from task2 import MySimpleIter

class testMySimpleter(unittest.TestCase):

    def setUp(self):
        print('start')

    def test_SimpleIter(self):
        extected = [2, 3, 5, 7, 11, 13, 17, 19]
        result = [i for i in MySimpleIter(20)]
        self.assertCountEqual(extected, result)
        self.assertListEqual(extected,result)

if __name__ == '__main__':
    unittest.main()
