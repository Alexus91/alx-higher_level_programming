#!/usr/bin/python3
def remove_char_at(str, n):
    """print copy of the string,removing the character at the position n"""
    if n < 0:
        return(str)
    x = str[0:n] + str[n+1:]
    return (x)
