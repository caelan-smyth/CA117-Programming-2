import sys


def sorter(t):
    return t[1]


def main():
    food_cal = {}
    with open(sys.argv[1], 'r') as f:
        for line in f:
            tokens = line.strip().split()
            foodstuff = ' '.join(tokens[:-1])
            calories = tokens[-1]
            food_cal[foodstuff] = int(calories)

    total_cals_per_person = {}
    for line in sys.stdin:
        line = line.strip().split(',')
        name = line[0]
        consumed_food = line[1:]

        total = 0
        for food in consumed_food:
            try:
                total += food_cal[food]
            except KeyError:
                total += 100
        total_cals_per_person[name] = total

    for t in sorted(total_cals_per_person.items(), key=sorter):
        print('{:>{}s} : {:>{}d}'.format(t[0], len(max(total_cals_per_person.keys(), key=len)), t[1], len(str(max(total_cals_per_person.values())))))

if __name__ == '__main__':
    main()