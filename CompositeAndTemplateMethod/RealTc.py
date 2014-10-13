'''
Created on Oct 13, 2014

@author: pjhu
'''
from ITCLeaf import ITCLeaf

class RealTc(ITCLeaf):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        ITCLeaf.__init__(self, name)
        
    def initialize(self):
        print "TemplateMethod: Real Tc initilize"
        
    def process(self):
        print "TemplateMethod: Real Tc process"
        
    def clean(self):
        print "TemplateMethod: Real Tc clean"