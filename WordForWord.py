import os

file_path = '/Users/isiah/Projects/P1/PyWordForWord/testdata/testdata0.txt'

def printfile(filepath):
    with open(filepath, 'r') as file:
        file_content = file.read()
        a = str(file_content)
    return a


print(printfile(file_path))

def wc(filepath):
    num_chars = 0
    num_words = 0
    num_lines = 0
    with open(file_path, 'r') as file:
        for line in file:
            #separate lines on current platform
            line = line.strip(os.linesep)
            #split lines
            wordslist = line.split()
            num_lines += 1
            num_words = num_words + len(wordslist)
            num_chars = num_chars + sum(1 for c in line if c not in (os.linesep, ' '))

    print(f"Number of Chars: {num_chars}")
    print(f"Number of Words: {num_words}")
    print(f"Number of lines: {num_lines}")

wc(file_path)


