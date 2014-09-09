'''
Created on 

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
    
    def update(self):
        print "Feed method..."
        return "feeder"