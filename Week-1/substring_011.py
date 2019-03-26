def substring(s,t):
    return s in t

def main():
    import sys
    for line in sys.stdin:
        s = line.split()[0].casefold()
        t = line.split()[1].casefold()
        print(substring(s,t))

if __name__ == '__main__':
    main()