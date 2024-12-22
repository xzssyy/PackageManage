class Package:

    def __init__(self, version_string):
        """

        Args:
            version_string: numpy>=1.1.1
        """
        # version_list = [name, (symbol), versionNumber1, versionNumber2, ...]
        self.version_list = self.convert_version_as_list(version_string)
        self.name = self.version_list[0]
        self.symbol = self.version_list[1]
        self.version_number_list = self.version_list[2:]


    def __eq__(self, other):
        if isinstance(other, Package):
            return self.name == other.name
        return False


    def get_version_as_string(self):
        return '.'.join(self.version_number)


    @classmethod
    def convert_version_as_list(cls, version_string):
        """
        将记录转换为字符串的列表
        Args:
            version_string: numpy>=1.1.1

        Returns:
            [package_name, symbol, version_number1, version_number2, ...]
        """
        version_as_list = version_string.name.split('.')

        symbol_list=["==", '<=', '>=']

        for s in symbol_list:
            if s in version_as_list[0]:
                t = version_as_list[0].split(s)
                return [*t, *version_as_list[1:]]

        version_as_list = [version_as_list[0], None, *version_as_list[1]]
        return version_as_list


    @classmethod
    def version_cmp(cls, v1, v2):
        if v1[0] == v2[0]:
            return Package.version_cmp(v1[1:], v2[1:])

        if v1[0] > v2[0]:
            return 1
        else:
            return 0












