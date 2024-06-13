class SimilarityChecker:
    def check_valid(self, str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise TypeError
        if not str1.isupper() or not str2.isupper():
            raise TypeError

    def calc(self, str1, str2):
        score = 0
        self.check_valid(str1, str2)

        short, long = (len(str2), len(str1)) if len(str1) >= len(str2) else (len(str1), len(str2))
        if short == long:
            score += 60
        elif long >= short * 2:
            pass
        else:
            score += int(60 * (2 * short - long) / short)
        return score




