'''
Created on Oct 7, 2014

@author: pjhu
'''
import unittest
from Command.ConcreteCommandClose import ConcreteCommandClose
from mock import Mock

class Test(unittest.TestCase):


    def setUp(self):
        receiver = Mock()
        self.obj = ConcreteCommandClose(receiver)
        pass


    def tearDown(self):
        del self.obj
        pass


    def test_execute(self):
        self.obj.receiver = Mock()
        self.obj.execute()
        self.obj.receiver.actionClose.assert_called_once_with()
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()