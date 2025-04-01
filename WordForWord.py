import os
import re


class Word4word:

    def printfile(self, file_path):
        with open(file_path, 'r') as file:
            file_content = file.read()
        return file_content

    def wc(self, obj):
        word_count = len(re.findall(r'\w+', obj))
        words = word_count
        chars = len(obj)
        lines = obj.count('\n')
        tupe = (lines, words, chars)
        return tupe

    def word_freq(self, obj):
        onlywrds = re.sub(r'[^a-zA-Z0-9]', ' ', obj)
        splitwrds = onlywrds.lower().split()
        wrd = {}
        for l in splitwrds:
            if l in wrd:
                wrd[l] += 1
            else:
                wrd[l] = 1
        return wrd

    def letter_freq(self, obj):
        onlywrds = re.sub(r'[^a-zA-Z0-9]', ' ', obj).lower()
        freq = {}
        for l in onlywrds:
            if l in freq:
                freq[l] += 1
            else:
                freq[l] = 1
        return freq

    def freq_word(self, obj, word, total_words):
        count = 0
        new_string = re.sub(r'[^\w\s]', '', obj)
        split_new_string = new_string.split()
        for i in split_new_string:
            if i == word:
                count += 1
        freq = count / total_words
        return freq



# x = Word4word()
# b = x.printfile('/Users/isiah/Projects/P1/PyWordForWord/testdata/testdata5a.txt')
# tupe = Word4word.wc(b)
# print(tupe)
# print(Word4word.word_freq(b))
# print(Word4word.letter_freq(b))
# print(Word4word.freq_word(b, 'the', tupe[1]))

path = '/Users/isiah/Projects/P1/PyWordForWord/testdata'

with open('ResultsOfProcessing.txt', 'w') as text_file:
    for file in os.listdir(path):
        full_path = "%s/%s" % (path, file)
        wrd = Word4word()
        b = wrd.printfile(full_path)
        text_file.write(file + '\n')
        text_file.write(str(wrd.wc(b)) + '\n')
        text_file.write(str(wrd.word_freq(b))+ '\n')
        text_file.write(str(wrd.letter_freq(b))+ '\n')
        text_file.write('\n\n\n')




