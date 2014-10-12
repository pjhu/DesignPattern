'''
Created on Oct 12, 2014

@author: pjhu
'''

class IComponent(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
    
    def addChild(self, child):
        raise Exception("No Implemented!")
        pass
    
    def removeChild(self, child):
        raise Exception("No Implemented!")
        pass
    
    def getChild(self):
        raise Exception("No Implemented!")
        pass
    
    def initialize(self):
        raise Exception("No Implemented!")
        pass
    
    def process(self):
        raise Exception("No Implemented!")
        pass
    
    def clean(self):
        raise Exception("No Implemented!")
        pass
    
    def run(self):
        raise Exception("No Implemented!")
        pass
    