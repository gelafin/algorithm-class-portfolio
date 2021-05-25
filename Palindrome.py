# Author: Mark Mendez
# Date: 05/24/2021
# Description: Two implementations of k-palindrome solutions with different time complexities


class PalindromeInputError(Exception):
    """Exception raised when caller input is invalid"""


def is_valid_palindrome_input(string):
    """
    Determines whether a given string meets validation requirements for the cs325 portfolio assignment
    :param string: any string to test
    :return: True if the string is valid input; False if not
    """
    if len(string) < 1:
        return False

    # string passed all checks
    return True


def is_palindrome(string):
    """
    Determines whether a given string is a palindrome or not
    :param string: any non-empty string to test
    :return: True if the string is a palindrome; False if not
    """
    if not is_valid_palindrome_input(string):
        raise PalindromeInputError

    # traverse string inwards from both ends
    index_left = 0
    index_right = -1
    while len(string) > index_left >= index_right:
        # compare this pair of chars
        if string[index_left] != string[index_right]:
            return False

        index_left += 1
        index_right -= 1

    # string passed the check
    return True


def checkPalindrome_1(string, k):
    """
    Determines whether a given string is a k-palindrome or not
    A k-palindrome string is a string that becomes a palindrome when 0-k characters are removed
    BRUTE FORCE implementation
    :param string: any non-empty string to test
    :param k: int for the number of allowed character removals
    :return: True if the string is a k-palindrome; False if not
    """
    if not is_valid_palindrome_input(string):
        raise PalindromeInputError

    # special case: no characters need to be removed to form a palindrome
    if is_palindrome(string):
        return True

    # try every possible permutation of string and see if any is a palindrome
    for substring_length in range(1, k + 1):  # convert to 1-based
        for slice_start_index in range(len(string)):
            slice_end_index = slice_start_index + substring_length
            test_string = string[0:slice_start_index] + string[slice_end_index:None]
            if is_palindrome(test_string):
                return True

    # no palindrome found in above check
    return False


def checkPalindrome_2(string, k):
    """
    Determines whether a given string is a k-palindrome or not
    A k-palindrome string is a string that becomes a palindrome when 0-k characters are removed
    OPTIMIZED implementation
    :param string: any non-empty string to test
    :param k: int for the number of allowed character removals
    :return: True if the string is k-palindrome; False if not
    """
    if not is_valid_palindrome_input(string):
        raise PalindromeInputError

    # traverse string inwards from both ends
    index_left = 0
    index_right = -1
    while len(string)//2 >= index_left >= index_right:
        # compare this pair of chars
        if string[index_left] != string[index_right]:
            # try moving each index inward up to k times
            is_mirror = False
            step = 1
            while is_mirror is False and step <= k:
                # LTR
                index_left_probe = index_left + step
                if string[index_left_probe] == string[index_right]:
                    index_left = index_left_probe
                    k -= step  # k gets "used up"
                    is_mirror = True
                    continue

                # RTL
                index_right_probe = index_right - step
                if string[index_right_probe] == string[index_left]:
                    index_right = index_right_probe
                    k -= step  # k gets "used up"
                    is_mirror = True
                    continue

                step += 1

            if is_mirror is False:
                # mirror broke, and using k couldn't restore mirror
                return False

        index_left += 1
        index_right -= 1

    # passed test
    return True


if __name__ == '__main__':
    # test input validation
    # print('expecting Exception', is_palindrome(''))

    # some mild tests for is_palindrome helper
    # print('expecting True', is_palindrome('aba'))
    # print('expecting True', is_palindrome('abba'))
    # print('expecting False', is_palindrome('abc'))
    # print('expecting False', is_palindrome('abfdba'))

    # some mild tests for brute force solution
    # print('check 1: expecting True', checkPalindrome_1('aba', 0))
    # print('check 2: expecting True', checkPalindrome_1('aba', 1))
    # print('check 3: expecting True', checkPalindrome_1('aba', 2))
    # print('check 4: expecting True', checkPalindrome_1('aba', 3))
    # print('check 5: expecting True', checkPalindrome_1('abba', 0))
    # print('check 6: expecting True', checkPalindrome_1('abba', 1))
    # print('check 7: expecting True', checkPalindrome_1('abba', 2))
    # print('check 8: expecting True', checkPalindrome_1('abba', 3))
    # print('check 9: expecting True', checkPalindrome_1('abba', 4))
    # print('check 10: expecting True', checkPalindrome_1('abba', 5))
    # print('check 11: expecting False', checkPalindrome_1('abc', 0))
    # print('check 12: expecting False', checkPalindrome_1('abc', 1))
    # print('check 13: expecting True', checkPalindrome_1('abc', 2))
    # print('check 14: expecting True', checkPalindrome_1('abc', 3))
    # print('check 15: expecting True', checkPalindrome_1('abc', 4))
    # print('check 16: expecting False', checkPalindrome_1('abfdba', 0))
    # print('check 17: expecting True', checkPalindrome_1('abfdba', 1))
    # print('check 18: expecting True', checkPalindrome_1('abfdba', 6))
    # print('check 19: expecting True', checkPalindrome_1('abfdba', 7))

    # some mild tests for optimized solution
    # print('check 1: expecting True', checkPalindrome_2('aba', 0))
    # print('check 2: expecting True', checkPalindrome_2('aba', 1))
    # print('check 3: expecting True', checkPalindrome_2('aba', 2))
    # print('check 4: expecting True', checkPalindrome_2('aba', 3))
    # print('check 5: expecting True', checkPalindrome_2('abba', 0))
    # print('check 6: expecting True', checkPalindrome_2('abba', 1))
    # print('check 7: expecting True', checkPalindrome_2('abba', 2))
    # print('check 8: expecting True', checkPalindrome_2('abba', 3))
    # print('check 9: expecting True', checkPalindrome_2('abba', 4))
    # print('check 10: expecting True', checkPalindrome_2('abba', 5))
    # print('check 11: expecting False', checkPalindrome_2('abc', 0))
    # print('check 12: expecting False', checkPalindrome_2('abc', 1))
    # print('check 13: expecting True', checkPalindrome_2('abc', 2))
    # print('check 14: expecting True', checkPalindrome_2('abc', 3))
    # print('check 15: expecting True', checkPalindrome_2('abc', 4))
    # print('check 16: expecting False', checkPalindrome_2('abfdba', 0))
    # print('check 17: expecting True', checkPalindrome_2('abfdba', 1))
    # print('check 18: expecting True', checkPalindrome_2('abfdba', 6))
    # print('check 19: expecting True', checkPalindrome_2('abfdba', 7))

    pass
