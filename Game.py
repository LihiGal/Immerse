import random
#0. Define a variable for the game score, e.g. score=3
score = 3
print("your score is ", score)

#1. Load all the available words in memory (by reading them from a text file, or hard-coding them)
with open("word_list.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))

#2. Pick a random word from all the available words.
random_word = (random.choice(words))

#3. Turn the letters in the word into capital letters, search for the default method .upper()
word = random_word.upper()

#4. Use the function get_masked_word() that I provided for you above.
def get_masked_word(word):
    unique_letters_list = list(set(word)) # set() finds unique elements in string

    random.shuffle(unique_letters_list)

    split_point = len(unique_letters_list) // 2
    letters_to_mask_list = unique_letters_list[0:split_point]

    masked_word = ""
    masked_letter_position_dict = {}
    for letter_position, letter in enumerate(word):
        if(letter in letters_to_mask_list):
            masked_word = masked_word + "_"
            # We store the position of the masked letter in a dictionary
            if(letter in masked_letter_position_dict):
                # If the letter is in the dictionary we append the position
                masked_letter_position_dict[letter].append(letter_position)
            else:
                # If the letter is NOT in the dictionary we create the entry (a list)
                masked_letter_position_dict[letter] = [letter_position]
        else:
            masked_word = masked_word + letter        
    return masked_word, masked_letter_position_dict


#5. Print on screen the masked word and ask the user to 
# type a letter in the terminal, you can use the default method input()

print("guess the word by typing a letter")

masked_word, masked_letters_dict = get_masked_word(word)
print(masked_word)

for e in range(10):

    import string

    while True:
        userInput = input(':')
        if userInput.isalpha():
            break
        print ('Please enter only letters')
        if len(userInput) >= 1:
            print('Please enter only one letter')

    #7. Turn the character provided by the user into a capital letter
    guess = userInput.upper()


    #8. Check if the letter provided by the user is a good one or a bad one.
    #9. Print the current user score, the masked word, and the list of letters already tried.
    if guess in masked_letters_dict:
        print("You got one!")
        score = score
        print("Your score is ", score)

        letter_position_list = masked_letters_dict[guess]
        for position in letter_position_list:
            tmp_list = list(masked_word)
            tmp_list[position] = guess
            masked_word = "".join(tmp_list)
            
       
        print(masked_word)
        masked_letters_dict.pop(guess)
    else:
        print ("Wrong!")
        score = score - 1
        print(masked_word)
        print("Your score is ", score)



    if masked_word == word:
        print ("You got the word!")
        exit()

        
    
    if score==0:
        print("you failed loser")
        exit()
