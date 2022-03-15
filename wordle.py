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

# letters to avoid, that are not part of the word
avoid = ['S','E','I','B','T','V','D']
# letters to include, that ARE part of the word
include = ['R','A','L']

for i in range(65, 91):
    # generate the entire ALPHabet (of uppercase letters)
    if (chr(i) not in avoid):
        alph.append(chr(i))
first = second[:] = third[:] = fourth[:] = fifth[:] = alph[:]

# remove letters on specific spots
firstR = ['L','A']
secondR = ['']
thirdR = ['R','A']
fourthR = ['']
fifthR = ['']

# set letters that have been found in the right spot
#first = ['']
#second = ['']
#third = ['']
fourth = ['A']
#fifth = ['']

# check that input data is correct
exclude = [firstR[0], secondR[0], thirdR[0], fourthR[0], fifthR[0]]

for letter in include:
    if letter in avoid:
        print ('Cannot avoid and include the same letter: ', letter)
        print ('Please remove', letter, 'from either the include or exclude list')
        raise SystemExit(0)

for f in first:
    print(end = '\n\n')
    if f not in firstR:
        for s in second:
            if s not in secondR:
                for t in third:
                    if t not in thirdR:
                        for fo in fourth:
                            if fo not in fourthR:
                                for fi in fifth:
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
