#!/usr/bin/env python3
from collections import defaultdict
import sys

sys.stdin.reconfigure(encoding='utf-8')
# pagename_dic = defaultdict(int)
# page_date_dic = defaultdict(int)
# page_count_dic = defaultdict(int)
# sum_dic = defaultdict(int)
# diff_dic = defaultdict(int) 

pagename_prev = ""
page_date_prev = ""
page_count_prev = ""
sum_prev = 0
diff_prev = 0

def combine_lists(list1, list2):
    return list1[:-1] + "," + list2[1:]

for line in sys.stdin:
    try:
        line = line.strip()
        pagename, page_date, page_count, sum, diff = line.split('\t')
        sum = int(sum)
        diff = int(diff)
    except:
        sys.stderr.write("ERROR %s" % (line))
        continue

    if pagename_prev == pagename:
        # print("DEBUG_INFO: case 1")
        page_date_prev = combine_lists(page_date_prev, page_date)
        page_count_prev = combine_lists(page_count_prev, page_count)
        sum_prev = sum_prev + sum
        diff_prev = diff_prev + diff
    else:
        # print("DEBUG_INFO: case 2")
        pagename_prev = pagename
        page_date_prev = page_date
        page_count_prev = page_count
        sum_prev = sum
        diff_prev = diff
        sys.stdout.write('%s\t%s\t%s\t%d\t%d\n' % 
                    (pagename_prev,
                    page_date_prev, 
                    page_count_prev,
                    sum_prev, diff_prev))

sys.stdout.write('%s\t%s\t%s\t%d\t%d\n' % 
                (pagename_prev,
                page_date_prev, 
                page_count_prev,
                sum_prev, diff_prev))