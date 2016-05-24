#!/usr/bin/env python
#-*-coding: utf-8-*-

import os
import random

# Dummy data generator class.
class Generator(object):

    # Initial method to define global variables.
    # This method automatically called when the class initialized.
    def __init__(self):
        self.tables      = ['universite','fakulte','bolum',
                            'ogrenci','akademisyen','ders']
        self.letters     = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.columns     = ['id','name','phone','address','email']
        self.columnTypes = ['integer_auto_increment', 'string',
                            'phone', 'text', 'email']
        self.tld         = ['com','net','org']
        self.minLength   = 3
        self.maxLength   = 12

    # Generates random word in length between 'minLength' and 'maxLength'.
    def generateWord(self):
        randomLength = random.randint(self.minLength, self.maxLength)
        result = ""
        for i in range(randomLength):
            randomIndex = random.randrange(len(self.letters))
            if i is 0:
                result += self.letters[randomIndex]
            else:
                result += self.letters[randomIndex].lower()
        return result

    # Generates random phone number.
    def generatePhoneNumber(self):
        return "+90%s" % str(random.randint(1000000000, 9999999999))

    # Generates random e-mail address ending with one of the 'tld'.
    def generateEmailAddress(self):
        randomIndex = random.randrange(len(self.tld))
        return "%s@%s.%s" % (self.generateWord().lower(),
                             self.generateWord().lower(),
                             self.tld[randomIndex])

    # Generates random address.
    def generateAddress(self):
        randomLength = random.randint(self.minLength, self.maxLength)
        result = ""
        for i in range(randomLength):
            if i is 0:
                result += "%s " % self.generateWord()
            elif i is randomLength - 1:
                result += "%s" % self.generateWord().lower()
            else:
                result += "%s " % self.generateWord().lower()
        return result

    # Clears the file content and puts a row as column for a specific table.
    def createTable(self, table):
        f = open("%s.txt" % table, "w")
        row = ""
        for i in range(len(self.columns)):
            row += self.columns[i]
            if i < len(self.columns) - 1:
                row += "::"

        if table is 'fakulte':
            row += '::universiteId'
        elif table is 'bolum':
            row += '::fakulteId'
        elif table is 'ogrenci':
            row += '::bolumId'
        elif table is 'akademisyen':
            row += '::bolumId'
        elif table is 'ders':
            row += '::bolumId'

        row += '\n'

        f.write(row)
        f.close()

    # Calls 'createTable' for each table in 'tables' list.
    def createTables(self):
        for i in range(len(self.tables)):
            self.createTable(self.tables[i])

    # Returns a random ID which placed in the table given.
    def getRandomId(self, table):
        f = open("%s.txt" % table, "r")
        content = f.readlines()
        f.close()
        return random.randint(0, len(content) - 2)

    # Generates a row and appends it to the table given.
    def insertRow(self, table):
        f = open("%s.txt" % table, "a+")
        row = ""

        ct = self.columnTypes

        if table is 'universite':
            columnRange = len(self.columnTypes)
        else:
            columnRange = len(self.columnTypes) + 1
            ct = ['integer_auto_increment', 'string',
                  'phone', 'text', 'email', 'foreign_key']

        for i in range(columnRange):
            f.seek(0, os.SEEK_SET)
            content = f.readlines()
            c = content[0].replace('\n', '').split('::')
            lastLine = content[len(content) - 1].replace('\n', '').split('::')
            try:
                lastId = int(lastLine[0])
                newId = lastId + 1
            except ValueError:
                newId = 0

            if ct[i] is 'integer':
                row += str(random.randint(1, 100000))
            elif ct[i] is 'integer_auto_increment':
                row += str(newId)
            elif ct[i] is 'string':
                row += self.generateWord()
            elif ct[i] is 'phone':
                row += self.generatePhoneNumber()
            elif ct[i] is 'text':
                row += self.generateAddress()
            elif ct[i] is 'email':
                row += self.generateEmailAddress()
            elif ct[i] is 'foreign_key':
                if table is 'fakulte':
                    row += str(self.getRandomId('universite'))
                elif table is 'bolum':
                    row += str(self.getRandomId('fakulte'))
                elif table is 'ogrenci':
                    row += str(self.getRandomId('bolum'))
                elif table is 'akademisyen':
                    row += str(self.getRandomId('bolum'))
                elif table is 'ders':
                    row += str(self.getRandomId('bolum'))

            if i < columnRange - 1:
                row += "::"
            else:
                row += "\n"

        f.write(row)
        f.close()

    # Inserts dummy data to the tables given in 'tables' list.
    def insertDummyData(self):
        for i in range(len(self.tables)):
            for j in range(random.randint(5, 50)):
                self.insertRow(self.tables[i])


