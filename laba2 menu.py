name = None
a = 0
while True:
    print("Menu")
    print("1. Count the number of letters in words: ")
    print("2. Sort a string: ")
    print("3. Quit")

    response = input("Please choose an action: ")

    print()
    if response == "1":
        s = input("Enter a string: ")
        letters = [0] * 26
        for i in s.lower():
            if 'a' <= i <= 'z':
                number = ord(i) - 97
                letters[number] += 1
        for i in range(26):
            if letters[i] > 0:
                print(chr(i + 97), letters[i])
    elif response == "2":
        string = input("Enter a string: ")
        words = string.split(' ')

        words = list(set(words))

        nodublication = ' '.join(words)
        words.sort()
        print("Your words - ")
        for nodublication in words:
            print(nodublication)
    elif response == "3":
        break
    else:
        input("Incorrect choose! ")

    print()
