from cs50 import get_string
import sys

COLEMAN_LIAU_LETTER_COEFFICIENT = 0.0588
COLEMAN_LIAU_SENTENCE_COEFFICIENT = 0.296
COLEMAN_LIAU_OFFSET = 15.8

# The Coleman-Liau index formula
# is used to estimate the grade level required
# to comprehend a piece of text


def count_letters(text):
    count = 0
    for i in text:
        if i.isalpha():
            count += 1
    return count


def count_words(text):
    count = 0
    for i in text:
        if i.isspace():
            count += 1
    return count+1


def count_sentences(text):
    count = 0
    for i in text:
        if i in ".?!":
            count += 1
    return count


# empty input error handling
while True:
    text = get_string("Text: ")
    if text:
        break

letters = count_letters(text)
words = count_words(text)
sentences = count_sentences(text)

# error handling for zero words or sentences
if words == 0 or sentences == 0:
    print("No words or sentences found")
    sys.exit(1)

# Coleman-Liau formula part 1
# l_formula is the average no.of letters per 100 words
# s_formula is the sentence equivalent
l_formula = letters/words * 100
s_formula = sentences/words * 100

# Coleman-Liau formula part 2
index = COLEMAN_LIAU_LETTER_COEFFICIENT * l_formula - \
    COLEMAN_LIAU_SENTENCE_COEFFICIENT * s_formula - COLEMAN_LIAU_OFFSET
# to get integers
index = round(index)
# printing according to index
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
