#MÉTODOS

value = input('Type anything you want (letters, words, integer numbers, real numbers, special characters):\n')
print('The primary type of {} is:'.format(value), type(value))
print('{} is blank space?'.format(value), value.isspace())
print('{} is a number?'.format(value), value.isnumeric())
print('{} is a word?'.format(value), value.isalpha())
print('{} is alphanumeric?'.format(value), value.isalnum())
print('{} is only uppercase?'.format(value), value.isupper())
print('{} is only in lowercase?'.format(value), value.islower())
print('{} is capitalized?'.format(value), value.istitle())