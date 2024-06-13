class SimilarityChecker:
    def check(self, str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise TypeError
        # if not str1.isalpha() or not str2.isalpha():
        #     raise TypeError
        if not str1.isupper() or not str2.isupper():
            raise TypeError

