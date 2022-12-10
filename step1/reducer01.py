#!/usr/bin/env python3
from collections import defaultdict
import sys

sys.stdin.reconfigure(encoding='utf-8')
word_count = defaultdict(int)
for line in sys.stdin:
    try:
        line = line.strip()
        word, count = line.split()
        count = int(count)
    except:
        sys.stderr.write("%s" % (line))
        continue

    word_count[word] += count

# print(word_count)
for word, count in word_count.items():
    sys.stdout.write('%s %d\n' % (word, count))