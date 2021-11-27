# Description: In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues. The game
# offers one of the following hints in response to your guess:
# “Pico” when your guess has a correct digit in the wrong place,
# “Fermi” when your guess has a correct digit in the correct place, and
# “Bagels” if your guess has no correct digits.
# You have 10 tries to guess the secret number.

import random


def check_guess(guess_num, real_num):
    """Helper method that checks to see if the guess shares any similar numbers with the generated number
    Returns a string that is either 'Bagels' if nothing matches or 'Fermi' and or 'Pico' depending on the number of
    matches for each type."""
    fermi_ct = 0
    pico_ct = 0
    bagels_ct = 0

    if int(real_num) < 10:
        real_num = "00" + real_num
    elif int(real_num) < 100:
        real_num = "0" + real_num

    if guess_num == real_num:
        return "You got it!"
    else:
        for el in range(0, len(guess_num)):
            if guess_num[el] == real_num[el]:
                fermi_ct += 1
            elif guess_num[el] in real_num:
                pico_ct += 1
            else:
                bagels_ct += 1

        feedback = (fermi_ct * "Fermi ") + (pico_ct * "Pico ")

        if bagels_ct == 3:
            return "Bagels"
        else:
            return feedback


def bagels_game():
    """Initiates the bagels game, will keep looping until a guess is correct or a user uses all 10 guesses.
    Returns feedback from the check_guess function, or a message if the user got it."""
    gen_num = str(random.randint(0, 999))
    guess_ct = 1
    keep_playing = True

    while keep_playing:
        user_guess = input(f"Guess #{guess_ct}: ")
        result = check_guess(user_guess, gen_num)

        if result == "You got it!":
            print(result)
            play_again = input("Do you want to play again? (yes or no) ")
            if play_again == "yes":
                bagels_game()
                keep_playing = True
            elif play_again == "no":
                keep_playing = False
        else:
            print(result)
            guess_ct += 1
            if guess_ct > 10:
                print("Game over! You are out of guesses.")
                keep_playing = False


bagels_game()
