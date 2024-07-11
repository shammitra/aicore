import random as rdm

word_list = ['apple','banana', 'grapes','strawberries','blueberries']

def random_word(self):
    for index,fruit in enumerate(word_list, start=1):
        print(index, fruit)
        
choice = rdm.choice(word_list)
word = choice
print(word)

def random_letter(self):
    
    guess = input("enter a single letter: ")
    
    if len(guess)==0 and guess.isalpha():
        print('yes')
    else:
        print('Oops! That is not a valid input.')


