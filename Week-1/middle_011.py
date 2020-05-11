import sys

def middle(s):
    if len(s) == 1:
        return s
    elif len(s) % 2 == 1 and len(s) > 2:
        return s[len(s)//2]
    else:
        return "No middle character!"

def main():
    for line in sys.stdin:
        line = line.strip()
        if line:
            print(middle(line))

if __name__ == "__main__":
    main()