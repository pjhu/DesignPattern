'''
Created on 

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
    
    def action(self):
        return "trainer_action"