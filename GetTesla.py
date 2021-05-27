# Author: Mark Mendez
# Date: 05/27/2021
# Description: Implements a shortest-path function with the special constraints of the class assignment


import math
from GetTeslaHelpers import *


def get_tesla_neighbors(node):
    """
    Gets all neighbors of a given node which are valid in a *reversed* "GetTesla" puzzle path
    :param node: tuple of ints for x and y coordinates
    :return: list of tuples of ints for x and y coordinates; list of all valid neighbor nodes
             If the node has no valid neighbors, returns an empty list
    """
    x, y = node
    list_out = list()

    # subtract 1 in both directions and return if valid
    if x - 1 >= 0:
        step_right = (x - 1, y)
        list_out.append(step_right)

    if y - 1 >= 0:
        step_down = (x, y - 1)
        list_out.append(step_down)

    return list_out


def get_tesla_recursive(current_node, M, max_hp_table):
    """
    Calculates the max hp possible at the destination node of a GetTesla puzzle
    Recursive helper for GetTesla
    :param current_node: tuple of ints for x and y coordinates
    :param M: list of lists of ints for the matrix with its nodes' values
    :param max_hp_table: list of lists of ints for the max hp possible at each node
    :return: int for the max hp possible at the destination node
    """
    # base case: reached the starting node
    if current_node == (0, 0):
        return M[0][0]

    current_node_x, current_node_y = current_node
    current_node_hp = M[current_node_y][current_node_x]

    # get the max HP possible from both neighbors and use the higher one
    current_node_max_hp = -math.inf  # guarantee overwrite
    for neighbor_node in get_tesla_neighbors(current_node):
        neighbor_node_x, neighbor_node_y = neighbor_node

        # get neighbor's max hp from memo or calculate it for the first time
        if max_hp_table[neighbor_node_x][neighbor_node_y] is None:
            neighbor_max_hp = get_tesla_recursive(neighbor_node, M, max_hp_table)
        else:
            neighbor_max_hp = max_hp_table[neighbor_node_x][neighbor_node_y]

        # use the greater max hp of both neighbors
        total_hp_from_neighbor = neighbor_max_hp + current_node_hp
        current_node_max_hp = max(current_node_max_hp, total_hp_from_neighbor)
        return current_node_max_hp


def getTesla(M):
    """
    Calculates the minimum health points needed to traverse the input matrix from top-left to bottom-right, where
        positive node values increase health, and
        negative node values decrease health
    :param M: list of lists of ints for the matrix with its nodes' values
    :return: int of the minimum health points needed to traverse the matrix
    """
    # keep a table of results for max hp possible at each node
    # initialize to guarantee overwrite on first comparison
    max_hp_table = [[None for _ in range(len(M[0]))] for _ in range(len(M))]
    max_hp_table[0][0] = M[0][0]

    destination_node = len(M[0]) - 1, len(M) - 1
    destination_node_max_hp = get_tesla_recursive(destination_node, M, max_hp_table)

    return calculate_min_survival_hp(destination_node_max_hp)


if __name__ == '__main__':
    # test
    m = [[-1, -2, 2], [10, -8, 1], [-5, -2, -3]]
    expected = 2
    result = getTesla(m)
    if (result != expected):
        print('test 1 expected', expected, 'but got', result)
