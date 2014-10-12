'''
Created on Oct 7, 2014

@author: pjhu
'''
import unittest
from Command.ReceiverAC import ReceiverAC

class Test(unittest.TestCase):


    def setUp(self):
        self.obj = ReceiverAC()
        pass


    def tearDown(self):
        del self.obj
        pass


    def test_actionOpen(self):
        pass
    
    def test_actionClose(self):
        pass
    
    def test_actionAddTemp(self):
        self.obj.temp = -2
        self.obj.actionAddTemp()
        self.assertEqual(self.obj.temp, -1)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()