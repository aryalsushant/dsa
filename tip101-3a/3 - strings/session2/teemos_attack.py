"""
In the game League of Legends, Teemo attacks his enemy Ashe with poison arrows. Write a function find_poisoned_duration() 
that takes in two parameters: time_series (the time at which Teemo's attacks hits Ashe) and time_duration (the duration of
 the poisoning effect). The function returns the total time that Ashe is in a poisoned condition.

time_series is a list of integers that represents the times at which Teemo attacks and makes Ashe poisoned 
for the exact 
time_duration.

If Teemo hits Ashe while she is still poisoned, the poison's duration starts over. For example,
 if Teemo attacks at times 
1 and 4 for 3 seconds, the states at each time would be:

1. loop through range
2. for each range, add the minimum between the duration or the gap between this range and next range
3. at the end of the loop, add total duration of the last range
"""
def find_poisoned_duration(time_series, duration):
    total = 0
    for i in range(len(time_series)-1):
        gap = time_series[i+1]-time_series[i]
        total += min(gap, duration)
    total += duration
    return total

#test case
time_series = [1,4,9]
damage = find_poisoned_duration(time_series, 3)
print(damage)

       