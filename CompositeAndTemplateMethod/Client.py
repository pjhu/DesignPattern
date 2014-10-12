'''
Created on Oct 12, 2014

@author: pjhu
'''

if __name__ == '__main__':
    from ITSComposite import ITSComposite
    from ITCLeaf import ITCLeaf
    tc1 = ITCLeaf("tc1")
    tc2 = ITCLeaf("tc2")
    tc3 = ITCLeaf("tc3")
    
    tsRoot = ITSComposite("tsRoot")
    tsHT = ITSComposite("tsHT")
    tsLT = ITSComposite("tsLT")
    
    
    tsHV = ITSComposite("tsHV")
    tsNV = ITSComposite("tsNV")
    tsLV = ITSComposite("tsLV")
    
    
    tsHV.addChild(tc1)
    tsNV.addChild(tc1)
    tsNV.addChild(tc2)
    tsLV.addChild(tc1)
    tsLV.addChild(tc2)
    tsLV.addChild(tc3)
    
    tsHT.addChild(tsHV)
    tsHT.addChild(tsNV)
    tsHT.addChild(tsLV)
    tsHT.addChild(tc1)
    tsLT.addChild(tsHV)
    tsLT.addChild(tc2)
    tsLT.addChild(tc3)
    
    tsRoot.addChild(tsHT)
    tsRoot.addChild(tsLT)
    
    tsRoot.run()