'''
Created on Sep 8, 2014

@author: pjhu
'''
from IStaff import IStaff

class Feeder(IStaff):
    '''
    classdocs
    '''


    def __init__(self):
        IStaff.__init__(self)
        '''
        Constructor
        '''
        
    def feeder(self):
        return "feeder"
    
    def action(self):
        print "Feed method..."
        return "feeder"