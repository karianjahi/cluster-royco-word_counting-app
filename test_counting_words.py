"""
This is the testing environment for the counting_words app
Any test must begin with the word test
Any Class that is meant to be tested must begin with Test
We use the module `pytest` to test our application
Installing it: `pip3 install pytest`
pip3 ensures we pull pytest that is python3-compliant
"""
from counting_words import WordCounter

class TestWordCounter:
    """
    This class tests the counting_words app
    """
    def test_blank(self):
        """
        counting zero words
        :return:
        """
        text = ""
        assert WordCounter().count_words(text) == 0

    def test_single_word(self):
        """
        testing single word
        :return:
        """
        text = "python"
        assert WordCounter().count_words(text) == 1

    def test_multiple_words(self):
        """
        Testing multiple words
        :return: None
        """
        text = "python is easy to learn"
        assert WordCounter().count_words(text) == 5

    def test_html(self):
        """
        Testing whether we can count words
        entrapped in html tags
        :return: None
        """
        text = '<p> python is easy to learn </p>'
        assert WordCounter().count_words(text) == 5


    def test_html_with_attrs(self):
        """
        Testing whether we can count words
        entrapped in html tags
        :return: None
        """
        text = '<p class="special-headers"> python is easy to learn </p>'
        assert WordCounter().count_words(text) == 5




