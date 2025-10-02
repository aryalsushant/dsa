"""
As part of the festival, attendees cast votes for their favorite set. Given a dictionary votes that maps attendees 
id numbers to the artist they voted for, return the artist that had the highest number of votes. If there is a tie, 
return any artist with the top number of votes.
"""
def best_set(votes):
    f_map = {}
    for key, value in votes.items():
        if value not in f_map:
            f_map[value]=1
        else:
            f_map[value]+=1
    max_vote = 0
    max_artist = None
    for artist, vots in f_map.items():
        if vots > max_vote:
            max_vote = vots
            max_artist = artist
    return max_artist

#test case
votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))


