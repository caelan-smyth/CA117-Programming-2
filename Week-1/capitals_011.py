import sys

def capitals(s):
    return s[0].upper() + s[1:-1] + s[-1].upper()

def main():
    for line in sys.stdin:
        line = line.strip()
        if len(line) >= 2:
            print(capitals(line))

if __name__ == "__main__":
    main()