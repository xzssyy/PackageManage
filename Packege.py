class Package:
    """

    """



    def __init__(self, versionString):
        """

        :param args:
        """
        # versionList = [name, (symbol), versionNumber1, versionNumber2, ...]
        self.remark, self.isPontificated = self.convertVsersionAsList(versionString)
        self.name = self.remark[0]
        self.symbol = None

        if self.isPontificated:
            self.symbol = self.remark[1]
            self.versionList = self.remark[2:]
        else:
            self.versionList = self.remark[1:]




    def getVersionString(self):
        return'.'.join(self.versionList)







    def convertVersionAsList(versionString):
        versinAsList = versionString.name.split('.')

        symbol=["==", '<=', '>=']
        isPontificated = False

        for s in symbol:
            if s in versinAsList[0]:
                t = versinAsList[0].split(s)
                t.extend(versinAsList)
                versinAsList = t
                isPontificated = True
                break

        return versinAsList, isPontificated


    @classmethod
    def versionCmp(cls, v1, v2):
        if v1[0] == v2[0]:
            return Package.versionCmp(v1[1:], v2[1:])

        if v1[0] > v2[0]:
            return 1
        else:
            return 0










