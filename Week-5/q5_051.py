import sys

def seconds(t):
    minutes, seconds = t.split(':')
    total = int(minutes) * 60 + int(seconds)
    return total

def sorter(t):
    return seconds(t[1])

def main():
    d = {}
    for line in sys.stdin:
        try:
            tokens = line.strip().split()
            d[tokens[0]] = min(tokens[1:], key=seconds)
        except ValueError:
            continue

    winner = min(d.items(), key=sorter)
    print('{} : {}'.format(winner[0], winner[1]))

if __name__ == '__main__':
    main()