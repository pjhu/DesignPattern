'''
Created on Oct 7, 2014

@author: pjhu
'''

from ICommand import ICommand

class ConcreteCommandOpen(ICommand):
    '''
    classdocs
    '''


    def __init__(self, receiver):
        '''
        Constructor
        '''
        ICommand.__init__(self)
        self.receiver = receiver
        
    def execute(self):
        self.receiver.actionOpen()