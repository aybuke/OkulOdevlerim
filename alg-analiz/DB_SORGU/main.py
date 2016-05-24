#!/usr/bin/env python
#-*-coding: utf-8-*-

import random
from aybuke import Generator, QueryBuilder

def main():
    generator = Generator()
    qb = QueryBuilder()
    generator.createTables()
    generator.insertDummyData()
    print(qb.makeQuery())

if __name__ == '__main__':
    main()
