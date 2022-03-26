Python assist for playing Wordle

How to use:

- Start with a word, ideally "SERAI" as it _should_ yield the most info (as per: https://towardsdatascience.com/a-frequency-analysis-on-wordle-9c5778283363)
- Add BLACK LETTERS to the "black_letters" string
- Add YELLOW LETTERS to each "yellow" string in the spot they were found in (1, 2, etc.) - OR black letters that are already part of the word but not doubled
- Add GREEN LETTERS to each "green" string in the spot they were found in

Examples for green letters:
X in the 2nd position: green = '-X---'
B in the 1st and 4th position: green ='B--B-'

Running:
- ALL strings take **UPPERCASE letters** as elements
- Run and try to find a word; the more info you have the less results will have to be parsed
- You can modify the "words_per_line" var to print a different number of words per line (for readability)

Rules:  
- No word ending in "J", "V" or "Q"
- No consecutive 3 letters
- When in the word, "Q" has to be followed by a "U"
- No groups of letters: 'KK', 'QQ', 'UU', 'YY', 'HH', 'WW', 'BQ', 'CJ', 'CV', 'FZ', 'GQ', 'VJ', 'JV', 'JX', 'KQ', 'PQ', 'XZ', 'QB','JC', 'VC', 'ZF', 'QG', 'QJ', 'JQ', 'XJ', 'QK', 'QP', 'ZX', 'VP' or 'XS'
