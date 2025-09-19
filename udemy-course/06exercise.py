# exercise 6
x = 5
y = 7

if x > y:
    print("x is greater than y")
elif x == y:
    print("x equals y")
else:
    print("x is smaller than y")

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char.isupper():
        print(char)

