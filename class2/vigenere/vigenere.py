from itertools import cycle
import time
text = input("Enter a text: ")
key_values = [1,3,5]
ascii_values = [ord(char) for char in text]

new_ascii_values = [value + key for value, key in zip(ascii_values, cycle(key_values))]
print("암호화 진행중")
time.sleep(1)
new_text = ''.join(chr(value) for value in new_ascii_values)

print (new_text)