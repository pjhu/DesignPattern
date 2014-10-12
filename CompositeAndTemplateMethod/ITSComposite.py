'''
Created on Oct 12, 2014

@author: pjhu
'''
from IComponent import IComponent

class ITSComposite(IComponent):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        IComponent.__init__(self, name)
        self.name = name
        self.tclist = []
    
    def addChild(self, child):
        self.tclist.append(child)
        pass
    
    def removeChild(self, child):
        if child in self.tclist:
            self.tclist.remove(child)
        pass
    
    def getChild(self):
        return self.tclist
        pass
    
    def initialize(self):
        pass
    
    def process(self):
        for tc in self.tclist:
            tc.run()
        pass
    
    def clean(self):
        pass
    
    def run(self):
        print "Run, TS Name: ", self.name
        self.initialize()
        self.process()
        self.clean()
        pass
    
