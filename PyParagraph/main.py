"""PyParagraph Solution"""

import re
file_to_load = "raw_data/paragraph_2.txt"
file_to_output = "analysis/paragraph_analysis.txt"

paragraph = ""

with open(file_to_load) as txt_data:
    paragraph = txt_data.read().replace("\n", " ")

wordsplit = paragraph.split(" ")
wordcount = len(wordsplit)


letter_counts = []

for word in wordsplit:

    letter_counts.append(len(word))

avg_letter_count = sum(letter_counts) / float(len(letter_counts))

sentsplits = re.split("(?<=[.!?]) +", paragraph)

print(sentsplits)
sentence_count = len(sentsplits)

words_per_sentence = []

for sentence in sentsplits:

    words_per_sentence.append(len(sentence.split(" ")))

avg_sentence_len = sum(words_per_sentence) / float(len(words_per_sentence))

output = (
    f"\nParagraph Analysis\n"
    f"-----------------\n"
    f"Approximate Word Count: {wordcount}\n"
    f"Approximate Sentence Count: {sentence_count}\n"
    f"Average Letter Count: {avg_letter_count}\n"
    f"Average Sentence Length: {avg_sentence_len}\n")

print(output)

with open(file_to_output, "a") as txt_file:
    txt_file.write(output)
