'''
Created on

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
        type = 'F'
        rtn = 'feeder'
        real = self.obj.staff_type(type)
        self.assertEqual(rtn, real)
        
    def test_staff_type_trainer(self):
        type = 'T'
        rtn = 'trainer'
        real = self.obj.staff_type(type)
        self.assertEqual(rtn, real)
    
    def test_staff_type_veterinarian(self):
        type = 'V'
        rtn = 'veterinarian'
        real = self.obj.staff_type(type)
        self.assertEqual(rtn, real)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()