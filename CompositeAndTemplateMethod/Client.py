'''
Created on Oct 12, 2014

@author: pjhu
'''

if __name__ == '__main__':
    from ITSComposite import ITSComposite
    from RealTc import RealTc
    tc1 = RealTc("tc1")
    tc2 = RealTc("tc2")
    tc3 = RealTc("tc3")
    
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