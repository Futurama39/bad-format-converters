#Takes in a 1D Array of 1 Byte per member and outs a square image from it
def txt_png(np_array):
    numpy.append(np_array,numpy.zeros((math.ceil(math.sqrt((len(np_array)))))^2-len(np_array)))
    numpy.transpose(np_array,(math.sqrt(len(np_array)),math.sqrt(len(np_array))))
    out = Image.fromarray(np_array)
    out.save("out.png")
if __name__ == "__main__":
    import math
    import numpy
    from PIL import Image
    txt_png(numpy.zeros((100,)))