from unittest import TestCase

from similarity_checker import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def setUp(self):
        self.similarity_checker = SimilarityChecker()

    def test_exception_when_input_is_none(self):
        with self.assertRaises(TypeError):
            self.similarity_checker.check(None, 'ABC')
