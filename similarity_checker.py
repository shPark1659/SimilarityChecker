class SimilarityChecker:
    def check_valid(self, str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise TypeError
        if not str1.isupper() or not str2.isupper():
            raise TypeError

    def calc(self, str1, str2):
        score = 0
        self.check_valid(str1, str2)
        score += self.check_length(str1, str2)
        return score

    def check_length(self, str1, str2):
        short = min(len(str1), len(str2))
        long = max(len(str1), len(str2))
        return int(min(1, max(0, (2 * short - long) / short)) * 60)
