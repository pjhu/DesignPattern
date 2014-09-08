'''
Created on 

@author: pjhu
'''

from IStaff import IStaff
class Veterinarian(IStaff):
    '''
    classdocs
    '''


    def __init__(self):
        IStaff.__init__(self)
        '''
        Constructor
        '''
    
    def veterinarian(self):
        return "veterinarian"
    
    def action(self):
        return "veterinarian_action"