# Author: Mark Mendez
# Date: 05/25/2021
# Description: Implements a shortest-path function with the special constraints of the class assignment


import math
from queue import SimpleQueue
from GetTeslaHelpers import *


def get_tesla_neighbors(node, highest_x, highest_y):
    """
    Gets all neighbors of a given node which are valid in a "GetTesla" puzzle path
    :param highest_x: int for the highest valid x-coordinate
    :param highest_y: int for the highest valid y-coordinate
    :param node: tuple of ints for x and y coordinates
    :return: list of tuples of ints for x and y coordinates; list of all valid neighbor nodes
             If the node has no valid neighbors, returns an empty list
    """
    x, y = node
    list_out = list()

    # add 1 in both directions and return if valid
    if x + 1 <= highest_x:
        step_right = (x + 1, y)
        list_out.append(step_right)

    if y + 1 <= highest_y:
        step_down = (x, y + 1)
        list_out.append(step_down)

    return list_out


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
    max_hp_table = [[-math.inf for _ in range(len(M[0]))] for _ in range(len(M))]
    max_hp_table[0][0] = M[0][0]

    # fill the max hp table by visiting every valid node
    itinerary = SimpleQueue()
    itinerary.put((0, 0))  # nodes stored as (x, y) coordinates
    debug_count = 0
    while itinerary.qsize() > 0:
        current_node = itinerary.get()
        current_x, current_y = current_node
        current_node_max_hp = max_hp_table[current_x][current_y]
        debug_count += 1

        for neighbor in get_tesla_neighbors(current_node, len(M[0]) - 1, len(M) - 1):
            neighbor_x, neighbor_y = neighbor
            neighbor_hp = M[neighbor_y][neighbor_x]

            # calculate max hp to reach each neighbor
            total_hp_from_current_node = current_node_max_hp + neighbor_hp

            if total_hp_from_current_node > max_hp_table[neighbor_x][neighbor_y]:
                # this neighbor's path is the new best
                max_hp_table[neighbor_x][neighbor_y] = total_hp_from_current_node
                itinerary.put(neighbor)

    print('debug count', debug_count)

    final_max_hp = max_hp_table[len(max_hp_table[0]) - 1][len(max_hp_table) - 1]
    return calculate_min_survival_hp(final_max_hp)


if __name__ == '__main__':
    # test
    m = [[-1, -2, 2], [10, -8, 1], [-5, -2, -3]]
    expected = 2
    result = getTesla(m)
    if (result != expected):
        print('test 1 expected', expected, 'but got', result)


