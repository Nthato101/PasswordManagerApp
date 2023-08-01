#Password Generator Project
import random
def password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  letters_list = [random.choice(letters) for letter in range(nr_letters)]
  numbers_list = [random.choice(numbers) for number in range(nr_numbers)]
  symbols_list = [random.choice(symbols) for symbol in range(nr_symbols)]

  password_list = letters_list + numbers_list + symbols_list


  random.shuffle(password_list)

  password = ""
  for char in password_list:
    password += char

  return password
