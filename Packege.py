import re


class Package:

    def __init__(self, version_string):
        """

        Args:
            version_string: numpy>=1.1.1
        """
        # version_list = [name, (symbol), (versionNumber1), (versionNumber2), ...]
        patten = r"([a-zA-Z0-9_.]+)+(<=|<|>=|>|==|!=)*([\d.]+)*"
        match = re.match(patten, version_string)
        self.name = match.group(0)
        self.symbol = match.group(1)
        self.version = match.group(2)
        self.version_number_list =self.version.split(",") if self.version else []

    def __eq__(self, other):
        if isinstance(other, Package):
            return self.name == other.name
        return False

    @classmethod
    def version_cmp(cls, v1, v2):
        if v1[0] == v2[0]:
            return Package.version_cmp(v1[1:], v2[1:])

        if v1[0] > v2[0]:
            return 1
        else:
            return 0












