# 2022 Alin-Gabriel Drăghici <guky667@gmail.com>  #
# # # # # # # # # # # # # # # # # # # # # # # # # #

# region Vars and inits
# SERAI _should_ be the best starting word

words_per_line = 24
print_counter = 0
all_letters = []
pivot_letter = ''
pivot_point = 0
#endregion

### BLACK LETTERS - all inline
black_letters = 'SERIKTBD'

### YELLOW LETTERS - per positions
yellow1 = 'L'
yellow2 = ''
yellow3 = 'LMA'
yellow4 = 'A'
yellow5 = ''

### GREEN LETTERS - per positions
green1 = 'M'
green2 = 'A'
green3 = ''
green4 = 'L'
green5 = 'Y'

#region Execution
# generate the entire alphabet (of uppercase letters) and base lists of letter combinations 
all_letters = [chr(char) for char in range(65,91) if chr(char) not in ''.join(set(black_letters))]

if green1 == '': green1 = [first_letter for first_letter in all_letters if first_letter not in yellow1]
if green2 == '': green2 = [second_letter for second_letter in all_letters if second_letter not in yellow2]
if green3 == '': green3 = [third_letter for third_letter in all_letters if third_letter not in yellow3]
if green4 == '': green4 = [fourth_letter for fourth_letter in all_letters if fourth_letter not in yellow4]
if green5 == '': green5 = [fifth_letter for fifth_letter in all_letters if fifth_letter not in yellow5 and fifth_letter not in 'VJ']
# create list of letters to include based on Yellow Letters
include = ''.join(set(yellow1 + yellow2 + yellow3 + yellow4 + yellow5))


# Bad input check
for yellow_letter in include:
    if yellow_letter in black_letters:
        print ('Cannot include and exclude letter',yellow_letter,'. Please remove from either black_letters or yellow letters')
        raise SystemExit(0)

# Generating a list of words
words = [
    first_letter + second_letter + third_letter + fourth_letter + fifth_letter

    for first_letter in green1 
    for second_letter in green2
    for third_letter in green3 
    for fourth_letter in green4
    for fifth_letter in green5

    if(
        not (
            first_letter == second_letter == third_letter or
            second_letter == third_letter == fourth_letter or
            third_letter == fourth_letter == fifth_letter
        )
    )]

for letter in include:
    for word in words[:]:
        if (letter not in word):
            try:
                words.remove(word)
            except:
                pass

# Filtering words based on grammar rules
words = [word for word in words 
            if(# Grammar rules
                'XS' not in word and
                not('Q' in word and 'QU' not in word)
            )]

# Choosing a pivot point for formatting
if (len(green1) == 1 and len(green2) == 1): pivot_point = 1

# Printing the words
for word in words:
    print (word, end = ' ')
    if pivot_letter != word[pivot_point]:
        print(end = '\n\n')
        print_counter = 0
    if print_counter >= words_per_line:
        print(end = '\n')
        print_counter = 0
    pivot_letter = word[pivot_point]
    print_counter += 1
#endregion
