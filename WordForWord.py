import os
import re
from itertools import count


class Word4word:

    def printfile(self, file_path):
        with open(file_path, 'r') as file:
            file_content = file.read()
        return file_content

    def wc(obj: str):
        word_count = len(re.findall(r'\w+', obj))
        words = word_count
        chars = len(obj)
        lines = obj.count('\n')
        tupe = (lines, words, chars)
        return tupe

    def word_freq(obj: str):
        new_lst = obj.split()
        freq = [new_lst.count(c) for c in new_lst]
        return dict(zip(new_lst, freq))

    def letter_freq(obj: str):
        onlywrds = re.sub(r'[^a-zA-Z0-9]', ' ', obj).lower()
        freq = {}
        for l in onlywrds:
            if l in freq:
                freq[l] += 1
            else:
                freq[l] = 1
        return freq

    def freq_word(obj: str, word, total_words):
        count = 0
        new_string = re.sub(r'[^\w\s]', '', obj)
        split_new_string = new_string.split()
        for i in split_new_string:
            if i == word:
                count += 1
        freq = count / total_words
        return freq



x = Word4word()
b = x.printfile('/Users/isiah/Projects/P1/PyWordForWord/testdata/testdata5a.txt')
tupe = Word4word.wc(b)
print(tupe)
# print(Word4word.word_freq(b))
print(Word4word.letter_freq(b))
print(Word4word.freq_word(b, 'the', tupe[1]))


