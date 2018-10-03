# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import re
result = []

while True:
    input_str = input()
    if input_str != 'END':
        date_regex = r"([0-9]{2,4})(\/|-|년)([0-9]{1,2})(\/|-|월)([0-9]{1,2})(일)?"
        is_match = re.search(date_regex, input_str)
        if is_match:
            date_string = is_match.group(0)
            year = int(is_match.group(1) if len(is_match.group(1)) == 2 else is_match.group(1)[2:])
            month = int(is_match.group(3)[1:] if is_match.group(3).startswith('0') else is_match.group(3))
            day = int(is_match.group(5)[1:] if is_match.group(5).startswith('0') else is_match.group(5))

            result.append([(year, month, day), input_str])
    else:
        break

result.sort(key=lambda x: x[0])
for r in result:
    print(r[1])