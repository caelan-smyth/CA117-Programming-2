def chop(s):
    if len(s) > 2:
        return s[1:-1]

def main():
    import sys
    for line in sys.stdin:
        print(chop(line.strip()))

if __name__ == '__main__':
    main()
