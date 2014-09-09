'''
Created on
@author: pjhu
'''

if __name__ == '__main__':
    from ZookeeperSubject import ZookeeperSubject
    from ZookeeperBJ import ZookeeperBJ
    from ZookeeperSH import ZookeeperSH
    
    zooS = ZookeeperSubject()
    bj = ZookeeperBJ(zooS)
    sh = ZookeeperBJ(zooS)
    
    zooS.setMethodChanged('F1', 'T1')
    zooS.setMethodChanged('F2', 'T2')
    zooS.setMethodChanged('F3', 'T3')