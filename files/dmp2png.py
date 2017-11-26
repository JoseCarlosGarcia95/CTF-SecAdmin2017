#!/usr/bin/python
import re, struct
regex = r"PNG"
data  = file('mspaint.dmp', 'r').read()

matches = re.finditer(regex, data)

i = 0
for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    
    baseaddr = match.start()
    pointer = 0
    pngdata = data[baseaddr - 1]

    pngdata += data[baseaddr:baseaddr + 7]

    baseaddr += 7
    # length
    length = data[baseaddr: baseaddr + 4]
    pngdata += length

    length  = struct.unpack("I", length)[0]

    baseaddr += 4

    # chunk type
    pngdata += data[baseaddr:baseaddr + 4]

    baseaddr += 4

    # chunk data
    pngdata += data[baseaddr:baseaddr + length]

    baseaddr += length

    # CRC
    pngdata += data[baseaddr:baseaddr + 4]

    file('dump/{}.png'.format(i), 'wb').write(pngdata)
    i += 1

    
