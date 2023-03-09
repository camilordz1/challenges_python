# Create a function that takes a decimal number representation 
# of a signal and returns the analog voltage level that would 
# be created by a DAC if it were given the same number in binary.
#
# Reference: https://edabit.com/challenge/AJGqpNL2yAyhbdpvB

def V_DAC(value):
    return round(value*5/1023,2)

if __name__ == "__main__":
    print(V_DAC(400))