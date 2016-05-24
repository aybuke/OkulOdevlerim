#!/usr/bin/env python
#-*- coding: utf-8 -*-
import random
def generateRow():
    result = ''
    for i in range(10):
        result += str(random.randint(0,1))
        if i < 9:
            result += ','
    return result
def generate():
    result = ''
    for at in range(10):
        result += '%s\n' % generateRow()
    with open('tablo.txt', 'w') as f:
        f.write('header-1,header-2,header-3,header-4,header-5,header-6,header-7,header-8,header-9,header-10\n%s' % result)
    return result
def rowsAndCols():
    with open('tablo.txt') as f:
        content = f.readlines()
    headers = content[0].split(',')
    a = content[1:11]
    rows = []
    for row in a:
        items = row.replace('\n','').split(',')
        rows.append(items)
    cols = [list(i) for i in zip(*rows)]
    return rows, cols
def all_true(subset):
    for item in subset:
        if not item:
            return False
    return True
def match(num):
    rows, cols = rowsAndCols()
    c = []
    for row in rows:
        c.append(list(map(int, row)))
    rows = c
    matches = []
    for row in rows:
        if not matches:
            matches = list(0 for i in range(len(row) - num + 1))
        i = 0
        while i + num <= len(row):
            if all_true(row[i:i+num]):
                matches[i] += 1
            i += 1
    return matches, max(matches)
if __name__ == '__main__':
    #generate()
    #rows, cols = rowsAndCols()
    #for row in rows:
    #    print(row)
    #print()
    for i in range(1, 11):
        m, maxm = match(i)
        print('%sx matches:' % str(i))
        print(m)
        print('Max: %s' % str(maxm))
        print()
