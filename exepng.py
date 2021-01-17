import math, numpy
from PIL import Image
fp = 'F:\\Spews of creativity\\pyshit\\bad-format-converters\\setup-stub.exe'
arr = [] #NOTE: list appends are much faster than numpy appends
with open(fp,"rb") as f:
    for line in f:
        for val in line:
            arr.append(val)
arr = numpy.array(arr,dtype=numpy.uint8)
len_to_add = 3 - len(arr)%3 # append 0-2 zeros at the end of last pixel 
arr = numpy.append(arr,numpy.zeros(len_to_add,dtype=numpy.uint8))#fill zeros to cover for last pixel
arr = numpy.reshape(arr,(int(len(arr)/3),3))
arr_len = numpy.shape(arr)[0] 
side_len = math.ceil(math.sqrt(arr_len)) #pixel len
add_zeros = side_len**2-arr_len
arr = numpy.append(arr,numpy.zeros((add_zeros,3),dtype=numpy.uint8),axis=0)
arr = numpy.reshape(arr,(side_len,side_len,3))
out = Image.fromarray(arr,"RGB")
out.save("out.png")