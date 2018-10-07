import find_all


def test_search():
    words_string = find_all.load_words_string()
    results = find_all.word_search(" ate", words_string)
    expected = ['bate', 'cate', 'date', 'fate', 'gate', 'hate', 'yate', 'kate', 'late', 'mate', 'nate', 'pate', 'rate', 'sate', 'tate']
    assert results == expected


def test_filter():
    words_list = ['bate', 'cate', 'date', 'fate', 'gate', 'hate', 'yate', 'kate', 'late', 'mate', 'nate', 'pate', 'rate', 'sate', 'tate']
    results = find_all.letter_filter(words_list, 'faterd')
    expected = ['date', 'fate', 'rate']
    assert results == expected


def test_only_allowed_once():
    assert find_all.only_allowed_once('feet', 'etf') == False
    assert find_all.only_allowed_once('feet', 'eetf') == True


# def test_filter_no_repeat():
#     words_list = ['feet', 'eft']
#     results = find_all.letter_filter(words_list, 'fet')
#     expected = ['eft']
#     assert results == expected


def test_cheat():
    words_string = find_all.load_words_string()
    results = find_all.cheat(' ate', 'faterd', words_string)
    expected = ['date', 'fate', 'rate']
    assert results == expected

