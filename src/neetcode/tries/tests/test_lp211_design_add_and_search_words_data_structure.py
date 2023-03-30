from ..lp211_design_add_and_search_words_data_structure import WordDictionary


def test_case1():
    wd = WordDictionary()
    wd.addWord("bad")
    assert wd.search("bad") is True
