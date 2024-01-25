#!/usr/bin/python3
"""
Logs stdin operations
"""
import sys
import re
from collections import defaultdict


def print_metrics(file_size, status_codes):
    print(f'File size: {file_size}')
    for code in sorted(status_codes.keys()):
        print(f'{code}: {status_codes[code]}')


def main():
    file_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            match = re.match(
                r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$', line.strip())
            if match:
                status_code, size = match.groups()
                file_size += int(size)
                status_codes[status_code] += 1
                line_count += 1
            if line_count % 10 == 0:
                print_metrics(file_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(file_size, status_codes)
        sys.exit(0)
