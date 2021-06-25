#!/usr/bin/python3
import argparse
import numpy as np
import matplotlib.pyplot as plt

from math import floor, ceil
from decimal import Decimal


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
                    filename = ''.join(
                        ofile.replace(
                            '../',
                            '').split('.')[
                            :-1])
                    extension = ''.join(ofile.split('.')[-1])
                    with open(filename + '_raw.' + extension, 'w') as o:
                        for item in d:
                            o.write("%s\n" % item)
                    distances = np.array(d, dtype=float)
                    result, bin_edges = pofr(distances, bin_size)
                    with open(filename + '.' + extension, 'w') as o:
                        txt = "{bin_c:8.6f} \t {val:8.6f} \n"
                        o.write(
                            "# bin_center \t value \t bin_size = {} \n".format(
                                bin_size))
                        for value, edge in zip(result, bin_edges[:-1]):
                            o.write(
                                txt.format(
                                    val=value,
                                    bin_c=(edge + float(bin_size) / 2.0)))
    return


def distance(c):
    r = np.sqrt((c[0, 0]-c[1, 0])**2+(c[0, 1]-c[1, 1])**2+(c[0, 2]-c[1, 2])**2)
    return(r)


def round_down(div, *args):
    result = []
    for i in args:
        # Decimal reduces error chance from binary fractions
        # round precision of 5 should be enough for all reasonable bins
        # consider using something like:
        # https://stackoverflow.com/questions/6189956/easy-way-of-finding-decimal-places
        result.append(round(div * floor(float(Decimal(str(i)))/div), 5))
    return result


def pofr(d, bin_size):
    # find lowest datapoint
    d_min = d.min()
    # round_down to bin multiple
    d_min = round_down(bin_size, d_min)[0]
    # create bins
    n_bins = int(ceil((d.max()-d_min)/bin_size))
    # get d.max()
    d_max = (d_min + n_bins * bin_size)
    # create histogram
    hist, bin_edges = np.histogram(d,
                                   bins=n_bins,
                                   range=(d_min, d_max),
                                   density=True)
    # arguments are passed to np.histogram
    plt.hist(d, density=True, bins=n_bins, range=(d_min, d_max))
    plt.title("N-N p(r)")
    plt.xlabel("r")
    plt.ylabel("p(r)")
    plt.savefig(
        "{0}.png".format(
            args.output.replace(
                "../",
                "").replace(
                ".dat",
                "")))
    #  fig.show()
    return hist, bin_edges


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Generate the p(r) for an xyz file with only 2 atoms')
    parser.add_argument(
        '--input',
        '-i',
        help='Path to the input xyz file',
        required=True)
    parser.add_argument(
        '--output',
        '-o',
        help='Path to the output p(r) file',
        default='pr.dat')
    parser.add_argument(
        '--bin_size',
        '-b',
        help='Bin size. Default = 0.1',
        default='0.1')

    args = parser.parse_args()

    read_file(args.input, args.output, float(args.bin_size))
