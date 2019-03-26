def capitals(s):
    return (s[0].upper() + s[1:-1] + s[-1].upper())

def main():
    import sys
    for line in sys.stdin:
        if len(line) > 2:
            print(capitals(line.strip()))

if __name__ == '__main__':
    main()