import numpy as np
import random
import scipy.stats as ss
#def distance(p1,p2):
 #   x=np.sqrt(np.sum(np.power(p2-p1,2)))
  #  return x

def majourity_votes_short(votes):
    '''vote_counts={}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote]+=1
        else:
            vote_counts[vote]=1
    winners=[]
    max_countval=max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count==max_countval:
            winners.append(vote)'''
    mode, count= ss.mstats.mode(votes)
    return mode
            
votes=[1,2,1,2,1,2,3,3,1,2]    
winner=majourity_votes(votes)





'''
p1=np.array([1,1])
p2=np.array([4,4])
distance(p1,p2)    
'''
