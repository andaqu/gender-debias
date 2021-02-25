# simple function to convert maltese letters to english equivalents.
def maltese_to_english(s):
    s = s.replace('à', 'a')
    s = s.replace('ċ', 'c')
    s = s.replace('ħ', 'h')
    s = s.replace('ћ', 'h')
    s = s.replace('ġ', 'g')
    s = s.replace('ż', 'z')
    s = s.replace('Ċ', 'C')
    s = s.replace('Ħ', 'H')
    s = s.replace('Ġ', 'G')
    s = s.replace('Ż', 'Z')

    return s