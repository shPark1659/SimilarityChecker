class SimilarityChecker:
    def check(self, str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise TypeError

