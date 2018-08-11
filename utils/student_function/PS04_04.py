import numpy as np

def get_storage_order(r):
    s = []
    for i in range(len(r.shape)):
        slices = [slice(0,1,None)]*len(r.shape)
        slices[i] = slice(0,2,None)
        s.append(r[slices].flatten())
    s = np.r_[s]
    return np.argsort(s[:,-1]-s[:,0])