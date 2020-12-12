# Still need to add a lowercase version of fully uppercase words #
# Still need to add a first letter uppercase,
# or str.title() version of the fully lowercase words #

import io
import glob
from pathlib import Path

class SpellCheck():
    def __init__(self, name : str):
        self.words = self.__loadDictionaryWords__(name)

    def check(self, s : str) -> bool:
        if s in self.words:
            return True
        else:
            return False

    def __loadDictionaryWords__(self,name: str):
        if (self.__checkDictionary__(name)):
            return self.__readIn__(name)
        else:
            raise FileNotFoundError("Make sure you entered file's name correctly")

    def __checkDictionary__(self, name: str) -> bool:
        L = glob.glob(str(Path(__file__).parent)+ "/dictionaries/*.dic")
        if name.replace(".dic","") in [Path(l).name.replace(".dic","") for l in L]:
            for i in range(len(L)):
                if name.replace(".dic","") == Path(L[i]).name.replace(".dic",""):
                    self.PathToFile = Path(L[i])
                    return True
            return True
        else:
            return False

    def __readIn__(self,name : str):
        with open(str(self.PathToFile), mode="r", encoding="utf-8") as f:
            L = [l.replace("\n","") for l in f.readlines()]
        return L

if __name__ == "__main__":
    import sys
    checker = SpellCheck("en_US")
    print(checker.check(sys.argv[1]))


