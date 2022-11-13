# in this file we will be creating the hangman game 
import random 
from words import words 
import string

def get_valid_word(words):
    word = random.choice(words)# randomly choose something from the list
    while '-'in word or ' ' in word:
        word=random.choice(words)

    return word.upper()

def hangman():
    """
    we need to keep the travk of what words we have guessed correct for that this function is defined 
    """
    print("check this funtion is working \n")
    word=get_valid_word(words)
    # print(word)
    word_letter =set(word) # to keep the track of the set of words in the list 
    alphabet = set(string.ascii_uppercase)  
    used_letters = set() # to keep the track of what user has guessed

    lives=6

    #getting the user input
    while len(word_letter)>0 and lives>0:
        # Letters Used
        # ' ' .join(['a','b','c']) ---> a b c
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        #print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))
        user_letter = input("Guess a letter :").upper()
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)

            else:
                lives=lives-1
                print("Letter is Not in the Word\n")

                

        elif user_letter in used_letters:
            print("You have already used this letter. please Try Again \n" )
    
        else:
            print("Invalid Chracter, Please Enter a valid charcter \n")

    # get's out of the while loop , it will get out based on the two conditions 
    if lives==0:
        print("You died , Better luck next time! \n", word)
    else:
        print("You guessed the word correctly!!", word, "Let's Celebrate \n")


print("Starting Game")
hangman()
print("Ending Game")




 