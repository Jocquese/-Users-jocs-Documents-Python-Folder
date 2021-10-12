import random

words = ["dog", "monkey", "cat", "book", "love", "exams", "rocket", "space", "rain", "KFC"]

letters = []
word = words[random.randrange(len(words))]

print("Welcome to HangMan!")
life = 10
while life < 30:
    guess = input("Enter your first guess: ")
    if word.__contains__(guess):
        print("Wow, You guessed this right!!!")
        letters.append(guess)
        if letters.__len__() == word.__len__():
            print("Congratulations!!!")
            break
        else: 
            lettersLeft = word.__len__() - letters.__len__()
            print("You Have ", lettersLeft, " Letters Left")
    else:
        life -= 1
        if life == 0:
            print("GameOver!!!! The word was -> ", word)
            break
        else:
            print("OOOPS, you have ", life, " Lives left, TRY AGAIN!")