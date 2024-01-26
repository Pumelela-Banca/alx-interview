#!/usr/bin/python3
"""
Logs stdin operations by using inputs from
other files
"""
import sys
import re
from collections import defaultdict


def main():
    """
    listens to stdin and prints results
    """
    file_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            match = re.match(
                r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$',
                line.strip())

            if match and int(line.strip().split(" ")[-2]) in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_code, size = match.groups()
                file_size += int(size)
                status_codes[status_code] += 1
                line_count += 1

            if line_count % 10 == 0:
                print(f'File size: {file_size}')
                for code in sorted(status_codes.keys()):
                    print(f'{code}: {status_codes[code]}')

    except KeyboardInterrupt:
        print(f'File size: {file_size}')
        for code in sorted(status_codes.keys()):
            print(f'{code}: {status_codes[code]}')
        sys.exit(0)


main()
