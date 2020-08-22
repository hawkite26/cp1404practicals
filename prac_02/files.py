name_file = open("name.txt", 'w')
name = input("What is your name? ")
print(name, file=name_file)
name_file.close()

name_file = open("name.txt", 'r')
name_in_file = name_file.read()
print("Your name is {}".format(name_in_file))
name_file.close()

numbers_file = open("numbers.txt", 'r')
number_one = int(numbers_file.readline().strip())
number_two = int(numbers_file.readline().strip())
total = number_one + number_two
print(total)
numbers_file.close()

numbers_file = open("numbers.txt", 'r')
total = 0
for line in numbers_file:
    number = int(line.strip())
    total += number
print(total)
numbers_file.close()
