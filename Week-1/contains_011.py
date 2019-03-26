def contains(s,t):
    for c in s:
        if c in t:
            t = t.replace(c,"",1)
        elif c not in t:
            return False
    return True

def main():
    import sys
    for line in sys.stdin:
        s = line.split()[0].casefold()
        t = line.split()[1].casefold()

        print(contains(s,t))

if __name__ == '__main__':
    main()