import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Provide the filename')
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, 'r') as f:

        batches = [[]]
        for line in f:
            line = line.strip()
            if not line:
                print('{}: {}'.format(sum(batches[-1]), batches[-1]))
                batches.append([])
            else:
                batches[-1].append(int(line))

    sums = [sum(b) for b in batches]
    top = sorted(sums, reverse = True)[:3]
    print('Top: {}'.format(top))
    print('Sum: {}'.format(sum(top)))
