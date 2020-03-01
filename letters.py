Alphabet ="abcdefghijklmnopqrstuvwxyz"
b = len(Alphabet)
for letter in range(b):
    reverse= Alphabet[letter:]+Alphabet[:letter]
    print(reverse)

