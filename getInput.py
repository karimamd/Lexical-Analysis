
# Lexical Rules Input File Format
# • Lexical rules input file is a text file.
# • Regular definitions are lines in the form LHS = RHS
# • Regular expressions are lines in the form LHS: RHS
# • Keywords are enclosed by { } in separate lines.
# • Punctuations are enclosed by [ ] in separate lines
# • \L represents Lambda symbol.
# • The following symbols are used in regular definitions and regular expressions with the
# meaning discussed in class: - | + * ( )
# • Any reserved symbol needed to be used within the language, is preceded by an
# escape backslash character.


# Input file example for the above lexical rules:
# letter = a-z | A-Z
# digit = 0 - 9
# id: letter (letter|digit)*
# digits = digit+
# {boolean int float}
# num: digit+ | digit+ . digits ( \L | E digits)
# relop: \=\= | !\= | > | >\= | < | <\=
# assign: =
# { if else while }
# [; , \( \) { }]
# addop: \+ | -
# mulop: \* | /


# from this file we need
# 1. save regex and definitions
# 2. extract keywords , reserved symbols , punctuation sybmols
# 3. given a character/string return if it satisfies a definition or not


def readInput():





# now we have the regex