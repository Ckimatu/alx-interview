#!/usr/bin/python3

"""
reads stdin line by line and computes metrics
"""

import sys


def print_metrics(total_size, status_codes):
    """
    print the computed metrics
    args:
	 @total_size: total file size
	 @status_codes: dictionary containing
	 the counts of each status code
    """
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))

def main():
    line_count = 0
    total_size = 0
    status_codes = {}

    try:
        for line in sys.stdin:
            line_count += 1
            data = line.split()

            if len(data) >= 8:
                """
		check if the line has at least 8 fields. we expect:
		<IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
		<status code> <file size>
		"""
                status_code = data[-2]
                file_size = data[-1]

                if status_code.isdigit() and file_size.isdigit():
                    total_size += int(file_size)

                    if status_code in status_codes:
                        status_codes[status_code] += 1
                    else:
                        status_codes[status_code] = 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
