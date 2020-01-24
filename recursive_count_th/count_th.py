'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

check index 0 and 1
if == "th" return 1 else return 0
check index 1 and 2
...

'''
def count_th(word):
    
    # TBC
    if len(word) < 2:
        return 0
    else:
        n = 0
        if word[0:2] == "th":
            n=1
        new_word = word[1:]
        return n+count_th(new_word)
    pass
