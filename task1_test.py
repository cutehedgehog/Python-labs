import main

def test_count_sentences_0():
    text = ''
    assert main.count_sentences(text) == 0

def test_count_sentences_1():
    text = 'Hi, Mr. Tom.'
    assert main.count_sentences(text) == 1

def test_count_sentences_2():
    text = 'Hi, Mr. Tom!'
    assert main.count_sentences(text) == 1

def test_count_sentences_3():
    text = 'Hi, Mr. Tom! Goodbye, Mrs. Smith.'
    assert main.count_sentences(text) == 2

def test_count_sentences_4():
    text = 'Hi, Mr. Tom! Goodbye, Mrs. Smith?!'
    assert main.count_sentences(text) == 2

def test_count_sentences_5():
    text = 'Hi, Mr. Tom! Goodbye, Jan.'
    assert main.count_sentences(text) == 2

def test_count_sentences_6():
    text = 'Hi, Mr. Tom. See Jan. qwert.'
    assert main.count_sentences(text) == 2

#------------------------------------------------------------#
#------------------------------------------------------------#
#------------------------------------------------------------#

def test_nondecl_sentences_0():
    text = ''
    assert main.count_non_decl_sentences(text) == 0

def test_nondecl_sentences_1():
    text = 'Hi, Mr. Tom. Goodbye, Mrs. Smith?!'
    assert main.count_non_decl_sentences(text) == 1

def test_nondecl_sentences_3():
    text = 'Hi, Mr. Tom. Goodbye, Mrs. Smith?!'
    assert main.count_non_decl_sentences(text) == 1

def test_nondecl_sentences_3():
    text = 'Hi, Mr. Tom. Goodbye, Mrs. Smith?! Some text... Some text!'
    assert main.count_non_decl_sentences(text) == 2

def test_nondecl_sentences_4():
    text = 'Some text; some text...'
    assert main.count_non_decl_sentences(text) == 0

def test_nondecl_sentences_5():
    text = 'Some text; some text... Some text!!!'
    assert main.count_non_decl_sentences(text) == 1

#------------------------------------------------------------#
#------------------------------------------------------------#
#------------------------------------------------------------#

def test_avg_sen_len_1():
    text = ''
    assert main.average_sent_length(text) == 0

def test_avg_sen_len_5():
    text = '123 123 hi.'
    assert main.average_sent_length(text) == 2

def test_avg_sen_len_6():
    text = 'Hi, Mr. Tom. Goodbye, Mrs. Smith! How r u, 123 Tolkien?!'
    exp = (7 + 12 + 15) / 3
    assert main.average_sent_length(text) == round(exp, 2)

#------------------------------------------------------------#
#------------------------------------------------------------#
#------------------------------------------------------------#

def test_avg_word_len_1():
    text = ''
    assert main.average_word_length(text) == 0

def test_avg_word_len_2():
    text = 'Hi, Mr. Tom.'
    exp = (2 + 2 + 3) / 3
    assert main.average_word_length(text) == round(exp, 2)

def test_avg_word_len_3():
    text = 'Hi, Mr. Tom. Hi; Goodbye.'
    exp = (2 + 2 + 3 + 2 + 7) / 5
    assert main.average_word_length(text) == round(exp, 2)

def test_avg_word_len_4():
    text = 'Hi, Mr. Tom 123 A1.'
    exp = (2 + 2 + 3 + 2) / 4
    assert main.average_word_length(text) == round(exp, 2)

def test_avg_word_len_5():
    text = 'Hi, Mr. Tom. What u\'ll do?'
    exp = (2 + 2 + 3 + 4 + 1 + 2 + 2) / 7
    assert main.average_word_length(text) == round(exp, 2)

def test_avg_word_len_6():
    text = 'Hi, Mr. Tom. What u\'ll do? I\'m Ph.d! Some text e.g.'
    exp = (2+2+3+4+1+2+2+1+1+2+1+4+4+1+1) / 15
    assert main.average_word_length(text) == round(exp, 2)

#------------------------------------------------------------#
#------------------------------------------------------------#
#------------------------------------------------------------#
#
# def test_top_k_repeated_ngrams_1():
#     text = ''
#     assert main.top_k_repeated_ngrams(text, 10, 2) == []
#
# def test_top_k_repeated_ngrams_2():
#     text = 'Hi, Mr. Tom. Hi, Mr. Tom.'
#     exp = [('Hi Mr', 2), ('Mr Tom', 2), ('Tom Hi', 1)]
#     assert main.top_k_repeated_ngrams(text, 10, 2) == exp
#
# def test_top_k_repeated_ngrams_3():
#     text = 'Hi, Mr. Tom. Hi, Mr. Tom 123 123 123 123 123 123.'
#     exp = [('Hi Mr', 2), ('Mr Tom', 2), ('Tom Hi', 1)]
#     assert main.top_k_repeated_ngrams(text, 10, 2) == exp
#
# def test_top_k_repeated_ngrams_4():
#     text = 'A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12'
#     exp = [('A1 A2', 1),('A2 A3', 1), ('A3 A4', 1), ('A4 A5', 1), ('A5 A6', 1)
#     , ('A6 A7', 1), ('A7 A8', 1), ('A8 A9', 1), ('A9 A10', 1), ('A10 A11', 1)]
#     assert main.top_k_repeated_ngrams(text, 10, 2) == exp
#
# def test_top_k_repeated_ngrams_5():
#     text = 'Hi, Mr. Tom. Hi, Mr. Tom 123 123 123 123 123 123.'
#     exp = [('Hi Mr Tom', 2), ('Mr Tom Hi', 1)]
#     assert main.top_k_repeated_ngrams(text, 2, 3) == exp
#
# def test_top_k_repeated_ngrams_6():
#     text = 'Привет ривет Привет ривет Привет ривет Привет ривет Hi hi Hi hi 123 123 123 123 123 123 123 123 123 123'
#     exp = [('Hi hi', 2), ('hi Hi', 1)]
#     assert main.top_k_repeated_ngrams(text, 2, 2) == exp