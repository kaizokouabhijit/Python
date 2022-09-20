import unittest
from Sum import sum

class Test_sum(unittest.TestCase):
    def test_sum(self):
        data = [1,2,3]
        res = sum(data)
        self.assertEqual(res, 6)
    

    

if __name__ == "__main__":
    unittest.main()

