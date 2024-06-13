from unittest import TestCase

from similarity_checker import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def setUp(self):
        self.similarity_checker = SimilarityChecker()

    def assert_not_exception(self, str1, str2):
        try:
            self.similarity_checker.check(str1, str2)
            self.fail()
        except TypeError:
            pass

    def test_exception_when_input_is_none(self):
        self.assert_not_exception('ABC', None)
        self.assert_not_exception(None, 'ABC')
