from PIL import Image
import numpy

I = (Image.open('out.png'))
red = list(I.getdata(0))
green = list(I.getdata(1))
blue = list(I.getdata(2))
#PIL doesn't like unloading in a pure RGBRGB sequence so the pure data stream has to be reconstructed manually
finlist = []
for i in range(len(red)):
    finlist.append(red[i])
    finlist.append(green[i])
    finlist.append(blue[i])
finlist = bytes(finlist) #convert to bytes-like for writing
with open('out.exe',"wb") as f:
    f.write(finlist)
input()