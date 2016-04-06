def cross_section_diagram(lines):
    S1 = []
    S2 = []
    sum = 0

    for i in range(len(lines)):
        if lines[i] == "\\":
            S1.append(i)
        elif lines[i] == "/" and S1:
            j = S1.pop()
            area = i - j
            sum += area
            while S2 and S2[-1][0] > j:
                area += S2.pop()[1]
            S2.append([j, area])

    print(sum)
    print(len(S2), *(area for j, area in S2))


if __name__ == '__main__':
    lines = input()
    cross_section_diagram(lines)