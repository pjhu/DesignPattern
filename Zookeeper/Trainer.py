'''
Created on Sep 8, 2014

@author: pjhu
'''

from IStaff import IStaff
class Trainer(IStaff):
    '''
    classdocs
    '''


    def __init__(self):
        IStaff.__init__(self)
        '''
        Constructor
        '''
    
    def trainer(self):
        return "trainer"
    
    def update(self):
        print "Train method..."
        return "trainer"