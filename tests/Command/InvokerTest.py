'''
Created on Oct 7, 2014

@author: pjhu
'''
import unittest
from Command.Invoker import Invoker
from mock import Mock

class Test(unittest.TestCase):


    def setUp(self):
        self.obj = Invoker()
        pass


    def tearDown(self):
        pass

    def test_setCommand(self):
        commandDict = {"CMD":"cmd object"}
        self.obj.setCommand("CMD", "cmd object")
        self.assertEqual(self.obj.commandDict, commandDict)
        pass
    
    def test_buttonWasPushed(self):
        self.obj.commandDict["CMD"] = Mock()
        self.obj.buttonWasPushed("CMD")
        self.obj.commandDict["CMD"].execute.assert_called_once_with()
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()