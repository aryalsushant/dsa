"""
Given a string s, determine if it can become a palindrome by removing at most one character.

A palindrome is a word, phrase, or sequence that reads the same backward as forward.
"""

def valid_palindrome(s):
    left = 0
    right = len(s) - 1
    deletion = False

    while left < right:

        if s[left]==s[right]:
            left+=1
            right-=1
        elif not deletion:
            deletion = True
            #i'll do it later


