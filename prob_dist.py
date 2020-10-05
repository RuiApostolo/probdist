import argparse
import numpy as np
import matplotlib.pyplot as plt

def read_file(ifile: object, ofile: object, bin_size: float) -> object:
    size = (2, 3)
    coords = np.zeros(size, dtype=float)
    d = []

    with open(ifile) as f:
        next(f)
        next(f)
        while True:
            line = f.readline()
            if not line:
                break
            else:
                data = line.split()
                coords[0, :] = data[1:]
                line = f.readline()
                data = line.split()
                coords[1, :] = data[1:]
                d.append(distance(coords))
                try:
                    next(f)
                    next(f)
                except StopIteration:
                    distances = np.array(d, dtype=float)
                    result, bin_edges = pofr(distances, bin_size)
                    # with open(ofile, "w") as g:
                    #     g.write(str(result))
    return



def distance(c):
    r = np.sqrt((c[0, 0]-c[1, 0])**2+(c[0, 1]-c[1, 1])**2+(c[0, 2]-c[1, 2])**2)
    return(r)

def pofr(d, bin_size):
    # bin_array = np.array([], dtype=float)
    # b = []
    # for i in d:
    #     bin = round(i/bin_size) + 1
    #     b.append(bin)
    # bin_array = np.array(b, dtype=float)
    # hist, bin_edges = np.histogram(bin_array)
    # return hist, bin_edges

    # print(hist)
    # print(bin_edges)
    hist, bin_edges = np.histogram(d, bins=int((d.max()-d.min())/bin_size), density=True)
    z = plt.hist(d, density=True, bins=int((d.max()-d.min())/bin_size))  # arguments are passed to np.histogram
    plt.show()
    return hist, bin_edges

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate the p(r) for xyz file with only 2 atoms')
    parser.add_argument('--input', '-i', help='Path to the input xyz file', required=True)
    parser.add_argument('--output', '-o', help='Path to the output p(r) file', default='pr.dat')
    parser.add_argument('--bin_size', '-b', help='Bin size. Default = 0.1', default='0.1')

    args = parser.parse_args()

    read_file(args.input, args.output, float(args.bin_size))