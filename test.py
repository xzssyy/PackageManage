import re

from Manager import Manager
from Packege import Package


def main_test():
    m = Manager('./custom_nodes')


def unitest_cmp():
    p1 = Package("numpy>=1.2.3.4")
    p2 = Package("numpy>=1.2.5")

    print(Package.version_cmp(p2, p2))



if __name__ == "__main__":
    main_test()

