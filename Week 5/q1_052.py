import sys


def main():
    word = sys.argv[1]
    N = int(sys.argv[2]) % len(word)
    print(word[-N:] + word[:-N])

if __name__ == '__main__':
    main()