import sys

def main():
    place = 'POS'
    club = 'CLUB'
    p = 'P'
    won = 'W'
    draw = 'D'
    lost = 'L'
    gf = 'GF'
    ga = 'GA'
    gd = 'GD'
    points = 'PTS'

    clubs = []
    lines = []

    for line in sys.stdin:
        clubs.append(" ".join(line.split()[1:-8]).strip())
        lines.append(line)

    longest = 0
    for e in clubs:
        if len(e) > longest:
            longest = len(e)

    print('{:>3s} {:{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(place, club, longest, p, won, draw, lost, gf, ga, gd, points))

    for line in lines:
        a = line.split()
        place = a[0]
        club = " ".join(a[1:-8]).strip()
        p = a[-8]
        won = a[-7]
        draw = a[-6]
        lost = a[-5]
        gf = a[-4]
        ga = a[-3]
        gd = a[-2]
        points = a[-1]

        print('{:>3s} {:{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(place, club, longest, p, won, draw, lost, gf, ga, gd, points))

if __name__ == '__main__':
    main()