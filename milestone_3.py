
guess = input("Please guess a letter: ")

def check_guess(letter):
    letter = letter.lower()
    while True:
        if letter.isalpha():
            print("Valid letter")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

def ask_for_input(letter):

     if letter in "hello":
        print("Good guess! {one} is in the word.".format(one=letter))
     else:
        print("Sorry, {two} is not in the word. Try again.".format(two=letter))

check_guess(guess)
ask_for_input(guess)