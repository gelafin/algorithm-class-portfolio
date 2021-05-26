# Author: Mark Mendez
# Date: 05/25/2021
# Description: Implementation of a basic pattern matcher


class PatternMatcher:
    """namespace for wildcard chars"""
    def __init__(self):
        self.match_all = '*'
        self.match_1 = '?'
        self.wildcard_chars = {self.match_all, self.match_1}


pattern_matcher = PatternMatcher()


def is_wildcard(char):
    """
    Determines whether a given char is a pattern's wildcard char
    :param char: any char of a pattern to check
    :return: True if the char is a wildcard; False if not
    """
    if char in pattern_matcher.wildcard_chars:
        return True

    return False


def get_index_of_last_non_wildcard(string):
    """
    Determines whether a given index is the index of the last char in a given string
    :param string: any string to test
    :return: True if the index is of the last char in string; False if not
    """
    # TODO: raise argument_error if invalid index
    for index in range(len(string) - 1, 0, -1):
        if string[index] not in pattern_matcher.wildcard_chars:
            # there is another non-wildcard later in the string
            return index

        index += 1


def patternmatch(string, p):
    """
    Determines whether a given pattern matches a given string
    :param string: any string to test
    :param p: string with a pattern; can include literal chars or wildcards:
              *: matches any char sequence
              ?: matches any one char
    :return: True if the pattern matches the string; False if not
    """
    MATCH_ALL = pattern_matcher.match_all
    MATCH_1 = pattern_matcher.match_1
    index_of_last_non_wildcard = get_index_of_last_non_wildcard(p)

    # scan pattern, stopping at chars
    index_string = 0
    for index_p in range(len(p)):
        if not is_wildcard(p[index_p]):
            if p[index_p] == string[index_string]:
                # chars match; step string pointer, because there's more to compare
                if index_p != index_of_last_non_wildcard:
                    index_string += 1
            elif index_p > 0:
                previous_pattern_char = p[index_p - 1]

                if previous_pattern_char == MATCH_ALL:
                    # chars don't match, but it's ok because of the match-all
                    index_string += 1
                elif previous_pattern_char == MATCH_1:
                    # probe string by 1 char; are we ok?
                    index_string += 1
                    if string[index_string] != p[index_p]:
                        # match-1 wildcard was used with no match
                        return False
            else:
                # pattern's first char doesn't match
                return False

    # handle any remaining chars in string
    if index_string < len(string) - 1:
        if p[-1] == MATCH_1:
            index_string += 1
            if index_string < len(string) - 1:
                return False
        elif p[-1] != MATCH_ALL:
            # string has unmatched chars at the end
            return False

    return True


if __name__ == '__main__':
    # test
    string = 'abcde'
    pattern = '*'
    expected = True
    result = patternmatch(string, pattern)
    if result != expected:
        print('! test 1 expected', expected, 'but got', result)

    string = 'abcde'
    pattern = '*a?c*'
    expected = True
    result = patternmatch(string, pattern)
    if result != expected:
        print('! test 2 expected', expected, 'but got', result)

    string = 'abcde'
    pattern = '*a?c'
    expected = False
    result = patternmatch(string, pattern)
    if result != expected:
        print('! test 3 expected', expected, 'but got', result)

    string = 'abcde'
    pattern = '*a?c*'
    expected = True
    result = patternmatch(string, pattern)
    if result != expected:
        print('! test 4 expected', expected, 'but got', result)

    string = 'abcde'
    pattern = 'a*'
    expected = True
    result = patternmatch(string, pattern)
    if result != expected:
        print('! test 5 expected', expected, 'but got', result)

    string = 'abcde'
    pattern = 'ae'
    expected = False
    result = patternmatch(string, pattern)
    if result != expected:
        print('! test 6 expected', expected, 'but got', result)

    string = 'abcde'
    pattern = 'ad?'
    expected = False
    result = patternmatch(string, pattern)
    if result != expected:
        print('! test 7 expected', expected, 'but got', result)

    string = 'abcde'
    pattern = 'abc?'
    expected = False
    result = patternmatch(string, pattern)
    if result != expected:
        print('! test 8 expected', expected, 'but got', result)

    string = 'abcde'
    pattern = 'abcd?'
    expected = True
    result = patternmatch(string, pattern)
    if result != expected:
        print('! test 9 expected', expected, 'but got', result)

    string = 'a'
    pattern = '?'
    expected = True
    result = patternmatch(string, pattern)
    if result != expected:
        print('! test 10 expected', expected, 'but got', result)
    pass
