alphabet = "abcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvxy01234567890123456789"
encrypt = input("Enter a clear message: ")
key = int(input("Please enter a key(number from 1-25: "))
encrypt = encrypt.lower()
encrypted = ""
for letter in encrypt:
    position = alphabet.find(letter)
    newPosition = position + key
    if letter in alphabet:
        encrypted = encrypted + alphabet[newPosition]
    else:
        encrypted = encrypted + letter
print("You cipher is", encrypted)
