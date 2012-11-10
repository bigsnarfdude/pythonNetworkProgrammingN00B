# making 8 bit words of data
# bytearray is a mutable list of bytes

# remaining = number of bytes being received (determined already)
# write this in place of putting network data into a list
# or appending to some type of list with +=
# write to bytearray instead and enjoy the benefits of clean code


msg = bytearray()
while remaining > 0:
        chunk = s.recv(remaining)    # Get available data
            msg.extend(chunk)            # Add to message
                remaining -= len(chunk) 



file_input = u'٩(͡๏̯͡๏)۶'

for c in file_input:
    if ord(c) > 127:
        outbytes += bytes('&#{:04d};'.format(ord(c)))
    else: 
        outbytes.append(ord(c))
outstr = str(outbytes)
print (outstr)
