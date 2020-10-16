def append_list_to_number(numbers, a, space): 
    i = 0
    while i < a:
        print "At the top i is %d" % i 
        numbers.append(i)

        i = i + space
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i 

    return numbers


numbers = []

print "The numbers: " 

for num in numbers: 
    print num

numbers = append_list_to_number(numbers, 10, 2)

print "The numbers: " 

for num in numbers: 
    print num
