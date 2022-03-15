# wordle
Python assist for playing Wordle

How to use:
  
- Start with a word, ideally "SERAI" as it _should_ yield the most info
- Add BLACK LETTERS to the "black_letters" array
- Add YELLOW LETTERS to each "yellow" array they were found in (1, 2, etc.)
- Add GREEN LETTERS to each "green" array in the spot they were found in (1, 2, etc.); don't forget to uncomment the arays where leters were added

Running:
- ALL arrays take **single UPPERCASE letters** as elements
- Run and try to find your word; the more info you have the less results will have to be parsed
- You can modify the "wpl" var to print a different number of words per line (for readability)

Rules:  
- No consecutive 3 letters
- No "XS" group of letters
- No word ending in "V" or "J"
- When in the word, "Q" has to be preceeded by a "U"
