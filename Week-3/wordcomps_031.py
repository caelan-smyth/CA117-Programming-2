#!/usr/bin/env python3

import sys

vowels = 'aeiou'


def allvowels(s):
    for c in vowels:
        if not c in s:
            return False
    return True


def four_a(s):
    if s.count('a') == 4:
        return True
    else:
        return False


def two_plus_q(s):
    if 2 <= s.count('q'):
        return True
    else:
        return False


def anagram_angle(s):
    if len(s) != len('angle') or s == 'angle':
        return False
    else:
        for c in 'angle':
            if not c in s:
                return False
        return True


def most_e(l):
    words_with_e = [w for w in l if 'e' in w]
    most_es = 0
    for w in l:
        if most_es < w.count('e'):
            most_es = w.count('e')
    return [w for w in l if w.count('e') == most_es]


def main():
    l = [line.strip() for line in sys.stdin]
    print('Words containing 17 letters: {}'.format(
        [w for w in l if len(w) == 17]))
    print(
        'Words containing 18+ letters: {}'.format([w for w in l if 17 < len(w)]))
    print('Shortest word containing all vowels: {}'.format(
        min([w for w in l if allvowels(w.casefold())], key=len)))
    print('Words with 4 a\'s: {}'.format(
        [w for w in l if four_a(w.casefold())]))
    print(
        'Words with 2+ q\'s: {}'.format([w for w in l if two_plus_q(w.casefold())]))
    print('Words containing cie: {}'.format(
        [w for w in l if 'cie' in w.casefold()]))
    print('Anagrams of angle: {}'.format(
        [w for w in l if anagram_angle(w.casefold())]))
    print('Words ending in iary: {}'.format(
        len([w for w in l if w[-4:] == 'iary'])))
    print('Words with q but no u: {}'.format(
        [w for w in l if 'q' in w.casefold() and not 'u' in w.casefold()]))
    print('Words with most e\'s: {}'.format(most_e(l)))

if __name__ == '__main__':
    main()