'''
Created on Sep 8, 2014

@author: pjhu
'''
import unittest
from Zookeeper.SimpleZookeeper import SimpleZookeeper

class Test(unittest.TestCase):
    def setUp(self):
        self.obj = SimpleZookeeper()
        pass

    def tearDown(self):
        del self.obj
        pass

    def test_staff_type_feeder(self):
        T = 'F'
        rtn = 'feeder'
        real = self.obj.staff_type(T)
        self.assertEqual(rtn, real)
        
    def test_staff_type_trainer(self):
        T = 'T'
        rtn = 'trainer'
        real = self.obj.staff_type(T)
        self.assertEqual(rtn, real)
    
    def test_staff_type_veterinarian(self):
        T = 'V'
        rtn = 'veterinarian'
        real = self.obj.staff_type(T)
        self.assertEqual(rtn, real)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()