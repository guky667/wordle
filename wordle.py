# 2022 Alin-Gabriel Drăghici <guky667@gmail.com>  #
# # # # # # # # # # # # # # # # # # # # # # # # # #

# region Vars and inits
# SERAI _should_ be the best starting word

wpl = 20 # Words Per Line
counter = 0
first = []
second = []
third = []
fourth = []
fifth = []
alph = []
#endregion

### BLACK LETTERS 
# letters to avoid, that are not part of the word
avoid = ['R','A','I','N','D']

# generate the entire ALPHabet (of uppercase letters)
for i in range(65, 91):
    if (chr(i) not in avoid):
        alph.append(chr(i))
first = second[:] = third[:] = fourth[:] = fifth[:] = alph[:]

### YELLOW LETTERS
# remove letters on specific spots
firstR = ['']
secondR = ['E','P']
thirdR = ['']
fourthR = ['']
fifthR = ['']

### GREEN LETTERS
# set letters that have been found in the right spot - uncomment and add letter
first = ['S']
#second = ['']
third = ['E']
#fourth = ['']
#fifth = ['']

#region Execution
# create list of letters to include based on Yellow Letters
include = list(dict.fromkeys(','.join(filter(None,[*firstR, *secondR, *thirdR, *fourthR, *fifthR])).split(',')))

# check that input data is correct
exclude = [firstR[0], secondR[0], thirdR[0], fourthR[0], fifthR[0]]

for letter in include:
    if letter in avoid:
        print ('Cannot avoid and include the same letter: ', letter)
        print ('Please remove', letter, 'from either the include or exclude list')
        raise SystemExit(0)

counter = 0

for f in first:
    if (len(first) != 1):
        print(end = '\n\n')
        counter = 0
    if f not in firstR:
        for s in second:
            if (len(first) == 1):
                print(end = '\n\n')
                counter = 0
            if s not in secondR:
                for t in third:
                    if (len(second) == 1 and len(first) == 1):
                        print(end = '\n\n')
                        counter = 0
                    if t not in thirdR:
                        for fo in fourth:
                            if (len(third) == 1 and len(second) == 1 and len(first) == 1):
                                print(end = '\n\n')
                                counter = 0
                            if fo not in fourthR:
                                for fi in fifth:
                                    if (len(fourth) == 1 and len(third) == 1 and len(second) == 1 and len(first) == 1):
                                        print(end = '\n\n')
                                        counter = 0
                                    if fi not in fifthR:
                                        word = f + s + t + fo + fi
                                        valid = True
                                        for letter in include:
                                            if letter not in word:
                                                valid = False
                                        if valid == True:
                                            # rules
                                            if (
                                                not(f==s==t or s==t==fo or t==fo==fi)
                                                and ('XS' not in word)
                                                and (fi!='V' and fi!='J')
                                                and not('Q' in word and 'QU' not in word)
                                            ):
                                                counter += 1
                                                print (word, end = ' ')
                                                if counter == wpl:
                                                    counter = 0
                                                    print()
#endregion
