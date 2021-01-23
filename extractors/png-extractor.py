from PIL import Image

def extract(im):
    #Expected a file object that contains a png image
    #returns a list of bytes in RGBRGB sequence
    im = Image.open(im)
    red = list(im.getdata(0))
    green = list(im.getdata(1))
    blue = list(im.getdata(2))
    #PIL doesn't like unloading in a pure RGBRGB sequence so the pure data stream has to be reconstructed manually
    finlist = []
    for i in range(len(red)):
        finlist.append(red[i])
        finlist.append(green[i])
        finlist.append(blue[i])
    finlist = bytes(finlist) #convert to bytes-like for writing 
    return finlist
