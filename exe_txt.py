
#reads an exe and returns a list of 1 byte ints
def read_exe(fp):
    out = numpy.array() #new 1-d array construct to feed data into
    with open(fp,"rb") as f:
        for line in f:
            for char in line:
                numpy.append(out,char)
    return out

#TESTING USE ONLY
if __name__ == "__main__":
    import numpy
    fp = 'F:\\Spews of creativity\\pyshit\\bad-format-converters\\Firefox.exe'
    read_exe(fp)