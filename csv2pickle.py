import csv
#from six.moves import cPickle as pickle
import pickle
import numpy as np

def main(path_csv, path_pickle):

    x = set()
    with open(path_csv,'r') as f:
        reader = csv.reader(f)
        for line in reader: x.update(line)

    with open(path_pickle,'wb') as g:
        pickle.dump(x, g)


if __name__ == '__main__':
	main('/wherever/input.00.csv', '/wherever/output.00.pickle')
	main('/wherever/input.03.csv', '/wherever/output.01.pickle')
	main('/wherever/input.02.csv', '/wherever/output.02.pickle')
	main('/wherever/input.01.csv', '/wherever/output.03.pickle')
	