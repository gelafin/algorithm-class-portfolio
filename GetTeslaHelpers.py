# Author: Mark Mendez
# Date: 05/27/2021
# Description: Defines helper methods shared between bottom-up and top-down solutions to GetTesla


def calculate_min_survival_hp(destination_max_hp):
    """
    Calculates min hp needed to survive a GetTesla puzzle given the max hp possible at the destination
    Helper for GetTesla functions
    :param destination_max_hp: int for the max hp possible at the destination
    :return: int for the min hp needed to survive the puzzle
    """
    if destination_max_hp > 0:
        # no health is needed
        return 0
    else:
        # return difference from 1 hp (which is min hp to live)
        return 1 - destination_max_hp

