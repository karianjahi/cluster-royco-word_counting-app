"""
This script counts words in a string
"""

from bs4 import BeautifulSoup


class WordCounter:
    """
    This is the class that counts words
    """

    def __init__(self):
        """
        This is the class constructor method
        """
        pass

    def count_words(self, text):
        """
        This is the method that counts words
        :param text: str - The sentence
        :return: int
        """
        text = self.run_text_through_html_filter(text)
        text_split = text.split()
        return len(text_split)

    def run_text_through_html_filter(self, text):
        """
        We want to extract text in case we have
        a html string
        :param text: str
        :return: str
        """
        soup = BeautifulSoup(text, 'html.parser')
        all_tags_list = soup.find_all()
        if len(all_tags_list) != 0:
            text_list = [i.text.strip() for i in all_tags_list]
            return text_list[0]
        return text


if __name__ == "__main__":
    inst = WordCounter()
    text = ""
    text = '<p> python is easy to learn </p>'
    # text = "no html"
    print(inst.count_words(text))
    print(inst.run_text_through_html_filter(text))
    # text = 5
    # assert text == 5
