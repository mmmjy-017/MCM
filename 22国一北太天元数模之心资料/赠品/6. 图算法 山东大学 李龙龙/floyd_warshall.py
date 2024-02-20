import numpy as np

D = np.array([[0,10,5,999,999],[999,0,2,1,999],[999,3,0,9,2],[999,999,999,0,4],[7,999,999,6,0]])

n = D.shape[0]


# Algorithm implementation
def floyd_warshall(distance,nV):

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return(distance)


Res = floyd_warshall(D,n)
