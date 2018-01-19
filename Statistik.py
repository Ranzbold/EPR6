import FormatUtils
class Statistik(object):
    """Class which provides methods for statistical analysis of texts"""
    inputpath = ""
    wordcount = 0
    charcount = 0

    def __init__(self, inputpath):
        self.inputpath = inputpath

    def get_wordcount(self):
        words = 0
        lines = FormatUtils.get_lineswithoutblank(self.inputpath)
        for line in lines:
            words += len(line.split())
        self.wordcount = words
        return self.wordcount

    def get_charcount(self):
        chars = 0
        lines = FormatUtils.get_lineswithoutblank(self.inputpath)
        for line in lines:
            chars += sum(len(word) for word in line)
        return chars

    def get_avglength(self):
        average = 0
        lengthsum = 0
        lines = FormatUtils.get_lineswithoutblank(self.inputpath)
        for line in lines:
            words = line.split()
            lengthsum += sum(len(word) for word in words)
        average = lengthsum / self.get_wordcount()
        return average




