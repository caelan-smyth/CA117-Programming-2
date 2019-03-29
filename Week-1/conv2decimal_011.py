def conv2decimal(x,n):
    return int(x, n)

def main():
    import sys
    for line in sys.stdin:
        line = line.strip()
        print(conv2decimal(line.split()[0],int(line.split()[1])))
    
if __name__ == '__main__':
    main()