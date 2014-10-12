'''
Created on Oct 12, 2014

@author: pjhu
'''
import unittest
from CompositeAndTemplateMethod.ITCLeaf import ITCLeaf
from mock import Mock

class Test(unittest.TestCase):


    def setUp(self):
        self.obj = ITCLeaf("tcname")
        pass

    def tearDown(self):
        del self.obj
        pass


    def test_run(self):
        self.obj.initialize = Mock()
        self.obj.process = Mock()
        self.obj.clean = Mock()
        self.obj.run()
        self.obj.initialize.assert_called_once_with()
        self.obj.process.assert_called_once_with()
        self.obj.clean.assert_called_once_with()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()