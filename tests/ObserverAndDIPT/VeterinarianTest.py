'''
Created on Sep 8, 2014

@author: pjhu
'''
import unittest
from ObserverAndDIP.Veterinarian import Veterinarian



class Test(unittest.TestCase):


    def setUp(self):
        self.obj = Veterinarian()
        pass


    def tearDown(self):
        del self.obj
        pass

    def test_veterinarian(self):
        rtn = "veterinarian"
        real = self.obj.veterinarian()
        self.assertEqual(rtn, real)
        pass
    
    def test_action(self):
        rtn = "veterinarian"
        real = self.obj.action()
        self.assertEqual(rtn, real)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()