"""
CP1404/CP5632 - Practical
Loops with range.
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=" ")
print()

# b. count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# c. print n stars based on user input
user_input = int(input("Number of stars: "))
for i in range(1, user_input + 1):
    print("*", end=" ")

# d. print n lines of increasing stars
user_input = int(input("Number of stars: "))
for i in range(1, user_input + 1):
    print()
    for j in range(i):
        print("*", end="")
