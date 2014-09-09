'''
Created on Sep 8, 2014

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
    
    def update(self):
        print "Veterinarian method..."
        return "veterinarian"