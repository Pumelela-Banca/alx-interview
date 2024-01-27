#!/usr/bin/python3
"""
Logs stdin operations by using inputs from
other files
"""
import sys
import re


def print_statistics(total_size, status_code_counts):
    """
    print format
    """
    print(f"File size: {total_size}")
    for code in status_code_counts.keys():
        if status_code_counts[code] == 0:
            continue
        print(code, ": ",status_code_counts[code], sep="")


line_number = 0
codes = [200, 301, 400, 401, 403, 404, 405, 500]
sum_all = 0
times = []
n_of_counts = {f"{x}": 0 for x in codes}
try:
    for line in sys.stdin:

        if line_number == 10:
            print_statistics(sum_all, n_of_counts)
            line_number = 0
        line_number += 1
        args = line.split()
        if len(args) not in [8, 9]:
            continue
        if not re.match(
                r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$",
                args[0]):
            # not ip match
            continue
        spc = " "
        if args[4] + spc + args[5] + spc + args[6] \
                + spc != '"GET /projects/260 HTTP/1.1" ':
            continue
        if args[1] != "-":
            continue
        if not re.match(
                r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))",
                args[2].lstrip("[")):
            # not date match
            continue
        sum_all += int(args[-1])
        if len(args) == 8:
            continue
        if not args[-2].isdigit():
            continue
        n_of_counts[args[-2]] += 1
except KeyboardInterrupt:
    print_statistics(sum_all, n_of_counts)
    sys.exit(0)
