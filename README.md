# wordle
Python assist for playing Wordle

How to use:

- Start with a word, ideally "SERAI" as it _should_ yield the most info
- Populate the "avoid" array with letters that are not part of the word
- Populate the "include" array with letters that are part of the word
- Add letters to the arrays ending in R to skip words that have letters in those positions
- Uncomment and add the letter found in each spot

- Run and try to find your word; the more info you have the less results will have to be parsed
- You can modify the "wpl" var to print a different number of words per line (for readability)

Rules:
- No consecutive 3 letters
- No "XS" group of letters
- No word ending in "V" or "J"
- When in the word, "Q" has to be preceeded by a "U"
