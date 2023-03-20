# An avid hiker keeps meticulous records of their hikes. During the last hike that took 
# exactly "x steps" steps, for every step it was noted if it was an uphill,U, or a downhill,D step. 
# Hikes always start and end at sea level, and each step up or down represents a 1 unit change 
# in altitude. 

# We define the following terms:

# A mountain is a sequence of consecutive steps above sea level, starting with a step up 
# from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down 
# from sea level and ending with a step up to sea level.
# Given the sequence of up and down steps during a hike, find and print the number of 
# valleys walked through.

# Example

# step = 8 path = DDUUUUDD 

# The hiker first enters a valley 2 units deep. Then they climb out and up onto a mountain 2
# units high. Finally, the hiker returns to sea level and ends the hike.

# Function Description

# Complete the countingValleys function in the editor below.

# countingValleys has the following parameter(s):

# int steps: the number of steps on the hike
# string path: a string describing the path

# Returns

# int: the number of valleys traversed
# Input Format

# The first line contains an integer , the number of steps in the hike.
# The second line contains a single string , of  characters that describe the path.


from test28 import steps,path

def countingValleys(steps, path):

    trs = {"U":1,"D":-1}
    valley, segment, type_segment = 0, 0, 0
    
    for step in path:
        
        if segment == 0:
            type_segment = trs[step]
             
        segment = segment+trs[step]

        if segment == 0: 
            if type_segment == -1:
                valley += 1
            segment = 0   
    
    return valley 


print(countingValleys(8,"UDDDUDUUUDDDUUDDUU") ) 
print(countingValleys(steps,path))   