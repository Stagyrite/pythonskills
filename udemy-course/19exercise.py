# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

for char in text:

    if char.isalnum():
        word_count[char.lower()] = word_count.setdefault(char.lower(), 0) + 1

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
