import random
import string

alphabets = list(string.ascii_lowercase)
numbers = list(string.digits)
symbols = list(string.punctuation)

list1 = random.choices(alphabets, k = 3)
print(list1)
list2 = random.choices(numbers, k = 3)
print(list2)
list3 = random.choices(symbols, k = 3)
print(list3)

result =''.join(list1 + list2 + list3)
print(result)

