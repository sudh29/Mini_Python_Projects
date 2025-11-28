import unittest
from search import perform_youtube_search, SEARCH_QUERY


class TestSeleniumScript(unittest.TestCase):
    def test_search_functionality(self):
        perform_youtube_search(SEARCH_QUERY)


if __name__ == "__main__":
    unittest.main()
