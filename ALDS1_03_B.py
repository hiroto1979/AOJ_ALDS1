def queuing(q, processes):
    times = 0
    while len(processes):
        next_processes = []
        for i in processes:
            if q < i[1]:
                i[1] -= q
                times += q
                next_processes += [i]
            else:
                times += i[1]
                print(i[0], times)
        processes = next_processes


if __name__ == '__main__':
    n, q = [int(i) for i in input().split()]

    processes = []
    for i in range(n):
        name, time =input().split()
        processes += [[name, int(time)]]

    queuing(q, processes)
