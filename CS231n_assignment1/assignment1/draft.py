import numpy as np

if __name__ == '__main__':

    B = np.reshape(np.arange(6),[2,3])
    B = np.transpose(B)
    B = np.tile(B,(4,1,1))
    A = np.reshape(np.arange(12),[4,3])
    A = np.reshape(A,(4,3,1))
    C = np.sqrt(np.sum(np.square(B-A), axis = 1))
    print(C)