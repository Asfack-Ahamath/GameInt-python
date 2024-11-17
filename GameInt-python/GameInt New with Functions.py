import random
from colorama import Fore, init

init(autoreset=True)

correct_color_correct_position = 15
correct_color_wrong_position = 5
attempt_decrease_factor = 125

def display_welcome_message():
    print("\n")
    print("◈━◈━◈━◈━◈━◈━◈".center(92))
    print("GameInt".center(92))
    print("◈━◈━◈━◈━◈━◈━◈".center(92))
    print("\n")

def display_rules():
    print("\n============================================================================================\n")
    print("Game Rules :")
    print("\n\t✽  The game will generate a random 4-digit color code.")
    print("\n\t✽  Each digit represents a color from the color mapping.")
    print("\n\t✽  You have to guess randomly generated numbers from 1 to 6.")
    print("\n\t✽  It only requires 4 (XXXX) digits to be entered.")
    print("\n\t✽  You have only 8 attempts to guess the colour code.")
    print("\n\t✽  For each attempt, you will receive a result.")
    print("\n\t✽  If you don't guess the secret number on the 8th try, you will lose!")
    print("\n\t✽  When you enter 0000, it will terminate the game.\n")
    print("✽ ✽ ✽ ✽ ✽ ✽ ✽ ✽ ✽".center(92))
    print("\n\t✽  If the guessed digit is correct and it is in the right place,\n\t   then '1' will be the result. Score = 15")
    print("\n\t✽  If the guessed digit is correct and it is in the wrong place,\n\t   then '0' will be the result. Score = 5")
    print("\n\t✽  If the guessed digit is wrong and not on the list,\n\t   then '●' will be the result. Score = 0\n")
    print("--------------------------".center(91))
    print("Good Luck.✌️  Let's Play!!".center(93))
    print("--------------------------".center(91))

def display_color_mapping(player_name):
    print("\n============================================================================================\n")
    print("Hi {} Welcome to GameInt!".format(player_name).center(93))
    print("\n============================================================================================\n")
    print("Number to Guess - XXXX ", end="")
    print("Colour Mapping :".rjust(43))
    print(Fore.WHITE + '1-White'.rjust(73), Fore.BLUE + '2-Blue', Fore.RED + '3-Red')
    print(Fore.YELLOW + '4-Yellow'.rjust(74), Fore.GREEN + '5-Green', Fore.MAGENTA + '6-Purple', Fore.WHITE + '')

def display_attempt_header():
    print("Attempt No\t\t\tGuess\t\t\t   Result")
    print("──────────\t\t\t─────\t\t\t   ──────")

def get_player_input(attempts):
    while True:
        print(attempts, end="")
        guess = input("".ljust(32))
        if guess == "0000":
            return guess
        elif len(guess) < 4:
            print("Error: You need to input 4 numbers between 1 to 6.")
        elif len(guess) > 4:
            print("Error: You can only input 4 numbers between 1 to 6.")
        elif not guess.isdigit():
            print("Error: You can only input 4 integers between 1 to 6.")
        elif not all([int(index) <= 6 for index in guess]):
            print("Error: The secret number is only from 1 to 6.")
        else:
            return guess

def generate_color_code():
    colours = ["1", "2", "3", "4", "5", "6"]
    colour_code = random.sample(colours, 4)
    return colour_code

def calculate_result(player_guess, colour_code):
    result = []
    score = 0

    for i in range(4):
        if player_guess[i] == colour_code[i]:
            result.append("1")
            score += correct_color_correct_position
        elif player_guess[i] in colour_code:
            result.append("0")
            score += correct_color_wrong_position
        else:
            result.append("●")

    return result, score

def display_result(result):
    print("", result[0].rjust(61), end=" ")
    print(result[1])
    print("", result[2].rjust(61), end=" ")
    print(result[3])
    print("─────────────────────────────────────────────────────────────────")

