 # Imports

import numpy as np

# Coordinates:
x1, y1 = 3, 4
x2, y2 = 0, 0
x3, y3 = 3, 0

# Member lengths

# Member 1 (btw nodes 2 and 3)
len1 = np.linalg.norm(np.array((x2, y2)) - np.array((x3, y3)))

# Member 2 (btw nodes 2 and 1)
len2 = np.linalg.norm(np.array((x2, y2)) - np.array((x1, y1)))

print('Length 1:', len1, '\nLength 2:', len2)

def calc_length(xy1: tuple, xy2: tuple) -> float:
    """ Given the coordinates of two points, it will calculate the
    distance between the two points.
    """
    return np.linalg.norm(np.array(xy1) - np.array(xy2))

len1 = calc_length((x2, y2), (x3, y3))
len2 = calc_length((x1, y1), (x2, y2))

print('Length 1:', len1, '\nLength 2:', len2)

def dir_cos(xy1, xy2):
    """ Returns the direction cosine for a member given point coordinates.
    """
    l = calc_length(xy1, xy2)
    return (xy2[0] - xy1[0])/l, (xy2[1] - xy1[1])/l

lx1, ly1 = dir_cos((x2, y2), (x3, y3))
lx2, ly2 = dir_cos((x2, y2), (x1, y1))

print(lx1, ly1, lx2, ly2)

def stiff_matrix(xy1, xy2):
    """ Returns the stiffness matrix for a member, given the coordinates of 
    its near and far end nodes.
    """
    length = calc_length(xy1, xy2)
    lx, ly = dir_cos(xy1, xy2)
    return np.array(
        [
        [lx**2, lx*ly, -lx**2, -lx*ly],
        [lx*ly, ly**2, -lx*ly, -ly**2],
        [-lx**2, -lx*ly, lx**2, lx*ly],
        [-lx*ly, -ly**2, lx*ly, ly**2]
        ]
    ) / length

k1 = stiff_matrix((x2, y2), (x3, y3))
k2 = stiff_matrix((x2, y2), (x1, y1))

print(k1, '\n')
print(k2)

def stiff_matrix(xy1, xy2, other_dofs=None):
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
k2 = stiff_matrix((x2, y2), (x1, y1), (3, 4, ))

print(k1, '\n')
print(k2)