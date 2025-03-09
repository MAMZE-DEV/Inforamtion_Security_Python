import time
text = input("Enter a text: ")
key = int(input("Enter a key: "))
ascii_values = [ord(char) for char in text]
new_ascii_values = [value + key for value in ascii_values]
print("암호화 진행중")
time.sleep(1)
new_text = ''.join([chr(value+key) for value in new_ascii_values])

print(new_text)
