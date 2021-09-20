#Day 1: L33t$p3@]< (LeetSpeak)
#This is only encoding part
import random
leetmessage = ""
charMapping = {'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],
               'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
               'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
               'v': ['\\/']}


def converttoleet(user_message):

    leetmessage = ""
    leetreplacement = ""
    random_probability = random.random()
    for char in user_message:
        if (char.lower() in charMapping) and (random_probability <= 0.70):
            possibilities = charMapping[char.lower()]
            leetreplacement = random.choice(possibilities)
            leetmessage += leetreplacement
        else:
            leetmessage += char
    return leetmessage



a = input("Enter your message : ")
secret_message = converttoleet(a)
print("Your original message is {}".format(a))
print("Your encoded message is {}".format(secret_message))




