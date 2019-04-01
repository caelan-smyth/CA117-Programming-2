def camelcase(lst):
    strlst = []
    for s in lst:
        s = s.capitalize()
        strlst.append(s)
    return " ".join(strlst).strip()

def main():
    import sys
    for line in sys.stdin:
        lines = line.split()
        print(camelcase(lines))

if __name__ == '__main__':
    main()