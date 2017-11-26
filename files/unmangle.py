#!/usr/bin/python

data = file('mangle', 'r').read()

items = data.split('\n')

values = []

for item in items:
    if item != '':
        values.append(int(item, 0))


string = ''
for value in values:
    string += chr(value - 53)

print string
