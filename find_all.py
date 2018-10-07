import re
import copy
import pytest


words_filename = 'deps/english-words/words_alpha.txt'


def load_words_set():
    with open(words_filename) as word_file:
        valid_words = set(word_file.read().split())
    return valid_words


def load_words_string():
    with open(words_filename) as word_file:
        words = word_file.read()
        words = '\n' + words + '\n'
    return words


def word_search(query_string, words):
    query_string = query_string.replace(' ', '.{1}')
    query_string = r'\s' + query_string + r'\s'
    expression = re.compile(query_string)
    matches = re.findall(expression, words)
    return [match.strip() for match in matches]


def only_allowed_once(word, original_allowed_letters):
    allowed_letters = copy.copy(original_allowed_letters)
    for letter in word:
        # print("LETTER", letter, allowed_letters, letter in allowed_letters)
        if letter in allowed_letters:
            # allowed_letters.replace(letter, '', 1)
            allowed_letters_list = list(allowed_letters)
            index = allowed_letters_list.index(letter)
            del(allowed_letters_list[index])
            allowed_letters = ''.join(allowed_letters_list)
        else:
            return False
    return True


def letter_filter(words_list, allowed_letters):
    return [word for word in words_list if only_allowed_once(word, allowed_letters)]


def cheat(query_string, allowed_letters, words):
    words_list = word_search(query_string, words)
    return letter_filter(words_list, allowed_letters)


def main():
    words_string = load_words_string()
    while(True):
        print("allowed_letters: ")
        allowed_letters = input()
        while(True):
            print("query_string: ")
            query_string = input()
            if len(query_string) == 0:
                break
            results = cheat(query_string, allowed_letters, words_string)
            print(results)


if __name__ == '__main__':
    main()
