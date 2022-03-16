# wordle
Python assist for playing Wordle

How to use:
  
- Start with a word, ideally "SERAI" as it _should_ yield the most info (as per: https://towardsdatascience.com/a-frequency-analysis-on-wordle-9c5778283363)
- Add BLACK LETTERS to the "black_letters" string
- Add YELLOW LETTERS to each "yellow" string in the spot they were found in (1, 2, etc.)
- Add GREEN LETTERS to each "green" string in the spot they were found in (1, 2, etc.)

Running:
- ALL strings take **UPPERCASE letters** as elements
- Run and try to find a word; the more info you have the less results will have to be parsed
- You can modify the "words_per_line" var to print a different number of words per line (for readability)

Rules:  
- No word ending in "V" or "J"
- No groups of: KK, QQ, UU, YY or HH
- No consecutive 3 letters
- When in the word, "Q" has to be preceeded by a "U"
- No groups of letters: BQ, CJ, CV, FZ, GQ, JQ, JV, JX, KQ, PQ, XZ, QB, JC, VC, ZF, QG, QJ, VJ, XJ, QK, QP, ZX, VP or XS
