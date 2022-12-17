#!/usr/bin/env python3 
from collections import defaultdict
import os 
import sys 
import string 
import urllib.parse

sys.stdin.reconfigure(encoding='utf-8')

def list_to_string(list):
    output = '['
    for i in list:
        output = output + i + ', '
    output = output[:-2]
    output = output + ']'
    return output

def count_sum(page_count):
    sum = 0
    for c in page_count:
        sum = sum + int(c)
    return sum

def count_diff(page_date, page_count):
    diff = 0
    for i in range(len(page_date)):
        if page_date[i].endswith("01"):
            diff -= int(page_count[i])
        elif page_date[i].endswith("02"):
            diff -= int(page_count[i])
        elif page_date[i].endswith("03"):
            diff += int(page_count[i])
        elif page_date[i].endswith("04"): 
            diff += int(page_count[i])
        elif page_date[i].endswith("05"): 
            diff += int(page_count[i])
    return diff

page_date = defaultdict(list)
page_count = defaultdict(list)
 
for line in sys.stdin:
    try:
        line = line.strip()
        key, count = line.split('\t')
        pagename, date = key.split('}')
    except:
        continue

    page_date[pagename].append(date)
    page_count[pagename].append(count)

for pagename, count in page_date.items():
    sys.stdout.write('%s\t%s\t%s\t%d\t%d\n' % 
                    (pagename,
                    list_to_string(page_date[pagename]), 
                    list_to_string(page_count[pagename]), 
                    count_sum(page_count[pagename]),
                    count_diff(page_date[pagename], page_count[pagename])))