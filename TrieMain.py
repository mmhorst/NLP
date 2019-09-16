import sys
import glob
from TrieNode import TrieNode

def main ():
    root = TrieNode("*")
    fname = sys.argv[1]

    with open(fname, 'r', encoding = 'utf8') as fi:
        for line in fi.readlines():
            root.add(line)

    route = sys.argv[2]
    fnames = glob.glob(route + "test_d*")
    print(fnames)
    for fname in fnames:
        print(fname)
        with open(fname, 'r', encoding = 'utf8') as file:
            root.search(file)

if __name__ == '__main__':
    main()
