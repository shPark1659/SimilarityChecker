class SimilarityChecker:
    def check_valid(self, str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise TypeError
        if not str1.isupper() or not str2.isupper():
            raise TypeError

    def calc(self, str1, str2):
        score = 0
        self.check_valid(str1, str2)
        return score