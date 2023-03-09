# Your task is to determine if two nodes are adjacent 
# in an undirected graph when given the adjacency matrix 
# and the two nodes."""
#
# Refence: https://edabit.com/challenge/3DAkZHv2LZjgqWbvW

def is_adjacent(matrix,node1,node2):
    if matrix[node1][node2] == 1:
        return True
    return False

if __name__ == '__main__':

    matrix = [[ 0, 1, 0, 0 ],
              [ 1, 0, 1, 1 ],
              [ 0, 1, 0, 1 ],
              [ 0, 1, 1, 0 ]]

    node1 = 0
    node2 = 1
    print(f">>> {node1} and {node2} are adjacent: ",is_adjacent(matrix,node1,node2))
    
    node1 = 0
    node2 = 2
    print(f">>> {node1} and {node2} are adjacent: ",is_adjacent(matrix,node1,node2))
