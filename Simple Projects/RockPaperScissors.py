input ("Lets play rock paper scissors! ")
def main():
    from random import randint
    rpsChoices = ["rock","paper","scissors"]
    rpsP = input("rock, paper, or scissors?: ")
    rpsC = rpsChoices[randint(0,2)]

    print("You chose",rpsP)
    print("The computer chose",rpsC)
    if rpsC == rpsP:
        print("You tied. Well you had luck.")
    elif rpsC == "paper" and rpsP == "rock" or rpsC == "rock" and rpsP == "scissors" or rpsC == "scissors" and rpsP == "paper":
        print("You lose. YAY I BEAT YOU. YOU SUCK.")
    elif rpsC == 'paper' and rpsP == 'scissors' or rpsC == 'rock' and rpsP == 'paper' or rpsC == 'scissors' and rpsP == 'rock':
        print("You win. How did you beat me? You probably cheated >:(") 
        input (" Did you cheat or not? Be honest ")
        input (" Stop lying you cheated ")
        input (' STOP LYING IF YOU LIE ILL COME AND FIND OUT WHERE YOU LIVE AND KIDNAP YOU AND THEN WE WILL go to the ice cream shop! :D ')
        input (' Fine fine, you won and didnt cheat. BUT THAT WAS JUST LUCK NO ONE BEATS THE COMPUTER ')

main()