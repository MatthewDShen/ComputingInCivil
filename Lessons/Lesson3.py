# Truss Sloving Program

import numpy as np

# Coordinates

x1 , y1 = 3 , 4
x2 , y2 = 0 , 0
x3 , y3 = 3 , 0

# Member Lengths
def calc_length(xy1: tuple,xy2: tuple) -> float:
    """Given Coordinates of two points get distance betwen them"""
    return np.linalg.norm(np.array(xy1) - np.array((xy2)))

# Length 1 (between 2 and 3)

len1 = calc_length((x2 , y2) , (x3 , y3))

# Length 2 (between 1 and 2)

len2 = calc_length((x1 , y1) , (x2 , y2))

#Direction Cosines

def dir_cos(xy1,xy2):
    """Returns the direction cosine for a member given points and length"""

    len = calc_length(xy1,xy2)
    return (xy2[0] - xy1[0])/len, (xy2[1] - xy1[1]/len)

lx1, ly1 = dir_cos((x2,y2), (x3, y3))
lx2, ly2 = dir_cos((x2, y2), (x1, y1))
# Member 1 (btw 2 and 3)

# Member 2 (btw 1 and 2)

# print(lx1, lx2, lx3, lx4)

# Stifness Matrix
def stiff_matrix(xy1, xy2, other_dofs = None):
    """ Returns the stiffness matrix for a member, given the coordinates of 
    its near and far end nodes. Can optionally provide a tuple that includes 
    other degrees of freedom in order to compile a matrix corresponding 
    to the entire system.
    """
    length = calc_length(xy1, xy2)
    lx, ly = dir_cos(xy1, xy2)
    k = np.array(
        [
        [lx**2, lx*ly, -lx**2, -lx*ly],
        [lx*ly, ly**2, -lx*ly, -ly**2],
        [-lx**2, -lx*ly, lx**2, lx*ly],
        [-lx*ly, -ly**2, lx*ly, ly**2]
        ]
    ) / length
    
    if other_dofs:
        for i in other_dofs:
            k = np.insert(k, i-1, 0, axis=0)
            k = np.insert(k, i-1, 0, axis=1)
    
    return k

k1 = stiff_matrix((x2, y2), (x3, y3), (5, 6, ))
k2 = stiff_matrix((x2, y2), (x1, y1) (5, 6, ))

k = k1 + k2

print(k)