# Query builder class.
class QueryBuilder(object):

    def __init__(self):
        self.g = Generator()
        self.acceptableCommands = ['SELECT']
        self.acceptableFroms    = ['FROM']
        self.acceptableWheres   = ['WHERE']
        self.syntaxError = 'Undefined SQL query!'
        self.tableNotFoundException = 'Table not found!'
        self.columnNotFoundException = 'Column not found!'

    def getByColumn(self, table, dataColumn):
        f = open("%s.txt" % table, "r")
        content = f.readlines()
        f.close()
        result = "\n"
        for i in range(len(content)):
            col = 0
            firstRow = content[0].replace('\n', '').split('::')
            for j in range(len(firstRow)):
                if firstRow[j] == dataColumn:
                    col = j
                    break
            result += "%s\n" % content[i].replace('\n', '').split('::')[col]
        result += "\n"
        return result

    def getByColumnWithWhere(self, table, column, whereCase):
        f = open("%s.txt" % table, "r")
        content = f.readlines()
        f.close()
        result = "\n"
        # for i in range(len(content)):
        #     col = 0

    def makeQuery(self):
        self.query = input("Query: ")
        result = ""
        splittedQuery = self.query.replace(';', '').split(' ')

        if len(splittedQuery) < 4:
            return self.syntaxError

        command = splittedQuery[0].upper()
        if command not in self.acceptableCommands:
            return self.syntaxError

        fromCase = splittedQuery[2].upper()
        if fromCase not in self.acceptableFroms:
            return self.syntaxError

        if len(splittedQuery) is 5:
            return self.syntaxError
        elif len(splittedQuery) > 5:
            whereCase = splittedQuery[4].upper()
            if whereCase not in self.acceptableWheres:
                return self.syntaxError

        data = splittedQuery[1]
        table = splittedQuery[3]

        if table not in self.g.tables:
            return self.tableNotFoundException

        # if whereCase:

        if data is '*':
            f = open("%s.txt" % table, "r")
            content = f.readlines()
            f.close()
            result = "\n"
            for i in range(len(content)):
                result += content[i].replace("::", ", ")
            result += "\n"
            return result

        if '.' in data and ',' in data:
            f = open("%s.txt" % table, "r")
            content = f.readlines()
            f.close()
            result = '\n'
            splittedData = data.split(',')
            for data in splittedData:
                param = data.split('.')
                dataTable = param[0]
                dataColumn = param[1]
                if dataTable not in self.g.tables:
                    return self.tableNotFoundException
                if dataColumn not in self.g.columns:
                    return self.columnNotFoundException
                result += self.getByColumn(dataTable, dataColumn)
            return result

        if '.' in data:
            splittedData = data.split('.')
            dataTable = splittedData[0]
            dataColumn = splittedData[1]

            if dataTable not in self.g.tables:
                return self.tableNotFoundException

            if dataColumn not in self.g.columns:
                return self.columnNotFoundException

            return self.getByColumn(table, dataColumn)

        return self.getByColumn(table, data)
