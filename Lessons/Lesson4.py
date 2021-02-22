#import libraries
import numpy as np
from numpy.lib.shape_base import _kron_dispatcher

#Stiffness Functions
def calc_length(xy1: tuple, xy2: tuple) -> float:
    """ Given the coordinates of two points, it will calculate the
    distance between the two points.
    """
    return np.linalg.norm(np.array(xy1) - np.array(xy2))

def dir_cos(xy1, xy2):
    """ Returns the direction cosine for a member given point coordinates.
    """
    l = calc_length(xy1, xy2)
    return (xy2[0] - xy1[0])/l, (xy2[1] - xy1[1])/l

def element_stiff_matrix(xy1, xy2, other_dofs=None):
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

# Rule: we are storing in (x,y) format
node_a = {
    'coord': (0,6),
    'dof' : (1,2),
    'force' : (150,0),
    'displ' : [None, None]
}

node_b = {
    'coord': (4,4),
    'dof' : (1,2),
    'force' : (0,0),
    'displ' : [None, None]
}

node_c = {
    'coord': (12,0),
    'dof' : (5,6),
    'force' : [0,None],
    'displ' : [None,0]
}

node_d = {
    'coord': (0,0),
    'dof' : (7,8),
    'force' : [None,None],
    'displ' : [0,0]
}

node_e = {
    'coord': (4,0),
    'dof' : (9,10),
    'force' : (0,120),
    'displ' : [None,None]
}

nodes = [
    node_a,
    node_b,
    node_c,
    node_d,
    node_e
]

members = [
    (node_a,node_b),
    (node_a,node_b),
    (node_b,node_d),
    (node_b,node_e),
    (node_b,node_c),
    (node_c,node_e),
    (node_e,node_d)
]

#Calculate the element stiffness matrix for each member

k = np.zeros((10, 10))

for member in members:
    n1, n2 = member
    all_dof = [i for i in range(1, 2*len(nodes)+1)]
    member_dof = n1['dof'] + n2['dof']
    other_dofs = [i for i in all_dof if i not in member_dof]
    k_i = element_stiff_matrix(n1['coord'], n2['coord'], other_dofs=other_dofs)

    k += k_i

print(k)

def global_stiff_matrix(nodes, members):
    """ It returns the global stiffness matrix given a list of members
    and their nodes, formated as:

    members = [
        (node_a, node_b),
        (node_a, node_d),
        (node_b, node_d),
        (node_b, node_e),
        (node_b, node_c),
        (node_c, node_e),
        (node_e, node_d)
    ]

    and each node as:

    node_a = {
        'coord': (0, 6),
        'dof': (1, 2),
        'force': (150, 0),
        'displ': [None, None]
    }
    """

    k = np.zeros((2*len(nodes), 2*len(nodes)))

    for member in members:
        n1, n2 = member
        all_dof = [i for i in range(1, 2*len(nodes)+1)]
        member_dof = n1['dof'] + n2['dof']
        other_dofs = [i for i in all_dof if i not in member_dof]
        k_i = element_stiff_matrix(n1['coord'], n2['coord'], other_dofs=other_dofs)

        k += k_i

    return k

    for node in nodes:
        print(node['force'])