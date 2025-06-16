"""
you get a dictionary of candidates and their votes
and a string candidate that represents what candidate the voter wants to vote for
you add the number of votes to that candidate and return the list

look for candidate in dicrtionary
nahh this is self explanatory just read the code
"""

def cast_vote(votes, candidate):
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1
    
#test case
votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)
    
        
