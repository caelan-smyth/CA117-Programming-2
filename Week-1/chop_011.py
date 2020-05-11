import sys

def chop(s):
    return s[1:-1]

def main():
    for line in sys.stdin:
        line = line.strip()
        if len(line) > 2:
            print(chop(line))

if __name__ == "__main__":
    main()