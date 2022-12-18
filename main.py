import random
password = []

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

nr_letters = int(input("How many letters? "))
nr_numbers = int(input("How many numbers? "))
nr_symbols = int(input("How many symbols? "))

for i in range(0, nr_letters):
    random_letter_pick = random.choice(letters)
    password.append(random_letter_pick)

for i in range(0, nr_numbers):
    random_number_pick = random.choice(numbers)
    password.append(random_number_pick)

for i in range(0, nr_symbols):
    random_symbol_pick = random.choice(symbols)
    password.append(random_symbol_pick)

random.shuffle(password)

formatted_password = ""
for char in password:
    formatted_password += char
print(f"Your Password is: {formatted_password}")