def main():
    player_name = ""
    score = 0

    start_game = ""
    while True:
        if not start_game:
            start_game = input("\nWould you like to play this GameInt? (Yes-Y / No-N) : ").lower()
            if start_game != 'y' and start_game != 'n':
                print("\n\t\t\t Invalid Input. Enter Y or N.")
                start_game = ""
                continue
        if start_game == "n":
            print("\n════════════════════════════════════════════════════════\n")
            print("         At Least Play The GameInt Next Time!\n")
            print("\t         👋 👋 Bye! Bye! 👋 👋")
            print("\n════════════════════════════════════════════════════════\n")
            break

        display_welcome_message()
        player_name = input("Please Enter Your Name : ")

        while True:
            print("\n============================================================================================\n")
            rules = input(player_name + "! do you want to know about the rules of this GAME? (Yes-Y / No-N) : ").lower()
            if rules == 'y':
                display_rules()
                break
            elif rules == 'n':
                break
            else:
                print("\nInvalid Input. Please enter 'Y' for Yes or 'N' for No.")

        display_color_mapping(player_name)

        attempts = 0
        colour_code = generate_color_code()
        print("Generated color code (for testing): " + ''.join(colour_code))
        print("\r")

        display_attempt_header()

        for attempts in range(1, 9):
            guess = get_player_input(attempts)
            
            if guess == "0000":
                print("\n─────────────────────────────────────────────────────────────────\n")
                print("        You have decided to terminate the game. Goodbye!")
                print("\n=================================================================\n")
                break

            if not all([int(index) <= 6 for index in guess]):
                print("The secret number is only from 1 to 6.")
                continue

            player_guess = list(guess)
            result, current_score = calculate_result(player_guess, colour_code)
            score += current_score
            display_result(result)

            if all([player_guess[i] == colour_code[i] for i in range(4)]):
                print("Secret Code was : [ " + ''.join(colour_code) + " ]")
                print("🎉 Congratulations!! "+ player_name +" You have won the game!!! 🎉")
                if attempts == 1:
                    print("You guessed the code at the First Attempt! 😊")
                else:
                    print("You Needed " + str(attempts) + " attempts to guess the Colour Code.")
                print("─────────────────────────────────────────────────────────────────\n")
                remaining_attempts = 8 - attempts
                attempt_bonus = remaining_attempts * attempt_decrease_factor
                score += attempt_bonus
                if attempts == 1:
                    score = 1000
                print("\t\t   You have scored " + str(score) + " points.")
                print("\n─────────────────────────────────────────────────────────────────")
                print("\t\t  ▼△▼△▼△▼△▼△▼△▼△▼△▼△▼△▼△▼△▼△▼△▼")
                print("=================================================================\n")
                break

            elif attempts == 8:
                print("You have lost this Game. 😢")
                print("Secret Code was : [ " + ''.join(colour_code) + " ]")
                print("Secret Code was : [ " + ''.join(colour_code) + " ]")
                print("Don't worry, You can try to win next time! 🙂")
                print("─────────────────────────────────────────────────────────────────")
                print("\t\t  ▼△▼△▼△▼△▼△▼△▼△▼△▼△▼△▼△▼△▼△▼△▼")
                print("=================================================================\n")
                break
            else:
                pass

        while True:
            finish_game = input("\t  Do you want to play again? (Yes-Y / No-N) : ").lower()
            if finish_game == 'y' or finish_game == 'n':
                break
            else:
                print("\n\t\t         Invalid Input. Enter Y or N.\n")
        
        if finish_game == "y":
            print("\n\t\t      So, Let's play again...")
            print("\n=================================================================")
            continue

        elif finish_game == "n":
            print("\n=================================================================\n")
            print("\t\t  Thank you for playing GameInt!\n")
            print("\t\t      👋 👋 Bye! Bye! 👋 👋")
            print("\n=================================================================\n")
            break

main()
