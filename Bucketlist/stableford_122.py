
import sys

lines = []
par = {}
index = {}
totals_dict = {}
disqualified = []

score_to_par = {-7: 9,
                -6: 8,
                -5: 7,
                -4: 6,
                -3: 5,
                -2: 4,
                -1: 3,
                0: 2,
                1: 1,
                2: 0}


def stableford_points(scores, handicap):
    points = 0
    for n in range(18):
        if scores[n] == 'X':
            continue
        elif not scores[n].isdigit() and scores[n] != 'X':
            return 'Disqualified'
        else:
            free_shots = 0
            hcap = handicap
            while index[n] <= hcap:
                free_shots += 1
                hcap = hcap - 18
            net_strokes = int(scores[n]) - free_shots
            par_score = net_strokes - par[n]
            if 2 < par_score:
                par_score = 2
            points += score_to_par[par_score]
    return points


def main():
    for line in sys.stdin:
        lines.append(line.strip())

    for n in range(18):
        par[n] = int(lines[0].split()[n])
        index[n] = int(lines[1].split()[n])

    longest_name = 0
    totals_list = []

    for line in lines[2:]:
        name = ' '.join(line.split()[:-19])
        if longest_name < len(name):
            longest_name = len(name)
        handicap = int(line.split()[-19])
        scores = line.split()[-18:]
        if stableford_points(scores, handicap) == 'Disqualified':
            disqualified.append(name)
        else:
            totals_list.append(stableford_points(scores, handicap))
            totals_dict[stableford_points(scores, handicap)] = name

    totals_list = sorted(totals_list, reverse=True)

    for points in totals_list:
        print('{:>{}} : {:>2d}'.format(
            totals_dict[points], longest_name, points))
    for player in disqualified:
        print('{:>{}} : Disqualified'.format(player, longest_name))


if __name__ == '__main__':
    main()