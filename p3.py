intro = input("Write about yourself")
wordCount = 1
for w in intro:
    if (w == ' '):
        wordCount = wordCount + 1
print(wordCount)