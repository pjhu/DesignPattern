'''
Created on Sep 9, 2014

@author: pjhu
'''


class ISubject(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def registerObserver(self, observer):
        pass
    
    def removeObserver(self, observer):
        pass
    
    def notifyObserver(self):
        pass