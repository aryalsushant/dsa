"""
takes in a string as and returns the length of the longest substring without a repeating character


"""
def length_of_longest_substring(s):
    #initialize a set to track characters
    seen = set()

    #initialize left and max length to 0
    left = 0
    max_length = 0

    #for each character at position right
    for right in range(len(s)):

        #when character is in the set, then
        while s[right] in seen:

            #remove s[left] from set
            seen.remove(s[left])

            #move left foreward
            left+=1

        #otherwise
        #add s[right] to set
        seen.add(s[right])

        # update max length
        if len(seen) >1:
            max_length = max(max_length, right- left + 1)
    return max_length

#test cases
s = "abcdeefghhhhh"
count = length_of_longest_substring(s)
print(count)

s2 = "aaaaaaaaaaaaaaa"
count = length_of_longest_substring(s2)
print(count)