# Random password generator
import random

def generate_password(wordlist):
    random.shuffle(wordlist)
    return "".join(wordlist)

wordlist = input().split()
print(generate_password(wordlist))
