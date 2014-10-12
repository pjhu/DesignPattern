'''
Created on Oct 12, 2014

@author: pjhu
'''
from IComponent import IComponent

class ITCLeaf(IComponent):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        IComponent.__init__(self, name)
        self.name = name
    
    def initialize(self):
        pass
    
    def process(self):
        pass
    
    def clean(self):
        pass
    
    def run(self):
        print "Run, TC Name: ", self.name
        self.initialize()
        self.process()
        self.clean()
        pass