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

#print('Length 1:' , len1 , '\nLength2:' , len2)

#Direction Cosines

def dir_cos(xy1,xy2):
    """Returns the direction cosine for a member given points and length"""

    len = calc_length(xy1,xy2)
    return (xy2[0] - xy1[0]/len, xy2[1] - xy1[1]/len)

# Member 1 (btw 2 and 3)

# Member 2 (btw 1 and 2)

# print(lx1, lx2, lx3, lx4)

# Stifness Matrix
def stiff_matrix(xy1, xy2):
    """Return the stiffness matrix for a member given the """
    
    length = calc_length(xy1, xy2)
    lx, ly = dir_cos(xy1, xy2)

    k1 = np.array(
        [lx1**2, lx1*ly1, -lx1**2, -lx1*ly1],
        [lx1*ly1, ly1**2, -lx1*ly1, -ly1**2],
        [-lx1**2 , -lx1*ly1 , lx1**2 , lx1*ly1]
        [-lx1*ly1, -ly1**2, lx1*ly1, ly1**2]
    ) / length



