# 2022 Alin-Gabriel Drăghici <guky667@gmail.com>  #
# # # # # # # # # # # # # # # # # # # # # # # # # #

# SERAI _should_ be the best starting word

wpl = 30
counter = 0
first = []
second = []
third = []
fourth = []
fifth = []
alph = []

# letters to avoid, that are not part of the word
avoid = ['S','R','I','C']
# letters to include, that ARE part of the word
include = ['']

for i in range(65, 91):
    if (chr(i) not in avoid):
        alph.append(chr(i))
first = second[:] = third[:] = fourth[:] = fifth[:] = alph[:]

# remove letters on specific spots
firstR = ['']
secondR = ['']
thirdR = ['']
fourthR = ['']
fifthR = ['']

# set letters that have been found in the right spot
#first = ['']
second = ['H']
third = ['E']
fourth = ['A']
fifth = ['T']

for f in first:
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
                                        for letter in include:
                                            if letter in word:
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