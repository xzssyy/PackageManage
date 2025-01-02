import re

from Manager import Manager
from Packege import Package


def main_test():
    m = Manager('./custom_nodes')


def unitest_cmp():
    print(Package.version_cmp([1,2,3,4], [1, 2, 5]))



if __name__ == "__main__":
    main_test()

