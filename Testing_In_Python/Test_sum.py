import unittest
def Sum(arg):
    Total =0
    for x in arg:
        Total+=x

class Test_sum(unittest.TestCase):
    def test_sum(self):
        data = [1,3,3]
        res = sum(data)
        self.assertEqual(res, 6)
    

    

if __name__ == "__main__":
    unittest.main()

