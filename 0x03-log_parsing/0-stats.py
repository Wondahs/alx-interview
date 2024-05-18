#!/usr/bin/python3
'''reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)

After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order'''
import re
import sys
from collections import Counter


status_code_dict = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }
total_filesize = 0
count = 0
result = []
try:
    for line in sys.stdin:
        pattern = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - (\[\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2}\.\d{6}\]) (\"GET \/projects\/260 HTTP\/1.1\" \w* \w*)$"
        if re.match(pattern, line):
            split_content = line.split()
            status_code = split_content[-2]
            if type(eval(status_code)) is not int:
                continue
            file_size = split_content[-1]
            if status_code in status_code_dict:
                status_code_dict[status_code] += 1
            total_filesize += int(file_size) if type(eval(file_size)) is int else 0
            count += 1
            if count % 10 == 0:
                print("File size:",total_filesize)
                for key, value in status_code_dict.items():
                    if value > 0:
                        print(f"{key}: {value}")
                result = []
except (KeyboardInterrupt, EOFError):
    print("File size:",total_filesize  if total_filesize else "")
    print(f"{key}: {value}"  if (key and value) else "")
