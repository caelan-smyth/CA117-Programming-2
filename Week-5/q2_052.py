import sys

vowels = ['a', 'e', 'i', 'o', 'u']


def main():
    for line in sys.stdin:
        s = line.strip().casefold()
        vowel_chars = []
        for c in s:
            if c in vowels:
                vowel_chars.append(c)

        if vowel_chars == vowels:
            print(line.strip())

if __name__ == '__main__':
    main()