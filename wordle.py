# 2022 Alin-Gabriel Drăghici <guky667@gmail.com>  #
# # # # # # # # # # # # # # # # # # # # # # # # # #

# region Vars and inits
# SERAI _should_ be the best starting word

words_per_line = 20
print_counter = 0
green1 = []
green2 = []
green3 = []
green4 = []
green5 = []
all_letters = []
#endregion

### BLACK LETTERS 
# letters to avoid, that are not part of the word
black_letters = ['S','R','A','P','L','P','L','T','H','W']

# generate the entire alphabet (of uppercase letters)
for char in range(65, 91):
    if (chr(char) not in black_letters):
        all_letters.append(chr(char))
green1 = green2[:] = green3[:] = green4[:] = green5[:] = all_letters[:]
# remove any duplicate black letters
black_letters = list(dict.fromkeys(black_letters))

### YELLOW LETTERS
# add letters to be removed from specific positions
yellow1 = ['']
yellow2 = ['']
yellow3 = ['E']
yellow4 = ['N']
yellow5 = ['D','I']

### GREEN LETTERS
# set letters that have been found in the right position - uncomment and add letter
#green1 = ['']
green2 = ['E']
#green3 = ['']
#green4 = ['']
#green5 = ['']

#region Execution
# create list of letters to include based on Yellow Letters
include = list(dict.fromkeys(','.join(filter(None,[*yellow1, *yellow2, *yellow3, *yellow4, *yellow5])).split(',')))

for yellow_letter in include:
    if yellow_letter in black_letters:
        print ('Cannot include and exclude letter',yellow_letter,'. Please remove from either black_letters or yellow letters')
        raise SystemExit(0)

for first_letter in green1:
    if (len(green1) != 1):
        print(end = '\n\n')
        counter = 0
    if first_letter not in yellow1:
        for second_letter in green2:
            if second_letter not in yellow2:
                if (len(green2) != 1 and len(green1) == 1):
                    print(end = '\n\n')
                    print_counter = 0
                for third_letter in green3:
                    if third_letter not in yellow3:
                        if (len(green3) != 1 and len(green2) == 1 and len(green1) == 1):
                            print(end = '\n\n')
                            print_counter = 0
                        for fourth_letter in green4:
                            if fourth_letter not in yellow4:
                                if (len(green4) != 1 and len(green3) == 1 and len(green2) == 1 and len(green1) == 1):
                                    print(end = '\n\n')
                                    print_counter = 0
                                for fifth_letter in green5:
                                    if fifth_letter not in yellow5:
                                        if (len(green5) != 1 and len(green4) == 1 and len(green3) == 1 and len(green2) == 1 and len(green1) == 1):
                                            print(end = '\n\n')
                                            print_counter = 0
                                        word = first_letter + second_letter + third_letter + fourth_letter + fifth_letter
                                        valid = True
                                        for letter in include:
                                            if letter not in word:
                                                valid = False
                                        if valid == True:
                                            # rules
                                            if (
                                                not(
                                                    first_letter == second_letter == third_letter or
                                                    second_letter == third_letter == fourth_letter or
                                                    third_letter == fourth_letter == fifth_letter
                                                )
                                            and ('XS' not in word)
                                            and (fifth_letter not in ['V','J'])
                                            and not('Q' in word and 'QU' not in word)):
                                                print_counter += 1
                                                print (word, end = ' ')
                                                if print_counter == words_per_line:
                                                    print_counter = 0
                                                    print()
#endregion
