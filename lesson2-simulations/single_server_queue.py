from random import expovariate, gauss, seed
from statistics import mean, median, stdev

if __name__ == '__main__':

    average_arrival_interval = 5.6
    average_service_time = 4.8
    stdev_service_time = .5

    num_waiting = 0
    arrivals = []
    starts = []
    arrival = service_end = 0.0

    seed(42)
    arrival_flag = False

    ITERATIONS = 10  # 20000

    for i in range(ITERATIONS):
        if arrival <= service_end:
            num_waiting += 1
            arrival += expovariate(1.0 / average_arrival_interval)
            arrivals.append((f'{arrival:.1f}', num_waiting))
            arrival_flag = True
        else:
            num_waiting -= 1
            service_start = service_end if num_waiting else arrival
            service_time = gauss(average_service_time, stdev_service_time)
            service_end = service_start + service_time
            starts.append((f'{service_start:.1f}-{service_time:.1f}-{service_end:.1f}', num_waiting))
        print(f'it:{i:d} wait:{num_waiting:d}', end='')
        print(' arrival') if arrival_flag else print()
        arrival_flag = False

    print(arrivals)
    print(starts)

    # waits = [start - arrival for arrival, start in zip(arrivals, starts)]
    # print(f'Mean wait: {mean(waits):.1f} Stdev wait: {stdev(waits):.1f}')
    # print(f'Median wait: {median(waits):.1f} Max wait: {max(waits):.1f}')


