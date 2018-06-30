import string

keys = list(string.ascii_uppercase) + list(string.digits) + ['.', ',', '?', ':']
code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
        '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--',
        '....-', '.....', '-....', '--...', '---..', '----.', '.-.-.-', '--..--', '..--..', '---...']

morse_code = dict(zip(keys, code))
rev_morse = dict(zip(code, keys))

# print(morse_code)
# print(rev_morse)

message = str(input('Please enter a message to encode: ')).upper()
encoding = []
decoded = []

for i in message:
    if i in morse_code:
        encoding.append(morse_code[i])
print('  '.join(encoding))

for i in encoding:
    if i in rev_morse:
        decoded.append(rev_morse[i])
print(''.join(decoded))


