message = input(">")
words = message.split(' ')

# emojis dictionary
emojis = {
    ':)': "😂",
    ':(': "☹️",
}

printoutWords = ""

for word in words:
    printoutWords += emojis.get(word, word) + " "

print(printoutWords)
