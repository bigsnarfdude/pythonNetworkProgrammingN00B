# making 8 bit words of data
# bytearray is a mutable list of bytes

file_input = u'٩(͡๏̯͡๏)۶'

for c in file_input:
    if ord(c) > 127:
        outbytes += bytes('&#{:04d};'.format(ord(c)))
    else: 
        outbytes.append(ord(c))
outstr = str(outbytes)
print (outstr)
