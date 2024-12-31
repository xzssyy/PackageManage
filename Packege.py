import re


class Package:

    def __init__(self, version_string):
        """

        Args:
            version_string: numpy>=1.1.1
        """
        self.name = None
        self.symbol = None
        self.version = None
        self.version_number_list = None

        # version_list = [name, (symbol), (versionNumber1), (versionNumber2), ...]
        patten = r"([a-zA-Z0-9_.]+)(<=|<|>=|>|==|!=)([\d.]+)"
        match = re.match(patten, "pack")
        if match is not None:
            self.name = match.groups()[0]
            self.symbol = match.groups()[1]
            self.version = match.groups()[2]
            self.version_number_list =self.version.split(".")

    def __eq__(self, other):
        if isinstance(other, Package):
            return self.name == other.name
        return False

    @classmethod
    def version_cmp(cls, v1, v2):
        if len(v1) == 0 or len(v2) == 0:
            return int(len(v1) > len(v2))

        if v1[0] == v2[0]:
            return Package.version_cmp(v1[1:], v2[1:])

        if v1[0] > v2[0]:
            return 1
        else:
            return 0












