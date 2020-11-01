import re

def scan(sentence):
    words = sentence.split(' ')
     
    direction = ['north', 'south', 'east', 'west']
    verbs = ['kill', 'go', 'eat']
    stop = ['in', 'the', 'of']
    noun = ['bear', 'princess']
    stuff = [] 
    for i in words:
        if i in direction:
            stuff.append(('direction', i))
        elif i in verbs:
            stuff.append(('verb', i))
        elif i in stop:
            stuff.append(('stop', i))
        elif i in noun:
            stuff.append(('noun', i))
        elif re.search('\d+', i):
            stuff.append(('number', int(i)))
        else:
            stuff.append(('error', i))
    print(stuff)
    return stuff
                

    
