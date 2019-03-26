def middle(s):
    return s[(len(s)//2)]

def main():
    import sys
    for line in sys.stdin:
        if len(line.strip())%2:
            print(middle(line.strip()))
        else:
            print("No middle character!")

if __name__ == '__main__':
    main()