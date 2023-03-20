def marsExploration(s):
    messages = int(len(s)/3)
    count = 0
    s = list(s) 
    for index in range(messages):
        msg = s[3*index:3*index+3]
        if msg[0] != "S": 
            count +=1
        if msg[1] != "O":
            count +=1
        if msg[2] != "S":
            count +=1    
    return(count)

print(marsExploration("AAAAAAAAA"))        