#!/usr/bin/python3
"""
Logs stdin operations by using inputs from
other files
"""

import sys


def print_statistics(total_size, status_code_counts):
    """
    print format
    """
    print(f"File size: {total_size}")
    for code in sorted(status_code_counts):
        print(f"{code}: {status_code_counts[code]}")


line_number = 0
codes = [200, 301, 400, 401, 403, 404, 405, 500]
sum_all = 0
times = []
n_of_counts = {}
try:
    for line in sys.stdin:
        args = line.split()
        sum_all += int(args[-1])
        times.append(int(args[-2]))
        line_number += 1

        if line_number % 10 == 0:
            for i in sorted(times):
                if i is None or not isinstance(i, int):
                    continue
                if i in n_of_counts and i in codes:
                    n_of_counts[i] += 1
                else:
                    n_of_counts[i] = 1
            print_statistics(sum_all, n_of_counts)
            times.clear()
except KeyboardInterrupt:
    print_statistics(sum_all, n_of_counts)
    sys.exit(0)
