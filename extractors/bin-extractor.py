'''
Accepts any file in binary data, arguably accepts any file, however there's no data decompression of other
'''
def extract(fileobj):
    #Expects a file object to read from
    #Returns a list of bytes (but not of bytes type)
    out = [] #NOTE : lists writes are much faster than numpy appends
    for line in fileobj:
        for val in line:
            out.append(val) #expected to be 'int' type
    return out